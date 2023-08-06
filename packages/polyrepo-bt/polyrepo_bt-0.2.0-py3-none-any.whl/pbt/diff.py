import os

import orjson
import rocksdb
from pathlib import Path
from typing import TYPE_CHECKING, List

from loguru import logger

from pbt.config import PBTConfig
from pbt.git import Git, GitFileStatus

if TYPE_CHECKING:
    from pbt.package import Package

# file size limit
SOFT_SIZE_LIMIT = (1024 ** 2) * 1  # 1MB
HARD_SIZE_LIMIT = (1024 ** 2) * 100  # 100MBs


def is_modified(pkg: "Package", cfg: PBTConfig) -> bool:
    """Detect if content of a package has been changed"""
    db = rocksdb.DB(
        str(cfg.cache_dir / f"{pkg.name}.db"), rocksdb.Options(create_if_missing=True)
    )
    is_changed = False

    commit_id = Git.get_current_commit(pkg.dir)

    # TODO: filter to keep files that only affect the content of the package (not the repository)
    changed_files = sorted(
        [file_status for file_status in Git.get_new_modified_deleted_files(pkg.dir)]
    )

    prev_commit_id = db.get(b"commit_id")
    if prev_commit_id is None:
        # we have no previous information in the system, so we have to assume it's modified
        update_db(db, commit_id, changed_files, [])
        is_changed = True
    else:
        prev_commit_id = prev_commit_id.decode()
        prev_changed_files = orjson.loads(db.get(b'changed_files'))
        prev_changed_files = [GitFileStatus(*x) for x in prev_changed_files]

        if commit_id != prev_commit_id or changed_files != prev_changed_files:
            # different commit or different file
            update_db(db, commit_id, changed_files, prev_changed_files)
            is_changed = True
        else:
            wb = rocksdb.WriteBatch()
            for file in changed_files:
                if file.is_deleted:
                    continue

                file_key = b"content:%s" % file.fpath.encode()
                prev_file_content = db.get(file_key)
                file_content = read_file(file.fpath)
                if prev_file_content != file_content:
                    wb.put(file_key, file_content)

            if wb.count() > 0:
                db.write(wb)
                is_changed = True

    del db
    return is_changed


def update_db(db: rocksdb.DB, commit_id: str, changed_files: List[GitFileStatus], prev_changed_files: List[GitFileStatus]):
    wb = rocksdb.WriteBatch()
    wb.put(b"commit_id", commit_id.encode())
    wb.put(b"changed_files", orjson.dumps([tuple(x) for x in changed_files]))

    for file in prev_changed_files:
        if file.is_deleted:
            continue
        wb.delete(b"content:%s" % file.fpath.encode())

    for file in changed_files:
        if file.is_deleted:
            continue
        wb.put(b"content:%s" % file.fpath.encode(), read_file(file.fpath))
    db.write(wb)


def read_file(fpath: str):
    fsize = os.path.getsize(fpath)
    if fsize > HARD_SIZE_LIMIT:
        raise Exception(
            f"File {fpath} is bigger than the hard limit ({format_size(fsize)} > {format_size(HARD_SIZE_LIMIT)})"
        )

    if fsize > SOFT_SIZE_LIMIT:
        logger.warning(
            "File {} is quite big ({} > {}). Consider ignore or commit it to speed up the process",
            fpath,
            format_size(fsize),
            format_size(SOFT_SIZE_LIMIT),
        )

    with open(fpath, "rb") as f:
        return f.read()


def format_size(n_bytes: int) -> str:
    if n_bytes < 1024:
        size = n_bytes
        unit = "Bs"
    elif n_bytes >= 1024 and n_bytes < (1024 ** 2):
        size = round(n_bytes / 1024, 2)
        unit = "KBs"
    elif n_bytes >= (1024 ** 2) and n_bytes < (1024 ** 3):
        size = round(n_bytes / (1024 ** 2), 2)
        unit = "MBs"
    elif n_bytes >= (1024 ** 3):
        size = round(n_bytes / (1024 ** 3), 2)
        unit = "GBs"
    return f"{size}{unit}"
