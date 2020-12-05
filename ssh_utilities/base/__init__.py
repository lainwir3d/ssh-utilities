"""Template module for all connection classes."""

from ._builtins import BuiltinsABC
from ._connection import ConnectionABC
from ._os import OsABC, OsPathABC
from ._pathlib import PathlibABC
from ._shutil import ShutilABC
from ._subprocess import SubprocessABC

from typing import TYPE_CHECKING, Iterator, Union, List, IO
from typing_extensions import Literal

if TYPE_CHECKING:
    from os import stat_result

    from paramiko.sftp_attr import SFTPAttributes
    from paramiko.sftp_file import SFTPFile
    from subprocess import CompletedProcess as sCP
    from ..utils import CompletedProcess as CP

    from pathlib import Path
    from ..typeshed import _WALK
    from ..remote.path import SSHPath
    _ATTRIBUTES = Union[SFTPAttributes, stat_result]

    # * multi types
    _BUILTINS_MULTI = BuiltinsABC[Iterator[Union[IO, SFTPFile]]]
    _OS_MULTI = OsABC[Iterator[bool], Iterator[List[str]],
                      Iterator[_ATTRIBUTES],
                      Iterator[Literal["nt", "posix", "java"]],
                      Iterator[OsPathABC], Iterator[_WALK]]
    _PATHLIB_MULTI = PathlibABC[Iterator[Union[Path, SSHPath]]]
    _SHUTIL_MULTI = ShutilABC
    _SUBPROCESS_MULTI = SubprocessABC[Iterator[Union[CP, sCP]]]

    # * remote types
    _BUILTINS_REMOTE = BuiltinsABC["SFTPFile"]
    _OS_REMOTE = OsABC[bool, List[str], "SFTPAttributes",
                       Literal["nt", "posix"], OsPathABC, "_WALK"]
    _PATHLIB_REMOTE = PathlibABC["SSHPath"]
    _SHUTIL_REMOTE = ShutilABC
    _SUBPROCESS_REMOTE = SubprocessABC[Union[CP, sCP]]

    # * local types
    _BUILTINS_LOCAL = BuiltinsABC[IO]
    _OS_LOCAL = OsABC[bool, List[str], "stat_result",
                      Literal["nt", "posix", "java"], OsPathABC, "_WALK"]
    _PATHLIB_LOCAL = PathlibABC["Path"]
    _SHUTIL_LOCAL = ShutilABC
    _SUBPROCESS_LOCAL = SubprocessABC[Union[CP, sCP]]


__all__ = ["ConnectionABC", "OsPathABC", "BuiltinsABC", "OsABC", "ShutilABC",
           "SubprocessABC", "PathlibABC"]
