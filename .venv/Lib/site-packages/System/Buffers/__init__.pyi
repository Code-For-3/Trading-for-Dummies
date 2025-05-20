from typing import overload
from enum import Enum
import abc
import typing

import System
import System.Buffers
import System.Runtime.InteropServices

System_Buffers_StandardFormat = typing.Any

System_Buffers_SearchValues_T = typing.TypeVar("System_Buffers_SearchValues_T")
System_Buffers_ArrayPool_T = typing.TypeVar("System_Buffers_ArrayPool_T")
System_Buffers_IMemoryOwner_T = typing.TypeVar("System_Buffers_IMemoryOwner_T")
System_Buffers_MemoryManager_T = typing.TypeVar("System_Buffers_MemoryManager_T")


class SearchValues(typing.Generic[System_Buffers_SearchValues_T], System.Object):
    """
    Provides an immutable, read-only set of values optimized for efficient searching.
    Instances are created by SearchValues.Create(ReadOnlySpan{byte}), SearchValues.Create(ReadOnlySpan{char}), or
    SearchValues.Create(ReadOnlySpan{string}, StringComparison).
    """

    def contains(self, value: System_Buffers_SearchValues_T) -> bool:
        """
        Searches for the specified value and returns true if found. If not found, returns false.
        
        :param value: The value to search for.
        """
        ...

    @staticmethod
    @overload
    def create(*values: typing.Union[int, typing.Iterable[int]]) -> System.Buffers.SearchValues[int]:
        """
        Creates an optimized representation of  used for efficient searching.
        
        :param values: The set of values.
        :returns: The optimized representation of  used for efficient searching.
        """
        ...

    @staticmethod
    @overload
    def create(*values: typing.Union[str, typing.Iterable[str]]) -> System.Buffers.SearchValues[str]:
        """
        Creates an optimized representation of  used for efficient searching.
        
        :param values: The set of values.
        :returns: The optimized representation of  used for efficient searching.
        """
        ...

    @staticmethod
    @overload
    def create(values: System.ReadOnlySpan[str], comparison_type: System.StringComparison) -> System.Buffers.SearchValues[str]:
        """
        Creates an optimized representation of  used for efficient searching.
        
        :param values: The set of values.
        :param comparison_type: Specifies whether to use StringComparison.Ordinal or StringComparison.OrdinalIgnoreCase search semantics.
        :returns: The optimized representation of  used for efficient searching.
        """
        ...


class ArrayPool(typing.Generic[System_Buffers_ArrayPool_T], System.Object, metaclass=abc.ABCMeta):
    """Provides a resource pool that enables reusing instances of arrays."""

    SHARED: System.Buffers.ArrayPool[System_Buffers_ArrayPool_T]
    """Retrieves a shared ArrayPool{T} instance."""

    @staticmethod
    @overload
    def create() -> System.Buffers.ArrayPool[System_Buffers_ArrayPool_T]:
        """
        Creates a new ArrayPool{T} instance using default configuration options.
        
        :returns: A new ArrayPool{T} instance.
        """
        ...

    @staticmethod
    @overload
    def create(max_array_length: int, max_arrays_per_bucket: int) -> System.Buffers.ArrayPool[System_Buffers_ArrayPool_T]:
        """
        Creates a new ArrayPool{T} instance using custom configuration options.
        
        :param max_array_length: The maximum length of array instances that may be stored in the pool.
        :param max_arrays_per_bucket: The maximum number of array instances that may be stored in each bucket in the pool.  The pool groups arrays of similar lengths into buckets for faster access.
        :returns: A new ArrayPool{T} instance with the specified configuration options.
        """
        ...

    def rent(self, minimum_length: int) -> typing.List[System_Buffers_ArrayPool_T]:
        """
        Retrieves a buffer that is at least the requested length.
        
        :param minimum_length: The minimum length of the array needed.
        :returns: An array that is at least  in length.
        """
        ...

    def Return(self, array: typing.List[System_Buffers_ArrayPool_T], clearArray: bool = False) -> None:
        """
        Returns to the pool an array that was previously obtained via Rent on the same
        ArrayPool{T} instance.
        
        :param array: The buffer previously obtained from Rent to return to the pool.
        :param clearArray: If true and if the pool will store the buffer to enable subsequent reuse, Return will clear  of its contents so that a subsequent consumer via Rent will not see the previous consumer's content.  If false or if the pool will release the buffer, the array's contents are left unchanged.
        """
        ...


class MemoryHandle(System.IDisposable):
    """A handle for the memory."""

    @property
    def pointer(self) -> typing.Any:
        """Returns the pointer to memory, where the memory is assumed to be pinned and hence the address won't change."""
        ...

    def __init__(self, pointer: typing.Any, handle: System.Runtime.InteropServices.GCHandle = ..., pinnable: System.Buffers.IPinnable = ...) -> None:
        """
        Creates a new memory handle for the memory.
        
        :param pointer: pointer to memory
        :param handle: handle used to pin array buffers
        :param pinnable: reference to manually managed object, or default if there is no memory manager
        """
        ...

    def dispose(self) -> None:
        """Frees the pinned handle and releases IPinnable."""
        ...


class IPinnable(metaclass=abc.ABCMeta):
    """Provides a mechanism for pinning and unpinning objects to prevent the GC from moving them."""

    def pin(self, element_index: int) -> System.Buffers.MemoryHandle:
        """
        Call this method to indicate that the IPinnable object can not be moved by the garbage collector.
        The address of the pinned object can be taken.
        
        :param element_index: The offset to the element within the memory at which the returned MemoryHandle points to.
        """
        ...

    def unpin(self) -> None:
        """
        Call this method to indicate that the IPinnable object no longer needs to be pinned.
        The garbage collector is free to move the object now.
        """
        ...


class StandardFormat(System.IEquatable[System_Buffers_StandardFormat]):
    """
    Represents a standard formatting string without using an actual String. A StandardFormat consists of a character (such as 'G', 'D' or 'X')
    and an optional precision ranging from 0..99, or the special value NoPrecision.
    """

    NO_PRECISION: int = ...
    """Precision values for format that don't use a precision, or for when the precision is to be unspecified."""

    MAX_PRECISION: int = 99
    """The maximum valid precision value."""

    @property
    def symbol(self) -> str:
        """The character component of the format."""
        ...

    @property
    def precision(self) -> int:
        """The precision component of the format. Ranges from 0..9 or the special value NoPrecision."""
        ...

    @property
    def has_precision(self) -> bool:
        """true if Precision is a value other than NoPrecision"""
        ...

    @property
    def is_default(self) -> bool:
        """true if the StandardFormat == default(StandardFormat)"""
        ...

    def __eq__(self, right: System.Buffers.StandardFormat) -> bool:
        """Returns true if both the Symbol and Precision are equal."""
        ...

    def __init__(self, symbol: str, precision: int = ...) -> None:
        """
        Create a StandardFormat.
        
        :param symbol: A type-specific formatting character such as 'G', 'D' or 'X'
        :param precision: An optional precision ranging from 0..9 or the special value NoPrecision (the default)
        """
        ...

    def __ne__(self, right: System.Buffers.StandardFormat) -> bool:
        """Returns false if both the Symbol and Precision are equal."""
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        """Returns true if both the Symbol and Precision are equal."""
        ...

    @overload
    def equals(self, other: System.Buffers.StandardFormat) -> bool:
        """Returns true if both the Symbol and Precision are equal."""
        ...

    def get_hash_code(self) -> int:
        """Compute a hash code."""
        ...

    @staticmethod
    @overload
    def parse(format: System.ReadOnlySpan[str]) -> System.Buffers.StandardFormat:
        """Converts a ReadOnlySpan{Char} into a StandardFormat"""
        ...

    @staticmethod
    @overload
    def parse(format: str) -> System.Buffers.StandardFormat:
        """Converts a classic .NET format string into a StandardFormat"""
        ...

    def to_string(self) -> str:
        """Returns the format in classic .NET format."""
        ...

    @staticmethod
    def try_parse(format: System.ReadOnlySpan[str], result: typing.Optional[System.Buffers.StandardFormat]) -> typing.Tuple[bool, System.Buffers.StandardFormat]:
        """Tries to convert a ReadOnlySpan{Char} into a StandardFormat. A return value indicates whether the conversion succeeded or failed."""
        ...


class OperationStatus(Enum):
    """
    This enum defines the various potential status that can be returned from Span-based operations
    that support processing of input contained in multiple discontiguous buffers.
    """

    DONE = 0
    """The entire input buffer has been processed and the operation is complete."""

    DESTINATION_TOO_SMALL = 1
    """
    The input is partially processed, up to what could fit into the destination buffer.
    The caller can enlarge the destination buffer, slice the buffers appropriately, and retry.
    """

    NEED_MORE_DATA = 2
    """
    The input is partially processed, up to the last valid chunk of the input that could be consumed.
    The caller can stitch the remaining unprocessed input with more data, slice the buffers appropriately, and retry.
    """

    INVALID_DATA = 3
    """
    The input contained invalid bytes which could not be processed. If the input is partially processed,
    the destination contains the partial result. This guarantees that no additional data appended to the input
    will make the invalid sequence valid.
    """


class IMemoryOwner(typing.Generic[System_Buffers_IMemoryOwner_T], System.IDisposable, metaclass=abc.ABCMeta):
    """Owner of MemoryT that is responsible for disposing the underlying memory appropriately."""

    @property
    @abc.abstractmethod
    def memory(self) -> System.Memory[System_Buffers_IMemoryOwner_T]:
        """Returns a MemoryT."""
        ...


class MemoryManager(typing.Generic[System_Buffers_MemoryManager_T], System.Object, System.Buffers.IMemoryOwner[System_Buffers_MemoryManager_T], System.Buffers.IPinnable, metaclass=abc.ABCMeta):
    """Manager of Memory{T} that provides the implementation."""

    @property
    def memory(self) -> System.Memory[System_Buffers_MemoryManager_T]:
        """Returns a Memory{T}."""
        ...

    @overload
    def create_memory(self, length: int) -> System.Memory[System_Buffers_MemoryManager_T]:
        """
        Returns a Memory{T} for the current MemoryManager{T}.
        
        This method is protected.
        
        :param length: The element count in the memory, starting at offset 0.
        """
        ...

    @overload
    def create_memory(self, start: int, length: int) -> System.Memory[System_Buffers_MemoryManager_T]:
        """
        Returns a Memory{T} for the current MemoryManager{T}.
        
        This method is protected.
        
        :param start: The offset to the element which the returned memory starts at.
        :param length: The element count in the memory, starting at element offset .
        """
        ...

    def dispose(self, disposing: bool) -> None:
        """
        Clean up of any leftover managed and unmanaged resources.
        
        This method is protected.
        """
        ...

    def get_span(self) -> System.Span[System_Buffers_MemoryManager_T]:
        """Returns a span wrapping the underlying memory."""
        ...

    def pin(self, element_index: int = 0) -> System.Buffers.MemoryHandle:
        """
        Returns a handle to the memory that has been pinned and hence its address can be taken.
        
        :param element_index: The offset to the element within the memory at which the returned MemoryHandle points to. (default = 0)
        """
        ...

    def unpin(self) -> None:
        """Lets the garbage collector know that the object is free to be moved now."""
        ...


