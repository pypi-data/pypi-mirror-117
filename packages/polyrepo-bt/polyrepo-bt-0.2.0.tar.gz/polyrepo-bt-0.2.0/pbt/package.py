import os
import shutil
import subprocess
from dataclasses import dataclass
from enum import Enum
from glob import glob
from graphlib import TopologicalSorter
from pathlib import Path
from typing import Dict, Optional, Union, List

import orjson
import toml
from loguru import logger

from pbt.config import PBTConfig
from pbt.diff import is_modified
from pbt.git import Git
from pbt.poetry import Poetry


class PackageType(str, Enum):
    Poetry = "poetry"


@dataclass
class Package:
    name: str
    type: PackageType
    dir: Path
    version: str
    dependencies: Dict[str, str]
    # list of packages that this package uses
    inter_dependencies: List["Package"]
    # list of packages that use the current package
    invert_inter_dependencies: List["Package"]

    def build(self, cfg: PBTConfig):
        """Build the package if needed"""
        # check if package has been modified since the last built
        whl_file = self.get_wheel_file()
        if whl_file is not None:
            if not self.is_modified(cfg):
                logger.info("Skip package {} as the content does not change", self.name)
                return

        logger.info("Build package {}", self.name)
        if (self.dir / "dist").exists():
            shutil.rmtree(str(self.dir / "dist"))
        subprocess.check_call(["poetry", "build"], cwd=str(self.dir))

    def compute_pip_hash(self, cfg: PBTConfig, build: bool = True) -> str:
        """Compute hash of the content of the package"""
        if build:
            self.build(cfg)
        output = subprocess.check_output(["pip", "hash", self.get_wheel_file()]).decode().strip()
        output = output[output.find("--hash=")+len("--hash="):]
        assert output.startswith("sha256:")
        return output[len("sha256:"):]

    def install_into(self, package: "Package", cfg: PBTConfig, build: bool = True):
        """Install the current package (self) in the virtual environment of another package (`package`)"""
        if build:
            self.build(cfg)
        logger.info(
            "Install package {} into package {} environment", self.name, package.name
        )
        pipfile = package.pkg_handler.get_pip_file(package.dir)
        subprocess.check_output([pipfile, "uninstall", "-y", self.name])
        subprocess.check_output([pipfile, "install", self.get_wheel_file()])

    def update_package_version(self, package: "Package"):
        """Update the version of another package in this package"""
        assert package.name in self.dependencies
        self.pkg_handler.update_package(self, package.name, package.version)

    def is_modified(self, cfg: PBTConfig):
        """Check if package has been modified"""
        return is_modified(self, cfg)

    @property
    def pkg_handler(self):
        if self.type == PackageType.Poetry:
            return Poetry
        raise NotImplementedError(self.type)
    
    def get_tar_file(self) -> Optional[str]:
        tar_file = self.dir / "dist" / f"{self.name}-{self.version}.tar.gz"
        if tar_file.exists():
            return str(tar_file)
        return None

    def get_wheel_file(self) -> Optional[str]:
        whl_files = glob(str(self.dir / f"dist/{self.name.replace('-', '_')}*.whl"))
        if len(whl_files) == 0:
            return None
        return whl_files[0]

    def to_dict(self):
        return {
            "name": self.name,
            "type": self.type,
            "dir": self.dir,
            "version": self.version,
            "dependencies": self.dependencies,
            "inter_dependencies": [p.name for p in self.inter_dependencies],
            "invert_inter_dependencies": [
                p.name for p in self.invert_inter_dependencies
            ],
        }

    @staticmethod
    def save(packages: Dict[str, "Package"], outfile: Union[str, Path]):
        with open(str(outfile), "wb") as f:
            f.write(
                orjson.dumps(
                    {package.name: package.to_dict() for package in packages.values()}
                )
            )

    @staticmethod
    def load(infile: str) -> Dict[str, "Package"]:
        with open(infile, "r") as f:
            raw_packages = orjson.loads(f.read())
        packages = {name: Package(**o) for name, o in raw_packages}
        for package in packages:
            package.type = PackageType(package.type)
            packages.inter_dependencies = [
                packages[name] for name in package.inter_dependencies
            ]
            packages.invert_inter_dependencies = [
                packages[name] for name in package.invert_inter_dependencies
            ]
        return packages

    def __repr__(self) -> str:
        return f"{self.name}={self.version}"


def search_packages(pbt_cfg: PBTConfig):
    logger.info("Search packages...")
    packages = {}

    for poetry_file in glob(str(pbt_cfg.cwd / "*/pyproject.toml")):
        poetry_file = Path(poetry_file)
        package_dir = poetry_file.parent

        try:
            with open(poetry_file, "r") as f:
                project_cfg = toml.loads(f.read())
                package_name = project_cfg["tool"]["poetry"]["name"]
                package_version = project_cfg["tool"]["poetry"]["version"]
                package_dependencies = project_cfg["tool"]["poetry"]["dependencies"]
        except:
            logger.error("Error while parsing configuration in {}", package_dir)
            raise

        logger.info("Found package {}", package_name)
        packages[package_name] = Package(
            name=package_name,
            type=PackageType.Poetry,
            version=package_version,
            dependencies=package_dependencies,
            dir=package_dir,
            inter_dependencies=[],
            invert_inter_dependencies=[],
        )

    package_names = set(packages.keys())
    for package in packages.values():
        for pname in package_names.intersection(package.dependencies.keys()):
            package.inter_dependencies.append(packages[pname])
            packages[pname].invert_inter_dependencies.append(package)

    return packages


def topological_sort(packages: Dict[str, Package]) -> List[str]:
    """Sort the packages so that the first item is always leaf node in the dependency graph (i.e., it doesn't use any
    package in the repository.
    """
    graph = {}
    for package in packages.values():
        graph[package.name] = {child.name for child in package.inter_dependencies}
    return list(TopologicalSorter(graph).static_order())
