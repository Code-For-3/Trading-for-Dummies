from typing import overload
from enum import Enum
import abc
import typing

import System
import System.Collections.Generic
import System.IO
import System.IO.Enumeration
import System.Runtime.ConstrainedExecution

System_IO_Enumeration_FileSystemEnumerator_TResult = typing.TypeVar("System_IO_Enumeration_FileSystemEnumerator_TResult")
System_IO_Enumeration_FileSystemEnumerable_TResult = typing.TypeVar("System_IO_Enumeration_FileSystemEnumerable_TResult")


class FileSystemEntry:
    """Provides a lower level view of FileSystemInfo to help process and filter find results."""

    @property
    def directory(self) -> System.ReadOnlySpan[str]:
        """Gets the full path of the directory this entry resides in."""
        ...

    @property
    def root_directory(self) -> System.ReadOnlySpan[str]:
        """Gets the full path of the root directory used for the enumeration."""
        ...

    @property
    def original_root_directory(self) -> System.ReadOnlySpan[str]:
        """Gets the root directory for the enumeration as specified in the constructor."""
        ...

    @property
    def file_name(self) -> System.ReadOnlySpan[str]:
        """Gets the file name for this entry."""
        ...

    @property
    def attributes(self) -> System.IO.FileAttributes:
        """Gets the attributes for this entry."""
        ...

    @property
    def length(self) -> int:
        """Gets the length of the file, in bytes."""
        ...

    @property
    def creation_time_utc(self) -> System.DateTimeOffset:
        """Gets the creation time for the entry or the oldest available time stamp if the operating system does not support creation time stamps."""
        ...

    @property
    def last_access_time_utc(self) -> System.DateTimeOffset:
        """Gets a datetime offset that represents the last access time in UTC."""
        ...

    @property
    def last_write_time_utc(self) -> System.DateTimeOffset:
        """Gets a datetime offset that represents the last write time in UTC."""
        ...

    @property
    def is_directory(self) -> bool:
        """Gets a value that indicates whether this entry is a directory."""
        ...

    @property
    def is_hidden(self) -> bool:
        """Gets a value that indicates whether the file has the hidden attribute."""
        ...

    def to_file_system_info(self) -> System.IO.FileSystemInfo:
        """
        Converts the value of this instance to a FileSystemInfo.
        
        :returns: The value of this instance as a FileSystemInfo.
        """
        ...

    def to_full_path(self) -> str:
        """
        Returns the full path of the find result.
        
        :returns: A string representing the full path.
        """
        ...

    def to_specified_full_path(self) -> str:
        """
        Returns the full path for the find results, based on the initially provided path.
        
        :returns: A string representing the full path.
        """
        ...


class FileSystemEnumerator(typing.Generic[System_IO_Enumeration_FileSystemEnumerator_TResult], System.Runtime.ConstrainedExecution.CriticalFinalizerObject, System.Collections.Generic.IEnumerator[System_IO_Enumeration_FileSystemEnumerator_TResult], metaclass=abc.ABCMeta):
    """Enumerates the file system elements of the provided type that are being searched and filtered by a FileSystemEnumerable{T}."""

    @property
    def current(self) -> System_IO_Enumeration_FileSystemEnumerator_TResult:
        """Gets the currently visited element."""
        ...

    def __init__(self, directory: str, options: System.IO.EnumerationOptions = None) -> None:
        """
        Encapsulates a find operation.
        
        :param directory: The directory to search in.
        :param options: Enumeration options to use.
        """
        ...

    def continue_on_error(self, error: int) -> bool:
        """
        When overridden in a derived class, returns a value that indicates whether to continue execution or throw the default exception.
        
        This method is protected.
        
        :param error: The native error code.
        :returns: true to continue; false to throw the default exception for the given error.
        """
        ...

    @overload
    def dispose(self) -> None:
        """Releases the resources used by the current instance of the FileSystemEnumerator{T} class."""
        ...

    @overload
    def dispose(self, disposing: bool) -> None:
        """
        When overridden in a derived class, releases the unmanaged resources used by the FileSystemEnumerator{T} class and optionally releases the managed resources.
        
        This method is protected.
        
        :param disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
        """
        ...

    def move_next(self) -> bool:
        """
        Advances the enumerator to the next item of the FileSystemEnumerator{T}.
        
        :returns: true if the enumerator successfully advanced to the next item; false if the end of the enumerator has been passed.
        """
        ...

    def on_directory_finished(self, directory: System.ReadOnlySpan[str]) -> None:
        """
        When overridden in a derived class, this method is called whenever the end of a directory is reached.
        
        This method is protected.
        
        :param directory: The directory path as a read-only span.
        """
        ...

    def reset(self) -> None:
        """Always throws NotSupportedException."""
        ...

    def should_include_entry(self, entry: System.IO.Enumeration.FileSystemEntry) -> bool:
        """
        When overridden in a derived class, determines whether the specified file system entry should be included in the results.
        
        This method is protected.
        
        :param entry: A file system entry reference.
        :returns: true if the specified file system entry should be included in the results; otherwise, false.
        """
        ...

    def should_recurse_into_entry(self, entry: System.IO.Enumeration.FileSystemEntry) -> bool:
        """
        When overridden in a derived class, determines whether the specified file system entry should be recursed.
        
        This method is protected.
        
        :param entry: A file system entry reference.
        :returns: true if the specified directory entry should be recursed into; otherwise, false.
        """
        ...

    def transform_entry(self, entry: System.IO.Enumeration.FileSystemEntry) -> System_IO_Enumeration_FileSystemEnumerator_TResult:
        """
        When overridden in a derived class, generates the result type from the current entry.
        
        This method is protected.
        
        :param entry: A file system entry reference.
        :returns: The result type from the current entry.
        """
        ...


class FileSystemEnumerable(typing.Generic[System_IO_Enumeration_FileSystemEnumerable_TResult], System.Object, System.Collections.Generic.IEnumerable[System_IO_Enumeration_FileSystemEnumerable_TResult], typing.Iterable[System_IO_Enumeration_FileSystemEnumerable_TResult]):
    """Enumerable that allows utilizing custom filter predicates and transform delegates."""

    @property
    def should_include_predicate(self) -> typing.Callable[[System.IO.Enumeration.FileSystemEntry], bool]:
        ...

    @should_include_predicate.setter
    def should_include_predicate(self, value: typing.Callable[[System.IO.Enumeration.FileSystemEntry], bool]) -> None:
        ...

    @property
    def should_recurse_predicate(self) -> typing.Callable[[System.IO.Enumeration.FileSystemEntry], bool]:
        ...

    @should_recurse_predicate.setter
    def should_recurse_predicate(self, value: typing.Callable[[System.IO.Enumeration.FileSystemEntry], bool]) -> None:
        ...

    def __init__(self, directory: str, transform: typing.Callable[[System.IO.Enumeration.FileSystemEntry], System_IO_Enumeration_FileSystemEnumerable_TResult], options: System.IO.EnumerationOptions = None) -> None:
        ...

    def __iter__(self) -> typing.Iterator[System_IO_Enumeration_FileSystemEnumerable_TResult]:
        ...

    def find_predicate(self, entry: System.IO.Enumeration.FileSystemEntry) -> bool:
        """Delegate for filtering out find results."""
        ...

    def find_transform(self, entry: System.IO.Enumeration.FileSystemEntry) -> System_IO_Enumeration_FileSystemEnumerable_TResult:
        """Delegate for transforming raw find data into a result."""
        ...

    def get_enumerator(self) -> System.Collections.Generic.IEnumerator[System_IO_Enumeration_FileSystemEnumerable_TResult]:
        ...


class FileSystemName(System.Object):
    """Provides methods for matching file system names."""

    @staticmethod
    def matches_simple_expression(expression: System.ReadOnlySpan[str], name: System.ReadOnlySpan[str], ignore_case: bool = True) -> bool:
        """
        Verifies whether the given expression matches the given name. Supports the following wildcards: '*' and '?'. The backslash character '\\\\' escapes.
        
        :param expression: The expression to match with.
        :param name: The name to check against the expression.
        :param ignore_case: true to ignore case (default); false if the match should be case-sensitive.
        :returns: true if the given expression matches the given name; otherwise, false.
        """
        ...

    @staticmethod
    def matches_win_32_expression(expression: System.ReadOnlySpan[str], name: System.ReadOnlySpan[str], ignore_case: bool = True) -> bool:
        """
        Verifies whether the given Win32 expression matches the given name. Supports the following wildcards: '*', '?', '<', '>', '"'. The backslash character '\\' escapes.
        
        :param expression: The expression to match with, such as "*.foo".
        :param name: The name to check against the expression.
        :param ignore_case: true to ignore case (default), false if the match should be case-sensitive.
        :returns: true if the given expression matches the given name; otherwise, false.
        """
        ...

    @staticmethod
    def translate_win_32_expression(expression: str) -> str:
        """
        Translates the given Win32 expression. Change '*' and '?' to '<', '>' and '"' to match Win32 behavior.
        
        :param expression: The expression to translate.
        :returns: A string with the translated Win32 expression.
        """
        ...


