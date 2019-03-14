#!/usr/bin/env python3
from enum import Enum, auto
from typing import Any, Dict, List, Tuple, TypeVar

# class stubs
Reader = TypeVar("Reader")
Directory = TypeVar("Directory")
LogGroup = TypeVar("LogGroup")

# convenience
Attrs = Dict[str, Any]

# everything here is copied from the BOOST_PYTHON_MODULE in
# ~/fbcode/logdevice/clients/python/logdevice_client.cpp
# not everything is copied, but i have attempted to be as comprehensive as possible

class LogDeviceError(Exception): ...

# client API
class Client:
    def append(self, logid: int, data: str) -> int: ...
    def create_reader(self, max_logs: int) -> Reader: ...
    def data_size(self, logid: int, start_sec: float, end_sec: float) -> int: ...
    def find_key(self, logid: int, key: str) -> Tuple[int, int]: ...
    def find_time(self, logid: int, seconds: float) -> int: ...
    def get_directory(self, path: str) -> Directory: ...
    def get_directory_delimiter(self) -> str: ...
    def get_head_attributes(self, logid: int) -> Tuple[int, int]: ...
    def get_log_group_by_id(self, id: int) -> LogGroup: ...
    def get_log_group_by_name(self, path: str) -> LogGroup: ...
    def get_log_range_by_name(self, path: str) -> Tuple[int, int]: ...
    def get_max_payload_size(self) -> int: ...
    def get_tail_attributes(self, logid: int) -> Tuple[int, int, int]: ...
    def get_tail_lsn(self, logid: int) -> int: ...
    def is_log_empty(self, logid: int) -> bool: ...
    def make_directory(
        self, path: str, mk_intermediate_dirs: bool, attrs: Attrs
    ) -> Directory: ...
    def make_log_group(
        self,
        path: str,
        start_id: int,
        end_id: int,
        attrs: Attrs,
        mk_intermediate_dirs: bool,
    ) -> LogGroup: ...
    def remove_directory(self, path: str, recursive: bool) -> None: ...
    def remove_log_group(self, path: str) -> None: ...
    def rename(self, old_path: str, new_path: str) -> None: ...
    def set_attributes(self, path: str, attrs: Attrs) -> None: ...
    def set_log_group_range(self, path: str, from_: int, to: int) -> None: ...
    def set_timeout(self, timeout: float) -> None: ...
    def smoke_test(self, log_ids: List[int], count: int) -> None: ...
    def smoke_test_read(self, starting_points: Dict[int, int], count: int) -> None: ...
    def smoke_test_write(self, logids: List[int], count: int) -> Dict[int, int]: ...
    def sync_logsconfig_version(self, version: int) -> bool: ...
    def trim(self, logid: int, lsn: int) -> None: ...

# constants
BYTE_OFFSET_INVALID: int
LOGID_INVALID: int
LOGID_MAX: int
LSN_INVALID: int
LSN_OLDEST: int
LSN_MAX: int

# time
def timestr_to_seconds(time: str) -> int: ...
def timestr_to_milliseconds(time: str) -> int: ...
def seconds_to_timestr(seconds: int) -> str: ...
def milliseconds_to_timestr(millis: int) -> str: ...

# error codes:
# not even close to comprehensive! please add them as you need them
# i wonder if we can parse the errors.inc file here...
class status(Enum):
    EXISTS = auto()
    ID_CLASH = auto()
    NOTFOUND = auto()

# logging
class LoggingLevel(Enum):
    NONE = auto()
    CRITICAL = auto()
    ERROR = auto()
    WARNING = auto()
    NOTIFY = auto()
    INFO = auto()
    DEBUG = auto()
    SPEW = auto()

def getLoggingLevel() -> LoggingLevel: ...
def setLoggingLevel(level: LoggingLevel) -> None: ...
def lsn_to_string(lsn: int) -> str: ...
def validate_json(main: str, logs: str, verbose: bool) -> bool: ...
def normalize_json(main: str, logs: str, verbose: bool) -> bool: ...
def parse_log_level(value: str) -> LoggingLevel: ...
def use_python_logging(cb: Any) -> None: ...  # what kind of object is this?
def set_log_fd(fd: int) -> int: ...
