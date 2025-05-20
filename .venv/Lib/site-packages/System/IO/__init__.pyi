from typing import overload
from enum import Enum
import abc
import datetime
import typing
import warnings

import Microsoft.Win32.SafeHandles
import System
import System.Collections.Generic
import System.IO
import System.Runtime.InteropServices
import System.Runtime.Serialization
import System.Text
import System.Threading
import System.Threading.Tasks


class RandomAccess(System.Object):
    """This class has no documentation."""

    @staticmethod
    def flush_to_disk(handle: Microsoft.Win32.SafeHandles.SafeFileHandle) -> None:
        """
        Flushes the operating system buffers for the given file to disk.
        
        :param handle: The file handle.
        """
        ...

    @staticmethod
    def get_length(handle: Microsoft.Win32.SafeHandles.SafeFileHandle) -> int:
        """
        Gets the length of the file in bytes.
        
        :param handle: The file handle.
        :returns: A long value representing the length of the file in bytes.
        """
        ...

    @staticmethod
    @overload
    def read(handle: Microsoft.Win32.SafeHandles.SafeFileHandle, buffer: System.Span[int], file_offset: int) -> int:
        """
        Reads a sequence of bytes from given file at given offset.
        
        :param handle: The file handle.
        :param buffer: A region of memory. When this method returns, the contents of this region are replaced by the bytes read from the file.
        :param file_offset: The file position to read from.
        :returns: The total number of bytes read into the buffer. This can be less than the number of bytes allocated in the buffer if that many bytes are not currently available, or zero (0) if the end of the file has been reached.
        """
        ...

    @staticmethod
    @overload
    def read(handle: Microsoft.Win32.SafeHandles.SafeFileHandle, buffers: System.Collections.Generic.IReadOnlyList[System.Memory[int]], file_offset: int) -> int:
        """
        Reads a sequence of bytes from given file at given offset.
        
        :param handle: The file handle.
        :param buffers: A list of memory buffers. When this method returns, the contents of the buffers are replaced by the bytes read from the file.
        :param file_offset: The file position to read from.
        :returns: The total number of bytes read into the buffers. This can be less than the number of bytes allocated in the buffers if that many bytes are not currently available, or zero (0) if the end of the file has been reached.
        """
        ...

    @staticmethod
    @overload
    def read_async(handle: Microsoft.Win32.SafeHandles.SafeFileHandle, buffer: System.Memory[int], file_offset: int, cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.ValueTask[int]:
        """
        Reads a sequence of bytes from given file at given offset.
        
        :param handle: The file handle.
        :param buffer: A region of memory. When this method returns, the contents of this region are replaced by the bytes read from the file.
        :param file_offset: The file position to read from.
        :param cancellation_token: The token to monitor for cancellation requests. The default value is System.Threading.CancellationToken.None.
        :returns: The total number of bytes read into the buffer. This can be less than the number of bytes allocated in the buffer if that many bytes are not currently available, or zero (0) if the end of the file has been reached.
        """
        ...

    @staticmethod
    @overload
    def read_async(handle: Microsoft.Win32.SafeHandles.SafeFileHandle, buffers: System.Collections.Generic.IReadOnlyList[System.Memory[int]], file_offset: int, cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.ValueTask[int]:
        """
        Reads a sequence of bytes from given file at given offset.
        
        :param handle: The file handle.
        :param buffers: A list of memory buffers. When this method returns, the contents of these buffers are replaced by the bytes read from the file.
        :param file_offset: The file position to read from.
        :param cancellation_token: The token to monitor for cancellation requests. The default value is System.Threading.CancellationToken.None.
        :returns: The total number of bytes read into the buffers. This can be less than the number of bytes allocated in the buffers if that many bytes are not currently available, or zero (0) if the end of the file has been reached.
        """
        ...

    @staticmethod
    def set_length(handle: Microsoft.Win32.SafeHandles.SafeFileHandle, length: int) -> None:
        """
        Sets the length of the file to the given value.
        
        :param handle: The file handle.
        :param length: A long value representing the length of the file in bytes.
        """
        ...

    @staticmethod
    @overload
    def write(handle: Microsoft.Win32.SafeHandles.SafeFileHandle, buffer: System.ReadOnlySpan[int], file_offset: int) -> None:
        """
        Writes a sequence of bytes from given buffer to given file at given offset.
        
        :param handle: The file handle.
        :param buffer: A region of memory. This method copies the contents of this region to the file.
        :param file_offset: The file position to write to.
        """
        ...

    @staticmethod
    @overload
    def write(handle: Microsoft.Win32.SafeHandles.SafeFileHandle, buffers: System.Collections.Generic.IReadOnlyList[System.ReadOnlyMemory[int]], file_offset: int) -> None:
        """
        Writes a sequence of bytes from given buffers to given file at given offset.
        
        :param handle: The file handle.
        :param buffers: A list of memory buffers. This method copies the contents of these buffers to the file.
        :param file_offset: The file position to write to.
        """
        ...

    @staticmethod
    @overload
    def write_async(handle: Microsoft.Win32.SafeHandles.SafeFileHandle, buffer: System.ReadOnlyMemory[int], file_offset: int, cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.ValueTask:
        """
        Writes a sequence of bytes from given buffer to given file at given offset.
        
        :param handle: The file handle.
        :param buffer: A region of memory. This method copies the contents of this region to the file.
        :param file_offset: The file position to write to.
        :param cancellation_token: The token to monitor for cancellation requests. The default value is System.Threading.CancellationToken.None.
        :returns: A task representing the asynchronous completion of the write operation.
        """
        ...

    @staticmethod
    @overload
    def write_async(handle: Microsoft.Win32.SafeHandles.SafeFileHandle, buffers: System.Collections.Generic.IReadOnlyList[System.ReadOnlyMemory[int]], file_offset: int, cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.ValueTask:
        """
        Writes a sequence of bytes from given buffers to given file at given offset.
        
        :param handle: The file handle.
        :param buffers: A list of memory buffers. This method copies the contents of these buffers to the file.
        :param file_offset: The file position to write to.
        :param cancellation_token: The token to monitor for cancellation requests. The default value is System.Threading.CancellationToken.None.
        :returns: A task representing the asynchronous completion of the write operation.
        """
        ...


class FileAttributes(Enum):
    """This class has no documentation."""

    NONE = ...

    READ_ONLY = ...

    HIDDEN = ...

    SYSTEM = ...

    DIRECTORY = ...

    ARCHIVE = ...

    DEVICE = ...

    NORMAL = ...

    TEMPORARY = ...

    SPARSE_FILE = ...

    REPARSE_POINT = ...

    COMPRESSED = ...

    OFFLINE = ...

    NOT_CONTENT_INDEXED = ...

    ENCRYPTED = ...

    INTEGRITY_STREAM = ...

    NO_SCRUB_DATA = ...


class UnixFileMode(Enum):
    """Represents the Unix filesystem permissions.This enumeration supports a bitwise combination of its member values."""

    NONE = 0
    """No permissions."""

    OTHER_EXECUTE = 1
    """Execute permission for others."""

    OTHER_WRITE = 2
    """Write permission for others."""

    OTHER_READ = 4
    """Read permission for others."""

    GROUP_EXECUTE = 8
    """Execute permission for group."""

    GROUP_WRITE = 16
    """Write permission for group."""

    GROUP_READ = 32
    """Read permission for group."""

    USER_EXECUTE = 64
    """Execute permission for owner."""

    USER_WRITE = 128
    """Write permission for owner."""

    USER_READ = 256
    """Read permission for owner."""

    STICKY_BIT = 512
    """Sticky bit permission."""

    SET_GROUP = 1024
    """Set Group permission."""

    SET_USER = 2048
    """Set User permission."""


class FileSystemInfo(System.MarshalByRefObject, System.Runtime.Serialization.ISerializable):
    """This class has no documentation."""

    @property
    def attributes(self) -> System.IO.FileAttributes:
        ...

    @attributes.setter
    def attributes(self, value: System.IO.FileAttributes) -> None:
        ...

    @property
    def full_path(self) -> str:
        """This field is protected."""
        ...

    @full_path.setter
    def full_path(self, value: str) -> None:
        ...

    @property
    def original_path(self) -> str:
        """This field is protected."""
        ...

    @original_path.setter
    def original_path(self, value: str) -> None:
        ...

    @property
    def full_name(self) -> str:
        ...

    @property
    def extension(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def name(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def exists(self) -> bool:
        ...

    @property
    def creation_time(self) -> datetime.datetime:
        ...

    @creation_time.setter
    def creation_time(self, value: datetime.datetime) -> None:
        ...

    @property
    def creation_time_utc(self) -> datetime.datetime:
        ...

    @creation_time_utc.setter
    def creation_time_utc(self, value: datetime.datetime) -> None:
        ...

    @property
    def last_access_time(self) -> datetime.datetime:
        ...

    @last_access_time.setter
    def last_access_time(self, value: datetime.datetime) -> None:
        ...

    @property
    def last_access_time_utc(self) -> datetime.datetime:
        ...

    @last_access_time_utc.setter
    def last_access_time_utc(self, value: datetime.datetime) -> None:
        ...

    @property
    def last_write_time(self) -> datetime.datetime:
        ...

    @last_write_time.setter
    def last_write_time(self, value: datetime.datetime) -> None:
        ...

    @property
    def last_write_time_utc(self) -> datetime.datetime:
        ...

    @last_write_time_utc.setter
    def last_write_time_utc(self, value: datetime.datetime) -> None:
        ...

    @property
    def link_target(self) -> str:
        """
        If this FileSystemInfo instance represents a link, returns the link target's path.
        If a link does not exist in FullName, or this instance does not represent a link, returns null.
        """
        ...

    @property
    def unix_file_mode(self) -> System.IO.UnixFileMode:
        """Gets or sets the Unix file mode for the current file or directory."""
        ...

    @unix_file_mode.setter
    def unix_file_mode(self, value: System.IO.UnixFileMode) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """This method is protected."""
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """
        This method is protected.
        
        Obsoletions.LegacyFormatterImplMessage
        """
        ...

    def create_as_symbolic_link(self, path_to_target: str) -> None:
        """
        Creates a symbolic link located in FullName that points to the specified .
        
        :param path_to_target: The path of the symbolic link target.
        """
        ...

    def delete(self) -> None:
        ...

    def get_object_data(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """Obsoletions.LegacyFormatterImplMessage"""
        warnings.warn("Obsoletions.LegacyFormatterImplMessage", DeprecationWarning)

    def refresh(self) -> None:
        ...

    def resolve_link_target(self, return_final_target: bool) -> System.IO.FileSystemInfo:
        """
        Gets the target of the specified link.
        
        :param return_final_target: true to follow links to the final target; false to return the immediate next link.
        :returns: A FileSystemInfo instance if the link exists, independently if the target exists or not; null if this file or directory is not a link.
        """
        ...

    def to_string(self) -> str:
        """Returns the original path. Use FullName or Name properties for the full path or file/directory name."""
        ...


class SearchOption(Enum):
    """This class has no documentation."""

    TOP_DIRECTORY_ONLY = 0

    ALL_DIRECTORIES = 1


class MatchType(Enum):
    """Specifies the type of wildcard matching to use."""

    SIMPLE = 0
    """Matches using '*' and '?' wildcards.* matches from zero to any amount of characters. ? matches exactly one character. *.* matches any name with a period in it (with , this would match all items)."""

    WIN_32 = 1
    """Match using Win32 DOS style matching semantics.'*', '?', '<', '>', and '"' are all considered wildcards. Matches in a traditional DOS / Windows command prompt way. *.* matches all files. ? matches collapse to periods. file.??t will match file.t, file.at, and file.txt."""


class MatchCasing(Enum):
    """Specifies the type of character casing to match."""

    PLATFORM_DEFAULT = 0
    """Matches using the default casing for the given platform."""

    CASE_SENSITIVE = 1
    """Matches respecting character casing."""

    CASE_INSENSITIVE = 2
    """Matches ignoring character casing."""


class EnumerationOptions(System.Object):
    """Provides file and directory enumeration options."""

    @property
    def recurse_subdirectories(self) -> bool:
        """Gets or sets a value that indicates whether to recurse into subdirectories while enumerating. The default is false."""
        ...

    @recurse_subdirectories.setter
    def recurse_subdirectories(self, value: bool) -> None:
        ...

    @property
    def ignore_inaccessible(self) -> bool:
        """Gets or sets a value that indicates whether to skip files or directories when access is denied (for example, UnauthorizedAccessException or Security.SecurityException). The default is true."""
        ...

    @ignore_inaccessible.setter
    def ignore_inaccessible(self, value: bool) -> None:
        ...

    @property
    def buffer_size(self) -> int:
        """Gets or sets the suggested buffer size, in bytes. The default is 0 (no suggestion)."""
        ...

    @buffer_size.setter
    def buffer_size(self, value: int) -> None:
        ...

    @property
    def attributes_to_skip(self) -> System.IO.FileAttributes:
        """Gets or sets the attributes to skip. The default is FileAttributes.Hidden | FileAttributes.System."""
        ...

    @attributes_to_skip.setter
    def attributes_to_skip(self, value: System.IO.FileAttributes) -> None:
        ...

    @property
    def match_type(self) -> System.IO.MatchType:
        """Gets or sets the match type."""
        ...

    @match_type.setter
    def match_type(self, value: System.IO.MatchType) -> None:
        ...

    @property
    def match_casing(self) -> System.IO.MatchCasing:
        """Gets or sets the case matching behavior."""
        ...

    @match_casing.setter
    def match_casing(self, value: System.IO.MatchCasing) -> None:
        ...

    @property
    def max_recursion_depth(self) -> int:
        """Gets or sets a value that indicates the maximum directory depth to recurse while enumerating, when RecurseSubdirectories is set to true."""
        ...

    @max_recursion_depth.setter
    def max_recursion_depth(self, value: int) -> None:
        ...

    @property
    def return_special_directories(self) -> bool:
        """Gets or sets a value that indicates whether to return the special directory entries "." and ".."."""
        ...

    @return_special_directories.setter
    def return_special_directories(self, value: bool) -> None:
        ...

    def __init__(self) -> None:
        """Initializes a new instance of the EnumerationOptions class with the recommended default options."""
        ...


class DirectoryInfo(System.IO.FileSystemInfo):
    """This class has no documentation."""

    @property
    def name(self) -> str:
        ...

    @property
    def parent(self) -> System.IO.DirectoryInfo:
        ...

    @property
    def root(self) -> System.IO.DirectoryInfo:
        ...

    @property
    def exists(self) -> bool:
        ...

    def __init__(self, path: str) -> None:
        ...

    def create(self) -> None:
        ...

    def create_subdirectory(self, path: str) -> System.IO.DirectoryInfo:
        ...

    @overload
    def delete(self) -> None:
        ...

    @overload
    def delete(self, recursive: bool) -> None:
        ...

    @overload
    def enumerate_directories(self) -> System.Collections.Generic.IEnumerable[System.IO.DirectoryInfo]:
        ...

    @overload
    def enumerate_directories(self, search_pattern: str) -> System.Collections.Generic.IEnumerable[System.IO.DirectoryInfo]:
        ...

    @overload
    def enumerate_directories(self, search_pattern: str, search_option: System.IO.SearchOption) -> System.Collections.Generic.IEnumerable[System.IO.DirectoryInfo]:
        ...

    @overload
    def enumerate_directories(self, search_pattern: str, enumeration_options: System.IO.EnumerationOptions) -> System.Collections.Generic.IEnumerable[System.IO.DirectoryInfo]:
        ...

    @overload
    def enumerate_files(self) -> System.Collections.Generic.IEnumerable[System.IO.FileInfo]:
        ...

    @overload
    def enumerate_files(self, search_pattern: str) -> System.Collections.Generic.IEnumerable[System.IO.FileInfo]:
        ...

    @overload
    def enumerate_files(self, search_pattern: str, search_option: System.IO.SearchOption) -> System.Collections.Generic.IEnumerable[System.IO.FileInfo]:
        ...

    @overload
    def enumerate_files(self, search_pattern: str, enumeration_options: System.IO.EnumerationOptions) -> System.Collections.Generic.IEnumerable[System.IO.FileInfo]:
        ...

    @overload
    def enumerate_file_system_infos(self) -> System.Collections.Generic.IEnumerable[System.IO.FileSystemInfo]:
        ...

    @overload
    def enumerate_file_system_infos(self, search_pattern: str) -> System.Collections.Generic.IEnumerable[System.IO.FileSystemInfo]:
        ...

    @overload
    def enumerate_file_system_infos(self, search_pattern: str, search_option: System.IO.SearchOption) -> System.Collections.Generic.IEnumerable[System.IO.FileSystemInfo]:
        ...

    @overload
    def enumerate_file_system_infos(self, search_pattern: str, enumeration_options: System.IO.EnumerationOptions) -> System.Collections.Generic.IEnumerable[System.IO.FileSystemInfo]:
        ...

    @overload
    def get_directories(self) -> typing.List[System.IO.DirectoryInfo]:
        ...

    @overload
    def get_directories(self, search_pattern: str) -> typing.List[System.IO.DirectoryInfo]:
        ...

    @overload
    def get_directories(self, search_pattern: str, search_option: System.IO.SearchOption) -> typing.List[System.IO.DirectoryInfo]:
        ...

    @overload
    def get_directories(self, search_pattern: str, enumeration_options: System.IO.EnumerationOptions) -> typing.List[System.IO.DirectoryInfo]:
        ...

    @overload
    def get_files(self) -> typing.List[System.IO.FileInfo]:
        ...

    @overload
    def get_files(self, search_pattern: str) -> typing.List[System.IO.FileInfo]:
        ...

    @overload
    def get_files(self, search_pattern: str, search_option: System.IO.SearchOption) -> typing.List[System.IO.FileInfo]:
        ...

    @overload
    def get_files(self, search_pattern: str, enumeration_options: System.IO.EnumerationOptions) -> typing.List[System.IO.FileInfo]:
        ...

    @overload
    def get_file_system_infos(self) -> typing.List[System.IO.FileSystemInfo]:
        ...

    @overload
    def get_file_system_infos(self, search_pattern: str) -> typing.List[System.IO.FileSystemInfo]:
        ...

    @overload
    def get_file_system_infos(self, search_pattern: str, search_option: System.IO.SearchOption) -> typing.List[System.IO.FileSystemInfo]:
        ...

    @overload
    def get_file_system_infos(self, search_pattern: str, enumeration_options: System.IO.EnumerationOptions) -> typing.List[System.IO.FileSystemInfo]:
        ...

    def move_to(self, dest_dir_name: str) -> None:
        ...


class SeekOrigin(Enum):
    """This class has no documentation."""

    BEGIN = 0

    CURRENT = 1

    END = 2


class Stream(System.MarshalByRefObject, System.IDisposable, System.IAsyncDisposable, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    NULL: System.IO.Stream = ...

    @property
    @abc.abstractmethod
    def can_read(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def can_write(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def can_seek(self) -> bool:
        ...

    @property
    def can_timeout(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def length(self) -> int:
        ...

    @property
    @abc.abstractmethod
    def position(self) -> int:
        ...

    @position.setter
    def position(self, value: int) -> None:
        ...

    @property
    def read_timeout(self) -> int:
        ...

    @read_timeout.setter
    def read_timeout(self, value: int) -> None:
        ...

    @property
    def write_timeout(self) -> int:
        ...

    @write_timeout.setter
    def write_timeout(self, value: int) -> None:
        ...

    def begin_read(self, buffer: typing.List[int], offset: int, count: int, callback: typing.Callable[[System.IAsyncResult], None], state: typing.Any) -> System.IAsyncResult:
        ...

    def begin_write(self, buffer: typing.List[int], offset: int, count: int, callback: typing.Callable[[System.IAsyncResult], None], state: typing.Any) -> System.IAsyncResult:
        ...

    def close(self) -> None:
        ...

    @overload
    def copy_to(self, destination: System.IO.Stream) -> None:
        ...

    @overload
    def copy_to(self, destination: System.IO.Stream, buffer_size: int) -> None:
        ...

    @overload
    def copy_to_async(self, destination: System.IO.Stream) -> System.Threading.Tasks.Task:
        ...

    @overload
    def copy_to_async(self, destination: System.IO.Stream, buffer_size: int) -> System.Threading.Tasks.Task:
        ...

    @overload
    def copy_to_async(self, destination: System.IO.Stream, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        ...

    @overload
    def copy_to_async(self, destination: System.IO.Stream, buffer_size: int, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        ...

    def create_wait_handle(self) -> System.Threading.WaitHandle:
        """
        This method is protected.
        
        CreateWaitHandle has been deprecated. Use the ManualResetEvent(false) constructor instead.
        """
        warnings.warn("CreateWaitHandle has been deprecated. Use the ManualResetEvent(false) constructor instead.", DeprecationWarning)

    @overload
    def dispose(self) -> None:
        ...

    @overload
    def dispose(self, disposing: bool) -> None:
        """This method is protected."""
        ...

    def dispose_async(self) -> System.Threading.Tasks.ValueTask:
        ...

    def end_read(self, async_result: System.IAsyncResult) -> int:
        ...

    def end_write(self, async_result: System.IAsyncResult) -> None:
        ...

    def flush(self) -> None:
        ...

    @overload
    def flush_async(self) -> System.Threading.Tasks.Task:
        ...

    @overload
    def flush_async(self, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        ...

    def object_invariant(self) -> None:
        """
        This method is protected.
        
        Do not call or override this method.
        """
        warnings.warn("Do not call or override this method.", DeprecationWarning)

    @overload
    def read(self, buffer: typing.List[int], offset: int, count: int) -> int:
        ...

    @overload
    def read(self, buffer: System.Span[int]) -> int:
        ...

    @overload
    def read_async(self, buffer: typing.List[int], offset: int, count: int) -> System.Threading.Tasks.Task[int]:
        ...

    @overload
    def read_async(self, buffer: typing.List[int], offset: int, count: int, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task[int]:
        ...

    @overload
    def read_async(self, buffer: System.Memory[int], cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.ValueTask[int]:
        ...

    def read_at_least(self, buffer: System.Span[int], minimum_bytes: int, throw_on_end_of_stream: bool = True) -> int:
        """
        Reads at least a minimum number of bytes from the current stream and advances the position within the stream by the number of bytes read.
        
        :param buffer: A region of memory. When this method returns, the contents of this region are replaced by the bytes read from the current stream.
        :param minimum_bytes: The minimum number of bytes to read into the buffer.
        :param throw_on_end_of_stream: true to throw an exception if the end of the stream is reached before reading  of bytes; false to return less than  when the end of the stream is reached. The default is true.
        :returns: The total number of bytes read into the buffer. This is guaranteed to be greater than or equal to  when  is true. This will be less than  when the end of the stream is reached and  is false. This can be less than the number of bytes allocated in the buffer if that many bytes are not currently available.
        """
        ...

    def read_at_least_async(self, buffer: System.Memory[int], minimum_bytes: int, throw_on_end_of_stream: bool = True, cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.ValueTask[int]:
        """
        Asynchronously reads at least a minimum number of bytes from the current stream, advances the position within the stream by the
        number of bytes read, and monitors cancellation requests.
        
        :param buffer: The region of memory to write the data into.
        :param minimum_bytes: The minimum number of bytes to read into the buffer.
        :param throw_on_end_of_stream: true to throw an exception if the end of the stream is reached before reading  of bytes; false to return less than  when the end of the stream is reached. The default is true.
        :param cancellation_token: The token to monitor for cancellation requests.
        :returns: A task that represents the asynchronous read operation. The value of its ValueTask{TResult}.Result property contains the total number of bytes read into the buffer. This is guaranteed to be greater than or equal to  when  is true. This will be less than  when the end of the stream is reached and  is false. This can be less than the number of bytes allocated in the buffer if that many bytes are not currently available.
        """
        ...

    def read_byte(self) -> int:
        ...

    @overload
    def read_exactly(self, buffer: System.Span[int]) -> None:
        """
        Reads bytes from the current stream and advances the position within the stream until the  is filled.
        
        :param buffer: A region of memory. When this method returns, the contents of this region are replaced by the bytes read from the current stream.
        """
        ...

    @overload
    def read_exactly(self, buffer: typing.List[int], offset: int, count: int) -> None:
        """
        Reads  number of bytes from the current stream and advances the position within the stream.
        
        :param buffer: An array of bytes. When this method returns, the buffer contains the specified byte array with the values between  and ( +  - 1) replaced by the bytes read from the current stream.
        :param offset: The byte offset in  at which to begin storing the data read from the current stream.
        :param count: The number of bytes to be read from the current stream.
        """
        ...

    @overload
    def read_exactly_async(self, buffer: System.Memory[int], cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.ValueTask:
        """
        Asynchronously reads bytes from the current stream, advances the position within the stream until the  is filled,
        and monitors cancellation requests.
        
        :param buffer: The buffer to write the data into.
        :param cancellation_token: The token to monitor for cancellation requests.
        :returns: A task that represents the asynchronous read operation.
        """
        ...

    @overload
    def read_exactly_async(self, buffer: typing.List[int], offset: int, count: int, cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.ValueTask:
        """
        Asynchronously reads  number of bytes from the current stream, advances the position within the stream,
        and monitors cancellation requests.
        
        :param buffer: The buffer to write the data into.
        :param offset: The byte offset in  at which to begin writing data from the stream.
        :param count: The number of bytes to be read from the current stream.
        :param cancellation_token: The token to monitor for cancellation requests.
        :returns: A task that represents the asynchronous read operation.
        """
        ...

    def seek(self, offset: int, origin: System.IO.SeekOrigin) -> int:
        ...

    def set_length(self, value: int) -> None:
        ...

    @staticmethod
    def synchronized(stream: System.IO.Stream) -> System.IO.Stream:
        ...

    @staticmethod
    def validate_buffer_arguments(buffer: typing.List[int], offset: int, count: int) -> None:
        """
        Validates arguments provided to reading and writing methods on Stream.
        
        This method is protected.
        
        :param buffer: The array "buffer" argument passed to the reading or writing method.
        :param offset: The integer "offset" argument passed to the reading or writing method.
        :param count: The integer "count" argument passed to the reading or writing method.
        """
        ...

    @staticmethod
    def validate_copy_to_arguments(destination: System.IO.Stream, buffer_size: int) -> None:
        """
        Validates arguments provided to the CopyTo(Stream, int) or CopyToAsync(Stream, int, CancellationToken) methods.
        
        This method is protected.
        
        :param destination: The Stream "destination" argument passed to the copy method.
        :param buffer_size: The integer "buffer_size" argument passed to the copy method.
        """
        ...

    @overload
    def write(self, buffer: typing.List[int], offset: int, count: int) -> None:
        ...

    @overload
    def write(self, buffer: System.ReadOnlySpan[int]) -> None:
        ...

    @overload
    def write_async(self, buffer: typing.List[int], offset: int, count: int) -> System.Threading.Tasks.Task:
        ...

    @overload
    def write_async(self, buffer: typing.List[int], offset: int, count: int, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        ...

    @overload
    def write_async(self, buffer: System.ReadOnlyMemory[int], cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.ValueTask:
        ...

    def write_byte(self, value: int) -> None:
        ...


class FileAccess(Enum):
    """This class has no documentation."""

    READ = 1

    WRITE = 2

    READ_WRITE = 3


class FileMode(Enum):
    """This class has no documentation."""

    CREATE_NEW = 1

    CREATE = 2

    OPEN = 3

    OPEN_OR_CREATE = 4

    TRUNCATE = 5

    APPEND = 6


class FileShare(Enum):
    """This class has no documentation."""

    NONE = 0

    READ = 1

    WRITE = 2

    READ_WRITE = 3

    DELETE = 4

    INHERITABLE = ...


class FileOptions(Enum):
    """This class has no documentation."""

    NONE = 0

    WRITE_THROUGH = ...

    ASYNCHRONOUS = ...

    RANDOM_ACCESS = ...

    DELETE_ON_CLOSE = ...

    SEQUENTIAL_SCAN = ...

    ENCRYPTED = ...


class FileStreamOptions(System.Object):
    """This class has no documentation."""

    @property
    def mode(self) -> System.IO.FileMode:
        """One of the enumeration values that determines how to open or create the file."""
        ...

    @mode.setter
    def mode(self, value: System.IO.FileMode) -> None:
        ...

    @property
    def access(self) -> System.IO.FileAccess:
        """A bitwise combination of the enumeration values that determines how the file can be accessed by the FileStream object. This also determines the values returned by the FileStream.CanRead and FileStream.CanWrite properties of the FileStream object."""
        ...

    @access.setter
    def access(self, value: System.IO.FileAccess) -> None:
        ...

    @property
    def share(self) -> System.IO.FileShare:
        """A bitwise combination of the enumeration values that determines how the file will be shared by processes. The default value is FileShare.Read."""
        ...

    @share.setter
    def share(self, value: System.IO.FileShare) -> None:
        ...

    @property
    def options(self) -> System.IO.FileOptions:
        """A bitwise combination of the enumeration values that specifies additional file options. The default value is FileOptions.None, which indicates synchronous IO."""
        ...

    @options.setter
    def options(self, value: System.IO.FileOptions) -> None:
        ...

    @property
    def preallocation_size(self) -> int:
        """
        The initial allocation size in bytes for the file. A positive value is effective only when a regular file is being created, overwritten, or replaced.
        Negative values are not allowed.
        In other cases (including the default 0 value), it's ignored.
        """
        ...

    @preallocation_size.setter
    def preallocation_size(self, value: int) -> None:
        ...

    @property
    def buffer_size(self) -> int:
        """
        The size of the buffer used by FileStream for buffering. The default buffer size is 4096.
        0 or 1 means that buffering should be disabled. Negative values are not allowed.
        """
        ...

    @buffer_size.setter
    def buffer_size(self, value: int) -> None:
        ...

    @property
    def unix_create_mode(self) -> typing.Optional[System.IO.UnixFileMode]:
        """Unix file mode used when a new file is created."""
        ...

    @unix_create_mode.setter
    def unix_create_mode(self, value: typing.Optional[System.IO.UnixFileMode]) -> None:
        ...


class FileStream(System.IO.Stream):
    """This class has no documentation."""

    @property
    def handle(self) -> System.IntPtr:
        """FileStream.Handle has been deprecated. Use FileStream's SafeFileHandle property instead."""
        warnings.warn("FileStream.Handle has been deprecated. Use FileStream's SafeFileHandle property instead.", DeprecationWarning)

    @property
    def can_read(self) -> bool:
        """Gets a value indicating whether the current stream supports reading."""
        ...

    @property
    def can_write(self) -> bool:
        """Gets a value indicating whether the current stream supports writing."""
        ...

    @property
    def safe_file_handle(self) -> Microsoft.Win32.SafeHandles.SafeFileHandle:
        ...

    @property
    def name(self) -> str:
        """Gets the path that was passed to the constructor."""
        ...

    @property
    def is_async(self) -> bool:
        """Gets a value indicating whether the stream was opened for I/O to be performed synchronously or asynchronously."""
        ...

    @property
    def length(self) -> int:
        """Gets the length of the stream in bytes."""
        ...

    @property
    def position(self) -> int:
        """Gets or sets the position within the current stream"""
        ...

    @position.setter
    def position(self, value: int) -> None:
        ...

    @property
    def can_seek(self) -> bool:
        ...

    @overload
    def __init__(self, handle: Microsoft.Win32.SafeHandles.SafeFileHandle, access: System.IO.FileAccess) -> None:
        ...

    @overload
    def __init__(self, handle: Microsoft.Win32.SafeHandles.SafeFileHandle, access: System.IO.FileAccess, buffer_size: int) -> None:
        ...

    @overload
    def __init__(self, handle: Microsoft.Win32.SafeHandles.SafeFileHandle, access: System.IO.FileAccess, buffer_size: int, is_async: bool) -> None:
        ...

    @overload
    def __init__(self, path: str, mode: System.IO.FileMode) -> None:
        ...

    @overload
    def __init__(self, path: str, mode: System.IO.FileMode, access: System.IO.FileAccess) -> None:
        ...

    @overload
    def __init__(self, path: str, mode: System.IO.FileMode, access: System.IO.FileAccess, share: System.IO.FileShare) -> None:
        ...

    @overload
    def __init__(self, path: str, mode: System.IO.FileMode, access: System.IO.FileAccess, share: System.IO.FileShare, buffer_size: int) -> None:
        ...

    @overload
    def __init__(self, path: str, mode: System.IO.FileMode, access: System.IO.FileAccess, share: System.IO.FileShare, buffer_size: int, use_async: bool) -> None:
        ...

    @overload
    def __init__(self, path: str, mode: System.IO.FileMode, access: System.IO.FileAccess, share: System.IO.FileShare, buffer_size: int, options: System.IO.FileOptions) -> None:
        ...

    @overload
    def __init__(self, path: str, options: System.IO.FileStreamOptions) -> None:
        """
        Initializes a new instance of the FileStream class with the specified path, creation mode, read/write and sharing permission, the access other FileStreams can have to the same file, the buffer size,  additional file options and the allocation size.
        
        :param path: A relative or absolute path for the file that the current FileStream instance will encapsulate.
        :param options: An object that describes optional FileStream parameters to use.
        """
        ...

    @overload
    def __init__(self, handle: System.IntPtr, access: System.IO.FileAccess) -> None:
        """This constructor has been deprecated. Use FileStream(SafeFileHandle handle, FileAccess access) instead."""
        ...

    @overload
    def __init__(self, handle: System.IntPtr, access: System.IO.FileAccess, owns_handle: bool) -> None:
        """This constructor has been deprecated. Use FileStream(SafeFileHandle handle, FileAccess access) and optionally make a new SafeFileHandle with owns_handle=false if needed instead."""
        ...

    @overload
    def __init__(self, handle: System.IntPtr, access: System.IO.FileAccess, owns_handle: bool, buffer_size: int) -> None:
        """This constructor has been deprecated. Use FileStream(SafeFileHandle handle, FileAccess access, int buffer_size) and optionally make a new SafeFileHandle with owns_handle=false if needed instead."""
        ...

    @overload
    def __init__(self, handle: System.IntPtr, access: System.IO.FileAccess, owns_handle: bool, buffer_size: int, is_async: bool) -> None:
        """This constructor has been deprecated. Use FileStream(SafeFileHandle handle, FileAccess access, int buffer_size, bool is_async) and optionally make a new SafeFileHandle with owns_handle=false if needed instead."""
        ...

    def begin_read(self, buffer: typing.List[int], offset: int, count: int, callback: typing.Callable[[System.IAsyncResult], None], state: typing.Any) -> System.IAsyncResult:
        ...

    def begin_write(self, buffer: typing.List[int], offset: int, count: int, callback: typing.Callable[[System.IAsyncResult], None], state: typing.Any) -> System.IAsyncResult:
        ...

    def copy_to(self, destination: System.IO.Stream, buffer_size: int) -> None:
        ...

    def copy_to_async(self, destination: System.IO.Stream, buffer_size: int, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        ...

    def dispose(self, disposing: bool) -> None:
        """This method is protected."""
        ...

    def dispose_async(self) -> System.Threading.Tasks.ValueTask:
        ...

    def end_read(self, async_result: System.IAsyncResult) -> int:
        ...

    def end_write(self, async_result: System.IAsyncResult) -> None:
        ...

    @overload
    def flush(self) -> None:
        """Clears buffers for this stream and causes any buffered data to be written to the file."""
        ...

    @overload
    def flush(self, flush_to_disk: bool) -> None:
        """
        Clears buffers for this stream, and if  is true,
        causes any buffered data to be written to the file.
        """
        ...

    def flush_async(self, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        ...

    def lock(self, position: int, length: int) -> None:
        ...

    @overload
    def read(self, buffer: typing.List[int], offset: int, count: int) -> int:
        ...

    @overload
    def read(self, buffer: System.Span[int]) -> int:
        ...

    @overload
    def read_async(self, buffer: typing.List[int], offset: int, count: int, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task[int]:
        ...

    @overload
    def read_async(self, buffer: System.Memory[int], cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.ValueTask[int]:
        ...

    def read_byte(self) -> int:
        """
        Reads a byte from the file stream.  Returns the byte cast to an int
        or -1 if reading from the end of the stream.
        """
        ...

    def seek(self, offset: int, origin: System.IO.SeekOrigin) -> int:
        ...

    def set_length(self, value: int) -> None:
        """
        Sets the length of this stream to the given value.
        
        :param value: The new length of the stream.
        """
        ...

    def unlock(self, position: int, length: int) -> None:
        ...

    @overload
    def write(self, buffer: typing.List[int], offset: int, count: int) -> None:
        ...

    @overload
    def write(self, buffer: System.ReadOnlySpan[int]) -> None:
        ...

    @overload
    def write_async(self, buffer: typing.List[int], offset: int, count: int, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        ...

    @overload
    def write_async(self, buffer: System.ReadOnlyMemory[int], cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.ValueTask:
        ...

    def write_byte(self, value: int) -> None:
        """
        Writes a byte to the current position in the stream and advances the position
        within the stream by one byte.
        
        :param value: The byte to write to the stream.
        """
        ...


class TextReader(System.MarshalByRefObject, System.IDisposable, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    NULL: System.IO.TextReader = ...

    def __init__(self) -> None:
        """This method is protected."""
        ...

    def close(self) -> None:
        ...

    @overload
    def dispose(self) -> None:
        ...

    @overload
    def dispose(self, disposing: bool) -> None:
        """This method is protected."""
        ...

    def peek(self) -> int:
        ...

    @overload
    def read(self) -> int:
        ...

    @overload
    def read(self, buffer: typing.List[str], index: int, count: int) -> int:
        ...

    @overload
    def read(self, buffer: System.Span[str]) -> int:
        ...

    @overload
    def read_async(self, buffer: typing.List[str], index: int, count: int) -> System.Threading.Tasks.Task[int]:
        ...

    @overload
    def read_async(self, buffer: System.Memory[str], cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.ValueTask[int]:
        ...

    @overload
    def read_block(self, buffer: typing.List[str], index: int, count: int) -> int:
        ...

    @overload
    def read_block(self, buffer: System.Span[str]) -> int:
        ...

    @overload
    def read_block_async(self, buffer: typing.List[str], index: int, count: int) -> System.Threading.Tasks.Task[int]:
        ...

    @overload
    def read_block_async(self, buffer: System.Memory[str], cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.ValueTask[int]:
        ...

    def read_line(self) -> str:
        ...

    @overload
    def read_line_async(self) -> System.Threading.Tasks.Task[str]:
        ...

    @overload
    def read_line_async(self, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.ValueTask[str]:
        """
        Reads a line of characters asynchronously and returns the data as a string.
        
        :param cancellation_token: The token to monitor for cancellation requests.
        :returns: A value task that represents the asynchronous read operation. The value of the TResult parameter contains the next line from the text reader, or is null if all of the characters have been read.
        """
        ...

    def read_to_end(self) -> str:
        ...

    @overload
    def read_to_end_async(self) -> System.Threading.Tasks.Task[str]:
        ...

    @overload
    def read_to_end_async(self, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task[str]:
        """
        Reads all characters from the current position to the end of the text reader asynchronously and returns them as one string.
        
        :param cancellation_token: The token to monitor for cancellation requests.
        :returns: A task that represents the asynchronous read operation. The value of the TResult parameter contains a string with the characters from the current position to the end of the text reader.
        """
        ...

    @staticmethod
    def synchronized(reader: System.IO.TextReader) -> System.IO.TextReader:
        ...


class StreamReader(System.IO.TextReader):
    """This class has no documentation."""

    NULL: System.IO.StreamReader = ...

    @property
    def current_encoding(self) -> System.Text.Encoding:
        ...

    @property
    def base_stream(self) -> System.IO.Stream:
        ...

    @property
    def end_of_stream(self) -> bool:
        ...

    @overload
    def __init__(self, stream: System.IO.Stream) -> None:
        ...

    @overload
    def __init__(self, stream: System.IO.Stream, detect_encoding_from_byte_order_marks: bool) -> None:
        ...

    @overload
    def __init__(self, stream: System.IO.Stream, encoding: System.Text.Encoding) -> None:
        ...

    @overload
    def __init__(self, stream: System.IO.Stream, encoding: System.Text.Encoding, detect_encoding_from_byte_order_marks: bool) -> None:
        ...

    @overload
    def __init__(self, stream: System.IO.Stream, encoding: System.Text.Encoding, detect_encoding_from_byte_order_marks: bool, buffer_size: int) -> None:
        ...

    @overload
    def __init__(self, stream: System.IO.Stream, encoding: System.Text.Encoding = None, detect_encoding_from_byte_order_marks: bool = True, buffer_size: int = -1, leave_open: bool = False) -> None:
        ...

    @overload
    def __init__(self, path: str) -> None:
        ...

    @overload
    def __init__(self, path: str, detect_encoding_from_byte_order_marks: bool) -> None:
        ...

    @overload
    def __init__(self, path: str, encoding: System.Text.Encoding) -> None:
        ...

    @overload
    def __init__(self, path: str, encoding: System.Text.Encoding, detect_encoding_from_byte_order_marks: bool) -> None:
        ...

    @overload
    def __init__(self, path: str, encoding: System.Text.Encoding, detect_encoding_from_byte_order_marks: bool, buffer_size: int) -> None:
        ...

    @overload
    def __init__(self, path: str, options: System.IO.FileStreamOptions) -> None:
        ...

    @overload
    def __init__(self, path: str, encoding: System.Text.Encoding, detect_encoding_from_byte_order_marks: bool, options: System.IO.FileStreamOptions) -> None:
        ...

    def close(self) -> None:
        ...

    def discard_buffered_data(self) -> None:
        ...

    def dispose(self, disposing: bool) -> None:
        """This method is protected."""
        ...

    def peek(self) -> int:
        ...

    @overload
    def read(self) -> int:
        ...

    @overload
    def read(self, buffer: typing.List[str], index: int, count: int) -> int:
        ...

    @overload
    def read(self, buffer: System.Span[str]) -> int:
        ...

    @overload
    def read_async(self, buffer: typing.List[str], index: int, count: int) -> System.Threading.Tasks.Task[int]:
        ...

    @overload
    def read_async(self, buffer: System.Memory[str], cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.ValueTask[int]:
        ...

    @overload
    def read_block(self, buffer: typing.List[str], index: int, count: int) -> int:
        ...

    @overload
    def read_block(self, buffer: System.Span[str]) -> int:
        ...

    @overload
    def read_block_async(self, buffer: typing.List[str], index: int, count: int) -> System.Threading.Tasks.Task[int]:
        ...

    @overload
    def read_block_async(self, buffer: System.Memory[str], cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.ValueTask[int]:
        ...

    def read_line(self) -> str:
        ...

    @overload
    def read_line_async(self) -> System.Threading.Tasks.Task[str]:
        ...

    @overload
    def read_line_async(self, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.ValueTask[str]:
        """
        Reads a line of characters asynchronously from the current stream and returns the data as a string.
        
        :param cancellation_token: The token to monitor for cancellation requests.
        :returns: A value task that represents the asynchronous read operation. The value of the TResult parameter contains the next line from the stream, or is null if all of the characters have been read.
        """
        ...

    def read_to_end(self) -> str:
        ...

    @overload
    def read_to_end_async(self) -> System.Threading.Tasks.Task[str]:
        ...

    @overload
    def read_to_end_async(self, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task[str]:
        """
        Reads all characters from the current position to the end of the stream asynchronously and returns them as one string.
        
        :param cancellation_token: The token to monitor for cancellation requests.
        :returns: A task that represents the asynchronous read operation. The value of the TResult parameter contains a string with the characters from the current position to the end of the stream.
        """
        ...


class TextWriter(System.MarshalByRefObject, System.IDisposable, System.IAsyncDisposable, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    NULL: System.IO.TextWriter = ...

    @property
    def core_new_line(self) -> typing.List[str]:
        """
        This is the 'NewLine' property expressed as a char[].
        It is exposed to subclasses as a protected field for read-only
        purposes.  You should only modify it by using the 'NewLine' property.
        In particular you should never modify the elements of the array
        as they are shared among many instances of TextWriter.
        
        This field is protected.
        """
        ...

    @core_new_line.setter
    def core_new_line(self, value: typing.List[str]) -> None:
        ...

    @property
    def format_provider(self) -> System.IFormatProvider:
        ...

    @property
    @abc.abstractmethod
    def encoding(self) -> System.Text.Encoding:
        ...

    @property
    def new_line(self) -> str:
        """
        Returns the line terminator string used by this TextWriter. The default line
        terminator string is Environment.NewLine, which is platform specific.
        On Windows this is a carriage return followed by a line feed ("\\r\\n").
        On OSX and Linux this is a line feed ("\\n").
        """
        ...

    @new_line.setter
    def new_line(self, value: str) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """This method is protected."""
        ...

    @overload
    def __init__(self, format_provider: System.IFormatProvider) -> None:
        """This method is protected."""
        ...

    def close(self) -> None:
        ...

    @staticmethod
    def create_broadcasting(*writers: typing.Union[System.IO.TextWriter, typing.Iterable[System.IO.TextWriter]]) -> System.IO.TextWriter:
        """
        Creates an instance of TextWriter that writes supplied inputs to each of the writers in .
        
        :param writers: The TextWriter instances to which all operations should be broadcast (multiplexed).
        :returns: An instance of TextWriter that writes supplied inputs to each of the writers in.
        """
        ...

    @overload
    def dispose(self, disposing: bool) -> None:
        """This method is protected."""
        ...

    @overload
    def dispose(self) -> None:
        ...

    def dispose_async(self) -> System.Threading.Tasks.ValueTask:
        ...

    def flush(self) -> None:
        ...

    @overload
    def flush_async(self) -> System.Threading.Tasks.Task:
        ...

    @overload
    def flush_async(self, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        """
        Asynchronously clears all buffers for the current writer and causes any buffered data to
        be written to the underlying device.
        
        :param cancellation_token: The CancellationToken to monitor for cancellation requests.
        :returns: A Task that represents the asynchronous flush operation.
        """
        ...

    @staticmethod
    def synchronized(writer: System.IO.TextWriter) -> System.IO.TextWriter:
        ...

    @overload
    def write(self, value: typing.Any) -> None:
        ...

    @overload
    def write(self, format: str, arg_0: typing.Any) -> None:
        ...

    @overload
    def write(self, format: str, arg_0: typing.Any, arg_1: typing.Any) -> None:
        ...

    @overload
    def write(self, format: str, arg_0: typing.Any, arg_1: typing.Any, arg_2: typing.Any) -> None:
        ...

    @overload
    def write(self, value: str) -> None:
        ...

    @overload
    def write(self, buffer: typing.List[str]) -> None:
        ...

    @overload
    def write(self, buffer: typing.List[str], index: int, count: int) -> None:
        ...

    @overload
    def write(self, buffer: System.ReadOnlySpan[str]) -> None:
        ...

    @overload
    def write(self, value: bool) -> None:
        ...

    @overload
    def write(self, value: int) -> None:
        ...

    @overload
    def write(self, value: float) -> None:
        ...

    @overload
    def write(self, value: System.Text.StringBuilder) -> None:
        """
        Equivalent to Write(stringBuilder.ToString()) however it uses the
        StringBuilder.GetChunks() method to avoid creating the intermediate string
        
        :param value: The string (as a StringBuilder) to write to the stream
        """
        ...

    @overload
    def write(self, format: str, *arg: typing.Union[System.Object, typing.Iterable[System.Object]]) -> None:
        ...

    @overload
    def write_async(self, value: str) -> System.Threading.Tasks.Task:
        ...

    @overload
    def write_async(self, value: System.Text.StringBuilder, cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        """
        Equivalent to WriteAsync(stringBuilder.ToString()) however it uses the
        StringBuilder.GetChunks() method to avoid creating the intermediate string
        
        :param value: The string (as a StringBuilder) to write to the stream
        :param cancellation_token: The token to monitor for cancellation requests.
        """
        ...

    @overload
    def write_async(self, buffer: typing.List[str]) -> System.Threading.Tasks.Task:
        ...

    @overload
    def write_async(self, buffer: typing.List[str], index: int, count: int) -> System.Threading.Tasks.Task:
        ...

    @overload
    def write_async(self, buffer: System.ReadOnlyMemory[str], cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        ...

    @overload
    def write_line(self, value: typing.Any) -> None:
        ...

    @overload
    def write_line(self, format: str, arg_0: typing.Any) -> None:
        ...

    @overload
    def write_line(self, format: str, arg_0: typing.Any, arg_1: typing.Any) -> None:
        ...

    @overload
    def write_line(self, format: str, arg_0: typing.Any, arg_1: typing.Any, arg_2: typing.Any) -> None:
        ...

    @overload
    def write_line(self) -> None:
        ...

    @overload
    def write_line(self, value: str) -> None:
        ...

    @overload
    def write_line(self, buffer: typing.List[str]) -> None:
        ...

    @overload
    def write_line(self, buffer: typing.List[str], index: int, count: int) -> None:
        ...

    @overload
    def write_line(self, buffer: System.ReadOnlySpan[str]) -> None:
        ...

    @overload
    def write_line(self, value: bool) -> None:
        ...

    @overload
    def write_line(self, value: int) -> None:
        ...

    @overload
    def write_line(self, value: float) -> None:
        ...

    @overload
    def write_line(self, value: System.Text.StringBuilder) -> None:
        """
        Equivalent to WriteLine(stringBuilder.ToString()) however it uses the
        StringBuilder.GetChunks() method to avoid creating the intermediate string
        """
        ...

    @overload
    def write_line(self, format: str, *arg: typing.Union[System.Object, typing.Iterable[System.Object]]) -> None:
        ...

    @overload
    def write_line_async(self, value: str) -> System.Threading.Tasks.Task:
        ...

    @overload
    def write_line_async(self, value: System.Text.StringBuilder, cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        """
        Equivalent to WriteLineAsync(stringBuilder.ToString()) however it uses the
        StringBuilder.GetChunks() method to avoid creating the intermediate string
        
        :param value: The string (as a StringBuilder) to write to the stream
        :param cancellation_token: The token to monitor for cancellation requests.
        """
        ...

    @overload
    def write_line_async(self, buffer: typing.List[str]) -> System.Threading.Tasks.Task:
        ...

    @overload
    def write_line_async(self, buffer: typing.List[str], index: int, count: int) -> System.Threading.Tasks.Task:
        ...

    @overload
    def write_line_async(self, buffer: System.ReadOnlyMemory[str], cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        ...

    @overload
    def write_line_async(self) -> System.Threading.Tasks.Task:
        ...


class StreamWriter(System.IO.TextWriter):
    """This class has no documentation."""

    NULL: System.IO.StreamWriter = ...

    @property
    def auto_flush(self) -> bool:
        ...

    @auto_flush.setter
    def auto_flush(self, value: bool) -> None:
        ...

    @property
    def base_stream(self) -> System.IO.Stream:
        ...

    @property
    def encoding(self) -> System.Text.Encoding:
        ...

    @overload
    def __init__(self, stream: System.IO.Stream) -> None:
        ...

    @overload
    def __init__(self, stream: System.IO.Stream, encoding: System.Text.Encoding) -> None:
        ...

    @overload
    def __init__(self, stream: System.IO.Stream, encoding: System.Text.Encoding, buffer_size: int) -> None:
        ...

    @overload
    def __init__(self, stream: System.IO.Stream, encoding: System.Text.Encoding = None, buffer_size: int = -1, leave_open: bool = False) -> None:
        ...

    @overload
    def __init__(self, path: str) -> None:
        ...

    @overload
    def __init__(self, path: str, append: bool) -> None:
        ...

    @overload
    def __init__(self, path: str, append: bool, encoding: System.Text.Encoding) -> None:
        ...

    @overload
    def __init__(self, path: str, append: bool, encoding: System.Text.Encoding, buffer_size: int) -> None:
        ...

    @overload
    def __init__(self, path: str, options: System.IO.FileStreamOptions) -> None:
        ...

    @overload
    def __init__(self, path: str, encoding: System.Text.Encoding, options: System.IO.FileStreamOptions) -> None:
        ...

    def close(self) -> None:
        ...

    def dispose(self, disposing: bool) -> None:
        """This method is protected."""
        ...

    def dispose_async(self) -> System.Threading.Tasks.ValueTask:
        ...

    def flush(self) -> None:
        ...

    @overload
    def flush_async(self) -> System.Threading.Tasks.Task:
        ...

    @overload
    def flush_async(self, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        """
        Clears all buffers for this stream asynchronously and causes any buffered data to be written to the underlying device.
        
        :param cancellation_token: The CancellationToken to monitor for cancellation requests.
        :returns: A Task that represents the asynchronous flush operation.
        """
        ...

    @overload
    def write(self, format: str, arg_0: typing.Any) -> None:
        ...

    @overload
    def write(self, format: str, arg_0: typing.Any, arg_1: typing.Any) -> None:
        ...

    @overload
    def write(self, format: str, arg_0: typing.Any, arg_1: typing.Any, arg_2: typing.Any) -> None:
        ...

    @overload
    def write(self, value: str) -> None:
        ...

    @overload
    def write(self, buffer: typing.List[str]) -> None:
        ...

    @overload
    def write(self, buffer: typing.List[str], index: int, count: int) -> None:
        ...

    @overload
    def write(self, buffer: System.ReadOnlySpan[str]) -> None:
        ...

    @overload
    def write(self, format: str, *arg: typing.Union[System.Object, typing.Iterable[System.Object]]) -> None:
        ...

    @overload
    def write_async(self, value: str) -> System.Threading.Tasks.Task:
        ...

    @overload
    def write_async(self, buffer: typing.List[str], index: int, count: int) -> System.Threading.Tasks.Task:
        ...

    @overload
    def write_async(self, buffer: System.ReadOnlyMemory[str], cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        ...

    @overload
    def write_line(self, format: str, arg_0: typing.Any) -> None:
        ...

    @overload
    def write_line(self, format: str, arg_0: typing.Any, arg_1: typing.Any) -> None:
        ...

    @overload
    def write_line(self, format: str, arg_0: typing.Any, arg_1: typing.Any, arg_2: typing.Any) -> None:
        ...

    @overload
    def write_line(self, value: str) -> None:
        ...

    @overload
    def write_line(self, buffer: System.ReadOnlySpan[str]) -> None:
        ...

    @overload
    def write_line(self, format: str, *arg: typing.Union[System.Object, typing.Iterable[System.Object]]) -> None:
        ...

    @overload
    def write_line_async(self) -> System.Threading.Tasks.Task:
        ...

    @overload
    def write_line_async(self, value: str) -> System.Threading.Tasks.Task:
        ...

    @overload
    def write_line_async(self, buffer: typing.List[str], index: int, count: int) -> System.Threading.Tasks.Task:
        ...

    @overload
    def write_line_async(self, buffer: System.ReadOnlyMemory[str], cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        ...


class FileInfo(System.IO.FileSystemInfo):
    """This class has no documentation."""

    @property
    def name(self) -> str:
        ...

    @property
    def length(self) -> int:
        ...

    @property
    def directory_name(self) -> str:
        ...

    @property
    def directory(self) -> System.IO.DirectoryInfo:
        ...

    @property
    def is_read_only(self) -> bool:
        ...

    @is_read_only.setter
    def is_read_only(self, value: bool) -> None:
        ...

    @property
    def exists(self) -> bool:
        ...

    def __init__(self, file_name: str) -> None:
        ...

    def append_text(self) -> System.IO.StreamWriter:
        ...

    @overload
    def copy_to(self, dest_file_name: str) -> System.IO.FileInfo:
        ...

    @overload
    def copy_to(self, dest_file_name: str, overwrite: bool) -> System.IO.FileInfo:
        ...

    def create(self) -> System.IO.FileStream:
        ...

    def create_text(self) -> System.IO.StreamWriter:
        ...

    def decrypt(self) -> None:
        ...

    def delete(self) -> None:
        ...

    def encrypt(self) -> None:
        ...

    @overload
    def move_to(self, dest_file_name: str) -> None:
        ...

    @overload
    def move_to(self, dest_file_name: str, overwrite: bool) -> None:
        ...

    @overload
    def open(self, options: System.IO.FileStreamOptions) -> System.IO.FileStream:
        """Initializes a new instance of the FileStream class with the specified creation mode, read/write and sharing permission, the access other FileStreams can have to the same file, the buffer size, additional file options and the allocation size."""
        ...

    @overload
    def open(self, mode: System.IO.FileMode) -> System.IO.FileStream:
        ...

    @overload
    def open(self, mode: System.IO.FileMode, access: System.IO.FileAccess) -> System.IO.FileStream:
        ...

    @overload
    def open(self, mode: System.IO.FileMode, access: System.IO.FileAccess, share: System.IO.FileShare) -> System.IO.FileStream:
        ...

    def open_read(self) -> System.IO.FileStream:
        ...

    def open_text(self) -> System.IO.StreamReader:
        ...

    def open_write(self) -> System.IO.FileStream:
        ...

    @overload
    def replace(self, destination_file_name: str, destination_backup_file_name: str) -> System.IO.FileInfo:
        ...

    @overload
    def replace(self, destination_file_name: str, destination_backup_file_name: str, ignore_metadata_errors: bool) -> System.IO.FileInfo:
        ...


class File(System.Object):
    """This class has no documentation."""

    @staticmethod
    @overload
    def append_all_bytes(path: str, bytes: typing.List[int]) -> None:
        """
        Appends the specified byte array to the end of the file at the given path.
        If the file doesn't exist, this method creates a new file.
        
        :param path: The file to append to.
        :param bytes: The bytes to append to the file.
        """
        ...

    @staticmethod
    @overload
    def append_all_bytes(path: str, bytes: System.ReadOnlySpan[int]) -> None:
        """
        Appends the specified byte array to the end of the file at the given path.
        If the file doesn't exist, this method creates a new file.
        
        :param path: The file to append to.
        :param bytes: The bytes to append to the file.
        """
        ...

    @staticmethod
    @overload
    def append_all_bytes_async(path: str, bytes: typing.List[int], cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        """
        Asynchronously appends the specified byte array to the end of the file at the given path.
        If the file doesn't exist, this method creates a new file. If the operation is canceled, the task will return in a canceled state.
        
        :param path: The file to append to.
        :param bytes: The bytes to append to the file.
        :param cancellation_token: The token to monitor for cancellation requests. The default value is CancellationToken.None.
        :returns: A task that represents the asynchronous append operation.
        """
        ...

    @staticmethod
    @overload
    def append_all_bytes_async(path: str, bytes: System.ReadOnlyMemory[int], cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        """
        Asynchronously appends the specified byte array to the end of the file at the given path.
        If the file doesn't exist, this method creates a new file. If the operation is canceled, the task will return in a canceled state.
        
        :param path: The file to append to.
        :param bytes: The bytes to append to the file.
        :param cancellation_token: The token to monitor for cancellation requests. The default value is CancellationToken.None.
        :returns: A task that represents the asynchronous append operation.
        """
        ...

    @staticmethod
    @overload
    def append_all_lines(path: str, contents: System.Collections.Generic.IEnumerable[str]) -> None:
        ...

    @staticmethod
    @overload
    def append_all_lines(path: str, contents: System.Collections.Generic.IEnumerable[str], encoding: System.Text.Encoding) -> None:
        ...

    @staticmethod
    @overload
    def append_all_lines_async(path: str, contents: System.Collections.Generic.IEnumerable[str], cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        ...

    @staticmethod
    @overload
    def append_all_lines_async(path: str, contents: System.Collections.Generic.IEnumerable[str], encoding: System.Text.Encoding, cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        ...

    @staticmethod
    @overload
    def append_all_text(path: str, contents: str) -> None:
        ...

    @staticmethod
    @overload
    def append_all_text(path: str, contents: System.ReadOnlySpan[str]) -> None:
        """
        Appends the specified string to the file, creating the file if it does not already exist.
        
        :param path: The file to append to.
        :param contents: The characters to write to the file.
        """
        ...

    @staticmethod
    @overload
    def append_all_text(path: str, contents: str, encoding: System.Text.Encoding) -> None:
        ...

    @staticmethod
    @overload
    def append_all_text(path: str, contents: System.ReadOnlySpan[str], encoding: System.Text.Encoding) -> None:
        """
        Appends the specified string to the file, creating the file if it does not already exist.
        
        :param path: The file to append to.
        :param contents: The characters to write to the file.
        :param encoding: The encoding to apply to the string.
        """
        ...

    @staticmethod
    @overload
    def append_all_text_async(path: str, contents: str, cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        ...

    @staticmethod
    @overload
    def append_all_text_async(path: str, contents: System.ReadOnlyMemory[str], cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        """
        Asynchronously opens a file or creates a file if it does not already exist, appends the specified string to the file, and then closes the file.
        
        :param path: The file to append the specified string to.
        :param contents: The characters to append to the file.
        :param cancellation_token: The token to monitor for cancellation requests. The default value is CancellationToken.None.
        :returns: A task that represents the asynchronous append operation.
        """
        ...

    @staticmethod
    @overload
    def append_all_text_async(path: str, contents: str, encoding: System.Text.Encoding, cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        ...

    @staticmethod
    @overload
    def append_all_text_async(path: str, contents: System.ReadOnlyMemory[str], encoding: System.Text.Encoding, cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        """
        Asynchronously opens a file or creates the file if it does not already exist, appends the specified string to the file using the specified encoding, and then closes the file.
        
        :param path: The file to append the specified string to.
        :param contents: The characters to append to the file.
        :param encoding: The character encoding to use.
        :param cancellation_token: The token to monitor for cancellation requests. The default value is CancellationToken.None.
        :returns: A task that represents the asynchronous append operation.
        """
        ...

    @staticmethod
    def append_text(path: str) -> System.IO.StreamWriter:
        ...

    @staticmethod
    @overload
    def copy(source_file_name: str, dest_file_name: str) -> None:
        """
        Copies an existing file to a new file.
        An exception is raised if the destination file already exists.
        """
        ...

    @staticmethod
    @overload
    def copy(source_file_name: str, dest_file_name: str, overwrite: bool) -> None:
        """
        Copies an existing file to a new file.
        If  is false, an exception will be
        raised if the destination exists. Otherwise it will be overwritten.
        """
        ...

    @staticmethod
    @overload
    def create(path: str) -> System.IO.FileStream:
        ...

    @staticmethod
    @overload
    def create(path: str, buffer_size: int) -> System.IO.FileStream:
        ...

    @staticmethod
    @overload
    def create(path: str, buffer_size: int, options: System.IO.FileOptions) -> System.IO.FileStream:
        ...

    @staticmethod
    def create_symbolic_link(path: str, path_to_target: str) -> System.IO.FileSystemInfo:
        """
        Creates a file symbolic link identified by  that points to .
        
        :param path: The path where the symbolic link should be created.
        :param path_to_target: The path of the target to which the symbolic link points.
        :returns: A FileInfo instance that wraps the newly created file symbolic link.
        """
        ...

    @staticmethod
    def create_text(path: str) -> System.IO.StreamWriter:
        ...

    @staticmethod
    def decrypt(path: str) -> None:
        ...

    @staticmethod
    def delete(path: str) -> None:
        ...

    @staticmethod
    def encrypt(path: str) -> None:
        ...

    @staticmethod
    def exists(path: str) -> bool:
        ...

    @staticmethod
    @overload
    def get_attributes(path: str) -> System.IO.FileAttributes:
        ...

    @staticmethod
    @overload
    def get_attributes(file_handle: Microsoft.Win32.SafeHandles.SafeFileHandle) -> System.IO.FileAttributes:
        """
        Gets the specified FileAttributes of the file or directory associated to
        
        :param file_handle: A SafeFileHandle to the file or directory for which the attributes are to be retrieved.
        :returns: The FileAttributes of the file or directory.
        """
        ...

    @staticmethod
    @overload
    def get_creation_time(path: str) -> datetime.datetime:
        ...

    @staticmethod
    @overload
    def get_creation_time(file_handle: Microsoft.Win32.SafeHandles.SafeFileHandle) -> datetime.datetime:
        """
        Returns the creation date and time of the specified file or directory.
        
        :param file_handle: A SafeFileHandle to the file or directory for which to obtain creation date and time information.
        :returns: A DateTime structure set to the creation date and time for the specified file or directory. This value is expressed in local time.
        """
        ...

    @staticmethod
    @overload
    def get_creation_time_utc(path: str) -> datetime.datetime:
        ...

    @staticmethod
    @overload
    def get_creation_time_utc(file_handle: Microsoft.Win32.SafeHandles.SafeFileHandle) -> datetime.datetime:
        """
        Returns the creation date and time, in coordinated universal time (UTC), of the specified file or directory.
        
        :param file_handle: A SafeFileHandle to the file or directory for which to obtain creation date and time information.
        :returns: A DateTime structure set to the creation date and time for the specified file or directory. This value is expressed in UTC time.
        """
        ...

    @staticmethod
    @overload
    def get_last_access_time(path: str) -> datetime.datetime:
        ...

    @staticmethod
    @overload
    def get_last_access_time(file_handle: Microsoft.Win32.SafeHandles.SafeFileHandle) -> datetime.datetime:
        """
        Returns the last access date and time of the specified file or directory.
        
        :param file_handle: A SafeFileHandle to the file or directory for which to obtain last access date and time information.
        :returns: A DateTime structure set to the last access date and time for the specified file or directory. This value is expressed in local time.
        """
        ...

    @staticmethod
    @overload
    def get_last_access_time_utc(path: str) -> datetime.datetime:
        ...

    @staticmethod
    @overload
    def get_last_access_time_utc(file_handle: Microsoft.Win32.SafeHandles.SafeFileHandle) -> datetime.datetime:
        """
        Returns the last access date and time, in coordinated universal time (UTC), of the specified file or directory.
        
        :param file_handle: A SafeFileHandle to the file or directory for which to obtain last access date and time information.
        :returns: A DateTime structure set to the last access date and time for the specified file or directory. This value is expressed in UTC time.
        """
        ...

    @staticmethod
    @overload
    def get_last_write_time(path: str) -> datetime.datetime:
        ...

    @staticmethod
    @overload
    def get_last_write_time(file_handle: Microsoft.Win32.SafeHandles.SafeFileHandle) -> datetime.datetime:
        """
        Returns the last write date and time of the specified file or directory.
        
        :param file_handle: A SafeFileHandle to the file or directory for which to obtain last write date and time information.
        :returns: A DateTime structure set to the last write date and time for the specified file or directory. This value is expressed in local time.
        """
        ...

    @staticmethod
    @overload
    def get_last_write_time_utc(path: str) -> datetime.datetime:
        ...

    @staticmethod
    @overload
    def get_last_write_time_utc(file_handle: Microsoft.Win32.SafeHandles.SafeFileHandle) -> datetime.datetime:
        """
        Returns the last write date and time, in coordinated universal time (UTC), of the specified file or directory.
        
        :param file_handle: A SafeFileHandle to the file or directory for which to obtain last write date and time information.
        :returns: A DateTime structure set to the last write date and time for the specified file or directory. This value is expressed in UTC time.
        """
        ...

    @staticmethod
    @overload
    def get_unix_file_mode(path: str) -> System.IO.UnixFileMode:
        """
        Gets the System.IO.UnixFileMode of the file on the path.
        
        :param path: The path to the file.
        :returns: The System.IO.UnixFileMode of the file on the path.
        """
        ...

    @staticmethod
    @overload
    def get_unix_file_mode(file_handle: Microsoft.Win32.SafeHandles.SafeFileHandle) -> System.IO.UnixFileMode:
        """
        Gets the System.IO.UnixFileMode of the specified file handle.
        
        :param file_handle: The file handle.
        :returns: The System.IO.UnixFileMode of the file handle.
        """
        ...

    @staticmethod
    @overload
    def move(source_file_name: str, dest_file_name: str) -> None:
        ...

    @staticmethod
    @overload
    def move(source_file_name: str, dest_file_name: str, overwrite: bool) -> None:
        ...

    @staticmethod
    @overload
    def open(path: str, options: System.IO.FileStreamOptions) -> System.IO.FileStream:
        """Initializes a new instance of the FileStream class with the specified path, creation mode, read/write and sharing permission, the access other FileStreams can have to the same file, the buffer size, additional file options and the allocation size."""
        ...

    @staticmethod
    @overload
    def open(path: str, mode: System.IO.FileMode) -> System.IO.FileStream:
        ...

    @staticmethod
    @overload
    def open(path: str, mode: System.IO.FileMode, access: System.IO.FileAccess) -> System.IO.FileStream:
        ...

    @staticmethod
    @overload
    def open(path: str, mode: System.IO.FileMode, access: System.IO.FileAccess, share: System.IO.FileShare) -> System.IO.FileStream:
        ...

    @staticmethod
    def open_handle(path: str, mode: System.IO.FileMode = ..., access: System.IO.FileAccess = ..., share: System.IO.FileShare = ..., options: System.IO.FileOptions = ..., preallocation_size: int = 0) -> Microsoft.Win32.SafeHandles.SafeFileHandle:
        """
        Initializes a new instance of the SafeFileHandle class with the specified path, creation mode, read/write and sharing permission, the access other SafeFileHandles can have to the same file, additional file options and the allocation size.
        
        :param path: A relative or absolute path for the file that the current SafeFileHandle instance will encapsulate.
        :param mode: One of the enumeration values that determines how to open or create the file. The default value is FileMode.Open
        :param access: A bitwise combination of the enumeration values that determines how the file can be accessed. The default value is FileAccess.Read
        :param share: A bitwise combination of the enumeration values that determines how the file will be shared by processes. The default value is FileShare.Read.
        :param options: An object that describes optional SafeFileHandle parameters to use.
        :param preallocation_size: The initial allocation size in bytes for the file. A positive value is effective only when a regular file is being created, overwritten, or replaced. Negative values are not allowed. In other cases (including the default 0 value), it's ignored.
        """
        ...

    @staticmethod
    def open_read(path: str) -> System.IO.FileStream:
        ...

    @staticmethod
    def open_text(path: str) -> System.IO.StreamReader:
        ...

    @staticmethod
    def open_write(path: str) -> System.IO.FileStream:
        ...

    @staticmethod
    def read_all_bytes(path: str) -> typing.List[int]:
        ...

    @staticmethod
    def read_all_bytes_async(path: str, cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task[typing.List[int]]:
        ...

    @staticmethod
    @overload
    def read_all_lines(path: str) -> typing.List[str]:
        ...

    @staticmethod
    @overload
    def read_all_lines(path: str, encoding: System.Text.Encoding) -> typing.List[str]:
        ...

    @staticmethod
    @overload
    def read_all_lines_async(path: str, cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task[typing.List[str]]:
        ...

    @staticmethod
    @overload
    def read_all_lines_async(path: str, encoding: System.Text.Encoding, cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task[typing.List[str]]:
        ...

    @staticmethod
    @overload
    def read_all_text(path: str) -> str:
        ...

    @staticmethod
    @overload
    def read_all_text(path: str, encoding: System.Text.Encoding) -> str:
        ...

    @staticmethod
    @overload
    def read_all_text_async(path: str, cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task[str]:
        ...

    @staticmethod
    @overload
    def read_all_text_async(path: str, encoding: System.Text.Encoding, cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task[str]:
        ...

    @staticmethod
    @overload
    def read_lines(path: str) -> System.Collections.Generic.IEnumerable[str]:
        ...

    @staticmethod
    @overload
    def read_lines(path: str, encoding: System.Text.Encoding) -> System.Collections.Generic.IEnumerable[str]:
        ...

    @staticmethod
    @overload
    def read_lines_async(path: str, cancellation_token: System.Threading.CancellationToken = ...) -> System.Collections.Generic.IAsyncEnumerable[str]:
        """
        Asynchronously reads the lines of a file.
        
        :param path: The file to read.
        :param cancellation_token: The token to monitor for cancellation requests. The default value is CancellationToken.None.
        :returns: The async enumerable that represents all the lines of the file, or the lines that are the result of a query.
        """
        ...

    @staticmethod
    @overload
    def read_lines_async(path: str, encoding: System.Text.Encoding, cancellation_token: System.Threading.CancellationToken = ...) -> System.Collections.Generic.IAsyncEnumerable[str]:
        """
        Asynchronously reads the lines of a file that has a specified encoding.
        
        :param path: The file to read.
        :param encoding: The encoding that is applied to the contents of the file.
        :param cancellation_token: The token to monitor for cancellation requests. The default value is CancellationToken.None.
        :returns: The async enumerable that represents all the lines of the file, or the lines that are the result of a query.
        """
        ...

    @staticmethod
    @overload
    def replace(source_file_name: str, destination_file_name: str, destination_backup_file_name: str) -> None:
        ...

    @staticmethod
    @overload
    def replace(source_file_name: str, destination_file_name: str, destination_backup_file_name: str, ignore_metadata_errors: bool) -> None:
        ...

    @staticmethod
    def resolve_link_target(link_path: str, return_final_target: bool) -> System.IO.FileSystemInfo:
        """
        Gets the target of the specified file link.
        
        :param link_path: The path of the file link.
        :param return_final_target: true to follow links to the final target; false to return the immediate next link.
        :returns: A FileInfo instance if  exists, independently if the target exists or not. null if  is not a link.
        """
        ...

    @staticmethod
    @overload
    def set_attributes(path: str, file_attributes: System.IO.FileAttributes) -> None:
        ...

    @staticmethod
    @overload
    def set_attributes(file_handle: Microsoft.Win32.SafeHandles.SafeFileHandle, file_attributes: System.IO.FileAttributes) -> None:
        """
        Sets the specified FileAttributes of the file or directory associated to .
        
        :param file_handle: A SafeFileHandle to the file or directory for which  should be set.
        :param file_attributes: A bitwise combination of the enumeration values.
        """
        ...

    @staticmethod
    @overload
    def set_creation_time(path: str, creation_time: typing.Union[datetime.datetime, datetime.date]) -> None:
        ...

    @staticmethod
    @overload
    def set_creation_time(file_handle: Microsoft.Win32.SafeHandles.SafeFileHandle, creation_time: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Sets the date and time the file or directory was created.
        
        :param file_handle: A SafeFileHandle to the file or directory for which to set the creation date and time information.
        :param creation_time: A DateTime containing the value to set for the creation date and time of . This value is expressed in local time.
        """
        ...

    @staticmethod
    @overload
    def set_creation_time_utc(path: str, creation_time_utc: typing.Union[datetime.datetime, datetime.date]) -> None:
        ...

    @staticmethod
    @overload
    def set_creation_time_utc(file_handle: Microsoft.Win32.SafeHandles.SafeFileHandle, creation_time_utc: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Sets the date and time, in coordinated universal time (UTC), that the file or directory was created.
        
        :param file_handle: A SafeFileHandle to the file or directory for which to set the creation date and time information.
        :param creation_time_utc: A DateTime containing the value to set for the creation date and time of . This value is expressed in UTC time.
        """
        ...

    @staticmethod
    @overload
    def set_last_access_time(path: str, last_access_time: typing.Union[datetime.datetime, datetime.date]) -> None:
        ...

    @staticmethod
    @overload
    def set_last_access_time(file_handle: Microsoft.Win32.SafeHandles.SafeFileHandle, last_access_time: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Sets the date and time the specified file or directory was last accessed.
        
        :param file_handle: A SafeFileHandle to the file or directory for which to set the last access date and time information.
        :param last_access_time: A DateTime containing the value to set for the last access date and time of . This value is expressed in local time.
        """
        ...

    @staticmethod
    @overload
    def set_last_access_time_utc(path: str, last_access_time_utc: typing.Union[datetime.datetime, datetime.date]) -> None:
        ...

    @staticmethod
    @overload
    def set_last_access_time_utc(file_handle: Microsoft.Win32.SafeHandles.SafeFileHandle, last_access_time_utc: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Sets the date and time, in coordinated universal time (UTC), that the specified file or directory was last accessed.
        
        :param file_handle: A SafeFileHandle to the file or directory for which to set the last access date and time information.
        :param last_access_time_utc: A DateTime containing the value to set for the last access date and time of . This value is expressed in UTC time.
        """
        ...

    @staticmethod
    @overload
    def set_last_write_time(path: str, last_write_time: typing.Union[datetime.datetime, datetime.date]) -> None:
        ...

    @staticmethod
    @overload
    def set_last_write_time(file_handle: Microsoft.Win32.SafeHandles.SafeFileHandle, last_write_time: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Sets the date and time that the specified file or directory was last written to.
        
        :param file_handle: A SafeFileHandle to the file or directory for which to set the last write date and time information.
        :param last_write_time: A DateTime containing the value to set for the last write date and time of . This value is expressed in local time.
        """
        ...

    @staticmethod
    @overload
    def set_last_write_time_utc(path: str, last_write_time_utc: typing.Union[datetime.datetime, datetime.date]) -> None:
        ...

    @staticmethod
    @overload
    def set_last_write_time_utc(file_handle: Microsoft.Win32.SafeHandles.SafeFileHandle, last_write_time_utc: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Sets the date and time, in coordinated universal time (UTC), that the specified file or directory was last written to.
        
        :param file_handle: A SafeFileHandle to the file or directory for which to set the last write date and time information.
        :param last_write_time_utc: A DateTime containing the value to set for the last write date and time of . This value is expressed in UTC time.
        """
        ...

    @staticmethod
    @overload
    def set_unix_file_mode(path: str, mode: System.IO.UnixFileMode) -> None:
        """
        Sets the specified System.IO.UnixFileMode of the file on the specified path.
        
        :param path: The path to the file.
        :param mode: The unix file mode.
        """
        ...

    @staticmethod
    @overload
    def set_unix_file_mode(file_handle: Microsoft.Win32.SafeHandles.SafeFileHandle, mode: System.IO.UnixFileMode) -> None:
        """
        Sets the specified System.IO.UnixFileMode of the specified file handle.
        
        :param file_handle: The file handle.
        :param mode: The unix file mode.
        """
        ...

    @staticmethod
    @overload
    def write_all_bytes(path: str, bytes: typing.List[int]) -> None:
        ...

    @staticmethod
    @overload
    def write_all_bytes(path: str, bytes: System.ReadOnlySpan[int]) -> None:
        """
        Creates a new file, writes the specified byte array to the file, and then closes the file. If the target file already exists, it is truncated and overwritten.
        
        :param path: The file to write to.
        :param bytes: The bytes to write to the file.
        """
        ...

    @staticmethod
    @overload
    def write_all_bytes_async(path: str, bytes: typing.List[int], cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        ...

    @staticmethod
    @overload
    def write_all_bytes_async(path: str, bytes: System.ReadOnlyMemory[int], cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        """
        Asynchronously creates a new file, writes the specified byte array to the file, and then closes the file. If the target file already exists, it is truncated and overwritten.
        
        :param path: The file to write to.
        :param bytes: The bytes to write to the file.
        :param cancellation_token: The token to monitor for cancellation requests. The default value is CancellationToken.None.
        :returns: A task that represents the asynchronous write operation.
        """
        ...

    @staticmethod
    @overload
    def write_all_lines(path: str, contents: typing.List[str]) -> None:
        ...

    @staticmethod
    @overload
    def write_all_lines(path: str, contents: System.Collections.Generic.IEnumerable[str]) -> None:
        ...

    @staticmethod
    @overload
    def write_all_lines(path: str, contents: typing.List[str], encoding: System.Text.Encoding) -> None:
        ...

    @staticmethod
    @overload
    def write_all_lines(path: str, contents: System.Collections.Generic.IEnumerable[str], encoding: System.Text.Encoding) -> None:
        ...

    @staticmethod
    @overload
    def write_all_lines_async(path: str, contents: System.Collections.Generic.IEnumerable[str], cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        ...

    @staticmethod
    @overload
    def write_all_lines_async(path: str, contents: System.Collections.Generic.IEnumerable[str], encoding: System.Text.Encoding, cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        ...

    @staticmethod
    @overload
    def write_all_text(path: str, contents: str) -> None:
        ...

    @staticmethod
    @overload
    def write_all_text(path: str, contents: System.ReadOnlySpan[str]) -> None:
        """
        Creates a new file, writes the specified string to the file, and then closes the file.
        If the target file already exists, it is truncated and overwritten.
        
        :param path: The file to write to.
        :param contents: The characters to write to the file.
        """
        ...

    @staticmethod
    @overload
    def write_all_text(path: str, contents: str, encoding: System.Text.Encoding) -> None:
        ...

    @staticmethod
    @overload
    def write_all_text(path: str, contents: System.ReadOnlySpan[str], encoding: System.Text.Encoding) -> None:
        """
        Creates a new file, writes the specified string to the file using the specified encoding, and then closes the file.
        If the target file already exists, it is truncated and overwritten.
        
        :param path: The file to write to.
        :param contents: The characters to write to the file.
        :param encoding: The encoding to apply to the string.
        """
        ...

    @staticmethod
    @overload
    def write_all_text_async(path: str, contents: str, cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        ...

    @staticmethod
    @overload
    def write_all_text_async(path: str, contents: System.ReadOnlyMemory[str], cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        """
        Asynchronously creates a new file, writes the specified string to the file, and then closes the file.
        If the target file already exists, it is truncated and overwritten.
        
        :param path: The file to write to.
        :param contents: The characters to write to the file.
        :param cancellation_token: The token to monitor for cancellation requests. The default value is CancellationToken.None.
        :returns: A task that represents the asynchronous write operation.
        """
        ...

    @staticmethod
    @overload
    def write_all_text_async(path: str, contents: str, encoding: System.Text.Encoding, cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        ...

    @staticmethod
    @overload
    def write_all_text_async(path: str, contents: System.ReadOnlyMemory[str], encoding: System.Text.Encoding, cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        """
        Asynchronously creates a new file, writes the specified string to the file using the specified encoding, and then closes the file.
        If the target file already exists, it is truncated and overwritten.
        
        :param path: The file to write to.
        :param contents: The characters to write to the file.
        :param encoding: The encoding to apply to the string.
        :param cancellation_token: The token to monitor for cancellation requests. The default value is CancellationToken.None.
        :returns: A task that represents the asynchronous write operation.
        """
        ...


class StringReader(System.IO.TextReader):
    """This class has no documentation."""

    def __init__(self, s: str) -> None:
        ...

    def close(self) -> None:
        ...

    def dispose(self, disposing: bool) -> None:
        """This method is protected."""
        ...

    def peek(self) -> int:
        ...

    @overload
    def read(self) -> int:
        ...

    @overload
    def read(self, buffer: typing.List[str], index: int, count: int) -> int:
        ...

    @overload
    def read(self, buffer: System.Span[str]) -> int:
        ...

    @overload
    def read_async(self, buffer: typing.List[str], index: int, count: int) -> System.Threading.Tasks.Task[int]:
        ...

    @overload
    def read_async(self, buffer: System.Memory[str], cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.ValueTask[int]:
        ...

    def read_block(self, buffer: System.Span[str]) -> int:
        ...

    @overload
    def read_block_async(self, buffer: typing.List[str], index: int, count: int) -> System.Threading.Tasks.Task[int]:
        ...

    @overload
    def read_block_async(self, buffer: System.Memory[str], cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.ValueTask[int]:
        ...

    def read_line(self) -> str:
        ...

    @overload
    def read_line_async(self) -> System.Threading.Tasks.Task[str]:
        ...

    @overload
    def read_line_async(self, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.ValueTask[str]:
        """
        Reads a line of characters asynchronously from the current string and returns the data as a string.
        
        :param cancellation_token: The token to monitor for cancellation requests.
        :returns: A value task that represents the asynchronous read operation. The value of the TResult parameter contains the next line from the string reader, or is null if all of the characters have been read.
        """
        ...

    def read_to_end(self) -> str:
        ...

    @overload
    def read_to_end_async(self) -> System.Threading.Tasks.Task[str]:
        ...

    @overload
    def read_to_end_async(self, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task[str]:
        """
        Reads all characters from the current position to the end of the string asynchronously and returns them as a single string.
        
        :param cancellation_token: The token to monitor for cancellation requests.
        :returns: A task that represents the asynchronous read operation. The value of the TResult parameter contains a string with the characters from the current position to the end of the string.
        """
        ...


class IOException(System.SystemException):
    """This class has no documentation."""

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, message: str) -> None:
        ...

    @overload
    def __init__(self, message: str, hresult: int) -> None:
        ...

    @overload
    def __init__(self, message: str, inner_exception: System.Exception) -> None:
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """
        This method is protected.
        
        Obsoletions.LegacyFormatterImplMessage
        """
        ...


class PathTooLongException(System.IO.IOException):
    """This class has no documentation."""

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, message: str) -> None:
        ...

    @overload
    def __init__(self, message: str, inner_exception: System.Exception) -> None:
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """
        This method is protected.
        
        Obsoletions.LegacyFormatterImplMessage
        """
        ...


class UnmanagedMemoryAccessor(System.Object, System.IDisposable):
    """Provides random access to unmanaged blocks of memory from managed code."""

    @property
    def capacity(self) -> int:
        ...

    @property
    def can_read(self) -> bool:
        ...

    @property
    def can_write(self) -> bool:
        ...

    @property
    def is_open(self) -> bool:
        """This property is protected."""
        ...

    @overload
    def __init__(self) -> None:
        """This method is protected."""
        ...

    @overload
    def __init__(self, buffer: System.Runtime.InteropServices.SafeBuffer, offset: int, capacity: int) -> None:
        ...

    @overload
    def __init__(self, buffer: System.Runtime.InteropServices.SafeBuffer, offset: int, capacity: int, access: System.IO.FileAccess) -> None:
        ...

    @overload
    def dispose(self, disposing: bool) -> None:
        """This method is protected."""
        ...

    @overload
    def dispose(self) -> None:
        ...

    def initialize(self, buffer: System.Runtime.InteropServices.SafeBuffer, offset: int, capacity: int, access: System.IO.FileAccess) -> None:
        """This method is protected."""
        ...

    def read_boolean(self, position: int) -> bool:
        ...

    def read_byte(self, position: int) -> int:
        ...

    def read_char(self, position: int) -> str:
        ...

    def read_decimal(self, position: int) -> float:
        ...

    def read_double(self, position: int) -> float:
        ...

    def read_int_16(self, position: int) -> int:
        ...

    def read_int_32(self, position: int) -> int:
        ...

    def read_int_64(self, position: int) -> int:
        ...

    def read_s_byte(self, position: int) -> int:
        ...

    def read_single(self, position: int) -> float:
        ...

    def read_u_int_16(self, position: int) -> int:
        ...

    def read_u_int_32(self, position: int) -> int:
        ...

    def read_u_int_64(self, position: int) -> int:
        ...

    @overload
    def write(self, position: int, value: bool) -> None:
        ...

    @overload
    def write(self, position: int, value: int) -> None:
        ...

    @overload
    def write(self, position: int, value: str) -> None:
        ...

    @overload
    def write(self, position: int, value: float) -> None:
        ...


class UnmanagedMemoryStream(System.IO.Stream):
    """Stream over a memory pointer or over a SafeBuffer"""

    @property
    def can_read(self) -> bool:
        """Returns true if the stream can be read; otherwise returns false."""
        ...

    @property
    def can_seek(self) -> bool:
        """Returns true if the stream can seek; otherwise returns false."""
        ...

    @property
    def can_write(self) -> bool:
        """Returns true if the stream can be written to; otherwise returns false."""
        ...

    @property
    def length(self) -> int:
        """Number of bytes in the stream."""
        ...

    @property
    def capacity(self) -> int:
        """Number of bytes that can be written to the stream."""
        ...

    @property
    def position(self) -> int:
        """ReadByte will read byte at the Position in the stream"""
        ...

    @position.setter
    def position(self, value: int) -> None:
        ...

    @property
    def position_pointer(self) -> typing.Any:
        """Pointer to memory at the current Position in the stream."""
        ...

    @position_pointer.setter
    def position_pointer(self, value: typing.Any) -> None:
        ...

    @overload
    def __init__(self, pointer: typing.Any, length: int) -> None:
        """Creates a stream over a byte*."""
        ...

    @overload
    def __init__(self, pointer: typing.Any, length: int, capacity: int, access: System.IO.FileAccess) -> None:
        """Creates a stream over a byte*."""
        ...

    @overload
    def __init__(self) -> None:
        """
        Creates a closed stream.
        
        This method is protected.
        """
        ...

    @overload
    def __init__(self, buffer: System.Runtime.InteropServices.SafeBuffer, offset: int, length: int) -> None:
        """Creates a stream over a SafeBuffer."""
        ...

    @overload
    def __init__(self, buffer: System.Runtime.InteropServices.SafeBuffer, offset: int, length: int, access: System.IO.FileAccess) -> None:
        """Creates a stream over a SafeBuffer."""
        ...

    def dispose(self, disposing: bool) -> None:
        """
        Closes the stream. The stream's memory needs to be dealt with separately.
        
        This method is protected.
        """
        ...

    def flush(self) -> None:
        """Since it's a memory stream, this method does nothing."""
        ...

    def flush_async(self, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        """Since it's a memory stream, this method does nothing specific."""
        ...

    @overload
    def initialize(self, pointer: typing.Any, length: int, capacity: int, access: System.IO.FileAccess) -> None:
        """
        Subclasses must call this method (or the other overload) to properly initialize all instance fields.
        
        This method is protected.
        """
        ...

    @overload
    def initialize(self, buffer: System.Runtime.InteropServices.SafeBuffer, offset: int, length: int, access: System.IO.FileAccess) -> None:
        """
        Subclasses must call this method (or the other overload) to properly initialize all instance fields.
        
        This method is protected.
        """
        ...

    @overload
    def read(self, buffer: typing.List[int], offset: int, count: int) -> int:
        """
        Reads bytes from stream and puts them into the buffer
        
        :param buffer: Buffer to read the bytes to.
        :param offset: Starting index in the buffer.
        :param count: Maximum number of bytes to read.
        :returns: Number of bytes actually read.
        """
        ...

    @overload
    def read(self, buffer: System.Span[int]) -> int:
        ...

    @overload
    def read_async(self, buffer: typing.List[int], offset: int, count: int, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task[int]:
        """
        Reads bytes from stream and puts them into the buffer
        
        :param buffer: Buffer to read the bytes to.
        :param offset: Starting index in the buffer.
        :param count: Maximum number of bytes to read.
        :param cancellation_token: Token that can be used to cancel this operation.
        :returns: Task that can be used to access the number of bytes actually read.
        """
        ...

    @overload
    def read_async(self, buffer: System.Memory[int], cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.ValueTask[int]:
        """
        Reads bytes from stream and puts them into the buffer
        
        :param buffer: Buffer to read the bytes to.
        :param cancellation_token: Token that can be used to cancel this operation.
        """
        ...

    def read_byte(self) -> int:
        """Returns the byte at the stream current Position and advances the Position."""
        ...

    def seek(self, offset: int, loc: System.IO.SeekOrigin) -> int:
        """
        Advanced the Position to specific location in the stream.
        
        :param offset: Offset from the loc parameter.
        :param loc: Origin for the offset parameter.
        """
        ...

    def set_length(self, value: int) -> None:
        """Sets the Length of the stream."""
        ...

    @overload
    def write(self, buffer: typing.List[int], offset: int, count: int) -> None:
        """
        Writes buffer into the stream
        
        :param buffer: Buffer that will be written.
        :param offset: Starting index in the buffer.
        :param count: Number of bytes to write.
        """
        ...

    @overload
    def write(self, buffer: System.ReadOnlySpan[int]) -> None:
        ...

    @overload
    def write_async(self, buffer: typing.List[int], offset: int, count: int, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        """
        Writes buffer into the stream. The operation completes synchronously.
        
        :param buffer: Buffer that will be written.
        :param offset: Starting index in the buffer.
        :param count: Number of bytes to write.
        :param cancellation_token: Token that can be used to cancel the operation.
        :returns: Task that can be awaited.
        """
        ...

    @overload
    def write_async(self, buffer: System.ReadOnlyMemory[int], cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.ValueTask:
        """
        Writes buffer into the stream. The operation completes synchronously.
        
        :param buffer: Buffer that will be written.
        :param cancellation_token: Token that can be used to cancel the operation.
        """
        ...

    def write_byte(self, value: int) -> None:
        """Writes a byte to the stream and advances the current Position."""
        ...


class FileLoadException(System.IO.IOException):
    """This class has no documentation."""

    @property
    def message(self) -> str:
        ...

    @property
    def file_name(self) -> str:
        ...

    @property
    def fusion_log(self) -> str:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, message: str) -> None:
        ...

    @overload
    def __init__(self, message: str, inner: System.Exception) -> None:
        ...

    @overload
    def __init__(self, message: str, file_name: str) -> None:
        ...

    @overload
    def __init__(self, message: str, file_name: str, inner: System.Exception) -> None:
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """
        This method is protected.
        
        Obsoletions.LegacyFormatterImplMessage
        """
        ...

    def get_object_data(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """Obsoletions.LegacyFormatterImplMessage"""
        warnings.warn("Obsoletions.LegacyFormatterImplMessage", DeprecationWarning)

    def to_string(self) -> str:
        ...


class StringWriter(System.IO.TextWriter):
    """This class has no documentation."""

    @property
    def encoding(self) -> System.Text.Encoding:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, format_provider: System.IFormatProvider) -> None:
        ...

    @overload
    def __init__(self, sb: System.Text.StringBuilder) -> None:
        ...

    @overload
    def __init__(self, sb: System.Text.StringBuilder, format_provider: System.IFormatProvider) -> None:
        ...

    def close(self) -> None:
        ...

    def dispose(self, disposing: bool) -> None:
        """This method is protected."""
        ...

    def flush_async(self) -> System.Threading.Tasks.Task:
        ...

    def get_string_builder(self) -> System.Text.StringBuilder:
        ...

    def to_string(self) -> str:
        ...

    @overload
    def write(self, value: str) -> None:
        ...

    @overload
    def write(self, buffer: typing.List[str], index: int, count: int) -> None:
        ...

    @overload
    def write(self, buffer: System.ReadOnlySpan[str]) -> None:
        ...

    @overload
    def write(self, value: System.Text.StringBuilder) -> None:
        ...

    @overload
    def write_async(self, value: str) -> System.Threading.Tasks.Task:
        ...

    @overload
    def write_async(self, buffer: typing.List[str], index: int, count: int) -> System.Threading.Tasks.Task:
        ...

    @overload
    def write_async(self, buffer: System.ReadOnlyMemory[str], cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        ...

    @overload
    def write_async(self, value: System.Text.StringBuilder, cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        ...

    @overload
    def write_line(self, buffer: System.ReadOnlySpan[str]) -> None:
        ...

    @overload
    def write_line(self, value: System.Text.StringBuilder) -> None:
        ...

    @overload
    def write_line_async(self, value: str) -> System.Threading.Tasks.Task:
        ...

    @overload
    def write_line_async(self, value: System.Text.StringBuilder, cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        ...

    @overload
    def write_line_async(self, buffer: typing.List[str], index: int, count: int) -> System.Threading.Tasks.Task:
        ...

    @overload
    def write_line_async(self, buffer: System.ReadOnlyMemory[str], cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        ...


class EndOfStreamException(System.IO.IOException):
    """This class has no documentation."""

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, message: str) -> None:
        ...

    @overload
    def __init__(self, message: str, inner_exception: System.Exception) -> None:
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """
        This method is protected.
        
        Obsoletions.LegacyFormatterImplMessage
        """
        ...


class DirectoryNotFoundException(System.IO.IOException):
    """This class has no documentation."""

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, message: str) -> None:
        ...

    @overload
    def __init__(self, message: str, inner_exception: System.Exception) -> None:
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """
        This method is protected.
        
        Obsoletions.LegacyFormatterImplMessage
        """
        ...


class InvalidDataException(System.SystemException):
    """The exception that is thrown when a data stream is in an invalid format."""

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the InvalidDataException class."""
        ...

    @overload
    def __init__(self, message: str) -> None:
        """
        Initializes a new instance of the InvalidDataException class with a specified error message.
        
        :param message: The error message that explains the reason for the exception.
        """
        ...

    @overload
    def __init__(self, message: str, inner_exception: System.Exception) -> None:
        """
        Initializes a new instance of the InvalidDataException class with a reference to the inner exception that is the cause of this exception.
        
        :param message: The error message that explains the reason for the exception.
        :param inner_exception: The exception that is the cause of the current exception. If the  parameter is not null, the current exception is raised in a catch block that handles the inner exception.
        """
        ...


class BinaryReader(System.Object, System.IDisposable):
    """Reads primitive data types as binary values in a specific encoding."""

    @property
    def base_stream(self) -> System.IO.Stream:
        ...

    @overload
    def __init__(self, input: System.IO.Stream) -> None:
        ...

    @overload
    def __init__(self, input: System.IO.Stream, encoding: System.Text.Encoding) -> None:
        ...

    @overload
    def __init__(self, input: System.IO.Stream, encoding: System.Text.Encoding, leave_open: bool) -> None:
        ...

    def close(self) -> None:
        ...

    @overload
    def dispose(self, disposing: bool) -> None:
        """This method is protected."""
        ...

    @overload
    def dispose(self) -> None:
        ...

    def fill_buffer(self, num_bytes: int) -> None:
        """This method is protected."""
        ...

    def peek_char(self) -> int:
        ...

    @overload
    def read(self) -> int:
        ...

    @overload
    def read(self, buffer: typing.List[str], index: int, count: int) -> int:
        ...

    @overload
    def read(self, buffer: System.Span[str]) -> int:
        ...

    @overload
    def read(self, buffer: typing.List[int], index: int, count: int) -> int:
        ...

    @overload
    def read(self, buffer: System.Span[int]) -> int:
        ...

    def read_7_bit_encoded_int(self) -> int:
        ...

    def read_7_bit_encoded_int_64(self) -> int:
        ...

    def read_boolean(self) -> bool:
        ...

    def read_byte(self) -> int:
        ...

    def read_bytes(self, count: int) -> typing.List[int]:
        ...

    def read_char(self) -> str:
        ...

    def read_chars(self, count: int) -> typing.List[str]:
        ...

    def read_decimal(self) -> float:
        ...

    def read_double(self) -> float:
        ...

    def read_exactly(self, buffer: System.Span[int]) -> None:
        """
        Reads bytes from the current stream and advances the position within the stream until the  is filled.
        
        :param buffer: A region of memory. When this method returns, the contents of this region are replaced by the bytes read from the current stream.
        """
        ...

    def read_half(self) -> System.Half:
        ...

    def read_int_16(self) -> int:
        ...

    def read_int_32(self) -> int:
        ...

    def read_int_64(self) -> int:
        ...

    def read_s_byte(self) -> int:
        ...

    def read_single(self) -> float:
        ...

    def read_string(self) -> str:
        ...

    def read_u_int_16(self) -> int:
        ...

    def read_u_int_32(self) -> int:
        ...

    def read_u_int_64(self) -> int:
        ...


class FileNotFoundException(System.IO.IOException):
    """This class has no documentation."""

    @property
    def message(self) -> str:
        ...

    @property
    def file_name(self) -> str:
        ...

    @property
    def fusion_log(self) -> str:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, message: str) -> None:
        ...

    @overload
    def __init__(self, message: str, inner_exception: System.Exception) -> None:
        ...

    @overload
    def __init__(self, message: str, file_name: str) -> None:
        ...

    @overload
    def __init__(self, message: str, file_name: str, inner_exception: System.Exception) -> None:
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """
        This method is protected.
        
        Obsoletions.LegacyFormatterImplMessage
        """
        ...

    def get_object_data(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """Obsoletions.LegacyFormatterImplMessage"""
        warnings.warn("Obsoletions.LegacyFormatterImplMessage", DeprecationWarning)

    def to_string(self) -> str:
        ...


class BinaryWriter(System.Object, System.IDisposable, System.IAsyncDisposable):
    """This class has no documentation."""

    NULL: System.IO.BinaryWriter = ...

    @property
    def out_stream(self) -> System.IO.Stream:
        """This field is protected."""
        ...

    @out_stream.setter
    def out_stream(self, value: System.IO.Stream) -> None:
        ...

    @property
    def base_stream(self) -> System.IO.Stream:
        ...

    @overload
    def __init__(self) -> None:
        """This method is protected."""
        ...

    @overload
    def __init__(self, output: System.IO.Stream) -> None:
        ...

    @overload
    def __init__(self, output: System.IO.Stream, encoding: System.Text.Encoding) -> None:
        ...

    @overload
    def __init__(self, output: System.IO.Stream, encoding: System.Text.Encoding, leave_open: bool) -> None:
        ...

    def close(self) -> None:
        ...

    @overload
    def dispose(self, disposing: bool) -> None:
        """This method is protected."""
        ...

    @overload
    def dispose(self) -> None:
        ...

    def dispose_async(self) -> System.Threading.Tasks.ValueTask:
        ...

    def flush(self) -> None:
        ...

    def seek(self, offset: int, origin: System.IO.SeekOrigin) -> int:
        ...

    @overload
    def write(self, value: bool) -> None:
        ...

    @overload
    def write(self, value: int) -> None:
        ...

    @overload
    def write(self, buffer: typing.List[int]) -> None:
        ...

    @overload
    def write(self, buffer: typing.List[int], index: int, count: int) -> None:
        ...

    @overload
    def write(self, ch: str) -> None:
        ...

    @overload
    def write(self, chars: typing.List[str]) -> None:
        ...

    @overload
    def write(self, chars: typing.List[str], index: int, count: int) -> None:
        ...

    @overload
    def write(self, value: float) -> None:
        ...

    @overload
    def write(self, value: System.Half) -> None:
        ...

    @overload
    def write(self, value: str) -> None:
        ...

    @overload
    def write(self, buffer: System.ReadOnlySpan[int]) -> None:
        ...

    @overload
    def write(self, chars: System.ReadOnlySpan[str]) -> None:
        ...

    def write_7_bit_encoded_int(self, value: int) -> None:
        ...

    def write_7_bit_encoded_int_64(self, value: int) -> None:
        ...


class MemoryStream(System.IO.Stream):
    """This class has no documentation."""

    @property
    def can_read(self) -> bool:
        ...

    @property
    def can_seek(self) -> bool:
        ...

    @property
    def can_write(self) -> bool:
        ...

    @property
    def capacity(self) -> int:
        ...

    @capacity.setter
    def capacity(self, value: int) -> None:
        ...

    @property
    def length(self) -> int:
        ...

    @property
    def position(self) -> int:
        ...

    @position.setter
    def position(self, value: int) -> None:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, capacity: int) -> None:
        ...

    @overload
    def __init__(self, buffer: typing.List[int]) -> None:
        ...

    @overload
    def __init__(self, buffer: typing.List[int], writable: bool) -> None:
        ...

    @overload
    def __init__(self, buffer: typing.List[int], index: int, count: int) -> None:
        ...

    @overload
    def __init__(self, buffer: typing.List[int], index: int, count: int, writable: bool) -> None:
        ...

    @overload
    def __init__(self, buffer: typing.List[int], index: int, count: int, writable: bool, publicly_visible: bool) -> None:
        ...

    def copy_to(self, destination: System.IO.Stream, buffer_size: int) -> None:
        ...

    def copy_to_async(self, destination: System.IO.Stream, buffer_size: int, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        ...

    def dispose(self, disposing: bool) -> None:
        """This method is protected."""
        ...

    def flush(self) -> None:
        ...

    def flush_async(self, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        ...

    def get_buffer(self) -> typing.List[int]:
        ...

    @overload
    def read(self, buffer: typing.List[int], offset: int, count: int) -> int:
        ...

    @overload
    def read(self, buffer: System.Span[int]) -> int:
        ...

    @overload
    def read_async(self, buffer: typing.List[int], offset: int, count: int, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task[int]:
        ...

    @overload
    def read_async(self, buffer: System.Memory[int], cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.ValueTask[int]:
        ...

    def read_byte(self) -> int:
        ...

    def seek(self, offset: int, loc: System.IO.SeekOrigin) -> int:
        ...

    def set_length(self, value: int) -> None:
        ...

    def to_array(self) -> typing.List[int]:
        ...

    def try_get_buffer(self, buffer: typing.Optional[System.ArraySegment[int]]) -> typing.Tuple[bool, System.ArraySegment[int]]:
        ...

    @overload
    def write(self, buffer: typing.List[int], offset: int, count: int) -> None:
        ...

    @overload
    def write(self, buffer: System.ReadOnlySpan[int]) -> None:
        ...

    @overload
    def write_async(self, buffer: typing.List[int], offset: int, count: int, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        ...

    @overload
    def write_async(self, buffer: System.ReadOnlyMemory[int], cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.ValueTask:
        ...

    def write_byte(self, value: int) -> None:
        ...

    def write_to(self, stream: System.IO.Stream) -> None:
        ...


class HandleInheritability(Enum):
    """Specifies whether the underlying handle is inheritable by child processes."""

    NONE = 0
    """Specifies that the handle is not inheritable by child processes."""

    INHERITABLE = 1
    """Specifies that the handle is inheritable by child processes."""


class Path(System.Object):
    """This class has no documentation."""

    DIRECTORY_SEPARATOR_CHAR: str = ...

    ALT_DIRECTORY_SEPARATOR_CHAR: str = ...

    VOLUME_SEPARATOR_CHAR: str = ...

    PATH_SEPARATOR: str = ...

    INVALID_PATH_CHARS: typing.List[str] = ...
    """Path.InvalidPathChars has been deprecated. Use GetInvalidPathChars or GetInvalidFileNameChars instead."""

    @staticmethod
    def change_extension(path: str, extension: str) -> str:
        ...

    @staticmethod
    @overload
    def combine(path_1: str, path_2: str) -> str:
        ...

    @staticmethod
    @overload
    def combine(path_1: str, path_2: str, path_3: str) -> str:
        ...

    @staticmethod
    @overload
    def combine(path_1: str, path_2: str, path_3: str, path_4: str) -> str:
        ...

    @staticmethod
    @overload
    def combine(*paths: typing.Union[str, typing.Iterable[str]]) -> str:
        ...

    @staticmethod
    @overload
    def ends_in_directory_separator(path: System.ReadOnlySpan[str]) -> bool:
        """Returns true if the path ends in a directory separator."""
        ...

    @staticmethod
    @overload
    def ends_in_directory_separator(path: str) -> bool:
        """Returns true if the path ends in a directory separator."""
        ...

    @staticmethod
    def exists(path: str) -> bool:
        """
        Determines whether the specified file or directory exists.
        
        :param path: The path to check
        :returns: true if the caller has the required permissions and  contains the name of an existing file or directory; otherwise, false. This method also returns false if  is null, an invalid path, or a zero-length string. If the caller does not have sufficient permissions to read the specified path, no exception is thrown and the method returns false regardless of the existence of .
        """
        ...

    @staticmethod
    @overload
    def get_directory_name(path: str) -> str:
        """
        Returns the directory portion of a file path. This method effectively
        removes the last segment of the given file path, i.e. it returns a
        string consisting of all characters up to but not including the last
        backslash ("\\") in the file path. The returned value is null if the
        specified path is null, empty, or a root (such as "\\", "C:", or
        "\\\\server\\share").
        """
        ...

    @staticmethod
    @overload
    def get_directory_name(path: System.ReadOnlySpan[str]) -> System.ReadOnlySpan[str]:
        """
        Returns the directory portion of a file path. The returned value is empty
        if the specified path is null, empty, or a root (such as "\\", "C:", or
        "\\\\server\\share").
        """
        ...

    @staticmethod
    @overload
    def get_extension(path: str) -> str:
        """
        Returns the extension of the given path. The returned value includes the period (".") character of the
        extension except when you have a terminal period when you get string.Empty, such as ".exe" or ".cpp".
        The returned value is null if the given path is null or empty if the given path does not include an
        extension.
        """
        ...

    @staticmethod
    @overload
    def get_extension(path: System.ReadOnlySpan[str]) -> System.ReadOnlySpan[str]:
        """Returns the extension of the given path."""
        ...

    @staticmethod
    @overload
    def get_file_name(path: str) -> str:
        """
        Returns the name and extension parts of the given path. The resulting string contains
        the characters of path that follow the last separator in path. The resulting string is
        null if path is null.
        """
        ...

    @staticmethod
    @overload
    def get_file_name(path: System.ReadOnlySpan[str]) -> System.ReadOnlySpan[str]:
        """The returned ReadOnlySpan contains the characters of the path that follows the last separator in path."""
        ...

    @staticmethod
    @overload
    def get_file_name_without_extension(path: str) -> str:
        ...

    @staticmethod
    @overload
    def get_file_name_without_extension(path: System.ReadOnlySpan[str]) -> System.ReadOnlySpan[str]:
        """Returns the characters between the last separator and last (.) in the path."""
        ...

    @staticmethod
    @overload
    def get_full_path(path: str) -> str:
        ...

    @staticmethod
    @overload
    def get_full_path(path: str, base_path: str) -> str:
        ...

    @staticmethod
    def get_invalid_file_name_chars() -> typing.List[str]:
        ...

    @staticmethod
    def get_invalid_path_chars() -> typing.List[str]:
        ...

    @staticmethod
    @overload
    def get_path_root(path: str) -> str:
        ...

    @staticmethod
    @overload
    def get_path_root(path: System.ReadOnlySpan[str]) -> System.ReadOnlySpan[str]:
        ...

    @staticmethod
    def get_random_file_name() -> str:
        """
        Returns a cryptographically strong random 8.3 string that can be
        used as either a folder name or a file name.
        """
        ...

    @staticmethod
    def get_relative_path(relative_to: str, path: str) -> str:
        """
        Create a relative path from one path to another. Paths will be resolved before calculating the difference.
        Default path comparison for the active platform will be used (OrdinalIgnoreCase for Windows or Mac, Ordinal for Unix).
        
        :param relative_to: The source path the output should be relative to. This path is always considered to be a directory.
        :param path: The destination path.
        :returns: The relative path or  if the paths don't share the same root.
        """
        ...

    @staticmethod
    def get_temp_file_name() -> str:
        ...

    @staticmethod
    def get_temp_path() -> str:
        ...

    @staticmethod
    @overload
    def has_extension(path: str) -> bool:
        """
        Tests if a path's file name includes a file extension. A trailing period
        is not considered an extension.
        """
        ...

    @staticmethod
    @overload
    def has_extension(path: System.ReadOnlySpan[str]) -> bool:
        ...

    @staticmethod
    @overload
    def is_path_fully_qualified(path: str) -> bool:
        """
        Returns true if the path is fixed to a specific drive or UNC path. This method does no
        validation of the path (URIs will be returned as relative as a result).
        Returns false if the path specified is relative to the current drive or working directory.
        """
        ...

    @staticmethod
    @overload
    def is_path_fully_qualified(path: System.ReadOnlySpan[str]) -> bool:
        ...

    @staticmethod
    @overload
    def is_path_rooted(path: str) -> bool:
        ...

    @staticmethod
    @overload
    def is_path_rooted(path: System.ReadOnlySpan[str]) -> bool:
        ...

    @staticmethod
    @overload
    def join(path_1: System.ReadOnlySpan[str], path_2: System.ReadOnlySpan[str]) -> str:
        ...

    @staticmethod
    @overload
    def join(path_1: System.ReadOnlySpan[str], path_2: System.ReadOnlySpan[str], path_3: System.ReadOnlySpan[str]) -> str:
        ...

    @staticmethod
    @overload
    def join(path_1: System.ReadOnlySpan[str], path_2: System.ReadOnlySpan[str], path_3: System.ReadOnlySpan[str], path_4: System.ReadOnlySpan[str]) -> str:
        ...

    @staticmethod
    @overload
    def join(path_1: str, path_2: str) -> str:
        ...

    @staticmethod
    @overload
    def join(path_1: str, path_2: str, path_3: str) -> str:
        ...

    @staticmethod
    @overload
    def join(path_1: str, path_2: str, path_3: str, path_4: str) -> str:
        ...

    @staticmethod
    @overload
    def join(*paths: typing.Union[str, typing.Iterable[str]]) -> str:
        ...

    @staticmethod
    @overload
    def trim_ending_directory_separator(path: str) -> str:
        """Trims one trailing directory separator beyond the root of the path."""
        ...

    @staticmethod
    @overload
    def trim_ending_directory_separator(path: System.ReadOnlySpan[str]) -> System.ReadOnlySpan[str]:
        """Trims one trailing directory separator beyond the root of the path."""
        ...

    @staticmethod
    @overload
    def try_join(path_1: System.ReadOnlySpan[str], path_2: System.ReadOnlySpan[str], destination: System.Span[str], chars_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_join(path_1: System.ReadOnlySpan[str], path_2: System.ReadOnlySpan[str], path_3: System.ReadOnlySpan[str], destination: System.Span[str], chars_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...


class Directory(System.Object):
    """This class has no documentation."""

    @staticmethod
    @overload
    def create_directory(path: str) -> System.IO.DirectoryInfo:
        ...

    @staticmethod
    @overload
    def create_directory(path: str, unix_create_mode: System.IO.UnixFileMode) -> System.IO.DirectoryInfo:
        """
        Creates all directories and subdirectories in the specified path with the specified permissions unless they already exist.
        
        :param path: The directory to create.
        :param unix_create_mode: Unix file mode used to create directories.
        :returns: An object that represents the directory at the specified path. This object is returned regardless of whether a directory at the specified path already exists.
        """
        ...

    @staticmethod
    def create_symbolic_link(path: str, path_to_target: str) -> System.IO.FileSystemInfo:
        """
        Creates a directory symbolic link identified by  that points to .
        
        :param path: The absolute path where the symbolic link should be created.
        :param path_to_target: The target directory of the symbolic link.
        :returns: A DirectoryInfo instance that wraps the newly created directory symbolic link.
        """
        ...

    @staticmethod
    def create_temp_subdirectory(prefix: str = None) -> System.IO.DirectoryInfo:
        """
        Creates a uniquely-named, empty directory in the current user's temporary directory.
        
        :param prefix: An optional string to add to the beginning of the subdirectory name.
        :returns: An object that represents the directory that was created.
        """
        ...

    @staticmethod
    @overload
    def delete(path: str) -> None:
        ...

    @staticmethod
    @overload
    def delete(path: str, recursive: bool) -> None:
        ...

    @staticmethod
    @overload
    def enumerate_directories(path: str) -> System.Collections.Generic.IEnumerable[str]:
        ...

    @staticmethod
    @overload
    def enumerate_directories(path: str, search_pattern: str) -> System.Collections.Generic.IEnumerable[str]:
        ...

    @staticmethod
    @overload
    def enumerate_directories(path: str, search_pattern: str, search_option: System.IO.SearchOption) -> System.Collections.Generic.IEnumerable[str]:
        ...

    @staticmethod
    @overload
    def enumerate_directories(path: str, search_pattern: str, enumeration_options: System.IO.EnumerationOptions) -> System.Collections.Generic.IEnumerable[str]:
        ...

    @staticmethod
    @overload
    def enumerate_files(path: str) -> System.Collections.Generic.IEnumerable[str]:
        ...

    @staticmethod
    @overload
    def enumerate_files(path: str, search_pattern: str) -> System.Collections.Generic.IEnumerable[str]:
        ...

    @staticmethod
    @overload
    def enumerate_files(path: str, search_pattern: str, search_option: System.IO.SearchOption) -> System.Collections.Generic.IEnumerable[str]:
        ...

    @staticmethod
    @overload
    def enumerate_files(path: str, search_pattern: str, enumeration_options: System.IO.EnumerationOptions) -> System.Collections.Generic.IEnumerable[str]:
        ...

    @staticmethod
    @overload
    def enumerate_file_system_entries(path: str) -> System.Collections.Generic.IEnumerable[str]:
        ...

    @staticmethod
    @overload
    def enumerate_file_system_entries(path: str, search_pattern: str) -> System.Collections.Generic.IEnumerable[str]:
        ...

    @staticmethod
    @overload
    def enumerate_file_system_entries(path: str, search_pattern: str, search_option: System.IO.SearchOption) -> System.Collections.Generic.IEnumerable[str]:
        ...

    @staticmethod
    @overload
    def enumerate_file_system_entries(path: str, search_pattern: str, enumeration_options: System.IO.EnumerationOptions) -> System.Collections.Generic.IEnumerable[str]:
        ...

    @staticmethod
    def exists(path: str) -> bool:
        ...

    @staticmethod
    def get_creation_time(path: str) -> datetime.datetime:
        ...

    @staticmethod
    def get_creation_time_utc(path: str) -> datetime.datetime:
        ...

    @staticmethod
    def get_current_directory() -> str:
        ...

    @staticmethod
    @overload
    def get_directories(path: str) -> typing.List[str]:
        ...

    @staticmethod
    @overload
    def get_directories(path: str, search_pattern: str) -> typing.List[str]:
        ...

    @staticmethod
    @overload
    def get_directories(path: str, search_pattern: str, search_option: System.IO.SearchOption) -> typing.List[str]:
        ...

    @staticmethod
    @overload
    def get_directories(path: str, search_pattern: str, enumeration_options: System.IO.EnumerationOptions) -> typing.List[str]:
        ...

    @staticmethod
    def get_directory_root(path: str) -> str:
        ...

    @staticmethod
    @overload
    def get_files(path: str) -> typing.List[str]:
        ...

    @staticmethod
    @overload
    def get_files(path: str, search_pattern: str) -> typing.List[str]:
        ...

    @staticmethod
    @overload
    def get_files(path: str, search_pattern: str, search_option: System.IO.SearchOption) -> typing.List[str]:
        ...

    @staticmethod
    @overload
    def get_files(path: str, search_pattern: str, enumeration_options: System.IO.EnumerationOptions) -> typing.List[str]:
        ...

    @staticmethod
    @overload
    def get_file_system_entries(path: str) -> typing.List[str]:
        ...

    @staticmethod
    @overload
    def get_file_system_entries(path: str, search_pattern: str) -> typing.List[str]:
        ...

    @staticmethod
    @overload
    def get_file_system_entries(path: str, search_pattern: str, search_option: System.IO.SearchOption) -> typing.List[str]:
        ...

    @staticmethod
    @overload
    def get_file_system_entries(path: str, search_pattern: str, enumeration_options: System.IO.EnumerationOptions) -> typing.List[str]:
        ...

    @staticmethod
    def get_last_access_time(path: str) -> datetime.datetime:
        ...

    @staticmethod
    def get_last_access_time_utc(path: str) -> datetime.datetime:
        ...

    @staticmethod
    def get_last_write_time(path: str) -> datetime.datetime:
        ...

    @staticmethod
    def get_last_write_time_utc(path: str) -> datetime.datetime:
        ...

    @staticmethod
    def get_logical_drives() -> typing.List[str]:
        ...

    @staticmethod
    def get_parent(path: str) -> System.IO.DirectoryInfo:
        ...

    @staticmethod
    def move(source_dir_name: str, dest_dir_name: str) -> None:
        ...

    @staticmethod
    def resolve_link_target(link_path: str, return_final_target: bool) -> System.IO.FileSystemInfo:
        """
        Gets the target of the specified directory link.
        
        :param link_path: The path of the directory link.
        :param return_final_target: true to follow links to the final target; false to return the immediate next link.
        :returns: A DirectoryInfo instance if  exists, independently if the target exists or not. null if  is not a link.
        """
        ...

    @staticmethod
    def set_creation_time(path: str, creation_time: typing.Union[datetime.datetime, datetime.date]) -> None:
        ...

    @staticmethod
    def set_creation_time_utc(path: str, creation_time_utc: typing.Union[datetime.datetime, datetime.date]) -> None:
        ...

    @staticmethod
    def set_current_directory(path: str) -> None:
        ...

    @staticmethod
    def set_last_access_time(path: str, last_access_time: typing.Union[datetime.datetime, datetime.date]) -> None:
        ...

    @staticmethod
    def set_last_access_time_utc(path: str, last_access_time_utc: typing.Union[datetime.datetime, datetime.date]) -> None:
        ...

    @staticmethod
    def set_last_write_time(path: str, last_write_time: typing.Union[datetime.datetime, datetime.date]) -> None:
        ...

    @staticmethod
    def set_last_write_time_utc(path: str, last_write_time_utc: typing.Union[datetime.datetime, datetime.date]) -> None:
        ...


class BufferedStream(System.IO.Stream):
    """
    One of the design goals here is to prevent the buffer from getting in the way and slowing
    down underlying stream accesses when it is not needed. If you always read & write for sizes
    greater than the internal buffer size, then this class may not even allocate the internal buffer.
    See a large comment in Write for the details of the write buffer heuristic.
    
    This class buffers reads & writes in a shared buffer.
    (If you maintained two buffers separately, one operation would always trash the other buffer
    anyways, so we might as well use one buffer.)
    The assumption here is you will almost always be doing a series of reads or writes, but rarely
    alternate between the two of them on the same stream.
    
    Class Invariants:
    The class has one buffer, shared for reading & writing.
    It can only be used for one or the other at any point in time - not both.
    The following should be true:
    
      * 0 <= _readPos <= _readLen < _bufferSize
      * 0 <= _writePos < _bufferSize
      * _readPos == _readLen && _readPos > 0 implies the read buffer is valid, but we're at the end of the buffer.
      * _readPos == _readLen == 0 means the read buffer contains garbage.
      * Either _writePos can be greater than 0, or _readLen & _readPos can be greater than zero,
        but neither can be greater than zero at the same time.
     
    This class will never cache more bytes than the max specified buffer size.
    However, it may use a temporary buffer of up to twice the size in order to combine several IO operations on
    the underlying stream into a single operation. This is because we assume that memory copies are significantly
    faster than IO operations on the underlying stream (if this was not true, using buffering is never appropriate).
    The max size of this "shadow" buffer is limited as to not allocate it on the LOH.
    Shadowing is always transient. Even when using this technique, this class still guarantees that the number of
    bytes cached (not yet written to the target stream or not yet consumed by the user) is never larger than the
    actual specified buffer size.
    """

    @property
    def underlying_stream(self) -> System.IO.Stream:
        ...

    @property
    def buffer_size(self) -> int:
        ...

    @property
    def can_read(self) -> bool:
        ...

    @property
    def can_write(self) -> bool:
        ...

    @property
    def can_seek(self) -> bool:
        ...

    @property
    def length(self) -> int:
        ...

    @property
    def position(self) -> int:
        ...

    @position.setter
    def position(self, value: int) -> None:
        ...

    @overload
    def __init__(self, stream: System.IO.Stream) -> None:
        ...

    @overload
    def __init__(self, stream: System.IO.Stream, buffer_size: int) -> None:
        ...

    def begin_read(self, buffer: typing.List[int], offset: int, count: int, callback: typing.Callable[[System.IAsyncResult], None], state: typing.Any) -> System.IAsyncResult:
        ...

    def begin_write(self, buffer: typing.List[int], offset: int, count: int, callback: typing.Callable[[System.IAsyncResult], None], state: typing.Any) -> System.IAsyncResult:
        ...

    def copy_to(self, destination: System.IO.Stream, buffer_size: int) -> None:
        ...

    def copy_to_async(self, destination: System.IO.Stream, buffer_size: int, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        ...

    def dispose(self, disposing: bool) -> None:
        """This method is protected."""
        ...

    def dispose_async(self) -> System.Threading.Tasks.ValueTask:
        ...

    def end_read(self, async_result: System.IAsyncResult) -> int:
        ...

    def end_write(self, async_result: System.IAsyncResult) -> None:
        ...

    def flush(self) -> None:
        ...

    def flush_async(self, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        ...

    @overload
    def read(self, buffer: typing.List[int], offset: int, count: int) -> int:
        ...

    @overload
    def read(self, destination: System.Span[int]) -> int:
        ...

    @overload
    def read_async(self, buffer: typing.List[int], offset: int, count: int, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task[int]:
        ...

    @overload
    def read_async(self, buffer: System.Memory[int], cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.ValueTask[int]:
        ...

    def read_byte(self) -> int:
        ...

    def seek(self, offset: int, origin: System.IO.SeekOrigin) -> int:
        ...

    def set_length(self, value: int) -> None:
        ...

    @overload
    def write(self, buffer: typing.List[int], offset: int, count: int) -> None:
        ...

    @overload
    def write(self, buffer: System.ReadOnlySpan[int]) -> None:
        ...

    @overload
    def write_async(self, buffer: typing.List[int], offset: int, count: int, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        ...

    @overload
    def write_async(self, buffer: System.ReadOnlyMemory[int], cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.ValueTask:
        ...

    def write_byte(self, value: int) -> None:
        ...


