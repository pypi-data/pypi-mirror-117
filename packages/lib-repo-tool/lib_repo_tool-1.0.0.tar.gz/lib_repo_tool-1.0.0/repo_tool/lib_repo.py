import json
import os
import argparse
import shutil
from dataclasses import dataclass, asdict
from typing import Optional

from .common import is_legal_local_lib_dir
from . import common
from dacite import from_dict

import logging
logger = logging.getLogger(__name__)


@dataclass
class LibData:
    name: str
    version: Optional[str]
    platform: Optional[str]
    arch: Optional[str]
    build: Optional[str]

    @classmethod
    def from_dict(cls, data) -> "LibData":
        return from_dict(LibData, data)

    def to_dict(self):
        return asdict(self)

    def file_key(self):
        if not self.name:
            raise Exception(f'invalid lib data: {self}')
        file_key = os.path.join(common.OSS_BASE_PATH, self.gen_path())
        file_key = os.path.join(file_key, self.get_zip_file_name())

        file_key = file_key.replace('\\', '/')

        return file_key

    def gen_path(self):
        p = self.name
        if self.version:
            p = os.path.join(p, self.version)
        if self.platform:
            p = os.path.join(p, self.platform)
        if self.arch:
            p = os.path.join(p, self.arch)
        if self.build:
            p = os.path.join(p, self.build)

        return p

    def get_zip_file_name(self):
        return self.name + "_lib.zip"


class LibRepo:
    def __init__(self):
        self.libs: Optional[list[LibData]] = None
        self.__repo_file_key = os.path.join(common.OSS_BASE_PATH, 'repo.json')
        self.__repo_file_key = self.__repo_file_key.replace('\\', '/')
    def pull_repo(self) -> "LibRepo":
        content = common.get_file_obj_2_str(self.__repo_file_key)
        if not content:
            return self

        libs_data = json.loads(content)
        self.libs = [LibData.from_dict(lib) for lib in libs_data]

        return self

    def push_repo(self) -> "LibRepo":
        if not self.libs:
            return self

        libs = [lib.to_dict() for lib in self.libs]
        common.upload_file_obj(self.__repo_file_key, json.dumps(libs))

        return self

    def add_new_lib(self, lib: LibData):
        if not self.libs:
            self.libs = []
        if self.exist(lib):
            raise Exception('already exist')
        self.libs.append(lib)

    def exist(self, lib: LibData):
        if not self.libs:
            return False

        return any(lb == lib for lb in self.libs)


def update_lib(local_path: str, lib: LibData):
    if not os.path.exists(local_path):
        logger.error(f'Lib path not exit: {local_path}')
        raise Exception('lib path not exist!')

    zip_file_name = lib.get_zip_file_name()
    zip_file_path = os.path.join(local_path, zip_file_name)
    common.zip_dir(local_path, zip_file_path)

    file_key = lib.file_key()
    common.upload_file(zip_file_path, file_key)
    os.remove(zip_file_path)

    repo = LibRepo()
    repo.pull_repo()
    if not repo.exist(lib):
        repo.add_new_lib(lib)
        repo.push_repo()


def parse_args():
    description = "Upload your lib to cloud"
    parser = argparse.ArgumentParser(description=description)
    sub_parsers = parser.add_subparsers(dest='sub_command')
    add_parser = sub_parsers.add_parser('add')
    add_parser.add_argument('--path', help='The library folder you want to upload.')
    add_parser.add_argument('--name', help='The library name.')
    add_parser.add_argument('--version', help='The library version.')
    add_parser.add_argument('--platform', help='Platform the library running.', choices=common.available_platforms())
    add_parser.add_argument('--arch', help='The library architecture.', choices=common.all_available_arches())
    add_parser.add_argument('--build', help='The library build type.', choices=common.available_build_names())

    remove_parser = sub_parsers.add_parser('remove')
    remove_parser.add_argument('--name')

    return parser.parse_args()


def lib_repo():
    args = parse_args()

    if args.sub_command != 'add':
        exit(1)

    if not args.path:
        while True:
            path = input("Input the lib local path you want to upload: ")
            if path:
                args.path = path
                break
    if not args.name:
        while True:
            name = input("Input the lib name you want to upload: ")
            if name:
                args.name = name.strip()
                break
    if not args.platform:
        platform = input("Input the platform for the lib you want to upload: ")
        args.platform = platform
    if not args.arch:
        arch = input("Input the architecture for the lib you want to upload: ")
        args.arch = arch
    if not args.build:
        build = input("Input the build type for the lib you want to upload: ")
        args.build = build

    def strip(s):
        return s.strip() if s else None

    lib_data = LibData(name=args.name, version=strip(args.version),
                       platform=strip(args.platform),
                       arch=strip(args.arch),
                       build=strip(args.build))

    lib_repo = LibRepo().pull_repo()
    upload = True
    if lib_repo.exist(lib_data):
        while True:
            override = input("The lib you want to upload has existed in repo. Do you want to override that? yes/no")
            if override == 'yes':
                upload = True
                break
            elif override == 'no':
                upload = False
                break
            else:
                logger.info("Please input yes or no")

    if upload:
        update_lib(args.path, lib_data)


if __name__ == "__main__":
    lib_repo()


