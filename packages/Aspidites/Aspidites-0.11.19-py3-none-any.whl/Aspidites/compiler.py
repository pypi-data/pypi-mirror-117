
# Aspidites
# Copyright (C) 2021 Ross J. Duff

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import os
import py_compile
import sys
from glob import glob
from warnings import warn
import typing as t
from mypy import api
from .templates import lib, makefile, pyproject, setup
from pyrsistent import pmap
from hashlib import sha256
from pathlib import Path
from .final import final
from ._vendor.semantic_version import Version
from pyparsing import ParseResults


@final()
class CheckedFileStack:

    """A convenience class for reading file data streams to stdout or to checksum"""

    def __init__(self, initial=None, pre_size=128):
        if initial is None:
            initial = {}
        self._files = pmap(initial, pre_size)
        self.all_files = self._files.evolver()
        self.pre_size = pre_size

    def read(self, data, print__=False, hash_func=None):
        curr_hash = hash_func() if hash_func else {}
        chunk = data.read(self.pre_size)
        while chunk:
            curr_hash.update(chunk) if hash_func else {}
            chunk = data.read(self.pre_size)
            if print__:
                print(chunk, '')
        return curr_hash if hash_func else None

    def __checksum(self, fname, write=True, check=False):
        fname = Path(fname)
        base, name = fname.parent, fname.name
        base = Path(base)
        fname_sha256 = base/("." + name + ".sha256")

        if write:
            with open(fname, "rb") as data:
                curr_hash = self.read(data, hash_func=sha256)
                with open(fname_sha256, "wb") as digest:
                    digest.write(curr_hash.digest())
                return pmap({curr_hash.digest(): fname}).items()[0]  # immutable
        if check:
            with open(fname_sha256, "rb") as digest:
                with open(fname, "rb") as data:
                    curr_hash = self.read(data, hash_func=sha256)
                    old = digest.read()
                    new = curr_hash.digest()
                    if new == old:
                        print(
                            "sha256 digest check successful: %s, %s == %s"
                            % (fname, new.hex(), old.hex())
                        )
                        return new
                    else:
                        print(
                            "sha256 digest failure: %s, %s != %s"
                            % (fname, new.hex(), old.hex())
                        )
                        return ""

    def register(self, fname):
        self.all_files.set(*self.__checksum(fname))

    def commit(self):
        return self.all_files.persistent()

    def create_file(self, fname, mode, root='',
                    text="# THIS FILE IS GENERATED - DO NOT EDIT #") -> None:

        if len(str(root)) > 0:
            root = Path(root)
            file = root/fname
        else:
            file = fname
        try:
            open(file, mode).write(text)
        except FileExistsError:
            self.register(file)

    def finalize(self):
        all_file_checksums = self.commit()
        print("running checksums")
        for k, v in all_file_checksums.items():
            digest = self.__checksum(v, write=False, check=True)
            try:
                all_file_checksums.get(digest)
            except AttributeError:
                raise RuntimeError("\nfor file %s\n%s\n  did not match cached digest\n%s")


file_stack = CheckedFileStack()


def compile_module(**kwargs):
    code          : ParseResults         = kwargs['code']
    fname         : Path                 = kwargs['fname']
    force         : bool                 = kwargs['force']
    bytecode      : bool                 = kwargs['bytecode']
    c             : bool                 = kwargs['c']
    build_requires: t.Union[t.List, str] = kwargs['build_requires']
    verbose       : int                  = kwargs['verbose']

    fname = Path(fname)
    app_name = fname.parent / fname.stem
    project = app_name.stem
    module_name = str(app_name).replace("/", ".")
    file_c = str(app_name) + ".c"
    root = fname.parent
    mode = "x" if force else "w"

    files = {
        fname           : (mode, {'root': '', 'text': lib.substitute(code="\n".join(code))}),
        '__init__.py'   : (mode, {'root': root}),
        'py.typed'      : (mode, {'root': root}),
        'pyproject.toml': (mode,
            {'root': root, 'text': pyproject.substitute(build_requires=build_requires)}
                           ),
        'Makefile'      : (mode, {'root': root, 'text': makefile.substitute(project=project)}),
    }

    for k, v in files.items():
        args_, kwargs_ = v
        file_stack.create_file(k, args_, **kwargs_)

    typecheck(module_name)
    create_stubs(fname, app_name)

    if bytecode:
        fname_pyc = str(app_name) + ".pyc"
        quiet = tuple(reversed(range(3))).index(verbose if verbose < 2 else 2)
        major, minor, patch, *_ = sys.version_info
        if Version(major=major, minor=minor, patch=patch) < Version('3.8.0'):
            py_compile.compile(str(fname), fname_pyc)
        else:
            py_compile.compile(str(fname), fname_pyc, quiet=quiet)
        file_stack.register(fname_pyc)

    if c:
        compile_c(fname, force, verbose)
        create_setup(root, app_name, **kwargs)
        compile_object(str(app_name), file_c, root)

    file_stack.finalize()


def typecheck(module_name: str):
    mypy_args = [
        "-m",
        module_name,
        "--follow-imports=skip",
        "--show-error-context",
        "--show-error-codes",
        "--allow-incomplete-defs",
        "--disable-error-code=valid-type",
        "--exclude=builtins"
        # '--disallow-untyped-defs',
        # '--disallow-untyped-calls',
    ]
    print("running mypy", " ".join(mypy_args))
    type_report = None
    error_report = None
    return_code = 0
    try:
        type_report, error_report, return_code = api.run(mypy_args)
    except AttributeError:
        warn("mypy api call failed")

    finally:
        print("mypy type report: ", type_report) if type_report else None
        print("mypy error report: ", error_report) if error_report else None
        print("mypy returned with exit code:", return_code) if return_code else None
        # exit(return_code) if return_code != 0 else print("running compile")


def create_stubs(fname, app_name):
    fname_pyi = str(app_name) + '.pyi'
    stubgen = 'stubgen %s -o .' % fname
    print("running %s" % stubgen)
    with os.popen(stubgen) as p:
        file_stack.read(p, print__=True)
    try:
        file_stack.register(fname_pyi)
    except FileNotFoundError as e:
        warn(str(e))
        try:
            cwd = Path.cwd()
            path = cwd / Path('__main__.py')
            print("trying rename %s/__main__.pyi to %s" % (str(cwd), fname_pyi))
            path.rename(fname_pyi)
            file_stack.register(fname_pyi)
        except FileNotFoundError:
            warn("failed to create stubs")


def compile_c(fname, force, verbose) -> None:
    verb = int(bool(verbose))
    os.popen("cython %s %s %s" % (fname, "--force" * force, "--verbose" * verb))


def create_setup(root, app_name, **kwargs) -> None:
    module_name = str(app_name).replace("/", ".")
    file_stack.create_file('setup.py',
                "x" if kwargs['force'] else "w",
                root=root,
                text=setup.substitute(
                    app_name=module_name,
                    src_file=kwargs['fname'],
                    inc_dirs=[],
                    libs=[],
                    exe_name=app_name,
                    lib_dirs=[],
                    **kwargs))


def compile_object(app_name, file_c, root) -> None:
    glob_so = app_name + ".*.so"
    # TODO: get this working for docker builds
    #  (maybe executable param with os.path.relpath?)
    setup_runner = "%s %s build_ext -b ." % (sys.executable, str(Path(root)/'setup.py'))
    print("running", setup_runner)
    with os.popen(setup_runner) as p:
        file_stack.read(p, print__=True)
    file_stack.register(file_c)
    for i in glob(glob_so):
        file_stack.register(i)
