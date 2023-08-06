import subprocess

import click
from typing import List

from loguru import logger

from pbt.config import PBTConfig
from pbt.lock import PBTLock, PkgIdent
from pbt.package import search_packages
from pbt.pypi import PyPI


@click.group()
def cli():
    pass


@click.command()
@click.option(
    "-p",
    "--package",
    multiple=True,
    help="Specify the active package that we are working on. If empty, use all packages",
)
@click.option("--cwd", default="", help="Override current working directory")
def make(package: List[str], cwd: str = ""):
    pbt_cfg = PBTConfig.from_dir(cwd)
    pbt_dat = PBTLock.from_dir(pbt_cfg.cwd)

    active_packages = package
    packages = search_packages(pbt_cfg)
    if len(active_packages) == 0:
        active_packages = packages.keys()
    active_packages = set(active_packages)
    if len(active_packages.difference(packages.keys())) > 0:
        raise Exception(
            f"Passing unknown packages: {active_packages.difference(packages.keys())}. Available options: {list(packages.keys())}"
        )

    pkg2ident = {}
    for pkg in packages.values():
        pkg_hash = pbt_dat.get_hash(pkg)
        current_pkg_hash = pkg.compute_pip_hash(pbt_cfg)
        if pkg_hash != current_pkg_hash:
            if pkg_hash is None:
                pkg_hash = current_pkg_hash
                pbt_dat.update_pkg_version(pkg, pkg_hash)
            else:
                logger.warning(
                    "Package {} is modified but its version has not been updated",
                    pkg.name,
                )
                pkg_hash = current_pkg_hash
                pbt_dat.update_pkg_version(pkg, pkg_hash)

        # make sure that other packages use the same version
        for pp in pkg.invert_inter_dependencies:
            pp.update_package_version(pkg)

        pkg2ident[pkg.name] = PkgIdent(pkg.version, pkg_hash)

    for pkg_name in active_packages:
        logger.info("Process package {}", pkg_name)
        pkg = packages[pkg_name]
        for dep_pkg in pkg.inter_dependencies:
            dep_pkg_ident = pbt_dat.get_pkg_dependency_ident(pkg, dep_pkg)
            if dep_pkg_ident != pkg2ident[dep_pkg.name]:
                logger.info("\t+ Update package {}", dep_pkg.name)
                dep_pkg.install_into(pkg, pbt_cfg, build=False)
                pbt_dat.update_pkg_dependency(pkg, dep_pkg, pkg2ident[dep_pkg.name])
            else:
                logger.info("\t+ Skip package {}", dep_pkg.name)

    pbt_dat.save(pbt_cfg.cwd)


@click.command()
@click.option("--cwd", default="", help="Override current working directory")
def publish(cwd: str = ""):
    pbt_cfg = PBTConfig.from_dir(cwd)
    packages = search_packages(pbt_cfg)
    for package in packages.values():
        if PyPI.get_instance().does_package_exist(package.name, package.version):
            logger.info("Skip publishing package {} as it exists", package.name)
            continue
        logger.info("Publish package {}", package.name)
        package.build(pbt_cfg)
        for pp in package.invert_inter_dependencies:
            pp.update_package_version(package)
        subprocess.check_call(["poetry", "publish"], cwd=str(package.dir))


cli.add_command(make)
cli.add_command(publish)


if __name__ == "__main__":
    cli()
