from typing import overload
from enum import Enum
import abc
import datetime
import typing
import warnings

import System
import System.Buffers
import System.Collections
import System.Collections.Generic
import System.Collections.ObjectModel
import System.ComponentModel
import System.Configuration.Assemblies
import System.Globalization
import System.IO
import System.Numerics
import System.Reflection
import System.Runtime.CompilerServices
import System.Runtime.ExceptionServices
import System.Runtime.InteropServices
import System.Runtime.Remoting
import System.Runtime.Serialization
import System.Security
import System.Security.Principal
import System.Text
import System.Threading
import System.Threading.Tasks

System_Guid = typing.Any
System_ReadOnlyMemory = typing.Any
System_ValueTuple = typing.Any
System_TimeZoneInfo = typing.Any
System_TimeZoneInfo_AdjustmentRule = typing.Any
System_TimeZoneInfo_TransitionTime = typing.Any
System_DateTimeOffset = typing.Any
System_UIntPtr = typing.Any
System_Version = typing.Any
System_UInt128 = typing.Any
System_Int128 = typing.Any
System_Lazy = typing.Any
System_Memory = typing.Any
System_DateOnly = typing.Any
System_Half = typing.Any
System_TimeOnly = typing.Any
System_IntPtr = typing.Any
System_ConsoleKeyInfo = typing.Any

System_Nullable_T = typing.TypeVar("System_Nullable_T")
System_ReadOnlyMemory_T = typing.TypeVar("System_ReadOnlyMemory_T")
System_MemoryExtensions_SpanSplitEnumerator_T = typing.TypeVar("System_MemoryExtensions_SpanSplitEnumerator_T")
System_IParsable_TSelf = typing.TypeVar("System_IParsable_TSelf")
System_ValueTuple_T1 = typing.TypeVar("System_ValueTuple_T1")
System_ValueTuple_T2 = typing.TypeVar("System_ValueTuple_T2")
System_ValueTuple_T3 = typing.TypeVar("System_ValueTuple_T3")
System_ValueTuple_T4 = typing.TypeVar("System_ValueTuple_T4")
System_ValueTuple_T5 = typing.TypeVar("System_ValueTuple_T5")
System_ValueTuple_T6 = typing.TypeVar("System_ValueTuple_T6")
System_ValueTuple_T7 = typing.TypeVar("System_ValueTuple_T7")
System_ValueTuple_TRest = typing.TypeVar("System_ValueTuple_TRest")
System_IObservable_T = typing.TypeVar("System_IObservable_T")
System_IComparable_T = typing.TypeVar("System_IComparable_T")
System_WeakReference_T = typing.TypeVar("System_WeakReference_T")
System_IEquatable_T = typing.TypeVar("System_IEquatable_T")
System_ReadOnlySpan_T = typing.TypeVar("System_ReadOnlySpan_T")
System_IProgress_T = typing.TypeVar("System_IProgress_T")
System_Lazy_TMetadata = typing.TypeVar("System_Lazy_TMetadata")
System_Lazy_T = typing.TypeVar("System_Lazy_T")
System_Memory_T = typing.TypeVar("System_Memory_T")
System_IObserver_T = typing.TypeVar("System_IObserver_T")
System_Progress_T = typing.TypeVar("System_Progress_T")
System_ISpanParsable_TSelf = typing.TypeVar("System_ISpanParsable_TSelf")
System_Delegate_InvocationListEnumerator_TDelegate = typing.TypeVar("System_Delegate_InvocationListEnumerator_TDelegate")
System_Tuple_T1 = typing.TypeVar("System_Tuple_T1")
System_Tuple_T2 = typing.TypeVar("System_Tuple_T2")
System_Tuple_T3 = typing.TypeVar("System_Tuple_T3")
System_Tuple_T4 = typing.TypeVar("System_Tuple_T4")
System_Tuple_T5 = typing.TypeVar("System_Tuple_T5")
System_Tuple_T6 = typing.TypeVar("System_Tuple_T6")
System_Tuple_T7 = typing.TypeVar("System_Tuple_T7")
System_Tuple_TRest = typing.TypeVar("System_Tuple_TRest")
System_Span_T = typing.TypeVar("System_Span_T")
System_ArraySegment_T = typing.TypeVar("System_ArraySegment_T")
System_IUtf8SpanParsable_TSelf = typing.TypeVar("System_IUtf8SpanParsable_TSelf")
System__EventContainer_Callable = typing.TypeVar("System__EventContainer_Callable")
System__EventContainer_ReturnType = typing.TypeVar("System__EventContainer_ReturnType")


class Object:
    """This class has no documentation."""

    def __init__(self) -> None:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        """
        Determines whether the specified object is equal to the current object.
        
        :param obj: The object to compare with the current object.
        :returns: true if the specified object is equal to the current object; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def equals(obj_a: typing.Any, obj_b: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        """
        Serves as the default hash function.
        
        :returns: A hash code for the current object.
        """
        ...

    def get_type(self) -> typing.Type:
        ...

    def memberwise_clone(self) -> System.Object:
        """This method is protected."""
        ...

    @staticmethod
    def reference_equals(obj_a: typing.Any, obj_b: typing.Any) -> bool:
        ...

    def to_string(self) -> str:
        """
        Returns a string that represents the current object.
        
        :returns: A string that represents the current object.
        """
        ...


class IFormatProvider(metaclass=abc.ABCMeta):
    """Provides a mechanism for retrieving an object to control formatting."""

    def get_format(self, format_type: typing.Type) -> System.Object:
        ...


class IFormattable(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def to_string(self, format: str, format_provider: System.IFormatProvider) -> str:
        ...


class ISpanFormattable(System.IFormattable, metaclass=abc.ABCMeta):
    """Provides functionality to format the string representation of an object into a span."""

    def try_format(self, destination: System.Span[str], chars_written: typing.Optional[int], format: System.ReadOnlySpan[str], provider: System.IFormatProvider) -> typing.Tuple[bool, int]:
        """
        Tries to format the value of the current instance into the provided span of characters.
        
        :param destination: When this method returns, this instance's value formatted as a span of characters.
        :param chars_written: When this method returns, the number of characters that were written in .
        :param format: A span containing the characters that represent a standard or custom format string that defines the acceptable format for .
        :param provider: An optional object that supplies culture-specific formatting information for .
        :returns: true if the formatting was successful; otherwise, false.
        """
        ...


class TypeCode(Enum):
    """This class has no documentation."""

    EMPTY = 0

    OBJECT = 1

    DB_NULL = 2

    BOOLEAN = 3

    CHAR = 4

    S_BYTE = 5

    BYTE = 6

    INT_16 = 7

    U_INT_16 = 8

    INT_32 = 9

    U_INT_32 = 10

    INT_64 = 11

    U_INT_64 = 12

    SINGLE = 13

    DOUBLE = 14

    DECIMAL = 15

    DATE_TIME = 16

    STRING = 18


class IConvertible(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def get_type_code(self) -> System.TypeCode:
        ...

    def to_boolean(self, provider: System.IFormatProvider) -> bool:
        ...

    def to_byte(self, provider: System.IFormatProvider) -> int:
        ...

    def to_char(self, provider: System.IFormatProvider) -> str:
        ...

    def to_date_time(self, provider: System.IFormatProvider) -> datetime.datetime:
        ...

    def to_decimal(self, provider: System.IFormatProvider) -> float:
        ...

    def to_double(self, provider: System.IFormatProvider) -> float:
        ...

    def to_int_16(self, provider: System.IFormatProvider) -> int:
        ...

    def to_int_32(self, provider: System.IFormatProvider) -> int:
        ...

    def to_int_64(self, provider: System.IFormatProvider) -> int:
        ...

    def to_s_byte(self, provider: System.IFormatProvider) -> int:
        ...

    def to_single(self, provider: System.IFormatProvider) -> float:
        ...

    def to_string(self, provider: System.IFormatProvider) -> str:
        ...

    def to_type(self, conversion_type: typing.Type, provider: System.IFormatProvider) -> System.Object:
        ...

    def to_u_int_16(self, provider: System.IFormatProvider) -> int:
        ...

    def to_u_int_32(self, provider: System.IFormatProvider) -> int:
        ...

    def to_u_int_64(self, provider: System.IFormatProvider) -> int:
        ...


class ICloneable(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def clone(self) -> System.Object:
        ...


class Array(System.Object, System.ICloneable, System.Collections.IList, System.Collections.IStructuralComparable, System.Collections.IStructuralEquatable, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    def sync_root(self) -> System.Object:
        ...

    @property
    def is_read_only(self) -> bool:
        ...

    @property
    def is_fixed_size(self) -> bool:
        ...

    @property
    def is_synchronized(self) -> bool:
        ...

    MAX_LENGTH: int
    """Gets the maximum number of elements that may be contained in an array."""

    @property
    def length(self) -> int:
        ...

    @property
    def long_length(self) -> int:
        ...

    @property
    def rank(self) -> int:
        ...

    @staticmethod
    @overload
    def binary_search(array: System.Array, value: typing.Any) -> int:
        ...

    @staticmethod
    @overload
    def binary_search(array: System.Array, index: int, length: int, value: typing.Any) -> int:
        ...

    @staticmethod
    @overload
    def binary_search(array: System.Array, value: typing.Any, comparer: System.Collections.IComparer) -> int:
        ...

    @staticmethod
    @overload
    def binary_search(array: System.Array, index: int, length: int, value: typing.Any, comparer: System.Collections.IComparer) -> int:
        ...

    @staticmethod
    @overload
    def clear(array: System.Array) -> None:
        ...

    @staticmethod
    @overload
    def clear(array: System.Array, index: int, length: int) -> None:
        ...

    def clone(self) -> System.Object:
        ...

    @staticmethod
    def constrained_copy(source_array: System.Array, source_index: int, destination_array: System.Array, destination_index: int, length: int) -> None:
        ...

    @staticmethod
    @overload
    def copy(source_array: System.Array, destination_array: System.Array, length: int) -> None:
        ...

    @staticmethod
    @overload
    def copy(source_array: System.Array, source_index: int, destination_array: System.Array, destination_index: int, length: int) -> None:
        ...

    def copy_to(self, array: System.Array, index: int) -> None:
        ...

    @staticmethod
    @overload
    def create_instance(element_type: typing.Type, length: int) -> System.Array:
        ...

    @staticmethod
    @overload
    def create_instance(element_type: typing.Type, length_1: int, length_2: int) -> System.Array:
        ...

    @staticmethod
    @overload
    def create_instance(element_type: typing.Type, length_1: int, length_2: int, length_3: int) -> System.Array:
        ...

    @staticmethod
    @overload
    def create_instance(element_type: typing.Type, *lengths: typing.Union[int, typing.Iterable[int]]) -> System.Array:
        ...

    @staticmethod
    @overload
    def create_instance(element_type: typing.Type, lengths: typing.List[int], lower_bounds: typing.List[int]) -> System.Array:
        ...

    @staticmethod
    @overload
    def create_instance_from_array_type(array_type: typing.Type, length: int) -> System.Array:
        """
        Creates a one-dimensional Array of the specified array type and length, with zero-based indexing.
        
        :param array_type: The type of the array (not of the array element type).
        :param length: The size of the Array to create.
        :returns: A new one-dimensional Array of the specified Type with the specified length.
        """
        ...

    @staticmethod
    @overload
    def create_instance_from_array_type(array_type: typing.Type, *lengths: typing.Union[int, typing.Iterable[int]]) -> System.Array:
        """
        Creates a multidimensional Array of the specified Type and dimension lengths, with zero-based indexing.
        
        :param array_type: The type of the array (not of the array element type).
        :param lengths: The dimension lengths, specified in an array of 32-bit integers.
        :returns: A new multidimensional Array of the specified Type with the specified length for each dimension, using zero-based indexing.
        """
        ...

    @staticmethod
    @overload
    def create_instance_from_array_type(array_type: typing.Type, lengths: typing.List[int], lower_bounds: typing.List[int]) -> System.Array:
        """
        Creates a multidimensional Array of the specified Type and dimension lengths, with the specified lower bounds.
        
        :param array_type: The type of the array (not of the array element type).
        :param lengths: The dimension lengths, specified in an array of 32-bit integers.
        :param lower_bounds: A one-dimensional array that contains the lower bound (starting index) of each dimension of the Array to create.
        :returns: A new multidimensional Array of the specified Type with the specified length and lower bound for each dimension.
        """
        ...

    def get_enumerator(self) -> System.Collections.IEnumerator:
        ...

    def get_length(self, dimension: int) -> int:
        ...

    def get_long_length(self, dimension: int) -> int:
        ...

    def get_lower_bound(self, dimension: int) -> int:
        ...

    def get_upper_bound(self, dimension: int) -> int:
        ...

    @overload
    def get_value(self, *indices: typing.Union[int, typing.Iterable[int]]) -> System.Object:
        ...

    @overload
    def get_value(self, index: int) -> System.Object:
        ...

    @overload
    def get_value(self, index_1: int, index_2: int) -> System.Object:
        ...

    @overload
    def get_value(self, index_1: int, index_2: int, index_3: int) -> System.Object:
        ...

    @staticmethod
    @overload
    def index_of(array: System.Array, value: typing.Any) -> int:
        ...

    @staticmethod
    @overload
    def index_of(array: System.Array, value: typing.Any, start_index: int) -> int:
        ...

    @staticmethod
    @overload
    def index_of(array: System.Array, value: typing.Any, start_index: int, count: int) -> int:
        ...

    def initialize(self) -> None:
        ...

    @staticmethod
    @overload
    def last_index_of(array: System.Array, value: typing.Any) -> int:
        ...

    @staticmethod
    @overload
    def last_index_of(array: System.Array, value: typing.Any, start_index: int) -> int:
        ...

    @staticmethod
    @overload
    def last_index_of(array: System.Array, value: typing.Any, start_index: int, count: int) -> int:
        ...

    @staticmethod
    @overload
    def reverse(array: System.Array) -> None:
        ...

    @staticmethod
    @overload
    def reverse(array: System.Array, index: int, length: int) -> None:
        ...

    @overload
    def set_value(self, value: typing.Any, index: int) -> None:
        ...

    @overload
    def set_value(self, value: typing.Any, index_1: int, index_2: int) -> None:
        ...

    @overload
    def set_value(self, value: typing.Any, index_1: int, index_2: int, index_3: int) -> None:
        ...

    @overload
    def set_value(self, value: typing.Any, *indices: typing.Union[int, typing.Iterable[int]]) -> None:
        ...

    @staticmethod
    @overload
    def sort(array: System.Array) -> None:
        ...

    @staticmethod
    @overload
    def sort(keys: System.Array, items: System.Array) -> None:
        ...

    @staticmethod
    @overload
    def sort(array: System.Array, index: int, length: int) -> None:
        ...

    @staticmethod
    @overload
    def sort(keys: System.Array, items: System.Array, index: int, length: int) -> None:
        ...

    @staticmethod
    @overload
    def sort(array: System.Array, comparer: System.Collections.IComparer) -> None:
        ...

    @staticmethod
    @overload
    def sort(keys: System.Array, items: System.Array, comparer: System.Collections.IComparer) -> None:
        ...

    @staticmethod
    @overload
    def sort(array: System.Array, index: int, length: int, comparer: System.Collections.IComparer) -> None:
        ...

    @staticmethod
    @overload
    def sort(keys: System.Array, items: System.Array, index: int, length: int, comparer: System.Collections.IComparer) -> None:
        ...


class Enum(System.Object, System.IComparable, System.ISpanFormattable, System.IConvertible, metaclass=abc.ABCMeta):
    """Provides the base class for enumerations."""

    def __ge__(self, other: typing.Any) -> bool:
        ...

    def __gt__(self, other: typing.Any) -> bool:
        ...

    def __le__(self, other: typing.Any) -> bool:
        ...

    def __lt__(self, other: typing.Any) -> bool:
        ...

    def compare_to(self, target: typing.Any) -> int:
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    @staticmethod
    def format(enum_type: typing.Type, value: typing.Any, format: str) -> str:
        """
        Converts the specified value of a specified enumerated type to its equivalent string representation according to the specified format.
        
        :param enum_type: The enumeration type of the value to convert.
        :param value: The value to convert.
        :param format: The output format to use.
        :returns: A string representation of .
        """
        ...

    def get_hash_code(self) -> int:
        ...

    @staticmethod
    def get_name(enum_type: typing.Type, value: typing.Any) -> str:
        """
        Retrieves the name of the constant in the specified enumeration type that has the specified value.
        
        :param enum_type: An enumeration type.
        :param value: The value of a particular enumerated constant in terms of its underlying type.
        :returns: A string containing the name of the enumerated constant in  whose value is , or null if no such constant is found.
        """
        ...

    @staticmethod
    def get_names(enum_type: typing.Type) -> typing.List[str]:
        """
        Retrieves an array of the names of the constants in a specified enumeration.
        
        :param enum_type: An enumeration type.
        :returns: A string array of the names of the constants in .
        """
        ...

    def get_type_code(self) -> System.TypeCode:
        ...

    @staticmethod
    def get_underlying_type(enum_type: typing.Type) -> typing.Type:
        """
        Returns the underlying type of the specified enumeration.
        
        :param enum_type: The enumeration whose underlying type will be retrieved.
        :returns: The underlying type of .
        """
        ...

    @staticmethod
    def get_values(enum_type: typing.Type) -> System.Array:
        """
        Retrieves an array of the values of the constants in a specified enumeration.
        
        :param enum_type: An enumeration type.
        :returns: An array that contains the values of the constants in .
        """
        ...

    @staticmethod
    def get_values_as_underlying_type(enum_type: typing.Type) -> System.Array:
        """
        Retrieves an array of the values of the underlying type constants in a specified enumeration.
        
        :param enum_type: An enumeration type.
        :returns: An array that contains the values of the underlying type constants in  .
        """
        ...

    def has_flag(self, flag: System.Enum) -> bool:
        """
        Determines whether one or more bit fields are set in the current instance.
        
        :param flag: An enumeration value.
        :returns: true if the bit field or bit fields that are set in flag are also set in the current instance; otherwise, false.
        """
        ...

    @staticmethod
    def is_defined(enum_type: typing.Type, value: typing.Any) -> bool:
        """
        Returns a bool telling whether a given integral value, or its name as a string, exists in a specified enumeration.
        
        :param enum_type: An enumeration type.
        :param value: The value or name of a constant in .
        :returns: true if a constant in  has a value equal to value; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def parse(enum_type: typing.Type, value: str) -> System.Object:
        """
        Converts the string representation of the name or numeric value of one or more enumerated constants to an equivalent enumerated object.
        
        :param enum_type: An enumeration type.
        :param value: A string containing the name or value to convert.
        :returns: An object of type  whose value is represented by .
        """
        ...

    @staticmethod
    @overload
    def parse(enum_type: typing.Type, value: System.ReadOnlySpan[str]) -> System.Object:
        """
        Converts the span of chars representation of the name or numeric value of one or more enumerated constants to an equivalent enumerated object.
        
        :param enum_type: An enumeration type.
        :param value: A span containing the name or value to convert.
        :returns: An object of type  whose value is represented by .
        """
        ...

    @staticmethod
    @overload
    def parse(enum_type: typing.Type, value: str, ignore_case: bool) -> System.Object:
        """
        Converts the string representation of the name or numeric value of one or more enumerated constants to an equivalent enumerated object.
        A parameter specifies whether the operation is case-insensitive.
        
        :param enum_type: An enumeration type.
        :param value: A string containing the name or value to convert.
        :param ignore_case: true to ignore case; false to regard case.
        :returns: An object of type  whose value is represented by .
        """
        ...

    @staticmethod
    @overload
    def parse(enum_type: typing.Type, value: System.ReadOnlySpan[str], ignore_case: bool) -> System.Object:
        """
        Converts the span of chars representation of the name or numeric value of one or more enumerated constants to an equivalent enumerated object.
        A parameter specifies whether the operation is case-insensitive.
        
        :param enum_type: An enumeration type.
        :param value: A span containing the name or value to convert.
        :param ignore_case: true to ignore case; false to regard case.
        :returns: An object of type  whose value is represented by .
        """
        ...

    @staticmethod
    @overload
    def to_object(enum_type: typing.Type, value: typing.Any) -> System.Object:
        ...

    @staticmethod
    @overload
    def to_object(enum_type: typing.Type, value: int) -> System.Object:
        ...

    @overload
    def to_string(self) -> str:
        """Converts the value of this instance to its equivalent string representation."""
        ...

    @overload
    def to_string(self, format: str) -> str:
        """
        Converts the value of this instance to its equivalent string representation using the specified format.
        
        :param format: A format string.
        :returns: The string representation of the value of this instance as specified by .
        """
        ...

    @overload
    def to_string(self, provider: System.IFormatProvider) -> str:
        """
        This method overload is obsolete; use ToString().
        
        The provider argument is not used. Use ToString() instead.
        """
        ...

    @overload
    def to_string(self, format: str, provider: System.IFormatProvider) -> str:
        """
        This method overload is obsolete; use ToString(string).
        
        The provider argument is not used. Use ToString(String) instead.
        """
        ...

    @staticmethod
    @overload
    def try_parse(enum_type: typing.Type, value: str, result: typing.Optional[typing.Any]) -> typing.Tuple[bool, typing.Any]:
        """
        Converts the string representation of the name or numeric value of one or more enumerated constants to an equivalent enumerated object.
        
        :param enum_type: The enum type to use for parsing.
        :param value: The string representation of the name or numeric value of one or more enumerated constants.
        :param result: When this method returns true, an object containing an enumeration constant representing the parsed value.
        :returns: true if the conversion succeeded; false otherwise.
        """
        ...

    @staticmethod
    @overload
    def try_parse(enum_type: typing.Type, value: System.ReadOnlySpan[str], result: typing.Optional[typing.Any]) -> typing.Tuple[bool, typing.Any]:
        """
        Converts the span of chars representation of the name or numeric value of one or more enumerated constants to an equivalent enumerated object.
        
        :param enum_type: The enum type to use for parsing.
        :param value: The span representation of the name or numeric value of one or more enumerated constants.
        :param result: When this method returns true, an object containing an enumeration constant representing the parsed value.
        :returns: true if the conversion succeeded; false otherwise.
        """
        ...

    @staticmethod
    @overload
    def try_parse(enum_type: typing.Type, value: str, ignore_case: bool, result: typing.Optional[typing.Any]) -> typing.Tuple[bool, typing.Any]:
        """
        Converts the string representation of the name or numeric value of one or more enumerated constants to an equivalent enumerated object.
        A parameter specifies whether the operation is case-insensitive.
        
        :param enum_type: The enum type to use for parsing.
        :param value: The string representation of the name or numeric value of one or more enumerated constants.
        :param ignore_case: true to read  in case insensitive mode; false to read  in case sensitive mode.
        :param result: When this method returns true, an object containing an enumeration constant representing the parsed value.
        :returns: true if the conversion succeeded; false otherwise.
        """
        ...

    @staticmethod
    @overload
    def try_parse(enum_type: typing.Type, value: System.ReadOnlySpan[str], ignore_case: bool, result: typing.Optional[typing.Any]) -> typing.Tuple[bool, typing.Any]:
        """
        Converts the span of chars representation of the name or numeric value of one or more enumerated constants to an equivalent enumerated object.
        A parameter specifies whether the operation is case-insensitive.
        
        :param enum_type: The enum type to use for parsing.
        :param value: The span representation of the name or numeric value of one or more enumerated constants.
        :param ignore_case: true to read  in case insensitive mode; false to read  in case sensitive mode.
        :param result: When this method returns true, an object containing an enumeration constant representing the parsed value.
        :returns: true if the conversion succeeded; false otherwise.
        """
        ...


class MidpointRounding(Enum):
    """This class has no documentation."""

    TO_EVEN = 0

    AWAY_FROM_ZERO = 1

    TO_ZERO = 2

    TO_NEGATIVE_INFINITY = 3

    TO_POSITIVE_INFINITY = 4


class PlatformID(Enum):
    """This class has no documentation."""

    WIN_32S = 0

    WIN_32_WINDOWS = 1

    WIN_32_NT = 2

    WIN_CE = 3

    UNIX = 4

    XBOX = 5

    MAC_OSX = 6

    OTHER = 7


class IUtf8SpanFormattable(metaclass=abc.ABCMeta):
    """Provides functionality to format the string representation of an object into a span as UTF-8."""

    def try_format(self, utf_8_destination: System.Span[int], bytes_written: typing.Optional[int], format: System.ReadOnlySpan[str], provider: System.IFormatProvider) -> typing.Tuple[bool, int]:
        """
        Tries to format the value of the current instance as UTF-8 into the provided span of bytes.
        
        :param utf_8_destination: When this method returns, this instance's value formatted as a span of bytes.
        :param bytes_written: When this method returns, the number of bytes that were written in .
        :param format: A span containing the characters that represent a standard or custom format string that defines the acceptable format for .
        :param provider: An optional object that supplies culture-specific formatting information for .
        :returns: true if the formatting was successful; otherwise, false.
        """
        ...


class Version(System.Object, System.ICloneable, System.IComparable[System_Version], System.IEquatable[System_Version], System.ISpanFormattable, System.IUtf8SpanFormattable, System.IUtf8SpanParsable[System_Version]):
    """This class has no documentation."""

    @property
    def major(self) -> int:
        ...

    @property
    def minor(self) -> int:
        ...

    @property
    def build(self) -> int:
        ...

    @property
    def revision(self) -> int:
        ...

    @property
    def major_revision(self) -> int:
        ...

    @property
    def minor_revision(self) -> int:
        ...

    def __eq__(self, v_2: System.Version) -> bool:
        ...

    @overload
    def __ge__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __ge__(self, other: System.Version) -> bool:
        ...

    @overload
    def __ge__(self, v_2: System.Version) -> bool:
        ...

    @overload
    def __gt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __gt__(self, other: System.Version) -> bool:
        ...

    @overload
    def __gt__(self, v_2: System.Version) -> bool:
        ...

    @overload
    def __init__(self, major: int, minor: int, build: int, revision: int) -> None:
        ...

    @overload
    def __init__(self, major: int, minor: int, build: int) -> None:
        ...

    @overload
    def __init__(self, major: int, minor: int) -> None:
        ...

    @overload
    def __init__(self, version: str) -> None:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __le__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __le__(self, other: System.Version) -> bool:
        ...

    @overload
    def __le__(self, v_2: System.Version) -> bool:
        ...

    @overload
    def __lt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __lt__(self, other: System.Version) -> bool:
        ...

    @overload
    def __lt__(self, v_2: System.Version) -> bool:
        ...

    def __ne__(self, v_2: System.Version) -> bool:
        ...

    def clone(self) -> System.Object:
        ...

    @overload
    def compare_to(self, version: typing.Any) -> int:
        ...

    @overload
    def compare_to(self, value: System.Version) -> int:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, obj: System.Version) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    @staticmethod
    @overload
    def parse(input: str) -> System.Version:
        ...

    @staticmethod
    @overload
    def parse(input: System.ReadOnlySpan[str]) -> System.Version:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int]) -> System.Version:
        """
        Converts the specified read-only span of UTF-8 characters that represents a version number to an equivalent Version object.
        
        :param utf_8_text: A read-only span of UTF-8 characters that contains a version number to convert.
        :returns: An object that is equivalent to the version number specified in the  parameter.
        """
        ...

    @overload
    def to_string(self) -> str:
        ...

    @overload
    def to_string(self, field_count: int) -> str:
        ...

    @overload
    def try_format(self, destination: System.Span[str], chars_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @overload
    def try_format(self, destination: System.Span[str], field_count: int, chars_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @overload
    def try_format(self, utf_8_destination: System.Span[int], bytes_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        """
        Tries to format this version instance into a span of bytes.
        
        :param utf_8_destination: The span in which to write this instance's value formatted as a span of UTF-8 bytes.
        :param bytes_written: When this method returns, contains the number of bytes that were written in .
        :returns: true if the formatting was successful; otherwise, false.
        """
        ...

    @overload
    def try_format(self, utf_8_destination: System.Span[int], field_count: int, bytes_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        """
        Tries to format this version instance into a span of bytes.
        
        :param utf_8_destination: The span in which to write this instance's value formatted as a span of UTF-8 bytes.
        :param field_count: The number of components to return. This value ranges from 0 to 4.
        :param bytes_written: When this method returns, contains the number of bytes that were written in .
        :returns: true if the formatting was successful; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def try_parse(input: str, result: typing.Optional[System.Version]) -> typing.Tuple[bool, System.Version]:
        ...

    @staticmethod
    @overload
    def try_parse(input: System.ReadOnlySpan[str], result: typing.Optional[System.Version]) -> typing.Tuple[bool, System.Version]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], result: typing.Optional[System.Version]) -> typing.Tuple[bool, System.Version]:
        """
        Tries to convert the UTF-8 representation of a version number to an equivalent Version object, and returns a value that indicates whether the conversion succeeded.
        
        :param utf_8_text: The span of UTF-8 characters to parse.
        :param result: When this method returns, contains the Version equivalent of the number that is contained in , if the conversion succeeded.     If  is empty, or if the conversion fails, result is null when the method returns.
        :returns: true if the  parameter was converted successfully; otherwise, false.
        """
        ...


class OperatingSystem(System.Object, System.Runtime.Serialization.ISerializable, System.ICloneable):
    """This class has no documentation."""

    @property
    def platform(self) -> System.PlatformID:
        ...

    @property
    def service_pack(self) -> str:
        ...

    @property
    def version(self) -> System.Version:
        ...

    @property
    def version_string(self) -> str:
        ...

    def __init__(self, platform: System.PlatformID, version: System.Version) -> None:
        ...

    def clone(self) -> System.Object:
        ...

    def get_object_data(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """Obsoletions.LegacyFormatterImplMessage"""
        warnings.warn("Obsoletions.LegacyFormatterImplMessage", DeprecationWarning)

    @staticmethod
    def is_android() -> bool:
        """Indicates whether the current application is running on Android."""
        ...

    @staticmethod
    def is_android_version_at_least(major: int, minor: int = 0, build: int = 0, revision: int = 0) -> bool:
        """Check for the Android API level (returned by 'ro.build.version.sdk') with a >= version comparison. Used to guard APIs that were added in the given Android release."""
        ...

    @staticmethod
    def is_browser() -> bool:
        """Indicates whether the current application is running as WASM in a Browser."""
        ...

    @staticmethod
    def is_free_bsd() -> bool:
        """Indicates whether the current application is running on FreeBSD."""
        ...

    @staticmethod
    def is_free_bsd_version_at_least(major: int, minor: int = 0, build: int = 0, revision: int = 0) -> bool:
        """Check for the FreeBSD version (returned by 'uname') with a >= version comparison. Used to guard APIs that were added in the given FreeBSD release."""
        ...

    @staticmethod
    def is_ios() -> bool:
        """Indicates whether the current application is running on iOS or MacCatalyst."""
        ...

    @staticmethod
    def is_ios_version_at_least(major: int, minor: int = 0, build: int = 0) -> bool:
        """Check for the iOS/MacCatalyst version (returned by 'libobjc.get_operatingSystemVersion') with a >= version comparison. Used to guard APIs that were added in the given iOS release."""
        ...

    @staticmethod
    def is_linux() -> bool:
        """Indicates whether the current application is running on Linux."""
        ...

    @staticmethod
    def is_mac_catalyst() -> bool:
        """Indicates whether the current application is running on Mac Catalyst."""
        ...

    @staticmethod
    def is_mac_catalyst_version_at_least(major: int, minor: int = 0, build: int = 0) -> bool:
        """Check for the Mac Catalyst version (iOS version as presented in Apple documentation) with a >= version comparison. Used to guard APIs that were added in the given Mac Catalyst release."""
        ...

    @staticmethod
    def is_mac_os() -> bool:
        """Indicates whether the current application is running on macOS."""
        ...

    @staticmethod
    def is_mac_os_version_at_least(major: int, minor: int = 0, build: int = 0) -> bool:
        """Check for the macOS version (returned by 'libobjc.get_operatingSystemVersion') with a >= version comparison. Used to guard APIs that were added in the given macOS release."""
        ...

    @staticmethod
    def is_os_platform(platform: str) -> bool:
        """
        Indicates whether the current application is running on the specified platform.
        
        :param platform: Case-insensitive platform name. Examples: Browser, Linux, FreeBSD, Android, iOS, macOS, tvOS, watchOS, Windows.
        """
        ...

    @staticmethod
    def is_os_platform_version_at_least(platform: str, major: int, minor: int = 0, build: int = 0, revision: int = 0) -> bool:
        """
        Check for the OS with a >= version comparison. Used to guard APIs that were added in the given OS release.
        
        :param platform: Case-insensitive platform name. Examples: Browser, Linux, FreeBSD, Android, iOS, macOS, tvOS, watchOS, Windows.
        :param major: Major OS version number.
        :param minor: Minor OS version number (optional).
        :param build: Build OS version number (optional).
        :param revision: Revision OS version number (optional).
        """
        ...

    @staticmethod
    def is_tv_os() -> bool:
        """Indicates whether the current application is running on tvOS."""
        ...

    @staticmethod
    def is_tv_os_version_at_least(major: int, minor: int = 0, build: int = 0) -> bool:
        """Check for the tvOS version (returned by 'libobjc.get_operatingSystemVersion') with a >= version comparison. Used to guard APIs that were added in the given tvOS release."""
        ...

    @staticmethod
    def is_wasi() -> bool:
        """Indicates whether the current application is running as WASI."""
        ...

    @staticmethod
    def is_watch_os() -> bool:
        """Indicates whether the current application is running on watchOS."""
        ...

    @staticmethod
    def is_watch_os_version_at_least(major: int, minor: int = 0, build: int = 0) -> bool:
        """Check for the watchOS version (returned by 'libobjc.get_operatingSystemVersion') with a >= version comparison. Used to guard APIs that were added in the given watchOS release."""
        ...

    @staticmethod
    def is_windows() -> bool:
        """Indicates whether the current application is running on Windows."""
        ...

    @staticmethod
    def is_windows_version_at_least(major: int, minor: int = 0, build: int = 0, revision: int = 0) -> bool:
        """Check for the Windows version (returned by 'RtlGetVersion') with a >= version comparison. Used to guard APIs that were added in the given Windows release."""
        ...

    def to_string(self) -> str:
        ...


class EnvironmentVariableTarget(Enum):
    """This class has no documentation."""

    PROCESS = 0

    USER = 1

    MACHINE = 2


class Exception(System.Object, System.Runtime.Serialization.ISerializable):
    """This class has no documentation."""

    @property
    def message(self) -> str:
        ...

    @property
    def data(self) -> System.Collections.IDictionary:
        ...

    @property
    def inner_exception(self) -> System.Exception:
        ...

    @property
    def help_link(self) -> str:
        ...

    @help_link.setter
    def help_link(self, value: str) -> None:
        ...

    @property
    def source(self) -> str:
        ...

    @source.setter
    def source(self, value: str) -> None:
        ...

    @property
    def serialize_object_state(self) -> _EventContainer[typing.Callable[[System.Object, System.Runtime.Serialization.SafeSerializationEventArgs], None], None]:
        """
        This property is protected.
        
        Obsoletions.BinaryFormatterMessage
        """
        warnings.warn("Obsoletions.BinaryFormatterMessage", DeprecationWarning)

    @serialize_object_state.setter
    def serialize_object_state(self, value: _EventContainer[typing.Callable[[System.Object, System.Runtime.Serialization.SafeSerializationEventArgs], None], None]) -> None:
        warnings.warn("Obsoletions.BinaryFormatterMessage", DeprecationWarning)

    @property
    def h_result(self) -> int:
        ...

    @h_result.setter
    def h_result(self, value: int) -> None:
        ...

    @property
    def stack_trace(self) -> str:
        ...

    @property
    def target_site(self) -> System.Reflection.MethodBase:
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
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """
        This method is protected.
        
        Obsoletions.LegacyFormatterImplMessage
        """
        ...

    def get_base_exception(self) -> System.Exception:
        ...

    def get_object_data(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """Obsoletions.LegacyFormatterImplMessage"""
        warnings.warn("Obsoletions.LegacyFormatterImplMessage", DeprecationWarning)

    def get_type(self) -> typing.Type:
        ...

    def to_string(self) -> str:
        ...


class Environment(System.Object):
    """This class has no documentation."""

    class SpecialFolder(Enum):
        """This class has no documentation."""

        APPLICATION_DATA = ...

        COMMON_APPLICATION_DATA = ...

        LOCAL_APPLICATION_DATA = ...

        COOKIES = ...

        DESKTOP = ...

        FAVORITES = ...

        HISTORY = ...

        INTERNET_CACHE = ...

        PROGRAMS = ...

        MY_COMPUTER = ...

        MY_MUSIC = ...

        MY_PICTURES = ...

        MY_VIDEOS = ...

        RECENT = ...

        SEND_TO = ...

        START_MENU = ...

        STARTUP = ...

        SYSTEM = ...

        TEMPLATES = ...

        DESKTOP_DIRECTORY = ...

        PERSONAL = ...

        MY_DOCUMENTS = ...

        PROGRAM_FILES = ...

        COMMON_PROGRAM_FILES = ...

        ADMIN_TOOLS = ...

        CD_BURNING = ...

        COMMON_ADMIN_TOOLS = ...

        COMMON_DOCUMENTS = ...

        COMMON_MUSIC = ...

        COMMON_OEM_LINKS = ...

        COMMON_PICTURES = ...

        COMMON_START_MENU = ...

        COMMON_PROGRAMS = ...

        COMMON_STARTUP = ...

        COMMON_DESKTOP_DIRECTORY = ...

        COMMON_TEMPLATES = ...

        COMMON_VIDEOS = ...

        FONTS = ...

        NETWORK_SHORTCUTS = ...

        PRINTER_SHORTCUTS = ...

        USER_PROFILE = ...

        COMMON_PROGRAM_FILES_X_86 = ...

        PROGRAM_FILES_X_86 = ...

        RESOURCES = ...

        LOCALIZED_RESOURCES = ...

        SYSTEM_X_86 = ...

        WINDOWS = ...

    class SpecialFolderOption(Enum):
        """This class has no documentation."""

        NONE = 0

        CREATE = ...

        DO_NOT_VERIFY = ...

    class ProcessCpuUsage:
        """Represents the CPU usage statistics of a process."""

        @property
        def user_time(self) -> datetime.timedelta:
            """Gets the amount of time the associated process has spent running code inside the application portion of the process (not the operating system code)."""
            ...

        @property
        def privileged_time(self) -> datetime.timedelta:
            """Gets the amount of time the process has spent running code inside the operating system code."""
            ...

        @property
        def total_time(self) -> datetime.timedelta:
            """Gets the amount of time the process has spent utilizing the CPU including the process time spent in the application code and the process time spent in the operating system code."""
            ...

    MACHINE_NAME: str

    SYSTEM_DIRECTORY: str

    USER_INTERACTIVE: bool

    WORKING_SET: int

    CPU_USAGE: System.Environment.ProcessCpuUsage
    """
    Get the CPU usage, including the process time spent running the application code, the process time spent running the operating system code,
    and the total time spent running both the application and operating system code.
    """

    USER_DOMAIN_NAME: str

    USER_NAME: str

    PROCESSOR_COUNT: int

    IS_PRIVILEGED_PROCESS: bool
    """Gets whether the current process is authorized to perform security-relevant functions."""

    HAS_SHUTDOWN_STARTED: bool

    COMMAND_LINE: str

    current_directory: str

    PROCESS_ID: int
    """Gets the unique identifier for the current process."""

    PROCESS_PATH: str
    """Returns the path of the executable that started the currently executing process. Returns null when the path is not available."""

    IS_64_BIT_PROCESS: bool

    IS_64_BIT_OPERATING_SYSTEM: bool

    NEW_LINE: str

    OS_VERSION: System.OperatingSystem

    STACK_TRACE: str

    SYSTEM_PAGE_SIZE: int

    CURRENT_MANAGED_THREAD_ID: int

    exit_code: int

    TICK_COUNT: int

    TICK_COUNT_64: int

    @staticmethod
    def exit(exit_code: int) -> None:
        ...

    @staticmethod
    def expand_environment_variables(name: str) -> str:
        ...

    @staticmethod
    @overload
    def fail_fast(message: str) -> None:
        ...

    @staticmethod
    @overload
    def fail_fast(message: str, exception: System.Exception) -> None:
        ...

    @staticmethod
    def get_command_line_args() -> typing.List[str]:
        ...

    @staticmethod
    @overload
    def get_environment_variable(variable: str) -> str:
        ...

    @staticmethod
    @overload
    def get_environment_variable(variable: str, target: System.EnvironmentVariableTarget) -> str:
        ...

    @staticmethod
    @overload
    def get_environment_variables() -> System.Collections.IDictionary:
        ...

    @staticmethod
    @overload
    def get_environment_variables(target: System.EnvironmentVariableTarget) -> System.Collections.IDictionary:
        ...

    @staticmethod
    @overload
    def get_folder_path(folder: System.Environment.SpecialFolder) -> str:
        ...

    @staticmethod
    @overload
    def get_folder_path(folder: System.Environment.SpecialFolder, option: System.Environment.SpecialFolderOption) -> str:
        ...

    @staticmethod
    def get_logical_drives() -> typing.List[str]:
        ...

    @staticmethod
    @overload
    def set_environment_variable(variable: str, value: str) -> None:
        ...

    @staticmethod
    @overload
    def set_environment_variable(variable: str, value: str, target: System.EnvironmentVariableTarget) -> None:
        ...


class Attribute(System.Object, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    def type_id(self) -> System.Object:
        ...

    def __init__(self) -> None:
        """This method is protected."""
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    @staticmethod
    @overload
    def get_custom_attribute(element: System.Reflection.Assembly, attribute_type: typing.Type) -> System.Attribute:
        ...

    @staticmethod
    @overload
    def get_custom_attribute(element: System.Reflection.Assembly, attribute_type: typing.Type, inherit: bool) -> System.Attribute:
        ...

    @staticmethod
    @overload
    def get_custom_attribute(element: System.Reflection.MemberInfo, attribute_type: typing.Type) -> System.Attribute:
        ...

    @staticmethod
    @overload
    def get_custom_attribute(element: System.Reflection.MemberInfo, attribute_type: typing.Type, inherit: bool) -> System.Attribute:
        ...

    @staticmethod
    @overload
    def get_custom_attribute(element: System.Reflection.Module, attribute_type: typing.Type) -> System.Attribute:
        ...

    @staticmethod
    @overload
    def get_custom_attribute(element: System.Reflection.Module, attribute_type: typing.Type, inherit: bool) -> System.Attribute:
        ...

    @staticmethod
    @overload
    def get_custom_attribute(element: System.Reflection.ParameterInfo, attribute_type: typing.Type) -> System.Attribute:
        ...

    @staticmethod
    @overload
    def get_custom_attribute(element: System.Reflection.ParameterInfo, attribute_type: typing.Type, inherit: bool) -> System.Attribute:
        ...

    @staticmethod
    @overload
    def get_custom_attributes(element: System.Reflection.Assembly) -> typing.List[System.Attribute]:
        ...

    @staticmethod
    @overload
    def get_custom_attributes(element: System.Reflection.Assembly, inherit: bool) -> typing.List[System.Attribute]:
        ...

    @staticmethod
    @overload
    def get_custom_attributes(element: System.Reflection.Assembly, attribute_type: typing.Type) -> typing.List[System.Attribute]:
        ...

    @staticmethod
    @overload
    def get_custom_attributes(element: System.Reflection.Assembly, attribute_type: typing.Type, inherit: bool) -> typing.List[System.Attribute]:
        ...

    @staticmethod
    @overload
    def get_custom_attributes(element: System.Reflection.MemberInfo) -> typing.List[System.Attribute]:
        ...

    @staticmethod
    @overload
    def get_custom_attributes(element: System.Reflection.MemberInfo, inherit: bool) -> typing.List[System.Attribute]:
        ...

    @staticmethod
    @overload
    def get_custom_attributes(element: System.Reflection.MemberInfo, attribute_type: typing.Type) -> typing.List[System.Attribute]:
        ...

    @staticmethod
    @overload
    def get_custom_attributes(element: System.Reflection.MemberInfo, attribute_type: typing.Type, inherit: bool) -> typing.List[System.Attribute]:
        ...

    @staticmethod
    @overload
    def get_custom_attributes(element: System.Reflection.Module) -> typing.List[System.Attribute]:
        ...

    @staticmethod
    @overload
    def get_custom_attributes(element: System.Reflection.Module, inherit: bool) -> typing.List[System.Attribute]:
        ...

    @staticmethod
    @overload
    def get_custom_attributes(element: System.Reflection.Module, attribute_type: typing.Type) -> typing.List[System.Attribute]:
        ...

    @staticmethod
    @overload
    def get_custom_attributes(element: System.Reflection.Module, attribute_type: typing.Type, inherit: bool) -> typing.List[System.Attribute]:
        ...

    @staticmethod
    @overload
    def get_custom_attributes(element: System.Reflection.ParameterInfo) -> typing.List[System.Attribute]:
        ...

    @staticmethod
    @overload
    def get_custom_attributes(element: System.Reflection.ParameterInfo, inherit: bool) -> typing.List[System.Attribute]:
        ...

    @staticmethod
    @overload
    def get_custom_attributes(element: System.Reflection.ParameterInfo, attribute_type: typing.Type) -> typing.List[System.Attribute]:
        ...

    @staticmethod
    @overload
    def get_custom_attributes(element: System.Reflection.ParameterInfo, attribute_type: typing.Type, inherit: bool) -> typing.List[System.Attribute]:
        ...

    def get_hash_code(self) -> int:
        ...

    def is_default_attribute(self) -> bool:
        ...

    @staticmethod
    @overload
    def is_defined(element: System.Reflection.Assembly, attribute_type: typing.Type) -> bool:
        ...

    @staticmethod
    @overload
    def is_defined(element: System.Reflection.Assembly, attribute_type: typing.Type, inherit: bool) -> bool:
        ...

    @staticmethod
    @overload
    def is_defined(element: System.Reflection.MemberInfo, attribute_type: typing.Type) -> bool:
        ...

    @staticmethod
    @overload
    def is_defined(element: System.Reflection.MemberInfo, attribute_type: typing.Type, inherit: bool) -> bool:
        ...

    @staticmethod
    @overload
    def is_defined(element: System.Reflection.Module, attribute_type: typing.Type) -> bool:
        ...

    @staticmethod
    @overload
    def is_defined(element: System.Reflection.Module, attribute_type: typing.Type, inherit: bool) -> bool:
        ...

    @staticmethod
    @overload
    def is_defined(element: System.Reflection.ParameterInfo, attribute_type: typing.Type) -> bool:
        ...

    @staticmethod
    @overload
    def is_defined(element: System.Reflection.ParameterInfo, attribute_type: typing.Type, inherit: bool) -> bool:
        ...

    def match(self, obj: typing.Any) -> bool:
        ...


class AttributeTargets(Enum):
    """This class has no documentation."""

    ASSEMBLY = ...

    MODULE = ...

    CLASS = ...

    STRUCT = ...

    ENUM = ...

    CONSTRUCTOR = ...

    METHOD = ...

    PROPERTY = ...

    FIELD = ...

    EVENT = ...

    INTERFACE = ...

    PARAMETER = ...

    DELEGATE = ...

    RETURN_VALUE = ...

    GENERIC_PARAMETER = ...

    ALL = ...


class AttributeUsageAttribute(System.Attribute):
    """Specifies the usage of another attribute class."""

    @property
    def valid_on(self) -> System.AttributeTargets:
        ...

    @property
    def allow_multiple(self) -> bool:
        ...

    @allow_multiple.setter
    def allow_multiple(self, value: bool) -> None:
        ...

    @property
    def inherited(self) -> bool:
        ...

    @inherited.setter
    def inherited(self, value: bool) -> None:
        ...

    def __init__(self, valid_on: System.AttributeTargets) -> None:
        ...


class UInt32(System.IComparable[int], System.IConvertible, System.ISpanFormattable, System.IEquatable[int], System.Numerics.IUnsignedNumber[int], System.IUtf8SpanFormattable, System.IBinaryIntegerParseAndFormatInfo[int]):
    """This class has no documentation."""

    MAX_VALUE: int = ...

    MIN_VALUE: int = ...

    @overload
    def __ge__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __ge__(self, other: int) -> bool:
        ...

    @overload
    def __gt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __gt__(self, other: int) -> bool:
        ...

    @overload
    def __le__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __le__(self, other: int) -> bool:
        ...

    @overload
    def __lt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __lt__(self, other: int) -> bool:
        ...

    @staticmethod
    def big_mul(left: int, right: int) -> int:
        """
        Produces the full product of two unsigned 32-bit numbers.
        
        :param left: The first number to multiply.
        :param right: The second number to multiply.
        :returns: The number containing the product of the specified numbers.
        """
        ...

    @staticmethod
    def clamp(value: int, min: int, max: int) -> int:
        ...

    @overload
    def compare_to(self, value: typing.Any) -> int:
        ...

    @overload
    def compare_to(self, value: int) -> int:
        ...

    @staticmethod
    def div_rem(left: int, right: int) -> System.ValueTuple[int, int]:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, obj: int) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def get_type_code(self) -> System.TypeCode:
        ...

    @staticmethod
    def is_even_integer(value: int) -> bool:
        ...

    @staticmethod
    def is_odd_integer(value: int) -> bool:
        ...

    @staticmethod
    def is_pow_2(value: int) -> bool:
        ...

    @staticmethod
    def leading_zero_count(value: int) -> int:
        ...

    @staticmethod
    def log_2(value: int) -> int:
        ...

    @staticmethod
    def max(x: int, y: int) -> int:
        ...

    @staticmethod
    def min(x: int, y: int) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: str) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: str, style: System.Globalization.NumberStyles) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: str, provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: str, style: System.Globalization.NumberStyles, provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int], style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> int:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int], provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    def pop_count(value: int) -> int:
        ...

    @staticmethod
    def rotate_left(value: int, rotate_amount: int) -> int:
        ...

    @staticmethod
    def rotate_right(value: int, rotate_amount: int) -> int:
        ...

    @staticmethod
    def sign(value: int) -> int:
        ...

    @overload
    def to_string(self) -> str:
        ...

    @overload
    def to_string(self, provider: System.IFormatProvider) -> str:
        ...

    @overload
    def to_string(self, format: str) -> str:
        ...

    @overload
    def to_string(self, format: str, provider: System.IFormatProvider) -> str:
        ...

    @staticmethod
    def trailing_zero_count(value: int) -> int:
        ...

    @overload
    def try_format(self, destination: System.Span[str], chars_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @overload
    def try_format(self, utf_8_destination: System.Span[int], bytes_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        """
        Tries to convert a UTF-8 character span containing the string representation of a number to its 32-bit unsigned integer equivalent.
        
        :param utf_8_text: A span containing the UTF-8 characters representing the number to convert.
        :param result: When this method returns, contains the 32-bit unsigned integer value equivalent to the number contained in  if the conversion succeeded, or zero if the conversion failed. This parameter is passed uninitialized; any value originally supplied in result will be overwritten.
        :returns: true if  was converted successfully; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def try_parse(s: str, style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...


class DayOfWeek(Enum):
    """Specifies the day of the week."""

    SUNDAY = 0

    MONDAY = 1

    TUESDAY = 2

    WEDNESDAY = 3

    THURSDAY = 4

    FRIDAY = 5

    SATURDAY = 6


class DateTimeKind(Enum):
    """This class has no documentation."""

    UNSPECIFIED = 0

    UTC = 1

    LOCAL = 2


class TimeOnly(System.IComparable[System_TimeOnly], System.IEquatable[System_TimeOnly], System.ISpanFormattable, System.ISpanParsable[System_TimeOnly], System.IUtf8SpanFormattable):
    """Represents a time of day, as would be read from a clock, within the range 00:00:00 to 23:59:59.9999999."""

    MIN_VALUE: System.TimeOnly
    """Represents the smallest possible value of TimeOnly."""

    MAX_VALUE: System.TimeOnly
    """Represents the largest possible value of TimeOnly."""

    @property
    def hour(self) -> int:
        """Gets the hour component of the time represented by this instance."""
        ...

    @property
    def minute(self) -> int:
        """Gets the minute component of the time represented by this instance."""
        ...

    @property
    def second(self) -> int:
        """Gets the second component of the time represented by this instance."""
        ...

    @property
    def millisecond(self) -> int:
        """Gets the millisecond component of the time represented by this instance."""
        ...

    @property
    def microsecond(self) -> int:
        """Gets the microsecond component of the time represented by this instance."""
        ...

    @property
    def nanosecond(self) -> int:
        """Gets the nanosecond component of the time represented by this instance."""
        ...

    @property
    def ticks(self) -> int:
        """Gets the number of ticks that represent the time of this instance."""
        ...

    def __eq__(self, right: System.TimeOnly) -> bool:
        """
        Determines whether two specified instances of TimeOnly are equal.
        
        :param left: The first object to compare.
        :param right: The second object to compare.
        :returns: true if left and right represent the same time; otherwise, false.
        """
        ...

    @overload
    def __ge__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __ge__(self, right: System.TimeOnly) -> bool:
        """
        Determines whether one specified TimeOnly represents a time that is the same as or later than another specified TimeOnly.
        
        :param left: The first object to compare.
        :param right: The second object to compare.
        :returns: true if left is the same as or later than right; otherwise, false.
        """
        ...

    @overload
    def __ge__(self, other: System.TimeOnly) -> bool:
        ...

    @overload
    def __gt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __gt__(self, right: System.TimeOnly) -> bool:
        """
        Determines whether one specified TimeOnly is later than another specified TimeOnly.
        
        :param left: The first object to compare.
        :param right: The second object to compare.
        :returns: true if left is later than right; otherwise, false.
        """
        ...

    @overload
    def __gt__(self, other: System.TimeOnly) -> bool:
        ...

    @overload
    def __init__(self, hour: int, minute: int) -> None:
        """
        Initializes a new instance of the timeOnly structure to the specified hour and the minute.
        
        :param hour: The hours (0 through 23).
        :param minute: The minutes (0 through 59).
        """
        ...

    @overload
    def __init__(self, hour: int, minute: int, second: int) -> None:
        """
        Initializes a new instance of the timeOnly structure to the specified hour, minute, and second.
        
        :param hour: The hours (0 through 23).
        :param minute: The minutes (0 through 59).
        :param second: The seconds (0 through 59).
        """
        ...

    @overload
    def __init__(self, hour: int, minute: int, second: int, millisecond: int) -> None:
        """
        Initializes a new instance of the timeOnly structure to the specified hour, minute, second, and millisecond.
        
        :param hour: The hours (0 through 23).
        :param minute: The minutes (0 through 59).
        :param second: The seconds (0 through 59).
        :param millisecond: The millisecond (0 through 999).
        """
        ...

    @overload
    def __init__(self, hour: int, minute: int, second: int, millisecond: int, microsecond: int) -> None:
        """
        Initializes a new instance of the TimeOnly structure to the specified hour, minute, second, and millisecond.
        
        :param hour: The hours (0 through 23).
        :param minute: The minutes (0 through 59).
        :param second: The seconds (0 through 59).
        :param millisecond: The millisecond (0 through 999).
        :param microsecond: The microsecond (0 through 999).
        """
        ...

    @overload
    def __init__(self, ticks: int) -> None:
        """
        Initializes a new instance of the TimeOnly structure using a specified number of ticks.
        
        :param ticks: A time of day expressed in the number of 100-nanosecond units since 00:00:00.0000000.
        """
        ...

    def __isub__(self, t_2: System.TimeOnly) -> datetime.timedelta:
        """
        Gives the elapsed time between two points on a circular clock, which will always be a positive value.
        
        :param t1: The first TimeOnly instance.
        :param t_2: The second TimeOnly instance..
        :returns: The elapsed time between t1 and t_2.
        """
        ...

    @overload
    def __le__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __le__(self, right: System.TimeOnly) -> bool:
        """
        Determines whether one specified TimeOnly represents a time that is the same as or earlier than another specified TimeOnly.
        
        :param left: The first object to compare.
        :param right: The second object to compare.
        :returns: true if left is the same as or earlier than right; otherwise, false.
        """
        ...

    @overload
    def __le__(self, other: System.TimeOnly) -> bool:
        ...

    @overload
    def __lt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __lt__(self, right: System.TimeOnly) -> bool:
        """
        Determines whether one specified TimeOnly is earlier than another specified TimeOnly.
        
        :param left: The first object to compare.
        :param right: The second object to compare.
        :returns: true if left is earlier than right; otherwise, false.
        """
        ...

    @overload
    def __lt__(self, other: System.TimeOnly) -> bool:
        ...

    def __ne__(self, right: System.TimeOnly) -> bool:
        """
        Determines whether two specified instances of TimeOnly are not equal.
        
        :param left: The first object to compare.
        :param right: The second object to compare.
        :returns: true if left and right do not represent the same time; otherwise, false.
        """
        ...

    def __sub__(self, t_2: System.TimeOnly) -> datetime.timedelta:
        """
        Gives the elapsed time between two points on a circular clock, which will always be a positive value.
        
        :param t1: The first TimeOnly instance.
        :param t_2: The second TimeOnly instance..
        :returns: The elapsed time between t1 and t_2.
        """
        ...

    @overload
    def add(self, value: datetime.timedelta) -> System.TimeOnly:
        """
        Returns a new TimeOnly that adds the value of the specified TimeSpan to the value of this instance.
        
        :param value: A positive or negative time interval.
        :returns: An object whose value is the sum of the time represented by this instance and the time interval represented by value.
        """
        ...

    @overload
    def add(self, value: datetime.timedelta, wrapped_days: typing.Optional[int]) -> typing.Tuple[System.TimeOnly, int]:
        """
        Returns a new TimeOnly that adds the value of the specified TimeSpan to the value of this instance.
        If the result wraps past the end of the day, this method will return the number of excess days as an out parameter.
        
        :param value: A positive or negative time interval.
        :param wrapped_days: When this method returns, contains the number of excess days if any that resulted from wrapping during this addition operation.
        :returns: An object whose value is the sum of the time represented by this instance and the time interval represented by value.
        """
        ...

    @overload
    def add_hours(self, value: float) -> System.TimeOnly:
        """
        Returns a new TimeOnly that adds the specified number of hours to the value of this instance.
        
        :param value: A number of whole and fractional hours. The value parameter can be negative or positive.
        :returns: An object whose value is the sum of the time represented by this instance and the number of hours represented by value.
        """
        ...

    @overload
    def add_hours(self, value: float, wrapped_days: typing.Optional[int]) -> typing.Tuple[System.TimeOnly, int]:
        """
        Returns a new TimeOnly that adds the specified number of hours to the value of this instance.
        If the result wraps past the end of the day, this method will return the number of excess days as an out parameter.
        
        :param value: A number of whole and fractional hours. The value parameter can be negative or positive.
        :param wrapped_days: When this method returns, contains the number of excess days if any that resulted from wrapping during this addition operation.
        :returns: An object whose value is the sum of the time represented by this instance and the number of hours represented by value.
        """
        ...

    @overload
    def add_minutes(self, value: float) -> System.TimeOnly:
        """
        Returns a new TimeOnly that adds the specified number of minutes to the value of this instance.
        
        :param value: A number of whole and fractional minutes. The value parameter can be negative or positive.
        :returns: An object whose value is the sum of the time represented by this instance and the number of minutes represented by value.
        """
        ...

    @overload
    def add_minutes(self, value: float, wrapped_days: typing.Optional[int]) -> typing.Tuple[System.TimeOnly, int]:
        """
        Returns a new TimeOnly that adds the specified number of minutes to the value of this instance.
        If the result wraps past the end of the day, this method will return the number of excess days as an out parameter.
        
        :param value: A number of whole and fractional minutes. The value parameter can be negative or positive.
        :param wrapped_days: When this method returns, contains the number of excess days if any that resulted from wrapping during this addition operation.
        :returns: An object whose value is the sum of the time represented by this instance and the number of minutes represented by value.
        """
        ...

    @overload
    def compare_to(self, value: typing.Any) -> int:
        """
        Compares the value of this instance to a specified object that contains a specified TimeOnly value, and returns an integer that indicates whether this instance is earlier than, the same as, or later than the specified TimeOnly value.
        
        :param value: A boxed object to compare, or null.
        :returns: A signed number indicating the relative values of this instance and the value parameter. Less than zero if this instance is earlier than value. Zero if this instance is the same as value. Greater than zero if this instance is later than value.
        """
        ...

    @overload
    def compare_to(self, value: System.TimeOnly) -> int:
        """
        Compares the value of this instance to a specified TimeOnly value and indicates whether this instance is earlier than, the same as, or later than the specified TimeOnly value.
        
        :param value: The object to compare to the current instance.
        :returns: A signed number indicating the relative values of this instance and the value parameter. Less than zero if this instance is earlier than value. Zero if this instance is the same as value. Greater than zero if this instance is later than value.
        """
        ...

    @overload
    def deconstruct(self, hour: typing.Optional[int], minute: typing.Optional[int]) -> typing.Tuple[None, int, int]:
        """
        Deconstructs TimeOnly by Hour and Minute.
        
        :param hour: Deconstructed parameter for Hour.
        :param minute: Deconstructed parameter for Minute.
        """
        ...

    @overload
    def deconstruct(self, hour: typing.Optional[int], minute: typing.Optional[int], second: typing.Optional[int]) -> typing.Tuple[None, int, int, int]:
        """
        Deconstructs TimeOnly by Hour, Minute and Second.
        
        :param hour: Deconstructed parameter for Hour.
        :param minute: Deconstructed parameter for Minute.
        :param second: Deconstructed parameter for Second.
        """
        ...

    @overload
    def deconstruct(self, hour: typing.Optional[int], minute: typing.Optional[int], second: typing.Optional[int], millisecond: typing.Optional[int]) -> typing.Tuple[None, int, int, int, int]:
        """
        Deconstructs TimeOnly by Hour, Minute, Second and Millisecond.
        
        :param hour: Deconstructed parameter for Hour.
        :param minute: Deconstructed parameter for Minute.
        :param second: Deconstructed parameter for Second.
        :param millisecond: Deconstructed parameter for Millisecond.
        """
        ...

    @overload
    def deconstruct(self, hour: typing.Optional[int], minute: typing.Optional[int], second: typing.Optional[int], millisecond: typing.Optional[int], microsecond: typing.Optional[int]) -> typing.Tuple[None, int, int, int, int, int]:
        """
        Deconstructs TimeOnly by Hour, Minute, Second, Millisecond and Microsecond.
        
        :param hour: Deconstructed parameter for Hour.
        :param minute: Deconstructed parameter for Minute.
        :param second: Deconstructed parameter for Second.
        :param millisecond: Deconstructed parameter for Millisecond.
        :param microsecond: Deconstructed parameter for Microsecond.
        """
        ...

    @overload
    def equals(self, value: typing.Any) -> bool:
        """
        Returns a value indicating whether this instance is equal to a specified object.
        
        :param value: The object to compare to this instance.
        :returns: true if value is an instance of TimeOnly and equals the value of this instance; otherwise, false.
        """
        ...

    @overload
    def equals(self, value: System.TimeOnly) -> bool:
        """
        Returns a value indicating whether the value of this instance is equal to the value of the specified TimeOnly instance.
        
        :param value: The object to compare to this instance.
        :returns: true if the value parameter equals the value of this instance; otherwise, false.
        """
        ...

    @staticmethod
    def from_date_time(date_time: typing.Union[datetime.datetime, datetime.date]) -> System.TimeOnly:
        """
        Constructs a TimeOnly object from a DateTime representing the time of the day in this DateTime object.
        
        :param date_time: The time DateTime object to extract the time of the day from.
        :returns: A TimeOnly object representing time of the day specified in the DateTime object.
        """
        ...

    @staticmethod
    def from_time_span(time_span: datetime.timedelta) -> System.TimeOnly:
        """
        Constructs a TimeOnly object from a TimeSpan representing the time elapsed since midnight.
        
        :param time_span: The time interval measured since midnight. This value has to be positive and not exceeding the time of the day.
        :returns: A TimeOnly object representing the time elapsed since midnight using the time_span value.
        """
        ...

    def get_hash_code(self) -> int:
        """
        Returns the hash code for this instance.
        
        :returns: A 32-bit signed integer hash code.
        """
        ...

    def is_between(self, start: System.TimeOnly, end: System.TimeOnly) -> bool:
        """
        Determines if a time falls within the range provided.
        Supports both "normal" ranges such as 10:00-12:00, and ranges that span midnight such as 23:00-01:00.
        
        :param start: The starting time of day, inclusive.
        :param end: The ending time of day, exclusive.
        :returns: True, if the time falls within the range, false otherwise.
        """
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider = ..., style: System.Globalization.DateTimeStyles = ...) -> System.TimeOnly:
        """
        Converts a memory span that contains string representation of a time to its TimeOnly equivalent by using culture-specific format information and a formatting style.
        
        :param s: The memory span that contains the string to parse.
        :param provider: An object that supplies culture-specific format information about s.
        :param style: A bitwise combination of enumeration values that indicates the permitted format of s. A typical value to specify is None.
        :returns: An object that is equivalent to the time contained in s, as specified by provider and styles.
        """
        ...

    @staticmethod
    @overload
    def parse(s: str) -> System.TimeOnly:
        """
        Converts a string that contains string representation of a time to its TimeOnly equivalent by using the conventions of the current culture.
        
        :param s: The string that contains the string to parse.
        :returns: An object that is equivalent to the time contained in s.
        """
        ...

    @staticmethod
    @overload
    def parse(s: str, provider: System.IFormatProvider, style: System.Globalization.DateTimeStyles = ...) -> System.TimeOnly:
        """
        Converts a string that contains string representation of a time to its TimeOnly equivalent by using culture-specific format information and a formatting style.
        
        :param s: The string that contains the string to parse.
        :param provider: An object that supplies culture-specific format information about s.
        :param style: A bitwise combination of the enumeration values that indicates the style elements that can be present in s for the parse operation to succeed, and that defines how to interpret the parsed date. A typical value to specify is None.
        :returns: An object that is equivalent to the time contained in s, as specified by provider and styles.
        """
        ...

    @staticmethod
    @overload
    def parse(s: str, provider: System.IFormatProvider) -> System.TimeOnly:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider) -> System.TimeOnly:
        ...

    @staticmethod
    @overload
    def parse_exact(s: System.ReadOnlySpan[str], format: System.ReadOnlySpan[str], provider: System.IFormatProvider = ..., style: System.Globalization.DateTimeStyles = ...) -> System.TimeOnly:
        """
        Converts the specified span representation of a time to its TimeOnly equivalent using the specified format, culture-specific format information, and style.
        The format of the string representation must match the specified format exactly or an exception is thrown.
        
        :param s: A span containing the characters that represent a time to convert.
        :param format: A span containing the characters that represent a format specifier that defines the required format of s.
        :param provider: An object that supplies culture-specific formatting information about s.
        :param style: A bitwise combination of enumeration values that indicates the permitted format of s. A typical value to specify is None.
        :returns: An object that is equivalent to the time contained in s, as specified by format, provider, and style.
        """
        ...

    @staticmethod
    @overload
    def parse_exact(s: System.ReadOnlySpan[str], formats: typing.List[str]) -> System.TimeOnly:
        """
        Converts the specified span representation of a time to its TimeOnly equivalent using the specified array of formats.
        The format of the string representation must match at least one of the specified formats exactly or an exception is thrown.
        
        :param s: A span containing the characters that represent a time to convert.
        :param formats: An array of allowable formats of s.
        :returns: An object that is equivalent to the time contained in s, as specified by format, provider, and style.
        """
        ...

    @staticmethod
    @overload
    def parse_exact(s: System.ReadOnlySpan[str], formats: typing.List[str], provider: System.IFormatProvider, style: System.Globalization.DateTimeStyles = ...) -> System.TimeOnly:
        """
        Converts the specified span representation of a time to its TimeOnly equivalent using the specified array of formats, culture-specific format information, and style.
        The format of the string representation must match at least one of the specified formats exactly or an exception is thrown.
        
        :param s: A span containing the characters that represent a time to convert.
        :param formats: An array of allowable formats of s.
        :param provider: An object that supplies culture-specific formatting information about s.
        :param style: A bitwise combination of enumeration values that indicates the permitted format of s. A typical value to specify is None.
        :returns: An object that is equivalent to the time contained in s, as specified by format, provider, and style.
        """
        ...

    @staticmethod
    @overload
    def parse_exact(s: str, format: str) -> System.TimeOnly:
        """
        Converts the specified string representation of a time to its TimeOnly equivalent using the specified format.
        The format of the string representation must match the specified format exactly or an exception is thrown.
        
        :param s: A string containing the characters that represent a time to convert.
        :param format: A string that represent a format specifier that defines the required format of s.
        :returns: An object that is equivalent to the time contained in s, as specified by format.
        """
        ...

    @staticmethod
    @overload
    def parse_exact(s: str, format: str, provider: System.IFormatProvider, style: System.Globalization.DateTimeStyles = ...) -> System.TimeOnly:
        """
        Converts the specified string representation of a time to its TimeOnly equivalent using the specified format, culture-specific format information, and style.
        The format of the string representation must match the specified format exactly or an exception is thrown.
        
        :param s: A string containing the characters that represent a time to convert.
        :param format: A string containing the characters that represent a format specifier that defines the required format of s.
        :param provider: An object that supplies culture-specific formatting information about s.
        :param style: A bitwise combination of the enumeration values that provides additional information about s, about style elements that may be present in s, or about the conversion from s to a TimeOnly value. A typical value to specify is None.
        :returns: An object that is equivalent to the time contained in s, as specified by format, provider, and style.
        """
        ...

    @staticmethod
    @overload
    def parse_exact(s: str, formats: typing.List[str]) -> System.TimeOnly:
        """
        Converts the specified span representation of a time to its TimeOnly equivalent using the specified array of formats.
        The format of the string representation must match at least one of the specified formats exactly or an exception is thrown.
        
        :param s: A span containing the characters that represent a time to convert.
        :param formats: An array of allowable formats of s.
        :returns: An object that is equivalent to the time contained in s, as specified by format, provider, and style.
        """
        ...

    @staticmethod
    @overload
    def parse_exact(s: str, formats: typing.List[str], provider: System.IFormatProvider, style: System.Globalization.DateTimeStyles = ...) -> System.TimeOnly:
        """
        Converts the specified string representation of a time to its TimeOnly equivalent using the specified array of formats, culture-specific format information, and style.
        The format of the string representation must match at least one of the specified formats exactly or an exception is thrown.
        
        :param s: A string containing the characters that represent a time to convert.
        :param formats: An array of allowable formats of s.
        :param provider: An object that supplies culture-specific formatting information about s.
        :param style: A bitwise combination of enumeration values that indicates the permitted format of s. A typical value to specify is None.
        :returns: An object that is equivalent to the time contained in s, as specified by format, provider, and style.
        """
        ...

    def to_long_time_string(self) -> str:
        """
        Converts the value of the current TimeOnly object to its equivalent long date string representation.
        
        :returns: A string that contains the long time string representation of the current TimeOnly object.
        """
        ...

    def to_short_time_string(self) -> str:
        """
        Converts the value of the current TimeOnly object to its equivalent short time string representation.
        
        :returns: A string that contains the short time string representation of the current TimeOnly object.
        """
        ...

    @overload
    def to_string(self) -> str:
        """
        Converts the value of the current TimeOnly object to its equivalent string representation using the formatting conventions of the current culture.
        The TimeOnly object will be formatted in short form.
        
        :returns: A string that contains the short time string representation of the current TimeOnly object.
        """
        ...

    @overload
    def to_string(self, format: str) -> str:
        """
        Converts the value of the current TimeOnly object to its equivalent string representation using the specified format and the formatting conventions of the current culture.
        
        :param format: A standard or custom time format string.
        :returns: A string representation of value of the current TimeOnly object as specified by format.
        """
        ...

    @overload
    def to_string(self, provider: System.IFormatProvider) -> str:
        """
        Converts the value of the current TimeOnly object to its equivalent string representation using the specified culture-specific format information.
        
        :param provider: An object that supplies culture-specific formatting information.
        :returns: A string representation of value of the current TimeOnly object as specified by provider.
        """
        ...

    @overload
    def to_string(self, format: str, provider: System.IFormatProvider) -> str:
        """
        Converts the value of the current TimeOnly object to its equivalent string representation using the specified culture-specific format information.
        
        :param format: A standard or custom time format string.
        :param provider: An object that supplies culture-specific formatting information.
        :returns: A string representation of value of the current TimeOnly object as specified by format and provider.
        """
        ...

    def to_time_span(self) -> datetime.timedelta:
        """
        Convert the current TimeOnly instance to a TimeSpan object.
        
        :returns: A TimeSpan object spanning to the time specified in the current TimeOnly object.
        """
        ...

    @overload
    def try_format(self, destination: System.Span[str], chars_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        """
        Tries to format the value of the current TimeOnly instance into the provided span of characters.
        
        :param destination: When this method returns, this instance's value formatted as a span of characters.
        :param chars_written: When this method returns, the number of characters that were written in destination.
        :param format: A span containing the characters that represent a standard or custom format string that defines the acceptable format for destination.
        :param provider: An optional object that supplies culture-specific formatting information for destination.
        :returns: true if the formatting was successful; otherwise, false.
        """
        ...

    @overload
    def try_format(self, utf_8_destination: System.Span[int], bytes_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], result: typing.Optional[System.TimeOnly]) -> typing.Tuple[bool, System.TimeOnly]:
        """
        Converts the specified span representation of a time to its TimeOnly equivalent and returns a value that indicates whether the conversion succeeded.
        
        :param s: A span containing the characters representing the time to convert.
        :param result: When this method returns, contains the TimeOnly value equivalent to the time contained in s, if the conversion succeeded, or MinValue if the conversion failed. The conversion fails if the s parameter is empty string, or does not contain a valid string representation of a time. This parameter is passed uninitialized.
        :returns: true if the s parameter was converted successfully; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider, style: System.Globalization.DateTimeStyles, result: typing.Optional[System.TimeOnly]) -> typing.Tuple[bool, System.TimeOnly]:
        """
        Converts the specified span representation of a time to its TimeOnly equivalent using the specified array of formats, culture-specific format information, and style. And returns a value that indicates whether the conversion succeeded.
        
        :param s: A string containing the characters that represent a time to convert.
        :param provider: An object that supplies culture-specific formatting information about s.
        :param style: A bitwise combination of enumeration values that indicates the permitted format of s. A typical value to specify is None.
        :param result: When this method returns, contains the TimeOnly value equivalent to the time contained in s, if the conversion succeeded, or MinValue if the conversion failed. The conversion fails if the s parameter is empty string, or does not contain a valid string representation of a date. This parameter is passed uninitialized.
        :returns: true if the s parameter was converted successfully; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def try_parse(s: str, result: typing.Optional[System.TimeOnly]) -> typing.Tuple[bool, System.TimeOnly]:
        """
        Converts the specified string representation of a time to its TimeOnly equivalent and returns a value that indicates whether the conversion succeeded.
        
        :param s: A string containing the characters representing the time to convert.
        :param result: When this method returns, contains the TimeOnly value equivalent to the time contained in s, if the conversion succeeded, or MinValue if the conversion failed. The conversion fails if the s parameter is empty string, or does not contain a valid string representation of a time. This parameter is passed uninitialized.
        :returns: true if the s parameter was converted successfully; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def try_parse(s: str, provider: System.IFormatProvider, style: System.Globalization.DateTimeStyles, result: typing.Optional[System.TimeOnly]) -> typing.Tuple[bool, System.TimeOnly]:
        """
        Converts the specified string representation of a time to its TimeOnly equivalent using the specified array of formats, culture-specific format information, and style. And returns a value that indicates whether the conversion succeeded.
        
        :param s: A string containing the characters that represent a time to convert.
        :param provider: An object that supplies culture-specific formatting information about s.
        :param style: A bitwise combination of enumeration values that indicates the permitted format of s. A typical value to specify is None.
        :param result: When this method returns, contains the TimeOnly value equivalent to the time contained in s, if the conversion succeeded, or MinValue if the conversion failed. The conversion fails if the s parameter is empty string, or does not contain a valid string representation of a time. This parameter is passed uninitialized.
        :returns: true if the s parameter was converted successfully; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def try_parse(s: str, provider: System.IFormatProvider, result: typing.Optional[System.TimeOnly]) -> typing.Tuple[bool, System.TimeOnly]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider, result: typing.Optional[System.TimeOnly]) -> typing.Tuple[bool, System.TimeOnly]:
        ...

    @staticmethod
    @overload
    def try_parse_exact(s: System.ReadOnlySpan[str], format: System.ReadOnlySpan[str], result: typing.Optional[System.TimeOnly]) -> typing.Tuple[bool, System.TimeOnly]:
        """
        Converts the specified span representation of a time to its TimeOnly equivalent using the specified format and style.
        The format of the string representation must match the specified format exactly. The method returns a value that indicates whether the conversion succeeded.
        
        :param s: A span containing the characters representing a time to convert.
        :param format: The required format of s.
        :param result: When this method returns, contains the TimeOnly value equivalent to the time contained in s, if the conversion succeeded, or MinValue if the conversion failed. The conversion fails if the s is empty string, or does not contain a time that correspond to the pattern specified in format. This parameter is passed uninitialized.
        :returns: true if s was converted successfully; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def try_parse_exact(s: System.ReadOnlySpan[str], format: System.ReadOnlySpan[str], provider: System.IFormatProvider, style: System.Globalization.DateTimeStyles, result: typing.Optional[System.TimeOnly]) -> typing.Tuple[bool, System.TimeOnly]:
        """
        Converts the specified span representation of a time to its TimeOnly equivalent using the specified format, culture-specific format information, and style.
        The format of the string representation must match the specified format exactly. The method returns a value that indicates whether the conversion succeeded.
        
        :param s: A span containing the characters representing a time to convert.
        :param format: The required format of s.
        :param provider: An object that supplies culture-specific formatting information about s.
        :param style: A bitwise combination of one or more enumeration values that indicate the permitted format of s.
        :param result: When this method returns, contains the TimeOnly value equivalent to the time contained in s, if the conversion succeeded, or MinValue if the conversion failed. The conversion fails if the s is empty string, or does not contain a time that correspond to the pattern specified in format. This parameter is passed uninitialized.
        :returns: true if s was converted successfully; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def try_parse_exact(s: System.ReadOnlySpan[str], formats: typing.List[str], result: typing.Optional[System.TimeOnly]) -> typing.Tuple[bool, System.TimeOnly]:
        """
        Converts the specified char span of a time to its TimeOnly equivalent and returns a value that indicates whether the conversion succeeded.
        
        :param s: The span containing the string to parse.
        :param formats: An array of allowable formats of s.
        :param result: When this method returns, contains the TimeOnly value equivalent to the time contained in s, if the conversion succeeded, or MinValue if the conversion failed. The conversion fails if the s parameter is Empty, or does not contain a valid string representation of a time. This parameter is passed uninitialized.
        :returns: true if the s parameter was converted successfully; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def try_parse_exact(s: System.ReadOnlySpan[str], formats: typing.List[str], provider: System.IFormatProvider, style: System.Globalization.DateTimeStyles, result: typing.Optional[System.TimeOnly]) -> typing.Tuple[bool, System.TimeOnly]:
        """
        Converts the specified char span of a time to its TimeOnly equivalent and returns a value that indicates whether the conversion succeeded.
        
        :param s: The span containing the string to parse.
        :param formats: An array of allowable formats of s.
        :param provider: An object that supplies culture-specific formatting information about s.
        :param style: A bitwise combination of enumeration values that defines how to interpret the parsed time. A typical value to specify is None.
        :param result: When this method returns, contains the TimeOnly value equivalent to the time contained in s, if the conversion succeeded, or MinValue if the conversion failed. The conversion fails if the s parameter is Empty, or does not contain a valid string representation of a time. This parameter is passed uninitialized.
        :returns: true if the s parameter was converted successfully; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def try_parse_exact(s: str, format: str, result: typing.Optional[System.TimeOnly]) -> typing.Tuple[bool, System.TimeOnly]:
        """
        Converts the specified string representation of a time to its TimeOnly equivalent using the specified format and style.
        The format of the string representation must match the specified format exactly. The method returns a value that indicates whether the conversion succeeded.
        
        :param s: A string containing the characters representing a time to convert.
        :param format: The required format of s.
        :param result: When this method returns, contains the TimeOnly value equivalent to the time contained in s, if the conversion succeeded, or MinValue if the conversion failed. The conversion fails if the s is empty string, or does not contain a time that correspond to the pattern specified in format. This parameter is passed uninitialized.
        :returns: true if s was converted successfully; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def try_parse_exact(s: str, format: str, provider: System.IFormatProvider, style: System.Globalization.DateTimeStyles, result: typing.Optional[System.TimeOnly]) -> typing.Tuple[bool, System.TimeOnly]:
        """
        Converts the specified span representation of a time to its TimeOnly equivalent using the specified format, culture-specific format information, and style.
        The format of the string representation must match the specified format exactly. The method returns a value that indicates whether the conversion succeeded.
        
        :param s: A span containing the characters representing a time to convert.
        :param format: The required format of s.
        :param provider: An object that supplies culture-specific formatting information about s.
        :param style: A bitwise combination of one or more enumeration values that indicate the permitted format of s.
        :param result: When this method returns, contains the TimeOnly value equivalent to the time contained in s, if the conversion succeeded, or MinValue if the conversion failed. The conversion fails if the s is empty string, or does not contain a time that correspond to the pattern specified in format. This parameter is passed uninitialized.
        :returns: true if s was converted successfully; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def try_parse_exact(s: str, formats: typing.List[str], result: typing.Optional[System.TimeOnly]) -> typing.Tuple[bool, System.TimeOnly]:
        """
        Converts the specified string of a time to its TimeOnly equivalent and returns a value that indicates whether the conversion succeeded.
        
        :param s: The string containing time to parse.
        :param formats: An array of allowable formats of s.
        :param result: When this method returns, contains the timeOnly value equivalent to the time contained in s, if the conversion succeeded, or MinValue if the conversion failed. The conversion fails if the s parameter is Empty, or does not contain a valid string representation of a time. This parameter is passed uninitialized.
        :returns: true if the s parameter was converted successfully; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def try_parse_exact(s: str, formats: typing.List[str], provider: System.IFormatProvider, style: System.Globalization.DateTimeStyles, result: typing.Optional[System.TimeOnly]) -> typing.Tuple[bool, System.TimeOnly]:
        """
        Converts the specified string of a time to its TimeOnly equivalent and returns a value that indicates whether the conversion succeeded.
        
        :param s: The string containing the time to parse.
        :param formats: An array of allowable formats of s.
        :param provider: An object that supplies culture-specific formatting information about s.
        :param style: A bitwise combination of enumeration values that defines how to interpret the parsed date. A typical value to specify is None.
        :param result: When this method returns, contains the TimeOnly value equivalent to the time contained in s, if the conversion succeeded, or MinValue if the conversion failed. The conversion fails if the s parameter is Empty, or does not contain a valid string representation of a time. This parameter is passed uninitialized.
        :returns: true if the s parameter was converted successfully; otherwise, false.
        """
        ...


class DateOnly(System.IComparable[System_DateOnly], System.IEquatable[System_DateOnly], System.ISpanFormattable, System.ISpanParsable[System_DateOnly], System.IUtf8SpanFormattable):
    """Represents dates with values ranging from January 1, 0001 Anno Domini (Common Era) through December 31, 9999 A.D. (C.E.) in the Gregorian calendar."""

    MIN_VALUE: System.DateOnly
    """Gets the earliest possible date that can be created."""

    MAX_VALUE: System.DateOnly
    """Gets the latest possible date that can be created."""

    @property
    def year(self) -> int:
        """Gets the year component of the date represented by this instance."""
        ...

    @property
    def month(self) -> int:
        """Gets the month component of the date represented by this instance."""
        ...

    @property
    def day(self) -> int:
        """Gets the day component of the date represented by this instance."""
        ...

    @property
    def day_of_week(self) -> System.DayOfWeek:
        """Gets the day of the week represented by this instance."""
        ...

    @property
    def day_of_year(self) -> int:
        """Gets the day of the year represented by this instance."""
        ...

    @property
    def day_number(self) -> int:
        """Gets the number of days since January 1, 0001 in the Proleptic Gregorian calendar represented by this instance."""
        ...

    def __eq__(self, right: System.DateOnly) -> bool:
        """
        Determines whether two specified instances of DateOnly are equal.
        
        :param left: The first object to compare.
        :param right: The second object to compare.
        :returns: true if left and right represent the same date; otherwise, false.
        """
        ...

    @overload
    def __ge__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __ge__(self, right: System.DateOnly) -> bool:
        """
        Determines whether one specified DateOnly represents a date that is the same as or later than another specified DateOnly.
        
        :param left: The first object to compare.
        :param right: The second object to compare.
        :returns: true if left is the same as or later than right; otherwise, false.
        """
        ...

    @overload
    def __ge__(self, other: System.DateOnly) -> bool:
        ...

    @overload
    def __gt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __gt__(self, right: System.DateOnly) -> bool:
        """
        Determines whether one specified DateOnly is later than another specified DateOnly.
        
        :param left: The first object to compare.
        :param right: The second object to compare.
        :returns: true if left is later than right; otherwise, false.
        """
        ...

    @overload
    def __gt__(self, other: System.DateOnly) -> bool:
        ...

    @overload
    def __init__(self, year: int, month: int, day: int) -> None:
        """
        Creates a new instance of the DateOnly structure to the specified year, month, and day.
        
        :param year: The year (1 through 9999).
        :param month: The month (1 through 12).
        :param day: The day (1 through the number of days in ).
        """
        ...

    @overload
    def __init__(self, year: int, month: int, day: int, calendar: System.Globalization.Calendar) -> None:
        """
        Creates a new instance of the DateOnly structure to the specified year, month, and day for the specified calendar.
        
        :param year: The year (1 through the number of years in calendar).
        :param month: The month (1 through the number of months in calendar).
        :param day: The day (1 through the number of days in ).
        :param calendar: The calendar that is used to interpret year, month, and day..
        """
        ...

    @overload
    def __le__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __le__(self, right: System.DateOnly) -> bool:
        """
        Determines whether one specified DateOnly represents a date that is the same as or earlier than another specified DateOnly.
        
        :param left: The first object to compare.
        :param right: The second object to compare.
        :returns: true if left is the same as or earlier than right; otherwise, false.
        """
        ...

    @overload
    def __le__(self, other: System.DateOnly) -> bool:
        ...

    @overload
    def __lt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __lt__(self, right: System.DateOnly) -> bool:
        """
        Determines whether one specified DateOnly is earlier than another specified DateOnly.
        
        :param left: The first object to compare.
        :param right: The second object to compare.
        :returns: true if left is earlier than right; otherwise, false.
        """
        ...

    @overload
    def __lt__(self, other: System.DateOnly) -> bool:
        ...

    def __ne__(self, right: System.DateOnly) -> bool:
        """
        Determines whether two specified instances of DateOnly are not equal.
        
        :param left: The first object to compare.
        :param right: The second object to compare.
        :returns: true if left and right do not represent the same date; otherwise, false.
        """
        ...

    def add_days(self, value: int) -> System.DateOnly:
        """
        Adds the specified number of days to the value of this instance.
        
        :param value: The number of days to add. To subtract days, specify a negative number.
        :returns: An instance whose value is the sum of the date represented by this instance and the number of days represented by value.
        """
        ...

    def add_months(self, value: int) -> System.DateOnly:
        """
        Adds the specified number of months to the value of this instance.
        
        :param value: A number of months. The months parameter can be negative or positive.
        :returns: An object whose value is the sum of the date represented by this instance and months.
        """
        ...

    def add_years(self, value: int) -> System.DateOnly:
        """
        Adds the specified number of years to the value of this instance.
        
        :param value: A number of years. The value parameter can be negative or positive.
        :returns: An object whose value is the sum of the date represented by this instance and the number of years represented by value.
        """
        ...

    @overload
    def compare_to(self, value: typing.Any) -> int:
        """
        Compares the value of this instance to a specified object that contains a specified DateOnly value, and returns an integer that indicates whether this instance is earlier than, the same as, or later than the specified DateOnly value.
        
        :param value: A boxed object to compare, or null.
        :returns: Less than zero if this instance is earlier than value. Greater than zero if this instance is later than value. Zero if this instance is the same as value.
        """
        ...

    @overload
    def compare_to(self, value: System.DateOnly) -> int:
        """
        Compares the value of this instance to a specified DateOnly value and returns an integer that indicates whether this instance is earlier than, the same as, or later than the specified DateTime value.
        
        :param value: The object to compare to the current instance.
        :returns: Less than zero if this instance is earlier than value. Greater than zero if this instance is later than value. Zero if this instance is the same as value.
        """
        ...

    def deconstruct(self, year: typing.Optional[int], month: typing.Optional[int], day: typing.Optional[int]) -> typing.Tuple[None, int, int, int]:
        """
        Deconstructs DateOnly by Year, Month and Day.
        
        :param year: Deconstructed parameter for Year.
        :param month: Deconstructed parameter for Month.
        :param day: Deconstructed parameter for Day.
        """
        ...

    @overload
    def equals(self, value: typing.Any) -> bool:
        """
        Returns a value indicating whether this instance is equal to a specified object.
        
        :param value: The object to compare to this instance.
        :returns: true if value is an instance of DateOnly and equals the value of this instance; otherwise, false.
        """
        ...

    @overload
    def equals(self, value: System.DateOnly) -> bool:
        """
        Returns a value indicating whether the value of this instance is equal to the value of the specified DateOnly instance.
        
        :param value: The object to compare to this instance.
        :returns: true if the value parameter equals the value of this instance; otherwise, false.
        """
        ...

    @staticmethod
    def from_date_time(date_time: typing.Union[datetime.datetime, datetime.date]) -> System.DateOnly:
        """
        Returns a DateOnly instance that is set to the date part of the specified date_time.
        
        :param date_time: The DateTime instance.
        :returns: The DateOnly instance composed of the date part of the specified input time date_time instance.
        """
        ...

    @staticmethod
    def from_day_number(day_number: int) -> System.DateOnly:
        """
        Creates a new instance of the DateOnly structure to the specified number of days.
        
        :param day_number: The number of days since January 1, 0001 in the Proleptic Gregorian calendar.
        """
        ...

    def get_hash_code(self) -> int:
        """
        Returns the hash code for this instance.
        
        :returns: A 32-bit signed integer hash code.
        """
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider = ..., style: System.Globalization.DateTimeStyles = ...) -> System.DateOnly:
        """
        Converts a memory span that contains string representation of a date to its DateOnly equivalent by using culture-specific format information and a formatting style.
        
        :param s: The memory span that contains the string to parse.
        :param provider: An object that supplies culture-specific format information about s.
        :param style: A bitwise combination of enumeration values that indicates the permitted format of s. A typical value to specify is None.
        :returns: An object that is equivalent to the date contained in s, as specified by provider and styles.
        """
        ...

    @staticmethod
    @overload
    def parse(s: str) -> System.DateOnly:
        """
        Converts a string that contains string representation of a date to its DateOnly equivalent by using the conventions of the current culture.
        
        :param s: The string that contains the string to parse.
        :returns: An object that is equivalent to the date contained in s.
        """
        ...

    @staticmethod
    @overload
    def parse(s: str, provider: System.IFormatProvider, style: System.Globalization.DateTimeStyles = ...) -> System.DateOnly:
        """
        Converts a string that contains string representation of a date to its DateOnly equivalent by using culture-specific format information and a formatting style.
        
        :param s: The string that contains the string to parse.
        :param provider: An object that supplies culture-specific format information about s.
        :param style: A bitwise combination of the enumeration values that indicates the style elements that can be present in s for the parse operation to succeed, and that defines how to interpret the parsed date. A typical value to specify is None.
        :returns: An object that is equivalent to the date contained in s, as specified by provider and styles.
        """
        ...

    @staticmethod
    @overload
    def parse(s: str, provider: System.IFormatProvider) -> System.DateOnly:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider) -> System.DateOnly:
        ...

    @staticmethod
    @overload
    def parse_exact(s: System.ReadOnlySpan[str], format: System.ReadOnlySpan[str], provider: System.IFormatProvider = ..., style: System.Globalization.DateTimeStyles = ...) -> System.DateOnly:
        """
        Converts the specified span representation of a date to its DateOnly equivalent using the specified format, culture-specific format information, and style.
        The format of the string representation must match the specified format exactly or an exception is thrown.
        
        :param s: A span containing the characters that represent a date to convert.
        :param format: A span containing the characters that represent a format specifier that defines the required format of s.
        :param provider: An object that supplies culture-specific formatting information about s.
        :param style: A bitwise combination of enumeration values that indicates the permitted format of s. A typical value to specify is None.
        :returns: An object that is equivalent to the date contained in s, as specified by format, provider, and style.
        """
        ...

    @staticmethod
    @overload
    def parse_exact(s: System.ReadOnlySpan[str], formats: typing.List[str]) -> System.DateOnly:
        """
        Converts the specified span representation of a date to its DateOnly equivalent using the specified array of formats.
        The format of the string representation must match at least one of the specified formats exactly or an exception is thrown.
        
        :param s: A span containing the characters that represent a date to convert.
        :param formats: An array of allowable formats of s.
        :returns: An object that is equivalent to the date contained in s, as specified by format, provider, and style.
        """
        ...

    @staticmethod
    @overload
    def parse_exact(s: System.ReadOnlySpan[str], formats: typing.List[str], provider: System.IFormatProvider, style: System.Globalization.DateTimeStyles = ...) -> System.DateOnly:
        """
        Converts the specified span representation of a date to its DateOnly equivalent using the specified array of formats, culture-specific format information, and style.
        The format of the string representation must match at least one of the specified formats exactly or an exception is thrown.
        
        :param s: A span containing the characters that represent a date to convert.
        :param formats: An array of allowable formats of s.
        :param provider: An object that supplies culture-specific formatting information about s.
        :param style: A bitwise combination of enumeration values that indicates the permitted format of s. A typical value to specify is None.
        :returns: An object that is equivalent to the date contained in s, as specified by format, provider, and style.
        """
        ...

    @staticmethod
    @overload
    def parse_exact(s: str, format: str) -> System.DateOnly:
        """
        Converts the specified string representation of a date to its DateOnly equivalent using the specified format.
        The format of the string representation must match the specified format exactly or an exception is thrown.
        
        :param s: A string containing the characters that represent a date to convert.
        :param format: A string that represent a format specifier that defines the required format of s.
        :returns: An object that is equivalent to the date contained in s, as specified by format.
        """
        ...

    @staticmethod
    @overload
    def parse_exact(s: str, format: str, provider: System.IFormatProvider, style: System.Globalization.DateTimeStyles = ...) -> System.DateOnly:
        """
        Converts the specified string representation of a date to its DateOnly equivalent using the specified format, culture-specific format information, and style.
        The format of the string representation must match the specified format exactly or an exception is thrown.
        
        :param s: A string containing the characters that represent a date to convert.
        :param format: A string containing the characters that represent a format specifier that defines the required format of s.
        :param provider: An object that supplies culture-specific formatting information about s.
        :param style: A bitwise combination of the enumeration values that provides additional information about s, about style elements that may be present in s, or about the conversion from s to a DateOnly value. A typical value to specify is None.
        :returns: An object that is equivalent to the date contained in s, as specified by format, provider, and style.
        """
        ...

    @staticmethod
    @overload
    def parse_exact(s: str, formats: typing.List[str]) -> System.DateOnly:
        """
        Converts the specified span representation of a date to its DateOnly equivalent using the specified array of formats.
        The format of the string representation must match at least one of the specified formats exactly or an exception is thrown.
        
        :param s: A span containing the characters that represent a date to convert.
        :param formats: An array of allowable formats of s.
        :returns: An object that is equivalent to the date contained in s, as specified by format, provider, and style.
        """
        ...

    @staticmethod
    @overload
    def parse_exact(s: str, formats: typing.List[str], provider: System.IFormatProvider, style: System.Globalization.DateTimeStyles = ...) -> System.DateOnly:
        """
        Converts the specified string representation of a date to its DateOnly equivalent using the specified array of formats, culture-specific format information, and style.
        The format of the string representation must match at least one of the specified formats exactly or an exception is thrown.
        
        :param s: A string containing the characters that represent a date to convert.
        :param formats: An array of allowable formats of s.
        :param provider: An object that supplies culture-specific formatting information about s.
        :param style: A bitwise combination of enumeration values that indicates the permitted format of s. A typical value to specify is None.
        :returns: An object that is equivalent to the date contained in s, as specified by format, provider, and style.
        """
        ...

    @overload
    def to_date_time(self, time: System.TimeOnly) -> datetime.datetime:
        """
        Returns a DateTime that is set to the date of this DateOnly instance and the time of specified input time.
        
        :param time: The time of the day.
        :returns: The DateTime instance composed of the date of the current DateOnly instance and the time specified by the input time.
        """
        ...

    @overload
    def to_date_time(self, time: System.TimeOnly, kind: System.DateTimeKind) -> datetime.datetime:
        """
        Returns a DateTime instance with the specified input kind that is set to the date of this DateOnly instance and the time of specified input time.
        
        :param time: The time of the day.
        :param kind: One of the enumeration values that indicates whether ticks specifies a local time, Coordinated Universal Time (UTC), or neither.
        :returns: The DateTime instance composed of the date of the current DateOnly instance and the time specified by the input time.
        """
        ...

    def to_long_date_string(self) -> str:
        """
        Converts the value of the current DateOnly object to its equivalent long date string representation.
        
        :returns: A string that contains the long date string representation of the current DateOnly object.
        """
        ...

    def to_short_date_string(self) -> str:
        """
        Converts the value of the current DateOnly object to its equivalent short date string representation.
        
        :returns: A string that contains the short date string representation of the current DateOnly object.
        """
        ...

    @overload
    def to_string(self) -> str:
        """
        Converts the value of the current DateOnly object to its equivalent string representation using the formatting conventions of the current culture.
        The DateOnly object will be formatted in short form.
        
        :returns: A string that contains the short date string representation of the current DateOnly object.
        """
        ...

    @overload
    def to_string(self, format: str) -> str:
        """
        Converts the value of the current DateOnly object to its equivalent string representation using the specified format and the formatting conventions of the current culture.
        
        :param format: A standard or custom date format string.
        :returns: A string representation of value of the current DateOnly object as specified by format.
        """
        ...

    @overload
    def to_string(self, provider: System.IFormatProvider) -> str:
        """
        Converts the value of the current DateOnly object to its equivalent string representation using the specified culture-specific format information.
        
        :param provider: An object that supplies culture-specific formatting information.
        :returns: A string representation of value of the current DateOnly object as specified by provider.
        """
        ...

    @overload
    def to_string(self, format: str, provider: System.IFormatProvider) -> str:
        """
        Converts the value of the current DateOnly object to its equivalent string representation using the specified culture-specific format information.
        
        :param format: A standard or custom date format string.
        :param provider: An object that supplies culture-specific formatting information.
        :returns: A string representation of value of the current DateOnly object as specified by format and provider.
        """
        ...

    @overload
    def try_format(self, destination: System.Span[str], chars_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        """
        Tries to format the value of the current DateOnly instance into the provided span of characters.
        
        :param destination: When this method returns, this instance's value formatted as a span of characters.
        :param chars_written: When this method returns, the number of characters that were written in destination.
        :param format: A span containing the characters that represent a standard or custom format string that defines the acceptable format for destination.
        :param provider: An optional object that supplies culture-specific formatting information for destination.
        :returns: true if the formatting was successful; otherwise, false.
        """
        ...

    @overload
    def try_format(self, utf_8_destination: System.Span[int], bytes_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], result: typing.Optional[System.DateOnly]) -> typing.Tuple[bool, System.DateOnly]:
        """
        Converts the specified span representation of a date to its DateOnly equivalent and returns a value that indicates whether the conversion succeeded.
        
        :param s: A span containing the characters representing the date to convert.
        :param result: When this method returns, contains the DateOnly value equivalent to the date contained in s, if the conversion succeeded, or MinValue if the conversion failed. The conversion fails if the s parameter is empty string, or does not contain a valid string representation of a date. This parameter is passed uninitialized.
        :returns: true if the s parameter was converted successfully; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider, style: System.Globalization.DateTimeStyles, result: typing.Optional[System.DateOnly]) -> typing.Tuple[bool, System.DateOnly]:
        """
        Converts the specified span representation of a date to its DateOnly equivalent using the specified array of formats, culture-specific format information, and style. And returns a value that indicates whether the conversion succeeded.
        
        :param s: A string containing the characters that represent a date to convert.
        :param provider: An object that supplies culture-specific formatting information about s.
        :param style: A bitwise combination of enumeration values that indicates the permitted format of s. A typical value to specify is None.
        :param result: When this method returns, contains the DateOnly value equivalent to the date contained in s, if the conversion succeeded, or MinValue if the conversion failed. The conversion fails if the s parameter is empty string, or does not contain a valid string representation of a date. This parameter is passed uninitialized.
        :returns: true if the s parameter was converted successfully; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def try_parse(s: str, result: typing.Optional[System.DateOnly]) -> typing.Tuple[bool, System.DateOnly]:
        """
        Converts the specified string representation of a date to its DateOnly equivalent and returns a value that indicates whether the conversion succeeded.
        
        :param s: A string containing the characters representing the date to convert.
        :param result: When this method returns, contains the DateOnly value equivalent to the date contained in s, if the conversion succeeded, or MinValue if the conversion failed. The conversion fails if the s parameter is empty string, or does not contain a valid string representation of a date. This parameter is passed uninitialized.
        :returns: true if the s parameter was converted successfully; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def try_parse(s: str, provider: System.IFormatProvider, style: System.Globalization.DateTimeStyles, result: typing.Optional[System.DateOnly]) -> typing.Tuple[bool, System.DateOnly]:
        """
        Converts the specified string representation of a date to its DateOnly equivalent using the specified array of formats, culture-specific format information, and style. And returns a value that indicates whether the conversion succeeded.
        
        :param s: A string containing the characters that represent a date to convert.
        :param provider: An object that supplies culture-specific formatting information about s.
        :param style: A bitwise combination of enumeration values that indicates the permitted format of s. A typical value to specify is None.
        :param result: When this method returns, contains the DateOnly value equivalent to the date contained in s, if the conversion succeeded, or MinValue if the conversion failed. The conversion fails if the s parameter is empty string, or does not contain a valid string representation of a date. This parameter is passed uninitialized.
        :returns: true if the s parameter was converted successfully; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def try_parse(s: str, provider: System.IFormatProvider, result: typing.Optional[System.DateOnly]) -> typing.Tuple[bool, System.DateOnly]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider, result: typing.Optional[System.DateOnly]) -> typing.Tuple[bool, System.DateOnly]:
        ...

    @staticmethod
    @overload
    def try_parse_exact(s: System.ReadOnlySpan[str], format: System.ReadOnlySpan[str], result: typing.Optional[System.DateOnly]) -> typing.Tuple[bool, System.DateOnly]:
        """
        Converts the specified span representation of a date to its DateOnly equivalent using the specified format and style.
        The format of the string representation must match the specified format exactly. The method returns a value that indicates whether the conversion succeeded.
        
        :param s: A span containing the characters representing a date to convert.
        :param format: The required format of s.
        :param result: When this method returns, contains the DateOnly value equivalent to the date contained in s, if the conversion succeeded, or MinValue if the conversion failed. The conversion fails if the s is empty string, or does not contain a date that correspond to the pattern specified in format. This parameter is passed uninitialized.
        :returns: true if s was converted successfully; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def try_parse_exact(s: System.ReadOnlySpan[str], format: System.ReadOnlySpan[str], provider: System.IFormatProvider, style: System.Globalization.DateTimeStyles, result: typing.Optional[System.DateOnly]) -> typing.Tuple[bool, System.DateOnly]:
        """
        Converts the specified span representation of a date to its DateOnly equivalent using the specified format, culture-specific format information, and style.
        The format of the string representation must match the specified format exactly. The method returns a value that indicates whether the conversion succeeded.
        
        :param s: A span containing the characters representing a date to convert.
        :param format: The required format of s.
        :param provider: An object that supplies culture-specific formatting information about s.
        :param style: A bitwise combination of one or more enumeration values that indicate the permitted format of s.
        :param result: When this method returns, contains the DateOnly value equivalent to the date contained in s, if the conversion succeeded, or MinValue if the conversion failed. The conversion fails if the s is empty string, or does not contain a date that correspond to the pattern specified in format. This parameter is passed uninitialized.
        :returns: true if s was converted successfully; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def try_parse_exact(s: System.ReadOnlySpan[str], formats: typing.List[str], result: typing.Optional[System.DateOnly]) -> typing.Tuple[bool, System.DateOnly]:
        """
        Converts the specified char span of a date to its DateOnly equivalent and returns a value that indicates whether the conversion succeeded.
        
        :param s: The span containing the string to parse.
        :param formats: An array of allowable formats of s.
        :param result: When this method returns, contains the DateOnly value equivalent to the date contained in s, if the conversion succeeded, or MinValue if the conversion failed. The conversion fails if the s parameter is Empty, or does not contain a valid string representation of a date. This parameter is passed uninitialized.
        :returns: true if the s parameter was converted successfully; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def try_parse_exact(s: System.ReadOnlySpan[str], formats: typing.List[str], provider: System.IFormatProvider, style: System.Globalization.DateTimeStyles, result: typing.Optional[System.DateOnly]) -> typing.Tuple[bool, System.DateOnly]:
        """
        Converts the specified char span of a date to its DateOnly equivalent and returns a value that indicates whether the conversion succeeded.
        
        :param s: The span containing the string to parse.
        :param formats: An array of allowable formats of s.
        :param provider: An object that supplies culture-specific formatting information about s.
        :param style: A bitwise combination of enumeration values that defines how to interpret the parsed date. A typical value to specify is None.
        :param result: When this method returns, contains the DateOnly value equivalent to the date contained in s, if the conversion succeeded, or MinValue if the conversion failed. The conversion fails if the s parameter is Empty, or does not contain a valid string representation of a date. This parameter is passed uninitialized.
        :returns: true if the s parameter was converted successfully; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def try_parse_exact(s: str, format: str, result: typing.Optional[System.DateOnly]) -> typing.Tuple[bool, System.DateOnly]:
        """
        Converts the specified string representation of a date to its DateOnly equivalent using the specified format and style.
        The format of the string representation must match the specified format exactly. The method returns a value that indicates whether the conversion succeeded.
        
        :param s: A string containing the characters representing a date to convert.
        :param format: The required format of s.
        :param result: When this method returns, contains the DateOnly value equivalent to the date contained in s, if the conversion succeeded, or MinValue if the conversion failed. The conversion fails if the s is empty string, or does not contain a date that correspond to the pattern specified in format. This parameter is passed uninitialized.
        :returns: true if s was converted successfully; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def try_parse_exact(s: str, format: str, provider: System.IFormatProvider, style: System.Globalization.DateTimeStyles, result: typing.Optional[System.DateOnly]) -> typing.Tuple[bool, System.DateOnly]:
        """
        Converts the specified span representation of a date to its DateOnly equivalent using the specified format, culture-specific format information, and style.
        The format of the string representation must match the specified format exactly. The method returns a value that indicates whether the conversion succeeded.
        
        :param s: A span containing the characters representing a date to convert.
        :param format: The required format of s.
        :param provider: An object that supplies culture-specific formatting information about s.
        :param style: A bitwise combination of one or more enumeration values that indicate the permitted format of s.
        :param result: When this method returns, contains the DateOnly value equivalent to the date contained in s, if the conversion succeeded, or MinValue if the conversion failed. The conversion fails if the s is empty string, or does not contain a date that correspond to the pattern specified in format. This parameter is passed uninitialized.
        :returns: true if s was converted successfully; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def try_parse_exact(s: str, formats: typing.List[str], result: typing.Optional[System.DateOnly]) -> typing.Tuple[bool, System.DateOnly]:
        """
        Converts the specified string of a date to its DateOnly equivalent and returns a value that indicates whether the conversion succeeded.
        
        :param s: The string containing date to parse.
        :param formats: An array of allowable formats of s.
        :param result: When this method returns, contains the DateOnly value equivalent to the date contained in s, if the conversion succeeded, or MinValue if the conversion failed. The conversion fails if the s parameter is Empty, or does not contain a valid string representation of a date. This parameter is passed uninitialized.
        :returns: true if the s parameter was converted successfully; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def try_parse_exact(s: str, formats: typing.List[str], provider: System.IFormatProvider, style: System.Globalization.DateTimeStyles, result: typing.Optional[System.DateOnly]) -> typing.Tuple[bool, System.DateOnly]:
        """
        Converts the specified string of a date to its DateOnly equivalent and returns a value that indicates whether the conversion succeeded.
        
        :param s: The string containing the date to parse.
        :param formats: An array of allowable formats of s.
        :param provider: An object that supplies culture-specific formatting information about s.
        :param style: A bitwise combination of enumeration values that defines how to interpret the parsed date. A typical value to specify is None.
        :param result: When this method returns, contains the DateOnly value equivalent to the date contained in s, if the conversion succeeded, or MinValue if the conversion failed. The conversion fails if the s parameter is Empty, or does not contain a valid string representation of a date. This parameter is passed uninitialized.
        :returns: true if the s parameter was converted successfully; otherwise, false.
        """
        ...


class DateTime(System.IComparable[datetime.datetime], System.ISpanFormattable, System.IConvertible, System.IEquatable[datetime.datetime], System.Runtime.Serialization.ISerializable, System.ISpanParsable[datetime.datetime], System.IUtf8SpanFormattable):
    """This class has no documentation."""

    UTC_NOW: datetime.datetime

    MIN_VALUE: datetime.datetime

    MAX_VALUE: datetime.datetime = ...

    UNIX_EPOCH: datetime.datetime = ...

    @property
    def date(self) -> datetime.datetime:
        ...

    @property
    def day(self) -> int:
        ...

    @property
    def day_of_week(self) -> System.DayOfWeek:
        ...

    @property
    def day_of_year(self) -> int:
        ...

    @property
    def hour(self) -> int:
        ...

    @property
    def kind(self) -> System.DateTimeKind:
        ...

    @property
    def millisecond(self) -> int:
        ...

    @property
    def microsecond(self) -> int:
        """The microseconds component, expressed as a value between 0 and 999."""
        ...

    @property
    def nanosecond(self) -> int:
        """The nanoseconds component, expressed as a value between 0 and 900 (in increments of 100 nanoseconds)."""
        ...

    @property
    def minute(self) -> int:
        ...

    @property
    def month(self) -> int:
        ...

    NOW: datetime.datetime

    @property
    def second(self) -> int:
        ...

    @property
    def ticks(self) -> int:
        ...

    @property
    def time_of_day(self) -> datetime.timedelta:
        ...

    TODAY: datetime.datetime

    @property
    def year(self) -> int:
        ...

    def __add__(self, t: datetime.timedelta) -> datetime.datetime:
        ...

    def __eq__(self, d_2: typing.Union[datetime.datetime, datetime.date]) -> bool:
        ...

    @overload
    def __ge__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __ge__(self, other: typing.Union[datetime.datetime, datetime.date]) -> bool:
        ...

    @overload
    def __ge__(self, t_2: typing.Union[datetime.datetime, datetime.date]) -> bool:
        ...

    @overload
    def __gt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __gt__(self, other: typing.Union[datetime.datetime, datetime.date]) -> bool:
        ...

    @overload
    def __gt__(self, t_2: typing.Union[datetime.datetime, datetime.date]) -> bool:
        ...

    def __iadd__(self, t: datetime.timedelta) -> datetime.datetime:
        ...

    @overload
    def __init__(self, ticks: int) -> None:
        ...

    @overload
    def __init__(self, ticks: int, kind: System.DateTimeKind) -> None:
        ...

    @overload
    def __init__(self, date: System.DateOnly, time: System.TimeOnly) -> None:
        """
        Initializes a new instance of the DateTime structure to the specified DateOnly and TimeOnly.
        The new instance will have the DateTimeKind.Unspecified kind.
        
        :param date: The date part.
        :param time: The time part.
        """
        ...

    @overload
    def __init__(self, date: System.DateOnly, time: System.TimeOnly, kind: System.DateTimeKind) -> None:
        """
        Initializes a new instance of the DateTime structure to the specified DateOnly and TimeOnly respecting a DateTimeKind.
        
        :param date: The date part.
        :param time: The time part.
        :param kind: One of the enumeration values that indicates whether  and  specify a local time, Coordinated Universal Time (UTC), or neither.
        """
        ...

    @overload
    def __init__(self, year: int, month: int, day: int) -> None:
        ...

    @overload
    def __init__(self, year: int, month: int, day: int, calendar: System.Globalization.Calendar) -> None:
        ...

    @overload
    def __init__(self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, calendar: System.Globalization.Calendar, kind: System.DateTimeKind) -> None:
        """
        Initializes a new instance of the DateTime structure to the specified year, month, day, hour, minute, second,
        millisecond, and Coordinated Universal Time (UTC) or local time for the specified calendar.
        
        :param year: The year (1 through the number of years in ).
        :param month: The month (1 through the number of months in ).
        :param day: The day (1 through the number of days in ).
        :param hour: The hours (0 through 23).
        :param minute: The minutes (0 through 59).
        :param second: The seconds (0 through 59).
        :param millisecond: The milliseconds (0 through 999).
        :param calendar: The calendar that is used to interpret , , and .
        :param kind: One of the enumeration values that indicates whether , , , , , , and  specify a local time, Coordinated Universal Time (UTC), or neither.
        """
        ...

    @overload
    def __init__(self, year: int, month: int, day: int, hour: int, minute: int, second: int) -> None:
        ...

    @overload
    def __init__(self, year: int, month: int, day: int, hour: int, minute: int, second: int, kind: System.DateTimeKind) -> None:
        ...

    @overload
    def __init__(self, year: int, month: int, day: int, hour: int, minute: int, second: int, calendar: System.Globalization.Calendar) -> None:
        ...

    @overload
    def __init__(self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int) -> None:
        """
        Initializes a new instance of the DateTime structure to the specified year, month, day, hour, minute, second,
        millisecond, and Coordinated Universal Time (UTC) or local time for the specified calendar.
        
        :param year: The year (1 through 9999).
        :param month: The month (1 through 12).
        :param day: The day (1 through the number of days in ).
        :param hour: The hours (0 through 23).
        :param minute: The minutes (0 through 59).
        :param second: The seconds (0 through 59).
        :param millisecond: The milliseconds (0 through 999).
        """
        ...

    @overload
    def __init__(self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, kind: System.DateTimeKind) -> None:
        """
        Initializes a new instance of the DateTime structure to the specified year, month, day, hour, minute, second,
        millisecond, and Coordinated Universal Time (UTC) or local time for the specified calendar.
        
        :param year: The year (1 through 9999).
        :param month: The month (1 through 12).
        :param day: The day (1 through the number of days in ).
        :param hour: The hours (0 through 23).
        :param minute: The minutes (0 through 59).
        :param second: The seconds (0 through 59).
        :param millisecond: The milliseconds (0 through 999).
        :param kind: One of the enumeration values that indicates whether , , , , , , and  specify a local time, Coordinated Universal Time (UTC), or neither.
        """
        ...

    @overload
    def __init__(self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, calendar: System.Globalization.Calendar) -> None:
        """
        Initializes a new instance of the DateTime structure to the specified year, month, day, hour, minute, second,
        millisecond, and Coordinated Universal Time (UTC) or local time for the specified calendar.
        
        :param year: The year (1 through the number of years in ).
        :param month: The month (1 through the number of months in ).
        :param day: The day (1 through the number of days in ).
        :param hour: The hours (0 through 23).
        :param minute: The minutes (0 through 59).
        :param second: The seconds (0 through 59).
        :param millisecond: The milliseconds (0 through 999).
        :param calendar: The calendar that is used to interpret , , and .
        """
        ...

    @overload
    def __init__(self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, microsecond: int) -> None:
        """
        Initializes a new instance of the DateTime structure to the specified year, month, day, hour, minute, second,
        millisecond, and Coordinated Universal Time (UTC) or local time for the specified calendar.
        
        :param year: The year (1 through 9999).
        :param month: The month (1 through 12).
        :param day: The day (1 through the number of days in ).
        :param hour: The hours (0 through 23).
        :param minute: The minutes (0 through 59).
        :param second: The seconds (0 through 59).
        :param millisecond: The milliseconds (0 through 999).
        :param microsecond: The microseconds (0 through 999).
        """
        ...

    @overload
    def __init__(self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, microsecond: int, kind: System.DateTimeKind) -> None:
        """
        Initializes a new instance of the DateTime structure to the specified year, month, day, hour, minute, second,
        millisecond, and Coordinated Universal Time (UTC) or local time for the specified calendar.
        
        :param year: The year (1 through 9999).
        :param month: The month (1 through 12).
        :param day: The day (1 through the number of days in ).
        :param hour: The hours (0 through 23).
        :param minute: The minutes (0 through 59).
        :param second: The seconds (0 through 59).
        :param millisecond: The milliseconds (0 through 999).
        :param microsecond: The microseconds (0 through 999).
        :param kind: One of the enumeration values that indicates whether , , , , , , and  specify a local time, Coordinated Universal Time (UTC), or neither.
        """
        ...

    @overload
    def __init__(self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, microsecond: int, calendar: System.Globalization.Calendar) -> None:
        """
        Initializes a new instance of the DateTime structure to the specified year, month, day, hour, minute, second,
        millisecond, and Coordinated Universal Time (UTC) or local time for the specified calendar.
        
        :param year: The year (1 through the number of years in ).
        :param month: The month (1 through the number of months in ).
        :param day: The day (1 through the number of days in ).
        :param hour: The hours (0 through 23).
        :param minute: The minutes (0 through 59).
        :param second: The seconds (0 through 59).
        :param millisecond: The milliseconds (0 through 999).
        :param microsecond: The microseconds (0 through 999).
        :param calendar: The calendar that is used to interpret , , and .
        """
        ...

    @overload
    def __init__(self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, microsecond: int, calendar: System.Globalization.Calendar, kind: System.DateTimeKind) -> None:
        """
        Initializes a new instance of the DateTime structure to the specified year, month, day, hour, minute, second,
        millisecond, and Coordinated Universal Time (UTC) or local time for the specified calendar.
        
        :param year: The year (1 through the number of years in ).
        :param month: The month (1 through the number of months in ).
        :param day: The day (1 through the number of days in ).
        :param hour: The hours (0 through 23).
        :param minute: The minutes (0 through 59).
        :param second: The seconds (0 through 59).
        :param millisecond: The milliseconds (0 through 999).
        :param microsecond: The microseconds (0 through 999).
        :param calendar: The calendar that is used to interpret , , and .
        :param kind: One of the enumeration values that indicates whether , , , , , , and  specify a local time, Coordinated Universal Time (UTC), or neither.
        """
        ...

    @overload
    def __isub__(self, t: datetime.timedelta) -> datetime.datetime:
        ...

    @overload
    def __isub__(self, d_2: typing.Union[datetime.datetime, datetime.date]) -> datetime.timedelta:
        ...

    @overload
    def __le__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __le__(self, other: typing.Union[datetime.datetime, datetime.date]) -> bool:
        ...

    @overload
    def __le__(self, t_2: typing.Union[datetime.datetime, datetime.date]) -> bool:
        ...

    @overload
    def __lt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __lt__(self, other: typing.Union[datetime.datetime, datetime.date]) -> bool:
        ...

    @overload
    def __lt__(self, t_2: typing.Union[datetime.datetime, datetime.date]) -> bool:
        ...

    def __ne__(self, d_2: typing.Union[datetime.datetime, datetime.date]) -> bool:
        ...

    @overload
    def __sub__(self, t: datetime.timedelta) -> datetime.datetime:
        ...

    @overload
    def __sub__(self, d_2: typing.Union[datetime.datetime, datetime.date]) -> datetime.timedelta:
        ...

    def add(self, value: datetime.timedelta) -> datetime.datetime:
        ...

    def add_days(self, value: float) -> datetime.datetime:
        """
        Returns a new DateTime that adds the specified number of days to the value of this instance.
        
        :param value: A number of whole and fractional days. The value parameter can be negative or positive.
        :returns: An object whose value is the sum of the date and time represented by this instance and the number of days represented by value.
        """
        ...

    def add_hours(self, value: float) -> datetime.datetime:
        """
        Returns a new DateTime that adds the specified number of hours to the value of this instance.
        
        :param value: A number of whole and fractional hours. The value parameter can be negative or positive.
        :returns: An object whose value is the sum of the date and time represented by this instance and the number of hours represented by value.
        """
        ...

    def add_microseconds(self, value: float) -> datetime.datetime:
        """
        Returns a new DateTime that adds the specified number of microseconds to the value of this instance.
        
        :param value: A number of whole and fractional microseconds. The  parameter can be negative or positive. Note that this value is rounded to the nearest integer.
        :returns: An object whose value is the sum of the date and time represented by this instance and the number of microseconds represented by .
        """
        ...

    def add_milliseconds(self, value: float) -> datetime.datetime:
        """
        Returns a new DateTime that adds the specified number of milliseconds to the value of this instance.
        
        :param value: A number of whole and fractional milliseconds. The value parameter can be negative or positive.
        :returns: An object whose value is the sum of the date and time represented by this instance and the number of milliseconds represented by value.
        """
        ...

    def add_minutes(self, value: float) -> datetime.datetime:
        """
        Returns a new DateTime that adds the specified number of minutes to the value of this instance.
        
        :param value: A number of whole and fractional minutes. The value parameter can be negative or positive.
        :returns: An object whose value is the sum of the date and time represented by this instance and the number of minutes represented by value.
        """
        ...

    def add_months(self, months: int) -> datetime.datetime:
        ...

    def add_seconds(self, value: float) -> datetime.datetime:
        """
        Returns a new DateTime that adds the specified number of seconds to the value of this instance.
        
        :param value: A number of whole and fractional seconds. The value parameter can be negative or positive.
        :returns: An object whose value is the sum of the date and time represented by this instance and the number of seconds represented by value.
        """
        ...

    def add_ticks(self, value: int) -> datetime.datetime:
        ...

    def add_years(self, value: int) -> datetime.datetime:
        ...

    @staticmethod
    def compare(t_1: typing.Union[datetime.datetime, datetime.date], t_2: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    @overload
    def compare_to(self, value: typing.Any) -> int:
        ...

    @overload
    def compare_to(self, value: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    @staticmethod
    def days_in_month(year: int, month: int) -> int:
        ...

    @overload
    def deconstruct(self, date: typing.Optional[System.DateOnly], time: typing.Optional[System.TimeOnly]) -> typing.Tuple[None, System.DateOnly, System.TimeOnly]:
        """
        Deconstructs DateTime into DateOnly and TimeOnly.
        
        :param date: Deconstructed DateOnly.
        :param time: Deconstructed TimeOnly.
        """
        ...

    @overload
    def deconstruct(self, year: typing.Optional[int], month: typing.Optional[int], day: typing.Optional[int]) -> typing.Tuple[None, int, int, int]:
        """
        Deconstructs DateOnly by Year, Month and Day.
        
        :param year: Deconstructed parameter for Year.
        :param month: Deconstructed parameter for Month.
        :param day: Deconstructed parameter for Day.
        """
        ...

    @overload
    def equals(self, value: typing.Any) -> bool:
        ...

    @overload
    def equals(self, value: typing.Union[datetime.datetime, datetime.date]) -> bool:
        ...

    @staticmethod
    @overload
    def equals(t_1: typing.Union[datetime.datetime, datetime.date], t_2: typing.Union[datetime.datetime, datetime.date]) -> bool:
        ...

    @staticmethod
    def from_binary(date_data: int) -> datetime.datetime:
        ...

    @staticmethod
    def from_file_time(file_time: int) -> datetime.datetime:
        ...

    @staticmethod
    def from_file_time_utc(file_time: int) -> datetime.datetime:
        ...

    @staticmethod
    def from_oa_date(d: float) -> datetime.datetime:
        ...

    @overload
    def get_date_time_formats(self) -> typing.List[str]:
        ...

    @overload
    def get_date_time_formats(self, provider: System.IFormatProvider) -> typing.List[str]:
        ...

    @overload
    def get_date_time_formats(self, format: str) -> typing.List[str]:
        ...

    @overload
    def get_date_time_formats(self, format: str, provider: System.IFormatProvider) -> typing.List[str]:
        ...

    def get_hash_code(self) -> int:
        ...

    def get_type_code(self) -> System.TypeCode:
        ...

    def is_daylight_saving_time(self) -> bool:
        ...

    @staticmethod
    def is_leap_year(year: int) -> bool:
        ...

    @staticmethod
    @overload
    def parse(s: str) -> datetime.datetime:
        ...

    @staticmethod
    @overload
    def parse(s: str, provider: System.IFormatProvider) -> datetime.datetime:
        ...

    @staticmethod
    @overload
    def parse(s: str, provider: System.IFormatProvider, styles: System.Globalization.DateTimeStyles) -> datetime.datetime:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider = None, styles: System.Globalization.DateTimeStyles = ...) -> datetime.datetime:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider) -> datetime.datetime:
        ...

    @staticmethod
    @overload
    def parse_exact(s: str, format: str, provider: System.IFormatProvider) -> datetime.datetime:
        ...

    @staticmethod
    @overload
    def parse_exact(s: str, format: str, provider: System.IFormatProvider, style: System.Globalization.DateTimeStyles) -> datetime.datetime:
        ...

    @staticmethod
    @overload
    def parse_exact(s: System.ReadOnlySpan[str], format: System.ReadOnlySpan[str], provider: System.IFormatProvider, style: System.Globalization.DateTimeStyles = ...) -> datetime.datetime:
        ...

    @staticmethod
    @overload
    def parse_exact(s: str, formats: typing.List[str], provider: System.IFormatProvider, style: System.Globalization.DateTimeStyles) -> datetime.datetime:
        ...

    @staticmethod
    @overload
    def parse_exact(s: System.ReadOnlySpan[str], formats: typing.List[str], provider: System.IFormatProvider, style: System.Globalization.DateTimeStyles = ...) -> datetime.datetime:
        ...

    @staticmethod
    def specify_kind(value: typing.Union[datetime.datetime, datetime.date], kind: System.DateTimeKind) -> datetime.datetime:
        ...

    @overload
    def subtract(self, value: typing.Union[datetime.datetime, datetime.date]) -> datetime.timedelta:
        ...

    @overload
    def subtract(self, value: datetime.timedelta) -> datetime.datetime:
        ...

    def to_binary(self) -> int:
        ...

    def to_file_time(self) -> int:
        ...

    def to_file_time_utc(self) -> int:
        ...

    def to_local_time(self) -> datetime.datetime:
        ...

    def to_long_date_string(self) -> str:
        ...

    def to_long_time_string(self) -> str:
        ...

    def to_oa_date(self) -> float:
        ...

    def to_short_date_string(self) -> str:
        ...

    def to_short_time_string(self) -> str:
        ...

    @overload
    def to_string(self) -> str:
        ...

    @overload
    def to_string(self, format: str) -> str:
        ...

    @overload
    def to_string(self, provider: System.IFormatProvider) -> str:
        ...

    @overload
    def to_string(self, format: str, provider: System.IFormatProvider) -> str:
        ...

    def to_universal_time(self) -> datetime.datetime:
        ...

    @overload
    def try_format(self, destination: System.Span[str], chars_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @overload
    def try_format(self, utf_8_destination: System.Span[int], bytes_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, result: typing.Optional[typing.Union[datetime.datetime, datetime.date]]) -> typing.Tuple[bool, typing.Union[datetime.datetime, datetime.date]]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], result: typing.Optional[typing.Union[datetime.datetime, datetime.date]]) -> typing.Tuple[bool, typing.Union[datetime.datetime, datetime.date]]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, provider: System.IFormatProvider, styles: System.Globalization.DateTimeStyles, result: typing.Optional[typing.Union[datetime.datetime, datetime.date]]) -> typing.Tuple[bool, typing.Union[datetime.datetime, datetime.date]]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider, styles: System.Globalization.DateTimeStyles, result: typing.Optional[typing.Union[datetime.datetime, datetime.date]]) -> typing.Tuple[bool, typing.Union[datetime.datetime, datetime.date]]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, provider: System.IFormatProvider, result: typing.Optional[typing.Union[datetime.datetime, datetime.date]]) -> typing.Tuple[bool, typing.Union[datetime.datetime, datetime.date]]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider, result: typing.Optional[typing.Union[datetime.datetime, datetime.date]]) -> typing.Tuple[bool, typing.Union[datetime.datetime, datetime.date]]:
        ...

    @staticmethod
    @overload
    def try_parse_exact(s: str, format: str, provider: System.IFormatProvider, style: System.Globalization.DateTimeStyles, result: typing.Optional[typing.Union[datetime.datetime, datetime.date]]) -> typing.Tuple[bool, typing.Union[datetime.datetime, datetime.date]]:
        ...

    @staticmethod
    @overload
    def try_parse_exact(s: System.ReadOnlySpan[str], format: System.ReadOnlySpan[str], provider: System.IFormatProvider, style: System.Globalization.DateTimeStyles, result: typing.Optional[typing.Union[datetime.datetime, datetime.date]]) -> typing.Tuple[bool, typing.Union[datetime.datetime, datetime.date]]:
        ...

    @staticmethod
    @overload
    def try_parse_exact(s: str, formats: typing.List[str], provider: System.IFormatProvider, style: System.Globalization.DateTimeStyles, result: typing.Optional[typing.Union[datetime.datetime, datetime.date]]) -> typing.Tuple[bool, typing.Union[datetime.datetime, datetime.date]]:
        ...

    @staticmethod
    @overload
    def try_parse_exact(s: System.ReadOnlySpan[str], formats: typing.List[str], provider: System.IFormatProvider, style: System.Globalization.DateTimeStyles, result: typing.Optional[typing.Union[datetime.datetime, datetime.date]]) -> typing.Tuple[bool, typing.Union[datetime.datetime, datetime.date]]:
        ...


class Nullable(typing.Generic[System_Nullable_T]):
    """This class has no documentation."""

    @property
    def has_value(self) -> bool:
        ...

    @property
    def value(self) -> System_Nullable_T:
        ...

    def __init__(self, value: System_Nullable_T) -> None:
        ...

    def equals(self, other: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    @staticmethod
    def get_underlying_type(nullable_type: typing.Type) -> typing.Type:
        ...

    @overload
    def get_value_or_default(self) -> System_Nullable_T:
        ...

    @overload
    def get_value_or_default(self, default_value: System_Nullable_T) -> System_Nullable_T:
        ...

    def to_string(self) -> str:
        ...


class DateTimeOffset(System.IComparable[System_DateTimeOffset], System.ISpanFormattable, System.IEquatable[System_DateTimeOffset], System.Runtime.Serialization.ISerializable, System.Runtime.Serialization.IDeserializationCallback, System.ISpanParsable[System_DateTimeOffset], System.IUtf8SpanFormattable):
    """This class has no documentation."""

    NOW: System.DateTimeOffset

    MIN_VALUE: System.DateTimeOffset

    MAX_VALUE: System.DateTimeOffset = ...

    UNIX_EPOCH: System.DateTimeOffset = ...

    UTC_NOW: System.DateTimeOffset

    @property
    def date_time(self) -> datetime.datetime:
        ...

    @property
    def utc_date_time(self) -> datetime.datetime:
        ...

    @property
    def local_date_time(self) -> datetime.datetime:
        ...

    @property
    def date(self) -> datetime.datetime:
        ...

    @property
    def day(self) -> int:
        ...

    @property
    def day_of_week(self) -> System.DayOfWeek:
        ...

    @property
    def day_of_year(self) -> int:
        ...

    @property
    def hour(self) -> int:
        ...

    @property
    def millisecond(self) -> int:
        ...

    @property
    def microsecond(self) -> int:
        """Gets the microsecond component of the time represented by the current DateTimeOffset object."""
        ...

    @property
    def nanosecond(self) -> int:
        """Gets the nanosecond component of the time represented by the current DateTimeOffset object."""
        ...

    @property
    def minute(self) -> int:
        ...

    @property
    def month(self) -> int:
        ...

    @property
    def offset(self) -> datetime.timedelta:
        ...

    @property
    def total_offset_minutes(self) -> int:
        """Gets the total number of minutes representing the time's offset from Coordinated Universal Time (UTC)."""
        ...

    @property
    def second(self) -> int:
        ...

    @property
    def ticks(self) -> int:
        ...

    @property
    def utc_ticks(self) -> int:
        ...

    @property
    def time_of_day(self) -> datetime.timedelta:
        ...

    @property
    def year(self) -> int:
        ...

    def __add__(self, time_span: datetime.timedelta) -> System.DateTimeOffset:
        ...

    def __eq__(self, right: System.DateTimeOffset) -> bool:
        ...

    @overload
    def __ge__(self, other: System.DateTimeOffset) -> bool:
        ...

    @overload
    def __ge__(self, right: System.DateTimeOffset) -> bool:
        ...

    @overload
    def __gt__(self, other: System.DateTimeOffset) -> bool:
        ...

    @overload
    def __gt__(self, right: System.DateTimeOffset) -> bool:
        ...

    def __iadd__(self, time_span: datetime.timedelta) -> System.DateTimeOffset:
        ...

    @overload
    def __init__(self, ticks: int, offset: datetime.timedelta) -> None:
        ...

    @overload
    def __init__(self, date_time: typing.Union[datetime.datetime, datetime.date]) -> None:
        ...

    @overload
    def __init__(self, date_time: typing.Union[datetime.datetime, datetime.date], offset: datetime.timedelta) -> None:
        ...

    @overload
    def __init__(self, date: System.DateOnly, time: System.TimeOnly, offset: datetime.timedelta) -> None:
        """
        Initializes a new instance of the DateTimeOffset structure by ,  and .
        
        :param date: The date part
        :param time: The time part
        :param offset: The time's offset from Coordinated Universal Time (UTC).
        """
        ...

    @overload
    def __init__(self, year: int, month: int, day: int, hour: int, minute: int, second: int, offset: datetime.timedelta) -> None:
        ...

    @overload
    def __init__(self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, offset: datetime.timedelta) -> None:
        ...

    @overload
    def __init__(self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, calendar: System.Globalization.Calendar, offset: datetime.timedelta) -> None:
        ...

    @overload
    def __init__(self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, microsecond: int, offset: datetime.timedelta) -> None:
        """
        Initializes a new instance of the DateTimeOffset structure using the
        specified , , , , ,
        , ,  and .
        
        :param year: The year (1 through 9999).
        :param month: The month (1 through 12).
        :param day: The day (1 through the number of days in ).
        :param hour: The hours (0 through 23).
        :param minute: The minutes (0 through 59).
        :param second: The seconds (0 through 59).
        :param millisecond: The milliseconds (0 through 999).
        :param microsecond: The microseconds (0 through 999).
        :param offset: The time's offset from Coordinated Universal Time (UTC).
        """
        ...

    @overload
    def __init__(self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, microsecond: int, calendar: System.Globalization.Calendar, offset: datetime.timedelta) -> None:
        """
        Initializes a new instance of the DateTimeOffset structure using the
        specified , , , , ,
        , ,  and .
        
        :param year: The year (1 through 9999).
        :param month: The month (1 through 12).
        :param day: The day (1 through the number of days in ).
        :param hour: The hours (0 through 23).
        :param minute: The minutes (0 through 59).
        :param second: The seconds (0 through 59).
        :param millisecond: The milliseconds (0 through 999).
        :param microsecond: The microseconds (0 through 999).
        :param calendar: The calendar that is used to interpret , , and .
        :param offset: The time's offset from Coordinated Universal Time (UTC).
        """
        ...

    @overload
    def __isub__(self, time_span: datetime.timedelta) -> System.DateTimeOffset:
        ...

    @overload
    def __isub__(self, right: System.DateTimeOffset) -> datetime.timedelta:
        ...

    @overload
    def __le__(self, other: System.DateTimeOffset) -> bool:
        ...

    @overload
    def __le__(self, right: System.DateTimeOffset) -> bool:
        ...

    @overload
    def __lt__(self, other: System.DateTimeOffset) -> bool:
        ...

    @overload
    def __lt__(self, right: System.DateTimeOffset) -> bool:
        ...

    def __ne__(self, right: System.DateTimeOffset) -> bool:
        ...

    @overload
    def __sub__(self, time_span: datetime.timedelta) -> System.DateTimeOffset:
        ...

    @overload
    def __sub__(self, right: System.DateTimeOffset) -> datetime.timedelta:
        ...

    def add(self, time_span: datetime.timedelta) -> System.DateTimeOffset:
        ...

    def add_days(self, days: float) -> System.DateTimeOffset:
        ...

    def add_hours(self, hours: float) -> System.DateTimeOffset:
        ...

    def add_microseconds(self, microseconds: float) -> System.DateTimeOffset:
        """
        Returns a new DateTimeOffset object that adds a specified number of microseconds to the value of this instance.
        
        :param microseconds: A number of whole and fractional microseconds. The number can be negative or positive.
        :returns: An object whose value is the sum of the date and time represented by the current DateTimeOffset object and the number of whole microseconds represented by .
        """
        ...

    def add_milliseconds(self, milliseconds: float) -> System.DateTimeOffset:
        ...

    def add_minutes(self, minutes: float) -> System.DateTimeOffset:
        ...

    def add_months(self, months: int) -> System.DateTimeOffset:
        ...

    def add_seconds(self, seconds: float) -> System.DateTimeOffset:
        ...

    def add_ticks(self, ticks: int) -> System.DateTimeOffset:
        ...

    def add_years(self, years: int) -> System.DateTimeOffset:
        ...

    @staticmethod
    def compare(first: System.DateTimeOffset, second: System.DateTimeOffset) -> int:
        ...

    def compare_to(self, other: System.DateTimeOffset) -> int:
        ...

    def deconstruct(self, date: typing.Optional[System.DateOnly], time: typing.Optional[System.TimeOnly], offset: typing.Optional[datetime.timedelta]) -> typing.Tuple[None, System.DateOnly, System.TimeOnly, datetime.timedelta]:
        """
        Deconstructs DateTimeOffset into DateOnly, TimeOnly and TimeSpan.
        
        :param date: Deconstructed DateOnly.
        :param time: Deconstructed TimeOnly
        :param offset: Deconstructed parameter for Offset.
        """
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, other: System.DateTimeOffset) -> bool:
        ...

    @staticmethod
    @overload
    def equals(first: System.DateTimeOffset, second: System.DateTimeOffset) -> bool:
        ...

    def equals_exact(self, other: System.DateTimeOffset) -> bool:
        ...

    @staticmethod
    def from_file_time(file_time: int) -> System.DateTimeOffset:
        ...

    @staticmethod
    def from_unix_time_milliseconds(milliseconds: int) -> System.DateTimeOffset:
        ...

    @staticmethod
    def from_unix_time_seconds(seconds: int) -> System.DateTimeOffset:
        ...

    def get_hash_code(self) -> int:
        ...

    @staticmethod
    @overload
    def parse(input: str) -> System.DateTimeOffset:
        ...

    @staticmethod
    @overload
    def parse(input: str, format_provider: System.IFormatProvider) -> System.DateTimeOffset:
        ...

    @staticmethod
    @overload
    def parse(input: str, format_provider: System.IFormatProvider, styles: System.Globalization.DateTimeStyles) -> System.DateTimeOffset:
        ...

    @staticmethod
    @overload
    def parse(input: System.ReadOnlySpan[str], format_provider: System.IFormatProvider = None, styles: System.Globalization.DateTimeStyles = ...) -> System.DateTimeOffset:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider) -> System.DateTimeOffset:
        ...

    @staticmethod
    @overload
    def parse_exact(input: str, format: str, format_provider: System.IFormatProvider) -> System.DateTimeOffset:
        ...

    @staticmethod
    @overload
    def parse_exact(input: str, format: str, format_provider: System.IFormatProvider, styles: System.Globalization.DateTimeStyles) -> System.DateTimeOffset:
        ...

    @staticmethod
    @overload
    def parse_exact(input: System.ReadOnlySpan[str], format: System.ReadOnlySpan[str], format_provider: System.IFormatProvider, styles: System.Globalization.DateTimeStyles = ...) -> System.DateTimeOffset:
        ...

    @staticmethod
    @overload
    def parse_exact(input: str, formats: typing.List[str], format_provider: System.IFormatProvider, styles: System.Globalization.DateTimeStyles) -> System.DateTimeOffset:
        ...

    @staticmethod
    @overload
    def parse_exact(input: System.ReadOnlySpan[str], formats: typing.List[str], format_provider: System.IFormatProvider, styles: System.Globalization.DateTimeStyles = ...) -> System.DateTimeOffset:
        ...

    @overload
    def subtract(self, value: System.DateTimeOffset) -> datetime.timedelta:
        ...

    @overload
    def subtract(self, value: datetime.timedelta) -> System.DateTimeOffset:
        ...

    def to_file_time(self) -> int:
        ...

    def to_local_time(self) -> System.DateTimeOffset:
        ...

    def to_offset(self, offset: datetime.timedelta) -> System.DateTimeOffset:
        ...

    @overload
    def to_string(self) -> str:
        ...

    @overload
    def to_string(self, format: str) -> str:
        ...

    @overload
    def to_string(self, format_provider: System.IFormatProvider) -> str:
        ...

    @overload
    def to_string(self, format: str, format_provider: System.IFormatProvider) -> str:
        ...

    def to_universal_time(self) -> System.DateTimeOffset:
        ...

    def to_unix_time_milliseconds(self) -> int:
        ...

    def to_unix_time_seconds(self) -> int:
        ...

    @overload
    def try_format(self, destination: System.Span[str], chars_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., format_provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @overload
    def try_format(self, utf_8_destination: System.Span[int], bytes_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., format_provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(input: str, result: typing.Optional[System.DateTimeOffset]) -> typing.Tuple[bool, System.DateTimeOffset]:
        ...

    @staticmethod
    @overload
    def try_parse(input: System.ReadOnlySpan[str], result: typing.Optional[System.DateTimeOffset]) -> typing.Tuple[bool, System.DateTimeOffset]:
        ...

    @staticmethod
    @overload
    def try_parse(input: str, format_provider: System.IFormatProvider, styles: System.Globalization.DateTimeStyles, result: typing.Optional[System.DateTimeOffset]) -> typing.Tuple[bool, System.DateTimeOffset]:
        ...

    @staticmethod
    @overload
    def try_parse(input: System.ReadOnlySpan[str], format_provider: System.IFormatProvider, styles: System.Globalization.DateTimeStyles, result: typing.Optional[System.DateTimeOffset]) -> typing.Tuple[bool, System.DateTimeOffset]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, provider: System.IFormatProvider, result: typing.Optional[System.DateTimeOffset]) -> typing.Tuple[bool, System.DateTimeOffset]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider, result: typing.Optional[System.DateTimeOffset]) -> typing.Tuple[bool, System.DateTimeOffset]:
        ...

    @staticmethod
    @overload
    def try_parse_exact(input: str, format: str, format_provider: System.IFormatProvider, styles: System.Globalization.DateTimeStyles, result: typing.Optional[System.DateTimeOffset]) -> typing.Tuple[bool, System.DateTimeOffset]:
        ...

    @staticmethod
    @overload
    def try_parse_exact(input: System.ReadOnlySpan[str], format: System.ReadOnlySpan[str], format_provider: System.IFormatProvider, styles: System.Globalization.DateTimeStyles, result: typing.Optional[System.DateTimeOffset]) -> typing.Tuple[bool, System.DateTimeOffset]:
        ...

    @staticmethod
    @overload
    def try_parse_exact(input: str, formats: typing.List[str], format_provider: System.IFormatProvider, styles: System.Globalization.DateTimeStyles, result: typing.Optional[System.DateTimeOffset]) -> typing.Tuple[bool, System.DateTimeOffset]:
        ...

    @staticmethod
    @overload
    def try_parse_exact(input: System.ReadOnlySpan[str], formats: typing.List[str], format_provider: System.IFormatProvider, styles: System.Globalization.DateTimeStyles, result: typing.Optional[System.DateTimeOffset]) -> typing.Tuple[bool, System.DateTimeOffset]:
        ...


class Guid(System.ISpanFormattable, System.IComparable[System_Guid], System.IEquatable[System_Guid], System.ISpanParsable[System_Guid], System.IUtf8SpanFormattable):
    """This class has no documentation."""

    EMPTY: System.Guid

    ALL_BITS_SET: System.Guid
    """Gets a Guid where all bits are set."""

    @property
    def variant(self) -> int:
        """Gets the value of the variant field for the Guid."""
        ...

    @property
    def version(self) -> int:
        """Gets the value of the version field for the Guid."""
        ...

    def __eq__(self, b: System.Guid) -> bool:
        ...

    @overload
    def __ge__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __ge__(self, other: System.Guid) -> bool:
        ...

    @overload
    def __ge__(self, right: System.Guid) -> bool:
        ...

    @overload
    def __gt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __gt__(self, other: System.Guid) -> bool:
        ...

    @overload
    def __gt__(self, right: System.Guid) -> bool:
        ...

    @overload
    def __init__(self, b: typing.List[int]) -> None:
        ...

    @overload
    def __init__(self, b: System.ReadOnlySpan[int]) -> None:
        ...

    @overload
    def __init__(self, b: System.ReadOnlySpan[int], big_endian: bool) -> None:
        ...

    @overload
    def __init__(self, a: int, b: int, c: int, d: int, e: int, f: int, g: int, h: int, i: int, j: int, k: int) -> None:
        ...

    @overload
    def __init__(self, a: int, b: int, c: int, d: typing.List[int]) -> None:
        ...

    @overload
    def __init__(self, g: str) -> None:
        ...

    @overload
    def __le__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __le__(self, other: System.Guid) -> bool:
        ...

    @overload
    def __le__(self, right: System.Guid) -> bool:
        ...

    @overload
    def __lt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __lt__(self, other: System.Guid) -> bool:
        ...

    @overload
    def __lt__(self, right: System.Guid) -> bool:
        ...

    def __ne__(self, b: System.Guid) -> bool:
        ...

    @overload
    def compare_to(self, value: typing.Any) -> int:
        ...

    @overload
    def compare_to(self, value: System.Guid) -> int:
        ...

    @staticmethod
    @overload
    def create_version_7() -> System.Guid:
        """
        Creates a new Guid according to RFC 9562, following the Version 7 format.
        
        :returns: A new Guid according to RFC 9562, following the Version 7 format.
        """
        ...

    @staticmethod
    @overload
    def create_version_7(timestamp: System.DateTimeOffset) -> System.Guid:
        """
        Creates a new Guid according to RFC 9562, following the Version 7 format.
        
        :param timestamp: The date time offset used to determine the Unix Epoch timestamp.
        :returns: A new Guid according to RFC 9562, following the Version 7 format.
        """
        ...

    @overload
    def equals(self, o: typing.Any) -> bool:
        ...

    @overload
    def equals(self, g: System.Guid) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    @staticmethod
    def new_guid() -> System.Guid:
        ...

    @staticmethod
    @overload
    def parse(input: str) -> System.Guid:
        ...

    @staticmethod
    @overload
    def parse(input: System.ReadOnlySpan[str]) -> System.Guid:
        ...

    @staticmethod
    @overload
    def parse(s: str, provider: System.IFormatProvider) -> System.Guid:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider) -> System.Guid:
        ...

    @staticmethod
    @overload
    def parse_exact(input: str, format: str) -> System.Guid:
        ...

    @staticmethod
    @overload
    def parse_exact(input: System.ReadOnlySpan[str], format: System.ReadOnlySpan[str]) -> System.Guid:
        ...

    @overload
    def to_byte_array(self) -> typing.List[int]:
        ...

    @overload
    def to_byte_array(self, big_endian: bool) -> typing.List[int]:
        ...

    @overload
    def to_string(self) -> str:
        ...

    @overload
    def to_string(self, format: str) -> str:
        ...

    @overload
    def to_string(self, format: str, provider: System.IFormatProvider) -> str:
        ...

    @overload
    def try_format(self, destination: System.Span[str], chars_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ...) -> typing.Tuple[bool, int]:
        ...

    @overload
    def try_format(self, utf_8_destination: System.Span[int], bytes_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ...) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(input: str, result: typing.Optional[System.Guid]) -> typing.Tuple[bool, System.Guid]:
        ...

    @staticmethod
    @overload
    def try_parse(input: System.ReadOnlySpan[str], result: typing.Optional[System.Guid]) -> typing.Tuple[bool, System.Guid]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, provider: System.IFormatProvider, result: typing.Optional[System.Guid]) -> typing.Tuple[bool, System.Guid]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider, result: typing.Optional[System.Guid]) -> typing.Tuple[bool, System.Guid]:
        ...

    @staticmethod
    @overload
    def try_parse_exact(input: str, format: str, result: typing.Optional[System.Guid]) -> typing.Tuple[bool, System.Guid]:
        ...

    @staticmethod
    @overload
    def try_parse_exact(input: System.ReadOnlySpan[str], format: System.ReadOnlySpan[str], result: typing.Optional[System.Guid]) -> typing.Tuple[bool, System.Guid]:
        ...

    @overload
    def try_write_bytes(self, destination: System.Span[int]) -> bool:
        ...

    @overload
    def try_write_bytes(self, destination: System.Span[int], big_endian: bool, bytes_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...


class MarshalByRefObject(System.Object, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def __init__(self) -> None:
        """This method is protected."""
        ...

    def get_lifetime_service(self) -> System.Object:
        """Obsoletions.RemotingApisMessage"""
        warnings.warn("Obsoletions.RemotingApisMessage", DeprecationWarning)

    def initialize_lifetime_service(self) -> System.Object:
        """Obsoletions.RemotingApisMessage"""
        warnings.warn("Obsoletions.RemotingApisMessage", DeprecationWarning)

    def memberwise_clone(self, clone_identity: bool) -> System.MarshalByRefObject:
        """This method is protected."""
        ...


class AppDomainSetup(System.Object):
    """This class has no documentation."""

    @property
    def application_base(self) -> str:
        ...

    @property
    def target_framework_name(self) -> str:
        ...


class EventArgs(System.Object):
    """This class has no documentation."""

    EMPTY: System.EventArgs = ...

    def __init__(self) -> None:
        ...


class UnhandledExceptionEventArgs(System.EventArgs):
    """This class has no documentation."""

    @property
    def exception_object(self) -> System.Object:
        ...

    @property
    def is_terminating(self) -> bool:
        ...

    def __init__(self, exception: typing.Any, is_terminating: bool) -> None:
        ...


class AssemblyLoadEventArgs(System.EventArgs):
    """This class has no documentation."""

    @property
    def loaded_assembly(self) -> System.Reflection.Assembly:
        ...

    def __init__(self, loaded_assembly: System.Reflection.Assembly) -> None:
        ...


class ResolveEventArgs(System.EventArgs):
    """This class has no documentation."""

    @property
    def name(self) -> str:
        ...

    @property
    def requesting_assembly(self) -> System.Reflection.Assembly:
        ...

    @overload
    def __init__(self, name: str) -> None:
        ...

    @overload
    def __init__(self, name: str, requesting_assembly: System.Reflection.Assembly) -> None:
        ...


class AppDomain(System.MarshalByRefObject):
    """This class has no documentation."""

    CURRENT_DOMAIN: System.AppDomain

    @property
    def base_directory(self) -> str:
        ...

    @property
    def relative_search_path(self) -> str:
        ...

    @property
    def setup_information(self) -> System.AppDomainSetup:
        ...

    @property
    def permission_set(self) -> System.Security.PermissionSet:
        """Obsoletions.CodeAccessSecurityMessage"""
        warnings.warn("Obsoletions.CodeAccessSecurityMessage", DeprecationWarning)

    @property
    def unhandled_exception(self) -> _EventContainer[typing.Callable[[System.Object, System.UnhandledExceptionEventArgs], None], None]:
        ...

    @unhandled_exception.setter
    def unhandled_exception(self, value: _EventContainer[typing.Callable[[System.Object, System.UnhandledExceptionEventArgs], None], None]) -> None:
        ...

    @property
    def dynamic_directory(self) -> str:
        ...

    @property
    def friendly_name(self) -> str:
        ...

    @property
    def id(self) -> int:
        ...

    @property
    def is_fully_trusted(self) -> bool:
        ...

    @property
    def is_homogenous(self) -> bool:
        ...

    @property
    def domain_unload(self) -> _EventContainer[typing.Callable[[System.Object, System.EventArgs], None], None]:
        ...

    @domain_unload.setter
    def domain_unload(self, value: _EventContainer[typing.Callable[[System.Object, System.EventArgs], None], None]) -> None:
        ...

    @property
    def first_chance_exception(self) -> _EventContainer[typing.Callable[[System.Object, System.Runtime.ExceptionServices.FirstChanceExceptionEventArgs], None], None]:
        ...

    @first_chance_exception.setter
    def first_chance_exception(self, value: _EventContainer[typing.Callable[[System.Object, System.Runtime.ExceptionServices.FirstChanceExceptionEventArgs], None], None]) -> None:
        ...

    @property
    def process_exit(self) -> _EventContainer[typing.Callable[[System.Object, System.EventArgs], None], None]:
        ...

    @process_exit.setter
    def process_exit(self, value: _EventContainer[typing.Callable[[System.Object, System.EventArgs], None], None]) -> None:
        ...

    monitoring_is_enabled: bool

    @property
    def monitoring_survived_memory_size(self) -> int:
        ...

    MONITORING_SURVIVED_PROCESS_MEMORY_SIZE: int

    @property
    def monitoring_total_allocated_memory_size(self) -> int:
        ...

    @property
    def shadow_copy_files(self) -> bool:
        ...

    @property
    def assembly_load(self) -> _EventContainer[typing.Callable[[System.Object, System.AssemblyLoadEventArgs], None], None]:
        ...

    @assembly_load.setter
    def assembly_load(self, value: _EventContainer[typing.Callable[[System.Object, System.AssemblyLoadEventArgs], None], None]) -> None:
        ...

    @property
    def assembly_resolve(self) -> _EventContainer[typing.Callable[[System.Object, System.ResolveEventArgs], System.Reflection.Assembly], System.Reflection.Assembly]:
        ...

    @assembly_resolve.setter
    def assembly_resolve(self, value: _EventContainer[typing.Callable[[System.Object, System.ResolveEventArgs], System.Reflection.Assembly], System.Reflection.Assembly]) -> None:
        ...

    @property
    def reflection_only_assembly_resolve(self) -> _EventContainer[typing.Callable[[System.Object, System.ResolveEventArgs], System.Reflection.Assembly], System.Reflection.Assembly]:
        ...

    @reflection_only_assembly_resolve.setter
    def reflection_only_assembly_resolve(self, value: _EventContainer[typing.Callable[[System.Object, System.ResolveEventArgs], System.Reflection.Assembly], System.Reflection.Assembly]) -> None:
        ...

    @property
    def type_resolve(self) -> _EventContainer[typing.Callable[[System.Object, System.ResolveEventArgs], System.Reflection.Assembly], System.Reflection.Assembly]:
        ...

    @type_resolve.setter
    def type_resolve(self, value: _EventContainer[typing.Callable[[System.Object, System.ResolveEventArgs], System.Reflection.Assembly], System.Reflection.Assembly]) -> None:
        ...

    @property
    def resource_resolve(self) -> _EventContainer[typing.Callable[[System.Object, System.ResolveEventArgs], System.Reflection.Assembly], System.Reflection.Assembly]:
        ...

    @resource_resolve.setter
    def resource_resolve(self, value: _EventContainer[typing.Callable[[System.Object, System.ResolveEventArgs], System.Reflection.Assembly], System.Reflection.Assembly]) -> None:
        ...

    @property
    def monitoring_total_processor_time(self) -> datetime.timedelta:
        ...

    def append_private_path(self, path: str) -> None:
        """AppDomain.AppendPrivatePath has been deprecated and is not supported."""
        warnings.warn("AppDomain.AppendPrivatePath has been deprecated and is not supported.", DeprecationWarning)

    def apply_policy(self, assembly_name: str) -> str:
        ...

    def clear_private_path(self) -> None:
        """AppDomain.ClearPrivatePath has been deprecated and is not supported."""
        warnings.warn("AppDomain.ClearPrivatePath has been deprecated and is not supported.", DeprecationWarning)

    def clear_shadow_copy_path(self) -> None:
        """AppDomain.ClearShadowCopyPath has been deprecated and is not supported."""
        warnings.warn("AppDomain.ClearShadowCopyPath has been deprecated and is not supported.", DeprecationWarning)

    @staticmethod
    def create_domain(friendly_name: str) -> System.AppDomain:
        """Obsoletions.AppDomainCreateUnloadMessage"""
        warnings.warn("Obsoletions.AppDomainCreateUnloadMessage", DeprecationWarning)

    @overload
    def create_instance(self, assembly_name: str, type_name: str) -> System.Runtime.Remoting.ObjectHandle:
        ...

    @overload
    def create_instance(self, assembly_name: str, type_name: str, ignore_case: bool, binding_attr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, args: typing.List[System.Object], culture: System.Globalization.CultureInfo, activation_attributes: typing.List[System.Object]) -> System.Runtime.Remoting.ObjectHandle:
        ...

    @overload
    def create_instance(self, assembly_name: str, type_name: str, activation_attributes: typing.List[System.Object]) -> System.Runtime.Remoting.ObjectHandle:
        ...

    @overload
    def create_instance_and_unwrap(self, assembly_name: str, type_name: str) -> System.Object:
        ...

    @overload
    def create_instance_and_unwrap(self, assembly_name: str, type_name: str, ignore_case: bool, binding_attr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, args: typing.List[System.Object], culture: System.Globalization.CultureInfo, activation_attributes: typing.List[System.Object]) -> System.Object:
        ...

    @overload
    def create_instance_and_unwrap(self, assembly_name: str, type_name: str, activation_attributes: typing.List[System.Object]) -> System.Object:
        ...

    @overload
    def create_instance_from(self, assembly_file: str, type_name: str) -> System.Runtime.Remoting.ObjectHandle:
        ...

    @overload
    def create_instance_from(self, assembly_file: str, type_name: str, ignore_case: bool, binding_attr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, args: typing.List[System.Object], culture: System.Globalization.CultureInfo, activation_attributes: typing.List[System.Object]) -> System.Runtime.Remoting.ObjectHandle:
        ...

    @overload
    def create_instance_from(self, assembly_file: str, type_name: str, activation_attributes: typing.List[System.Object]) -> System.Runtime.Remoting.ObjectHandle:
        ...

    @overload
    def create_instance_from_and_unwrap(self, assembly_file: str, type_name: str) -> System.Object:
        ...

    @overload
    def create_instance_from_and_unwrap(self, assembly_file: str, type_name: str, ignore_case: bool, binding_attr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, args: typing.List[System.Object], culture: System.Globalization.CultureInfo, activation_attributes: typing.List[System.Object]) -> System.Object:
        ...

    @overload
    def create_instance_from_and_unwrap(self, assembly_file: str, type_name: str, activation_attributes: typing.List[System.Object]) -> System.Object:
        ...

    @overload
    def execute_assembly(self, assembly_file: str) -> int:
        ...

    @overload
    def execute_assembly(self, assembly_file: str, args: typing.List[str]) -> int:
        ...

    @overload
    def execute_assembly(self, assembly_file: str, args: typing.List[str], hash_value: typing.List[int], hash_algorithm: System.Configuration.Assemblies.AssemblyHashAlgorithm) -> int:
        """Obsoletions.CodeAccessSecurityMessage"""
        ...

    @overload
    def execute_assembly_by_name(self, assembly_name: System.Reflection.AssemblyName, *args: typing.Union[str, typing.Iterable[str]]) -> int:
        ...

    @overload
    def execute_assembly_by_name(self, assembly_name: str) -> int:
        ...

    @overload
    def execute_assembly_by_name(self, assembly_name: str, *args: typing.Union[str, typing.Iterable[str]]) -> int:
        ...

    def get_assemblies(self) -> typing.List[System.Reflection.Assembly]:
        ...

    @staticmethod
    def get_current_thread_id() -> int:
        """AppDomain.GetCurrentThreadId has been deprecated because it does not provide a stable Id when managed threads are running on fibers (aka lightweight threads). To get a stable identifier for a managed thread, use the ManagedThreadId property on Thread instead."""
        warnings.warn("AppDomain.GetCurrentThreadId has been deprecated because it does not provide a stable Id when managed threads are running on fibers (aka lightweight threads). To get a stable identifier for a managed thread, use the ManagedThreadId property on Thread instead.", DeprecationWarning)

    def get_data(self, name: str) -> System.Object:
        ...

    def is_compatibility_switch_set(self, value: str) -> typing.Optional[bool]:
        ...

    def is_default_app_domain(self) -> bool:
        ...

    def is_finalizing_for_unload(self) -> bool:
        ...

    @overload
    def load(self, raw_assembly: typing.List[int]) -> System.Reflection.Assembly:
        ...

    @overload
    def load(self, raw_assembly: typing.List[int], raw_symbol_store: typing.List[int]) -> System.Reflection.Assembly:
        ...

    @overload
    def load(self, assembly_ref: System.Reflection.AssemblyName) -> System.Reflection.Assembly:
        ...

    @overload
    def load(self, assembly_string: str) -> System.Reflection.Assembly:
        ...

    def reflection_only_get_assemblies(self) -> typing.List[System.Reflection.Assembly]:
        ...

    def set_cache_path(self, path: str) -> None:
        """AppDomain.SetCachePath has been deprecated and is not supported."""
        warnings.warn("AppDomain.SetCachePath has been deprecated and is not supported.", DeprecationWarning)

    def set_data(self, name: str, data: typing.Any) -> None:
        ...

    def set_dynamic_base(self, path: str) -> None:
        """AppDomain.SetDynamicBase has been deprecated and is not supported."""
        warnings.warn("AppDomain.SetDynamicBase has been deprecated and is not supported.", DeprecationWarning)

    def set_principal_policy(self, policy: System.Security.Principal.PrincipalPolicy) -> None:
        ...

    def set_shadow_copy_files(self) -> None:
        """AppDomain.SetShadowCopyFiles has been deprecated and is not supported."""
        warnings.warn("AppDomain.SetShadowCopyFiles has been deprecated and is not supported.", DeprecationWarning)

    def set_shadow_copy_path(self, path: str) -> None:
        """AppDomain.SetShadowCopyPath has been deprecated and is not supported."""
        warnings.warn("AppDomain.SetShadowCopyPath has been deprecated and is not supported.", DeprecationWarning)

    def set_thread_principal(self, principal: System.Security.Principal.IPrincipal) -> None:
        ...

    def to_string(self) -> str:
        ...

    @staticmethod
    def unload(domain: System.AppDomain) -> None:
        """Obsoletions.AppDomainCreateUnloadMessage"""
        warnings.warn("Obsoletions.AppDomainCreateUnloadMessage", DeprecationWarning)


class IAsyncResult(metaclass=abc.ABCMeta):
    """Represents the status of an asynchronous operation."""

    @property
    @abc.abstractmethod
    def is_completed(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def async_wait_handle(self) -> System.Threading.WaitHandle:
        ...

    @property
    @abc.abstractmethod
    def async_state(self) -> System.Object:
        ...

    @property
    @abc.abstractmethod
    def completed_synchronously(self) -> bool:
        ...


class AppContext(System.Object):
    """This class has no documentation."""

    BASE_DIRECTORY: str

    TARGET_FRAMEWORK_NAME: str

    @staticmethod
    def get_data(name: str) -> System.Object:
        ...

    @staticmethod
    def set_data(name: str, data: typing.Any) -> None:
        """
        Sets the value of the named data element assigned to the current application domain.
        
        :param name: The name of the data element
        :param data: The value of
        """
        ...

    @staticmethod
    def set_switch(switch_name: str, is_enabled: bool) -> None:
        """
        Assign a switch a value
        
        :param switch_name: The name of the switch
        :param is_enabled: The value to assign
        """
        ...

    @staticmethod
    def try_get_switch(switch_name: str, is_enabled: typing.Optional[bool]) -> typing.Tuple[bool, bool]:
        """
        Try to get the value of the switch.
        
        :param switch_name: The name of the switch
        :param is_enabled: A variable where to place the value of the switch
        :returns: A return value of true represents that the switch was set and  contains the value of the switch.
        """
        ...


class FormattableString(System.Object, System.IFormattable, metaclass=abc.ABCMeta):
    """Represents a composite format string, along with the arguments to be formatted."""

    @property
    @abc.abstractmethod
    def format(self) -> str:
        """The composite format string."""
        ...

    @property
    @abc.abstractmethod
    def argument_count(self) -> int:
        """The number of arguments to be formatted."""
        ...

    @staticmethod
    def current_culture(formattable: System.FormattableString) -> str:
        """
        Format the given object in the current culture. This static method may be
        imported in C# by
        
        using static System.FormattableString;
        .
        Within the scope
        of that import directive an interpolated string may be formatted in the
        current culture by writing, for example,
        
        CurrentCulture($"{{ lat = {latitude}; lon = {longitude} }}")
        """
        ...

    def get_argument(self, index: int) -> System.Object:
        """Returns one argument to be formatted from argument position ."""
        ...

    def get_arguments(self) -> typing.List[System.Object]:
        """
        Returns an object array that contains zero or more objects to format. Clients should not
        mutate the contents of the array.
        """
        ...

    @staticmethod
    def invariant(formattable: System.FormattableString) -> str:
        """
        Format the given object in the invariant culture. This static method may be
        imported in C# by
        
        using static System.FormattableString;
        .
        Within the scope
        of that import directive an interpolated string may be formatted in the
        invariant culture by writing, for example,
        
        Invariant($"{{ lat = {latitude}; lon = {longitude} }}")
        """
        ...

    @overload
    def to_string(self, format_provider: System.IFormatProvider) -> str:
        """Format to a string using the given culture."""
        ...

    @overload
    def to_string(self) -> str:
        ...


class DBNull(System.Object, System.Runtime.Serialization.ISerializable, System.IConvertible):
    """This class has no documentation."""

    VALUE: System.DBNull = ...

    def get_object_data(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """Obsoletions.LegacyFormatterImplMessage"""
        warnings.warn("Obsoletions.LegacyFormatterImplMessage", DeprecationWarning)

    def get_type_code(self) -> System.TypeCode:
        ...

    @overload
    def to_string(self) -> str:
        ...

    @overload
    def to_string(self, provider: System.IFormatProvider) -> str:
        ...


class SystemException(System.Exception):
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


class OutOfMemoryException(System.SystemException):
    """The exception class for OOM."""

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


class ReadOnlyMemory(typing.Generic[System_ReadOnlyMemory_T], System.IEquatable[System_ReadOnlyMemory]):
    """
    Represents a contiguous region of memory, similar to ReadOnlySpan{T}.
    Unlike ReadOnlySpan{T}, it is not a byref-like type.
    """

    EMPTY: System.ReadOnlyMemory[System_ReadOnlyMemory_T]
    """Returns an empty ReadOnlyMemory{T}"""

    @property
    def length(self) -> int:
        """The number of items in the memory."""
        ...

    @property
    def is_empty(self) -> bool:
        """Returns true if Length is 0."""
        ...

    @property
    def span(self) -> System.ReadOnlySpan[System_ReadOnlyMemory_T]:
        """Returns a span from the memory."""
        ...

    @overload
    def __init__(self, array: typing.List[System_ReadOnlyMemory_T]) -> None:
        """
        Creates a new memory over the entirety of the target array.
        
        :param array: The target array.
        """
        ...

    @overload
    def __init__(self, array: typing.List[System_ReadOnlyMemory_T], start: int, length: int) -> None:
        """
        Creates a new memory over the portion of the target array beginning
        at 'start' index and ending at 'end' index (exclusive).
        
        :param array: The target array.
        :param start: The index at which to begin the memory.
        :param length: The number of items in the memory.
        """
        ...

    def copy_to(self, destination: System.Memory[System_ReadOnlyMemory_T]) -> None:
        """
        Copies the contents of the read-only memory into the destination. If the source
        and destination overlap, this method behaves as if the original values are in
        a temporary location before the destination is overwritten.
        
        :param destination: The Memory to copy items into.
        """
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        """Determines whether the specified object is equal to the current object."""
        ...

    @overload
    def equals(self, other: System.ReadOnlyMemory[System_ReadOnlyMemory_T]) -> bool:
        """
        Returns true if the memory points to the same array and has the same length.  Note that
        this does *not* check to see if the *contents* are equal.
        """
        ...

    def get_hash_code(self) -> int:
        """Returns the hash code for this ReadOnlyMemory{T}"""
        ...

    def pin(self) -> System.Buffers.MemoryHandle:
        """
        Creates a handle for the memory.
        The GC will not move the memory until the returned MemoryHandle
        is disposed, enabling taking and using the memory's address.
        """
        ...

    @overload
    def slice(self, start: int) -> System.ReadOnlyMemory[System_ReadOnlyMemory_T]:
        """
        Forms a slice out of the given memory, beginning at 'start'.
        
        :param start: The index at which to begin this slice.
        """
        ...

    @overload
    def slice(self, start: int, length: int) -> System.ReadOnlyMemory[System_ReadOnlyMemory_T]:
        """
        Forms a slice out of the given memory, beginning at 'start', of given length
        
        :param start: The index at which to begin this slice.
        :param length: The desired length for the slice (exclusive).
        """
        ...

    def to_array(self) -> typing.List[System_ReadOnlyMemory_T]:
        """
        Copies the contents from the memory into a new array.  This heap
        allocates, so should generally be avoided, however it is sometimes
        necessary to bridge the gap with APIs written in terms of arrays.
        """
        ...

    def to_string(self) -> str:
        """
        For ReadOnlyMemory{Char}, returns a new instance of string that represents the characters pointed to by the memory.
        Otherwise, returns a string with the name of the type and the number of elements.
        """
        ...

    def try_copy_to(self, destination: System.Memory[System_ReadOnlyMemory_T]) -> bool:
        """
        Copies the contents of the readonly-only memory into the destination. If the source
        and destination overlap, this method behaves as if the original values are in
        a temporary location before the destination is overwritten.
        
        :param destination: The span to copy items into.
        :returns: If the destination is shorter than the source, this method return false and no data is written to the destination.
        """
        ...


class Char(System.IComparable[str], System.IEquatable[str], System.IConvertible, System.ISpanFormattable, System.Numerics.IUnsignedNumber[str], System.IUtf8SpanFormattable, System.IUtfChar[str], System.IBinaryIntegerParseAndFormatInfo[str]):
    """Represents a character as a UTF-16 code unit."""

    MAX_VALUE: str = ...

    MIN_VALUE: str = ...

    @overload
    def __ge__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __ge__(self, other: str) -> bool:
        ...

    @overload
    def __gt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __gt__(self, other: str) -> bool:
        ...

    @overload
    def __le__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __le__(self, other: str) -> bool:
        ...

    @overload
    def __lt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __lt__(self, other: str) -> bool:
        ...

    @overload
    def compare_to(self, value: typing.Any) -> int:
        ...

    @overload
    def compare_to(self, value: str) -> int:
        ...

    @staticmethod
    def convert_from_utf_32(utf_32: int) -> str:
        ...

    @staticmethod
    @overload
    def convert_to_utf_32(high_surrogate: str, low_surrogate: str) -> int:
        ...

    @staticmethod
    @overload
    def convert_to_utf_32(s: str, index: int) -> int:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, obj: str) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    @staticmethod
    @overload
    def get_numeric_value(c: str) -> float:
        ...

    @staticmethod
    @overload
    def get_numeric_value(s: str, index: int) -> float:
        ...

    def get_type_code(self) -> System.TypeCode:
        ...

    @staticmethod
    @overload
    def get_unicode_category(c: str) -> System.Globalization.UnicodeCategory:
        ...

    @staticmethod
    @overload
    def get_unicode_category(s: str, index: int) -> System.Globalization.UnicodeCategory:
        ...

    @staticmethod
    def is_ascii(c: str) -> bool:
        """
        Returns true if  is an ASCII
        character ([ U+0000..U+007F ]).
        """
        ...

    @staticmethod
    def is_ascii_digit(c: str) -> bool:
        """
        Indicates whether a character is categorized as an ASCII digit.
        
        :param c: The character to evaluate.
        :returns: true if  is an ASCII digit; otherwise, false.
        """
        ...

    @staticmethod
    def is_ascii_hex_digit(c: str) -> bool:
        """
        Indicates whether a character is categorized as an ASCII hexadecimal digit.
        
        :param c: The character to evaluate.
        :returns: true if  is a hexadecimal digit; otherwise, false.
        """
        ...

    @staticmethod
    def is_ascii_hex_digit_lower(c: str) -> bool:
        """
        Indicates whether a character is categorized as an ASCII lower-case hexadecimal digit.
        
        :param c: The character to evaluate.
        :returns: true if  is a lower-case hexadecimal digit; otherwise, false.
        """
        ...

    @staticmethod
    def is_ascii_hex_digit_upper(c: str) -> bool:
        """
        Indicates whether a character is categorized as an ASCII upper-case hexadecimal digit.
        
        :param c: The character to evaluate.
        :returns: true if  is a hexadecimal digit; otherwise, false.
        """
        ...

    @staticmethod
    def is_ascii_letter(c: str) -> bool:
        """
        Indicates whether a character is categorized as an ASCII letter.
        
        :param c: The character to evaluate.
        :returns: true if  is an ASCII letter; otherwise, false.
        """
        ...

    @staticmethod
    def is_ascii_letter_lower(c: str) -> bool:
        """
        Indicates whether a character is categorized as a lowercase ASCII letter.
        
        :param c: The character to evaluate.
        :returns: true if  is a lowercase ASCII letter; otherwise, false.
        """
        ...

    @staticmethod
    def is_ascii_letter_or_digit(c: str) -> bool:
        """
        Indicates whether a character is categorized as an ASCII letter or digit.
        
        :param c: The character to evaluate.
        :returns: true if  is an ASCII letter or digit; otherwise, false.
        """
        ...

    @staticmethod
    def is_ascii_letter_upper(c: str) -> bool:
        """
        Indicates whether a character is categorized as an uppercase ASCII letter.
        
        :param c: The character to evaluate.
        :returns: true if  is an uppercase ASCII letter; otherwise, false.
        """
        ...

    @staticmethod
    def is_between(c: str, min_inclusive: str, max_inclusive: str) -> bool:
        """
        Indicates whether a character is within the specified inclusive range.
        
        :param c: The character to evaluate.
        :param min_inclusive: The lower bound, inclusive.
        :param max_inclusive: The upper bound, inclusive.
        :returns: true if  is within the specified range; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def is_control(c: str) -> bool:
        ...

    @staticmethod
    @overload
    def is_control(s: str, index: int) -> bool:
        ...

    @staticmethod
    @overload
    def is_digit(c: str) -> bool:
        ...

    @staticmethod
    @overload
    def is_digit(s: str, index: int) -> bool:
        ...

    @staticmethod
    @overload
    def is_high_surrogate(c: str) -> bool:
        ...

    @staticmethod
    @overload
    def is_high_surrogate(s: str, index: int) -> bool:
        ...

    @staticmethod
    @overload
    def is_letter(c: str) -> bool:
        ...

    @staticmethod
    @overload
    def is_letter(s: str, index: int) -> bool:
        ...

    @staticmethod
    @overload
    def is_letter_or_digit(c: str) -> bool:
        ...

    @staticmethod
    @overload
    def is_letter_or_digit(s: str, index: int) -> bool:
        ...

    @staticmethod
    @overload
    def is_lower(c: str) -> bool:
        ...

    @staticmethod
    @overload
    def is_lower(s: str, index: int) -> bool:
        ...

    @staticmethod
    @overload
    def is_low_surrogate(c: str) -> bool:
        ...

    @staticmethod
    @overload
    def is_low_surrogate(s: str, index: int) -> bool:
        ...

    @staticmethod
    @overload
    def is_number(c: str) -> bool:
        ...

    @staticmethod
    @overload
    def is_number(s: str, index: int) -> bool:
        ...

    @staticmethod
    @overload
    def is_punctuation(c: str) -> bool:
        ...

    @staticmethod
    @overload
    def is_punctuation(s: str, index: int) -> bool:
        ...

    @staticmethod
    @overload
    def is_separator(c: str) -> bool:
        ...

    @staticmethod
    @overload
    def is_separator(s: str, index: int) -> bool:
        ...

    @staticmethod
    @overload
    def is_surrogate(c: str) -> bool:
        ...

    @staticmethod
    @overload
    def is_surrogate(s: str, index: int) -> bool:
        ...

    @staticmethod
    @overload
    def is_surrogate_pair(s: str, index: int) -> bool:
        ...

    @staticmethod
    @overload
    def is_surrogate_pair(high_surrogate: str, low_surrogate: str) -> bool:
        ...

    @staticmethod
    @overload
    def is_symbol(c: str) -> bool:
        ...

    @staticmethod
    @overload
    def is_symbol(s: str, index: int) -> bool:
        ...

    @staticmethod
    @overload
    def is_upper(c: str) -> bool:
        ...

    @staticmethod
    @overload
    def is_upper(s: str, index: int) -> bool:
        ...

    @staticmethod
    @overload
    def is_white_space(c: str) -> bool:
        ...

    @staticmethod
    @overload
    def is_white_space(s: str, index: int) -> bool:
        ...

    @staticmethod
    def parse(s: str) -> str:
        ...

    @staticmethod
    @overload
    def to_lower(c: str, culture: System.Globalization.CultureInfo) -> str:
        ...

    @staticmethod
    @overload
    def to_lower(c: str) -> str:
        ...

    @staticmethod
    def to_lower_invariant(c: str) -> str:
        ...

    @overload
    def to_string(self) -> str:
        ...

    @overload
    def to_string(self, provider: System.IFormatProvider) -> str:
        ...

    @staticmethod
    @overload
    def to_string(c: str) -> str:
        ...

    @staticmethod
    @overload
    def to_upper(c: str, culture: System.Globalization.CultureInfo) -> str:
        ...

    @staticmethod
    @overload
    def to_upper(c: str) -> str:
        ...

    @staticmethod
    def to_upper_invariant(c: str) -> str:
        ...

    @staticmethod
    def try_parse(s: str, result: typing.Optional[str]) -> typing.Tuple[bool, str]:
        ...


class StringSplitOptions(Enum):
    """Specifies how the results should be transformed when splitting a string into substrings."""

    NONE = 0
    """Do not transform the results. This is the default behavior."""

    REMOVE_EMPTY_ENTRIES = 1
    """Remove empty (zero-length) substrings from the result."""

    TRIM_ENTRIES = 2
    """Trim whitespace from each substring in the result."""


class StringComparison(Enum):
    """This class has no documentation."""

    CURRENT_CULTURE = 0

    CURRENT_CULTURE_IGNORE_CASE = 1

    INVARIANT_CULTURE = 2

    INVARIANT_CULTURE_IGNORE_CASE = 3

    ORDINAL = 4

    ORDINAL_IGNORE_CASE = 5


class MemoryExtensions(System.Object):
    """Extension methods for Span{T}, Memory{T}, and friends."""

    class SpanSplitEnumerator(typing.Generic[System_MemoryExtensions_SpanSplitEnumerator_T], typing.Iterable[System_MemoryExtensions_SpanSplitEnumerator_T]):
        """Enables enumerating each split within a ReadOnlySpan{T} that has been divided using one or more separators."""

        @property
        def source(self) -> System.ReadOnlySpan[System_MemoryExtensions_SpanSplitEnumerator_T]:
            """Gets the source span being enumerated."""
            ...

        @property
        def current(self) -> System.Range:
            """Gets the current element of the enumeration."""
            ...

        def __iter__(self) -> typing.Iterator[System_MemoryExtensions_SpanSplitEnumerator_T]:
            ...

        def get_enumerator(self) -> System.MemoryExtensions.SpanSplitEnumerator[System_MemoryExtensions_SpanSplitEnumerator_T]:
            """
            Gets an enumerator that allows for iteration over the split span.
            
            :returns: Returns a SpanSplitEnumerator{T} that can be used to iterate over the split span.
            """
            ...

        def move_next(self) -> bool:
            """
            Advances the enumerator to the next element of the enumeration.
            
            :returns: true if the enumerator was successfully advanced to the next element; false if the enumerator has passed the end of the enumeration.
            """
            ...

    class TryWriteInterpolatedStringHandler:
        """Provides a handler used by the language compiler to format interpolated strings into character spans."""

        @overload
        def __init__(self, literal_length: int, formatted_count: int, destination: System.Span[str], should_append: typing.Optional[bool]) -> typing.Tuple[None, bool]:
            """
            Creates a handler used to write an interpolated string into a Span{Char}.
            
            :param literal_length: The number of constant characters outside of interpolation expressions in the interpolated string.
            :param formatted_count: The number of interpolation expressions in the interpolated string.
            :param destination: The destination buffer.
            :param should_append: Upon return, true if the destination may be long enough to support the formatting, or false if it won't be.
            """
            ...

        @overload
        def __init__(self, literal_length: int, formatted_count: int, destination: System.Span[str], provider: System.IFormatProvider, should_append: typing.Optional[bool]) -> typing.Tuple[None, bool]:
            """
            Creates a handler used to write an interpolated string into a Span{Char}.
            
            :param literal_length: The number of constant characters outside of interpolation expressions in the interpolated string.
            :param formatted_count: The number of interpolation expressions in the interpolated string.
            :param destination: The destination buffer.
            :param provider: An object that supplies culture-specific formatting information.
            :param should_append: Upon return, true if the destination may be long enough to support the formatting, or false if it won't be.
            """
            ...

        @overload
        def append_formatted(self, value: typing.Any, alignment: int = 0, format: str = None) -> bool:
            ...

        @overload
        def append_formatted(self, value: System.ReadOnlySpan[str]) -> bool:
            ...

        @overload
        def append_formatted(self, value: System.ReadOnlySpan[str], alignment: int = 0, format: str = None) -> bool:
            """
            Writes the specified string of chars to the handler.
            
            :param value: The span to write.
            :param alignment: Minimum number of characters that should be written for this value.  If the value is negative, it indicates left-aligned and the required minimum is the absolute value.
            :param format: The format string.
            """
            ...

        @overload
        def append_formatted(self, value: str) -> bool:
            ...

        @overload
        def append_formatted(self, value: str, alignment: int = 0, format: str = None) -> bool:
            """
            Writes the specified value to the handler.
            
            :param value: The value to write.
            :param alignment: Minimum number of characters that should be written for this value.  If the value is negative, it indicates left-aligned and the required minimum is the absolute value.
            :param format: The format string.
            """
            ...

        def append_literal(self, value: str) -> bool:
            """
            Writes the specified string to the handler.
            
            :param value: The string to write.
            :returns: true if the value could be formatted to the span; otherwise, false.
            """
            ...

    @staticmethod
    @overload
    def as_memory(text: str) -> System.ReadOnlyMemory[str]:
        """
        Creates a new ReadOnlyMemory{T} over the portion of the target string.
        
        :param text: The target string.
        """
        ...

    @staticmethod
    @overload
    def as_memory(text: str, start: int) -> System.ReadOnlyMemory[str]:
        """
        Creates a new ReadOnlyMemory{T} over the portion of the target string.
        
        :param text: The target string.
        :param start: The index at which to begin this slice.
        """
        ...

    @staticmethod
    @overload
    def as_memory(text: str, start_index: System.Index) -> System.ReadOnlyMemory[str]:
        """
        Creates a new ReadOnlyMemory{T} over the portion of the target string.
        
        :param text: The target string.
        :param start_index: The index at which to begin this slice.
        """
        ...

    @staticmethod
    @overload
    def as_memory(text: str, start: int, length: int) -> System.ReadOnlyMemory[str]:
        """
        Creates a new ReadOnlyMemory{T} over the portion of the target string.
        
        :param text: The target string.
        :param start: The index at which to begin this slice.
        :param length: The desired length for the slice (exclusive).
        """
        ...

    @staticmethod
    @overload
    def as_memory(text: str, range: System.Range) -> System.ReadOnlyMemory[str]:
        """
        Creates a new ReadOnlyMemory{T} over the portion of the target string.
        
        :param text: The target string.
        :param range: The range used to indicate the start and length of the sliced string.
        """
        ...

    @staticmethod
    @overload
    def as_span(text: str) -> System.ReadOnlySpan[str]:
        """
        Creates a new readonly span over the portion of the target string.
        
        :param text: The target string.
        """
        ...

    @staticmethod
    @overload
    def as_span(text: str, start: int) -> System.ReadOnlySpan[str]:
        """
        Creates a new readonly span over the portion of the target string.
        
        :param text: The target string.
        :param start: The index at which to begin this slice.
        """
        ...

    @staticmethod
    @overload
    def as_span(text: str, start_index: System.Index) -> System.ReadOnlySpan[str]:
        """
        Creates a new ReadOnlySpan{Char} over a portion of the target string from a specified position to the end of the string.
        
        :param text: The target string.
        :param start_index: The index at which to begin this slice.
        """
        ...

    @staticmethod
    @overload
    def as_span(text: str, range: System.Range) -> System.ReadOnlySpan[str]:
        """
        Creates a new ReadOnlySpan{Char} over a portion of a target string using the range start and end indexes.
        
        :param text: The target string.
        :param range: The range which has start and end indexes to use for slicing the string.
        """
        ...

    @staticmethod
    @overload
    def as_span(text: str, start: int, length: int) -> System.ReadOnlySpan[str]:
        """
        Creates a new readonly span over the portion of the target string.
        
        :param text: The target string.
        :param start: The index at which to begin this slice.
        :param length: The desired length for the slice (exclusive).
        """
        ...

    @staticmethod
    def compare_to(span: System.ReadOnlySpan[str], other: System.ReadOnlySpan[str], comparison_type: System.StringComparison) -> int:
        """
        Compares the specified  and  using the specified ,
        and returns an integer that indicates their relative position in the sort order.
        
        :param span: The source span.
        :param other: The value to compare with the source span.
        :param comparison_type: One of the enumeration values that determines how the  and  are compared.
        """
        ...

    @staticmethod
    def contains(span: System.ReadOnlySpan[str], value: System.ReadOnlySpan[str], comparison_type: System.StringComparison) -> bool:
        """
        Returns a value indicating whether the specified  occurs within the .
        
        :param span: The source span.
        :param value: The value to seek within the source span.
        :param comparison_type: One of the enumeration values that determines how the  and  are compared.
        """
        ...

    @staticmethod
    @overload
    def contains_any(span: System.Span[str], values: System.Buffers.SearchValues[str]) -> bool:
        ...

    @staticmethod
    @overload
    def contains_any(span: System.ReadOnlySpan[str], values: System.Buffers.SearchValues[str]) -> bool:
        """
        Searches for any occurrence of any of the specified substring  and returns true if found. If not found, returns false.
        
        :param span: The span to search.
        :param values: The set of values to search for.
        """
        ...

    @staticmethod
    def ends_with(span: System.ReadOnlySpan[str], value: System.ReadOnlySpan[str], comparison_type: System.StringComparison) -> bool:
        """
        Determines whether the end of the  matches the specified  when compared using the specified  option.
        
        :param span: The source span.
        :param value: The sequence to compare to the end of the source span.
        :param comparison_type: One of the enumeration values that determines how the  and  are compared.
        """
        ...

    @staticmethod
    @overload
    def enumerate_lines(span: System.ReadOnlySpan[str]) -> System.Text.SpanLineEnumerator:
        """Returns an enumeration of lines over the provided span."""
        ...

    @staticmethod
    @overload
    def enumerate_lines(span: System.Span[str]) -> System.Text.SpanLineEnumerator:
        """Returns an enumeration of lines over the provided span."""
        ...

    @staticmethod
    @overload
    def enumerate_runes(span: System.ReadOnlySpan[str]) -> System.Text.SpanRuneEnumerator:
        """Returns an enumeration of Rune from the provided span."""
        ...

    @staticmethod
    @overload
    def enumerate_runes(span: System.Span[str]) -> System.Text.SpanRuneEnumerator:
        """Returns an enumeration of Rune from the provided span."""
        ...

    @staticmethod
    def equals(span: System.ReadOnlySpan[str], other: System.ReadOnlySpan[str], comparison_type: System.StringComparison) -> bool:
        """
        Determines whether this  and the specified  span have the same characters
        when compared using the specified  option.
        
        :param span: The source span.
        :param other: The value to compare with the source span.
        :param comparison_type: One of the enumeration values that determines how the  and  are compared.
        """
        ...

    @staticmethod
    def index_of(span: System.ReadOnlySpan[str], value: System.ReadOnlySpan[str], comparison_type: System.StringComparison) -> int:
        """
        Reports the zero-based index of the first occurrence of the specified  in the current .
        
        :param span: The source span.
        :param value: The value to seek within the source span.
        :param comparison_type: One of the enumeration values that determines how the  and  are compared.
        """
        ...

    @staticmethod
    @overload
    def index_of_any(span: System.Span[str], values: System.Buffers.SearchValues[str]) -> int:
        """
        Searches for the first index of any of the specified substring values.
        
        :param span: The span to search.
        :param values: The set of values to search for.
        """
        ...

    @staticmethod
    @overload
    def index_of_any(span: System.ReadOnlySpan[str], values: System.Buffers.SearchValues[str]) -> int:
        """
        Searches for the first index of any of the specified substring values.
        
        :param span: The span to search.
        :param values: The set of values to search for.
        :returns: The first index of any of the specified values, or -1 if none are found.
        """
        ...

    @staticmethod
    def is_white_space(span: System.ReadOnlySpan[str]) -> bool:
        """Indicates whether the specified span contains only white-space characters."""
        ...

    @staticmethod
    def last_index_of(span: System.ReadOnlySpan[str], value: System.ReadOnlySpan[str], comparison_type: System.StringComparison) -> int:
        """
        Reports the zero-based index of the last occurrence of the specified  in the current .
        
        :param span: The source span.
        :param value: The value to seek within the source span.
        :param comparison_type: One of the enumeration values that determines how the  and  are compared.
        """
        ...

    @staticmethod
    @overload
    def split(source: System.ReadOnlySpan[str], destination: System.Span[System.Range], separator: str, options: System.StringSplitOptions = ...) -> int:
        """
        Parses the source ReadOnlySpan{Char} for the specified , populating the  span
        with Range instances representing the regions between the separators.
        
        :param source: The source span to parse.
        :param destination: The destination span into which the resulting ranges are written.
        :param separator: A character that delimits the regions in this instance.
        :param options: A bitwise combination of the enumeration values that specifies whether to trim whitespace and include empty ranges.
        :returns: The number of ranges written into .
        """
        ...

    @staticmethod
    @overload
    def split(source: System.ReadOnlySpan[str], destination: System.Span[System.Range], separator: System.ReadOnlySpan[str], options: System.StringSplitOptions = ...) -> int:
        """
        Parses the source ReadOnlySpan{Char} for the specified , populating the  span
        with Range instances representing the regions between the separators.
        
        :param source: The source span to parse.
        :param destination: The destination span into which the resulting ranges are written.
        :param separator: A character that delimits the regions in this instance.
        :param options: A bitwise combination of the enumeration values that specifies whether to trim whitespace and include empty ranges.
        :returns: The number of ranges written into .
        """
        ...

    @staticmethod
    def split_any(source: System.ReadOnlySpan[str], destination: System.Span[System.Range], separators: System.ReadOnlySpan[str], options: System.StringSplitOptions = ...) -> int:
        """
        Parses the source ReadOnlySpan{Char} for one of the specified , populating the  span
        with Range instances representing the regions between the separators.
        
        :param source: The source span to parse.
        :param destination: The destination span into which the resulting ranges are written.
        :param separators: Any number of characters that may delimit the regions in this instance. If empty, all Unicode whitespace characters are used as the separators.
        :param options: A bitwise combination of the enumeration values that specifies whether to trim whitespace and include empty ranges.
        :returns: The number of ranges written into .
        """
        ...

    @staticmethod
    def starts_with(span: System.ReadOnlySpan[str], value: System.ReadOnlySpan[str], comparison_type: System.StringComparison) -> bool:
        """
        Determines whether the beginning of the  matches the specified  when compared using the specified  option.
        
        :param span: The source span.
        :param value: The sequence to compare to the beginning of the source span.
        :param comparison_type: One of the enumeration values that determines how the  and  are compared.
        """
        ...

    @staticmethod
    def to_lower(source: System.ReadOnlySpan[str], destination: System.Span[str], culture: System.Globalization.CultureInfo) -> int:
        """
        Copies the characters from the source span into the destination, converting each character to lowercase,
        using the casing rules of the specified culture.
        
        :param source: The source span.
        :param destination: The destination span which contains the transformed characters.
        :param culture: An object that supplies culture-specific casing rules.
        :returns: The number of characters written into the destination span. If the destination is too small, returns -1.
        """
        ...

    @staticmethod
    def to_lower_invariant(source: System.ReadOnlySpan[str], destination: System.Span[str]) -> int:
        """
        Copies the characters from the source span into the destination, converting each character to lowercase,
        using the casing rules of the invariant culture.
        
        :param source: The source span.
        :param destination: The destination span which contains the transformed characters.
        :returns: The number of characters written into the destination span. If the destination is too small, returns -1.
        """
        ...

    @staticmethod
    def to_upper(source: System.ReadOnlySpan[str], destination: System.Span[str], culture: System.Globalization.CultureInfo) -> int:
        """
        Copies the characters from the source span into the destination, converting each character to uppercase,
        using the casing rules of the specified culture.
        
        :param source: The source span.
        :param destination: The destination span which contains the transformed characters.
        :param culture: An object that supplies culture-specific casing rules.
        :returns: The number of characters written into the destination span. If the destination is too small, returns -1.
        """
        ...

    @staticmethod
    def to_upper_invariant(source: System.ReadOnlySpan[str], destination: System.Span[str]) -> int:
        """
        Copies the characters from the source span into the destination, converting each character to uppercase
        using the casing rules of the invariant culture.
        
        :param source: The source span.
        :param destination: The destination span which contains the transformed characters.
        :returns: The number of characters written into the destination span. If the destination is too small, returns -1.
        """
        ...

    @staticmethod
    @overload
    def trim(memory: System.Memory[str]) -> System.Memory[str]:
        """
        Removes all leading and trailing white-space characters from the memory.
        
        :param memory: The source memory from which the characters are removed.
        """
        ...

    @staticmethod
    @overload
    def trim(memory: System.ReadOnlyMemory[str]) -> System.ReadOnlyMemory[str]:
        """
        Removes all leading and trailing white-space characters from the memory.
        
        :param memory: The source memory from which the characters are removed.
        """
        ...

    @staticmethod
    @overload
    def trim(span: System.ReadOnlySpan[str]) -> System.ReadOnlySpan[str]:
        """
        Removes all leading and trailing white-space characters from the span.
        
        :param span: The source span from which the characters are removed.
        """
        ...

    @staticmethod
    @overload
    def trim(span: System.ReadOnlySpan[str], trim_char: str) -> System.ReadOnlySpan[str]:
        """
        Removes all leading and trailing occurrences of a specified character from the span.
        
        :param span: The source span from which the character is removed.
        :param trim_char: The specified character to look for and remove.
        """
        ...

    @staticmethod
    @overload
    def trim(span: System.ReadOnlySpan[str], trim_chars: System.ReadOnlySpan[str]) -> System.ReadOnlySpan[str]:
        """
        Removes all leading and trailing occurrences of a set of characters specified
        in a readonly span from the span.
        
        :param span: The source span from which the characters are removed.
        :param trim_chars: The span which contains the set of characters to remove.
        """
        ...

    @staticmethod
    @overload
    def trim(span: System.Span[str]) -> System.Span[str]:
        """
        Removes all leading and trailing white-space characters from the span.
        
        :param span: The source span from which the characters are removed.
        """
        ...

    @staticmethod
    @overload
    def trim_end(memory: System.Memory[str]) -> System.Memory[str]:
        """
        Removes all trailing white-space characters from the memory.
        
        :param memory: The source memory from which the characters are removed.
        """
        ...

    @staticmethod
    @overload
    def trim_end(memory: System.ReadOnlyMemory[str]) -> System.ReadOnlyMemory[str]:
        """
        Removes all trailing white-space characters from the memory.
        
        :param memory: The source memory from which the characters are removed.
        """
        ...

    @staticmethod
    @overload
    def trim_end(span: System.ReadOnlySpan[str]) -> System.ReadOnlySpan[str]:
        """
        Removes all trailing white-space characters from the span.
        
        :param span: The source span from which the characters are removed.
        """
        ...

    @staticmethod
    @overload
    def trim_end(span: System.ReadOnlySpan[str], trim_char: str) -> System.ReadOnlySpan[str]:
        """
        Removes all trailing occurrences of a specified character from the span.
        
        :param span: The source span from which the character is removed.
        :param trim_char: The specified character to look for and remove.
        """
        ...

    @staticmethod
    @overload
    def trim_end(span: System.ReadOnlySpan[str], trim_chars: System.ReadOnlySpan[str]) -> System.ReadOnlySpan[str]:
        """
        Removes all trailing occurrences of a set of characters specified
        in a readonly span from the span.
        
        :param span: The source span from which the characters are removed.
        :param trim_chars: The span which contains the set of characters to remove.
        """
        ...

    @staticmethod
    @overload
    def trim_end(span: System.Span[str]) -> System.Span[str]:
        """
        Removes all trailing white-space characters from the span.
        
        :param span: The source span from which the characters are removed.
        """
        ...

    @staticmethod
    @overload
    def trim_start(memory: System.Memory[str]) -> System.Memory[str]:
        """
        Removes all leading white-space characters from the memory.
        
        :param memory: The source memory from which the characters are removed.
        """
        ...

    @staticmethod
    @overload
    def trim_start(memory: System.ReadOnlyMemory[str]) -> System.ReadOnlyMemory[str]:
        """
        Removes all leading white-space characters from the memory.
        
        :param memory: The source memory from which the characters are removed.
        """
        ...

    @staticmethod
    @overload
    def trim_start(span: System.ReadOnlySpan[str]) -> System.ReadOnlySpan[str]:
        """
        Removes all leading white-space characters from the span.
        
        :param span: The source span from which the characters are removed.
        """
        ...

    @staticmethod
    @overload
    def trim_start(span: System.ReadOnlySpan[str], trim_char: str) -> System.ReadOnlySpan[str]:
        """
        Removes all leading occurrences of a specified character from the span.
        
        :param span: The source span from which the character is removed.
        :param trim_char: The specified character to look for and remove.
        """
        ...

    @staticmethod
    @overload
    def trim_start(span: System.ReadOnlySpan[str], trim_chars: System.ReadOnlySpan[str]) -> System.ReadOnlySpan[str]:
        """
        Removes all leading occurrences of a set of characters specified
        in a readonly span from the span.
        
        :param span: The source span from which the characters are removed.
        :param trim_chars: The span which contains the set of characters to remove.
        """
        ...

    @staticmethod
    @overload
    def trim_start(span: System.Span[str]) -> System.Span[str]:
        """
        Removes all leading white-space characters from the span.
        
        :param span: The source span from which the characters are removed.
        """
        ...

    @staticmethod
    @overload
    def try_write(destination: System.Span[str], handler: System.MemoryExtensions.TryWriteInterpolatedStringHandler, chars_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        """
        Writes the specified interpolated string to the character span.
        
        :param destination: The span to which the interpolated string should be formatted.
        :param handler: The interpolated string.
        :param chars_written: The number of characters written to the span.
        :returns: true if the entire interpolated string could be formatted successfully; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def try_write(destination: System.Span[str], provider: System.IFormatProvider, handler: System.MemoryExtensions.TryWriteInterpolatedStringHandler, chars_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        """
        Writes the specified interpolated string to the character span.
        
        :param destination: The span to which the interpolated string should be formatted.
        :param provider: An object that supplies culture-specific formatting information.
        :param handler: The interpolated string.
        :param chars_written: The number of characters written to the span.
        :returns: true if the entire interpolated string could be formatted successfully; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def try_write(destination: System.Span[str], provider: System.IFormatProvider, format: System.Text.CompositeFormat, chars_written: typing.Optional[int], *args: typing.Union[System.Object, typing.Iterable[System.Object]]) -> typing.Tuple[bool, int]:
        """
        Writes the CompositeFormat string to the character span, substituting the format item or items
        with the string representation of the corresponding arguments.
        
        :param destination: The span to which the string should be formatted.
        :param provider: An object that supplies culture-specific formatting information.
        :param format: A CompositeFormat.
        :param chars_written: The number of characters written to the span.
        :param args: An array of objects to format.
        :returns: true if the entire interpolated string could be formatted successfully; otherwise, false.
        """
        ...


class SerializableAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class MemberAccessException(System.SystemException):
    """This class has no documentation."""

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
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """
        This method is protected.
        
        Obsoletions.LegacyFormatterImplMessage
        """
        ...


class MissingMemberException(System.MemberAccessException):
    """This class has no documentation."""

    @property
    def message(self) -> str:
        ...

    @property
    def class_name(self) -> str:
        """This field is protected."""
        ...

    @class_name.setter
    def class_name(self, value: str) -> None:
        ...

    @property
    def member_name(self) -> str:
        """This field is protected."""
        ...

    @member_name.setter
    def member_name(self, value: str) -> None:
        ...

    @property
    def signature(self) -> typing.List[int]:
        """This field is protected."""
        ...

    @signature.setter
    def signature(self, value: typing.List[int]) -> None:
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
    def __init__(self, class_name: str, member_name: str) -> None:
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


class InsufficientMemoryException(System.OutOfMemoryException):
    """
    Purpose: The exception class for running out of memory
    but most likely in a non-fatal way that shouldn't
    be affected by escalation policy.  Use this for cases
    like MemoryFailPoint or a TryAllocate method, where you
    expect OOM's with no shared state corruption and you
    want to recover from these errors.
    """

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, message: str) -> None:
        ...

    @overload
    def __init__(self, message: str, inner_exception: System.Exception) -> None:
        ...


class IParsable(typing.Generic[System_IParsable_TSelf], metaclass=abc.ABCMeta):
    """Defines a mechanism for parsing a string to a value."""


class ValueTuple(typing.Generic[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3, System_ValueTuple_T4, System_ValueTuple_T5, System_ValueTuple_T6, System_ValueTuple_T7, System_ValueTuple_TRest], System.IEquatable[System_ValueTuple], System.Collections.IStructuralEquatable, System.Collections.IStructuralComparable, System.IComparable[System_ValueTuple], System.IValueTupleInternal):
    """Represents an 8-tuple, or octuple, as a value type."""

    @property
    def item_1(self) -> System_ValueTuple_T1:
        """The current ValueTuple{T1} instance's first component."""
        ...

    @item_1.setter
    def item_1(self, value: System_ValueTuple_T1) -> None:
        ...

    @property
    def item_1(self) -> System_ValueTuple_T1:
        """The current ValueTuple{T1, T2} instance's first component."""
        ...

    @item_1.setter
    def item_1(self, value: System_ValueTuple_T1) -> None:
        ...

    @property
    def item_2(self) -> System_ValueTuple_T2:
        """The current ValueTuple{T1, T2} instance's second component."""
        ...

    @item_2.setter
    def item_2(self, value: System_ValueTuple_T2) -> None:
        ...

    @property
    def item_1(self) -> System_ValueTuple_T1:
        """The current ValueTuple{T1, T2, T3} instance's first component."""
        ...

    @item_1.setter
    def item_1(self, value: System_ValueTuple_T1) -> None:
        ...

    @property
    def item_2(self) -> System_ValueTuple_T2:
        """The current ValueTuple{T1, T2, T3} instance's second component."""
        ...

    @item_2.setter
    def item_2(self, value: System_ValueTuple_T2) -> None:
        ...

    @property
    def item_3(self) -> System_ValueTuple_T3:
        """The current ValueTuple{T1, T2, T3} instance's third component."""
        ...

    @item_3.setter
    def item_3(self, value: System_ValueTuple_T3) -> None:
        ...

    @property
    def item_1(self) -> System_ValueTuple_T1:
        """The current ValueTuple{T1, T2, T3, T4} instance's first component."""
        ...

    @item_1.setter
    def item_1(self, value: System_ValueTuple_T1) -> None:
        ...

    @property
    def item_2(self) -> System_ValueTuple_T2:
        """The current ValueTuple{T1, T2, T3, T4} instance's second component."""
        ...

    @item_2.setter
    def item_2(self, value: System_ValueTuple_T2) -> None:
        ...

    @property
    def item_3(self) -> System_ValueTuple_T3:
        """The current ValueTuple{T1, T2, T3, T4} instance's third component."""
        ...

    @item_3.setter
    def item_3(self, value: System_ValueTuple_T3) -> None:
        ...

    @property
    def item_4(self) -> System_ValueTuple_T4:
        """The current ValueTuple{T1, T2, T3, T4} instance's fourth component."""
        ...

    @item_4.setter
    def item_4(self, value: System_ValueTuple_T4) -> None:
        ...

    @property
    def item_1(self) -> System_ValueTuple_T1:
        """The current ValueTuple{T1, T2, T3, T4, T5} instance's first component."""
        ...

    @item_1.setter
    def item_1(self, value: System_ValueTuple_T1) -> None:
        ...

    @property
    def item_2(self) -> System_ValueTuple_T2:
        """The current ValueTuple{T1, T2, T3, T4, T5} instance's second component."""
        ...

    @item_2.setter
    def item_2(self, value: System_ValueTuple_T2) -> None:
        ...

    @property
    def item_3(self) -> System_ValueTuple_T3:
        """The current ValueTuple{T1, T2, T3, T4, T5} instance's third component."""
        ...

    @item_3.setter
    def item_3(self, value: System_ValueTuple_T3) -> None:
        ...

    @property
    def item_4(self) -> System_ValueTuple_T4:
        """The current ValueTuple{T1, T2, T3, T4, T5} instance's fourth component."""
        ...

    @item_4.setter
    def item_4(self, value: System_ValueTuple_T4) -> None:
        ...

    @property
    def item_5(self) -> System_ValueTuple_T5:
        """The current ValueTuple{T1, T2, T3, T4, T5} instance's fifth component."""
        ...

    @item_5.setter
    def item_5(self, value: System_ValueTuple_T5) -> None:
        ...

    @property
    def item_1(self) -> System_ValueTuple_T1:
        """The current ValueTuple{T1, T2, T3, T4, T5, T6} instance's first component."""
        ...

    @item_1.setter
    def item_1(self, value: System_ValueTuple_T1) -> None:
        ...

    @property
    def item_2(self) -> System_ValueTuple_T2:
        """The current ValueTuple{T1, T2, T3, T4, T5, T6} instance's second component."""
        ...

    @item_2.setter
    def item_2(self, value: System_ValueTuple_T2) -> None:
        ...

    @property
    def item_3(self) -> System_ValueTuple_T3:
        """The current ValueTuple{T1, T2, T3, T4, T5, T6} instance's third component."""
        ...

    @item_3.setter
    def item_3(self, value: System_ValueTuple_T3) -> None:
        ...

    @property
    def item_4(self) -> System_ValueTuple_T4:
        """The current ValueTuple{T1, T2, T3, T4, T5, T6} instance's fourth component."""
        ...

    @item_4.setter
    def item_4(self, value: System_ValueTuple_T4) -> None:
        ...

    @property
    def item_5(self) -> System_ValueTuple_T5:
        """The current ValueTuple{T1, T2, T3, T4, T5, T6} instance's fifth component."""
        ...

    @item_5.setter
    def item_5(self, value: System_ValueTuple_T5) -> None:
        ...

    @property
    def item_6(self) -> System_ValueTuple_T6:
        """The current ValueTuple{T1, T2, T3, T4, T5, T6} instance's sixth component."""
        ...

    @item_6.setter
    def item_6(self, value: System_ValueTuple_T6) -> None:
        ...

    @property
    def item_1(self) -> System_ValueTuple_T1:
        """The current ValueTuple{T1, T2, T3, T4, T5, T6, T7} instance's first component."""
        ...

    @item_1.setter
    def item_1(self, value: System_ValueTuple_T1) -> None:
        ...

    @property
    def item_2(self) -> System_ValueTuple_T2:
        """The current ValueTuple{T1, T2, T3, T4, T5, T6, T7} instance's second component."""
        ...

    @item_2.setter
    def item_2(self, value: System_ValueTuple_T2) -> None:
        ...

    @property
    def item_3(self) -> System_ValueTuple_T3:
        """The current ValueTuple{T1, T2, T3, T4, T5, T6, T7} instance's third component."""
        ...

    @item_3.setter
    def item_3(self, value: System_ValueTuple_T3) -> None:
        ...

    @property
    def item_4(self) -> System_ValueTuple_T4:
        """The current ValueTuple{T1, T2, T3, T4, T5, T6, T7} instance's fourth component."""
        ...

    @item_4.setter
    def item_4(self, value: System_ValueTuple_T4) -> None:
        ...

    @property
    def item_5(self) -> System_ValueTuple_T5:
        """The current ValueTuple{T1, T2, T3, T4, T5, T6, T7} instance's fifth component."""
        ...

    @item_5.setter
    def item_5(self, value: System_ValueTuple_T5) -> None:
        ...

    @property
    def item_6(self) -> System_ValueTuple_T6:
        """The current ValueTuple{T1, T2, T3, T4, T5, T6, T7} instance's sixth component."""
        ...

    @item_6.setter
    def item_6(self, value: System_ValueTuple_T6) -> None:
        ...

    @property
    def item_7(self) -> System_ValueTuple_T7:
        """The current ValueTuple{T1, T2, T3, T4, T5, T6, T7} instance's seventh component."""
        ...

    @item_7.setter
    def item_7(self, value: System_ValueTuple_T7) -> None:
        ...

    @property
    def item_1(self) -> System_ValueTuple_T1:
        """The current ValueTuple{T1, T2, T3, T4, T5, T6, T7, TRest} instance's first component."""
        ...

    @item_1.setter
    def item_1(self, value: System_ValueTuple_T1) -> None:
        ...

    @property
    def item_2(self) -> System_ValueTuple_T2:
        """The current ValueTuple{T1, T2, T3, T4, T5, T6, T7, TRest} instance's second component."""
        ...

    @item_2.setter
    def item_2(self, value: System_ValueTuple_T2) -> None:
        ...

    @property
    def item_3(self) -> System_ValueTuple_T3:
        """The current ValueTuple{T1, T2, T3, T4, T5, T6, T7, TRest} instance's third component."""
        ...

    @item_3.setter
    def item_3(self, value: System_ValueTuple_T3) -> None:
        ...

    @property
    def item_4(self) -> System_ValueTuple_T4:
        """The current ValueTuple{T1, T2, T3, T4, T5, T6, T7, TRest} instance's fourth component."""
        ...

    @item_4.setter
    def item_4(self, value: System_ValueTuple_T4) -> None:
        ...

    @property
    def item_5(self) -> System_ValueTuple_T5:
        """The current ValueTuple{T1, T2, T3, T4, T5, T6, T7, TRest} instance's fifth component."""
        ...

    @item_5.setter
    def item_5(self, value: System_ValueTuple_T5) -> None:
        ...

    @property
    def item_6(self) -> System_ValueTuple_T6:
        """The current ValueTuple{T1, T2, T3, T4, T5, T6, T7, TRest} instance's sixth component."""
        ...

    @item_6.setter
    def item_6(self, value: System_ValueTuple_T6) -> None:
        ...

    @property
    def item_7(self) -> System_ValueTuple_T7:
        """The current ValueTuple{T1, T2, T3, T4, T5, T6, T7, TRest} instance's seventh component."""
        ...

    @item_7.setter
    def item_7(self, value: System_ValueTuple_T7) -> None:
        ...

    @property
    def rest(self) -> System_ValueTuple_TRest:
        """The current ValueTuple{T1, T2, T3, T4, T5, T6, T7, TRest} instance's eighth component."""
        ...

    @rest.setter
    def rest(self, value: System_ValueTuple_TRest) -> None:
        ...

    @overload
    def __ge__(self, other: System.ValueTuple) -> bool:
        ...

    @overload
    def __ge__(self, other: System.ValueTuple[System_ValueTuple_T1]) -> bool:
        ...

    @overload
    def __ge__(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2]) -> bool:
        ...

    @overload
    def __ge__(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3]) -> bool:
        ...

    @overload
    def __ge__(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3, System_ValueTuple_T4]) -> bool:
        ...

    @overload
    def __ge__(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3, System_ValueTuple_T4, System_ValueTuple_T5]) -> bool:
        ...

    @overload
    def __ge__(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3, System_ValueTuple_T4, System_ValueTuple_T5, System_ValueTuple_T6]) -> bool:
        ...

    @overload
    def __ge__(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3, System_ValueTuple_T4, System_ValueTuple_T5, System_ValueTuple_T6, System_ValueTuple_T7]) -> bool:
        ...

    @overload
    def __ge__(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3, System_ValueTuple_T4, System_ValueTuple_T5, System_ValueTuple_T6, System_ValueTuple_T7, System_ValueTuple_TRest]) -> bool:
        ...

    @overload
    def __gt__(self, other: System.ValueTuple) -> bool:
        ...

    @overload
    def __gt__(self, other: System.ValueTuple[System_ValueTuple_T1]) -> bool:
        ...

    @overload
    def __gt__(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2]) -> bool:
        ...

    @overload
    def __gt__(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3]) -> bool:
        ...

    @overload
    def __gt__(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3, System_ValueTuple_T4]) -> bool:
        ...

    @overload
    def __gt__(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3, System_ValueTuple_T4, System_ValueTuple_T5]) -> bool:
        ...

    @overload
    def __gt__(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3, System_ValueTuple_T4, System_ValueTuple_T5, System_ValueTuple_T6]) -> bool:
        ...

    @overload
    def __gt__(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3, System_ValueTuple_T4, System_ValueTuple_T5, System_ValueTuple_T6, System_ValueTuple_T7]) -> bool:
        ...

    @overload
    def __gt__(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3, System_ValueTuple_T4, System_ValueTuple_T5, System_ValueTuple_T6, System_ValueTuple_T7, System_ValueTuple_TRest]) -> bool:
        ...

    @overload
    def __init__(self, item_1: System_ValueTuple_T1) -> None:
        """
        Initializes a new instance of the ValueTuple{T1} value type.
        
        :param item_1: The value of the tuple's first component.
        """
        ...

    @overload
    def __init__(self, item_1: System_ValueTuple_T1, item_2: System_ValueTuple_T2) -> None:
        """
        Initializes a new instance of the ValueTuple{T1, T2} value type.
        
        :param item_1: The value of the tuple's first component.
        :param item_2: The value of the tuple's second component.
        """
        ...

    @overload
    def __init__(self, item_1: System_ValueTuple_T1, item_2: System_ValueTuple_T2, item_3: System_ValueTuple_T3) -> None:
        """
        Initializes a new instance of the ValueTuple{T1, T2, T3} value type.
        
        :param item_1: The value of the tuple's first component.
        :param item_2: The value of the tuple's second component.
        :param item_3: The value of the tuple's third component.
        """
        ...

    @overload
    def __init__(self, item_1: System_ValueTuple_T1, item_2: System_ValueTuple_T2, item_3: System_ValueTuple_T3, item_4: System_ValueTuple_T4) -> None:
        """
        Initializes a new instance of the ValueTuple{T1, T2, T3, T4} value type.
        
        :param item_1: The value of the tuple's first component.
        :param item_2: The value of the tuple's second component.
        :param item_3: The value of the tuple's third component.
        :param item_4: The value of the tuple's fourth component.
        """
        ...

    @overload
    def __init__(self, item_1: System_ValueTuple_T1, item_2: System_ValueTuple_T2, item_3: System_ValueTuple_T3, item_4: System_ValueTuple_T4, item_5: System_ValueTuple_T5) -> None:
        """
        Initializes a new instance of the ValueTuple{T1, T2, T3, T4, T5} value type.
        
        :param item_1: The value of the tuple's first component.
        :param item_2: The value of the tuple's second component.
        :param item_3: The value of the tuple's third component.
        :param item_4: The value of the tuple's fourth component.
        :param item_5: The value of the tuple's fifth component.
        """
        ...

    @overload
    def __init__(self, item_1: System_ValueTuple_T1, item_2: System_ValueTuple_T2, item_3: System_ValueTuple_T3, item_4: System_ValueTuple_T4, item_5: System_ValueTuple_T5, item_6: System_ValueTuple_T6) -> None:
        """
        Initializes a new instance of the ValueTuple{T1, T2, T3, T4, T5, T6} value type.
        
        :param item_1: The value of the tuple's first component.
        :param item_2: The value of the tuple's second component.
        :param item_3: The value of the tuple's third component.
        :param item_4: The value of the tuple's fourth component.
        :param item_5: The value of the tuple's fifth component.
        :param item_6: The value of the tuple's sixth component.
        """
        ...

    @overload
    def __init__(self, item_1: System_ValueTuple_T1, item_2: System_ValueTuple_T2, item_3: System_ValueTuple_T3, item_4: System_ValueTuple_T4, item_5: System_ValueTuple_T5, item_6: System_ValueTuple_T6, item_7: System_ValueTuple_T7) -> None:
        """
        Initializes a new instance of the ValueTuple{T1, T2, T3, T4, T5, T6, T7} value type.
        
        :param item_1: The value of the tuple's first component.
        :param item_2: The value of the tuple's second component.
        :param item_3: The value of the tuple's third component.
        :param item_4: The value of the tuple's fourth component.
        :param item_5: The value of the tuple's fifth component.
        :param item_6: The value of the tuple's sixth component.
        :param item_7: The value of the tuple's seventh component.
        """
        ...

    @overload
    def __init__(self, item_1: System_ValueTuple_T1, item_2: System_ValueTuple_T2, item_3: System_ValueTuple_T3, item_4: System_ValueTuple_T4, item_5: System_ValueTuple_T5, item_6: System_ValueTuple_T6, item_7: System_ValueTuple_T7, rest: System_ValueTuple_TRest) -> None:
        """
        Initializes a new instance of the ValueTuple{T1, T2, T3, T4, T5, T6, T7, TRest} value type.
        
        :param item_1: The value of the tuple's first component.
        :param item_2: The value of the tuple's second component.
        :param item_3: The value of the tuple's third component.
        :param item_4: The value of the tuple's fourth component.
        :param item_5: The value of the tuple's fifth component.
        :param item_6: The value of the tuple's sixth component.
        :param item_7: The value of the tuple's seventh component.
        :param rest: The value of the tuple's eight component.
        """
        ...

    @overload
    def __le__(self, other: System.ValueTuple) -> bool:
        ...

    @overload
    def __le__(self, other: System.ValueTuple[System_ValueTuple_T1]) -> bool:
        ...

    @overload
    def __le__(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2]) -> bool:
        ...

    @overload
    def __le__(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3]) -> bool:
        ...

    @overload
    def __le__(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3, System_ValueTuple_T4]) -> bool:
        ...

    @overload
    def __le__(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3, System_ValueTuple_T4, System_ValueTuple_T5]) -> bool:
        ...

    @overload
    def __le__(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3, System_ValueTuple_T4, System_ValueTuple_T5, System_ValueTuple_T6]) -> bool:
        ...

    @overload
    def __le__(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3, System_ValueTuple_T4, System_ValueTuple_T5, System_ValueTuple_T6, System_ValueTuple_T7]) -> bool:
        ...

    @overload
    def __le__(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3, System_ValueTuple_T4, System_ValueTuple_T5, System_ValueTuple_T6, System_ValueTuple_T7, System_ValueTuple_TRest]) -> bool:
        ...

    @overload
    def __lt__(self, other: System.ValueTuple) -> bool:
        ...

    @overload
    def __lt__(self, other: System.ValueTuple[System_ValueTuple_T1]) -> bool:
        ...

    @overload
    def __lt__(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2]) -> bool:
        ...

    @overload
    def __lt__(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3]) -> bool:
        ...

    @overload
    def __lt__(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3, System_ValueTuple_T4]) -> bool:
        ...

    @overload
    def __lt__(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3, System_ValueTuple_T4, System_ValueTuple_T5]) -> bool:
        ...

    @overload
    def __lt__(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3, System_ValueTuple_T4, System_ValueTuple_T5, System_ValueTuple_T6]) -> bool:
        ...

    @overload
    def __lt__(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3, System_ValueTuple_T4, System_ValueTuple_T5, System_ValueTuple_T6, System_ValueTuple_T7]) -> bool:
        ...

    @overload
    def __lt__(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3, System_ValueTuple_T4, System_ValueTuple_T5, System_ValueTuple_T6, System_ValueTuple_T7, System_ValueTuple_TRest]) -> bool:
        ...

    @overload
    def compare_to(self, other: System.ValueTuple) -> int:
        """
        Compares this instance to a specified instance and returns an indication of their relative values.
        
        :param other: An instance to compare.
        :returns: A signed number indicating the relative values of this instance and . Returns less than zero if this instance is less than , zero if this instance is equal to , and greater than zero if this instance is greater than .
        """
        ...

    @overload
    def compare_to(self, other: System.ValueTuple[System_ValueTuple_T1]) -> int:
        """
        Compares this instance to a specified instance and returns an indication of their relative values.
        
        :param other: An instance to compare.
        :returns: A signed number indicating the relative values of this instance and . Returns less than zero if this instance is less than , zero if this instance is equal to , and greater than zero if this instance is greater than .
        """
        ...

    @overload
    def compare_to(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2]) -> int:
        """
        Compares this instance to a specified instance and returns an indication of their relative values.
        
        :param other: An instance to compare.
        :returns: A signed number indicating the relative values of this instance and . Returns less than zero if this instance is less than , zero if this instance is equal to , and greater than zero if this instance is greater than .
        """
        ...

    @overload
    def compare_to(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3]) -> int:
        """
        Compares this instance to a specified instance and returns an indication of their relative values.
        
        :param other: An instance to compare.
        :returns: A signed number indicating the relative values of this instance and . Returns less than zero if this instance is less than , zero if this instance is equal to , and greater than zero if this instance is greater than .
        """
        ...

    @overload
    def compare_to(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3, System_ValueTuple_T4]) -> int:
        """
        Compares this instance to a specified instance and returns an indication of their relative values.
        
        :param other: An instance to compare.
        :returns: A signed number indicating the relative values of this instance and . Returns less than zero if this instance is less than , zero if this instance is equal to , and greater than zero if this instance is greater than .
        """
        ...

    @overload
    def compare_to(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3, System_ValueTuple_T4, System_ValueTuple_T5]) -> int:
        """
        Compares this instance to a specified instance and returns an indication of their relative values.
        
        :param other: An instance to compare.
        :returns: A signed number indicating the relative values of this instance and . Returns less than zero if this instance is less than , zero if this instance is equal to , and greater than zero if this instance is greater than .
        """
        ...

    @overload
    def compare_to(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3, System_ValueTuple_T4, System_ValueTuple_T5, System_ValueTuple_T6]) -> int:
        """
        Compares this instance to a specified instance and returns an indication of their relative values.
        
        :param other: An instance to compare.
        :returns: A signed number indicating the relative values of this instance and . Returns less than zero if this instance is less than , zero if this instance is equal to , and greater than zero if this instance is greater than .
        """
        ...

    @overload
    def compare_to(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3, System_ValueTuple_T4, System_ValueTuple_T5, System_ValueTuple_T6, System_ValueTuple_T7]) -> int:
        """
        Compares this instance to a specified instance and returns an indication of their relative values.
        
        :param other: An instance to compare.
        :returns: A signed number indicating the relative values of this instance and . Returns less than zero if this instance is less than , zero if this instance is equal to , and greater than zero if this instance is greater than .
        """
        ...

    @overload
    def compare_to(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3, System_ValueTuple_T4, System_ValueTuple_T5, System_ValueTuple_T6, System_ValueTuple_T7, System_ValueTuple_TRest]) -> int:
        """
        Compares this instance to a specified instance and returns an indication of their relative values.
        
        :param other: An instance to compare.
        :returns: A signed number indicating the relative values of this instance and . Returns less than zero if this instance is less than , zero if this instance is equal to , and greater than zero if this instance is greater than .
        """
        ...

    @staticmethod
    def create() -> System.ValueTuple:
        """
        Creates a new struct 0-tuple.
        
        :returns: A 0-tuple.
        """
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        """
        Returns a value that indicates whether the current ValueTuple instance is equal to a specified object.
        
        :param obj: The object to compare with this instance.
        :returns: true if  is a ValueTuple.
        """
        ...

    @overload
    def equals(self, other: System.ValueTuple) -> bool:
        """
        Returns a value indicating whether this instance is equal to a specified value.
        
        :param other: An instance to compare to this instance.
        :returns: true if  has the same value as this instance; otherwise, false.
        """
        ...

    @overload
    def equals(self, other: System.ValueTuple[System_ValueTuple_T1]) -> bool:
        """
        Returns a value that indicates whether the current ValueTuple{T1}
        instance is equal to a specified ValueTuple{T1}.
        
        :param other: The tuple to compare with this instance.
        :returns: true if the current instance is equal to the specified tuple; otherwise, false.
        """
        ...

    @overload
    def equals(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2]) -> bool:
        """
        Returns a value that indicates whether the current ValueTuple{T1, T2} instance is equal to a specified ValueTuple{T1, T2}.
        
        :param other: The tuple to compare with this instance.
        :returns: true if the current instance is equal to the specified tuple; otherwise, false.
        """
        ...

    @overload
    def equals(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3]) -> bool:
        """
        Returns a value that indicates whether the current ValueTuple{T1, T2, T3}
        instance is equal to a specified ValueTuple{T1, T2, T3}.
        
        :param other: The tuple to compare with this instance.
        :returns: true if the current instance is equal to the specified tuple; otherwise, false.
        """
        ...

    @overload
    def equals(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3, System_ValueTuple_T4]) -> bool:
        """
        Returns a value that indicates whether the current ValueTuple{T1, T2, T3, T4}
        instance is equal to a specified ValueTuple{T1, T2, T3, T4}.
        
        :param other: The tuple to compare with this instance.
        :returns: true if the current instance is equal to the specified tuple; otherwise, false.
        """
        ...

    @overload
    def equals(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3, System_ValueTuple_T4, System_ValueTuple_T5]) -> bool:
        """
        Returns a value that indicates whether the current ValueTuple{T1, T2, T3, T4, T5}
        instance is equal to a specified ValueTuple{T1, T2, T3, T4, T5}.
        
        :param other: The tuple to compare with this instance.
        :returns: true if the current instance is equal to the specified tuple; otherwise, false.
        """
        ...

    @overload
    def equals(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3, System_ValueTuple_T4, System_ValueTuple_T5, System_ValueTuple_T6]) -> bool:
        """
        Returns a value that indicates whether the current ValueTuple{T1, T2, T3, T4, T5, T6}
        instance is equal to a specified ValueTuple{T1, T2, T3, T4, T5, T6}.
        
        :param other: The tuple to compare with this instance.
        :returns: true if the current instance is equal to the specified tuple; otherwise, false.
        """
        ...

    @overload
    def equals(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3, System_ValueTuple_T4, System_ValueTuple_T5, System_ValueTuple_T6, System_ValueTuple_T7]) -> bool:
        """
        Returns a value that indicates whether the current ValueTuple{T1, T2, T3, T4, T5, T6, T7}
        instance is equal to a specified ValueTuple{T1, T2, T3, T4, T5, T6, T7}.
        
        :param other: The tuple to compare with this instance.
        :returns: true if the current instance is equal to the specified tuple; otherwise, false.
        """
        ...

    @overload
    def equals(self, other: System.ValueTuple[System_ValueTuple_T1, System_ValueTuple_T2, System_ValueTuple_T3, System_ValueTuple_T4, System_ValueTuple_T5, System_ValueTuple_T6, System_ValueTuple_T7, System_ValueTuple_TRest]) -> bool:
        """
        Returns a value that indicates whether the current ValueTuple{T1, T2, T3, T4, T5, T6, T7, TRest}
        instance is equal to a specified ValueTuple{T1, T2, T3, T4, T5, T6, T7, TRest}.
        
        :param other: The tuple to compare with this instance.
        :returns: true if the current instance is equal to the specified tuple; otherwise, false.
        """
        ...

    def get_hash_code(self) -> int:
        """
        Returns the hash code for this instance.
        
        :returns: A 32-bit signed integer hash code.
        """
        ...

    def to_string(self) -> str:
        """
        Returns a string that represents the value of this ValueTuple instance.
        
        :returns: The string representation of this ValueTuple instance.
        """
        ...


class ApplicationException(System.Exception):
    """Serves as the base class for application-defined exceptions."""

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


class IDisposable(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def dispose(self) -> None:
        ...


class IObservable(typing.Generic[System_IObservable_T], metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def subscribe(self, observer: System.IObserver[System_IObservable_T]) -> System.IDisposable:
        ...


class CharEnumerator(System.Object, System.Collections.Generic.IEnumerator[str], System.ICloneable):
    """Supports iterating over a string object and reading its individual characters."""

    @property
    def current(self) -> str:
        ...

    def clone(self) -> System.Object:
        ...

    def dispose(self) -> None:
        ...

    def move_next(self) -> bool:
        ...

    def reset(self) -> None:
        ...


class String(System.Object, System.IComparable[str], System.IConvertible, System.Collections.Generic.IEnumerable[str], System.IEquatable[str], System.ICloneable, System.ISpanParsable[str], typing.Iterable[str]):
    """This class has no documentation."""

    EMPTY: str

    @property
    def length(self) -> int:
        ...

    def __eq__(self, b: str) -> bool:
        ...

    @overload
    def __ge__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __ge__(self, other: str) -> bool:
        ...

    def __getitem__(self, index: int) -> str:
        ...

    @overload
    def __gt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __gt__(self, other: str) -> bool:
        ...

    @overload
    def __init__(self, value: typing.Any) -> None:
        ...

    @overload
    def __init__(self, value: typing.Any, start_index: int, length: int) -> None:
        ...

    @overload
    def __init__(self, value: typing.Any, start_index: int, length: int, enc: System.Text.Encoding) -> None:
        ...

    @overload
    def __init__(self, value: typing.List[str]) -> None:
        ...

    @overload
    def __init__(self, value: typing.List[str], start_index: int, length: int) -> None:
        ...

    @overload
    def __init__(self, c: str, count: int) -> None:
        ...

    @overload
    def __init__(self, value: System.ReadOnlySpan[str]) -> None:
        ...

    def __iter__(self) -> typing.Iterator[str]:
        ...

    @overload
    def __le__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __le__(self, other: str) -> bool:
        ...

    @overload
    def __lt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __lt__(self, other: str) -> bool:
        ...

    def __ne__(self, b: str) -> bool:
        ...

    def clone(self) -> System.Object:
        ...

    @staticmethod
    @overload
    def compare(str_a: str, str_b: str) -> int:
        ...

    @staticmethod
    @overload
    def compare(str_a: str, str_b: str, ignore_case: bool) -> int:
        ...

    @staticmethod
    @overload
    def compare(str_a: str, str_b: str, comparison_type: System.StringComparison) -> int:
        ...

    @staticmethod
    @overload
    def compare(str_a: str, str_b: str, culture: System.Globalization.CultureInfo, options: System.Globalization.CompareOptions) -> int:
        ...

    @staticmethod
    @overload
    def compare(str_a: str, str_b: str, ignore_case: bool, culture: System.Globalization.CultureInfo) -> int:
        ...

    @staticmethod
    @overload
    def compare(str_a: str, index_a: int, str_b: str, index_b: int, length: int) -> int:
        ...

    @staticmethod
    @overload
    def compare(str_a: str, index_a: int, str_b: str, index_b: int, length: int, ignore_case: bool) -> int:
        ...

    @staticmethod
    @overload
    def compare(str_a: str, index_a: int, str_b: str, index_b: int, length: int, ignore_case: bool, culture: System.Globalization.CultureInfo) -> int:
        ...

    @staticmethod
    @overload
    def compare(str_a: str, index_a: int, str_b: str, index_b: int, length: int, culture: System.Globalization.CultureInfo, options: System.Globalization.CompareOptions) -> int:
        ...

    @staticmethod
    @overload
    def compare(str_a: str, index_a: int, str_b: str, index_b: int, length: int, comparison_type: System.StringComparison) -> int:
        ...

    @staticmethod
    @overload
    def compare_ordinal(str_a: str, str_b: str) -> int:
        ...

    @staticmethod
    @overload
    def compare_ordinal(str_a: str, index_a: int, str_b: str, index_b: int, length: int) -> int:
        ...

    @overload
    def compare_to(self, value: typing.Any) -> int:
        ...

    @overload
    def compare_to(self, str_b: str) -> int:
        ...

    @staticmethod
    @overload
    def concat(arg_0: typing.Any) -> str:
        ...

    @staticmethod
    @overload
    def concat(arg_0: typing.Any, arg_1: typing.Any) -> str:
        ...

    @staticmethod
    @overload
    def concat(arg_0: typing.Any, arg_1: typing.Any, arg_2: typing.Any) -> str:
        ...

    @staticmethod
    @overload
    def concat(*args: typing.Union[System.Object, typing.Iterable[System.Object]]) -> str:
        ...

    @staticmethod
    @overload
    def concat(values: System.Collections.Generic.IEnumerable[str]) -> str:
        ...

    @staticmethod
    @overload
    def concat(str_0: str, str_1: str) -> str:
        ...

    @staticmethod
    @overload
    def concat(str_0: str, str_1: str, str_2: str) -> str:
        ...

    @staticmethod
    @overload
    def concat(str_0: str, str_1: str, str_2: str, str_3: str) -> str:
        ...

    @staticmethod
    @overload
    def concat(str_0: System.ReadOnlySpan[str], str_1: System.ReadOnlySpan[str]) -> str:
        ...

    @staticmethod
    @overload
    def concat(str_0: System.ReadOnlySpan[str], str_1: System.ReadOnlySpan[str], str_2: System.ReadOnlySpan[str]) -> str:
        ...

    @staticmethod
    @overload
    def concat(str_0: System.ReadOnlySpan[str], str_1: System.ReadOnlySpan[str], str_2: System.ReadOnlySpan[str], str_3: System.ReadOnlySpan[str]) -> str:
        ...

    @staticmethod
    @overload
    def concat(*values: typing.Union[str, typing.Iterable[str]]) -> str:
        ...

    @overload
    def contains(self, value: str) -> bool:
        ...

    @overload
    def contains(self, value: str, comparison_type: System.StringComparison) -> bool:
        ...

    @staticmethod
    def copy(str: str) -> str:
        """This API should not be used to create mutable strings. See https://go.microsoft.com/fwlink/?linkid=2084035 for alternatives."""
        warnings.warn("This API should not be used to create mutable strings. See https://go.microsoft.com/fwlink/?linkid=2084035 for alternatives.", DeprecationWarning)

    @overload
    def copy_to(self, source_index: int, destination: typing.List[str], destination_index: int, count: int) -> None:
        ...

    @overload
    def copy_to(self, destination: System.Span[str]) -> None:
        """
        Copies the contents of this string into the destination span.
        
        :param destination: The span into which to copy this string's contents.
        """
        ...

    @staticmethod
    @overload
    def create(provider: System.IFormatProvider, handler: System.Runtime.CompilerServices.DefaultInterpolatedStringHandler) -> str:
        """
        Creates a new string by using the specified provider to control the formatting of the specified interpolated string.
        
        :param provider: An object that supplies culture-specific formatting information.
        :param handler: The interpolated string.
        :returns: The string that results for formatting the interpolated string using the specified format provider.
        """
        ...

    @staticmethod
    @overload
    def create(provider: System.IFormatProvider, initial_buffer: System.Span[str], handler: System.Runtime.CompilerServices.DefaultInterpolatedStringHandler) -> str:
        """
        Creates a new string by using the specified provider to control the formatting of the specified interpolated string.
        
        :param provider: An object that supplies culture-specific formatting information.
        :param initial_buffer: The initial buffer that may be used as temporary space as part of the formatting operation. The contents of this buffer may be overwritten.
        :param handler: The interpolated string.
        :returns: The string that results for formatting the interpolated string using the specified format provider.
        """
        ...

    @overload
    def ends_with(self, value: str) -> bool:
        ...

    @overload
    def ends_with(self, value: str, comparison_type: System.StringComparison) -> bool:
        ...

    @overload
    def ends_with(self, value: str, ignore_case: bool, culture: System.Globalization.CultureInfo) -> bool:
        ...

    def enumerate_runes(self) -> System.Text.StringRuneEnumerator:
        """Returns an enumeration of Rune from this string."""
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, value: str) -> bool:
        ...

    @overload
    def equals(self, value: str, comparison_type: System.StringComparison) -> bool:
        ...

    @staticmethod
    @overload
    def equals(a: str, b: str) -> bool:
        ...

    @staticmethod
    @overload
    def equals(a: str, b: str, comparison_type: System.StringComparison) -> bool:
        ...

    @staticmethod
    @overload
    def format(format: str, arg_0: typing.Any) -> str:
        ...

    @staticmethod
    @overload
    def format(format: str, arg_0: typing.Any, arg_1: typing.Any) -> str:
        ...

    @staticmethod
    @overload
    def format(format: str, arg_0: typing.Any, arg_1: typing.Any, arg_2: typing.Any) -> str:
        ...

    @staticmethod
    @overload
    def format(provider: System.IFormatProvider, format: str, arg_0: typing.Any) -> str:
        ...

    @staticmethod
    @overload
    def format(provider: System.IFormatProvider, format: str, arg_0: typing.Any, arg_1: typing.Any) -> str:
        ...

    @staticmethod
    @overload
    def format(provider: System.IFormatProvider, format: str, arg_0: typing.Any, arg_1: typing.Any, arg_2: typing.Any) -> str:
        ...

    @staticmethod
    @overload
    def format(format: str, *args: typing.Union[System.Object, typing.Iterable[System.Object]]) -> str:
        ...

    @staticmethod
    @overload
    def format(provider: System.IFormatProvider, format: str, *args: typing.Union[System.Object, typing.Iterable[System.Object]]) -> str:
        ...

    @staticmethod
    @overload
    def format(provider: System.IFormatProvider, format: System.Text.CompositeFormat, *args: typing.Union[System.Object, typing.Iterable[System.Object]]) -> str:
        """
        Replaces the format item or items in a CompositeFormat with the string representation of the corresponding objects.
        A parameter supplies culture-specific formatting information.
        
        :param provider: An object that supplies culture-specific formatting information.
        :param format: A CompositeFormat.
        :param args: An array of objects to format.
        :returns: The formatted string.
        """
        ...

    def get_enumerator(self) -> System.CharEnumerator:
        ...

    @overload
    def get_hash_code(self) -> int:
        ...

    @overload
    def get_hash_code(self, comparison_type: System.StringComparison) -> int:
        ...

    @staticmethod
    @overload
    def get_hash_code(value: System.ReadOnlySpan[str]) -> int:
        ...

    @staticmethod
    @overload
    def get_hash_code(value: System.ReadOnlySpan[str], comparison_type: System.StringComparison) -> int:
        ...

    def get_pinnable_reference(self) -> typing.Any:
        """Returns a reference to the first element of the String. If the string is null, an access will throw a NullReferenceException."""
        ...

    def get_type_code(self) -> System.TypeCode:
        ...

    @overload
    def index_of(self, value: str) -> int:
        ...

    @overload
    def index_of(self, value: str, start_index: int) -> int:
        ...

    @overload
    def index_of(self, value: str, comparison_type: System.StringComparison) -> int:
        ...

    @overload
    def index_of(self, value: str, start_index: int, count: int) -> int:
        ...

    @overload
    def index_of(self, value: str, start_index: int, comparison_type: System.StringComparison) -> int:
        ...

    @overload
    def index_of(self, value: str, start_index: int, count: int, comparison_type: System.StringComparison) -> int:
        ...

    @overload
    def index_of_any(self, any_of: typing.List[str]) -> int:
        ...

    @overload
    def index_of_any(self, any_of: typing.List[str], start_index: int) -> int:
        ...

    @overload
    def index_of_any(self, any_of: typing.List[str], start_index: int, count: int) -> int:
        ...

    def insert(self, start_index: int, value: str) -> str:
        ...

    @staticmethod
    def intern(str: str) -> str:
        ...

    @staticmethod
    def is_interned(str: str) -> str:
        ...

    @overload
    def is_normalized(self) -> bool:
        ...

    @overload
    def is_normalized(self, normalization_form: System.Text.NormalizationForm) -> bool:
        ...

    @staticmethod
    def is_null_or_empty(value: str) -> bool:
        ...

    @staticmethod
    def is_null_or_white_space(value: str) -> bool:
        ...

    @staticmethod
    @overload
    def join(separator: str, *value: typing.Union[str, typing.Iterable[str]]) -> str:
        ...

    @staticmethod
    @overload
    def join(separator: str, value: typing.List[str], start_index: int, count: int) -> str:
        ...

    @staticmethod
    @overload
    def join(separator: str, values: System.Collections.Generic.IEnumerable[str]) -> str:
        ...

    @staticmethod
    @overload
    def join(separator: str, *values: typing.Union[System.Object, typing.Iterable[System.Object]]) -> str:
        ...

    @overload
    def last_index_of(self, value: str) -> int:
        ...

    @overload
    def last_index_of(self, value: str, start_index: int) -> int:
        ...

    @overload
    def last_index_of(self, value: str, start_index: int, count: int) -> int:
        ...

    @overload
    def last_index_of(self, value: str, comparison_type: System.StringComparison) -> int:
        ...

    @overload
    def last_index_of(self, value: str, start_index: int, comparison_type: System.StringComparison) -> int:
        ...

    @overload
    def last_index_of(self, value: str, start_index: int, count: int, comparison_type: System.StringComparison) -> int:
        ...

    @overload
    def last_index_of_any(self, any_of: typing.List[str]) -> int:
        ...

    @overload
    def last_index_of_any(self, any_of: typing.List[str], start_index: int) -> int:
        ...

    @overload
    def last_index_of_any(self, any_of: typing.List[str], start_index: int, count: int) -> int:
        ...

    @overload
    def normalize(self) -> str:
        ...

    @overload
    def normalize(self, normalization_form: System.Text.NormalizationForm) -> str:
        ...

    @overload
    def pad_left(self, total_width: int) -> str:
        ...

    @overload
    def pad_left(self, total_width: int, padding_char: str) -> str:
        ...

    @overload
    def pad_right(self, total_width: int) -> str:
        ...

    @overload
    def pad_right(self, total_width: int, padding_char: str) -> str:
        ...

    @overload
    def remove(self, start_index: int, count: int) -> str:
        ...

    @overload
    def remove(self, start_index: int) -> str:
        ...

    @overload
    def replace(self, old_value: str, new_value: str, ignore_case: bool, culture: System.Globalization.CultureInfo) -> str:
        ...

    @overload
    def replace(self, old_value: str, new_value: str, comparison_type: System.StringComparison) -> str:
        ...

    @overload
    def replace(self, old_char: str, new_char: str) -> str:
        ...

    @overload
    def replace(self, old_value: str, new_value: str) -> str:
        ...

    @overload
    def replace_line_endings(self) -> str:
        """
        Replaces all newline sequences in the current string with Environment.NewLine.
        
        :returns: A string whose contents match the current string, but with all newline sequences replaced with Environment.NewLine.
        """
        ...

    @overload
    def replace_line_endings(self, replacement_text: str) -> str:
        """
        Replaces all newline sequences in the current string with .
        
        :returns: A string whose contents match the current string, but with all newline sequences replaced with .
        """
        ...

    @overload
    def split(self, separator: str, options: System.StringSplitOptions = ...) -> typing.List[str]:
        ...

    @overload
    def split(self, separator: str, count: int, options: System.StringSplitOptions = ...) -> typing.List[str]:
        ...

    @overload
    def split(self, *separator: typing.Union[str, typing.Iterable[str]]) -> typing.List[str]:
        ...

    @overload
    def split(self, separator: typing.List[str], count: int) -> typing.List[str]:
        ...

    @overload
    def split(self, separator: typing.List[str], options: System.StringSplitOptions) -> typing.List[str]:
        ...

    @overload
    def split(self, separator: typing.List[str], count: int, options: System.StringSplitOptions) -> typing.List[str]:
        ...

    @overload
    def starts_with(self, value: str) -> bool:
        ...

    @overload
    def starts_with(self, value: str, comparison_type: System.StringComparison) -> bool:
        ...

    @overload
    def starts_with(self, value: str, ignore_case: bool, culture: System.Globalization.CultureInfo) -> bool:
        ...

    @overload
    def substring(self, start_index: int) -> str:
        ...

    @overload
    def substring(self, start_index: int, length: int) -> str:
        ...

    @overload
    def to_char_array(self) -> typing.List[str]:
        ...

    @overload
    def to_char_array(self, start_index: int, length: int) -> typing.List[str]:
        ...

    @overload
    def to_lower(self) -> str:
        ...

    @overload
    def to_lower(self, culture: System.Globalization.CultureInfo) -> str:
        ...

    def to_lower_invariant(self) -> str:
        ...

    @overload
    def to_string(self) -> str:
        ...

    @overload
    def to_string(self, provider: System.IFormatProvider) -> str:
        ...

    @overload
    def to_upper(self) -> str:
        ...

    @overload
    def to_upper(self, culture: System.Globalization.CultureInfo) -> str:
        ...

    def to_upper_invariant(self) -> str:
        ...

    @overload
    def trim(self) -> str:
        ...

    @overload
    def trim(self, trim_char: str) -> str:
        ...

    @overload
    def trim(self, *trim_chars: typing.Union[str, typing.Iterable[str]]) -> str:
        ...

    @overload
    def trim_end(self) -> str:
        ...

    @overload
    def trim_end(self, trim_char: str) -> str:
        ...

    @overload
    def trim_end(self, *trim_chars: typing.Union[str, typing.Iterable[str]]) -> str:
        ...

    @overload
    def trim_start(self) -> str:
        ...

    @overload
    def trim_start(self, trim_char: str) -> str:
        ...

    @overload
    def trim_start(self, *trim_chars: typing.Union[str, typing.Iterable[str]]) -> str:
        ...

    def try_copy_to(self, destination: System.Span[str]) -> bool:
        """
        Copies the contents of this string into the destination span.
        
        :param destination: The span into which to copy this string's contents.
        :returns: true if the data was copied; false if the destination was too short to fit the contents of the string.
        """
        ...


class ArithmeticException(System.SystemException):
    """The exception that is thrown for errors in an arithmetic, casting, or conversion operation."""

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


class TimeoutException(System.SystemException):
    """The exception that is thrown when the time allotted for a process or operation has expired."""

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


class TimeZoneInfo(System.Object, System.IEquatable[System_TimeZoneInfo], System.Runtime.Serialization.ISerializable, System.Runtime.Serialization.IDeserializationCallback):
    """This class has no documentation."""

    class AdjustmentRule(System.Object, System.IEquatable[System_TimeZoneInfo_AdjustmentRule], System.Runtime.Serialization.ISerializable, System.Runtime.Serialization.IDeserializationCallback):
        """This class has no documentation."""

        @property
        def date_start(self) -> datetime.datetime:
            ...

        @property
        def date_end(self) -> datetime.datetime:
            ...

        @property
        def daylight_delta(self) -> datetime.timedelta:
            ...

        @property
        def daylight_transition_start(self) -> System.TimeZoneInfo.TransitionTime:
            ...

        @property
        def daylight_transition_end(self) -> System.TimeZoneInfo.TransitionTime:
            ...

        @property
        def base_utc_offset_delta(self) -> datetime.timedelta:
            """Gets the time difference with the base UTC offset for the time zone during the adjustment-rule period."""
            ...

        @staticmethod
        @overload
        def create_adjustment_rule(date_start: typing.Union[datetime.datetime, datetime.date], date_end: typing.Union[datetime.datetime, datetime.date], daylight_delta: datetime.timedelta, daylight_transition_start: System.TimeZoneInfo.TransitionTime, daylight_transition_end: System.TimeZoneInfo.TransitionTime, base_utc_offset_delta: datetime.timedelta) -> System.TimeZoneInfo.AdjustmentRule:
            """
            Creates a new adjustment rule for a particular time zone.
            
            :param date_start: The effective date of the adjustment rule. If the value is DateTime.MinValue.Date, this is the first adjustment rule in effect for a time zone.
            :param date_end: The last date that the adjustment rule is in force. If the value is DateTime.MaxValue.Date, the adjustment rule has no end date.
            :param daylight_delta: The time change that results from the adjustment. This value is added to the time zone's System.TimeZoneInfo.BaseUtcOffset and System.TimeZoneInfo.BaseUtcOffsetDelta properties to obtain the correct daylight offset from Coordinated Universal Time (UTC). This value can range from -14 to 14.
            :param daylight_transition_start: The start of daylight saving time.
            :param daylight_transition_end: The end of daylight saving time.
            :param base_utc_offset_delta: The time difference with the base UTC offset for the time zone during the adjustment-rule period.
            :returns: The new adjustment rule.
            """
            ...

        @staticmethod
        @overload
        def create_adjustment_rule(date_start: typing.Union[datetime.datetime, datetime.date], date_end: typing.Union[datetime.datetime, datetime.date], daylight_delta: datetime.timedelta, daylight_transition_start: System.TimeZoneInfo.TransitionTime, daylight_transition_end: System.TimeZoneInfo.TransitionTime) -> System.TimeZoneInfo.AdjustmentRule:
            ...

        @overload
        def equals(self, obj: typing.Any) -> bool:
            """
            Indicates whether the current instance is equal to another instance.
            
            :param obj: An instance to compare with this instance.
            :returns: true if the current instance is equal to the other instance; otherwise, false.
            """
            ...

        @overload
        def equals(self, other: System.TimeZoneInfo.AdjustmentRule) -> bool:
            ...

        def get_hash_code(self) -> int:
            ...

    class TransitionTime(System.IEquatable[System_TimeZoneInfo_TransitionTime], System.Runtime.Serialization.ISerializable, System.Runtime.Serialization.IDeserializationCallback):
        """This class has no documentation."""

        @property
        def time_of_day(self) -> datetime.datetime:
            ...

        @property
        def month(self) -> int:
            ...

        @property
        def week(self) -> int:
            ...

        @property
        def day(self) -> int:
            ...

        @property
        def day_of_week(self) -> System.DayOfWeek:
            ...

        @property
        def is_fixed_date_rule(self) -> bool:
            ...

        def __eq__(self, t_2: System.TimeZoneInfo.TransitionTime) -> bool:
            ...

        def __ne__(self, t_2: System.TimeZoneInfo.TransitionTime) -> bool:
            ...

        @staticmethod
        def create_fixed_date_rule(time_of_day: typing.Union[datetime.datetime, datetime.date], month: int, day: int) -> System.TimeZoneInfo.TransitionTime:
            ...

        @staticmethod
        def create_floating_date_rule(time_of_day: typing.Union[datetime.datetime, datetime.date], month: int, week: int, day_of_week: System.DayOfWeek) -> System.TimeZoneInfo.TransitionTime:
            ...

        @overload
        def equals(self, obj: typing.Any) -> bool:
            ...

        @overload
        def equals(self, other: System.TimeZoneInfo.TransitionTime) -> bool:
            ...

        def get_hash_code(self) -> int:
            ...

    @property
    def id(self) -> str:
        ...

    @property
    def has_iana_id(self) -> bool:
        """Returns true if this TimeZoneInfo object has an IANA ID."""
        ...

    @property
    def display_name(self) -> str:
        ...

    @property
    def standard_name(self) -> str:
        ...

    @property
    def daylight_name(self) -> str:
        ...

    @property
    def base_utc_offset(self) -> datetime.timedelta:
        ...

    @property
    def supports_daylight_saving_time(self) -> bool:
        ...

    LOCAL: System.TimeZoneInfo
    """
    Returns a TimeZoneInfo instance that represents the local time on the machine.
    Accessing this property may throw InvalidTimeZoneException or COMException
    if the machine is in an unstable or corrupt state.
    """

    UTC: System.TimeZoneInfo
    """Returns a TimeZoneInfo instance that represents Universal Coordinated Time (UTC)"""

    @staticmethod
    def clear_cached_data() -> None:
        """Clears data from static members."""
        ...

    @staticmethod
    @overload
    def convert_time(date_time_offset: System.DateTimeOffset, destination_time_zone: System.TimeZoneInfo) -> System.DateTimeOffset:
        """Converts the value of the dateTime object from sourceTimeZone to destination_time_zone"""
        ...

    @staticmethod
    @overload
    def convert_time(date_time: typing.Union[datetime.datetime, datetime.date], destination_time_zone: System.TimeZoneInfo) -> datetime.datetime:
        """Converts the value of the date_time object from sourceTimeZone to destination_time_zone"""
        ...

    @staticmethod
    @overload
    def convert_time(date_time: typing.Union[datetime.datetime, datetime.date], source_time_zone: System.TimeZoneInfo, destination_time_zone: System.TimeZoneInfo) -> datetime.datetime:
        """Converts the value of the date_time object from source_time_zone to destination_time_zone"""
        ...

    @staticmethod
    @overload
    def convert_time_by_system_time_zone_id(date_time_offset: System.DateTimeOffset, destination_time_zone_id: str) -> System.DateTimeOffset:
        """Converts the value of a DateTime object from sourceTimeZone to destinationTimeZone."""
        ...

    @staticmethod
    @overload
    def convert_time_by_system_time_zone_id(date_time: typing.Union[datetime.datetime, datetime.date], destination_time_zone_id: str) -> datetime.datetime:
        """Converts the value of a DateTime object from sourceTimeZone to destinationTimeZone."""
        ...

    @staticmethod
    @overload
    def convert_time_by_system_time_zone_id(date_time: typing.Union[datetime.datetime, datetime.date], source_time_zone_id: str, destination_time_zone_id: str) -> datetime.datetime:
        """Converts the value of a DateTime object from sourceTimeZone to destinationTimeZone."""
        ...

    @staticmethod
    def convert_time_from_utc(date_time: typing.Union[datetime.datetime, datetime.date], destination_time_zone: System.TimeZoneInfo) -> datetime.datetime:
        """Converts the value of a DateTime object from Coordinated Universal Time (UTC) to the destination_time_zone."""
        ...

    @staticmethod
    @overload
    def convert_time_to_utc(date_time: typing.Union[datetime.datetime, datetime.date]) -> datetime.datetime:
        """Converts the value of a DateTime object to Coordinated Universal Time (UTC)."""
        ...

    @staticmethod
    @overload
    def convert_time_to_utc(date_time: typing.Union[datetime.datetime, datetime.date], source_time_zone: System.TimeZoneInfo) -> datetime.datetime:
        """Converts the value of a DateTime object to Coordinated Universal Time (UTC)."""
        ...

    @staticmethod
    @overload
    def create_custom_time_zone(id: str, base_utc_offset: datetime.timedelta, display_name: str, standard_display_name: str) -> System.TimeZoneInfo:
        """Returns a simple TimeZoneInfo instance that does not support Daylight Saving Time."""
        ...

    @staticmethod
    @overload
    def create_custom_time_zone(id: str, base_utc_offset: datetime.timedelta, display_name: str, standard_display_name: str, daylight_display_name: str, adjustment_rules: typing.List[System.TimeZoneInfo.AdjustmentRule]) -> System.TimeZoneInfo:
        """Returns a TimeZoneInfo instance that may support Daylight Saving Time."""
        ...

    @staticmethod
    @overload
    def create_custom_time_zone(id: str, base_utc_offset: datetime.timedelta, display_name: str, standard_display_name: str, daylight_display_name: str, adjustment_rules: typing.List[System.TimeZoneInfo.AdjustmentRule], disable_daylight_saving_time: bool) -> System.TimeZoneInfo:
        """Returns a TimeZoneInfo instance that may support Daylight Saving Time."""
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, other: System.TimeZoneInfo) -> bool:
        """
        Returns value equality. Equals does not compare any localizable
        String objects (DisplayName, StandardName, DaylightName).
        """
        ...

    @staticmethod
    def find_system_time_zone_by_id(id: str) -> System.TimeZoneInfo:
        """
        Helper function for retrieving a TimeZoneInfo object by time zone name.
        This function wraps the logic necessary to keep the private
        SystemTimeZones cache in working order.
        
        This function will either return a valid TimeZoneInfo instance or
        it will throw InvalidTimeZoneException / TimeZoneNotFoundException /
        SecurityException
        
        :param id: Time zone name.
        :returns: Valid TimeZoneInfo instance.
        """
        ...

    @staticmethod
    def from_serialized_string(source: str) -> System.TimeZoneInfo:
        ...

    def get_adjustment_rules(self) -> typing.List[System.TimeZoneInfo.AdjustmentRule]:
        """Returns a cloned array of AdjustmentRule objects"""
        ...

    @overload
    def get_ambiguous_time_offsets(self, date_time_offset: System.DateTimeOffset) -> typing.List[datetime.timedelta]:
        """
        Returns an array of TimeSpan objects representing all of
        the possible UTC offset values for this ambiguous time.
        """
        ...

    @overload
    def get_ambiguous_time_offsets(self, date_time: typing.Union[datetime.datetime, datetime.date]) -> typing.List[datetime.timedelta]:
        """
        Returns an array of TimeSpan objects representing all of
        possible UTC offset values for this ambiguous time.
        """
        ...

    def get_hash_code(self) -> int:
        ...

    @staticmethod
    @overload
    def get_system_time_zones() -> System.Collections.ObjectModel.ReadOnlyCollection[System.TimeZoneInfo]:
        """
        Returns a ReadOnlyCollection{TimeZoneInfo} containing all valid TimeZone's
        from the local machine. The entries in the collection are sorted by
        DisplayName.
        This method does *not* throw TimeZoneNotFoundException or InvalidTimeZoneException.
        """
        ...

    @staticmethod
    @overload
    def get_system_time_zones(skip_sorting: bool) -> System.Collections.ObjectModel.ReadOnlyCollection[System.TimeZoneInfo]:
        """
        Returns a ReadOnlyCollection{TimeZoneInfo} containing all valid TimeZone's from the local machine.
        This method does *not* throw TimeZoneNotFoundException or InvalidTimeZoneException.
        
        :param skip_sorting: If true, The collection returned may not necessarily be sorted.
        """
        ...

    @overload
    def get_utc_offset(self, date_time_offset: System.DateTimeOffset) -> datetime.timedelta:
        """Returns the Universal Coordinated Time (UTC) Offset for the current TimeZoneInfo instance."""
        ...

    @overload
    def get_utc_offset(self, date_time: typing.Union[datetime.datetime, datetime.date]) -> datetime.timedelta:
        """Returns the Universal Coordinated Time (UTC) Offset for the current TimeZoneInfo instance."""
        ...

    def has_same_rules(self, other: System.TimeZoneInfo) -> bool:
        """Value equality on the "adjustmentRules" array"""
        ...

    @overload
    def is_ambiguous_time(self, date_time_offset: System.DateTimeOffset) -> bool:
        """
        Returns true if the time is during the ambiguous time period
        for the current TimeZoneInfo instance.
        """
        ...

    @overload
    def is_ambiguous_time(self, date_time: typing.Union[datetime.datetime, datetime.date]) -> bool:
        """
        Returns true if the time is during the ambiguous time period
        for the current TimeZoneInfo instance.
        """
        ...

    @overload
    def is_daylight_saving_time(self, date_time_offset: System.DateTimeOffset) -> bool:
        """Returns true if the time is during Daylight Saving time for the current TimeZoneInfo instance."""
        ...

    @overload
    def is_daylight_saving_time(self, date_time: typing.Union[datetime.datetime, datetime.date]) -> bool:
        """Returns true if the time is during Daylight Saving time for the current TimeZoneInfo instance."""
        ...

    def is_invalid_time(self, date_time: typing.Union[datetime.datetime, datetime.date]) -> bool:
        """Returns true when date_time falls into a "hole in time"."""
        ...

    def to_serialized_string(self) -> str:
        ...

    def to_string(self) -> str:
        """Returns the DisplayName: "(GMT-08:00) Pacific Time (US & Canada); Tijuana\""""
        ...

    @staticmethod
    def try_convert_iana_id_to_windows_id(iana_id: str, windows_id: typing.Optional[str]) -> typing.Tuple[bool, str]:
        """
        Tries to convert an IANA time zone ID to a Windows ID.
        
        :param iana_id: The IANA time zone ID.
        :param windows_id: String object holding the Windows ID which resulted from the IANA ID conversion.
        :returns: True if the ID conversion succeeded, false otherwise.
        """
        ...

    @staticmethod
    @overload
    def try_convert_windows_id_to_iana_id(windows_id: str, iana_id: typing.Optional[str]) -> typing.Tuple[bool, str]:
        """
        Tries to convert a Windows time zone ID to an IANA ID.
        
        :param windows_id: The Windows time zone ID.
        :param iana_id: String object holding the IANA ID which resulted from the Windows ID conversion.
        :returns: True if the ID conversion succeeded, false otherwise.
        """
        ...

    @staticmethod
    @overload
    def try_convert_windows_id_to_iana_id(windows_id: str, region: str, iana_id: typing.Optional[str]) -> typing.Tuple[bool, str]:
        """
        Tries to convert a Windows time zone ID to an IANA ID.
        
        :param windows_id: The Windows time zone ID.
        :param region: The ISO 3166 code for the country/region.
        :param iana_id: String object holding the IANA ID which resulted from the Windows ID conversion.
        :returns: True if the ID conversion succeeded, false otherwise.
        """
        ...

    @staticmethod
    def try_find_system_time_zone_by_id(id: str, time_zone_info: typing.Optional[System.TimeZoneInfo]) -> typing.Tuple[bool, System.TimeZoneInfo]:
        """
        Helper function for retrieving a TimeZoneInfo object by time zone name.
        This function wraps the logic necessary to keep the private
        SystemTimeZones cache in working order.
        
        This function will either return true and a valid TimeZoneInfo
        instance or return false and null.
        
        :param id: Time zone name.
        :param time_zone_info: A valid retrieved TimeZoneInfo or null.
        :returns: true if the TimeZoneInfo object was successfully retrieved, false otherwise.
        """
        ...


class Buffer(System.Object):
    """This class has no documentation."""

    @staticmethod
    def block_copy(src: System.Array, src_offset: int, dst: System.Array, dst_offset: int, count: int) -> None:
        ...

    @staticmethod
    def byte_length(array: System.Array) -> int:
        ...

    @staticmethod
    def get_byte(array: System.Array, index: int) -> int:
        ...

    @staticmethod
    def memory_copy(source: typing.Any, destination: typing.Any, destination_size_in_bytes: int, source_bytes_to_copy: int) -> None:
        ...

    @staticmethod
    def set_byte(array: System.Array, index: int, value: int) -> None:
        ...


class IntPtr(System.IEquatable[System_IntPtr], System.IComparable[System_IntPtr], System.ISpanFormattable, System.Runtime.Serialization.ISerializable, System.Numerics.IBinaryInteger[System_IntPtr], System.Numerics.IMinMaxValue[System_IntPtr], System.Numerics.ISignedNumber[System_IntPtr], System.IUtf8SpanFormattable):
    """This class has no documentation."""

    ZERO: System.IntPtr

    SIZE: int

    MAX_VALUE: System.IntPtr

    MIN_VALUE: System.IntPtr

    def __add__(self, offset: int) -> System.IntPtr:
        ...

    def __eq__(self, value_2: System.IntPtr) -> bool:
        ...

    @overload
    def __ge__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __ge__(self, other: System.IntPtr) -> bool:
        ...

    @overload
    def __gt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __gt__(self, other: System.IntPtr) -> bool:
        ...

    def __iadd__(self, offset: int) -> System.IntPtr:
        ...

    @overload
    def __init__(self, value: typing.Any) -> None:
        ...

    @overload
    def __init__(self, value: int) -> None:
        ...

    def __isub__(self, offset: int) -> System.IntPtr:
        ...

    @overload
    def __le__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __le__(self, other: System.IntPtr) -> bool:
        ...

    @overload
    def __lt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __lt__(self, other: System.IntPtr) -> bool:
        ...

    def __ne__(self, value_2: System.IntPtr) -> bool:
        ...

    def __sub__(self, offset: int) -> System.IntPtr:
        ...

    @staticmethod
    def abs(value: System.IntPtr) -> System.IntPtr:
        ...

    @staticmethod
    def add(pointer: System.IntPtr, offset: int) -> System.IntPtr:
        ...

    @staticmethod
    def clamp(value: System.IntPtr, min: System.IntPtr, max: System.IntPtr) -> System.IntPtr:
        ...

    @overload
    def compare_to(self, value: typing.Any) -> int:
        ...

    @overload
    def compare_to(self, value: System.IntPtr) -> int:
        ...

    @staticmethod
    def copy_sign(value: System.IntPtr, sign: System.IntPtr) -> System.IntPtr:
        ...

    @staticmethod
    def div_rem(left: System.IntPtr, right: System.IntPtr) -> System.ValueTuple[System.IntPtr, System.IntPtr]:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, other: System.IntPtr) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    @staticmethod
    def is_even_integer(value: System.IntPtr) -> bool:
        ...

    @staticmethod
    def is_negative(value: System.IntPtr) -> bool:
        ...

    @staticmethod
    def is_odd_integer(value: System.IntPtr) -> bool:
        ...

    @staticmethod
    def is_positive(value: System.IntPtr) -> bool:
        ...

    @staticmethod
    def is_pow_2(value: System.IntPtr) -> bool:
        ...

    @staticmethod
    def leading_zero_count(value: System.IntPtr) -> System.IntPtr:
        ...

    @staticmethod
    def log_2(value: System.IntPtr) -> System.IntPtr:
        ...

    @staticmethod
    def max(x: System.IntPtr, y: System.IntPtr) -> System.IntPtr:
        ...

    @staticmethod
    def max_magnitude(x: System.IntPtr, y: System.IntPtr) -> System.IntPtr:
        ...

    @staticmethod
    def min(x: System.IntPtr, y: System.IntPtr) -> System.IntPtr:
        ...

    @staticmethod
    def min_magnitude(x: System.IntPtr, y: System.IntPtr) -> System.IntPtr:
        ...

    @staticmethod
    @overload
    def parse(s: str) -> System.IntPtr:
        ...

    @staticmethod
    @overload
    def parse(s: str, style: System.Globalization.NumberStyles) -> System.IntPtr:
        ...

    @staticmethod
    @overload
    def parse(s: str, provider: System.IFormatProvider) -> System.IntPtr:
        ...

    @staticmethod
    @overload
    def parse(s: str, style: System.Globalization.NumberStyles, provider: System.IFormatProvider) -> System.IntPtr:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider) -> System.IntPtr:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> System.IntPtr:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int], style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> System.IntPtr:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int], provider: System.IFormatProvider) -> System.IntPtr:
        ...

    @staticmethod
    def pop_count(value: System.IntPtr) -> System.IntPtr:
        ...

    @staticmethod
    def rotate_left(value: System.IntPtr, rotate_amount: int) -> System.IntPtr:
        ...

    @staticmethod
    def rotate_right(value: System.IntPtr, rotate_amount: int) -> System.IntPtr:
        ...

    @staticmethod
    def sign(value: System.IntPtr) -> int:
        ...

    @staticmethod
    def subtract(pointer: System.IntPtr, offset: int) -> System.IntPtr:
        ...

    def to_int_32(self) -> int:
        ...

    def to_int_64(self) -> int:
        ...

    def to_pointer(self) -> typing.Any:
        ...

    @overload
    def to_string(self) -> str:
        ...

    @overload
    def to_string(self, format: str) -> str:
        ...

    @overload
    def to_string(self, provider: System.IFormatProvider) -> str:
        ...

    @overload
    def to_string(self, format: str, provider: System.IFormatProvider) -> str:
        ...

    @staticmethod
    def trailing_zero_count(value: System.IntPtr) -> System.IntPtr:
        ...

    @overload
    def try_format(self, destination: System.Span[str], chars_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @overload
    def try_format(self, utf_8_destination: System.Span[int], bytes_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, result: typing.Optional[System.IntPtr]) -> typing.Tuple[bool, System.IntPtr]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, provider: System.IFormatProvider, result: typing.Optional[System.IntPtr]) -> typing.Tuple[bool, System.IntPtr]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[System.IntPtr]) -> typing.Tuple[bool, System.IntPtr]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], result: typing.Optional[System.IntPtr]) -> typing.Tuple[bool, System.IntPtr]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], result: typing.Optional[System.IntPtr]) -> typing.Tuple[bool, System.IntPtr]:
        """
        Tries to convert a UTF-8 character span containing the string representation of a number to its signed integer equivalent.
        
        :param utf_8_text: A span containing the UTF-8 characters representing the number to convert.
        :param result: When this method returns, contains the signed integer value equivalent to the number contained in  if the conversion succeeded, or zero if the conversion failed. This parameter is passed uninitialized; any value originally supplied in result will be overwritten.
        :returns: true if  was converted successfully; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider, result: typing.Optional[System.IntPtr]) -> typing.Tuple[bool, System.IntPtr]:
        """
        Tries to parse a string into a value.
        
        :param s: A read-only span of characters containing a number to convert.
        :param provider: An object that provides culture-specific formatting information about .
        :param result: When this method returns, contains the result of successfully parsing  or an undefined value on failure.
        :returns: true if  was converted successfully; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[System.IntPtr]) -> typing.Tuple[bool, System.IntPtr]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[System.IntPtr]) -> typing.Tuple[bool, System.IntPtr]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], provider: System.IFormatProvider, result: typing.Optional[System.IntPtr]) -> typing.Tuple[bool, System.IntPtr]:
        ...


class UIntPtr(System.IEquatable[System_UIntPtr], System.IComparable[System_UIntPtr], System.ISpanFormattable, System.Runtime.Serialization.ISerializable, System.Numerics.IBinaryInteger[System_UIntPtr], System.Numerics.IMinMaxValue[System_UIntPtr], System.Numerics.IUnsignedNumber[System_UIntPtr], System.IUtf8SpanFormattable):
    """This class has no documentation."""

    ZERO: System.UIntPtr

    SIZE: int

    MAX_VALUE: System.UIntPtr

    MIN_VALUE: System.UIntPtr

    def __add__(self, offset: int) -> System.UIntPtr:
        ...

    def __eq__(self, value_2: System.UIntPtr) -> bool:
        ...

    @overload
    def __ge__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __ge__(self, other: System.UIntPtr) -> bool:
        ...

    @overload
    def __gt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __gt__(self, other: System.UIntPtr) -> bool:
        ...

    def __iadd__(self, offset: int) -> System.UIntPtr:
        ...

    @overload
    def __init__(self, value: typing.Any) -> None:
        ...

    @overload
    def __init__(self, value: int) -> None:
        ...

    def __isub__(self, offset: int) -> System.UIntPtr:
        ...

    @overload
    def __le__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __le__(self, other: System.UIntPtr) -> bool:
        ...

    @overload
    def __lt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __lt__(self, other: System.UIntPtr) -> bool:
        ...

    def __ne__(self, value_2: System.UIntPtr) -> bool:
        ...

    def __sub__(self, offset: int) -> System.UIntPtr:
        ...

    @staticmethod
    def add(pointer: System.UIntPtr, offset: int) -> System.UIntPtr:
        ...

    @staticmethod
    def clamp(value: System.UIntPtr, min: System.UIntPtr, max: System.UIntPtr) -> System.UIntPtr:
        ...

    @overload
    def compare_to(self, value: typing.Any) -> int:
        ...

    @overload
    def compare_to(self, value: System.UIntPtr) -> int:
        ...

    @staticmethod
    def div_rem(left: System.UIntPtr, right: System.UIntPtr) -> System.ValueTuple[System.UIntPtr, System.UIntPtr]:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, other: System.UIntPtr) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    @staticmethod
    def is_even_integer(value: System.UIntPtr) -> bool:
        ...

    @staticmethod
    def is_odd_integer(value: System.UIntPtr) -> bool:
        ...

    @staticmethod
    def is_pow_2(value: System.UIntPtr) -> bool:
        ...

    @staticmethod
    def leading_zero_count(value: System.UIntPtr) -> System.UIntPtr:
        ...

    @staticmethod
    def log_2(value: System.UIntPtr) -> System.UIntPtr:
        ...

    @staticmethod
    def max(x: System.UIntPtr, y: System.UIntPtr) -> System.UIntPtr:
        ...

    @staticmethod
    def min(x: System.UIntPtr, y: System.UIntPtr) -> System.UIntPtr:
        ...

    @staticmethod
    @overload
    def parse(s: str) -> System.UIntPtr:
        ...

    @staticmethod
    @overload
    def parse(s: str, style: System.Globalization.NumberStyles) -> System.UIntPtr:
        ...

    @staticmethod
    @overload
    def parse(s: str, provider: System.IFormatProvider) -> System.UIntPtr:
        ...

    @staticmethod
    @overload
    def parse(s: str, style: System.Globalization.NumberStyles, provider: System.IFormatProvider) -> System.UIntPtr:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider) -> System.UIntPtr:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> System.UIntPtr:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int], style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> System.UIntPtr:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int], provider: System.IFormatProvider) -> System.UIntPtr:
        ...

    @staticmethod
    def pop_count(value: System.UIntPtr) -> System.UIntPtr:
        ...

    @staticmethod
    def rotate_left(value: System.UIntPtr, rotate_amount: int) -> System.UIntPtr:
        ...

    @staticmethod
    def rotate_right(value: System.UIntPtr, rotate_amount: int) -> System.UIntPtr:
        ...

    @staticmethod
    def sign(value: System.UIntPtr) -> int:
        ...

    @staticmethod
    def subtract(pointer: System.UIntPtr, offset: int) -> System.UIntPtr:
        ...

    def to_pointer(self) -> typing.Any:
        ...

    @overload
    def to_string(self) -> str:
        ...

    @overload
    def to_string(self, format: str) -> str:
        ...

    @overload
    def to_string(self, provider: System.IFormatProvider) -> str:
        ...

    @overload
    def to_string(self, format: str, provider: System.IFormatProvider) -> str:
        ...

    def to_u_int_32(self) -> int:
        ...

    def to_u_int_64(self) -> int:
        ...

    @staticmethod
    def trailing_zero_count(value: System.UIntPtr) -> System.UIntPtr:
        ...

    @overload
    def try_format(self, destination: System.Span[str], chars_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @overload
    def try_format(self, utf_8_destination: System.Span[int], bytes_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, result: typing.Optional[System.UIntPtr]) -> typing.Tuple[bool, System.UIntPtr]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider, result: typing.Optional[System.UIntPtr]) -> typing.Tuple[bool, System.UIntPtr]:
        """
        Tries to parse a string into a value.
        
        :param s: A read-only span of characters containing a number to convert.
        :param provider: An object that provides culture-specific formatting information about .
        :param result: When this method returns, contains the result of successfully parsing  or an undefined value on failure.
        :returns: true if  was converted successfully; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def try_parse(s: str, style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[System.UIntPtr]) -> typing.Tuple[bool, System.UIntPtr]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], result: typing.Optional[System.UIntPtr]) -> typing.Tuple[bool, System.UIntPtr]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], result: typing.Optional[System.UIntPtr]) -> typing.Tuple[bool, System.UIntPtr]:
        """
        Tries to convert a UTF-8 character span containing the string representation of a number to its unsigned integer equivalent.
        
        :param utf_8_text: A span containing the UTF-8 characters representing the number to convert.
        :param result: When this method returns, contains the unsigned integer value equivalent to the number contained in  if the conversion succeeded, or zero if the conversion failed. This parameter is passed uninitialized; any value originally supplied in result will be overwritten.
        :returns: true if  was converted successfully; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def try_parse(s: str, provider: System.IFormatProvider, result: typing.Optional[System.UIntPtr]) -> typing.Tuple[bool, System.UIntPtr]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[System.UIntPtr]) -> typing.Tuple[bool, System.UIntPtr]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[System.UIntPtr]) -> typing.Tuple[bool, System.UIntPtr]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], provider: System.IFormatProvider, result: typing.Optional[System.UIntPtr]) -> typing.Tuple[bool, System.UIntPtr]:
        ...


class Math(System.Object):
    """Math helpers for generated code. The helpers here are referenced by the runtime."""

    E: float = 2.7182818284590452354

    PI: float = 3.14159265358979323846

    TAU: float = 6.283185307179586476925

    @staticmethod
    @overload
    def abs(value: int) -> int:
        ...

    @staticmethod
    @overload
    def abs(value: System.IntPtr) -> System.IntPtr:
        """
        Returns the absolute value of a native signed integer.
        
        :param value: A number that is greater than IntPtr.MinValue, but less than or equal to IntPtr.MaxValue.
        :returns: A native signed integer, x, such that 0 \\u2264 x \\u2264 IntPtr.MaxValue.
        """
        ...

    @staticmethod
    @overload
    def abs(value: float) -> float:
        ...

    @staticmethod
    def acos(d: float) -> float:
        ...

    @staticmethod
    def acosh(d: float) -> float:
        ...

    @staticmethod
    def asin(d: float) -> float:
        ...

    @staticmethod
    def asinh(d: float) -> float:
        ...

    @staticmethod
    def atan(d: float) -> float:
        ...

    @staticmethod
    def atan_2(y: float, x: float) -> float:
        ...

    @staticmethod
    def atanh(d: float) -> float:
        ...

    @staticmethod
    @overload
    def big_mul(a: int, b: int) -> int:
        """
        Produces the full product of two unsigned 32-bit numbers.
        
        :param a: The first number to multiply.
        :param b: The second number to multiply.
        :returns: The number containing the product of the specified numbers.
        """
        ...

    @staticmethod
    @overload
    def big_mul(a: int, b: int, low: typing.Optional[int]) -> typing.Tuple[int, int]:
        """
        Produces the full product of two unsigned 64-bit numbers.
        
        :param a: The first number to multiply.
        :param b: The second number to multiply.
        :param low: The low 64-bit of the product of the specified numbers.
        :returns: The high 64-bit of the product of the specified numbers.
        """
        ...

    @staticmethod
    def bit_decrement(x: float) -> float:
        ...

    @staticmethod
    def bit_increment(x: float) -> float:
        ...

    @staticmethod
    def cbrt(d: float) -> float:
        ...

    @staticmethod
    @overload
    def ceiling(d: float) -> float:
        ...

    @staticmethod
    @overload
    def ceiling(a: float) -> float:
        ...

    @staticmethod
    @overload
    def clamp(value: int, min: int, max: int) -> int:
        ...

    @staticmethod
    @overload
    def clamp(value: float, min: float, max: float) -> float:
        ...

    @staticmethod
    @overload
    def clamp(value: System.IntPtr, min: System.IntPtr, max: System.IntPtr) -> System.IntPtr:
        """
        Returns  clamped to the inclusive range of  and .
        
        :param value: The value to be clamped.
        :param min: The lower bound of the result.
        :param max: The upper bound of the result.
        :returns: if  \\u2264  \\u2264 .    -or-     if  < .    -or-     if  < .
        """
        ...

    @staticmethod
    @overload
    def clamp(value: System.UIntPtr, min: System.UIntPtr, max: System.UIntPtr) -> System.UIntPtr:
        """
        Returns  clamped to the inclusive range of  and .
        
        :param value: The value to be clamped.
        :param min: The lower bound of the result.
        :param max: The upper bound of the result.
        :returns: if  \\u2264  \\u2264 .    -or-     if  < .    -or-     if  < .
        """
        ...

    @staticmethod
    def copy_sign(x: float, y: float) -> float:
        ...

    @staticmethod
    def cos(d: float) -> float:
        ...

    @staticmethod
    def cosh(value: float) -> float:
        ...

    @staticmethod
    @overload
    def div_rem(a: int, b: int, result: typing.Optional[int]) -> typing.Tuple[int, int]:
        ...

    @staticmethod
    @overload
    def div_rem(left: int, right: int) -> System.ValueTuple[int, int]:
        """
        Produces the quotient and the remainder of two signed 8-bit numbers.
        
        :param left: The dividend.
        :param right: The divisor.
        :returns: The quotient and the remainder of the specified numbers.
        """
        ...

    @staticmethod
    @overload
    def div_rem(left: System.IntPtr, right: System.IntPtr) -> System.ValueTuple[System.IntPtr, System.IntPtr]:
        """
        Produces the quotient and the remainder of two signed native-size numbers.
        
        :param left: The dividend.
        :param right: The divisor.
        :returns: The quotient and the remainder of the specified numbers.
        """
        ...

    @staticmethod
    @overload
    def div_rem(left: System.UIntPtr, right: System.UIntPtr) -> System.ValueTuple[System.UIntPtr, System.UIntPtr]:
        """
        Produces the quotient and the remainder of two unsigned native-size numbers.
        
        :param left: The dividend.
        :param right: The divisor.
        :returns: The quotient and the remainder of the specified numbers.
        """
        ...

    @staticmethod
    def exp(d: float) -> float:
        ...

    @staticmethod
    def floor(d: float) -> float:
        ...

    @staticmethod
    def fused_multiply_add(x: float, y: float, z: float) -> float:
        ...

    @staticmethod
    def ieee_remainder(x: float, y: float) -> float:
        ...

    @staticmethod
    def i_log_b(x: float) -> int:
        ...

    @staticmethod
    @overload
    def log(a: float, new_base: float) -> float:
        ...

    @staticmethod
    @overload
    def log(d: float) -> float:
        ...

    @staticmethod
    def log_10(d: float) -> float:
        ...

    @staticmethod
    def log_2(x: float) -> float:
        ...

    @staticmethod
    @overload
    def max(val_1: int, val_2: int) -> int:
        ...

    @staticmethod
    @overload
    def max(val_1: float, val_2: float) -> float:
        ...

    @staticmethod
    @overload
    def max(val_1: System.IntPtr, val_2: System.IntPtr) -> System.IntPtr:
        """
        Returns the larger of two native signed integers.
        
        :param val_1: The first of two native signed integers to compare.
        :param val_2: The second of two native signed integers to compare.
        :returns: Parameter  or , whichever is larger.
        """
        ...

    @staticmethod
    @overload
    def max(val_1: System.UIntPtr, val_2: System.UIntPtr) -> System.UIntPtr:
        """
        Returns the larger of two native unsigned integers.
        
        :param val_1: The first of two native unsigned integers to compare.
        :param val_2: The second of two native unsigned integers to compare.
        :returns: Parameter  or , whichever is larger.
        """
        ...

    @staticmethod
    def max_magnitude(x: float, y: float) -> float:
        ...

    @staticmethod
    @overload
    def min(val_1: int, val_2: int) -> int:
        ...

    @staticmethod
    @overload
    def min(val_1: float, val_2: float) -> float:
        ...

    @staticmethod
    @overload
    def min(val_1: System.IntPtr, val_2: System.IntPtr) -> System.IntPtr:
        """
        Returns the smaller of two native signed integers.
        
        :param val_1: The first of two native signed integers to compare.
        :param val_2: The second of two native signed integers to compare.
        :returns: Parameter  or , whichever is smaller.
        """
        ...

    @staticmethod
    @overload
    def min(val_1: System.UIntPtr, val_2: System.UIntPtr) -> System.UIntPtr:
        """
        Returns the smaller of two native unsigned integers.
        
        :param val_1: The first of two native unsigned integers to compare.
        :param val_2: The second of two native unsigned integers to compare.
        :returns: Parameter  or , whichever is smaller.
        """
        ...

    @staticmethod
    def min_magnitude(x: float, y: float) -> float:
        ...

    @staticmethod
    def pow(x: float, y: float) -> float:
        ...

    @staticmethod
    def reciprocal_estimate(d: float) -> float:
        """
        Returns an estimate of the reciprocal of a specified number.
        
        :param d: The number whose reciprocal is to be estimated.
        :returns: An estimate of the reciprocal of .
        """
        ...

    @staticmethod
    def reciprocal_sqrt_estimate(d: float) -> float:
        """
        Returns an estimate of the reciprocal square root of a specified number.
        
        :param d: The number whose reciprocal square root is to be estimated.
        :returns: An estimate of the reciprocal square root .
        """
        ...

    @staticmethod
    @overload
    def round(d: float) -> float:
        ...

    @staticmethod
    @overload
    def round(d: float, decimals: int) -> float:
        ...

    @staticmethod
    @overload
    def round(d: float, mode: System.MidpointRounding) -> float:
        ...

    @staticmethod
    @overload
    def round(d: float, decimals: int, mode: System.MidpointRounding) -> float:
        ...

    @staticmethod
    @overload
    def round(a: float) -> float:
        ...

    @staticmethod
    @overload
    def round(value: float, digits: int) -> float:
        ...

    @staticmethod
    @overload
    def round(value: float, mode: System.MidpointRounding) -> float:
        ...

    @staticmethod
    @overload
    def round(value: float, digits: int, mode: System.MidpointRounding) -> float:
        ...

    @staticmethod
    def scale_b(x: float, n: int) -> float:
        ...

    @staticmethod
    @overload
    def sign(value: float) -> int:
        ...

    @staticmethod
    @overload
    def sign(value: int) -> int:
        ...

    @staticmethod
    @overload
    def sign(value: System.IntPtr) -> int:
        ...

    @staticmethod
    def sin(a: float) -> float:
        ...

    @staticmethod
    def sin_cos(x: float) -> System.ValueTuple[float, float]:
        ...

    @staticmethod
    def sinh(value: float) -> float:
        ...

    @staticmethod
    def sqrt(d: float) -> float:
        ...

    @staticmethod
    def tan(a: float) -> float:
        ...

    @staticmethod
    def tanh(value: float) -> float:
        ...

    @staticmethod
    def truncate(d: float) -> float:
        ...


class Int16(System.IComparable[int], System.IConvertible, System.ISpanFormattable, System.IEquatable[int], System.Numerics.ISignedNumber[int], System.IUtf8SpanFormattable, System.IBinaryIntegerParseAndFormatInfo[int]):
    """This class has no documentation."""

    MAX_VALUE: int = ...

    MIN_VALUE: int = ...

    @overload
    def __ge__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __ge__(self, other: int) -> bool:
        ...

    @overload
    def __gt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __gt__(self, other: int) -> bool:
        ...

    @overload
    def __le__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __le__(self, other: int) -> bool:
        ...

    @overload
    def __lt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __lt__(self, other: int) -> bool:
        ...

    @staticmethod
    def abs(value: int) -> int:
        ...

    @staticmethod
    def clamp(value: int, min: int, max: int) -> int:
        ...

    @overload
    def compare_to(self, value: typing.Any) -> int:
        ...

    @overload
    def compare_to(self, value: int) -> int:
        ...

    @staticmethod
    def copy_sign(value: int, sign: int) -> int:
        ...

    @staticmethod
    def div_rem(left: int, right: int) -> System.ValueTuple[int, int]:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, obj: int) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def get_type_code(self) -> System.TypeCode:
        ...

    @staticmethod
    def is_even_integer(value: int) -> bool:
        ...

    @staticmethod
    def is_negative(value: int) -> bool:
        ...

    @staticmethod
    def is_odd_integer(value: int) -> bool:
        ...

    @staticmethod
    def is_positive(value: int) -> bool:
        ...

    @staticmethod
    def is_pow_2(value: int) -> bool:
        ...

    @staticmethod
    def leading_zero_count(value: int) -> int:
        ...

    @staticmethod
    def log_2(value: int) -> int:
        ...

    @staticmethod
    def max(x: int, y: int) -> int:
        ...

    @staticmethod
    def max_magnitude(x: int, y: int) -> int:
        ...

    @staticmethod
    def min(x: int, y: int) -> int:
        ...

    @staticmethod
    def min_magnitude(x: int, y: int) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: str) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: str, style: System.Globalization.NumberStyles) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: str, provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: str, style: System.Globalization.NumberStyles, provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int], style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> int:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int], provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    def pop_count(value: int) -> int:
        ...

    @staticmethod
    def rotate_left(value: int, rotate_amount: int) -> int:
        ...

    @staticmethod
    def rotate_right(value: int, rotate_amount: int) -> int:
        ...

    @staticmethod
    def sign(value: int) -> int:
        ...

    @overload
    def to_string(self) -> str:
        ...

    @overload
    def to_string(self, provider: System.IFormatProvider) -> str:
        ...

    @overload
    def to_string(self, format: str) -> str:
        ...

    @overload
    def to_string(self, format: str, provider: System.IFormatProvider) -> str:
        ...

    @staticmethod
    def trailing_zero_count(value: int) -> int:
        ...

    @overload
    def try_format(self, destination: System.Span[str], chars_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @overload
    def try_format(self, utf_8_destination: System.Span[int], bytes_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        """
        Tries to convert a UTF-8 character span containing the string representation of a number to its 16-bit signed integer equivalent.
        
        :param utf_8_text: A span containing the UTF-8 characters representing the number to convert.
        :param result: When this method returns, contains the 16-bit signed integer value equivalent to the number contained in  if the conversion succeeded, or zero if the conversion failed. This parameter is passed uninitialized; any value originally supplied in result will be overwritten.
        :returns: true if  was converted successfully; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def try_parse(s: str, style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...


class TypedReference:
    """This class has no documentation."""

    def equals(self, o: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    @staticmethod
    def get_target_type(value: System.TypedReference) -> typing.Type:
        ...

    @staticmethod
    def make_typed_reference(target: typing.Any, flds: typing.List[System.Reflection.FieldInfo]) -> System.TypedReference:
        ...

    @staticmethod
    def set_typed_reference(target: System.TypedReference, value: typing.Any) -> None:
        ...

    @staticmethod
    def target_type_token(value: System.TypedReference) -> System.RuntimeTypeHandle:
        ...

    @staticmethod
    def to_object(value: System.TypedReference) -> System.Object:
        ...


class ThreadStaticAttribute(System.Attribute):
    """Indicates that the value of a static field is unique for each thread."""

    def __init__(self) -> None:
        ...


class IComparable(typing.Generic[System_IComparable_T], metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @overload
    def compare_to(self, obj: typing.Any) -> int:
        """
        Compares the current instance with another object of the same type and returns an integer that indicates whether the current instance precedes, follows, or occurs in the same position in the sort order as the other object.
        
        :param obj: An object to compare with this instance.
        :returns: A value that indicates the relative order of the objects being compared. The return value has these meanings:ValueMeaningLess than zeroThis instance precedes  in the sort order.ZeroThis instance occurs in the same position in the sort order as .Greater than zeroThis instance follows  in the sort order.
        """
        ...

    @overload
    def compare_to(self, other: System_IComparable_T) -> int:
        """
        Compares the current instance with another object of the same type and returns an integer that indicates whether the current instance precedes, follows, or occurs in the same position in the sort order as the other object.
        
        :param other: An object to compare with this instance.
        :returns: A value that indicates the relative order of the objects being compared. The return value has these meanings:ValueMeaningLess than zeroThis instance precedes  in the sort order.ZeroThis instance occurs in the same position in the sort order as .Greater than zeroThis instance follows  in the sort order.
        """
        ...


class Byte(System.IComparable[int], System.IConvertible, System.ISpanFormattable, System.IEquatable[int], System.Numerics.IUnsignedNumber[int], System.IUtf8SpanFormattable, System.IUtfChar[int], System.IBinaryIntegerParseAndFormatInfo[int]):
    """This class has no documentation."""

    MAX_VALUE: int = ...

    MIN_VALUE: int = 0

    @overload
    def __ge__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __ge__(self, other: int) -> bool:
        ...

    @overload
    def __gt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __gt__(self, other: int) -> bool:
        ...

    @overload
    def __le__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __le__(self, other: int) -> bool:
        ...

    @overload
    def __lt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __lt__(self, other: int) -> bool:
        ...

    @staticmethod
    def clamp(value: int, min: int, max: int) -> int:
        ...

    @overload
    def compare_to(self, value: typing.Any) -> int:
        ...

    @overload
    def compare_to(self, value: int) -> int:
        ...

    @staticmethod
    def div_rem(left: int, right: int) -> System.ValueTuple[int, int]:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, obj: int) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def get_type_code(self) -> System.TypeCode:
        ...

    @staticmethod
    def is_even_integer(value: int) -> bool:
        ...

    @staticmethod
    def is_odd_integer(value: int) -> bool:
        ...

    @staticmethod
    def is_pow_2(value: int) -> bool:
        ...

    @staticmethod
    def leading_zero_count(value: int) -> int:
        ...

    @staticmethod
    def log_2(value: int) -> int:
        ...

    @staticmethod
    def max(x: int, y: int) -> int:
        ...

    @staticmethod
    def min(x: int, y: int) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: str) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: str, style: System.Globalization.NumberStyles) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: str, provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: str, style: System.Globalization.NumberStyles, provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int], style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> int:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int], provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    def pop_count(value: int) -> int:
        ...

    @staticmethod
    def rotate_left(value: int, rotate_amount: int) -> int:
        ...

    @staticmethod
    def rotate_right(value: int, rotate_amount: int) -> int:
        ...

    @staticmethod
    def sign(value: int) -> int:
        ...

    @overload
    def to_string(self) -> str:
        ...

    @overload
    def to_string(self, format: str) -> str:
        ...

    @overload
    def to_string(self, provider: System.IFormatProvider) -> str:
        ...

    @overload
    def to_string(self, format: str, provider: System.IFormatProvider) -> str:
        ...

    @staticmethod
    def trailing_zero_count(value: int) -> int:
        ...

    @overload
    def try_format(self, destination: System.Span[str], chars_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @overload
    def try_format(self, utf_8_destination: System.Span[int], bytes_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        """
        Tries to convert a UTF-8 character span containing the string representation of a number to its 8-bit unsigned integer equivalent.
        
        :param utf_8_text: A span containing the UTF-8 characters representing the number to convert.
        :param result: When this method returns, contains the 8-bit unsigned integer value equivalent to the number contained in  if the conversion succeeded, or zero if the conversion failed. This parameter is passed uninitialized; any value originally supplied in result will be overwritten.
        :returns: true if  was converted successfully; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def try_parse(s: str, style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...


class Int128(System.Numerics.ISignedNumber[System_Int128], System.IUtf8SpanFormattable, System.IBinaryIntegerParseAndFormatInfo[System_Int128]):
    """Represents a 128-bit signed integer."""

    MIN_VALUE: System.Int128

    MAX_VALUE: System.Int128

    ONE: System.Int128

    ZERO: System.Int128

    NEGATIVE_ONE: System.Int128

    @overload
    def __add__(self, right: System.Int128) -> System.Int128:
        ...

    @overload
    def __add__(self, right: System.Int128) -> System.Int128:
        ...

    @overload
    def __add__(self) -> System.Int128:
        ...

    def __and__(self, right: System.Int128) -> System.Int128:
        ...

    def __eq__(self, right: System.Int128) -> bool:
        ...

    def __ge__(self, right: System.Int128) -> bool:
        ...

    def __gt__(self, right: System.Int128) -> bool:
        ...

    @overload
    def __iadd__(self, right: System.Int128) -> System.Int128:
        ...

    @overload
    def __iadd__(self, right: System.Int128) -> System.Int128:
        ...

    @overload
    def __iadd__(self) -> System.Int128:
        ...

    def __iand__(self, right: System.Int128) -> System.Int128:
        ...

    def __ilshift__(self, shift_amount: int) -> System.Int128:
        ...

    def __imod__(self, right: System.Int128) -> System.Int128:
        ...

    @overload
    def __imul__(self, right: System.Int128) -> System.Int128:
        ...

    @overload
    def __imul__(self, right: System.Int128) -> System.Int128:
        ...

    def __init__(self, upper: int, lower: int) -> None:
        """
        Initializes a new instance of the Int128 struct.
        
        :param upper: The upper 64-bits of the 128-bit value.
        :param lower: The lower 64-bits of the 128-bit value.
        """
        ...

    def __invert__(self) -> System.Int128:
        ...

    def __ior__(self, right: System.Int128) -> System.Int128:
        ...

    def __irshift__(self, shift_amount: int) -> System.Int128:
        ...

    @overload
    def __isub__(self, right: System.Int128) -> System.Int128:
        ...

    @overload
    def __isub__(self, right: System.Int128) -> System.Int128:
        ...

    @overload
    def __isub__(self) -> System.Int128:
        ...

    @overload
    def __isub__(self) -> System.Int128:
        ...

    @overload
    def __itruediv__(self, right: System.Int128) -> System.Int128:
        ...

    @overload
    def __itruediv__(self, right: System.Int128) -> System.Int128:
        ...

    def __ixor__(self, right: System.Int128) -> System.Int128:
        ...

    def __le__(self, right: System.Int128) -> bool:
        ...

    def __lshift__(self, shift_amount: int) -> System.Int128:
        ...

    def __lt__(self, right: System.Int128) -> bool:
        ...

    def __mod__(self, right: System.Int128) -> System.Int128:
        ...

    @overload
    def __mul__(self, right: System.Int128) -> System.Int128:
        ...

    @overload
    def __mul__(self, right: System.Int128) -> System.Int128:
        ...

    def __ne__(self, right: System.Int128) -> bool:
        ...

    def __or__(self, right: System.Int128) -> System.Int128:
        ...

    def __rshift__(self, shift_amount: int) -> System.Int128:
        ...

    @overload
    def __sub__(self, right: System.Int128) -> System.Int128:
        ...

    @overload
    def __sub__(self, right: System.Int128) -> System.Int128:
        ...

    @overload
    def __sub__(self) -> System.Int128:
        ...

    @overload
    def __sub__(self) -> System.Int128:
        ...

    @overload
    def __truediv__(self, right: System.Int128) -> System.Int128:
        ...

    @overload
    def __truediv__(self, right: System.Int128) -> System.Int128:
        ...

    def __xor__(self, right: System.Int128) -> System.Int128:
        ...

    @staticmethod
    def abs(value: System.Int128) -> System.Int128:
        ...

    @staticmethod
    def clamp(value: System.Int128, min: System.Int128, max: System.Int128) -> System.Int128:
        ...

    @overload
    def compare_to(self, value: typing.Any) -> int:
        ...

    @overload
    def compare_to(self, value: System.Int128) -> int:
        ...

    @staticmethod
    def copy_sign(value: System.Int128, sign: System.Int128) -> System.Int128:
        ...

    @staticmethod
    def div_rem(left: System.Int128, right: System.Int128) -> System.ValueTuple[System.Int128, System.Int128]:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, other: System.Int128) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    @staticmethod
    def is_even_integer(value: System.Int128) -> bool:
        ...

    @staticmethod
    def is_negative(value: System.Int128) -> bool:
        ...

    @staticmethod
    def is_odd_integer(value: System.Int128) -> bool:
        ...

    @staticmethod
    def is_positive(value: System.Int128) -> bool:
        ...

    @staticmethod
    def is_pow_2(value: System.Int128) -> bool:
        ...

    @staticmethod
    def leading_zero_count(value: System.Int128) -> System.Int128:
        ...

    @staticmethod
    def log_2(value: System.Int128) -> System.Int128:
        ...

    @staticmethod
    def max(x: System.Int128, y: System.Int128) -> System.Int128:
        ...

    @staticmethod
    def max_magnitude(x: System.Int128, y: System.Int128) -> System.Int128:
        ...

    @staticmethod
    def min(x: System.Int128, y: System.Int128) -> System.Int128:
        ...

    @staticmethod
    def min_magnitude(x: System.Int128, y: System.Int128) -> System.Int128:
        ...

    @staticmethod
    @overload
    def parse(s: str) -> System.Int128:
        ...

    @staticmethod
    @overload
    def parse(s: str, style: System.Globalization.NumberStyles) -> System.Int128:
        ...

    @staticmethod
    @overload
    def parse(s: str, provider: System.IFormatProvider) -> System.Int128:
        ...

    @staticmethod
    @overload
    def parse(s: str, style: System.Globalization.NumberStyles, provider: System.IFormatProvider) -> System.Int128:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> System.Int128:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider) -> System.Int128:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int], style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> System.Int128:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int], provider: System.IFormatProvider) -> System.Int128:
        ...

    @staticmethod
    def pop_count(value: System.Int128) -> System.Int128:
        ...

    @staticmethod
    def rotate_left(value: System.Int128, rotate_amount: int) -> System.Int128:
        ...

    @staticmethod
    def rotate_right(value: System.Int128, rotate_amount: int) -> System.Int128:
        ...

    @staticmethod
    def sign(value: System.Int128) -> int:
        ...

    @overload
    def to_string(self) -> str:
        ...

    @overload
    def to_string(self, provider: System.IFormatProvider) -> str:
        ...

    @overload
    def to_string(self, format: str) -> str:
        ...

    @overload
    def to_string(self, format: str, provider: System.IFormatProvider) -> str:
        ...

    @staticmethod
    def trailing_zero_count(value: System.Int128) -> System.Int128:
        ...

    @overload
    def try_format(self, destination: System.Span[str], chars_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @overload
    def try_format(self, utf_8_destination: System.Span[int], bytes_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, result: typing.Optional[System.Int128]) -> typing.Tuple[bool, System.Int128]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], result: typing.Optional[System.Int128]) -> typing.Tuple[bool, System.Int128]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], result: typing.Optional[System.Int128]) -> typing.Tuple[bool, System.Int128]:
        """
        Tries to convert a UTF-8 character span containing the string representation of a number to its 128-bit signed integer equivalent.
        
        :param utf_8_text: A span containing the UTF-8 characters representing the number to convert.
        :param result: When this method returns, contains the 128-bit signed integer value equivalent to the number contained in  if the conversion succeeded, or zero if the conversion failed. This parameter is passed uninitialized; any value originally supplied in result will be overwritten.
        :returns: true if  was converted successfully; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def try_parse(s: str, style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[System.Int128]) -> typing.Tuple[bool, System.Int128]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[System.Int128]) -> typing.Tuple[bool, System.Int128]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, provider: System.IFormatProvider, result: typing.Optional[System.Int128]) -> typing.Tuple[bool, System.Int128]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider, result: typing.Optional[System.Int128]) -> typing.Tuple[bool, System.Int128]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[System.Int128]) -> typing.Tuple[bool, System.Int128]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], provider: System.IFormatProvider, result: typing.Optional[System.Int128]) -> typing.Tuple[bool, System.Int128]:
        ...


class Int64(System.IComparable[int], System.IConvertible, System.ISpanFormattable, System.IEquatable[int], System.Numerics.ISignedNumber[int], System.IUtf8SpanFormattable, System.IBinaryIntegerParseAndFormatInfo[int]):
    """This class has no documentation."""

    MAX_VALUE: int = ...

    MIN_VALUE: int = ...

    @overload
    def __ge__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __ge__(self, other: int) -> bool:
        ...

    @overload
    def __gt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __gt__(self, other: int) -> bool:
        ...

    @overload
    def __le__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __le__(self, other: int) -> bool:
        ...

    @overload
    def __lt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __lt__(self, other: int) -> bool:
        ...

    @staticmethod
    def abs(value: int) -> int:
        ...

    @staticmethod
    def big_mul(left: int, right: int) -> System.Int128:
        """
        Produces the full product of two 64-bit numbers.
        
        :param left: The first number to multiply.
        :param right: The second number to multiply.
        :returns: The number containing the product of the specified numbers.
        """
        ...

    @staticmethod
    def clamp(value: int, min: int, max: int) -> int:
        ...

    @overload
    def compare_to(self, value: typing.Any) -> int:
        ...

    @overload
    def compare_to(self, value: int) -> int:
        ...

    @staticmethod
    def copy_sign(value: int, sign: int) -> int:
        ...

    @staticmethod
    def div_rem(left: int, right: int) -> System.ValueTuple[int, int]:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, obj: int) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def get_type_code(self) -> System.TypeCode:
        ...

    @staticmethod
    def is_even_integer(value: int) -> bool:
        ...

    @staticmethod
    def is_negative(value: int) -> bool:
        ...

    @staticmethod
    def is_odd_integer(value: int) -> bool:
        ...

    @staticmethod
    def is_positive(value: int) -> bool:
        ...

    @staticmethod
    def is_pow_2(value: int) -> bool:
        ...

    @staticmethod
    def leading_zero_count(value: int) -> int:
        ...

    @staticmethod
    def log_2(value: int) -> int:
        ...

    @staticmethod
    def max(x: int, y: int) -> int:
        ...

    @staticmethod
    def max_magnitude(x: int, y: int) -> int:
        ...

    @staticmethod
    def min(x: int, y: int) -> int:
        ...

    @staticmethod
    def min_magnitude(x: int, y: int) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: str) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: str, style: System.Globalization.NumberStyles) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: str, provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: str, style: System.Globalization.NumberStyles, provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int], style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> int:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int], provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    def pop_count(value: int) -> int:
        ...

    @staticmethod
    def rotate_left(value: int, rotate_amount: int) -> int:
        ...

    @staticmethod
    def rotate_right(value: int, rotate_amount: int) -> int:
        ...

    @staticmethod
    def sign(value: int) -> int:
        ...

    @overload
    def to_string(self) -> str:
        ...

    @overload
    def to_string(self, provider: System.IFormatProvider) -> str:
        ...

    @overload
    def to_string(self, format: str) -> str:
        ...

    @overload
    def to_string(self, format: str, provider: System.IFormatProvider) -> str:
        ...

    @staticmethod
    def trailing_zero_count(value: int) -> int:
        ...

    @overload
    def try_format(self, destination: System.Span[str], chars_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @overload
    def try_format(self, utf_8_destination: System.Span[int], bytes_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        """
        Tries to convert a UTF-8 character span containing the string representation of a number to its 64-bit signed integer equivalent.
        
        :param utf_8_text: A span containing the UTF-8 characters representing the number to convert.
        :param result: When this method returns, contains the 64-bit signed integer value equivalent to the number contained in  if the conversion succeeded, or zero if the conversion failed. This parameter is passed uninitialized; any value originally supplied in result will be overwritten.
        :returns: true if  was converted successfully; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def try_parse(s: str, style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...


class WeakReference(typing.Generic[System_WeakReference_T], System.Object, System.Runtime.Serialization.ISerializable):
    """This class has no documentation."""

    @property
    def track_resurrection(self) -> bool:
        ...

    @property
    def is_alive(self) -> bool:
        ...

    @property
    def target(self) -> System.Object:
        ...

    @target.setter
    def target(self, value: System.Object) -> None:
        ...

    @overload
    def __init__(self, target: typing.Any) -> None:
        ...

    @overload
    def __init__(self, target: typing.Any, track_resurrection: bool) -> None:
        ...

    @overload
    def __init__(self, target: System_WeakReference_T) -> None:
        ...

    @overload
    def __init__(self, target: System_WeakReference_T, track_resurrection: bool) -> None:
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

    def set_target(self, target: System_WeakReference_T) -> None:
        ...

    def try_get_target(self, target: typing.Optional[System_WeakReference_T]) -> typing.Tuple[bool, System_WeakReference_T]:
        ...


class MissingMethodException(System.MissingMemberException):
    """The exception that is thrown when there is an attempt to dynamically access a method that does not exist."""

    @property
    def message(self) -> str:
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
    def __init__(self, class_name: str, method_name: str) -> None:
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """
        This method is protected.
        
        Obsoletions.LegacyFormatterImplMessage
        """
        ...


class IEquatable(typing.Generic[System_IEquatable_T], metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def equals(self, other: System_IEquatable_T) -> bool:
        """
        Indicates whether the current object is equal to another object of the same type.
        
        :param other: An object to compare with this object.
        :returns: true if the current object is equal to the  parameter; otherwise, false.
        """
        ...


class Type(System.Reflection.MemberInfo, System.Reflection.IReflect, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    def is_serializable(self) -> bool:
        """Obsoletions.LegacyFormatterMessage"""
        warnings.warn("Obsoletions.LegacyFormatterMessage", DeprecationWarning)

    @property
    def contains_generic_parameters(self) -> bool:
        ...

    @property
    def is_visible(self) -> bool:
        ...

    @property
    def member_type(self) -> System.Reflection.MemberTypes:
        ...

    @property
    @abc.abstractmethod
    def namespace(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def assembly_qualified_name(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def full_name(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def assembly(self) -> System.Reflection.Assembly:
        ...

    @property
    @abc.abstractmethod
    def module(self) -> System.Reflection.Module:
        ...

    @property
    def is_interface(self) -> bool:
        ...

    @property
    def is_nested(self) -> bool:
        ...

    @property
    def declaring_type(self) -> typing.Type:
        ...

    @property
    def declaring_method(self) -> System.Reflection.MethodBase:
        ...

    @property
    def reflected_type(self) -> typing.Type:
        ...

    @property
    @abc.abstractmethod
    def underlying_system_type(self) -> typing.Type:
        ...

    @property
    def is_type_definition(self) -> bool:
        ...

    @property
    def is_array(self) -> bool:
        ...

    @property
    def is_by_ref(self) -> bool:
        ...

    @property
    def is_pointer(self) -> bool:
        ...

    @property
    def is_constructed_generic_type(self) -> bool:
        ...

    @property
    def is_generic_parameter(self) -> bool:
        ...

    @property
    def is_generic_type_parameter(self) -> bool:
        ...

    @property
    def is_generic_method_parameter(self) -> bool:
        ...

    @property
    def is_generic_type(self) -> bool:
        ...

    @property
    def is_generic_type_definition(self) -> bool:
        ...

    @property
    def is_sz_array(self) -> bool:
        ...

    @property
    def is_variable_bound_array(self) -> bool:
        ...

    @property
    def is_by_ref_like(self) -> bool:
        ...

    @property
    def is_function_pointer(self) -> bool:
        ...

    @property
    def is_unmanaged_function_pointer(self) -> bool:
        ...

    @property
    def has_element_type(self) -> bool:
        ...

    @property
    def generic_type_arguments(self) -> typing.List[typing.Type]:
        ...

    @property
    def generic_parameter_position(self) -> int:
        ...

    @property
    def generic_parameter_attributes(self) -> System.Reflection.GenericParameterAttributes:
        ...

    @property
    def attributes(self) -> System.Reflection.TypeAttributes:
        ...

    @property
    def is_abstract(self) -> bool:
        ...

    @property
    def is_import(self) -> bool:
        ...

    @property
    def is_sealed(self) -> bool:
        ...

    @property
    def is_special_name(self) -> bool:
        ...

    @property
    def is_class(self) -> bool:
        ...

    @property
    def is_nested_assembly(self) -> bool:
        ...

    @property
    def is_nested_fam_and_assem(self) -> bool:
        ...

    @property
    def is_nested_family(self) -> bool:
        ...

    @property
    def is_nested_fam_or_assem(self) -> bool:
        ...

    @property
    def is_nested_private(self) -> bool:
        ...

    @property
    def is_nested_public(self) -> bool:
        ...

    @property
    def is_not_public(self) -> bool:
        ...

    @property
    def is_public(self) -> bool:
        ...

    @property
    def is_auto_layout(self) -> bool:
        ...

    @property
    def is_explicit_layout(self) -> bool:
        ...

    @property
    def is_layout_sequential(self) -> bool:
        ...

    @property
    def is_ansi_class(self) -> bool:
        ...

    @property
    def is_auto_class(self) -> bool:
        ...

    @property
    def is_unicode_class(self) -> bool:
        ...

    @property
    def is_com_object(self) -> bool:
        ...

    @property
    def is_contextful(self) -> bool:
        ...

    @property
    def is_enum(self) -> bool:
        ...

    @property
    def is_marshal_by_ref(self) -> bool:
        ...

    @property
    def is_primitive(self) -> bool:
        ...

    @property
    def is_value_type(self) -> bool:
        ...

    @property
    def is_signature_type(self) -> bool:
        ...

    @property
    def is_security_critical(self) -> bool:
        ...

    @property
    def is_security_safe_critical(self) -> bool:
        ...

    @property
    def is_security_transparent(self) -> bool:
        ...

    @property
    def struct_layout_attribute(self) -> System.Runtime.InteropServices.StructLayoutAttribute:
        ...

    @property
    def type_initializer(self) -> System.Reflection.ConstructorInfo:
        ...

    @property
    def type_handle(self) -> System.RuntimeTypeHandle:
        ...

    @property
    @abc.abstractmethod
    def guid(self) -> System.Guid:
        ...

    @property
    @abc.abstractmethod
    def base_type(self) -> typing.Type:
        ...

    DEFAULT_BINDER: System.Reflection.Binder

    DELIMITER: str = ...

    EMPTY_TYPES: typing.List[typing.Type] = ...

    MISSING: System.Object = ...

    FILTER_ATTRIBUTE: typing.Callable[[System.Reflection.MemberInfo, System.Object], bool] = ...

    FILTER_NAME: typing.Callable[[System.Reflection.MemberInfo, System.Object], bool] = ...

    FILTER_NAME_IGNORE_CASE: typing.Callable[[System.Reflection.MemberInfo, System.Object], bool] = ...

    def __eq__(self, right: typing.Type) -> bool:
        ...

    def __init__(self) -> None:
        """This method is protected."""
        ...

    def __ne__(self, right: typing.Type) -> bool:
        ...

    @overload
    def equals(self, o: typing.Any) -> bool:
        ...

    @overload
    def equals(self, o: typing.Type) -> bool:
        ...

    def find_interfaces(self, filter: typing.Callable[[typing.Type, System.Object], bool], filter_criteria: typing.Any) -> typing.List[typing.Type]:
        ...

    def find_members(self, member_type: System.Reflection.MemberTypes, binding_attr: System.Reflection.BindingFlags, filter: typing.Callable[[System.Reflection.MemberInfo, System.Object], bool], filter_criteria: typing.Any) -> typing.List[System.Reflection.MemberInfo]:
        ...

    def get_array_rank(self) -> int:
        ...

    def get_attribute_flags_impl(self) -> System.Reflection.TypeAttributes:
        """This method is protected."""
        ...

    @overload
    def get_constructor(self, types: typing.List[typing.Type]) -> System.Reflection.ConstructorInfo:
        ...

    @overload
    def get_constructor(self, binding_attr: System.Reflection.BindingFlags, types: typing.List[typing.Type]) -> System.Reflection.ConstructorInfo:
        """
        Searches for a constructor whose parameters match the specified argument types, using the specified binding constraints.
        
        :param binding_attr: A bitwise combination of the enumeration values that specify how the search is conducted. -or- Default to return null.
        :param types: An array of Type objects representing the number, order, and type of the parameters for the constructor to get. -or- An empty array of the type Type (that is, Type[] types = Array.Empty{Type}()) to get a constructor that takes no parameters. -or- EmptyTypes.
        :returns: A ConstructorInfo object representing the constructor that matches the specified requirements, if found; otherwise, null.
        """
        ...

    @overload
    def get_constructor(self, binding_attr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, types: typing.List[typing.Type], modifiers: typing.List[System.Reflection.ParameterModifier]) -> System.Reflection.ConstructorInfo:
        ...

    @overload
    def get_constructor(self, binding_attr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, call_convention: System.Reflection.CallingConventions, types: typing.List[typing.Type], modifiers: typing.List[System.Reflection.ParameterModifier]) -> System.Reflection.ConstructorInfo:
        ...

    def get_constructor_impl(self, binding_attr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, call_convention: System.Reflection.CallingConventions, types: typing.List[typing.Type], modifiers: typing.List[System.Reflection.ParameterModifier]) -> System.Reflection.ConstructorInfo:
        """This method is protected."""
        ...

    @overload
    def get_constructors(self) -> typing.List[System.Reflection.ConstructorInfo]:
        ...

    @overload
    def get_constructors(self, binding_attr: System.Reflection.BindingFlags) -> typing.List[System.Reflection.ConstructorInfo]:
        ...

    def get_default_members(self) -> typing.List[System.Reflection.MemberInfo]:
        ...

    def get_element_type(self) -> typing.Type:
        ...

    def get_enum_name(self, value: typing.Any) -> str:
        ...

    def get_enum_names(self) -> typing.List[str]:
        ...

    def get_enum_underlying_type(self) -> typing.Type:
        ...

    def get_enum_values(self) -> System.Array:
        ...

    def get_enum_values_as_underlying_type(self) -> System.Array:
        """
        Retrieves an array of the values of the underlying type constants of this enumeration type.
        
        :returns: An array that contains the values of the underlying type constants in this enumeration type.
        """
        ...

    @overload
    def get_event(self, name: str) -> System.Reflection.EventInfo:
        ...

    @overload
    def get_event(self, name: str, binding_attr: System.Reflection.BindingFlags) -> System.Reflection.EventInfo:
        ...

    @overload
    def get_events(self) -> typing.List[System.Reflection.EventInfo]:
        ...

    @overload
    def get_events(self, binding_attr: System.Reflection.BindingFlags) -> typing.List[System.Reflection.EventInfo]:
        ...

    @overload
    def get_field(self, name: str) -> System.Reflection.FieldInfo:
        ...

    @overload
    def get_field(self, name: str, binding_attr: System.Reflection.BindingFlags) -> System.Reflection.FieldInfo:
        ...

    @overload
    def get_fields(self) -> typing.List[System.Reflection.FieldInfo]:
        ...

    @overload
    def get_fields(self, binding_attr: System.Reflection.BindingFlags) -> typing.List[System.Reflection.FieldInfo]:
        ...

    def get_function_pointer_calling_conventions(self) -> typing.List[typing.Type]:
        ...

    def get_function_pointer_parameter_types(self) -> typing.List[typing.Type]:
        ...

    def get_function_pointer_return_type(self) -> typing.Type:
        ...

    def get_generic_arguments(self) -> typing.List[typing.Type]:
        ...

    def get_generic_parameter_constraints(self) -> typing.List[typing.Type]:
        ...

    def get_generic_type_definition(self) -> typing.Type:
        ...

    def get_hash_code(self) -> int:
        ...

    @overload
    def get_interface(self, name: str) -> typing.Type:
        ...

    @overload
    def get_interface(self, name: str, ignore_case: bool) -> typing.Type:
        ...

    def get_interface_map(self, interface_type: typing.Type) -> System.Reflection.InterfaceMapping:
        ...

    def get_interfaces(self) -> typing.List[typing.Type]:
        ...

    @overload
    def get_member(self, name: str) -> typing.List[System.Reflection.MemberInfo]:
        ...

    @overload
    def get_member(self, name: str, binding_attr: System.Reflection.BindingFlags) -> typing.List[System.Reflection.MemberInfo]:
        ...

    @overload
    def get_member(self, name: str, type: System.Reflection.MemberTypes, binding_attr: System.Reflection.BindingFlags) -> typing.List[System.Reflection.MemberInfo]:
        ...

    @overload
    def get_members(self) -> typing.List[System.Reflection.MemberInfo]:
        ...

    @overload
    def get_members(self, binding_attr: System.Reflection.BindingFlags) -> typing.List[System.Reflection.MemberInfo]:
        ...

    def get_member_with_same_metadata_definition_as(self, member: System.Reflection.MemberInfo) -> System.Reflection.MemberInfo:
        """
        Searches for the MemberInfo on the current Type that matches the specified MemberInfo.
        
        :param member: The MemberInfo to find on the current Type.
        :returns: An object representing the member on the current Type that matches the specified member.
        """
        ...

    @overload
    def get_method(self, name: str) -> System.Reflection.MethodInfo:
        ...

    @overload
    def get_method(self, name: str, binding_attr: System.Reflection.BindingFlags) -> System.Reflection.MethodInfo:
        ...

    @overload
    def get_method(self, name: str, binding_attr: System.Reflection.BindingFlags, types: typing.List[typing.Type]) -> System.Reflection.MethodInfo:
        """
        Searches for the specified method whose parameters match the specified argument types, using the specified binding constraints.
        
        :param name: The string containing the name of the method to get.
        :param binding_attr: A bitwise combination of the enumeration values that specify how the search is conducted. -or- Default to return null.
        :param types: An array of Type objects representing the number, order, and type of the parameters for the method to get. -or- An empty array of Type objects (as provided by the EmptyTypes field) to get a method that takes no parameters.
        :returns: An object representing the method that matches the specified requirements, if found; otherwise, null.
        """
        ...

    @overload
    def get_method(self, name: str, types: typing.List[typing.Type]) -> System.Reflection.MethodInfo:
        ...

    @overload
    def get_method(self, name: str, types: typing.List[typing.Type], modifiers: typing.List[System.Reflection.ParameterModifier]) -> System.Reflection.MethodInfo:
        ...

    @overload
    def get_method(self, name: str, binding_attr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, types: typing.List[typing.Type], modifiers: typing.List[System.Reflection.ParameterModifier]) -> System.Reflection.MethodInfo:
        ...

    @overload
    def get_method(self, name: str, binding_attr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, call_convention: System.Reflection.CallingConventions, types: typing.List[typing.Type], modifiers: typing.List[System.Reflection.ParameterModifier]) -> System.Reflection.MethodInfo:
        ...

    @overload
    def get_method(self, name: str, generic_parameter_count: int, types: typing.List[typing.Type]) -> System.Reflection.MethodInfo:
        ...

    @overload
    def get_method(self, name: str, generic_parameter_count: int, types: typing.List[typing.Type], modifiers: typing.List[System.Reflection.ParameterModifier]) -> System.Reflection.MethodInfo:
        ...

    @overload
    def get_method(self, name: str, generic_parameter_count: int, binding_attr: System.Reflection.BindingFlags, types: typing.List[typing.Type]) -> System.Reflection.MethodInfo:
        """
        Searches for the specified method whose parameters match the specified generic parameter count and argument types, using the specified binding constraints.
        
        :param name: The string containing the name of the method to get.
        :param generic_parameter_count: The number of generic type parameters of the method.
        :param binding_attr: A bitwise combination of the enumeration values that specify how the search is conducted. -or- Default to return null.
        :param types: An array of Type objects representing the number, order, and type of the parameters for the method to get. -or- An empty array of Type objects (as provided by the EmptyTypes field) to get a method that takes no parameters.
        :returns: An object representing the method that matches the specified generic parameter count, argument types, and binding constraints, if found; otherwise, null.
        """
        ...

    @overload
    def get_method(self, name: str, generic_parameter_count: int, binding_attr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, types: typing.List[typing.Type], modifiers: typing.List[System.Reflection.ParameterModifier]) -> System.Reflection.MethodInfo:
        ...

    @overload
    def get_method(self, name: str, generic_parameter_count: int, binding_attr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, call_convention: System.Reflection.CallingConventions, types: typing.List[typing.Type], modifiers: typing.List[System.Reflection.ParameterModifier]) -> System.Reflection.MethodInfo:
        ...

    @overload
    def get_method_impl(self, name: str, binding_attr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, call_convention: System.Reflection.CallingConventions, types: typing.List[typing.Type], modifiers: typing.List[System.Reflection.ParameterModifier]) -> System.Reflection.MethodInfo:
        """This method is protected."""
        ...

    @overload
    def get_method_impl(self, name: str, generic_parameter_count: int, binding_attr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, call_convention: System.Reflection.CallingConventions, types: typing.List[typing.Type], modifiers: typing.List[System.Reflection.ParameterModifier]) -> System.Reflection.MethodInfo:
        """This method is protected."""
        ...

    @overload
    def get_methods(self) -> typing.List[System.Reflection.MethodInfo]:
        ...

    @overload
    def get_methods(self, binding_attr: System.Reflection.BindingFlags) -> typing.List[System.Reflection.MethodInfo]:
        ...

    @overload
    def get_nested_type(self, name: str) -> typing.Type:
        ...

    @overload
    def get_nested_type(self, name: str, binding_attr: System.Reflection.BindingFlags) -> typing.Type:
        ...

    @overload
    def get_nested_types(self) -> typing.List[typing.Type]:
        ...

    @overload
    def get_nested_types(self, binding_attr: System.Reflection.BindingFlags) -> typing.List[typing.Type]:
        ...

    def get_optional_custom_modifiers(self) -> typing.List[typing.Type]:
        ...

    @overload
    def get_properties(self) -> typing.List[System.Reflection.PropertyInfo]:
        ...

    @overload
    def get_properties(self, binding_attr: System.Reflection.BindingFlags) -> typing.List[System.Reflection.PropertyInfo]:
        ...

    @overload
    def get_property(self, name: str) -> System.Reflection.PropertyInfo:
        ...

    @overload
    def get_property(self, name: str, binding_attr: System.Reflection.BindingFlags) -> System.Reflection.PropertyInfo:
        ...

    @overload
    def get_property(self, name: str, return_type: typing.Type) -> System.Reflection.PropertyInfo:
        ...

    @overload
    def get_property(self, name: str, types: typing.List[typing.Type]) -> System.Reflection.PropertyInfo:
        ...

    @overload
    def get_property(self, name: str, return_type: typing.Type, types: typing.List[typing.Type]) -> System.Reflection.PropertyInfo:
        ...

    @overload
    def get_property(self, name: str, return_type: typing.Type, types: typing.List[typing.Type], modifiers: typing.List[System.Reflection.ParameterModifier]) -> System.Reflection.PropertyInfo:
        ...

    @overload
    def get_property(self, name: str, binding_attr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, return_type: typing.Type, types: typing.List[typing.Type], modifiers: typing.List[System.Reflection.ParameterModifier]) -> System.Reflection.PropertyInfo:
        ...

    def get_property_impl(self, name: str, binding_attr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, return_type: typing.Type, types: typing.List[typing.Type], modifiers: typing.List[System.Reflection.ParameterModifier]) -> System.Reflection.PropertyInfo:
        """This method is protected."""
        ...

    def get_required_custom_modifiers(self) -> typing.List[typing.Type]:
        ...

    @overload
    def get_type(self) -> typing.Type:
        ...

    @staticmethod
    @overload
    def get_type(type_name: str, throw_on_error: bool, ignore_case: bool) -> typing.Type:
        ...

    @staticmethod
    @overload
    def get_type(type_name: str, throw_on_error: bool) -> typing.Type:
        ...

    @staticmethod
    @overload
    def get_type(type_name: str) -> typing.Type:
        ...

    @staticmethod
    @overload
    def get_type(type_name: str, assembly_resolver: typing.Callable[[System.Reflection.AssemblyName], System.Reflection.Assembly], type_resolver: typing.Callable[[System.Reflection.Assembly, str, bool], typing.Type]) -> typing.Type:
        ...

    @staticmethod
    @overload
    def get_type(type_name: str, assembly_resolver: typing.Callable[[System.Reflection.AssemblyName], System.Reflection.Assembly], type_resolver: typing.Callable[[System.Reflection.Assembly, str, bool], typing.Type], throw_on_error: bool) -> typing.Type:
        ...

    @staticmethod
    @overload
    def get_type(type_name: str, assembly_resolver: typing.Callable[[System.Reflection.AssemblyName], System.Reflection.Assembly], type_resolver: typing.Callable[[System.Reflection.Assembly, str, bool], typing.Type], throw_on_error: bool, ignore_case: bool) -> typing.Type:
        ...

    @staticmethod
    def get_type_array(args: typing.List[System.Object]) -> typing.List[typing.Type]:
        ...

    @staticmethod
    def get_type_code(type: typing.Type) -> System.TypeCode:
        ...

    def get_type_code_impl(self) -> System.TypeCode:
        """This method is protected."""
        ...

    @staticmethod
    @overload
    def get_type_from_clsid(clsid: System.Guid) -> typing.Type:
        ...

    @staticmethod
    @overload
    def get_type_from_clsid(clsid: System.Guid, throw_on_error: bool) -> typing.Type:
        ...

    @staticmethod
    @overload
    def get_type_from_clsid(clsid: System.Guid, server: str) -> typing.Type:
        ...

    @staticmethod
    @overload
    def get_type_from_clsid(clsid: System.Guid, server: str, throw_on_error: bool) -> typing.Type:
        ...

    @staticmethod
    def get_type_from_handle(handle: System.RuntimeTypeHandle) -> typing.Type:
        ...

    @staticmethod
    @overload
    def get_type_from_prog_id(prog_id: str) -> typing.Type:
        ...

    @staticmethod
    @overload
    def get_type_from_prog_id(prog_id: str, throw_on_error: bool) -> typing.Type:
        ...

    @staticmethod
    @overload
    def get_type_from_prog_id(prog_id: str, server: str) -> typing.Type:
        ...

    @staticmethod
    @overload
    def get_type_from_prog_id(prog_id: str, server: str, throw_on_error: bool) -> typing.Type:
        ...

    @staticmethod
    def get_type_handle(o: typing.Any) -> System.RuntimeTypeHandle:
        ...

    def has_element_type_impl(self) -> bool:
        """This method is protected."""
        ...

    @overload
    def invoke_member(self, name: str, invoke_attr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, target: typing.Any, args: typing.List[System.Object]) -> System.Object:
        ...

    @overload
    def invoke_member(self, name: str, invoke_attr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, target: typing.Any, args: typing.List[System.Object], culture: System.Globalization.CultureInfo) -> System.Object:
        ...

    @overload
    def invoke_member(self, name: str, invoke_attr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, target: typing.Any, args: typing.List[System.Object], modifiers: typing.List[System.Reflection.ParameterModifier], culture: System.Globalization.CultureInfo, named_parameters: typing.List[str]) -> System.Object:
        ...

    def is_array_impl(self) -> bool:
        """This method is protected."""
        ...

    def is_assignable_from(self, c: typing.Type) -> bool:
        ...

    def is_assignable_to(self, target_type: typing.Type) -> bool:
        ...

    def is_by_ref_impl(self) -> bool:
        """This method is protected."""
        ...

    def is_com_object_impl(self) -> bool:
        """This method is protected."""
        ...

    def is_contextful_impl(self) -> bool:
        """This method is protected."""
        ...

    def is_enum_defined(self, value: typing.Any) -> bool:
        ...

    def is_equivalent_to(self, other: typing.Type) -> bool:
        ...

    def is_instance_of_type(self, o: typing.Any) -> bool:
        ...

    def is_marshal_by_ref_impl(self) -> bool:
        """This method is protected."""
        ...

    def is_pointer_impl(self) -> bool:
        """This method is protected."""
        ...

    def is_primitive_impl(self) -> bool:
        """This method is protected."""
        ...

    def is_subclass_of(self, c: typing.Type) -> bool:
        ...

    def is_value_type_impl(self) -> bool:
        """This method is protected."""
        ...

    @overload
    def make_array_type(self) -> typing.Type:
        ...

    @overload
    def make_array_type(self, rank: int) -> typing.Type:
        ...

    def make_by_ref_type(self) -> typing.Type:
        ...

    @staticmethod
    def make_generic_method_parameter(position: int) -> typing.Type:
        ...

    @staticmethod
    def make_generic_signature_type(generic_type_definition: typing.Type, *type_arguments: typing.Union[typing.Type, typing.Iterable[typing.Type]]) -> typing.Type:
        ...

    def make_generic_type(self, *type_arguments: typing.Union[typing.Type, typing.Iterable[typing.Type]]) -> typing.Type:
        ...

    def make_pointer_type(self) -> typing.Type:
        ...

    @staticmethod
    def reflection_only_get_type(type_name: str, throw_if_not_found: bool, ignore_case: bool) -> typing.Type:
        """Obsoletions.ReflectionOnlyLoadingMessage"""
        warnings.warn("Obsoletions.ReflectionOnlyLoadingMessage", DeprecationWarning)

    def to_string(self) -> str:
        ...


class TimeZone(System.Object, metaclass=abc.ABCMeta):
    """
    Represents a time zone.
    
    System.TimeZone has been deprecated. Investigate the use of System.TimeZoneInfo instead.
    """

    CURRENT_TIME_ZONE: System.TimeZone

    @property
    @abc.abstractmethod
    def standard_name(self) -> str:
        ...

    @property
    @abc.abstractmethod
    def daylight_name(self) -> str:
        ...

    def __init__(self) -> None:
        """This method is protected."""
        ...

    def get_daylight_changes(self, year: int) -> System.Globalization.DaylightTime:
        ...

    def get_utc_offset(self, time: typing.Union[datetime.datetime, datetime.date]) -> datetime.timedelta:
        ...

    @overload
    def is_daylight_saving_time(self, time: typing.Union[datetime.datetime, datetime.date]) -> bool:
        ...

    @staticmethod
    @overload
    def is_daylight_saving_time(time: typing.Union[datetime.datetime, datetime.date], daylight_times: System.Globalization.DaylightTime) -> bool:
        ...

    def to_local_time(self, time: typing.Union[datetime.datetime, datetime.date]) -> datetime.datetime:
        ...

    def to_universal_time(self, time: typing.Union[datetime.datetime, datetime.date]) -> datetime.datetime:
        ...


class UInt128(System.Numerics.IUnsignedNumber[System_UInt128], System.IUtf8SpanFormattable, System.IBinaryIntegerParseAndFormatInfo[System_UInt128]):
    """Represents a 128-bit unsigned integer."""

    MIN_VALUE: System.UInt128

    MAX_VALUE: System.UInt128

    ONE: System.UInt128

    ZERO: System.UInt128

    @overload
    def __add__(self, right: System.UInt128) -> System.UInt128:
        ...

    @overload
    def __add__(self, right: System.UInt128) -> System.UInt128:
        ...

    @overload
    def __add__(self) -> System.UInt128:
        ...

    def __and__(self, right: System.UInt128) -> System.UInt128:
        ...

    def __eq__(self, right: System.UInt128) -> bool:
        ...

    def __ge__(self, right: System.UInt128) -> bool:
        ...

    def __gt__(self, right: System.UInt128) -> bool:
        ...

    @overload
    def __iadd__(self, right: System.UInt128) -> System.UInt128:
        ...

    @overload
    def __iadd__(self, right: System.UInt128) -> System.UInt128:
        ...

    @overload
    def __iadd__(self) -> System.UInt128:
        ...

    def __iand__(self, right: System.UInt128) -> System.UInt128:
        ...

    def __ilshift__(self, shift_amount: int) -> System.UInt128:
        ...

    def __imod__(self, right: System.UInt128) -> System.UInt128:
        ...

    @overload
    def __imul__(self, right: System.UInt128) -> System.UInt128:
        ...

    @overload
    def __imul__(self, right: System.UInt128) -> System.UInt128:
        ...

    def __init__(self, upper: int, lower: int) -> None:
        """
        Initializes a new instance of the UInt128 struct.
        
        :param upper: The upper 64-bits of the 128-bit value.
        :param lower: The lower 64-bits of the 128-bit value.
        """
        ...

    def __invert__(self) -> System.UInt128:
        ...

    def __ior__(self, right: System.UInt128) -> System.UInt128:
        ...

    def __irshift__(self, shift_amount: int) -> System.UInt128:
        ...

    @overload
    def __isub__(self, right: System.UInt128) -> System.UInt128:
        ...

    @overload
    def __isub__(self, right: System.UInt128) -> System.UInt128:
        ...

    @overload
    def __isub__(self) -> System.UInt128:
        ...

    @overload
    def __isub__(self) -> System.UInt128:
        ...

    @overload
    def __itruediv__(self, right: System.UInt128) -> System.UInt128:
        ...

    @overload
    def __itruediv__(self, right: System.UInt128) -> System.UInt128:
        ...

    def __ixor__(self, right: System.UInt128) -> System.UInt128:
        ...

    def __le__(self, right: System.UInt128) -> bool:
        ...

    def __lshift__(self, shift_amount: int) -> System.UInt128:
        ...

    def __lt__(self, right: System.UInt128) -> bool:
        ...

    def __mod__(self, right: System.UInt128) -> System.UInt128:
        ...

    @overload
    def __mul__(self, right: System.UInt128) -> System.UInt128:
        ...

    @overload
    def __mul__(self, right: System.UInt128) -> System.UInt128:
        ...

    def __ne__(self, right: System.UInt128) -> bool:
        ...

    def __or__(self, right: System.UInt128) -> System.UInt128:
        ...

    def __rshift__(self, shift_amount: int) -> System.UInt128:
        ...

    @overload
    def __sub__(self, right: System.UInt128) -> System.UInt128:
        ...

    @overload
    def __sub__(self, right: System.UInt128) -> System.UInt128:
        ...

    @overload
    def __sub__(self) -> System.UInt128:
        ...

    @overload
    def __sub__(self) -> System.UInt128:
        ...

    @overload
    def __truediv__(self, right: System.UInt128) -> System.UInt128:
        ...

    @overload
    def __truediv__(self, right: System.UInt128) -> System.UInt128:
        ...

    def __xor__(self, right: System.UInt128) -> System.UInt128:
        ...

    @staticmethod
    def clamp(value: System.UInt128, min: System.UInt128, max: System.UInt128) -> System.UInt128:
        ...

    @overload
    def compare_to(self, value: typing.Any) -> int:
        ...

    @overload
    def compare_to(self, value: System.UInt128) -> int:
        ...

    @staticmethod
    def div_rem(left: System.UInt128, right: System.UInt128) -> System.ValueTuple[System.UInt128, System.UInt128]:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, other: System.UInt128) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    @staticmethod
    def is_even_integer(value: System.UInt128) -> bool:
        ...

    @staticmethod
    def is_odd_integer(value: System.UInt128) -> bool:
        ...

    @staticmethod
    def is_pow_2(value: System.UInt128) -> bool:
        ...

    @staticmethod
    def leading_zero_count(value: System.UInt128) -> System.UInt128:
        ...

    @staticmethod
    def log_2(value: System.UInt128) -> System.UInt128:
        ...

    @staticmethod
    def max(x: System.UInt128, y: System.UInt128) -> System.UInt128:
        ...

    @staticmethod
    def min(x: System.UInt128, y: System.UInt128) -> System.UInt128:
        ...

    @staticmethod
    @overload
    def parse(s: str) -> System.UInt128:
        ...

    @staticmethod
    @overload
    def parse(s: str, style: System.Globalization.NumberStyles) -> System.UInt128:
        ...

    @staticmethod
    @overload
    def parse(s: str, provider: System.IFormatProvider) -> System.UInt128:
        ...

    @staticmethod
    @overload
    def parse(s: str, style: System.Globalization.NumberStyles, provider: System.IFormatProvider) -> System.UInt128:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> System.UInt128:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider) -> System.UInt128:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int], style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> System.UInt128:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int], provider: System.IFormatProvider) -> System.UInt128:
        ...

    @staticmethod
    def pop_count(value: System.UInt128) -> System.UInt128:
        ...

    @staticmethod
    def rotate_left(value: System.UInt128, rotate_amount: int) -> System.UInt128:
        ...

    @staticmethod
    def rotate_right(value: System.UInt128, rotate_amount: int) -> System.UInt128:
        ...

    @staticmethod
    def sign(value: System.UInt128) -> int:
        ...

    @overload
    def to_string(self) -> str:
        ...

    @overload
    def to_string(self, provider: System.IFormatProvider) -> str:
        ...

    @overload
    def to_string(self, format: str) -> str:
        ...

    @overload
    def to_string(self, format: str, provider: System.IFormatProvider) -> str:
        ...

    @staticmethod
    def trailing_zero_count(value: System.UInt128) -> System.UInt128:
        ...

    @overload
    def try_format(self, destination: System.Span[str], chars_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @overload
    def try_format(self, utf_8_destination: System.Span[int], bytes_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, result: typing.Optional[System.UInt128]) -> typing.Tuple[bool, System.UInt128]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], result: typing.Optional[System.UInt128]) -> typing.Tuple[bool, System.UInt128]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], result: typing.Optional[System.UInt128]) -> typing.Tuple[bool, System.UInt128]:
        """
        Tries to convert a UTF-8 character span containing the string representation of a number to its 128-bit unsigned integer equivalent.
        
        :param utf_8_text: A span containing the UTF-8 characters representing the number to convert.
        :param result: When this method returns, contains the 128-bit unsigned integer value equivalent to the number contained in  if the conversion succeeded, or zero if the conversion failed. This parameter is passed uninitialized; any value originally supplied in result will be overwritten.
        :returns: true if  was converted successfully; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def try_parse(s: str, style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[System.UInt128]) -> typing.Tuple[bool, System.UInt128]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[System.UInt128]) -> typing.Tuple[bool, System.UInt128]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, provider: System.IFormatProvider, result: typing.Optional[System.UInt128]) -> typing.Tuple[bool, System.UInt128]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider, result: typing.Optional[System.UInt128]) -> typing.Tuple[bool, System.UInt128]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[System.UInt128]) -> typing.Tuple[bool, System.UInt128]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], provider: System.IFormatProvider, result: typing.Optional[System.UInt128]) -> typing.Tuple[bool, System.UInt128]:
        ...


class Random(System.Object):
    """
    Represents a pseudo-random number generator, which is an algorithm that produces a sequence of numbers
    that meet certain statistical requirements for randomness.
    """

    SHARED: System.Random
    """Provides a thread-safe Random instance that may be used concurrently from any thread."""

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the Random class using a default seed value."""
        ...

    @overload
    def __init__(self, seed: int) -> None:
        """
        Initializes a new instance of the Random class, using the specified seed value.
        
        :param seed: A number used to calculate a starting value for the pseudo-random number sequence. If a negative number is specified, the absolute value of the number is used.
        """
        ...

    @overload
    def get_hex_string(self, string_length: int, lowercase: bool = False) -> str:
        """
        Creates a string filled with random hexadecimal characters.
        
        :param string_length: The length of string to create.
        :param lowercase: true if the hexadecimal characters should be lowercase; false if they should be uppercase. The default is false.
        :returns: A string populated with random hexadecimal characters.
        """
        ...

    @overload
    def get_hex_string(self, destination: System.Span[str], lowercase: bool = False) -> None:
        """
        Fills a buffer with random hexadecimal characters.
        
        :param destination: The buffer to receive the characters.
        :param lowercase: true if the hexadecimal characters should be lowercase; false if they should be uppercase. The default is false.
        """
        ...

    def get_string(self, choices: System.ReadOnlySpan[str], length: int) -> str:
        """
        Creates a string populated with characters chosen at random from .
        
        :param choices: The characters to use to populate the string.
        :param length: The length of string to return.
        :returns: A string populated with items selected at random from .
        """
        ...

    @overload
    def next(self) -> int:
        """
        Returns a non-negative random integer.
        
        :returns: A 32-bit signed integer that is greater than or equal to 0 and less than int.MaxValue.
        """
        ...

    @overload
    def next(self, max_value: int) -> int:
        """
        Returns a non-negative random integer that is less than the specified maximum.
        
        :param max_value: The exclusive upper bound of the random number to be generated.  must be greater than or equal to 0.
        :returns: A 32-bit signed integer that is greater than or equal to 0, and less than ; that is, the range of return values ordinarily includes 0 but not . However, if  equals 0,  is returned.
        """
        ...

    @overload
    def next(self, min_value: int, max_value: int) -> int:
        """
        Returns a random integer that is within a specified range.
        
        :param min_value: The inclusive lower bound of the random number returned.
        :param max_value: The exclusive upper bound of the random number returned.  must be greater than or equal to .
        :returns: A 32-bit signed integer greater than or equal to  and less than ; that is, the range of return values includes  but not . If min_value equals ,  is returned.
        """
        ...

    @overload
    def next_bytes(self, buffer: typing.List[int]) -> None:
        """
        Fills the elements of a specified array of bytes with random numbers.
        
        :param buffer: The array to be filled with random numbers.
        """
        ...

    @overload
    def next_bytes(self, buffer: System.Span[int]) -> None:
        """
        Fills the elements of a specified span of bytes with random numbers.
        
        :param buffer: The array to be filled with random numbers.
        """
        ...

    def next_double(self) -> float:
        """
        Returns a random floating-point number that is greater than or equal to 0.0, and less than 1.0.
        
        :returns: A double-precision floating point number that is greater than or equal to 0.0, and less than 1.0.
        """
        ...

    @overload
    def next_int_64(self) -> int:
        """
        Returns a non-negative random integer.
        
        :returns: A 64-bit signed integer that is greater than or equal to 0 and less than long.MaxValue.
        """
        ...

    @overload
    def next_int_64(self, max_value: int) -> int:
        """
        Returns a non-negative random integer that is less than the specified maximum.
        
        :param max_value: The exclusive upper bound of the random number to be generated.  must be greater than or equal to 0.
        :returns: A 64-bit signed integer that is greater than or equal to 0, and less than ; that is, the range of return values ordinarily includes 0 but not . However, if  equals 0,  is returned.
        """
        ...

    @overload
    def next_int_64(self, min_value: int, max_value: int) -> int:
        """
        Returns a random integer that is within a specified range.
        
        :param min_value: The inclusive lower bound of the random number returned.
        :param max_value: The exclusive upper bound of the random number returned.  must be greater than or equal to .
        :returns: A 64-bit signed integer greater than or equal to  and less than ; that is, the range of return values includes  but not . If min_value equals ,  is returned.
        """
        ...

    def next_single(self) -> float:
        """
        Returns a random floating-point number that is greater than or equal to 0.0, and less than 1.0.
        
        :returns: A single-precision floating point number that is greater than or equal to 0.0, and less than 1.0.
        """
        ...

    def sample(self) -> float:
        """
        Returns a random floating-point number between 0.0 and 1.0.
        
        This method is protected.
        
        :returns: A double-precision floating point number that is greater than or equal to 0.0, and less than 1.0.
        """
        ...


class ReadOnlySpan(typing.Generic[System_ReadOnlySpan_T]):
    """
    ReadOnlySpan represents a contiguous region of arbitrary memory. Unlike arrays, it can point to either managed
    or native memory, or to memory allocated on the stack. It is type-safe and memory-safe.
    """

    class Enumerator:
        """Enumerates the elements of a ReadOnlySpan{T}."""

        @property
        def current(self) -> typing.Any:
            """Gets the element at the current position of the enumerator."""
            ...

        def move_next(self) -> bool:
            """Advances the enumerator to the next element of the span."""
            ...

    @property
    def length(self) -> int:
        """The number of items in the read-only span."""
        ...

    @property
    def is_empty(self) -> bool:
        """Gets a value indicating whether this ReadOnlySpan{T} is empty."""
        ...

    EMPTY: System.ReadOnlySpan[System_ReadOnlySpan_T]
    """Returns a 0-length read-only span whose base is the null pointer."""

    def __eq__(self, right: System.ReadOnlySpan[System_ReadOnlySpan_T]) -> bool:
        """
        Returns true if left and right point at the same memory and have the same length.  Note that
        this does *not* check to see if the *contents* are equal.
        """
        ...

    def __getitem__(self, index: int) -> typing.Any:
        """
        Returns the specified element of the read-only span.
        
        :param index: The zero-based index.
        """
        ...

    @overload
    def __init__(self, pointer: typing.Any, length: int) -> None:
        """
        Creates a new read-only span over the target unmanaged buffer.  Clearly this
        is quite dangerous, because we are creating arbitrarily typed T's
        out of a void*-typed block of memory.  And the length is not checked.
        But if this creation is correct, then all subsequent uses are correct.
        
        :param pointer: An unmanaged pointer to memory.
        :param length: The number of T elements the memory contains.
        """
        ...

    @overload
    def __init__(self, array: typing.List[System_ReadOnlySpan_T]) -> None:
        """
        Creates a new read-only span over the entirety of the target array.
        
        :param array: The target array.
        """
        ...

    @overload
    def __init__(self, array: typing.List[System_ReadOnlySpan_T], start: int, length: int) -> None:
        """
        Creates a new read-only span over the portion of the target array beginning
        at 'start' index and ending at 'end' index (exclusive).
        
        :param array: The target array.
        :param start: The zero-based index at which to begin the read-only span.
        :param length: The number of items in the read-only span.
        """
        ...

    @overload
    def __init__(self, reference: System_ReadOnlySpan_T) -> None:
        """
        Creates a new ReadOnlySpan{T} of length 1 around the specified reference.
        
        :param reference: A reference to data.
        """
        ...

    def __ne__(self, right: System.ReadOnlySpan[System_ReadOnlySpan_T]) -> bool:
        """
        Returns false if left and right point at the same memory and have the same length.  Note that
        this does *not* check to see if the *contents* are equal.
        """
        ...

    def copy_to(self, destination: System.Span[System_ReadOnlySpan_T]) -> None:
        """
        Copies the contents of this read-only span into destination span. If the source
        and destinations overlap, this method behaves as if the original values in
        a temporary location before the destination is overwritten.
        
        :param destination: The span to copy items into.
        """
        ...

    def equals(self, obj: typing.Any) -> bool:
        """
        This method is not supported as spans cannot be boxed. To compare two spans, use operator==.
        
        Equals() on ReadOnlySpan will always throw an exception. Use the equality operator instead.
        """
        warnings.warn("Equals() on ReadOnlySpan will always throw an exception. Use the equality operator instead.", DeprecationWarning)

    def get_enumerator(self) -> System.ReadOnlySpan.Enumerator:
        """Gets an enumerator for this span."""
        ...

    def get_hash_code(self) -> int:
        """
        This method is not supported as spans cannot be boxed.
        
        GetHashCode() on ReadOnlySpan will always throw an exception.
        """
        warnings.warn("GetHashCode() on ReadOnlySpan will always throw an exception.", DeprecationWarning)

    def get_pinnable_reference(self) -> typing.Any:
        """
        Returns a reference to the 0th element of the Span. If the Span is empty, returns null reference.
        It can be used for pinning and is required to support the use of span within a fixed statement.
        """
        ...

    @overload
    def slice(self, start: int) -> System.ReadOnlySpan[System_ReadOnlySpan_T]:
        """
        Forms a slice out of the given read-only span, beginning at 'start'.
        
        :param start: The zero-based index at which to begin this slice.
        """
        ...

    @overload
    def slice(self, start: int, length: int) -> System.ReadOnlySpan[System_ReadOnlySpan_T]:
        """
        Forms a slice out of the given read-only span, beginning at 'start', of given length
        
        :param start: The zero-based index at which to begin this slice.
        :param length: The desired length for the slice (exclusive).
        """
        ...

    def to_array(self) -> typing.List[System_ReadOnlySpan_T]:
        """
        Copies the contents of this read-only span into a new array.  This heap
        allocates, so should generally be avoided, however it is sometimes
        necessary to bridge the gap with APIs written in terms of arrays.
        """
        ...

    def to_string(self) -> str:
        """
        For ReadOnlySpan{Char}, returns a new instance of string that represents the characters pointed to by the span.
        Otherwise, returns a string with the name of the type and the number of elements.
        """
        ...

    def try_copy_to(self, destination: System.Span[System_ReadOnlySpan_T]) -> bool:
        """
        Copies the contents of this read-only span into destination span. If the source
        and destinations overlap, this method behaves as if the original values in
        a temporary location before the destination is overwritten.
        
        :param destination: The span to copy items into.
        :returns: If the destination span is shorter than the source span, this method return false and no data is written to the destination.
        """
        ...


class IProgress(typing.Generic[System_IProgress_T], metaclass=abc.ABCMeta):
    """Defines a provider for progress updates."""

    def report(self, value: System_IProgress_T) -> None:
        """
        Reports a progress update.
        
        :param value: The value of the updated progress.
        """
        ...


class Void:
    """This class has no documentation."""


class ArgumentException(System.SystemException):
    """The exception that is thrown when one of the arguments provided to a method is not valid."""

    @property
    def message(self) -> str:
        ...

    @property
    def param_name(self) -> str:
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
    def __init__(self, message: str, param_name: str, inner_exception: System.Exception) -> None:
        ...

    @overload
    def __init__(self, message: str, param_name: str) -> None:
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

    @staticmethod
    def throw_if_null_or_empty(argument: str, param_name: str = None) -> None:
        """
        Throws an exception if  is null or empty.
        
        :param argument: The string argument to validate as non-null and non-empty.
        :param param_name: The name of the parameter with which  corresponds.
        """
        ...

    @staticmethod
    def throw_if_null_or_white_space(argument: str, param_name: str = None) -> None:
        """
        Throws an exception if  is null, empty, or consists only of white-space characters.
        
        :param argument: The string argument to validate.
        :param param_name: The name of the parameter with which  corresponds.
        """
        ...


class ArgumentNullException(System.ArgumentException):
    """The exception that is thrown when a null reference (Nothing in Visual Basic) is passed to a method that does not accept it as a valid argument."""

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, param_name: str) -> None:
        ...

    @overload
    def __init__(self, message: str, inner_exception: System.Exception) -> None:
        ...

    @overload
    def __init__(self, param_name: str, message: str) -> None:
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """
        This method is protected.
        
        Obsoletions.LegacyFormatterImplMessage
        """
        ...

    @staticmethod
    def throw_if_null(argument: typing.Any, param_name: str = None) -> None:
        """
        Throws an ArgumentNullException if  is null.
        
        :param argument: The reference type argument to validate as non-null.
        :param param_name: The name of the parameter with which  corresponds.
        """
        ...


class MulticastNotSupportedException(System.SystemException):
    """This class has no documentation."""

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, message: str) -> None:
        ...

    @overload
    def __init__(self, message: str, inner: System.Exception) -> None:
        ...


class StringNormalizationExtensions(System.Object):
    """Extensions for string normalization."""

    @staticmethod
    def get_normalized_length(source: System.ReadOnlySpan[str], normalization_form: System.Text.NormalizationForm = ...) -> int:
        """
        Gets the estimated length of the normalized form of the specified string in the NormalizationForm.FormC.
        
        :param source: The character span to get the estimated length of the normalized form.
        :param normalization_form: The normalization form to use.
        :returns: The estimated length of the normalized form of the specified string.
        """
        ...

    @staticmethod
    @overload
    def is_normalized(str_input: str) -> bool:
        """
        Determines whether the specified string is in a normalized NormalizationForm.FormC.
        
        :param str_input: The string to check.
        :returns: true if the specified string is in a normalized form; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def is_normalized(str_input: str, normalization_form: System.Text.NormalizationForm) -> bool:
        """
        Determines whether the specified string is in a normalized form.
        
        :param str_input: The string to check.
        :param normalization_form: The normalization form to use.
        :returns: true if the specified string is in a normalized form; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def is_normalized(source: System.ReadOnlySpan[str], normalization_form: System.Text.NormalizationForm = ...) -> bool:
        """
        Determines whether the specified span of characters is in a normalized form.
        
        :param source: The span of characters to check.
        :param normalization_form: The normalization form to use.
        :returns: true if the specified span of characters is in a normalized form; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def normalize(str_input: str) -> str:
        """
        Normalizes the specified string to the NormalizationForm.FormC.
        
        :param str_input: The string to normalize.
        :returns: The normalized string in NormalizationForm.FormC.
        """
        ...

    @staticmethod
    @overload
    def normalize(str_input: str, normalization_form: System.Text.NormalizationForm) -> str:
        """
        Normalizes the specified string to the specified normalization form.
        
        :param str_input: The string to normalize.
        :param normalization_form: The normalization form to use.
        :returns: The normalized string in the specified normalization form.
        """
        ...

    @staticmethod
    def try_normalize(source: System.ReadOnlySpan[str], destination: System.Span[str], chars_written: typing.Optional[int], normalization_form: System.Text.NormalizationForm = ...) -> typing.Tuple[bool, int]:
        """
        Normalizes the specified span of characters to the specified normalization form.
        
        :param source: The span of characters to normalize.
        :param destination: The buffer to write the normalized characters to.
        :param chars_written: When this method returns, contains the number of characters written to .
        :param normalization_form: The normalization form to use.
        :returns: true if the specified span of characters was successfully normalized; otherwise, false.
        """
        ...


class InvalidOperationException(System.SystemException):
    """The exception that is thrown when a method call is invalid for the object's current state."""

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


class ObjectDisposedException(System.InvalidOperationException):
    """The exception that is thrown when accessing an object that was disposed."""

    @property
    def message(self) -> str:
        """Gets the text for the message for this exception."""
        ...

    @property
    def object_name(self) -> str:
        ...

    @overload
    def __init__(self, object_name: str) -> None:
        ...

    @overload
    def __init__(self, object_name: str, message: str) -> None:
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

    def get_object_data(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """Obsoletions.LegacyFormatterImplMessage"""
        warnings.warn("Obsoletions.LegacyFormatterImplMessage", DeprecationWarning)

    @staticmethod
    @overload
    def throw_if(condition: bool, instance: typing.Any) -> None:
        """
        Throws an ObjectDisposedException if the specified  is true.
        
        :param condition: The condition to evaluate.
        :param instance: The object whose type's full name should be included in any resulting ObjectDisposedException.
        """
        ...

    @staticmethod
    @overload
    def throw_if(condition: bool, type: typing.Type) -> None:
        """
        Throws an ObjectDisposedException if the specified  is true.
        
        :param condition: The condition to evaluate.
        :param type: The type whose full name should be included in any resulting ObjectDisposedException.
        """
        ...


class InsufficientExecutionStackException(System.SystemException):
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


class SByte(System.IComparable[int], System.IConvertible, System.ISpanFormattable, System.IEquatable[int], System.Numerics.ISignedNumber[int], System.IUtf8SpanFormattable, System.IBinaryIntegerParseAndFormatInfo[int]):
    """This class has no documentation."""

    MAX_VALUE: int = ...

    MIN_VALUE: int = ...

    @overload
    def __ge__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __ge__(self, other: int) -> bool:
        ...

    @overload
    def __gt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __gt__(self, other: int) -> bool:
        ...

    @overload
    def __le__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __le__(self, other: int) -> bool:
        ...

    @overload
    def __lt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __lt__(self, other: int) -> bool:
        ...

    @staticmethod
    def abs(value: int) -> int:
        ...

    @staticmethod
    def clamp(value: int, min: int, max: int) -> int:
        ...

    @overload
    def compare_to(self, obj: typing.Any) -> int:
        ...

    @overload
    def compare_to(self, value: int) -> int:
        ...

    @staticmethod
    def copy_sign(value: int, sign: int) -> int:
        ...

    @staticmethod
    def div_rem(left: int, right: int) -> System.ValueTuple[int, int]:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, obj: int) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def get_type_code(self) -> System.TypeCode:
        ...

    @staticmethod
    def is_even_integer(value: int) -> bool:
        ...

    @staticmethod
    def is_negative(value: int) -> bool:
        ...

    @staticmethod
    def is_odd_integer(value: int) -> bool:
        ...

    @staticmethod
    def is_positive(value: int) -> bool:
        ...

    @staticmethod
    def is_pow_2(value: int) -> bool:
        ...

    @staticmethod
    def leading_zero_count(value: int) -> int:
        ...

    @staticmethod
    def log_2(value: int) -> int:
        ...

    @staticmethod
    def max(x: int, y: int) -> int:
        ...

    @staticmethod
    def max_magnitude(x: int, y: int) -> int:
        ...

    @staticmethod
    def min(x: int, y: int) -> int:
        ...

    @staticmethod
    def min_magnitude(x: int, y: int) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: str) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: str, style: System.Globalization.NumberStyles) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: str, provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: str, style: System.Globalization.NumberStyles, provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int], style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> int:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int], provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    def pop_count(value: int) -> int:
        ...

    @staticmethod
    def rotate_left(value: int, rotate_amount: int) -> int:
        ...

    @staticmethod
    def rotate_right(value: int, rotate_amount: int) -> int:
        ...

    @staticmethod
    def sign(value: int) -> int:
        ...

    @overload
    def to_string(self) -> str:
        ...

    @overload
    def to_string(self, format: str) -> str:
        ...

    @overload
    def to_string(self, provider: System.IFormatProvider) -> str:
        ...

    @overload
    def to_string(self, format: str, provider: System.IFormatProvider) -> str:
        ...

    @staticmethod
    def trailing_zero_count(value: int) -> int:
        ...

    @overload
    def try_format(self, destination: System.Span[str], chars_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @overload
    def try_format(self, utf_8_destination: System.Span[int], bytes_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        """
        Tries to convert a UTF-8 character span containing the string representation of a number to its 8-bit signed integer equivalent.
        
        :param utf_8_text: A span containing the UTF-8 characters representing the number to convert.
        :param result: When this method returns, contains the 8-bit signed integer value equivalent to the number contained in  if the conversion succeeded, or zero if the conversion failed. This parameter is passed uninitialized; any value originally supplied in result will be overwritten.
        :returns: true if  was converted successfully; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def try_parse(s: str, style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...


class Decimal(System.ISpanFormattable, System.IComparable[float], System.IConvertible, System.IEquatable[float], System.Runtime.Serialization.ISerializable, System.Runtime.Serialization.IDeserializationCallback, System.Numerics.IFloatingPoint[float], System.Numerics.IMinMaxValue[float], System.IUtf8SpanFormattable):
    """This class has no documentation."""

    ZERO: float = 0

    ONE: float = 1

    MINUS_ONE: float = -1

    MAX_VALUE: float = 79228162514264337593543950335

    MIN_VALUE: float = -79228162514264337593543950335

    @property
    def scale(self) -> int:
        """Gets the scaling factor of the decimal, which is a number from 0 to 28 that represents the number of decimal digits."""
        ...

    @overload
    def __add__(self) -> float:
        ...

    @overload
    def __add__(self, d_2: float) -> float:
        ...

    def __eq__(self, d_2: float) -> bool:
        ...

    @overload
    def __ge__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __ge__(self, other: float) -> bool:
        ...

    @overload
    def __ge__(self, d_2: float) -> bool:
        ...

    @overload
    def __gt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __gt__(self, other: float) -> bool:
        ...

    @overload
    def __gt__(self, d_2: float) -> bool:
        ...

    @overload
    def __iadd__(self) -> float:
        ...

    @overload
    def __iadd__(self, d_2: float) -> float:
        ...

    def __imod__(self, d_2: float) -> float:
        ...

    def __imul__(self, d_2: float) -> float:
        ...

    @overload
    def __init__(self, value: int) -> None:
        ...

    @overload
    def __init__(self, value: float) -> None:
        ...

    @overload
    def __init__(self, bits: typing.List[int]) -> None:
        ...

    @overload
    def __init__(self, bits: System.ReadOnlySpan[int]) -> None:
        """
        Initializes a new instance of decimal to a decimal value represented in binary and contained in the specified span.
        
        :param bits: A span of four ints containing a binary representation of a decimal value.
        """
        ...

    @overload
    def __init__(self, lo: int, mid: int, hi: int, is_negative: bool, scale: int) -> None:
        ...

    @overload
    def __isub__(self) -> float:
        ...

    @overload
    def __isub__(self, d_2: float) -> float:
        ...

    def __itruediv__(self, d_2: float) -> float:
        ...

    @overload
    def __le__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __le__(self, other: float) -> bool:
        ...

    @overload
    def __le__(self, d_2: float) -> bool:
        ...

    @overload
    def __lt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __lt__(self, other: float) -> bool:
        ...

    @overload
    def __lt__(self, d_2: float) -> bool:
        ...

    def __mod__(self, d_2: float) -> float:
        ...

    def __mul__(self, d_2: float) -> float:
        ...

    def __ne__(self, d_2: float) -> bool:
        ...

    @overload
    def __sub__(self) -> float:
        ...

    @overload
    def __sub__(self, d_2: float) -> float:
        ...

    def __truediv__(self, d_2: float) -> float:
        ...

    @staticmethod
    def abs(value: float) -> float:
        ...

    @staticmethod
    def add(d_1: float, d_2: float) -> float:
        ...

    @staticmethod
    def ceiling(d: float) -> float:
        ...

    @staticmethod
    def clamp(value: float, min: float, max: float) -> float:
        ...

    @staticmethod
    def compare(d_1: float, d_2: float) -> int:
        ...

    @overload
    def compare_to(self, value: typing.Any) -> int:
        ...

    @overload
    def compare_to(self, value: float) -> int:
        ...

    @staticmethod
    def copy_sign(value: float, sign: float) -> float:
        ...

    @staticmethod
    def divide(d_1: float, d_2: float) -> float:
        ...

    @overload
    def equals(self, value: typing.Any) -> bool:
        ...

    @overload
    def equals(self, value: float) -> bool:
        ...

    @staticmethod
    @overload
    def equals(d_1: float, d_2: float) -> bool:
        ...

    @staticmethod
    def floor(d: float) -> float:
        ...

    @staticmethod
    def from_oa_currency(cy: int) -> float:
        ...

    @staticmethod
    @overload
    def get_bits(d: float) -> typing.List[int]:
        ...

    @staticmethod
    @overload
    def get_bits(d: float, destination: System.Span[int]) -> int:
        """
        Converts the value of a specified instance of decimal to its equivalent binary representation.
        
        :param d: The value to convert.
        :param destination: The span into which to store the four-integer binary representation.
        :returns: Four, the number of integers in the binary representation.
        """
        ...

    def get_hash_code(self) -> int:
        ...

    def get_type_code(self) -> System.TypeCode:
        ...

    @staticmethod
    def is_canonical(value: float) -> bool:
        ...

    @staticmethod
    def is_even_integer(value: float) -> bool:
        ...

    @staticmethod
    def is_integer(value: float) -> bool:
        ...

    @staticmethod
    def is_negative(value: float) -> bool:
        ...

    @staticmethod
    def is_odd_integer(value: float) -> bool:
        ...

    @staticmethod
    def is_positive(value: float) -> bool:
        ...

    @staticmethod
    def max(x: float, y: float) -> float:
        ...

    @staticmethod
    def max_magnitude(x: float, y: float) -> float:
        ...

    @staticmethod
    def min(x: float, y: float) -> float:
        ...

    @staticmethod
    def min_magnitude(x: float, y: float) -> float:
        ...

    @staticmethod
    def multiply(d_1: float, d_2: float) -> float:
        ...

    @staticmethod
    def negate(d: float) -> float:
        ...

    @staticmethod
    @overload
    def parse(s: str) -> float:
        ...

    @staticmethod
    @overload
    def parse(s: str, style: System.Globalization.NumberStyles) -> float:
        ...

    @staticmethod
    @overload
    def parse(s: str, provider: System.IFormatProvider) -> float:
        ...

    @staticmethod
    @overload
    def parse(s: str, style: System.Globalization.NumberStyles, provider: System.IFormatProvider) -> float:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> float:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider) -> float:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int], style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> float:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int], provider: System.IFormatProvider) -> float:
        ...

    @staticmethod
    def remainder(d_1: float, d_2: float) -> float:
        ...

    @staticmethod
    @overload
    def round(d: float) -> float:
        ...

    @staticmethod
    @overload
    def round(d: float, decimals: int) -> float:
        ...

    @staticmethod
    @overload
    def round(d: float, mode: System.MidpointRounding) -> float:
        ...

    @staticmethod
    @overload
    def round(d: float, decimals: int, mode: System.MidpointRounding) -> float:
        ...

    @staticmethod
    def sign(d: float) -> int:
        ...

    @staticmethod
    def subtract(d_1: float, d_2: float) -> float:
        ...

    @staticmethod
    def to_byte(value: float) -> int:
        ...

    @staticmethod
    def to_double(d: float) -> float:
        ...

    @staticmethod
    def to_int_16(value: float) -> int:
        ...

    @staticmethod
    def to_int_32(d: float) -> int:
        ...

    @staticmethod
    def to_int_64(d: float) -> int:
        ...

    @staticmethod
    def to_oa_currency(value: float) -> int:
        ...

    @staticmethod
    def to_s_byte(value: float) -> int:
        ...

    @staticmethod
    def to_single(d: float) -> float:
        ...

    @overload
    def to_string(self) -> str:
        ...

    @overload
    def to_string(self, format: str) -> str:
        ...

    @overload
    def to_string(self, provider: System.IFormatProvider) -> str:
        ...

    @overload
    def to_string(self, format: str, provider: System.IFormatProvider) -> str:
        ...

    @staticmethod
    def to_u_int_16(value: float) -> int:
        ...

    @staticmethod
    def to_u_int_32(d: float) -> int:
        ...

    @staticmethod
    def to_u_int_64(d: float) -> int:
        ...

    @staticmethod
    def truncate(d: float) -> float:
        ...

    @overload
    def try_format(self, destination: System.Span[str], chars_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @overload
    def try_format(self, utf_8_destination: System.Span[int], bytes_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    def try_get_bits(d: float, destination: System.Span[int], values_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        """
        Tries to convert the value of a specified instance of decimal to its equivalent binary representation.
        
        :param d: The value to convert.
        :param destination: The span into which to store the binary representation.
        :param values_written: The number of integers written to the destination.
        :returns: true if the decimal's binary representation was written to the destination; false if the destination wasn't long enough.
        """
        ...

    @staticmethod
    @overload
    def try_parse(s: str, result: typing.Optional[float]) -> typing.Tuple[bool, float]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], result: typing.Optional[float]) -> typing.Tuple[bool, float]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], result: typing.Optional[float]) -> typing.Tuple[bool, float]:
        """
        Tries to convert a UTF-8 character span containing the string representation of a number to its signed decimal equivalent.
        
        :param utf_8_text: A span containing the UTF-8 characters representing the number to convert.
        :param result: When this method returns, contains the signed decimal value equivalent to the number contained in  if the conversion succeeded, or zero if the conversion failed. This parameter is passed uninitialized; any value originally supplied in result will be overwritten.
        :returns: true if  was converted successfully; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def try_parse(s: str, style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[float]) -> typing.Tuple[bool, float]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[float]) -> typing.Tuple[bool, float]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, provider: System.IFormatProvider, result: typing.Optional[float]) -> typing.Tuple[bool, float]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider, result: typing.Optional[float]) -> typing.Tuple[bool, float]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[float]) -> typing.Tuple[bool, float]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], provider: System.IFormatProvider, result: typing.Optional[float]) -> typing.Tuple[bool, float]:
        ...


class Boolean(System.IComparable[bool], System.IConvertible, System.IEquatable[bool], System.ISpanParsable[bool]):
    """Represents a boolean (true or false) value."""

    TRUE_STRING: str = ...

    FALSE_STRING: str = ...

    @overload
    def __ge__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __ge__(self, other: bool) -> bool:
        ...

    @overload
    def __gt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __gt__(self, other: bool) -> bool:
        ...

    @overload
    def __le__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __le__(self, other: bool) -> bool:
        ...

    @overload
    def __lt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __lt__(self, other: bool) -> bool:
        ...

    @overload
    def compare_to(self, obj: typing.Any) -> int:
        ...

    @overload
    def compare_to(self, value: bool) -> int:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, obj: bool) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def get_type_code(self) -> System.TypeCode:
        ...

    @staticmethod
    @overload
    def parse(value: str) -> bool:
        ...

    @staticmethod
    @overload
    def parse(value: System.ReadOnlySpan[str]) -> bool:
        ...

    @overload
    def to_string(self) -> str:
        ...

    @overload
    def to_string(self, provider: System.IFormatProvider) -> str:
        ...

    def try_format(self, destination: System.Span[str], chars_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(value: str, result: typing.Optional[bool]) -> typing.Tuple[bool, bool]:
        ...

    @staticmethod
    @overload
    def try_parse(value: System.ReadOnlySpan[str], result: typing.Optional[bool]) -> typing.Tuple[bool, bool]:
        ...


class Int32(System.IComparable[int], System.IConvertible, System.ISpanFormattable, System.IEquatable[int], System.Numerics.ISignedNumber[int], System.IUtf8SpanFormattable, System.IBinaryIntegerParseAndFormatInfo[int]):
    """This class has no documentation."""

    MAX_VALUE: int = ...

    MIN_VALUE: int = ...

    @overload
    def __ge__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __ge__(self, other: int) -> bool:
        ...

    @overload
    def __gt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __gt__(self, other: int) -> bool:
        ...

    @overload
    def __le__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __le__(self, other: int) -> bool:
        ...

    @overload
    def __lt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __lt__(self, other: int) -> bool:
        ...

    @staticmethod
    def abs(value: int) -> int:
        ...

    @staticmethod
    def big_mul(left: int, right: int) -> int:
        """
        Produces the full product of two 32-bit numbers.
        
        :param left: The first number to multiply.
        :param right: The second number to multiply.
        :returns: The number containing the product of the specified numbers.
        """
        ...

    @staticmethod
    def clamp(value: int, min: int, max: int) -> int:
        ...

    @overload
    def compare_to(self, value: typing.Any) -> int:
        ...

    @overload
    def compare_to(self, value: int) -> int:
        ...

    @staticmethod
    def copy_sign(value: int, sign: int) -> int:
        ...

    @staticmethod
    def div_rem(left: int, right: int) -> System.ValueTuple[int, int]:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, obj: int) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def get_type_code(self) -> System.TypeCode:
        ...

    @staticmethod
    def is_even_integer(value: int) -> bool:
        ...

    @staticmethod
    def is_negative(value: int) -> bool:
        ...

    @staticmethod
    def is_odd_integer(value: int) -> bool:
        ...

    @staticmethod
    def is_positive(value: int) -> bool:
        ...

    @staticmethod
    def is_pow_2(value: int) -> bool:
        ...

    @staticmethod
    def leading_zero_count(value: int) -> int:
        ...

    @staticmethod
    def log_2(value: int) -> int:
        ...

    @staticmethod
    def max(x: int, y: int) -> int:
        ...

    @staticmethod
    def max_magnitude(x: int, y: int) -> int:
        ...

    @staticmethod
    def min(x: int, y: int) -> int:
        ...

    @staticmethod
    def min_magnitude(x: int, y: int) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: str) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: str, style: System.Globalization.NumberStyles) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: str, provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: str, style: System.Globalization.NumberStyles, provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int], style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> int:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int], provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    def pop_count(value: int) -> int:
        ...

    @staticmethod
    def rotate_left(value: int, rotate_amount: int) -> int:
        ...

    @staticmethod
    def rotate_right(value: int, rotate_amount: int) -> int:
        ...

    @staticmethod
    def sign(value: int) -> int:
        ...

    @overload
    def to_string(self) -> str:
        ...

    @overload
    def to_string(self, format: str) -> str:
        ...

    @overload
    def to_string(self, provider: System.IFormatProvider) -> str:
        ...

    @overload
    def to_string(self, format: str, provider: System.IFormatProvider) -> str:
        ...

    @staticmethod
    def trailing_zero_count(value: int) -> int:
        ...

    @overload
    def try_format(self, destination: System.Span[str], chars_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @overload
    def try_format(self, utf_8_destination: System.Span[int], bytes_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        """
        Tries to convert a UTF-8 character span containing the string representation of a number to its 32-bit signed integer equivalent.
        
        :param utf_8_text: A span containing the UTF-8 characters representing the number to convert.
        :param result: When this method returns, contains the 32-bit signed integer value equivalent to the number contained in  if the conversion succeeded, or zero if the conversion failed. This parameter is passed uninitialized; any value originally supplied in result will be overwritten.
        :returns: true if  was converted successfully; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def try_parse(s: str, style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...


class DuplicateWaitObjectException(System.ArgumentException):
    """The exception that is thrown when an object appears more than once in an array of synchronization objects."""

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, parameter_name: str) -> None:
        ...

    @overload
    def __init__(self, parameter_name: str, message: str) -> None:
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


class Lazy(typing.Generic[System_Lazy_T, System_Lazy_TMetadata], System_Lazy):
    """Provides support for lazy initialization."""

    @property
    def metadata(self) -> System_Lazy_TMetadata:
        ...

    @property
    def is_value_created(self) -> bool:
        """Gets a value indicating whether the Lazy{T} has been initialized."""
        ...

    @property
    def value(self) -> System_Lazy_T:
        """Gets the lazily initialized value of the current Lazy{T}."""
        ...

    @overload
    def __init__(self, value_factory: typing.Callable[[], System_Lazy_T], metadata: System_Lazy_TMetadata) -> None:
        ...

    @overload
    def __init__(self, metadata: System_Lazy_TMetadata) -> None:
        ...

    @overload
    def __init__(self, metadata: System_Lazy_TMetadata, is_thread_safe: bool) -> None:
        ...

    @overload
    def __init__(self, value_factory: typing.Callable[[], System_Lazy_T], metadata: System_Lazy_TMetadata, is_thread_safe: bool) -> None:
        ...

    @overload
    def __init__(self, metadata: System_Lazy_TMetadata, mode: System.Threading.LazyThreadSafetyMode) -> None:
        ...

    @overload
    def __init__(self, value_factory: typing.Callable[[], System_Lazy_T], metadata: System_Lazy_TMetadata, mode: System.Threading.LazyThreadSafetyMode) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """
        Initializes a new instance of the Lazy{T} class that
        uses T's default constructor for lazy initialization.
        """
        ...

    @overload
    def __init__(self, value: System_Lazy_T) -> None:
        """
        Initializes a new instance of the Lazy{T} class that
        uses a pre-initialized specified value.
        """
        ...

    @overload
    def __init__(self, value_factory: typing.Callable[[], System_Lazy_T]) -> None:
        """
        Initializes a new instance of the Lazy{T} class that uses a
        specified initialization function.
        
        :param value_factory: The Func{T} invoked to produce the lazily-initialized value when it is needed.
        """
        ...

    @overload
    def __init__(self, is_thread_safe: bool) -> None:
        """
        Initializes a new instance of the Lazy{T}
        class that uses T's default constructor and a specified thread-safety mode.
        
        :param is_thread_safe: true if this instance should be usable by multiple threads concurrently; false if the instance will only be used by one thread at a time.
        """
        ...

    @overload
    def __init__(self, mode: System.Threading.LazyThreadSafetyMode) -> None:
        """
        Initializes a new instance of the Lazy{T}
        class that uses T's default constructor and a specified thread-safety mode.
        
        :param mode: The lazy thread-safety mode
        """
        ...

    @overload
    def __init__(self, value_factory: typing.Callable[[], System_Lazy_T], is_thread_safe: bool) -> None:
        """
        Initializes a new instance of the Lazy{T} class
        that uses a specified initialization function and a specified thread-safety mode.
        
        :param value_factory: The Func{T} invoked to produce the lazily-initialized value when it is needed.
        :param is_thread_safe: true if this instance should be usable by multiple threads concurrently; false if the instance will only be used by one thread at a time.
        """
        ...

    @overload
    def __init__(self, value_factory: typing.Callable[[], System_Lazy_T], mode: System.Threading.LazyThreadSafetyMode) -> None:
        """
        Initializes a new instance of the Lazy{T} class
        that uses a specified initialization function and a specified thread-safety mode.
        
        :param value_factory: The Func{T} invoked to produce the lazily-initialized value when it is needed.
        :param mode: The lazy thread-safety mode.
        """
        ...

    def to_string(self) -> str:
        """
        Creates and returns a string representation of this instance.
        
        :returns: The result of calling object.ToString on the Value.
        """
        ...


class TupleExtensions(System.Object):
    """Provides extension methods for Tuple instances to interop with C# tuples features (deconstruction syntax, converting from and to ValueTuple)."""


class NullReferenceException(System.SystemException):
    """The exception that is thrown when there is an attempt to dereference a null object reference."""

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


class ExecutionEngineException(System.SystemException):
    """
    The exception that is thrown when there is an internal error in the execution engine of the common language runtime.
    
    ExecutionEngineException previously indicated an unspecified fatal error in the runtime. The runtime no longer raises this exception so this type is obsolete.
    """

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, message: str) -> None:
        ...

    @overload
    def __init__(self, message: str, inner_exception: System.Exception) -> None:
        ...


class LoaderOptimization(Enum):
    """This class has no documentation."""

    DISALLOW_BINDINGS = 4
    """LoaderOptimization.DisallowBindings has been deprecated and is not supported."""

    DOMAIN_MASK = 3
    """LoaderOptimization.DomainMask has been deprecated and is not supported."""

    MULTI_DOMAIN = 2

    MULTI_DOMAIN_HOST = 3

    NOT_SPECIFIED = 0

    SINGLE_DOMAIN = 1


class Activator(System.Object):
    """Activator contains the Activation (CreateInstance/New) methods for late bound support."""

    @staticmethod
    @overload
    def create_instance(type: typing.Type, binding_attr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, args: typing.List[System.Object], culture: System.Globalization.CultureInfo) -> System.Object:
        ...

    @staticmethod
    @overload
    def create_instance(type: typing.Type, *args: typing.Union[System.Object, typing.Iterable[System.Object]]) -> System.Object:
        ...

    @staticmethod
    @overload
    def create_instance(type: typing.Type, args: typing.List[System.Object], activation_attributes: typing.List[System.Object]) -> System.Object:
        ...

    @staticmethod
    @overload
    def create_instance(type: typing.Type) -> System.Object:
        ...

    @staticmethod
    @overload
    def create_instance(type: typing.Type, binding_attr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, args: typing.List[System.Object], culture: System.Globalization.CultureInfo, activation_attributes: typing.List[System.Object]) -> System.Object:
        ...

    @staticmethod
    @overload
    def create_instance(assembly_name: str, type_name: str) -> System.Runtime.Remoting.ObjectHandle:
        ...

    @staticmethod
    @overload
    def create_instance(assembly_name: str, type_name: str, ignore_case: bool, binding_attr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, args: typing.List[System.Object], culture: System.Globalization.CultureInfo, activation_attributes: typing.List[System.Object]) -> System.Runtime.Remoting.ObjectHandle:
        ...

    @staticmethod
    @overload
    def create_instance(assembly_name: str, type_name: str, activation_attributes: typing.List[System.Object]) -> System.Runtime.Remoting.ObjectHandle:
        ...

    @staticmethod
    @overload
    def create_instance(type: typing.Type, non_public: bool) -> System.Object:
        ...

    @staticmethod
    @overload
    def create_instance_from(assembly_file: str, type_name: str) -> System.Runtime.Remoting.ObjectHandle:
        ...

    @staticmethod
    @overload
    def create_instance_from(assembly_file: str, type_name: str, activation_attributes: typing.List[System.Object]) -> System.Runtime.Remoting.ObjectHandle:
        ...

    @staticmethod
    @overload
    def create_instance_from(assembly_file: str, type_name: str, ignore_case: bool, binding_attr: System.Reflection.BindingFlags, binder: System.Reflection.Binder, args: typing.List[System.Object], culture: System.Globalization.CultureInfo, activation_attributes: typing.List[System.Object]) -> System.Runtime.Remoting.ObjectHandle:
        ...


class FormatException(System.SystemException):
    """The exception that is thrown when the format of an argument is invalid, or when a composite format string is not well formed."""

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


class BadImageFormatException(System.SystemException):
    """The exception that is thrown when the file image of an assembly or an executable program is invalid."""

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


class Memory(typing.Generic[System_Memory_T], System.IEquatable[System_Memory]):
    """
    Memory represents a contiguous region of arbitrary memory similar to Span{T}.
    Unlike Span{T}, it is not a byref-like type.
    """

    EMPTY: System.Memory[System_Memory_T]
    """Returns an empty Memory{T}"""

    @property
    def length(self) -> int:
        """The number of items in the memory."""
        ...

    @property
    def is_empty(self) -> bool:
        """Returns true if Length is 0."""
        ...

    @property
    def span(self) -> System.Span[System_Memory_T]:
        """Returns a span from the memory."""
        ...

    @overload
    def __init__(self, array: typing.List[System_Memory_T]) -> None:
        """
        Creates a new memory over the entirety of the target array.
        
        :param array: The target array.
        """
        ...

    @overload
    def __init__(self, array: typing.List[System_Memory_T], start: int, length: int) -> None:
        """
        Creates a new memory over the portion of the target array beginning
        at 'start' index and ending at 'end' index (exclusive).
        
        :param array: The target array.
        :param start: The index at which to begin the memory.
        :param length: The number of items in the memory.
        """
        ...

    def copy_to(self, destination: System.Memory[System_Memory_T]) -> None:
        """
        Copies the contents of the memory into the destination. If the source
        and destination overlap, this method behaves as if the original values are in
        a temporary location before the destination is overwritten.
        
        :param destination: The Memory to copy items into.
        """
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        """
        Determines whether the specified object is equal to the current object.
        Returns true if the object is Memory or ReadOnlyMemory and if both objects point to the same array and have the same length.
        """
        ...

    @overload
    def equals(self, other: System.Memory[System_Memory_T]) -> bool:
        """
        Returns true if the memory points to the same array and has the same length.  Note that
        this does *not* check to see if the *contents* are equal.
        """
        ...

    def get_hash_code(self) -> int:
        """Serves as the default hash function."""
        ...

    def pin(self) -> System.Buffers.MemoryHandle:
        """
        Creates a handle for the memory.
        The GC will not move the memory until the returned MemoryHandle
        is disposed, enabling taking and using the memory's address.
        """
        ...

    @overload
    def slice(self, start: int) -> System.Memory[System_Memory_T]:
        """
        Forms a slice out of the given memory, beginning at 'start'.
        
        :param start: The index at which to begin this slice.
        """
        ...

    @overload
    def slice(self, start: int, length: int) -> System.Memory[System_Memory_T]:
        """
        Forms a slice out of the given memory, beginning at 'start', of given length
        
        :param start: The index at which to begin this slice.
        :param length: The desired length for the slice (exclusive).
        """
        ...

    def to_array(self) -> typing.List[System_Memory_T]:
        """
        Copies the contents from the memory into a new array.  This heap
        allocates, so should generally be avoided, however it is sometimes
        necessary to bridge the gap with APIs written in terms of arrays.
        """
        ...

    def to_string(self) -> str:
        """
        For Memory{Char}, returns a new instance of string that represents the characters pointed to by the memory.
        Otherwise, returns a string with the name of the type and the number of elements.
        """
        ...

    def try_copy_to(self, destination: System.Memory[System_Memory_T]) -> bool:
        """
        Copies the contents of the memory into the destination. If the source
        and destination overlap, this method behaves as if the original values are in
        a temporary location before the destination is overwritten.
        
        :param destination: The span to copy items into.
        :returns: If the destination is shorter than the source, this method return false and no data is written to the destination.
        """
        ...


class ParamArrayAttribute(System.Attribute):
    """Indicates that a method will allow a variable number of arguments in its invocation."""

    def __init__(self) -> None:
        ...


class HashCode:
    """This class has no documentation."""

    def add_bytes(self, value: System.ReadOnlySpan[int]) -> None:
        """
        Adds a span of bytes to the hash code.
        
        :param value: The span.
        """
        ...

    def equals(self, obj: typing.Any) -> bool:
        """HashCode is a mutable struct and should not be compared with other HashCodes."""
        warnings.warn("HashCode is a mutable struct and should not be compared with other HashCodes.", DeprecationWarning)

    def get_hash_code(self) -> int:
        """HashCode is a mutable struct and should not be compared with other HashCodes. Use ToHashCode to retrieve the computed hash code."""
        warnings.warn("HashCode is a mutable struct and should not be compared with other HashCodes. Use ToHashCode to retrieve the computed hash code.", DeprecationWarning)

    def to_hash_code(self) -> int:
        ...


class TimeSpan(System.IComparable[datetime.timedelta], System.IEquatable[datetime.timedelta], System.ISpanFormattable, System.ISpanParsable[datetime.timedelta], System.IUtf8SpanFormattable):
    """This class has no documentation."""

    NANOSECONDS_PER_TICK: int = 100
    """Represents the number of nanoseconds per tick. This field is constant."""

    TICKS_PER_MICROSECOND: int = 10
    """Represents the number of ticks in 1 microsecond. This field is constant."""

    TICKS_PER_MILLISECOND: int = ...
    """Represents the number of ticks in 1 millisecond. This field is constant."""

    TICKS_PER_SECOND: int = ...
    """Represents the number of ticks in 1 second. This field is constant."""

    TICKS_PER_MINUTE: int = ...
    """Represents the number of ticks in 1 minute. This field is constant."""

    TICKS_PER_HOUR: int = ...
    """Represents the number of ticks in 1 hour. This field is constant."""

    TICKS_PER_DAY: int = ...
    """Represents the number of ticks in 1 day. This field is constant."""

    MICROSECONDS_PER_MILLISECOND: int = ...
    """Represents the number of microseconds in 1 millisecond. This field is constant."""

    MICROSECONDS_PER_SECOND: int = ...
    """Represents the number of microseconds in 1 second. This field is constant."""

    MICROSECONDS_PER_MINUTE: int = ...
    """Represents the number of microseconds in 1 minute. This field is constant."""

    MICROSECONDS_PER_HOUR: int = ...
    """Represents the number of microseconds in 1 hour. This field is constant."""

    MICROSECONDS_PER_DAY: int = ...
    """Represents the number of microseconds in 1 day. This field is constant."""

    MILLISECONDS_PER_SECOND: int = ...
    """Represents the number of milliseconds in 1 second. This field is constant."""

    MILLISECONDS_PER_MINUTE: int = ...
    """Represents the number of milliseconds in 1 minute. This field is constant."""

    MILLISECONDS_PER_HOUR: int = ...
    """Represents the number of milliseconds in 1 hour. This field is constant."""

    MILLISECONDS_PER_DAY: int = ...
    """Represents the number of milliseconds in 1 day. This field is constant."""

    SECONDS_PER_MINUTE: int = ...
    """Represents the number of seconds in 1 minute. This field is constant."""

    SECONDS_PER_HOUR: int = ...
    """Represents the number of seconds in 1 hour. This field is constant."""

    SECONDS_PER_DAY: int = ...
    """Represents the number of seconds in 1 day. This field is constant."""

    MINUTES_PER_HOUR: int = ...
    """Represents the number of minutes in 1 hour. This field is constant."""

    MINUTES_PER_DAY: int = ...
    """Represents the number of minutes in 1 day. This field is constant."""

    HOURS_PER_DAY: int = ...
    """Represents the number of hours in 1 day. This field is constant."""

    ZERO: datetime.timedelta = ...

    MAX_VALUE: datetime.timedelta = ...

    MIN_VALUE: datetime.timedelta = ...

    @property
    def ticks(self) -> int:
        ...

    @property
    def days(self) -> int:
        ...

    @property
    def hours(self) -> int:
        ...

    @property
    def milliseconds(self) -> int:
        ...

    @property
    def microseconds(self) -> int:
        """Gets the microseconds component of the time interval represented by the current TimeSpan structure."""
        ...

    @property
    def nanoseconds(self) -> int:
        """Gets the nanoseconds component of the time interval represented by the current TimeSpan structure."""
        ...

    @property
    def minutes(self) -> int:
        ...

    @property
    def seconds(self) -> int:
        ...

    @property
    def total_days(self) -> float:
        ...

    @property
    def total_hours(self) -> float:
        ...

    @property
    def total_milliseconds(self) -> float:
        ...

    @property
    def total_microseconds(self) -> float:
        """Gets the value of the current TimeSpan structure expressed in whole and fractional microseconds."""
        ...

    @property
    def total_nanoseconds(self) -> float:
        """Gets the value of the current TimeSpan structure expressed in whole and fractional nanoseconds."""
        ...

    @property
    def total_minutes(self) -> float:
        ...

    @property
    def total_seconds(self) -> float:
        ...

    @overload
    def __add__(self) -> datetime.timedelta:
        ...

    @overload
    def __add__(self, t_2: datetime.timedelta) -> datetime.timedelta:
        ...

    def __eq__(self, t_2: datetime.timedelta) -> bool:
        ...

    @overload
    def __ge__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __ge__(self, other: datetime.timedelta) -> bool:
        ...

    @overload
    def __ge__(self, t_2: datetime.timedelta) -> bool:
        ...

    @overload
    def __gt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __gt__(self, other: datetime.timedelta) -> bool:
        ...

    @overload
    def __gt__(self, t_2: datetime.timedelta) -> bool:
        ...

    @overload
    def __iadd__(self) -> datetime.timedelta:
        ...

    @overload
    def __iadd__(self, t_2: datetime.timedelta) -> datetime.timedelta:
        ...

    @overload
    def __imul__(self, factor: float) -> datetime.timedelta:
        ...

    @overload
    def __imul__(self, time_span: datetime.timedelta) -> datetime.timedelta:
        ...

    @overload
    def __init__(self, ticks: int) -> None:
        ...

    @overload
    def __init__(self, hours: int, minutes: int, seconds: int) -> None:
        ...

    @overload
    def __init__(self, days: int, hours: int, minutes: int, seconds: int) -> None:
        ...

    @overload
    def __init__(self, days: int, hours: int, minutes: int, seconds: int, milliseconds: int) -> None:
        """
        Initializes a new instance of the TimeSpan structure to a specified number of
        days, hours, minutes, seconds, and milliseconds.
        
        :param days: Number of days.
        :param hours: Number of hours.
        :param minutes: Number of minutes.
        :param seconds: Number of seconds.
        :param milliseconds: Number of milliseconds.
        """
        ...

    @overload
    def __init__(self, days: int, hours: int, minutes: int, seconds: int, milliseconds: int, microseconds: int) -> None:
        """
        Initializes a new instance of the TimeSpan structure to a specified number of
        days, hours, minutes, seconds, and milliseconds.
        
        :param days: Number of days.
        :param hours: Number of hours.
        :param minutes: Number of minutes.
        :param seconds: Number of seconds.
        :param milliseconds: Number of milliseconds.
        :param microseconds: Number of microseconds.
        """
        ...

    @overload
    def __isub__(self) -> datetime.timedelta:
        ...

    @overload
    def __isub__(self, t_2: datetime.timedelta) -> datetime.timedelta:
        ...

    @overload
    def __itruediv__(self, divisor: float) -> datetime.timedelta:
        ...

    @overload
    def __itruediv__(self, t_2: datetime.timedelta) -> float:
        ...

    @overload
    def __le__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __le__(self, other: datetime.timedelta) -> bool:
        ...

    @overload
    def __le__(self, t_2: datetime.timedelta) -> bool:
        ...

    @overload
    def __lt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __lt__(self, other: datetime.timedelta) -> bool:
        ...

    @overload
    def __lt__(self, t_2: datetime.timedelta) -> bool:
        ...

    @overload
    def __mul__(self, factor: float) -> datetime.timedelta:
        ...

    @overload
    def __mul__(self, time_span: datetime.timedelta) -> datetime.timedelta:
        ...

    def __ne__(self, t_2: datetime.timedelta) -> bool:
        ...

    @overload
    def __sub__(self) -> datetime.timedelta:
        ...

    @overload
    def __sub__(self, t_2: datetime.timedelta) -> datetime.timedelta:
        ...

    @overload
    def __truediv__(self, divisor: float) -> datetime.timedelta:
        ...

    @overload
    def __truediv__(self, t_2: datetime.timedelta) -> float:
        ...

    def add(self, ts: datetime.timedelta) -> datetime.timedelta:
        ...

    @staticmethod
    def compare(t_1: datetime.timedelta, t_2: datetime.timedelta) -> int:
        ...

    @overload
    def compare_to(self, value: typing.Any) -> int:
        ...

    @overload
    def compare_to(self, value: datetime.timedelta) -> int:
        ...

    @overload
    def divide(self, divisor: float) -> datetime.timedelta:
        ...

    @overload
    def divide(self, ts: datetime.timedelta) -> float:
        ...

    def duration(self) -> datetime.timedelta:
        ...

    @overload
    def equals(self, value: typing.Any) -> bool:
        ...

    @overload
    def equals(self, obj: datetime.timedelta) -> bool:
        ...

    @staticmethod
    @overload
    def equals(t_1: datetime.timedelta, t_2: datetime.timedelta) -> bool:
        ...

    @staticmethod
    @overload
    def from_days(value: float) -> datetime.timedelta:
        ...

    @staticmethod
    @overload
    def from_days(days: int) -> datetime.timedelta:
        """
        Initializes a new instance of the TimeSpan structure to a specified number of
        days.
        
        :param days: Number of days.
        :returns: Returns a TimeSpan that represents a specified number of days.
        """
        ...

    @staticmethod
    @overload
    def from_days(days: int, hours: int = 0, minutes: int = 0, seconds: int = 0, milliseconds: int = 0, microseconds: int = 0) -> datetime.timedelta:
        """
        Initializes a new instance of the TimeSpan structure to a specified number of
        days, hours, minutes, seconds, milliseconds, and microseconds.
        
        :param days: Number of days.
        :param hours: Number of hours.
        :param minutes: Number of minutes.
        :param seconds: Number of seconds.
        :param milliseconds: Number of milliseconds.
        :param microseconds: Number of microseconds.
        :returns: Returns a TimeSpan that represents a specified number of days, hours, minutes, seconds, milliseconds, and microseconds.
        """
        ...

    @staticmethod
    @overload
    def from_hours(hours: int) -> datetime.timedelta:
        """
        Initializes a new instance of the TimeSpan structure to a specified number of
        hours.
        
        :param hours: Number of hours.
        :returns: Returns a TimeSpan that represents a specified number of hours.
        """
        ...

    @staticmethod
    @overload
    def from_hours(hours: int, minutes: int = 0, seconds: int = 0, milliseconds: int = 0, microseconds: int = 0) -> datetime.timedelta:
        """
        Initializes a new instance of the TimeSpan structure to a specified number of
        hours, minutes, seconds, milliseconds, and microseconds.
        
        :param hours: Number of hours.
        :param minutes: Number of minutes.
        :param seconds: Number of seconds.
        :param milliseconds: Number of milliseconds.
        :param microseconds: Number of microseconds.
        :returns: Returns a TimeSpan that represents a specified number of hours, minutes, seconds, milliseconds, and microseconds.
        """
        ...

    @staticmethod
    @overload
    def from_hours(value: float) -> datetime.timedelta:
        ...

    @staticmethod
    @overload
    def from_microseconds(microseconds: int) -> datetime.timedelta:
        """
        Initializes a new instance of the TimeSpan structure to a specified number of
        microseconds.
        
        :param microseconds: Number of microseconds.
        :returns: Returns a TimeSpan that represents a specified number of microseconds.
        """
        ...

    @staticmethod
    @overload
    def from_microseconds(value: float) -> datetime.timedelta:
        """
        Returns a TimeSpan that represents a specified number of microseconds.
        
        :param value: A number of microseconds.
        :returns: An object that represents .
        """
        ...

    @staticmethod
    @overload
    def from_milliseconds(milliseconds: int) -> datetime.timedelta:
        """
        Initializes a new instance of the TimeSpan structure to a specified number of
        milliseconds.
        
        :param milliseconds: Number of milliseconds.
        :returns: Returns a TimeSpan that represents a specified number of milliseconds.
        """
        ...

    @staticmethod
    @overload
    def from_milliseconds(milliseconds: int, microseconds: int) -> datetime.timedelta:
        """
        Initializes a new instance of the TimeSpan structure to a specified number of
        milliseconds, and microseconds.
        
        :param milliseconds: Number of milliseconds.
        :param microseconds: Number of microseconds.
        :returns: Returns a TimeSpan that represents a specified number of milliseconds, and microseconds.
        """
        ...

    @staticmethod
    @overload
    def from_milliseconds(value: float) -> datetime.timedelta:
        ...

    @staticmethod
    @overload
    def from_minutes(minutes: int) -> datetime.timedelta:
        """
        Initializes a new instance of the TimeSpan structure to a specified number of
        minutes.
        
        :param minutes: Number of minutes.
        :returns: Returns a TimeSpan that represents a specified number of minutes.
        """
        ...

    @staticmethod
    @overload
    def from_minutes(minutes: int, seconds: int = 0, milliseconds: int = 0, microseconds: int = 0) -> datetime.timedelta:
        """
        Initializes a new instance of the TimeSpan structure to a specified number of
        minutes, seconds, milliseconds, and microseconds.
        
        :param minutes: Number of minutes.
        :param seconds: Number of seconds.
        :param milliseconds: Number of milliseconds.
        :param microseconds: Number of microseconds.
        :returns: Returns a TimeSpan that represents a specified number of minutes, seconds, milliseconds, and microseconds.
        """
        ...

    @staticmethod
    @overload
    def from_minutes(value: float) -> datetime.timedelta:
        ...

    @staticmethod
    @overload
    def from_seconds(seconds: int) -> datetime.timedelta:
        """
        Initializes a new instance of the TimeSpan structure to a specified number of
        seconds.
        
        :param seconds: Number of seconds.
        :returns: Returns a TimeSpan that represents a specified number of seconds.
        """
        ...

    @staticmethod
    @overload
    def from_seconds(seconds: int, milliseconds: int = 0, microseconds: int = 0) -> datetime.timedelta:
        """
        Initializes a new instance of the TimeSpan structure to a specified number of
        seconds, milliseconds, and microseconds.
        
        :param seconds: Number of seconds.
        :param milliseconds: Number of milliseconds.
        :param microseconds: Number of microseconds.
        :returns: Returns a TimeSpan that represents a specified number of seconds, milliseconds, and microseconds.
        """
        ...

    @staticmethod
    @overload
    def from_seconds(value: float) -> datetime.timedelta:
        ...

    @staticmethod
    def from_ticks(value: int) -> datetime.timedelta:
        ...

    def get_hash_code(self) -> int:
        ...

    def multiply(self, factor: float) -> datetime.timedelta:
        ...

    def negate(self) -> datetime.timedelta:
        ...

    @staticmethod
    @overload
    def parse(s: str) -> datetime.timedelta:
        ...

    @staticmethod
    @overload
    def parse(input: str, format_provider: System.IFormatProvider) -> datetime.timedelta:
        ...

    @staticmethod
    @overload
    def parse(input: System.ReadOnlySpan[str], format_provider: System.IFormatProvider = None) -> datetime.timedelta:
        ...

    @staticmethod
    @overload
    def parse_exact(input: str, format: str, format_provider: System.IFormatProvider) -> datetime.timedelta:
        ...

    @staticmethod
    @overload
    def parse_exact(input: str, formats: typing.List[str], format_provider: System.IFormatProvider) -> datetime.timedelta:
        ...

    @staticmethod
    @overload
    def parse_exact(input: str, format: str, format_provider: System.IFormatProvider, styles: System.Globalization.TimeSpanStyles) -> datetime.timedelta:
        ...

    @staticmethod
    @overload
    def parse_exact(input: System.ReadOnlySpan[str], format: System.ReadOnlySpan[str], format_provider: System.IFormatProvider, styles: System.Globalization.TimeSpanStyles = ...) -> datetime.timedelta:
        ...

    @staticmethod
    @overload
    def parse_exact(input: str, formats: typing.List[str], format_provider: System.IFormatProvider, styles: System.Globalization.TimeSpanStyles) -> datetime.timedelta:
        ...

    @staticmethod
    @overload
    def parse_exact(input: System.ReadOnlySpan[str], formats: typing.List[str], format_provider: System.IFormatProvider, styles: System.Globalization.TimeSpanStyles = ...) -> datetime.timedelta:
        ...

    def subtract(self, ts: datetime.timedelta) -> datetime.timedelta:
        ...

    @overload
    def to_string(self) -> str:
        ...

    @overload
    def to_string(self, format: str) -> str:
        ...

    @overload
    def to_string(self, format: str, format_provider: System.IFormatProvider) -> str:
        ...

    @overload
    def try_format(self, destination: System.Span[str], chars_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., format_provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @overload
    def try_format(self, utf_8_destination: System.Span[int], bytes_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., format_provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, result: typing.Optional[datetime.timedelta]) -> typing.Tuple[bool, datetime.timedelta]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], result: typing.Optional[datetime.timedelta]) -> typing.Tuple[bool, datetime.timedelta]:
        ...

    @staticmethod
    @overload
    def try_parse(input: str, format_provider: System.IFormatProvider, result: typing.Optional[datetime.timedelta]) -> typing.Tuple[bool, datetime.timedelta]:
        ...

    @staticmethod
    @overload
    def try_parse(input: System.ReadOnlySpan[str], format_provider: System.IFormatProvider, result: typing.Optional[datetime.timedelta]) -> typing.Tuple[bool, datetime.timedelta]:
        ...

    @staticmethod
    @overload
    def try_parse_exact(input: str, format: str, format_provider: System.IFormatProvider, result: typing.Optional[datetime.timedelta]) -> typing.Tuple[bool, datetime.timedelta]:
        ...

    @staticmethod
    @overload
    def try_parse_exact(input: System.ReadOnlySpan[str], format: System.ReadOnlySpan[str], format_provider: System.IFormatProvider, result: typing.Optional[datetime.timedelta]) -> typing.Tuple[bool, datetime.timedelta]:
        ...

    @staticmethod
    @overload
    def try_parse_exact(input: str, formats: typing.List[str], format_provider: System.IFormatProvider, result: typing.Optional[datetime.timedelta]) -> typing.Tuple[bool, datetime.timedelta]:
        ...

    @staticmethod
    @overload
    def try_parse_exact(input: System.ReadOnlySpan[str], formats: typing.List[str], format_provider: System.IFormatProvider, result: typing.Optional[datetime.timedelta]) -> typing.Tuple[bool, datetime.timedelta]:
        ...

    @staticmethod
    @overload
    def try_parse_exact(input: str, format: str, format_provider: System.IFormatProvider, styles: System.Globalization.TimeSpanStyles, result: typing.Optional[datetime.timedelta]) -> typing.Tuple[bool, datetime.timedelta]:
        ...

    @staticmethod
    @overload
    def try_parse_exact(input: System.ReadOnlySpan[str], format: System.ReadOnlySpan[str], format_provider: System.IFormatProvider, styles: System.Globalization.TimeSpanStyles, result: typing.Optional[datetime.timedelta]) -> typing.Tuple[bool, datetime.timedelta]:
        ...

    @staticmethod
    @overload
    def try_parse_exact(input: str, formats: typing.List[str], format_provider: System.IFormatProvider, styles: System.Globalization.TimeSpanStyles, result: typing.Optional[datetime.timedelta]) -> typing.Tuple[bool, datetime.timedelta]:
        ...

    @staticmethod
    @overload
    def try_parse_exact(input: System.ReadOnlySpan[str], formats: typing.List[str], format_provider: System.IFormatProvider, styles: System.Globalization.TimeSpanStyles, result: typing.Optional[datetime.timedelta]) -> typing.Tuple[bool, datetime.timedelta]:
        ...


class FieldAccessException(System.MemberAccessException):
    """The exception that is thrown when there is an invalid attempt to access a private or protected field inside a class."""

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
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """
        This method is protected.
        
        Obsoletions.LegacyFormatterImplMessage
        """
        ...


class InvalidCastException(System.SystemException):
    """The exception that is thrown for invalid casting or explicit conversion."""

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
    def __init__(self, message: str, error_code: int) -> None:
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """
        This method is protected.
        
        Obsoletions.LegacyFormatterImplMessage
        """
        ...


class TimeZoneNotFoundException(System.Exception):
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


class Double(System.IComparable[float], System.IConvertible, System.ISpanFormattable, System.IEquatable[float], System.IUtf8SpanFormattable, System.IBinaryFloatParseAndFormatInfo[float]):
    """Represents a double-precision floating-point number."""

    MIN_VALUE: float = ...

    MAX_VALUE: float = ...

    EPSILON: float = ...

    NEGATIVE_INFINITY: float = ...

    POSITIVE_INFINITY: float = ...

    NA_N: float = ...

    NEGATIVE_ZERO: float = -0.0
    """Represents the number negative zero (-0)."""

    E: float = ...
    """Represents the natural logarithmic base, specified by the constant, e."""

    PI: float = ...
    """Represents the ratio of the circumference of a circle to its diameter, specified by the constant, PI."""

    TAU: float = ...
    """Represents the number of radians in one turn, specified by the constant, Tau."""

    def __eq__(self, right: float) -> bool:
        ...

    @overload
    def __ge__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __ge__(self, other: float) -> bool:
        ...

    @overload
    def __ge__(self, right: float) -> bool:
        ...

    @overload
    def __gt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __gt__(self, other: float) -> bool:
        ...

    @overload
    def __gt__(self, right: float) -> bool:
        ...

    @overload
    def __le__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __le__(self, other: float) -> bool:
        ...

    @overload
    def __le__(self, right: float) -> bool:
        ...

    @overload
    def __lt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __lt__(self, other: float) -> bool:
        ...

    @overload
    def __lt__(self, right: float) -> bool:
        ...

    def __ne__(self, right: float) -> bool:
        ...

    @staticmethod
    def abs(value: float) -> float:
        ...

    @staticmethod
    def acos(x: float) -> float:
        ...

    @staticmethod
    def acosh(x: float) -> float:
        ...

    @staticmethod
    def acos_pi(x: float) -> float:
        ...

    @staticmethod
    def asin(x: float) -> float:
        ...

    @staticmethod
    def asinh(x: float) -> float:
        ...

    @staticmethod
    def asin_pi(x: float) -> float:
        ...

    @staticmethod
    def atan(x: float) -> float:
        ...

    @staticmethod
    def atan_2(y: float, x: float) -> float:
        ...

    @staticmethod
    def atan_2_pi(y: float, x: float) -> float:
        ...

    @staticmethod
    def atanh(x: float) -> float:
        ...

    @staticmethod
    def atan_pi(x: float) -> float:
        ...

    @staticmethod
    def bit_decrement(x: float) -> float:
        ...

    @staticmethod
    def bit_increment(x: float) -> float:
        ...

    @staticmethod
    def cbrt(x: float) -> float:
        ...

    @staticmethod
    def ceiling(x: float) -> float:
        ...

    @staticmethod
    def clamp(value: float, min: float, max: float) -> float:
        ...

    @staticmethod
    def clamp_native(value: float, min: float, max: float) -> float:
        ...

    @overload
    def compare_to(self, value: typing.Any) -> int:
        ...

    @overload
    def compare_to(self, value: float) -> int:
        ...

    @staticmethod
    def copy_sign(value: float, sign: float) -> float:
        ...

    @staticmethod
    def cos(x: float) -> float:
        ...

    @staticmethod
    def cosh(x: float) -> float:
        ...

    @staticmethod
    def cos_pi(x: float) -> float:
        ...

    @staticmethod
    def degrees_to_radians(degrees: float) -> float:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, obj: float) -> bool:
        ...

    @staticmethod
    def exp(x: float) -> float:
        ...

    @staticmethod
    def exp_10(x: float) -> float:
        ...

    @staticmethod
    def exp_10_m_1(x: float) -> float:
        ...

    @staticmethod
    def exp_2(x: float) -> float:
        ...

    @staticmethod
    def exp_2_m_1(x: float) -> float:
        ...

    @staticmethod
    def exp_m_1(x: float) -> float:
        ...

    @staticmethod
    def floor(x: float) -> float:
        ...

    @staticmethod
    def fused_multiply_add(left: float, right: float, addend: float) -> float:
        ...

    def get_hash_code(self) -> int:
        ...

    def get_type_code(self) -> System.TypeCode:
        ...

    @staticmethod
    def hypot(x: float, y: float) -> float:
        ...

    @staticmethod
    def ieee_754_remainder(left: float, right: float) -> float:
        ...

    @staticmethod
    def i_log_b(x: float) -> int:
        ...

    @staticmethod
    def is_even_integer(value: float) -> bool:
        ...

    @staticmethod
    def is_finite(d: float) -> bool:
        """Determines whether the specified value is finite (zero, subnormal, or normal)."""
        ...

    @staticmethod
    def is_infinity(d: float) -> bool:
        """Determines whether the specified value is infinite."""
        ...

    @staticmethod
    def is_integer(value: float) -> bool:
        ...

    @staticmethod
    def is_na_n(d: float) -> bool:
        """Determines whether the specified value is NaN."""
        ...

    @staticmethod
    def is_negative(d: float) -> bool:
        """Determines whether the specified value is negative."""
        ...

    @staticmethod
    def is_negative_infinity(d: float) -> bool:
        """Determines whether the specified value is negative infinity."""
        ...

    @staticmethod
    def is_normal(d: float) -> bool:
        """Determines whether the specified value is normal (finite, but not zero or subnormal)."""
        ...

    @staticmethod
    def is_odd_integer(value: float) -> bool:
        ...

    @staticmethod
    def is_positive(value: float) -> bool:
        ...

    @staticmethod
    def is_positive_infinity(d: float) -> bool:
        """Determines whether the specified value is positive infinity."""
        ...

    @staticmethod
    def is_pow_2(value: float) -> bool:
        ...

    @staticmethod
    def is_real_number(value: float) -> bool:
        ...

    @staticmethod
    def is_subnormal(d: float) -> bool:
        """Determines whether the specified value is subnormal (finite, but not zero or normal)."""
        ...

    @staticmethod
    def lerp(value_1: float, value_2: float, amount: float) -> float:
        ...

    @staticmethod
    @overload
    def log(x: float) -> float:
        ...

    @staticmethod
    @overload
    def log(x: float, new_base: float) -> float:
        ...

    @staticmethod
    def log_10(x: float) -> float:
        ...

    @staticmethod
    def log_10_p_1(x: float) -> float:
        ...

    @staticmethod
    def log_2(value: float) -> float:
        ...

    @staticmethod
    def log_2_p_1(x: float) -> float:
        ...

    @staticmethod
    def log_p_1(x: float) -> float:
        ...

    @staticmethod
    def max(x: float, y: float) -> float:
        ...

    @staticmethod
    def max_magnitude(x: float, y: float) -> float:
        ...

    @staticmethod
    def max_magnitude_number(x: float, y: float) -> float:
        ...

    @staticmethod
    def max_native(x: float, y: float) -> float:
        ...

    @staticmethod
    def max_number(x: float, y: float) -> float:
        ...

    @staticmethod
    def min(x: float, y: float) -> float:
        ...

    @staticmethod
    def min_magnitude(x: float, y: float) -> float:
        ...

    @staticmethod
    def min_magnitude_number(x: float, y: float) -> float:
        ...

    @staticmethod
    def min_native(x: float, y: float) -> float:
        ...

    @staticmethod
    def min_number(x: float, y: float) -> float:
        ...

    @staticmethod
    def multiply_add_estimate(left: float, right: float, addend: float) -> float:
        ...

    @staticmethod
    @overload
    def parse(s: str) -> float:
        ...

    @staticmethod
    @overload
    def parse(s: str, style: System.Globalization.NumberStyles) -> float:
        ...

    @staticmethod
    @overload
    def parse(s: str, provider: System.IFormatProvider) -> float:
        ...

    @staticmethod
    @overload
    def parse(s: str, style: System.Globalization.NumberStyles, provider: System.IFormatProvider) -> float:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> float:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider) -> float:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int], style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> float:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int], provider: System.IFormatProvider) -> float:
        ...

    @staticmethod
    def pow(x: float, y: float) -> float:
        ...

    @staticmethod
    def radians_to_degrees(radians: float) -> float:
        ...

    @staticmethod
    def reciprocal_estimate(x: float) -> float:
        ...

    @staticmethod
    def reciprocal_sqrt_estimate(x: float) -> float:
        ...

    @staticmethod
    def root_n(x: float, n: int) -> float:
        ...

    @staticmethod
    @overload
    def round(x: float) -> float:
        ...

    @staticmethod
    @overload
    def round(x: float, digits: int) -> float:
        ...

    @staticmethod
    @overload
    def round(x: float, mode: System.MidpointRounding) -> float:
        ...

    @staticmethod
    @overload
    def round(x: float, digits: int, mode: System.MidpointRounding) -> float:
        ...

    @staticmethod
    def scale_b(x: float, n: int) -> float:
        ...

    @staticmethod
    def sign(value: float) -> int:
        ...

    @staticmethod
    def sin(x: float) -> float:
        ...

    @staticmethod
    def sin_cos(x: float) -> System.ValueTuple[float, float]:
        ...

    @staticmethod
    def sin_cos_pi(x: float) -> System.ValueTuple[float, float]:
        ...

    @staticmethod
    def sinh(x: float) -> float:
        ...

    @staticmethod
    def sin_pi(x: float) -> float:
        ...

    @staticmethod
    def sqrt(x: float) -> float:
        ...

    @staticmethod
    def tan(x: float) -> float:
        ...

    @staticmethod
    def tanh(x: float) -> float:
        ...

    @staticmethod
    def tan_pi(x: float) -> float:
        ...

    @overload
    def to_string(self) -> str:
        ...

    @overload
    def to_string(self, format: str) -> str:
        ...

    @overload
    def to_string(self, provider: System.IFormatProvider) -> str:
        ...

    @overload
    def to_string(self, format: str, provider: System.IFormatProvider) -> str:
        ...

    @staticmethod
    def truncate(x: float) -> float:
        ...

    @overload
    def try_format(self, destination: System.Span[str], chars_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @overload
    def try_format(self, utf_8_destination: System.Span[int], bytes_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, result: typing.Optional[float]) -> typing.Tuple[bool, float]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], result: typing.Optional[float]) -> typing.Tuple[bool, float]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], result: typing.Optional[float]) -> typing.Tuple[bool, float]:
        """
        Tries to convert a UTF-8 character span containing the string representation of a number to its double-precision floating-point number equivalent.
        
        :param utf_8_text: A read-only UTF-8 character span that contains the number to convert.
        :param result: When this method returns, contains a double-precision floating-point number equivalent of the numeric value or symbol contained in  if the conversion succeeded or zero if the conversion failed. The conversion fails if the  is ReadOnlySpan{T}.Empty or is not in a valid format. This parameter is passed uninitialized; any value originally supplied in result will be overwritten.
        :returns: true if  was converted successfully; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def try_parse(s: str, style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[float]) -> typing.Tuple[bool, float]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[float]) -> typing.Tuple[bool, float]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, provider: System.IFormatProvider, result: typing.Optional[float]) -> typing.Tuple[bool, float]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider, result: typing.Optional[float]) -> typing.Tuple[bool, float]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[float]) -> typing.Tuple[bool, float]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], provider: System.IFormatProvider, result: typing.Optional[float]) -> typing.Tuple[bool, float]:
        ...


class NotImplementedException(System.SystemException):
    """The exception that is thrown when a requested method or operation is not implemented."""

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
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """
        This method is protected.
        
        Obsoletions.LegacyFormatterImplMessage
        """
        ...


class IObserver(typing.Generic[System_IObserver_T], metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def on_completed(self) -> None:
        ...

    def on_error(self, error: System.Exception) -> None:
        ...

    def on_next(self, value: System_IObserver_T) -> None:
        ...


class UnitySerializationHolder(System.Object, System.Runtime.Serialization.ISerializable, System.Runtime.Serialization.IObjectReference):
    """
    Holds Null class for which we guarantee that there is only ever one instance of.
    This only exists for compatibility with .NET Framework.
    
    Obsoletions.LegacyFormatterMessage
    """

    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...

    def get_object_data(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...

    def get_real_object(self, context: System.Runtime.Serialization.StreamingContext) -> System.Object:
        ...


class GCNotificationStatus(Enum):
    """This class has no documentation."""

    SUCCEEDED = 0

    FAILED = 1

    CANCELED = 2

    TIMEOUT = 3

    NOT_APPLICABLE = 4


class GCCollectionMode(Enum):
    """This class has no documentation."""

    DEFAULT = 0

    FORCED = 1

    OPTIMIZED = 2

    AGGRESSIVE = 3


class GCGenerationInfo:
    """This class has no documentation."""

    @property
    def size_before_bytes(self) -> int:
        """Size in bytes on entry to the reported collection."""
        ...

    @property
    def fragmentation_before_bytes(self) -> int:
        """Fragmentation in bytes on entry to the reported collection."""
        ...

    @property
    def size_after_bytes(self) -> int:
        """Size in bytes on exit from the reported collection."""
        ...

    @property
    def fragmentation_after_bytes(self) -> int:
        """Fragmentation in bytes on exit from the reported collection."""
        ...


class GCMemoryInfo:
    """Provides a set of APIs that can be used to retrieve garbage collection information."""

    @property
    def high_memory_load_threshold_bytes(self) -> int:
        """High memory load threshold when this GC occurred"""
        ...

    @property
    def memory_load_bytes(self) -> int:
        """Memory load when this GC occurred"""
        ...

    @property
    def total_available_memory_bytes(self) -> int:
        """
        Total available memory for the GC to use when this GC occurred.
        
        If the environment variable DOTNET_GCHeapHardLimit is set,
        or "Server.GC.HeapHardLimit" is in runtimeconfig.json, this will come from that.
        If the program is run in a container, this will be an implementation-defined fraction of the container's size.
        Else, this is the physical memory on the machine that was available for the GC to use when this GC occurred.
        """
        ...

    @property
    def heap_size_bytes(self) -> int:
        """The total heap size when this GC occurred"""
        ...

    @property
    def fragmented_bytes(self) -> int:
        """
        The total fragmentation when this GC occurred
        
        Let's take the example below:
         | OBJ_A |     OBJ_B     | OBJ_C |   OBJ_D   | OBJ_E |
        
        Let's say OBJ_B, OBJ_C and and OBJ_E are garbage and get collected, but the heap does not get compacted, the resulting heap will look like the following:
         | OBJ_A |           F           |   OBJ_D   |
        
        The memory between OBJ_A and OBJ_D marked `F` is considered part of the FragmentedBytes, and will be used to allocate new objects. The memory after OBJ_D will not be
        considered part of the FragmentedBytes, and will also be used to allocate new objects
        """
        ...

    @property
    def index(self) -> int:
        """
        The index of this GC. GC indices start with 1 and get increased at the beginning of a GC.
        Since the info is updated at the end of a GC, this means you can get the info for a BGC
        with a smaller index than a foreground GC finished earlier.
        """
        ...

    @property
    def generation(self) -> int:
        """
        The generation this GC collected. Collecting a generation means all its younger generation(s)
        are also collected.
        """
        ...

    @property
    def compacted(self) -> bool:
        """Is this a compacting GC or not."""
        ...

    @property
    def concurrent(self) -> bool:
        """Is this a concurrent GC (BGC) or not."""
        ...

    @property
    def total_committed_bytes(self) -> int:
        """Total committed bytes of the managed heap."""
        ...

    @property
    def promoted_bytes(self) -> int:
        """Promoted bytes for this GC."""
        ...

    @property
    def pinned_objects_count(self) -> int:
        """Number of pinned objects this GC observed."""
        ...

    @property
    def finalization_pending_count(self) -> int:
        """Number of objects ready for finalization this GC observed."""
        ...

    @property
    def pause_durations(self) -> System.ReadOnlySpan[datetime.timedelta]:
        """Pause durations. For blocking GCs there's only 1 pause; for BGC there are 2."""
        ...

    @property
    def pause_time_percentage(self) -> float:
        """This is the % pause time in GC so far. If it's 1.2%, this number is 1.2."""
        ...

    @property
    def generation_info(self) -> System.ReadOnlySpan[System.GCGenerationInfo]:
        """Generation info for all generations."""
        ...


class GCKind(Enum):
    """This class has no documentation."""

    ANY = 0
    """Any kind of collection."""

    EPHEMERAL = 1
    """A gen0 or gen1 collection."""

    FULL_BLOCKING = 2
    """A blocking gen2 collection."""

    BACKGROUND = 3
    """A background collection."""


class GC(System.Object):
    """This class has no documentation."""

    MAX_GENERATION: int

    @staticmethod
    def add_memory_pressure(bytes_allocated: int) -> None:
        ...

    @staticmethod
    def cancel_full_gc_notification() -> None:
        ...

    @staticmethod
    @overload
    def collect(generation: int) -> None:
        ...

    @staticmethod
    @overload
    def collect() -> None:
        ...

    @staticmethod
    @overload
    def collect(generation: int, mode: System.GCCollectionMode) -> None:
        ...

    @staticmethod
    @overload
    def collect(generation: int, mode: System.GCCollectionMode, blocking: bool) -> None:
        ...

    @staticmethod
    @overload
    def collect(generation: int, mode: System.GCCollectionMode, blocking: bool, compacting: bool) -> None:
        ...

    @staticmethod
    def collection_count(generation: int) -> int:
        ...

    @staticmethod
    def end_no_gc_region() -> None:
        ...

    @staticmethod
    def get_allocated_bytes_for_current_thread() -> int:
        ...

    @staticmethod
    def get_configuration_variables() -> System.Collections.Generic.IReadOnlyDictionary[str, System.Object]:
        ...

    @staticmethod
    @overload
    def get_gc_memory_info() -> System.GCMemoryInfo:
        ...

    @staticmethod
    @overload
    def get_gc_memory_info(kind: System.GCKind) -> System.GCMemoryInfo:
        ...

    @staticmethod
    @overload
    def get_generation(obj: typing.Any) -> int:
        ...

    @staticmethod
    @overload
    def get_generation(wo: System.WeakReference) -> int:
        ...

    @staticmethod
    def get_total_allocated_bytes(precise: bool = False) -> int:
        ...

    @staticmethod
    def get_total_memory(force_full_collection: bool) -> int:
        ...

    @staticmethod
    def get_total_pause_duration() -> datetime.timedelta:
        ...

    @staticmethod
    def keep_alive(obj: typing.Any) -> None:
        ...

    @staticmethod
    def refresh_memory_limit() -> None:
        ...

    @staticmethod
    def register_for_full_gc_notification(max_generation_threshold: int, large_object_heap_threshold: int) -> None:
        ...

    @staticmethod
    def register_no_gc_region_callback(total_size: int, callback: typing.Callable[[], None]) -> None:
        ...

    @staticmethod
    def remove_memory_pressure(bytes_allocated: int) -> None:
        ...

    @staticmethod
    def re_register_for_finalize(obj: typing.Any) -> None:
        ...

    @staticmethod
    def suppress_finalize(obj: typing.Any) -> None:
        ...

    @staticmethod
    @overload
    def try_start_no_gc_region(total_size: int) -> bool:
        ...

    @staticmethod
    @overload
    def try_start_no_gc_region(total_size: int, loh_size: int) -> bool:
        ...

    @staticmethod
    @overload
    def try_start_no_gc_region(total_size: int, disallow_full_blocking_gc: bool) -> bool:
        ...

    @staticmethod
    @overload
    def try_start_no_gc_region(total_size: int, loh_size: int, disallow_full_blocking_gc: bool) -> bool:
        ...

    @staticmethod
    @overload
    def wait_for_full_gc_approach(timeout: datetime.timedelta) -> System.GCNotificationStatus:
        """
        Returns, in a specified time-out period, the status of a registered notification for determining whether a full,
        blocking garbage collection by the common language runtime is imminent.
        
        :param timeout: The timeout on waiting for a full GC approach
        :returns: The status of a registered full GC notification.
        """
        ...

    @staticmethod
    @overload
    def wait_for_full_gc_approach() -> System.GCNotificationStatus:
        ...

    @staticmethod
    @overload
    def wait_for_full_gc_approach(milliseconds_timeout: int) -> System.GCNotificationStatus:
        ...

    @staticmethod
    @overload
    def wait_for_full_gc_complete(timeout: datetime.timedelta) -> System.GCNotificationStatus:
        """
        Returns the status of a registered notification about whether a blocking garbage collection
        has completed. May wait indefinitely for a full collection.
        
        :param timeout: The timeout on waiting for a full collection
        :returns: The status of a registered full GC notification.
        """
        ...

    @staticmethod
    @overload
    def wait_for_full_gc_complete() -> System.GCNotificationStatus:
        ...

    @staticmethod
    @overload
    def wait_for_full_gc_complete(milliseconds_timeout: int) -> System.GCNotificationStatus:
        ...

    @staticmethod
    def wait_for_pending_finalizers() -> None:
        ...


class NotSupportedException(System.SystemException):
    """
    The exception that is thrown when an invoked method is not supported,
    typically because it should have been implemented on a subclass.
    """

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


class Single(System.IComparable[float], System.IConvertible, System.ISpanFormattable, System.IEquatable[float], System.IUtf8SpanFormattable, System.IBinaryFloatParseAndFormatInfo[float]):
    """Represents a single-precision floating-point number."""

    MIN_VALUE: float = ...

    MAX_VALUE: float = ...

    EPSILON: float = ...

    NEGATIVE_INFINITY: float = ...

    POSITIVE_INFINITY: float = ...

    NA_N: float = ...

    NEGATIVE_ZERO: float = ...
    """Represents the number negative zero (-0)."""

    E: float = ...
    """Represents the natural logarithmic base, specified by the constant, e."""

    PI: float = ...
    """Represents the ratio of the circumference of a circle to its diameter, specified by the constant, PI."""

    TAU: float = ...
    """Represents the number of radians in one turn, specified by the constant, Tau."""

    def __eq__(self, right: float) -> bool:
        ...

    @overload
    def __ge__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __ge__(self, other: float) -> bool:
        ...

    @overload
    def __ge__(self, right: float) -> bool:
        ...

    @overload
    def __gt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __gt__(self, other: float) -> bool:
        ...

    @overload
    def __gt__(self, right: float) -> bool:
        ...

    @overload
    def __le__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __le__(self, other: float) -> bool:
        ...

    @overload
    def __le__(self, right: float) -> bool:
        ...

    @overload
    def __lt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __lt__(self, other: float) -> bool:
        ...

    @overload
    def __lt__(self, right: float) -> bool:
        ...

    def __ne__(self, right: float) -> bool:
        ...

    @staticmethod
    def abs(value: float) -> float:
        ...

    @staticmethod
    def acos(x: float) -> float:
        ...

    @staticmethod
    def acosh(x: float) -> float:
        ...

    @staticmethod
    def acos_pi(x: float) -> float:
        ...

    @staticmethod
    def asin(x: float) -> float:
        ...

    @staticmethod
    def asinh(x: float) -> float:
        ...

    @staticmethod
    def asin_pi(x: float) -> float:
        ...

    @staticmethod
    def atan(x: float) -> float:
        ...

    @staticmethod
    def atan_2(y: float, x: float) -> float:
        ...

    @staticmethod
    def atan_2_pi(y: float, x: float) -> float:
        ...

    @staticmethod
    def atanh(x: float) -> float:
        ...

    @staticmethod
    def atan_pi(x: float) -> float:
        ...

    @staticmethod
    def bit_decrement(x: float) -> float:
        ...

    @staticmethod
    def bit_increment(x: float) -> float:
        ...

    @staticmethod
    def cbrt(x: float) -> float:
        ...

    @staticmethod
    def ceiling(x: float) -> float:
        ...

    @staticmethod
    def clamp(value: float, min: float, max: float) -> float:
        ...

    @staticmethod
    def clamp_native(value: float, min: float, max: float) -> float:
        ...

    @overload
    def compare_to(self, value: typing.Any) -> int:
        ...

    @overload
    def compare_to(self, value: float) -> int:
        ...

    @staticmethod
    def copy_sign(value: float, sign: float) -> float:
        ...

    @staticmethod
    def cos(x: float) -> float:
        ...

    @staticmethod
    def cosh(x: float) -> float:
        ...

    @staticmethod
    def cos_pi(x: float) -> float:
        ...

    @staticmethod
    def degrees_to_radians(degrees: float) -> float:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, obj: float) -> bool:
        ...

    @staticmethod
    def exp(x: float) -> float:
        ...

    @staticmethod
    def exp_10(x: float) -> float:
        ...

    @staticmethod
    def exp_10_m_1(x: float) -> float:
        ...

    @staticmethod
    def exp_2(x: float) -> float:
        ...

    @staticmethod
    def exp_2_m_1(x: float) -> float:
        ...

    @staticmethod
    def exp_m_1(x: float) -> float:
        ...

    @staticmethod
    def floor(x: float) -> float:
        ...

    @staticmethod
    def fused_multiply_add(left: float, right: float, addend: float) -> float:
        ...

    def get_hash_code(self) -> int:
        ...

    def get_type_code(self) -> System.TypeCode:
        ...

    @staticmethod
    def hypot(x: float, y: float) -> float:
        ...

    @staticmethod
    def ieee_754_remainder(left: float, right: float) -> float:
        ...

    @staticmethod
    def i_log_b(x: float) -> int:
        ...

    @staticmethod
    def is_even_integer(value: float) -> bool:
        ...

    @staticmethod
    def is_finite(f: float) -> bool:
        """Determines whether the specified value is finite (zero, subnormal, or normal)."""
        ...

    @staticmethod
    def is_infinity(f: float) -> bool:
        """Determines whether the specified value is infinite."""
        ...

    @staticmethod
    def is_integer(value: float) -> bool:
        ...

    @staticmethod
    def is_na_n(f: float) -> bool:
        """Determines whether the specified value is NaN."""
        ...

    @staticmethod
    def is_negative(f: float) -> bool:
        """Determines whether the specified value is negative."""
        ...

    @staticmethod
    def is_negative_infinity(f: float) -> bool:
        """Determines whether the specified value is negative infinity."""
        ...

    @staticmethod
    def is_normal(f: float) -> bool:
        """Determines whether the specified value is normal (finite, but not zero or subnormal)."""
        ...

    @staticmethod
    def is_odd_integer(value: float) -> bool:
        ...

    @staticmethod
    def is_positive(value: float) -> bool:
        ...

    @staticmethod
    def is_positive_infinity(f: float) -> bool:
        """Determines whether the specified value is positive infinity."""
        ...

    @staticmethod
    def is_pow_2(value: float) -> bool:
        ...

    @staticmethod
    def is_real_number(value: float) -> bool:
        ...

    @staticmethod
    def is_subnormal(f: float) -> bool:
        """Determines whether the specified value is subnormal (finite, but not zero or normal)."""
        ...

    @staticmethod
    def lerp(value_1: float, value_2: float, amount: float) -> float:
        ...

    @staticmethod
    @overload
    def log(x: float) -> float:
        ...

    @staticmethod
    @overload
    def log(x: float, new_base: float) -> float:
        ...

    @staticmethod
    def log_10(x: float) -> float:
        ...

    @staticmethod
    def log_10_p_1(x: float) -> float:
        ...

    @staticmethod
    def log_2(value: float) -> float:
        ...

    @staticmethod
    def log_2_p_1(x: float) -> float:
        ...

    @staticmethod
    def log_p_1(x: float) -> float:
        ...

    @staticmethod
    def max(x: float, y: float) -> float:
        ...

    @staticmethod
    def max_magnitude(x: float, y: float) -> float:
        ...

    @staticmethod
    def max_magnitude_number(x: float, y: float) -> float:
        ...

    @staticmethod
    def max_native(x: float, y: float) -> float:
        ...

    @staticmethod
    def max_number(x: float, y: float) -> float:
        ...

    @staticmethod
    def min(x: float, y: float) -> float:
        ...

    @staticmethod
    def min_magnitude(x: float, y: float) -> float:
        ...

    @staticmethod
    def min_magnitude_number(x: float, y: float) -> float:
        ...

    @staticmethod
    def min_native(x: float, y: float) -> float:
        ...

    @staticmethod
    def min_number(x: float, y: float) -> float:
        ...

    @staticmethod
    def multiply_add_estimate(left: float, right: float, addend: float) -> float:
        ...

    @staticmethod
    @overload
    def parse(s: str) -> float:
        ...

    @staticmethod
    @overload
    def parse(s: str, style: System.Globalization.NumberStyles) -> float:
        ...

    @staticmethod
    @overload
    def parse(s: str, provider: System.IFormatProvider) -> float:
        ...

    @staticmethod
    @overload
    def parse(s: str, style: System.Globalization.NumberStyles, provider: System.IFormatProvider) -> float:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> float:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider) -> float:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int], style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> float:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int], provider: System.IFormatProvider) -> float:
        ...

    @staticmethod
    def pow(x: float, y: float) -> float:
        ...

    @staticmethod
    def radians_to_degrees(radians: float) -> float:
        ...

    @staticmethod
    def reciprocal_estimate(x: float) -> float:
        ...

    @staticmethod
    def reciprocal_sqrt_estimate(x: float) -> float:
        ...

    @staticmethod
    def root_n(x: float, n: int) -> float:
        ...

    @staticmethod
    @overload
    def round(x: float) -> float:
        ...

    @staticmethod
    @overload
    def round(x: float, digits: int) -> float:
        ...

    @staticmethod
    @overload
    def round(x: float, mode: System.MidpointRounding) -> float:
        ...

    @staticmethod
    @overload
    def round(x: float, digits: int, mode: System.MidpointRounding) -> float:
        ...

    @staticmethod
    def scale_b(x: float, n: int) -> float:
        ...

    @staticmethod
    def sign(value: float) -> int:
        ...

    @staticmethod
    def sin(x: float) -> float:
        ...

    @staticmethod
    def sin_cos(x: float) -> System.ValueTuple[float, float]:
        ...

    @staticmethod
    def sin_cos_pi(x: float) -> System.ValueTuple[float, float]:
        ...

    @staticmethod
    def sinh(x: float) -> float:
        ...

    @staticmethod
    def sin_pi(x: float) -> float:
        ...

    @staticmethod
    def sqrt(x: float) -> float:
        ...

    @staticmethod
    def tan(x: float) -> float:
        ...

    @staticmethod
    def tanh(x: float) -> float:
        ...

    @staticmethod
    def tan_pi(x: float) -> float:
        ...

    @overload
    def to_string(self) -> str:
        ...

    @overload
    def to_string(self, provider: System.IFormatProvider) -> str:
        ...

    @overload
    def to_string(self, format: str) -> str:
        ...

    @overload
    def to_string(self, format: str, provider: System.IFormatProvider) -> str:
        ...

    @staticmethod
    def truncate(x: float) -> float:
        ...

    @overload
    def try_format(self, destination: System.Span[str], chars_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @overload
    def try_format(self, utf_8_destination: System.Span[int], bytes_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, result: typing.Optional[float]) -> typing.Tuple[bool, float]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], result: typing.Optional[float]) -> typing.Tuple[bool, float]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], result: typing.Optional[float]) -> typing.Tuple[bool, float]:
        """
        Tries to convert a UTF-8 character span containing the string representation of a number to its single-precision floating-point number equivalent.
        
        :param utf_8_text: A read-only UTF-8 character span that contains the number to convert.
        :param result: When this method returns, contains a single-precision floating-point number equivalent of the numeric value or symbol contained in  if the conversion succeeded or zero if the conversion failed. The conversion fails if the  is ReadOnlySpan{T}.Empty or is not in a valid format. This parameter is passed uninitialized; any value originally supplied in result will be overwritten.
        :returns: true if  was converted successfully; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def try_parse(s: str, style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[float]) -> typing.Tuple[bool, float]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[float]) -> typing.Tuple[bool, float]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, provider: System.IFormatProvider, result: typing.Optional[float]) -> typing.Tuple[bool, float]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider, result: typing.Optional[float]) -> typing.Tuple[bool, float]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[float]) -> typing.Tuple[bool, float]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], provider: System.IFormatProvider, result: typing.Optional[float]) -> typing.Tuple[bool, float]:
        ...


class Half(System.IComparable[System_Half], System.ISpanFormattable, System.IEquatable[System_Half], System.IUtf8SpanFormattable, System.IBinaryFloatParseAndFormatInfo[System_Half]):
    """Represents a half-precision floating-point number."""

    EPSILON: System.Half

    POSITIVE_INFINITY: System.Half

    NEGATIVE_INFINITY: System.Half

    NA_N: System.Half

    MIN_VALUE: System.Half

    MAX_VALUE: System.Half

    E: System.Half

    PI: System.Half

    TAU: System.Half

    NEGATIVE_ZERO: System.Half

    MULTIPLICATIVE_IDENTITY: System.Half

    ONE: System.Half

    ZERO: System.Half

    NEGATIVE_ONE: System.Half

    @overload
    def __add__(self, right: System.Half) -> System.Half:
        ...

    @overload
    def __add__(self) -> System.Half:
        ...

    def __eq__(self, right: System.Half) -> bool:
        ...

    @overload
    def __ge__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __ge__(self, right: System.Half) -> bool:
        ...

    @overload
    def __ge__(self, other: System.Half) -> bool:
        ...

    @overload
    def __gt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __gt__(self, right: System.Half) -> bool:
        ...

    @overload
    def __gt__(self, other: System.Half) -> bool:
        ...

    @overload
    def __iadd__(self, right: System.Half) -> System.Half:
        ...

    @overload
    def __iadd__(self) -> System.Half:
        ...

    def __imod__(self, right: System.Half) -> System.Half:
        ...

    def __imul__(self, right: System.Half) -> System.Half:
        ...

    @overload
    def __isub__(self, right: System.Half) -> System.Half:
        ...

    @overload
    def __isub__(self) -> System.Half:
        ...

    def __itruediv__(self, right: System.Half) -> System.Half:
        ...

    @overload
    def __le__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __le__(self, right: System.Half) -> bool:
        ...

    @overload
    def __le__(self, other: System.Half) -> bool:
        ...

    @overload
    def __lt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __lt__(self, right: System.Half) -> bool:
        ...

    @overload
    def __lt__(self, other: System.Half) -> bool:
        ...

    def __mod__(self, right: System.Half) -> System.Half:
        ...

    def __mul__(self, right: System.Half) -> System.Half:
        ...

    def __ne__(self, right: System.Half) -> bool:
        ...

    @overload
    def __sub__(self, right: System.Half) -> System.Half:
        ...

    @overload
    def __sub__(self) -> System.Half:
        ...

    def __truediv__(self, right: System.Half) -> System.Half:
        ...

    @staticmethod
    def abs(value: System.Half) -> System.Half:
        ...

    @staticmethod
    def acos(x: System.Half) -> System.Half:
        ...

    @staticmethod
    def acosh(x: System.Half) -> System.Half:
        ...

    @staticmethod
    def acos_pi(x: System.Half) -> System.Half:
        ...

    @staticmethod
    def asin(x: System.Half) -> System.Half:
        ...

    @staticmethod
    def asinh(x: System.Half) -> System.Half:
        ...

    @staticmethod
    def asin_pi(x: System.Half) -> System.Half:
        ...

    @staticmethod
    def atan(x: System.Half) -> System.Half:
        ...

    @staticmethod
    def atan_2(y: System.Half, x: System.Half) -> System.Half:
        ...

    @staticmethod
    def atan_2_pi(y: System.Half, x: System.Half) -> System.Half:
        ...

    @staticmethod
    def atanh(x: System.Half) -> System.Half:
        ...

    @staticmethod
    def atan_pi(x: System.Half) -> System.Half:
        ...

    @staticmethod
    def bit_decrement(x: System.Half) -> System.Half:
        ...

    @staticmethod
    def bit_increment(x: System.Half) -> System.Half:
        ...

    @staticmethod
    def cbrt(x: System.Half) -> System.Half:
        ...

    @staticmethod
    def ceiling(x: System.Half) -> System.Half:
        ...

    @staticmethod
    def clamp(value: System.Half, min: System.Half, max: System.Half) -> System.Half:
        ...

    @staticmethod
    def clamp_native(value: System.Half, min: System.Half, max: System.Half) -> System.Half:
        ...

    @overload
    def compare_to(self, obj: typing.Any) -> int:
        """
        Compares this object to another object, returning an integer that indicates the relationship.
        
        :returns: A value less than zero if this is less than , zero if this is equal to , or a value greater than zero if this is greater than .
        """
        ...

    @overload
    def compare_to(self, other: System.Half) -> int:
        """
        Compares this object to another object, returning an integer that indicates the relationship.
        
        :returns: A value less than zero if this is less than , zero if this is equal to , or a value greater than zero if this is greater than .
        """
        ...

    @staticmethod
    def copy_sign(value: System.Half, sign: System.Half) -> System.Half:
        ...

    @staticmethod
    def cos(x: System.Half) -> System.Half:
        ...

    @staticmethod
    def cosh(x: System.Half) -> System.Half:
        ...

    @staticmethod
    def cos_pi(x: System.Half) -> System.Half:
        ...

    @staticmethod
    def degrees_to_radians(degrees: System.Half) -> System.Half:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        """Returns a value that indicates whether this instance is equal to a specified ."""
        ...

    @overload
    def equals(self, other: System.Half) -> bool:
        """Returns a value that indicates whether this instance is equal to a specified  value."""
        ...

    @staticmethod
    def exp(x: System.Half) -> System.Half:
        ...

    @staticmethod
    def exp_10(x: System.Half) -> System.Half:
        ...

    @staticmethod
    def exp_10_m_1(x: System.Half) -> System.Half:
        ...

    @staticmethod
    def exp_2(x: System.Half) -> System.Half:
        ...

    @staticmethod
    def exp_2_m_1(x: System.Half) -> System.Half:
        ...

    @staticmethod
    def exp_m_1(x: System.Half) -> System.Half:
        ...

    @staticmethod
    def floor(x: System.Half) -> System.Half:
        ...

    @staticmethod
    def fused_multiply_add(left: System.Half, right: System.Half, addend: System.Half) -> System.Half:
        ...

    def get_hash_code(self) -> int:
        """Serves as the default hash function."""
        ...

    @staticmethod
    def hypot(x: System.Half, y: System.Half) -> System.Half:
        ...

    @staticmethod
    def ieee_754_remainder(left: System.Half, right: System.Half) -> System.Half:
        ...

    @staticmethod
    def i_log_b(x: System.Half) -> int:
        ...

    @staticmethod
    def is_even_integer(value: System.Half) -> bool:
        ...

    @staticmethod
    def is_finite(value: System.Half) -> bool:
        """Determines whether the specified value is finite (zero, subnormal, or normal)."""
        ...

    @staticmethod
    def is_infinity(value: System.Half) -> bool:
        """Determines whether the specified value is infinite."""
        ...

    @staticmethod
    def is_integer(value: System.Half) -> bool:
        ...

    @staticmethod
    def is_na_n(value: System.Half) -> bool:
        """Determines whether the specified value is NaN."""
        ...

    @staticmethod
    def is_negative(value: System.Half) -> bool:
        """Determines whether the specified value is negative."""
        ...

    @staticmethod
    def is_negative_infinity(value: System.Half) -> bool:
        """Determines whether the specified value is negative infinity."""
        ...

    @staticmethod
    def is_normal(value: System.Half) -> bool:
        """Determines whether the specified value is normal (finite, but not zero or subnormal)."""
        ...

    @staticmethod
    def is_odd_integer(value: System.Half) -> bool:
        ...

    @staticmethod
    def is_positive(value: System.Half) -> bool:
        ...

    @staticmethod
    def is_positive_infinity(value: System.Half) -> bool:
        """Determines whether the specified value is positive infinity."""
        ...

    @staticmethod
    def is_pow_2(value: System.Half) -> bool:
        ...

    @staticmethod
    def is_real_number(value: System.Half) -> bool:
        ...

    @staticmethod
    def is_subnormal(value: System.Half) -> bool:
        """Determines whether the specified value is subnormal (finite, but not zero or normal)."""
        ...

    @staticmethod
    def lerp(value_1: System.Half, value_2: System.Half, amount: System.Half) -> System.Half:
        ...

    @staticmethod
    @overload
    def log(x: System.Half) -> System.Half:
        ...

    @staticmethod
    @overload
    def log(x: System.Half, new_base: System.Half) -> System.Half:
        ...

    @staticmethod
    def log_10(x: System.Half) -> System.Half:
        ...

    @staticmethod
    def log_10_p_1(x: System.Half) -> System.Half:
        ...

    @staticmethod
    def log_2(value: System.Half) -> System.Half:
        ...

    @staticmethod
    def log_2_p_1(x: System.Half) -> System.Half:
        ...

    @staticmethod
    def log_p_1(x: System.Half) -> System.Half:
        ...

    @staticmethod
    def max(x: System.Half, y: System.Half) -> System.Half:
        ...

    @staticmethod
    def max_magnitude(x: System.Half, y: System.Half) -> System.Half:
        ...

    @staticmethod
    def max_magnitude_number(x: System.Half, y: System.Half) -> System.Half:
        ...

    @staticmethod
    def max_native(x: System.Half, y: System.Half) -> System.Half:
        ...

    @staticmethod
    def max_number(x: System.Half, y: System.Half) -> System.Half:
        ...

    @staticmethod
    def min(x: System.Half, y: System.Half) -> System.Half:
        ...

    @staticmethod
    def min_magnitude(x: System.Half, y: System.Half) -> System.Half:
        ...

    @staticmethod
    def min_magnitude_number(x: System.Half, y: System.Half) -> System.Half:
        ...

    @staticmethod
    def min_native(x: System.Half, y: System.Half) -> System.Half:
        ...

    @staticmethod
    def min_number(x: System.Half, y: System.Half) -> System.Half:
        ...

    @staticmethod
    def multiply_add_estimate(left: System.Half, right: System.Half, addend: System.Half) -> System.Half:
        ...

    @staticmethod
    @overload
    def parse(s: str) -> System.Half:
        """
        Parses a Half from a string in the default parse style.
        
        :param s: The input to be parsed.
        :returns: The equivalent Half value representing the input string. If the input exceeds Half's range, a PositiveInfinity or NegativeInfinity is returned.
        """
        ...

    @staticmethod
    @overload
    def parse(s: str, style: System.Globalization.NumberStyles) -> System.Half:
        """
        Parses a Half from a string in the given NumberStyles.
        
        :param s: The input to be parsed.
        :param style: The NumberStyles used to parse the input.
        :returns: The equivalent Half value representing the input string. If the input exceeds Half's range, a PositiveInfinity or NegativeInfinity is returned.
        """
        ...

    @staticmethod
    @overload
    def parse(s: str, provider: System.IFormatProvider) -> System.Half:
        """
        Parses a Half from a string and IFormatProvider.
        
        :param s: The input to be parsed.
        :param provider: A format provider.
        :returns: The equivalent Half value representing the input string. If the input exceeds Half's range, a PositiveInfinity or NegativeInfinity is returned.
        """
        ...

    @staticmethod
    @overload
    def parse(s: str, style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> System.Half:
        """
        Parses a Half from a string with the given NumberStyles and IFormatProvider.
        
        :param s: The input to be parsed.
        :param style: The NumberStyles used to parse the input.
        :param provider: A format provider.
        :returns: The equivalent Half value representing the input string. If the input exceeds Half's range, a PositiveInfinity or NegativeInfinity is returned.
        """
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> System.Half:
        """
        Parses a Half from a ReadOnlySpan{Char} and IFormatProvider.
        
        :param s: The input to be parsed.
        :param style: The NumberStyles used to parse the input.
        :param provider: A format provider.
        :returns: The equivalent Half value representing the input string. If the input exceeds Half's range, a PositiveInfinity or NegativeInfinity is returned.
        """
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider) -> System.Half:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int], style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> System.Half:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int], provider: System.IFormatProvider) -> System.Half:
        ...

    @staticmethod
    def pow(x: System.Half, y: System.Half) -> System.Half:
        ...

    @staticmethod
    def radians_to_degrees(radians: System.Half) -> System.Half:
        ...

    @staticmethod
    def reciprocal_estimate(x: System.Half) -> System.Half:
        ...

    @staticmethod
    def reciprocal_sqrt_estimate(x: System.Half) -> System.Half:
        ...

    @staticmethod
    def root_n(x: System.Half, n: int) -> System.Half:
        ...

    @staticmethod
    @overload
    def round(x: System.Half) -> System.Half:
        ...

    @staticmethod
    @overload
    def round(x: System.Half, digits: int) -> System.Half:
        ...

    @staticmethod
    @overload
    def round(x: System.Half, mode: System.MidpointRounding) -> System.Half:
        ...

    @staticmethod
    @overload
    def round(x: System.Half, digits: int, mode: System.MidpointRounding) -> System.Half:
        ...

    @staticmethod
    def scale_b(x: System.Half, n: int) -> System.Half:
        ...

    @staticmethod
    def sign(value: System.Half) -> int:
        ...

    @staticmethod
    def sin(x: System.Half) -> System.Half:
        ...

    @staticmethod
    def sin_cos(x: System.Half) -> System.ValueTuple[System.Half, System.Half]:
        ...

    @staticmethod
    def sin_cos_pi(x: System.Half) -> System.ValueTuple[System.Half, System.Half]:
        ...

    @staticmethod
    def sinh(x: System.Half) -> System.Half:
        ...

    @staticmethod
    def sin_pi(x: System.Half) -> System.Half:
        ...

    @staticmethod
    def sqrt(x: System.Half) -> System.Half:
        ...

    @staticmethod
    def tan(x: System.Half) -> System.Half:
        ...

    @staticmethod
    def tanh(x: System.Half) -> System.Half:
        ...

    @staticmethod
    def tan_pi(x: System.Half) -> System.Half:
        ...

    @overload
    def to_string(self) -> str:
        """Returns a string representation of the current value."""
        ...

    @overload
    def to_string(self, format: str) -> str:
        """Returns a string representation of the current value using the specified ."""
        ...

    @overload
    def to_string(self, provider: System.IFormatProvider) -> str:
        """Returns a string representation of the current value with the specified ."""
        ...

    @overload
    def to_string(self, format: str, provider: System.IFormatProvider) -> str:
        """Returns a string representation of the current value using the specified  and ."""
        ...

    @staticmethod
    def truncate(x: System.Half) -> System.Half:
        ...

    @overload
    def try_format(self, destination: System.Span[str], chars_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        """
        Tries to format the value of the current Half instance into the provided span of characters.
        
        :param destination: When this method returns, this instance's value formatted as a span of characters.
        :param chars_written: When this method returns, the number of characters that were written in .
        :param format: A span containing the characters that represent a standard or custom format string that defines the acceptable format for .
        :param provider: An optional object that supplies culture-specific formatting information for .
        """
        ...

    @overload
    def try_format(self, utf_8_destination: System.Span[int], bytes_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, result: typing.Optional[System.Half]) -> typing.Tuple[bool, System.Half]:
        """
        Tries to parse a Half from a string in the default parse style.
        
        :param s: The input to be parsed.
        :param result: The equivalent Half value representing the input string if the parse was successful. If the input exceeds Half's range, a PositiveInfinity or NegativeInfinity is returned. If the parse was unsuccessful, a default Half value is returned.
        :returns: true if the parse was successful, false otherwise.
        """
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], result: typing.Optional[System.Half]) -> typing.Tuple[bool, System.Half]:
        """
        Tries to parse a Half from a ReadOnlySpan{Char} in the default parse style.
        
        :param s: The input to be parsed.
        :param result: The equivalent Half value representing the input string if the parse was successful. If the input exceeds Half's range, a PositiveInfinity or NegativeInfinity is returned. If the parse was unsuccessful, a default Half value is returned.
        :returns: true if the parse was successful, false otherwise.
        """
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], result: typing.Optional[System.Half]) -> typing.Tuple[bool, System.Half]:
        """
        Tries to convert a UTF-8 character span containing the string representation of a number to its half-precision floating-point number equivalent.
        
        :param utf_8_text: A read-only UTF-8 character span that contains the number to convert.
        :param result: When this method returns, contains a half-precision floating-point number equivalent of the numeric value or symbol contained in  if the conversion succeeded or zero if the conversion failed. The conversion fails if the  is ReadOnlySpan{T}.Empty or is not in a valid format. This parameter is passed uninitialized; any value originally supplied in result will be overwritten.
        :returns: true if  was converted successfully; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def try_parse(s: str, style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[System.Half]) -> typing.Tuple[bool, System.Half]:
        """
        Tries to parse a Half from a string with the given NumberStyles and IFormatProvider.
        
        :param s: The input to be parsed.
        :param style: The NumberStyles used to parse the input.
        :param provider: A format provider.
        :param result: The equivalent Half value representing the input string if the parse was successful. If the input exceeds Half's range, a PositiveInfinity or NegativeInfinity is returned. If the parse was unsuccessful, a default Half value is returned.
        :returns: true if the parse was successful, false otherwise.
        """
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[System.Half]) -> typing.Tuple[bool, System.Half]:
        """
        Tries to parse a Half from a ReadOnlySpan{Char} with the given NumberStyles and IFormatProvider.
        
        :param s: The input to be parsed.
        :param style: The NumberStyles used to parse the input.
        :param provider: A format provider.
        :param result: The equivalent Half value representing the input string if the parse was successful. If the input exceeds Half's range, a PositiveInfinity or NegativeInfinity is returned. If the parse was unsuccessful, a default Half value is returned.
        :returns: true if the parse was successful, false otherwise.
        """
        ...

    @staticmethod
    @overload
    def try_parse(s: str, provider: System.IFormatProvider, result: typing.Optional[System.Half]) -> typing.Tuple[bool, System.Half]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider, result: typing.Optional[System.Half]) -> typing.Tuple[bool, System.Half]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[System.Half]) -> typing.Tuple[bool, System.Half]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], provider: System.IFormatProvider, result: typing.Optional[System.Half]) -> typing.Tuple[bool, System.Half]:
        ...


class BitConverter(System.Object):
    """Converts base data types to an array of bytes, and an array of bytes to base data types."""

    IS_LITTLE_ENDIAN: bool = True

    @staticmethod
    def double_to_int_64_bits(value: float) -> int:
        """
        Converts the specified double-precision floating point number to a 64-bit signed integer.
        
        :param value: The number to convert.
        :returns: A 64-bit signed integer whose bits are identical to .
        """
        ...

    @staticmethod
    def double_to_u_int_64_bits(value: float) -> int:
        """
        Converts the specified double-precision floating point number to a 64-bit unsigned integer.
        
        :param value: The number to convert.
        :returns: A 64-bit unsigned integer whose bits are identical to .
        """
        ...

    @staticmethod
    @overload
    def get_bytes(value: bool) -> typing.List[int]:
        """
        Returns the specified Boolean value as a byte array.
        
        :param value: A Boolean value.
        :returns: A byte array with length 1.
        """
        ...

    @staticmethod
    @overload
    def get_bytes(value: str) -> typing.List[int]:
        """
        Returns the specified Unicode character value as a byte array.
        
        :param value: A Char value.
        :returns: An array of bytes with length 2.
        """
        ...

    @staticmethod
    @overload
    def get_bytes(value: int) -> typing.List[int]:
        """
        Returns the specified 16-bit signed integer value as an array of bytes.
        
        :param value: The number to convert.
        :returns: An array of bytes with length 2.
        """
        ...

    @staticmethod
    @overload
    def get_bytes(value: System.Int128) -> typing.List[int]:
        """
        Returns the specified 128-bit signed integer value as an array of bytes.
        
        :param value: The number to convert.
        :returns: An array of bytes with length 16.
        """
        ...

    @staticmethod
    @overload
    def get_bytes(value: System.UInt128) -> typing.List[int]:
        """
        Returns the specified 128-bit unsigned integer value as an array of bytes.
        
        :param value: The number to convert.
        :returns: An array of bytes with length 16.
        """
        ...

    @staticmethod
    @overload
    def get_bytes(value: System.Half) -> typing.List[int]:
        """
        Returns the specified half-precision floating point value as an array of bytes.
        
        :param value: The number to convert.
        :returns: An array of bytes with length 2.
        """
        ...

    @staticmethod
    @overload
    def get_bytes(value: float) -> typing.List[int]:
        """
        Returns the specified single-precision floating point value as an array of bytes.
        
        :param value: The number to convert.
        :returns: An array of bytes with length 4.
        """
        ...

    @staticmethod
    def half_to_int_16_bits(value: System.Half) -> int:
        """
        Converts the specified half-precision floating point number to a 16-bit signed integer.
        
        :param value: The number to convert.
        :returns: A 16-bit signed integer whose bits are identical to .
        """
        ...

    @staticmethod
    def half_to_u_int_16_bits(value: System.Half) -> int:
        """
        Converts the specified half-precision floating point number to a 16-bit unsigned integer.
        
        :param value: The number to convert.
        :returns: A 16-bit unsigned integer whose bits are identical to .
        """
        ...

    @staticmethod
    def int_16_bits_to_half(value: int) -> System.Half:
        """
        Converts the specified 16-bit signed integer to a half-precision floating point number.
        
        :param value: The number to convert.
        :returns: A half-precision floating point number whose bits are identical to .
        """
        ...

    @staticmethod
    def int_32_bits_to_single(value: int) -> float:
        """
        Converts the specified 32-bit signed integer to a single-precision floating point number.
        
        :param value: The number to convert.
        :returns: A single-precision floating point number whose bits are identical to .
        """
        ...

    @staticmethod
    def int_64_bits_to_double(value: int) -> float:
        """
        Converts the specified 64-bit signed integer to a double-precision floating point number.
        
        :param value: The number to convert.
        :returns: A double-precision floating point number whose bits are identical to .
        """
        ...

    @staticmethod
    def single_to_int_32_bits(value: float) -> int:
        """
        Converts the specified single-precision floating point number to a 32-bit signed integer.
        
        :param value: The number to convert.
        :returns: A 32-bit signed integer whose bits are identical to .
        """
        ...

    @staticmethod
    def single_to_u_int_32_bits(value: float) -> int:
        """
        Converts the specified single-precision floating point number to a 32-bit unsigned integer.
        
        :param value: The number to convert.
        :returns: A 32-bit unsigned integer whose bits are identical to .
        """
        ...

    @staticmethod
    @overload
    def to_boolean(value: typing.List[int], start_index: int) -> bool:
        """
        Returns a Boolean value converted from two bytes at a specified position in a byte array.
        
        :param value: A byte array.
        :param start_index: The index of the byte within .
        :returns: true if the byte at  is nonzero; otherwise false.
        """
        ...

    @staticmethod
    @overload
    def to_boolean(value: System.ReadOnlySpan[int]) -> bool:
        """
        Converts a read-only byte span into a Boolean value.
        
        :param value: A read-only span containing the bytes to convert.
        :returns: A Boolean representing the converted bytes.
        """
        ...

    @staticmethod
    @overload
    def to_char(value: typing.List[int], start_index: int) -> str:
        """
        Returns a Unicode character converted from two bytes at a specified position in a byte array.
        
        :param value: An array.
        :param start_index: The starting position within .
        :returns: A character formed by two bytes beginning at .
        """
        ...

    @staticmethod
    @overload
    def to_char(value: System.ReadOnlySpan[int]) -> str:
        """
        Converts a read-only byte span into a character.
        
        :param value: A read-only span containing the bytes to convert.
        :returns: A character representing the converted bytes.
        """
        ...

    @staticmethod
    @overload
    def to_double(value: typing.List[int], start_index: int) -> float:
        """
        Returns a double-precision floating point number converted from four bytes at a specified position in a byte array.
        
        :param value: An array of bytes.
        :param start_index: The starting position within .
        :returns: A double-precision floating point number formed by eight bytes beginning at .
        """
        ...

    @staticmethod
    @overload
    def to_double(value: System.ReadOnlySpan[int]) -> float:
        """
        Converts a read-only byte span into a double-precision floating-point value.
        
        :param value: A read-only span containing the bytes to convert.
        :returns: A double-precision floating-point value representing the converted bytes.
        """
        ...

    @staticmethod
    @overload
    def to_half(value: typing.List[int], start_index: int) -> System.Half:
        """
        Returns a half-precision floating point number converted from two bytes at a specified position in a byte array.
        
        :param value: An array of bytes.
        :param start_index: The starting position within .
        :returns: A half-precision floating point number signed integer formed by two bytes beginning at .
        """
        ...

    @staticmethod
    @overload
    def to_half(value: System.ReadOnlySpan[int]) -> System.Half:
        """
        Converts a read-only byte span into a half-precision floating-point value.
        
        :param value: A read-only span containing the bytes to convert.
        :returns: A half-precision floating-point value representing the converted bytes.
        """
        ...

    @staticmethod
    @overload
    def to_int_128(value: typing.List[int], start_index: int) -> System.Int128:
        """
        Returns a 128-bit signed integer converted from sixteen bytes at a specified position in a byte array.
        
        :param value: An array of bytes.
        :param start_index: The starting position within .
        :returns: A 128-bit signed integer formed by sixteen bytes beginning at .
        """
        ...

    @staticmethod
    @overload
    def to_int_128(value: System.ReadOnlySpan[int]) -> System.Int128:
        """
        Converts a read-only byte span into a 128-bit signed integer.
        
        :param value: A read-only span containing the bytes to convert.
        :returns: A 128-bit signed integer representing the converted bytes.
        """
        ...

    @staticmethod
    @overload
    def to_int_16(value: typing.List[int], start_index: int) -> int:
        """
        Returns a 16-bit signed integer converted from two bytes at a specified position in a byte array.
        
        :param value: An array of bytes.
        :param start_index: The starting position within .
        :returns: A 16-bit signed integer formed by two bytes beginning at .
        """
        ...

    @staticmethod
    @overload
    def to_int_16(value: System.ReadOnlySpan[int]) -> int:
        """
        Converts a read-only byte span into a 16-bit signed integer.
        
        :param value: A read-only span containing the bytes to convert.
        :returns: A 16-bit signed integer representing the converted bytes.
        """
        ...

    @staticmethod
    @overload
    def to_int_32(value: typing.List[int], start_index: int) -> int:
        """
        Returns a 32-bit signed integer converted from four bytes at a specified position in a byte array.
        
        :param value: An array of bytes.
        :param start_index: The starting position within .
        :returns: A 32-bit signed integer formed by four bytes beginning at .
        """
        ...

    @staticmethod
    @overload
    def to_int_32(value: System.ReadOnlySpan[int]) -> int:
        """
        Converts a read-only byte span into a 32-bit signed integer.
        
        :param value: A read-only span containing the bytes to convert.
        :returns: A 32-bit signed integer representing the converted bytes.
        """
        ...

    @staticmethod
    @overload
    def to_int_64(value: typing.List[int], start_index: int) -> int:
        """
        Returns a 64-bit signed integer converted from eight bytes at a specified position in a byte array.
        
        :param value: An array of bytes.
        :param start_index: The starting position within .
        :returns: A 64-bit signed integer formed by eight bytes beginning at .
        """
        ...

    @staticmethod
    @overload
    def to_int_64(value: System.ReadOnlySpan[int]) -> int:
        """
        Converts a read-only byte span into a 64-bit signed integer.
        
        :param value: A read-only span containing the bytes to convert.
        :returns: A 64-bit signed integer representing the converted bytes.
        """
        ...

    @staticmethod
    @overload
    def to_single(value: typing.List[int], start_index: int) -> float:
        """
        Returns a single-precision floating point number converted from four bytes at a specified position in a byte array.
        
        :param value: An array of bytes.
        :param start_index: The starting position within .
        :returns: A single-precision floating point number formed by four bytes beginning at .
        """
        ...

    @staticmethod
    @overload
    def to_single(value: System.ReadOnlySpan[int]) -> float:
        """
        Converts a read-only byte span into a single-precision floating-point value.
        
        :param value: A read-only span containing the bytes to convert.
        :returns: A single-precision floating-point value representing the converted bytes.
        """
        ...

    @staticmethod
    @overload
    def to_string(value: typing.List[int], start_index: int, length: int) -> str:
        """
        Converts the numeric value of each element of a specified array of bytes
        to its equivalent hexadecimal string representation.
        
        :param value: An array of bytes.
        :param start_index: The starting position within .
        :param length: The number of array elements in  to convert.
        :returns: A string of hexadecimal pairs separated by hyphens, where each pair represents the corresponding element in a subarray of ; for example, "7F-2C-4A-00".
        """
        ...

    @staticmethod
    @overload
    def to_string(value: typing.List[int]) -> str:
        """
        Converts the numeric value of each element of a specified array of bytes
        to its equivalent hexadecimal string representation.
        
        :param value: An array of bytes.
        :returns: A string of hexadecimal pairs separated by hyphens, where each pair represents the corresponding element in ; for example, "7F-2C-4A-00".
        """
        ...

    @staticmethod
    @overload
    def to_string(value: typing.List[int], start_index: int) -> str:
        """
        Converts the numeric value of each element of a specified array of bytes
        to its equivalent hexadecimal string representation.
        
        :param value: An array of bytes.
        :param start_index: The starting position within .
        :returns: A string of hexadecimal pairs separated by hyphens, where each pair represents the corresponding element in a subarray of ; for example, "7F-2C-4A-00".
        """
        ...

    @staticmethod
    @overload
    def to_u_int_128(value: typing.List[int], start_index: int) -> System.UInt128:
        """
        Returns a 128-bit unsigned integer converted from four bytes at a specified position in a byte array.
        
        :param value: An array of bytes.
        :param start_index: The starting position within .
        :returns: A 128-bit unsigned integer formed by sixteen bytes beginning at .
        """
        ...

    @staticmethod
    @overload
    def to_u_int_128(value: System.ReadOnlySpan[int]) -> System.UInt128:
        """
        Converts a read-only byte span into a 128-bit unsigned integer.
        
        :param value: A read-only span containing the bytes to convert.
        :returns: A 128-bit unsigned integer representing the converted bytes.
        """
        ...

    @staticmethod
    @overload
    def to_u_int_16(value: typing.List[int], start_index: int) -> int:
        """
        Returns a 16-bit unsigned integer converted from two bytes at a specified position in a byte array.
        
        :param value: An array of bytes.
        :param start_index: The starting position within .
        :returns: A 16-bit unsigned integer formed by two bytes beginning at .
        """
        ...

    @staticmethod
    @overload
    def to_u_int_16(value: System.ReadOnlySpan[int]) -> int:
        """
        Converts a read-only byte span into a 16-bit unsigned integer.
        
        :param value: A read-only span containing the bytes to convert.
        :returns: A 16-bit unsigned integer representing the converted bytes.
        """
        ...

    @staticmethod
    @overload
    def to_u_int_32(value: typing.List[int], start_index: int) -> int:
        """
        Returns a 32-bit unsigned integer converted from four bytes at a specified position in a byte array.
        
        :param value: An array of bytes.
        :param start_index: The starting position within .
        :returns: A 32-bit unsigned integer formed by four bytes beginning at .
        """
        ...

    @staticmethod
    @overload
    def to_u_int_32(value: System.ReadOnlySpan[int]) -> int:
        """
        Converts a read-only byte span into a 32-bit unsigned integer.
        
        :param value: A read-only span containing the bytes to convert.
        :returns: A 32-bit unsigned integer representing the converted bytes.
        """
        ...

    @staticmethod
    @overload
    def to_u_int_64(value: typing.List[int], start_index: int) -> int:
        """
        Returns a 64-bit unsigned integer converted from four bytes at a specified position in a byte array.
        
        :param value: An array of bytes.
        :param start_index: The starting position within .
        :returns: A 64-bit unsigned integer formed by eight bytes beginning at .
        """
        ...

    @staticmethod
    @overload
    def to_u_int_64(value: System.ReadOnlySpan[int]) -> int:
        """
        Converts a read-only byte span into a 64-bit unsigned integer.
        
        :param value: A read-only span containing the bytes to convert.
        :returns: A 64-bit unsigned integer representing the converted bytes.
        """
        ...

    @staticmethod
    @overload
    def try_write_bytes(destination: System.Span[int], value: bool) -> bool:
        """
        Converts a Boolean into a span of bytes.
        
        :param destination: When this method returns, the bytes representing the converted Boolean.
        :param value: The Boolean to convert.
        :returns: true if the conversion was successful; false otherwise.
        """
        ...

    @staticmethod
    @overload
    def try_write_bytes(destination: System.Span[int], value: str) -> bool:
        """
        Converts a character into a span of bytes.
        
        :param destination: When this method returns, the bytes representing the converted character.
        :param value: The character to convert.
        :returns: true if the conversion was successful; false otherwise.
        """
        ...

    @staticmethod
    @overload
    def try_write_bytes(destination: System.Span[int], value: int) -> bool:
        """
        Converts a 16-bit signed integer into a span of bytes.
        
        :param destination: When this method returns, the bytes representing the converted 16-bit signed integer.
        :param value: The 16-bit signed integer to convert.
        :returns: true if the conversion was successful; false otherwise.
        """
        ...

    @staticmethod
    @overload
    def try_write_bytes(destination: System.Span[int], value: System.Int128) -> bool:
        """
        Converts a 128-bit signed integer into a span of bytes.
        
        :param destination: When this method returns, the bytes representing the converted 128-bit signed integer.
        :param value: The 128-bit signed integer to convert.
        :returns: true if the conversion was successful; false otherwise.
        """
        ...

    @staticmethod
    @overload
    def try_write_bytes(destination: System.Span[int], value: System.UInt128) -> bool:
        """
        Converts a 128-bit unsigned integer into a span of bytes.
        
        :param destination: When this method returns, the bytes representing the converted 128-bit unsigned integer.
        :param value: The 128-bit unsigned integer to convert.
        :returns: true if the conversion was successful; false otherwise.
        """
        ...

    @staticmethod
    @overload
    def try_write_bytes(destination: System.Span[int], value: System.Half) -> bool:
        """
        Converts a half-precision floating-point value into a span of bytes.
        
        :param destination: When this method returns, the bytes representing the converted half-precision floating-point value.
        :param value: The half-precision floating-point value to convert.
        :returns: true if the conversion was successful; false otherwise.
        """
        ...

    @staticmethod
    @overload
    def try_write_bytes(destination: System.Span[int], value: float) -> bool:
        """
        Converts a single-precision floating-point value into a span of bytes.
        
        :param destination: When this method returns, the bytes representing the converted single-precision floating-point value.
        :param value: The single-precision floating-point value to convert.
        :returns: true if the conversion was successful; false otherwise.
        """
        ...

    @staticmethod
    def u_int_16_bits_to_half(value: int) -> System.Half:
        """
        Converts the specified 16-bit unsigned integer to a half-precision floating point number.
        
        :param value: The number to convert.
        :returns: A half-precision floating point number whose bits are identical to .
        """
        ...

    @staticmethod
    def u_int_32_bits_to_single(value: int) -> float:
        """
        Converts the specified 32-bit unsigned integer to a single-precision floating point number.
        
        :param value: The number to convert.
        :returns: A single-precision floating point number whose bits are identical to .
        """
        ...

    @staticmethod
    def u_int_64_bits_to_double(value: int) -> float:
        """
        Converts the specified 64-bit unsigned integer to a double-precision floating point number.
        
        :param value: The number to convert.
        :returns: A double-precision floating point number whose bits are identical to .
        """
        ...


class RankException(System.SystemException):
    """The exception that is thrown when an array with the wrong number of dimensions is passed to a method."""

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


class OverflowException(System.ArithmeticException):
    """The exception that is thrown when an arithmetic, casting, or conversion operation in a checked context results in an overflow."""

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


class Progress(typing.Generic[System_Progress_T], System.Object, System.IProgress[System_Progress_T]):
    """Provides an IProgress{T} that invokes callbacks for each reported progress value."""

    @property
    def progress_changed(self) -> _EventContainer[typing.Callable[[System.Object, System_Progress_T], None], None]:
        """Raised for each reported progress value."""
        ...

    @progress_changed.setter
    def progress_changed(self, value: _EventContainer[typing.Callable[[System.Object, System_Progress_T], None], None]) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """Initializes the Progress{T}."""
        ...

    @overload
    def __init__(self, handler: typing.Callable[[System_Progress_T], None]) -> None:
        """
        Initializes the Progress{T} with the specified callback.
        
        :param handler: A handler to invoke for each reported progress value.  This handler will be invoked in addition to any delegates registered with the ProgressChanged event. Depending on the SynchronizationContext instance captured by the Progress{T} at construction, it's possible that this handler instance could be invoked concurrently with itself.
        """
        ...

    def on_report(self, value: System_Progress_T) -> None:
        """
        Reports a progress change.
        
        This method is protected.
        
        :param value: The value of the updated progress.
        """
        ...


class ISpanParsable(typing.Generic[System_ISpanParsable_TSelf], System.IParsable[System_ISpanParsable_TSelf], metaclass=abc.ABCMeta):
    """Defines a mechanism for parsing a span of characters to a value."""


class AppDomainUnloadedException(System.SystemException):
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


class ContextBoundObject(System.MarshalByRefObject, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def __init__(self) -> None:
        """This method is protected."""
        ...


class ContextMarshalException(System.SystemException):
    """This class has no documentation."""

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
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """
        This method is protected.
        
        Obsoletions.LegacyFormatterImplMessage
        """
        ...


class ContextStaticAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class IndexOutOfRangeException(System.SystemException):
    """The exception that is thrown when an attempt is made to access an element of an array or collection with an index that is outside its bounds."""

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, message: str) -> None:
        ...

    @overload
    def __init__(self, message: str, inner_exception: System.Exception) -> None:
        ...


class AggregateException(System.Exception):
    """Represents one or more errors that occur during application execution."""

    @property
    def inner_exceptions(self) -> System.Collections.ObjectModel.ReadOnlyCollection[System.Exception]:
        """
        Gets a read-only collection of the Exception instances that caused the
        current exception.
        """
        ...

    @property
    def message(self) -> str:
        """Gets a message that describes the exception."""
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the AggregateException class."""
        ...

    @overload
    def __init__(self, message: str) -> None:
        """
        Initializes a new instance of the AggregateException class with
        a specified error message.
        
        :param message: The error message that explains the reason for the exception.
        """
        ...

    @overload
    def __init__(self, message: str, inner_exception: System.Exception) -> None:
        """
        Initializes a new instance of the AggregateException class with a specified error
        message and a reference to the inner exception that is the cause of this exception.
        
        :param message: The error message that explains the reason for the exception.
        :param inner_exception: The exception that is the cause of the current exception.
        """
        ...

    @overload
    def __init__(self, inner_exceptions: System.Collections.Generic.IEnumerable[System.Exception]) -> None:
        """
        Initializes a new instance of the AggregateException class with
        references to the inner exceptions that are the cause of this exception.
        
        :param inner_exceptions: The exceptions that are the cause of the current exception.
        """
        ...

    @overload
    def __init__(self, *inner_exceptions: typing.Union[System.Exception, typing.Iterable[System.Exception]]) -> None:
        """
        Initializes a new instance of the AggregateException class with
        references to the inner exceptions that are the cause of this exception.
        
        :param inner_exceptions: The exceptions that are the cause of the current exception.
        """
        ...

    @overload
    def __init__(self, message: str, inner_exceptions: System.Collections.Generic.IEnumerable[System.Exception]) -> None:
        """
        Initializes a new instance of the AggregateException class with a specified error
        message and references to the inner exceptions that are the cause of this exception.
        
        :param message: The error message that explains the reason for the exception.
        :param inner_exceptions: The exceptions that are the cause of the current exception.
        """
        ...

    @overload
    def __init__(self, message: str, *inner_exceptions: typing.Union[System.Exception, typing.Iterable[System.Exception]]) -> None:
        """
        Initializes a new instance of the AggregateException class with a specified error
        message and references to the inner exceptions that are the cause of this exception.
        
        :param message: The error message that explains the reason for the exception.
        :param inner_exceptions: The exceptions that are the cause of the current exception.
        """
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """
        Initializes a new instance of the AggregateException class with serialized data.
        
        This method is protected.
        
        Obsoletions.LegacyFormatterImplMessage
        
        :param info: The SerializationInfo that holds the serialized object data about the exception being thrown.
        :param context: The StreamingContext that contains contextual information about the source or destination.
        """
        ...

    def flatten(self) -> System.AggregateException:
        """
        Flattens the inner instances of AggregateException by expanding its contained Exception instances
        into a new AggregateException
        
        :returns: A new, flattened AggregateException.
        """
        ...

    def get_base_exception(self) -> System.Exception:
        """Returns the Exception that is the root cause of this exception."""
        ...

    def get_object_data(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """
        Sets the SerializationInfo with information about
        the exception.
        
        Obsoletions.LegacyFormatterImplMessage
        
        :param info: The SerializationInfo that holds the serialized object data about the exception being thrown.
        :param context: The StreamingContext that contains contextual information about the source or destination.
        """
        warnings.warn("Obsoletions.LegacyFormatterImplMessage", DeprecationWarning)

    def handle(self, predicate: typing.Callable[[System.Exception], bool]) -> None:
        """
        Invokes a handler on each Exception contained by this AggregateException.
        
        :param predicate: The predicate to execute for each exception. The predicate accepts as an argument the Exception to be processed and returns a Boolean to indicate whether the exception was handled.
        """
        ...

    def to_string(self) -> str:
        """
        Creates and returns a string representation of the current AggregateException.
        
        :returns: A string representation of the current exception.
        """
        ...


class Base64FormattingOptions(Enum):
    """This class has no documentation."""

    NONE = 0

    INSERT_LINE_BREAKS = 1


class Convert(System.Object):
    """This class has no documentation."""

    DB_NULL: System.Object = ...

    @staticmethod
    @overload
    def change_type(value: typing.Any, type_code: System.TypeCode) -> System.Object:
        ...

    @staticmethod
    @overload
    def change_type(value: typing.Any, type_code: System.TypeCode, provider: System.IFormatProvider) -> System.Object:
        ...

    @staticmethod
    @overload
    def change_type(value: typing.Any, conversion_type: typing.Type) -> System.Object:
        ...

    @staticmethod
    @overload
    def change_type(value: typing.Any, conversion_type: typing.Type, provider: System.IFormatProvider) -> System.Object:
        ...

    @staticmethod
    def from_base_64_char_array(in_array: typing.List[str], offset: int, length: int) -> typing.List[int]:
        """
        Converts the specified range of a Char array, which encodes binary data as Base64 digits, to the equivalent byte array.
        
        :param in_array: Chars representing Base64 encoding characters
        :param offset: A position within the input array.
        :param length: Number of element to convert.
        :returns: The array of bytes represented by the specified Base64 encoding characters.
        """
        ...

    @staticmethod
    def from_base_64_string(s: str) -> typing.List[int]:
        """
        Converts the specified string, which encodes binary data as Base64 digits, to the equivalent byte array.
        
        :param s: The string to convert
        :returns: The array of bytes represented by the specified Base64 string.
        """
        ...

    @staticmethod
    @overload
    def from_hex_string(s: str) -> typing.List[int]:
        """
        Converts the specified string, which encodes binary data as hex characters, to an equivalent 8-bit unsigned integer array.
        
        :param s: The string to convert.
        :returns: An array of 8-bit unsigned integers that is equivalent to .
        """
        ...

    @staticmethod
    @overload
    def from_hex_string(chars: System.ReadOnlySpan[str]) -> typing.List[int]:
        """
        Converts the span, which encodes binary data as hex characters, to an equivalent 8-bit unsigned integer array.
        
        :param chars: The span to convert.
        :returns: An array of 8-bit unsigned integers that is equivalent to .
        """
        ...

    @staticmethod
    @overload
    def from_hex_string(source: str, destination: System.Span[int], chars_consumed: typing.Optional[int], bytes_written: typing.Optional[int]) -> typing.Tuple[System.Buffers.OperationStatus, int, int]:
        """
        Converts the string, which encodes binary data as hex characters, to an equivalent 8-bit unsigned integer span.
        
        :param source: The string to convert.
        :param destination: The span in which to write the converted 8-bit unsigned integers. When this method returns value different than OperationStatus.Done, either the span remains unmodified or contains an incomplete conversion of , up to the last valid character.
        :param chars_consumed: When this method returns, contains the number of characters that were consumed from .
        :param bytes_written: When this method returns, contains the number of bytes that were written to .
        :returns: An OperationStatus describing the result of the operation.
        """
        ...

    @staticmethod
    @overload
    def from_hex_string(source: System.ReadOnlySpan[str], destination: System.Span[int], chars_consumed: typing.Optional[int], bytes_written: typing.Optional[int]) -> typing.Tuple[System.Buffers.OperationStatus, int, int]:
        """
        Converts the span of chars, which encodes binary data as hex characters, to an equivalent 8-bit unsigned integer span.
        
        :param source: The span to convert.
        :param destination: The span in which to write the converted 8-bit unsigned integers. When this method returns value different than OperationStatus.Done, either the span remains unmodified or contains an incomplete conversion of , up to the last valid character.
        :param chars_consumed: When this method returns, contains the number of characters that were consumed from .
        :param bytes_written: When this method returns, contains the number of bytes that were written to .
        :returns: An OperationStatus describing the result of the operation.
        """
        ...

    @staticmethod
    def get_type_code(value: typing.Any) -> System.TypeCode:
        ...

    @staticmethod
    def is_db_null(value: typing.Any) -> bool:
        ...

    @staticmethod
    @overload
    def to_base_64_char_array(in_array: typing.List[int], offset_in: int, length: int, out_array: typing.List[str], offset_out: int) -> int:
        ...

    @staticmethod
    @overload
    def to_base_64_char_array(in_array: typing.List[int], offset_in: int, length: int, out_array: typing.List[str], offset_out: int, options: System.Base64FormattingOptions) -> int:
        ...

    @staticmethod
    @overload
    def to_base_64_string(in_array: typing.List[int]) -> str:
        ...

    @staticmethod
    @overload
    def to_base_64_string(in_array: typing.List[int], options: System.Base64FormattingOptions) -> str:
        ...

    @staticmethod
    @overload
    def to_base_64_string(in_array: typing.List[int], offset: int, length: int) -> str:
        ...

    @staticmethod
    @overload
    def to_base_64_string(in_array: typing.List[int], offset: int, length: int, options: System.Base64FormattingOptions) -> str:
        ...

    @staticmethod
    @overload
    def to_base_64_string(bytes: System.ReadOnlySpan[int], options: System.Base64FormattingOptions = ...) -> str:
        ...

    @staticmethod
    @overload
    def to_boolean(value: typing.Any) -> bool:
        ...

    @staticmethod
    @overload
    def to_boolean(value: typing.Any, provider: System.IFormatProvider) -> bool:
        ...

    @staticmethod
    @overload
    def to_boolean(value: bool) -> bool:
        ...

    @staticmethod
    @overload
    def to_boolean(value: int) -> bool:
        ...

    @staticmethod
    @overload
    def to_boolean(value: str) -> bool:
        ...

    @staticmethod
    @overload
    def to_boolean(value: str, provider: System.IFormatProvider) -> bool:
        ...

    @staticmethod
    @overload
    def to_boolean(value: float) -> bool:
        ...

    @staticmethod
    @overload
    def to_boolean(value: typing.Union[datetime.datetime, datetime.date]) -> bool:
        ...

    @staticmethod
    @overload
    def to_byte(value: typing.Any) -> int:
        ...

    @staticmethod
    @overload
    def to_byte(value: typing.Any, provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def to_byte(value: bool) -> int:
        ...

    @staticmethod
    @overload
    def to_byte(value: int) -> int:
        ...

    @staticmethod
    @overload
    def to_byte(value: str) -> int:
        ...

    @staticmethod
    @overload
    def to_byte(value: float) -> int:
        ...

    @staticmethod
    @overload
    def to_byte(value: str, provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def to_byte(value: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    @staticmethod
    @overload
    def to_byte(value: str, from_base: int) -> int:
        ...

    @staticmethod
    @overload
    def to_char(value: typing.Any) -> str:
        ...

    @staticmethod
    @overload
    def to_char(value: typing.Any, provider: System.IFormatProvider) -> str:
        ...

    @staticmethod
    @overload
    def to_char(value: bool) -> str:
        ...

    @staticmethod
    @overload
    def to_char(value: str) -> str:
        ...

    @staticmethod
    @overload
    def to_char(value: int) -> str:
        ...

    @staticmethod
    @overload
    def to_char(value: str, provider: System.IFormatProvider) -> str:
        ...

    @staticmethod
    @overload
    def to_char(value: float) -> str:
        ...

    @staticmethod
    @overload
    def to_char(value: typing.Union[datetime.datetime, datetime.date]) -> str:
        ...

    @staticmethod
    @overload
    def to_date_time(value: typing.Any) -> datetime.datetime:
        ...

    @staticmethod
    @overload
    def to_date_time(value: typing.Any, provider: System.IFormatProvider) -> datetime.datetime:
        ...

    @staticmethod
    @overload
    def to_date_time(value: typing.Union[datetime.datetime, datetime.date]) -> datetime.datetime:
        ...

    @staticmethod
    @overload
    def to_date_time(value: str) -> datetime.datetime:
        ...

    @staticmethod
    @overload
    def to_date_time(value: str, provider: System.IFormatProvider) -> datetime.datetime:
        ...

    @staticmethod
    @overload
    def to_date_time(value: int) -> datetime.datetime:
        ...

    @staticmethod
    @overload
    def to_date_time(value: bool) -> datetime.datetime:
        ...

    @staticmethod
    @overload
    def to_date_time(value: float) -> datetime.datetime:
        ...

    @staticmethod
    @overload
    def to_decimal(value: typing.Any) -> float:
        ...

    @staticmethod
    @overload
    def to_decimal(value: typing.Any, provider: System.IFormatProvider) -> float:
        ...

    @staticmethod
    @overload
    def to_decimal(value: int) -> float:
        ...

    @staticmethod
    @overload
    def to_decimal(value: str) -> float:
        ...

    @staticmethod
    @overload
    def to_decimal(value: float) -> float:
        ...

    @staticmethod
    @overload
    def to_decimal(value: str, provider: System.IFormatProvider) -> float:
        ...

    @staticmethod
    @overload
    def to_decimal(value: bool) -> float:
        ...

    @staticmethod
    @overload
    def to_decimal(value: typing.Union[datetime.datetime, datetime.date]) -> float:
        ...

    @staticmethod
    @overload
    def to_double(value: typing.Any) -> float:
        ...

    @staticmethod
    @overload
    def to_double(value: typing.Any, provider: System.IFormatProvider) -> float:
        ...

    @staticmethod
    @overload
    def to_double(value: int) -> float:
        ...

    @staticmethod
    @overload
    def to_double(value: str) -> float:
        ...

    @staticmethod
    @overload
    def to_double(value: float) -> float:
        ...

    @staticmethod
    @overload
    def to_double(value: str, provider: System.IFormatProvider) -> float:
        ...

    @staticmethod
    @overload
    def to_double(value: bool) -> float:
        ...

    @staticmethod
    @overload
    def to_double(value: typing.Union[datetime.datetime, datetime.date]) -> float:
        ...

    @staticmethod
    @overload
    def to_hex_string(in_array: typing.List[int]) -> str:
        """
        Converts an array of 8-bit unsigned integers to its equivalent string representation that is encoded with uppercase hex characters.
        
        :param in_array: An array of 8-bit unsigned integers.
        :returns: The string representation in hex of the elements in .
        """
        ...

    @staticmethod
    @overload
    def to_hex_string(in_array: typing.List[int], offset: int, length: int) -> str:
        """
        Converts a subset of an array of 8-bit unsigned integers to its equivalent string representation that is encoded with uppercase hex characters.
        Parameters specify the subset as an offset in the input array and the number of elements in the array to convert.
        
        :param in_array: An array of 8-bit unsigned integers.
        :param offset: An offset in .
        :param length: The number of elements of  to convert.
        :returns: The string representation in hex of  elements of , starting at position .
        """
        ...

    @staticmethod
    @overload
    def to_hex_string(bytes: System.ReadOnlySpan[int]) -> str:
        """
        Converts a span of 8-bit unsigned integers to its equivalent string representation that is encoded with uppercase hex characters.
        
        :param bytes: A span of 8-bit unsigned integers.
        :returns: The string representation in hex of the elements in .
        """
        ...

    @staticmethod
    @overload
    def to_hex_string_lower(in_array: typing.List[int]) -> str:
        """
        Converts an array of 8-bit unsigned integers to its equivalent string representation that is encoded with lowercase hex characters.
        
        :param in_array: An array of 8-bit unsigned integers.
        :returns: The string representation in hex of the elements in .
        """
        ...

    @staticmethod
    @overload
    def to_hex_string_lower(in_array: typing.List[int], offset: int, length: int) -> str:
        """
        Converts a subset of an array of 8-bit unsigned integers to its equivalent string representation that is encoded with lowercase hex characters.
        Parameters specify the subset as an offset in the input array and the number of elements in the array to convert.
        
        :param in_array: An array of 8-bit unsigned integers.
        :param offset: An offset in .
        :param length: The number of elements of  to convert.
        :returns: The string representation in hex of  elements of , starting at position .
        """
        ...

    @staticmethod
    @overload
    def to_hex_string_lower(bytes: System.ReadOnlySpan[int]) -> str:
        """
        Converts a span of 8-bit unsigned integers to its equivalent string representation that is encoded with lowercase hex characters.
        
        :param bytes: A span of 8-bit unsigned integers.
        :returns: The string representation in hex of the elements in .
        """
        ...

    @staticmethod
    @overload
    def to_int_16(value: typing.Any) -> int:
        ...

    @staticmethod
    @overload
    def to_int_16(value: typing.Any, provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def to_int_16(value: bool) -> int:
        ...

    @staticmethod
    @overload
    def to_int_16(value: str) -> int:
        ...

    @staticmethod
    @overload
    def to_int_16(value: int) -> int:
        ...

    @staticmethod
    @overload
    def to_int_16(value: float) -> int:
        ...

    @staticmethod
    @overload
    def to_int_16(value: str, provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def to_int_16(value: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    @staticmethod
    @overload
    def to_int_16(value: str, from_base: int) -> int:
        ...

    @staticmethod
    @overload
    def to_int_32(value: typing.Any) -> int:
        ...

    @staticmethod
    @overload
    def to_int_32(value: typing.Any, provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def to_int_32(value: bool) -> int:
        ...

    @staticmethod
    @overload
    def to_int_32(value: str) -> int:
        ...

    @staticmethod
    @overload
    def to_int_32(value: int) -> int:
        ...

    @staticmethod
    @overload
    def to_int_32(value: float) -> int:
        ...

    @staticmethod
    @overload
    def to_int_32(value: str, provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def to_int_32(value: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    @staticmethod
    @overload
    def to_int_32(value: str, from_base: int) -> int:
        ...

    @staticmethod
    @overload
    def to_int_64(value: typing.Any) -> int:
        ...

    @staticmethod
    @overload
    def to_int_64(value: typing.Any, provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def to_int_64(value: bool) -> int:
        ...

    @staticmethod
    @overload
    def to_int_64(value: str) -> int:
        ...

    @staticmethod
    @overload
    def to_int_64(value: int) -> int:
        ...

    @staticmethod
    @overload
    def to_int_64(value: float) -> int:
        ...

    @staticmethod
    @overload
    def to_int_64(value: str, provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def to_int_64(value: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    @staticmethod
    @overload
    def to_int_64(value: str, from_base: int) -> int:
        ...

    @staticmethod
    @overload
    def to_s_byte(value: typing.Any) -> int:
        ...

    @staticmethod
    @overload
    def to_s_byte(value: typing.Any, provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def to_s_byte(value: bool) -> int:
        ...

    @staticmethod
    @overload
    def to_s_byte(value: int) -> int:
        ...

    @staticmethod
    @overload
    def to_s_byte(value: str) -> int:
        ...

    @staticmethod
    @overload
    def to_s_byte(value: float) -> int:
        ...

    @staticmethod
    @overload
    def to_s_byte(value: str, provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def to_s_byte(value: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    @staticmethod
    @overload
    def to_s_byte(value: str, from_base: int) -> int:
        ...

    @staticmethod
    @overload
    def to_single(value: typing.Any) -> float:
        ...

    @staticmethod
    @overload
    def to_single(value: typing.Any, provider: System.IFormatProvider) -> float:
        ...

    @staticmethod
    @overload
    def to_single(value: int) -> float:
        ...

    @staticmethod
    @overload
    def to_single(value: str) -> float:
        ...

    @staticmethod
    @overload
    def to_single(value: float) -> float:
        ...

    @staticmethod
    @overload
    def to_single(value: str, provider: System.IFormatProvider) -> float:
        ...

    @staticmethod
    @overload
    def to_single(value: bool) -> float:
        ...

    @staticmethod
    @overload
    def to_single(value: typing.Union[datetime.datetime, datetime.date]) -> float:
        ...

    @staticmethod
    @overload
    def to_string(value: typing.Any) -> str:
        ...

    @staticmethod
    @overload
    def to_string(value: typing.Any, provider: System.IFormatProvider) -> str:
        ...

    @staticmethod
    @overload
    def to_string(value: bool) -> str:
        ...

    @staticmethod
    @overload
    def to_string(value: bool, provider: System.IFormatProvider) -> str:
        ...

    @staticmethod
    @overload
    def to_string(value: str) -> str:
        ...

    @staticmethod
    @overload
    def to_string(value: str, provider: System.IFormatProvider) -> str:
        ...

    @staticmethod
    @overload
    def to_string(value: int) -> str:
        ...

    @staticmethod
    @overload
    def to_string(value: int, provider: System.IFormatProvider) -> str:
        ...

    @staticmethod
    @overload
    def to_string(value: float) -> str:
        ...

    @staticmethod
    @overload
    def to_string(value: float, provider: System.IFormatProvider) -> str:
        ...

    @staticmethod
    @overload
    def to_string(value: typing.Union[datetime.datetime, datetime.date]) -> str:
        ...

    @staticmethod
    @overload
    def to_string(value: typing.Union[datetime.datetime, datetime.date], provider: System.IFormatProvider) -> str:
        ...

    @staticmethod
    @overload
    def to_string(value: int, to_base: int) -> str:
        ...

    @staticmethod
    @overload
    def to_u_int_16(value: typing.Any) -> int:
        ...

    @staticmethod
    @overload
    def to_u_int_16(value: typing.Any, provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def to_u_int_16(value: bool) -> int:
        ...

    @staticmethod
    @overload
    def to_u_int_16(value: str) -> int:
        ...

    @staticmethod
    @overload
    def to_u_int_16(value: int) -> int:
        ...

    @staticmethod
    @overload
    def to_u_int_16(value: float) -> int:
        ...

    @staticmethod
    @overload
    def to_u_int_16(value: str, provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def to_u_int_16(value: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    @staticmethod
    @overload
    def to_u_int_16(value: str, from_base: int) -> int:
        ...

    @staticmethod
    @overload
    def to_u_int_32(value: typing.Any) -> int:
        ...

    @staticmethod
    @overload
    def to_u_int_32(value: typing.Any, provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def to_u_int_32(value: bool) -> int:
        ...

    @staticmethod
    @overload
    def to_u_int_32(value: str) -> int:
        ...

    @staticmethod
    @overload
    def to_u_int_32(value: int) -> int:
        ...

    @staticmethod
    @overload
    def to_u_int_32(value: float) -> int:
        ...

    @staticmethod
    @overload
    def to_u_int_32(value: str, provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def to_u_int_32(value: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    @staticmethod
    @overload
    def to_u_int_32(value: str, from_base: int) -> int:
        ...

    @staticmethod
    @overload
    def to_u_int_64(value: typing.Any) -> int:
        ...

    @staticmethod
    @overload
    def to_u_int_64(value: typing.Any, provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def to_u_int_64(value: bool) -> int:
        ...

    @staticmethod
    @overload
    def to_u_int_64(value: str) -> int:
        ...

    @staticmethod
    @overload
    def to_u_int_64(value: int) -> int:
        ...

    @staticmethod
    @overload
    def to_u_int_64(value: float) -> int:
        ...

    @staticmethod
    @overload
    def to_u_int_64(value: str, provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def to_u_int_64(value: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    @staticmethod
    @overload
    def to_u_int_64(value: str, from_base: int) -> int:
        ...

    @staticmethod
    def try_from_base_64_chars(chars: System.ReadOnlySpan[str], bytes: System.Span[int], bytes_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    def try_from_base_64_string(s: str, bytes: System.Span[int], bytes_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    def try_to_base_64_chars(bytes: System.ReadOnlySpan[int], chars: System.Span[str], chars_written: typing.Optional[int], options: System.Base64FormattingOptions = ...) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    def try_to_hex_string(source: System.ReadOnlySpan[int], destination: System.Span[str], chars_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        """
        Converts a span of 8-bit unsigned integers to its equivalent span representation that is encoded with uppercase hex characters.
        
        :param source: A span of 8-bit unsigned integers.
        :param destination: The span representation in hex of the elements in .
        :param chars_written: When this method returns, contains the number of chars that were written in .
        :returns: true if the conversion was successful; otherwise, false.
        """
        ...

    @staticmethod
    def try_to_hex_string_lower(source: System.ReadOnlySpan[int], destination: System.Span[str], chars_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        """
        Converts a span of 8-bit unsigned integers to its equivalent span representation that is encoded with lowercase hex characters.
        
        :param source: A span of 8-bit unsigned integers.
        :param destination: The span representation in hex of the elements in .
        :param chars_written: When this method returns, contains the number of chars that were written in .
        :returns: true if the conversion was successful; otherwise, false.
        """
        ...


class FlagsAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class UnauthorizedAccessException(System.SystemException):
    """The exception that is thrown when the operating system denies access because of an I/O error or a specific type of security error."""

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
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """
        This method is protected.
        
        Obsoletions.LegacyFormatterImplMessage
        """
        ...


class ArgumentOutOfRangeException(System.ArgumentException):
    """The exception that is thrown when the value of an argument is outside the allowable range of values as defined by the invoked method."""

    @property
    def message(self) -> str:
        ...

    @property
    def actual_value(self) -> System.Object:
        ...

    @overload
    def __init__(self, param_name: str, actual_value: typing.Any, message: str) -> None:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, param_name: str) -> None:
        ...

    @overload
    def __init__(self, param_name: str, message: str) -> None:
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

    def get_object_data(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """Obsoletions.LegacyFormatterImplMessage"""
        warnings.warn("Obsoletions.LegacyFormatterImplMessage", DeprecationWarning)


class CLSCompliantAttribute(System.Attribute):
    """Indicates whether a program element is compliant with the Common Language Specification (CLS)."""

    @property
    def is_compliant(self) -> bool:
        ...

    def __init__(self, is_compliant: bool) -> None:
        ...


class Delegate(System.Object, System.ICloneable, System.Runtime.Serialization.ISerializable, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    class InvocationListEnumerator(typing.Generic[System_Delegate_InvocationListEnumerator_TDelegate], typing.Iterable[System_Delegate_InvocationListEnumerator_TDelegate]):
        """Provides an enumerator for the invocation list of a delegate."""

        @property
        def current(self) -> System_Delegate_InvocationListEnumerator_TDelegate:
            """Implements the IEnumerator pattern."""
            ...

        def __iter__(self) -> typing.Iterator[System_Delegate_InvocationListEnumerator_TDelegate]:
            ...

        def get_enumerator(self) -> System.Delegate.InvocationListEnumerator[System_Delegate_InvocationListEnumerator_TDelegate]:
            """
            Implement IEnumerable.GetEnumerator() to return 'this' as the IEnumerator.
            
            :returns: An IEnumerator instance that can be used to iterate through the invocation targets of the delegate.
            """
            ...

        def move_next(self) -> bool:
            """
            Implements the IEnumerator pattern.
            
            :returns: true if the enumerator was successfully advanced to the next element; otherwise, false if the enumerator has passed the end of the collection.
            """
            ...

    @property
    def has_single_target(self) -> bool:
        """Gets a value that indicates whether the Delegate has a single invocation target."""
        ...

    @property
    def method(self) -> System.Reflection.MethodInfo:
        ...

    @property
    def target(self) -> System.Object:
        ...

    def __eq__(self, d_2: System.Delegate) -> bool:
        ...

    @overload
    def __init__(self, target: typing.Any, method: str) -> None:
        """This method is protected."""
        ...

    @overload
    def __init__(self, target: typing.Type, method: str) -> None:
        """This method is protected."""
        ...

    def __ne__(self, d_2: System.Delegate) -> bool:
        ...

    def clone(self) -> System.Object:
        ...

    @staticmethod
    @overload
    def combine(a: System.Delegate, b: System.Delegate) -> System.Delegate:
        ...

    @staticmethod
    @overload
    def combine(*delegates: typing.Union[System.Delegate, typing.Iterable[System.Delegate]]) -> System.Delegate:
        ...

    def combine_impl(self, d: System.Delegate) -> System.Delegate:
        """This method is protected."""
        ...

    @staticmethod
    @overload
    def create_delegate(type: typing.Type, first_argument: typing.Any, method: System.Reflection.MethodInfo) -> System.Delegate:
        ...

    @staticmethod
    @overload
    def create_delegate(type: typing.Type, target: typing.Any, method: str) -> System.Delegate:
        ...

    @staticmethod
    @overload
    def create_delegate(type: typing.Type, target: typing.Any, method: str, ignore_case: bool) -> System.Delegate:
        ...

    @staticmethod
    @overload
    def create_delegate(type: typing.Type, first_argument: typing.Any, method: System.Reflection.MethodInfo, throw_on_bind_failure: bool) -> System.Delegate:
        ...

    @staticmethod
    @overload
    def create_delegate(type: typing.Type, target: typing.Any, method: str, ignore_case: bool, throw_on_bind_failure: bool) -> System.Delegate:
        ...

    @staticmethod
    @overload
    def create_delegate(type: typing.Type, method: System.Reflection.MethodInfo) -> System.Delegate:
        ...

    @staticmethod
    @overload
    def create_delegate(type: typing.Type, target: typing.Type, method: str) -> System.Delegate:
        ...

    @staticmethod
    @overload
    def create_delegate(type: typing.Type, target: typing.Type, method: str, ignore_case: bool) -> System.Delegate:
        ...

    @staticmethod
    @overload
    def create_delegate(type: typing.Type, method: System.Reflection.MethodInfo, throw_on_bind_failure: bool) -> System.Delegate:
        ...

    @staticmethod
    @overload
    def create_delegate(type: typing.Type, target: typing.Type, method: str, ignore_case: bool, throw_on_bind_failure: bool) -> System.Delegate:
        ...

    def dynamic_invoke(self, *args: typing.Union[System.Object, typing.Iterable[System.Object]]) -> System.Object:
        ...

    def dynamic_invoke_impl(self, args: typing.List[System.Object]) -> System.Object:
        """This method is protected."""
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def get_invocation_list(self) -> typing.List[System.Delegate]:
        ...

    def get_method_impl(self) -> System.Reflection.MethodInfo:
        """This method is protected."""
        ...

    def get_object_data(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """Obsoletions.LegacyFormatterImplMessage"""
        warnings.warn("Obsoletions.LegacyFormatterImplMessage", DeprecationWarning)

    @staticmethod
    def remove(source: System.Delegate, value: System.Delegate) -> System.Delegate:
        ...

    @staticmethod
    def remove_all(source: System.Delegate, value: System.Delegate) -> System.Delegate:
        ...

    def remove_impl(self, d: System.Delegate) -> System.Delegate:
        """This method is protected."""
        ...


class IAsyncDisposable(metaclass=abc.ABCMeta):
    """Provides a mechanism for releasing unmanaged resources asynchronously."""

    def dispose_async(self) -> System.Threading.Tasks.ValueTask:
        """
        Performs application-defined tasks associated with freeing, releasing, or
        resetting unmanaged resources asynchronously.
        """
        ...


class UInt16(System.IComparable[int], System.IConvertible, System.ISpanFormattable, System.IEquatable[int], System.Numerics.IUnsignedNumber[int], System.IUtf8SpanFormattable, System.IBinaryIntegerParseAndFormatInfo[int]):
    """This class has no documentation."""

    MAX_VALUE: int = ...

    MIN_VALUE: int = 0

    @overload
    def __ge__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __ge__(self, other: int) -> bool:
        ...

    @overload
    def __gt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __gt__(self, other: int) -> bool:
        ...

    @overload
    def __le__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __le__(self, other: int) -> bool:
        ...

    @overload
    def __lt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __lt__(self, other: int) -> bool:
        ...

    @staticmethod
    def clamp(value: int, min: int, max: int) -> int:
        ...

    @overload
    def compare_to(self, value: typing.Any) -> int:
        ...

    @overload
    def compare_to(self, value: int) -> int:
        ...

    @staticmethod
    def div_rem(left: int, right: int) -> System.ValueTuple[int, int]:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, obj: int) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def get_type_code(self) -> System.TypeCode:
        ...

    @staticmethod
    def is_even_integer(value: int) -> bool:
        ...

    @staticmethod
    def is_odd_integer(value: int) -> bool:
        ...

    @staticmethod
    def is_pow_2(value: int) -> bool:
        ...

    @staticmethod
    def leading_zero_count(value: int) -> int:
        ...

    @staticmethod
    def log_2(value: int) -> int:
        ...

    @staticmethod
    def max(x: int, y: int) -> int:
        ...

    @staticmethod
    def min(x: int, y: int) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: str) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: str, style: System.Globalization.NumberStyles) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: str, provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: str, style: System.Globalization.NumberStyles, provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int], style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> int:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int], provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    def pop_count(value: int) -> int:
        ...

    @staticmethod
    def rotate_left(value: int, rotate_amount: int) -> int:
        ...

    @staticmethod
    def rotate_right(value: int, rotate_amount: int) -> int:
        ...

    @staticmethod
    def sign(value: int) -> int:
        ...

    @overload
    def to_string(self) -> str:
        ...

    @overload
    def to_string(self, provider: System.IFormatProvider) -> str:
        ...

    @overload
    def to_string(self, format: str) -> str:
        ...

    @overload
    def to_string(self, format: str, provider: System.IFormatProvider) -> str:
        ...

    @staticmethod
    def trailing_zero_count(value: int) -> int:
        ...

    @overload
    def try_format(self, destination: System.Span[str], chars_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @overload
    def try_format(self, utf_8_destination: System.Span[int], bytes_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        """
        Tries to convert a UTF-8 character span containing the string representation of a number to its 16-bit unsigned integer equivalent.
        
        :param utf_8_text: A span containing the UTF-8 characters representing the number to convert.
        :param result: When this method returns, contains the 16-bit unsigned integer value equivalent to the number contained in  if the conversion succeeded, or zero if the conversion failed. This parameter is passed uninitialized; any value originally supplied in result will be overwritten.
        :returns: true if  was converted successfully; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def try_parse(s: str, style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...


class PlatformNotSupportedException(System.NotSupportedException):
    """The exception that is thrown when a feature is not supported on the current platform."""

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
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """
        This method is protected.
        
        Obsoletions.LegacyFormatterImplMessage
        """
        ...


class AccessViolationException(System.SystemException):
    """The exception that is thrown when there is an attempt to read or write protected memory."""

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


class MathF(System.Object):
    """Provides constants and static methods for trigonometric, logarithmic, and other common mathematical functions."""

    E: float = ...

    PI: float = ...

    TAU: float = ...

    @staticmethod
    def abs(x: float) -> float:
        ...

    @staticmethod
    def acos(x: float) -> float:
        ...

    @staticmethod
    def acosh(x: float) -> float:
        ...

    @staticmethod
    def asin(x: float) -> float:
        ...

    @staticmethod
    def asinh(x: float) -> float:
        ...

    @staticmethod
    def atan(x: float) -> float:
        ...

    @staticmethod
    def atan_2(y: float, x: float) -> float:
        ...

    @staticmethod
    def atanh(x: float) -> float:
        ...

    @staticmethod
    def bit_decrement(x: float) -> float:
        ...

    @staticmethod
    def bit_increment(x: float) -> float:
        ...

    @staticmethod
    def cbrt(x: float) -> float:
        ...

    @staticmethod
    def ceiling(x: float) -> float:
        ...

    @staticmethod
    def copy_sign(x: float, y: float) -> float:
        ...

    @staticmethod
    def cos(x: float) -> float:
        ...

    @staticmethod
    def cosh(x: float) -> float:
        ...

    @staticmethod
    def exp(x: float) -> float:
        ...

    @staticmethod
    def floor(x: float) -> float:
        ...

    @staticmethod
    def fused_multiply_add(x: float, y: float, z: float) -> float:
        ...

    @staticmethod
    def ieee_remainder(x: float, y: float) -> float:
        ...

    @staticmethod
    def i_log_b(x: float) -> int:
        ...

    @staticmethod
    @overload
    def log(x: float, y: float) -> float:
        ...

    @staticmethod
    @overload
    def log(x: float) -> float:
        ...

    @staticmethod
    def log_10(x: float) -> float:
        ...

    @staticmethod
    def log_2(x: float) -> float:
        ...

    @staticmethod
    def max(x: float, y: float) -> float:
        ...

    @staticmethod
    def max_magnitude(x: float, y: float) -> float:
        ...

    @staticmethod
    def min(x: float, y: float) -> float:
        ...

    @staticmethod
    def min_magnitude(x: float, y: float) -> float:
        ...

    @staticmethod
    def pow(x: float, y: float) -> float:
        ...

    @staticmethod
    def reciprocal_estimate(x: float) -> float:
        """
        Returns an estimate of the reciprocal of a specified number.
        
        :param x: The number whose reciprocal is to be estimated.
        :returns: An estimate of the reciprocal of .
        """
        ...

    @staticmethod
    def reciprocal_sqrt_estimate(x: float) -> float:
        """
        Returns an estimate of the reciprocal square root of a specified number.
        
        :param x: The number whose reciprocal square root is to be estimated.
        :returns: An estimate of the reciprocal square root .
        """
        ...

    @staticmethod
    @overload
    def round(x: float) -> float:
        ...

    @staticmethod
    @overload
    def round(x: float, digits: int) -> float:
        ...

    @staticmethod
    @overload
    def round(x: float, mode: System.MidpointRounding) -> float:
        ...

    @staticmethod
    @overload
    def round(x: float, digits: int, mode: System.MidpointRounding) -> float:
        ...

    @staticmethod
    def scale_b(x: float, n: int) -> float:
        ...

    @staticmethod
    def sign(x: float) -> int:
        ...

    @staticmethod
    def sin(x: float) -> float:
        ...

    @staticmethod
    def sin_cos(x: float) -> System.ValueTuple[float, float]:
        ...

    @staticmethod
    def sinh(x: float) -> float:
        ...

    @staticmethod
    def sqrt(x: float) -> float:
        ...

    @staticmethod
    def tan(x: float) -> float:
        ...

    @staticmethod
    def tanh(x: float) -> float:
        ...

    @staticmethod
    def truncate(x: float) -> float:
        ...


class ArrayTypeMismatchException(System.SystemException):
    """The exception that is thrown when an attempt is made to store an element of the wrong type within an array."""

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


class TypeUnloadedException(System.SystemException):
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


class InvalidProgramException(System.SystemException):
    """
    The exception that is thrown when a program contains invalid IL or metadata.
    This exception is also thrown when internal runtime implementation limits have been exceeded by the program.
    """

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, message: str) -> None:
        ...

    @overload
    def __init__(self, message: str, inner: System.Exception) -> None:
        ...


class Tuple(typing.Generic[System_Tuple_T1, System_Tuple_T2, System_Tuple_T3, System_Tuple_T4, System_Tuple_T5, System_Tuple_T6, System_Tuple_T7, System_Tuple_TRest], System.Object, System.Collections.IStructuralEquatable, System.Collections.IStructuralComparable, System.IComparable, System.ITupleInternal):
    """This class has no documentation."""

    @property
    def item_1(self) -> System_Tuple_T1:
        ...

    @property
    def item_2(self) -> System_Tuple_T2:
        ...

    @property
    def item_3(self) -> System_Tuple_T3:
        ...

    @property
    def item_4(self) -> System_Tuple_T4:
        ...

    @property
    def item_5(self) -> System_Tuple_T5:
        ...

    @property
    def item_6(self) -> System_Tuple_T6:
        ...

    @property
    def item_7(self) -> System_Tuple_T7:
        ...

    @property
    def rest(self) -> System_Tuple_TRest:
        ...

    @overload
    def __init__(self, item_1: System_Tuple_T1) -> None:
        ...

    @overload
    def __init__(self, item_1: System_Tuple_T1, item_2: System_Tuple_T2) -> None:
        ...

    @overload
    def __init__(self, item_1: System_Tuple_T1, item_2: System_Tuple_T2, item_3: System_Tuple_T3) -> None:
        ...

    @overload
    def __init__(self, item_1: System_Tuple_T1, item_2: System_Tuple_T2, item_3: System_Tuple_T3, item_4: System_Tuple_T4) -> None:
        ...

    @overload
    def __init__(self, item_1: System_Tuple_T1, item_2: System_Tuple_T2, item_3: System_Tuple_T3, item_4: System_Tuple_T4, item_5: System_Tuple_T5) -> None:
        ...

    @overload
    def __init__(self, item_1: System_Tuple_T1, item_2: System_Tuple_T2, item_3: System_Tuple_T3, item_4: System_Tuple_T4, item_5: System_Tuple_T5, item_6: System_Tuple_T6) -> None:
        ...

    @overload
    def __init__(self, item_1: System_Tuple_T1, item_2: System_Tuple_T2, item_3: System_Tuple_T3, item_4: System_Tuple_T4, item_5: System_Tuple_T5, item_6: System_Tuple_T6, item_7: System_Tuple_T7) -> None:
        ...

    @overload
    def __init__(self, item_1: System_Tuple_T1, item_2: System_Tuple_T2, item_3: System_Tuple_T3, item_4: System_Tuple_T4, item_5: System_Tuple_T5, item_6: System_Tuple_T6, item_7: System_Tuple_T7, rest: System_Tuple_TRest) -> None:
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def to_string(self) -> str:
        ...


class TypeLoadException(System.SystemException):
    """This class has no documentation."""

    @property
    def message(self) -> str:
        ...

    @property
    def type_name(self) -> str:
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
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """
        This method is protected.
        
        Obsoletions.LegacyFormatterImplMessage
        """
        ...

    def get_object_data(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """Obsoletions.LegacyFormatterImplMessage"""
        warnings.warn("Obsoletions.LegacyFormatterImplMessage", DeprecationWarning)


class EntryPointNotFoundException(System.TypeLoadException):
    """The exception that is thrown when an attempt to load a class fails due to the absence of an entry method."""

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
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """
        This method is protected.
        
        Obsoletions.LegacyFormatterImplMessage
        """
        ...


class DivideByZeroException(System.ArithmeticException):
    """The exception that is thrown when there is an attempt to divide an integral or decimal value by zero."""

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


class MissingFieldException(System.MissingMemberException, System.Runtime.Serialization.ISerializable):
    """This class has no documentation."""

    @property
    def message(self) -> str:
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
    def __init__(self, class_name: str, field_name: str) -> None:
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """
        This method is protected.
        
        Obsoletions.LegacyFormatterImplMessage
        """
        ...


class StringComparer(System.Object, System.Collections.IComparer, System.Collections.IEqualityComparer, System.Collections.Generic.IComparer[str], System.Collections.Generic.IEqualityComparer[str], metaclass=abc.ABCMeta):
    """This class has no documentation."""

    INVARIANT_CULTURE: System.StringComparer

    INVARIANT_CULTURE_IGNORE_CASE: System.StringComparer

    CURRENT_CULTURE: System.StringComparer

    CURRENT_CULTURE_IGNORE_CASE: System.StringComparer

    ORDINAL: System.StringComparer

    ORDINAL_IGNORE_CASE: System.StringComparer

    @overload
    def compare(self, x: typing.Any, y: typing.Any) -> int:
        ...

    @overload
    def compare(self, x: str, y: str) -> int:
        ...

    @staticmethod
    @overload
    def create(culture: System.Globalization.CultureInfo, ignore_case: bool) -> System.StringComparer:
        ...

    @staticmethod
    @overload
    def create(culture: System.Globalization.CultureInfo, options: System.Globalization.CompareOptions) -> System.StringComparer:
        ...

    @overload
    def equals(self, x: typing.Any, y: typing.Any) -> bool:
        ...

    @overload
    def equals(self, x: str, y: str) -> bool:
        ...

    @staticmethod
    def from_comparison(comparison_type: System.StringComparison) -> System.StringComparer:
        ...

    @overload
    def get_hash_code(self, obj: typing.Any) -> int:
        ...

    @overload
    def get_hash_code(self, obj: str) -> int:
        ...

    @staticmethod
    def is_well_known_culture_aware_comparer(comparer: System.Collections.Generic.IEqualityComparer[str], compare_info: typing.Optional[System.Globalization.CompareInfo], compare_options: typing.Optional[System.Globalization.CompareOptions]) -> typing.Tuple[bool, System.Globalization.CompareInfo, System.Globalization.CompareOptions]:
        """
        Determines whether the specified IEqualityComparer{String} is a well-known culture-aware string comparer.
        
        :param comparer: The comparer to query.
        :param compare_info: When this method returns, contains a value indicating which CompareInfo was used to create . Set to null if this method returns false.
        :param compare_options: When this method returns, contains a value indicating which CompareOptions was used to create . Set to CompareOptions.None if this method returns false.
        :returns: true if  is a well-known culture-aware string comparer; otherwise, false.
        """
        ...

    @staticmethod
    def is_well_known_ordinal_comparer(comparer: System.Collections.Generic.IEqualityComparer[str], ignore_case: typing.Optional[bool]) -> typing.Tuple[bool, bool]:
        """
        Determines whether the specified IEqualityComparer{String} is a well-known ordinal string comparer.
        
        :param comparer: The comparer to query.
        :param ignore_case: When this method returns, contains a value stating whether  is case-insensitive. Set to false if this method returns false.
        :returns: true if  is a well-known ordinal string comparer; otherwise, false.
        """
        ...


class CultureAwareComparer(System.StringComparer, System.Collections.Generic.IAlternateEqualityComparer[System.ReadOnlySpan[str], str], System.Runtime.Serialization.ISerializable):
    """This class has no documentation."""

    def compare(self, x: str, y: str) -> int:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, x: str, y: str) -> bool:
        ...

    @overload
    def get_hash_code(self, obj: str) -> int:
        ...

    @overload
    def get_hash_code(self) -> int:
        ...

    def get_object_data(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...


class OrdinalComparer(System.StringComparer, System.Collections.Generic.IAlternateEqualityComparer[System.ReadOnlySpan[str], str]):
    """This class has no documentation."""

    def compare(self, x: str, y: str) -> int:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, x: str, y: str) -> bool:
        ...

    @overload
    def get_hash_code(self, obj: str) -> int:
        ...

    @overload
    def get_hash_code(self) -> int:
        ...


class TypeAccessException(System.TypeLoadException):
    """This class has no documentation."""

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
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """
        This method is protected.
        
        Obsoletions.LegacyFormatterImplMessage
        """
        ...


class DataMisalignedException(System.SystemException):
    """The exception that is thrown when a unit of data is read from or written to an address that is not a multiple of the data size."""

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, message: str) -> None:
        ...

    @overload
    def __init__(self, message: str, inner_exception: System.Exception) -> None:
        ...


class LoaderOptimizationAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def value(self) -> System.LoaderOptimization:
        ...

    @overload
    def __init__(self, value: int) -> None:
        ...

    @overload
    def __init__(self, value: System.LoaderOptimization) -> None:
        ...


class UInt64(System.IComparable[int], System.IConvertible, System.ISpanFormattable, System.IEquatable[int], System.Numerics.IUnsignedNumber[int], System.IUtf8SpanFormattable, System.IBinaryIntegerParseAndFormatInfo[int]):
    """This class has no documentation."""

    MAX_VALUE: int = ...

    MIN_VALUE: int = ...

    @overload
    def __ge__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __ge__(self, other: int) -> bool:
        ...

    @overload
    def __gt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __gt__(self, other: int) -> bool:
        ...

    @overload
    def __le__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __le__(self, other: int) -> bool:
        ...

    @overload
    def __lt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __lt__(self, other: int) -> bool:
        ...

    @staticmethod
    def big_mul(left: int, right: int) -> System.UInt128:
        """
        Produces the full product of two unsigned 64-bit numbers.
        
        :param left: The first number to multiply.
        :param right: The second number to multiply.
        :returns: The number containing the product of the specified numbers.
        """
        ...

    @staticmethod
    def clamp(value: int, min: int, max: int) -> int:
        ...

    @overload
    def compare_to(self, value: typing.Any) -> int:
        ...

    @overload
    def compare_to(self, value: int) -> int:
        ...

    @staticmethod
    def div_rem(left: int, right: int) -> System.ValueTuple[int, int]:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, obj: int) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def get_type_code(self) -> System.TypeCode:
        ...

    @staticmethod
    def is_even_integer(value: int) -> bool:
        ...

    @staticmethod
    def is_odd_integer(value: int) -> bool:
        ...

    @staticmethod
    def is_pow_2(value: int) -> bool:
        ...

    @staticmethod
    def leading_zero_count(value: int) -> int:
        ...

    @staticmethod
    def log_2(value: int) -> int:
        ...

    @staticmethod
    def max(x: int, y: int) -> int:
        ...

    @staticmethod
    def min(x: int, y: int) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: str) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: str, style: System.Globalization.NumberStyles) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: str, provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: str, style: System.Globalization.NumberStyles, provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int], style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> int:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int], provider: System.IFormatProvider) -> int:
        ...

    @staticmethod
    def pop_count(value: int) -> int:
        ...

    @staticmethod
    def rotate_left(value: int, rotate_amount: int) -> int:
        ...

    @staticmethod
    def rotate_right(value: int, rotate_amount: int) -> int:
        ...

    @staticmethod
    def sign(value: int) -> int:
        ...

    @overload
    def to_string(self) -> str:
        ...

    @overload
    def to_string(self, provider: System.IFormatProvider) -> str:
        ...

    @overload
    def to_string(self, format: str) -> str:
        ...

    @overload
    def to_string(self, format: str, provider: System.IFormatProvider) -> str:
        ...

    @staticmethod
    def trailing_zero_count(value: int) -> int:
        ...

    @overload
    def try_format(self, destination: System.Span[str], chars_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @overload
    def try_format(self, utf_8_destination: System.Span[int], bytes_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        """
        Tries to convert a UTF-8 character span containing the string representation of a number to its 64-bit unsigned integer equivalent.
        
        :param utf_8_text: A span containing the UTF-8 characters representing the number to convert.
        :param result: When this method returns, contains the 64-bit unsigned integer value equivalent to the number contained in  if the conversion succeeded, or zero if the conversion failed. This parameter is passed uninitialized; any value originally supplied in result will be overwritten.
        :returns: true if  was converted successfully; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def try_parse(s: str, style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], provider: System.IFormatProvider, result: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...


class InvalidTimeZoneException(System.Exception):
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


class OperationCanceledException(System.SystemException):
    """The exception that is thrown in a thread upon cancellation of an operation that the thread was executing."""

    @property
    def cancellation_token(self) -> System.Threading.CancellationToken:
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
    def __init__(self, token: System.Threading.CancellationToken) -> None:
        ...

    @overload
    def __init__(self, message: str, token: System.Threading.CancellationToken) -> None:
        ...

    @overload
    def __init__(self, message: str, inner_exception: System.Exception, token: System.Threading.CancellationToken) -> None:
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """
        This method is protected.
        
        Obsoletions.LegacyFormatterImplMessage
        """
        ...


class MethodAccessException(System.MemberAccessException):
    """The exception that is thrown when there is an invalid attempt to access a method."""

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
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """
        This method is protected.
        
        Obsoletions.LegacyFormatterImplMessage
        """
        ...


class LocalDataStoreSlot(System.Object):
    """This class has no documentation."""


class Span(typing.Generic[System_Span_T]):
    """
    Span represents a contiguous region of arbitrary memory. Unlike arrays, it can point to either managed
    or native memory, or to memory allocated on the stack. It is type-safe and memory-safe.
    """

    class Enumerator:
        """Enumerates the elements of a Span{T}."""

        @property
        def current(self) -> typing.Any:
            """Gets the element at the current position of the enumerator."""
            ...

        def move_next(self) -> bool:
            """Advances the enumerator to the next element of the span."""
            ...

    @property
    def length(self) -> int:
        """The number of items in the span."""
        ...

    @property
    def is_empty(self) -> bool:
        """Gets a value indicating whether this Span{T} is empty."""
        ...

    EMPTY: System.Span[System_Span_T]
    """Returns an empty Span{T}"""

    def __eq__(self, right: System.Span[System_Span_T]) -> bool:
        """
        Returns true if left and right point at the same memory and have the same length.  Note that
        this does *not* check to see if the *contents* are equal.
        """
        ...

    def __getitem__(self, index: int) -> typing.Any:
        """
        Returns a reference to specified element of the Span.
        
        :param index: The zero-based index.
        """
        ...

    @overload
    def __init__(self, pointer: typing.Any, length: int) -> None:
        """
        Creates a new span over the target unmanaged buffer.  Clearly this
        is quite dangerous, because we are creating arbitrarily typed T's
        out of a void*-typed block of memory.  And the length is not checked.
        But if this creation is correct, then all subsequent uses are correct.
        
        :param pointer: An unmanaged pointer to memory.
        :param length: The number of T elements the memory contains.
        """
        ...

    @overload
    def __init__(self, array: typing.List[System_Span_T]) -> None:
        """
        Creates a new span over the entirety of the target array.
        
        :param array: The target array.
        """
        ...

    @overload
    def __init__(self, array: typing.List[System_Span_T], start: int, length: int) -> None:
        """
        Creates a new span over the portion of the target array beginning
        at 'start' index and ending at 'end' index (exclusive).
        
        :param array: The target array.
        :param start: The zero-based index at which to begin the span.
        :param length: The number of items in the span.
        """
        ...

    @overload
    def __init__(self, reference: System_Span_T) -> None:
        """
        Creates a new Span{T} of length 1 around the specified reference.
        
        :param reference: A reference to data.
        """
        ...

    def __ne__(self, right: System.Span[System_Span_T]) -> bool:
        """
        Returns false if left and right point at the same memory and have the same length.  Note that
        this does *not* check to see if the *contents* are equal.
        """
        ...

    def clear(self) -> None:
        """Clears the contents of this span."""
        ...

    def copy_to(self, destination: System.Span[System_Span_T]) -> None:
        """
        Copies the contents of this span into destination span. If the source
        and destinations overlap, this method behaves as if the original values in
        a temporary location before the destination is overwritten.
        
        :param destination: The span to copy items into.
        """
        ...

    def equals(self, obj: typing.Any) -> bool:
        """
        This method is not supported as spans cannot be boxed. To compare two spans, use operator==.
        
        Equals() on Span will always throw an exception. Use the equality operator instead.
        """
        warnings.warn("Equals() on Span will always throw an exception. Use the equality operator instead.", DeprecationWarning)

    def fill(self, value: System_Span_T) -> None:
        """Fills the contents of this span with the given value."""
        ...

    def get_enumerator(self) -> System.Span.Enumerator:
        """Gets an enumerator for this span."""
        ...

    def get_hash_code(self) -> int:
        """
        This method is not supported as spans cannot be boxed.
        
        GetHashCode() on Span will always throw an exception.
        """
        warnings.warn("GetHashCode() on Span will always throw an exception.", DeprecationWarning)

    def get_pinnable_reference(self) -> typing.Any:
        """
        Returns a reference to the 0th element of the Span. If the Span is empty, returns null reference.
        It can be used for pinning and is required to support the use of span within a fixed statement.
        """
        ...

    @overload
    def slice(self, start: int) -> System.Span[System_Span_T]:
        """
        Forms a slice out of the given span, beginning at 'start'.
        
        :param start: The zero-based index at which to begin this slice.
        """
        ...

    @overload
    def slice(self, start: int, length: int) -> System.Span[System_Span_T]:
        """
        Forms a slice out of the given span, beginning at 'start', of given length
        
        :param start: The zero-based index at which to begin this slice.
        :param length: The desired length for the slice (exclusive).
        """
        ...

    def to_array(self) -> typing.List[System_Span_T]:
        """
        Copies the contents of this span into a new array.  This heap
        allocates, so should generally be avoided, however it is sometimes
        necessary to bridge the gap with APIs written in terms of arrays.
        """
        ...

    def to_string(self) -> str:
        """
        For Span{Char}, returns a new instance of string that represents the characters pointed to by the span.
        Otherwise, returns a string with the name of the type and the number of elements.
        """
        ...

    def try_copy_to(self, destination: System.Span[System_Span_T]) -> bool:
        """
        Copies the contents of this span into destination span. If the source
        and destinations overlap, this method behaves as if the original values in
        a temporary location before the destination is overwritten.
        
        :param destination: The span to copy items into.
        :returns: If the destination span is shorter than the source span, this method return false and no data is written to the destination.
        """
        ...


class ApplicationId(System.Object):
    """This class has no documentation."""

    @property
    def culture(self) -> str:
        ...

    @property
    def name(self) -> str:
        ...

    @property
    def processor_architecture(self) -> str:
        ...

    @property
    def version(self) -> System.Version:
        ...

    @property
    def public_key_token(self) -> typing.List[int]:
        ...

    def __init__(self, public_key_token: typing.List[int], name: str, version: System.Version, processor_architecture: str, culture: str) -> None:
        ...

    def copy(self) -> System.ApplicationId:
        ...

    def equals(self, o: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def to_string(self) -> str:
        ...


class ArraySegment(typing.Generic[System_ArraySegment_T], System.Collections.Generic.IList[System_ArraySegment_T], System.Collections.Generic.IReadOnlyList[System_ArraySegment_T], typing.Iterable[System_ArraySegment_T]):
    """Delimits a section of a one-dimensional array."""

    class Enumerator(System.Collections.Generic.IEnumerator[System_ArraySegment_T]):
        """This class has no documentation."""

        @property
        def current(self) -> System_ArraySegment_T:
            ...

        def dispose(self) -> None:
            ...

        def move_next(self) -> bool:
            ...

    EMPTY: System.ArraySegment[System_ArraySegment_T]

    @property
    def array(self) -> typing.List[System_ArraySegment_T]:
        ...

    @property
    def offset(self) -> int:
        ...

    @property
    def count(self) -> int:
        ...

    def __eq__(self, b: System.ArraySegment[System_ArraySegment_T]) -> bool:
        ...

    def __getitem__(self, index: int) -> System_ArraySegment_T:
        ...

    @overload
    def __init__(self, array: typing.List[System_ArraySegment_T]) -> None:
        ...

    @overload
    def __init__(self, array: typing.List[System_ArraySegment_T], offset: int, count: int) -> None:
        ...

    def __iter__(self) -> typing.Iterator[System_ArraySegment_T]:
        ...

    def __ne__(self, b: System.ArraySegment[System_ArraySegment_T]) -> bool:
        ...

    def __setitem__(self, index: int, value: System_ArraySegment_T) -> None:
        ...

    @overload
    def copy_to(self, destination: typing.List[System_ArraySegment_T]) -> None:
        ...

    @overload
    def copy_to(self, destination: typing.List[System_ArraySegment_T], destination_index: int) -> None:
        ...

    @overload
    def copy_to(self, destination: System.ArraySegment[System_ArraySegment_T]) -> None:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, obj: System.ArraySegment[System_ArraySegment_T]) -> bool:
        ...

    def get_enumerator(self) -> System.ArraySegment.Enumerator:
        ...

    def get_hash_code(self) -> int:
        ...

    @overload
    def slice(self, index: int) -> System.ArraySegment[System_ArraySegment_T]:
        ...

    @overload
    def slice(self, index: int, count: int) -> System.ArraySegment[System_ArraySegment_T]:
        ...

    def to_array(self) -> typing.List[System_ArraySegment_T]:
        ...


class TypeInitializationException(System.SystemException):
    """The exception that is thrown as a wrapper around the exception thrown by the class initializer."""

    @property
    def type_name(self) -> str:
        ...

    def __init__(self, full_type_name: str, inner_exception: System.Exception) -> None:
        ...

    def get_object_data(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """Obsoletions.LegacyFormatterImplMessage"""
        warnings.warn("Obsoletions.LegacyFormatterImplMessage", DeprecationWarning)


class CannotUnloadAppDomainException(System.SystemException):
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


class IUtf8SpanParsable(typing.Generic[System_IUtf8SpanParsable_TSelf], metaclass=abc.ABCMeta):
    """Defines a mechanism for parsing a span of UTF-8 characters to a value."""


class DllNotFoundException(System.TypeLoadException):
    """The exception that is thrown when a DLL specified in a DLL import cannot be found."""

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
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """
        This method is protected.
        
        Obsoletions.LegacyFormatterImplMessage
        """
        ...


class ICustomFormatter(metaclass=abc.ABCMeta):
    """Defines a method that supports custom formatting of the value of an object."""

    def format(self, format: str, arg: typing.Any, format_provider: System.IFormatProvider) -> str:
        ...


class STAThreadAttribute(System.Attribute):
    """Indicates that the COM threading model for an application is single-threaded apartment (STA)."""

    def __init__(self) -> None:
        ...


class MTAThreadAttribute(System.Attribute):
    """Indicates that the COM threading model for an application is multi-threaded apartment (MTA)."""

    def __init__(self) -> None:
        ...


class NotFiniteNumberException(System.ArithmeticException):
    """This class has no documentation."""

    @property
    def offending_number(self) -> float:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, offending_number: float) -> None:
        ...

    @overload
    def __init__(self, message: str) -> None:
        ...

    @overload
    def __init__(self, message: str, offending_number: float) -> None:
        ...

    @overload
    def __init__(self, message: str, inner_exception: System.Exception) -> None:
        ...

    @overload
    def __init__(self, message: str, offending_number: float, inner_exception: System.Exception) -> None:
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


class NonSerializedAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class StackOverflowException(System.SystemException):
    """Exception thrown on a stack overflow."""

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, message: str) -> None:
        ...

    @overload
    def __init__(self, message: str, inner_exception: System.Exception) -> None:
        ...


class MulticastDelegate(System.Delegate, System.Runtime.Serialization.ISerializable, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def __eq__(self, d_2: System.MulticastDelegate) -> bool:
        ...

    @overload
    def __init__(self, target: typing.Any, method: str) -> None:
        """This method is protected."""
        ...

    @overload
    def __init__(self, target: typing.Type, method: str) -> None:
        """This method is protected."""
        ...

    def __ne__(self, d_2: System.MulticastDelegate) -> bool:
        ...

    def combine_impl(self, follow: System.Delegate) -> System.Delegate:
        """This method is protected."""
        ...

    def dynamic_invoke_impl(self, args: typing.List[System.Object]) -> System.Object:
        """This method is protected."""
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def get_invocation_list(self) -> typing.List[System.Delegate]:
        ...

    def get_method_impl(self) -> System.Reflection.MethodInfo:
        """This method is protected."""
        ...

    def get_object_data(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """Obsoletions.LegacyFormatterImplMessage"""
        warnings.warn("Obsoletions.LegacyFormatterImplMessage", DeprecationWarning)

    def remove_impl(self, value: System.Delegate) -> System.Delegate:
        """This method is protected."""
        ...


class UriTypeConverter(System.ComponentModel.TypeConverter):
    """
    Provides a type converter to convert Uri objects to and from
    various other representations.
    """

    def can_convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, source_type: typing.Type) -> bool:
        """
        Gets a value indicating whether this converter can convert an object in the
        given source type to a Uri.
        """
        ...

    def can_convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, destination_type: typing.Type) -> bool:
        """
        Gets a value indicating whether this converter can
        convert an object to the given destination type using the context.
        """
        ...

    def convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any) -> System.Object:
        """Converts the given object to the a Uri."""
        ...

    def convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any, destination_type: typing.Type) -> System.Object:
        """
        Converts the given value object to
        the specified destination type using the specified context and arguments.
        """
        ...

    def is_valid(self, context: System.ComponentModel.ITypeDescriptorContext, value: typing.Any) -> bool:
        ...


class ConsoleColor(Enum):
    """This class has no documentation."""

    BLACK = 0

    DARK_BLUE = 1

    DARK_GREEN = 2

    DARK_CYAN = 3

    DARK_RED = 4

    DARK_MAGENTA = 5

    DARK_YELLOW = 6

    GRAY = 7

    DARK_GRAY = 8

    BLUE = 9

    GREEN = 10

    CYAN = 11

    RED = 12

    MAGENTA = 13

    YELLOW = 14

    WHITE = 15


class ConsoleSpecialKey(Enum):
    """This class has no documentation."""

    CONTROL_C = 0

    CONTROL_BREAK = 1


class ConsoleCancelEventArgs(System.EventArgs):
    """This class has no documentation."""

    @property
    def cancel(self) -> bool:
        ...

    @cancel.setter
    def cancel(self, value: bool) -> None:
        ...

    @property
    def special_key(self) -> System.ConsoleSpecialKey:
        ...


class ConsoleKey(Enum):
    """This class has no documentation."""

    NONE = ...

    BACKSPACE = ...

    TAB = ...

    CLEAR = ...

    ENTER = ...

    PAUSE = ...

    ESCAPE = ...

    SPACEBAR = ...

    PAGE_UP = ...

    PAGE_DOWN = ...

    END = ...

    HOME = ...

    LEFT_ARROW = ...

    UP_ARROW = ...

    RIGHT_ARROW = ...

    DOWN_ARROW = ...

    SELECT = ...

    PRINT = ...

    EXECUTE = ...

    PRINT_SCREEN = ...

    INSERT = ...

    DELETE = ...

    HELP = ...

    D_0 = ...

    D_1 = ...

    D_2 = ...

    D_3 = ...

    D_4 = ...

    D_5 = ...

    D_6 = ...

    D_7 = ...

    D_8 = ...

    D_9 = ...

    A = ...

    B = ...

    C = ...

    D = ...

    E = ...

    F = ...

    G = ...

    H = ...

    I = ...

    J = ...

    K = ...

    L = ...

    M = ...

    N = ...

    O = ...

    P = ...

    Q = ...

    R = ...

    S = ...

    T = ...

    U = ...

    V = ...

    W = ...

    X = ...

    Y = ...

    Z = ...

    LEFT_WINDOWS = ...

    RIGHT_WINDOWS = ...

    APPLICATIONS = ...

    SLEEP = ...

    NUM_PAD_0 = ...

    NUM_PAD_1 = ...

    NUM_PAD_2 = ...

    NUM_PAD_3 = ...

    NUM_PAD_4 = ...

    NUM_PAD_5 = ...

    NUM_PAD_6 = ...

    NUM_PAD_7 = ...

    NUM_PAD_8 = ...

    NUM_PAD_9 = ...

    MULTIPLY = ...

    ADD = ...

    SEPARATOR = ...

    SUBTRACT = ...

    DECIMAL = ...

    DIVIDE = ...

    F_1 = ...

    F_2 = ...

    F_3 = ...

    F_4 = ...

    F_5 = ...

    F_6 = ...

    F_7 = ...

    F_8 = ...

    F_9 = ...

    F_10 = ...

    F_11 = ...

    F_12 = ...

    F_13 = ...

    F_14 = ...

    F_15 = ...

    F_16 = ...

    F_17 = ...

    F_18 = ...

    F_19 = ...

    F_20 = ...

    F_21 = ...

    F_22 = ...

    F_23 = ...

    F_24 = ...

    BROWSER_BACK = ...

    BROWSER_FORWARD = ...

    BROWSER_REFRESH = ...

    BROWSER_STOP = ...

    BROWSER_SEARCH = ...

    BROWSER_FAVORITES = ...

    BROWSER_HOME = ...

    VOLUME_MUTE = ...

    VOLUME_DOWN = ...

    VOLUME_UP = ...

    MEDIA_NEXT = ...

    MEDIA_PREVIOUS = ...

    MEDIA_STOP = ...

    MEDIA_PLAY = ...

    LAUNCH_MAIL = ...

    LAUNCH_MEDIA_SELECT = ...

    LAUNCH_APP_1 = ...

    LAUNCH_APP_2 = ...

    OEM_1 = ...

    OEM_PLUS = ...

    OEM_COMMA = ...

    OEM_MINUS = ...

    OEM_PERIOD = ...

    OEM_2 = ...

    OEM_3 = ...

    OEM_4 = ...

    OEM_5 = ...

    OEM_6 = ...

    OEM_7 = ...

    OEM_8 = ...

    OEM_102 = ...

    PROCESS = ...

    PACKET = ...

    ATTENTION = ...

    CR_SEL = ...

    EX_SEL = ...

    ERASE_END_OF_FILE = ...

    PLAY = ...

    ZOOM = ...

    NO_NAME = ...

    PA_1 = ...

    OEM_CLEAR = ...


class ConsoleModifiers(Enum):
    """This class has no documentation."""

    NONE = 0

    ALT = 1

    SHIFT = 2

    CONTROL = 4


class ConsoleKeyInfo(System.IEquatable[System_ConsoleKeyInfo]):
    """This class has no documentation."""

    @property
    def key_char(self) -> str:
        ...

    @property
    def key(self) -> System.ConsoleKey:
        ...

    @property
    def modifiers(self) -> System.ConsoleModifiers:
        ...

    def __eq__(self, b: System.ConsoleKeyInfo) -> bool:
        ...

    def __init__(self, key_char: str, key: System.ConsoleKey, shift: bool, alt: bool, control: bool) -> None:
        ...

    def __ne__(self, b: System.ConsoleKeyInfo) -> bool:
        ...

    @overload
    def equals(self, value: typing.Any) -> bool:
        ...

    @overload
    def equals(self, obj: System.ConsoleKeyInfo) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...


class Console(System.Object):
    """This class has no documentation."""

    IN: System.IO.TextReader

    input_encoding: System.Text.Encoding

    output_encoding: System.Text.Encoding

    KEY_AVAILABLE: bool

    OUT: System.IO.TextWriter

    ERROR: System.IO.TextWriter

    IS_INPUT_REDIRECTED: bool

    IS_OUTPUT_REDIRECTED: bool

    IS_ERROR_REDIRECTED: bool

    cursor_size: int

    NUMBER_LOCK: bool

    CAPS_LOCK: bool

    background_color: System.ConsoleColor

    foreground_color: System.ConsoleColor

    buffer_width: int

    buffer_height: int

    window_left: int

    window_top: int

    window_width: int

    window_height: int

    LARGEST_WINDOW_WIDTH: int

    LARGEST_WINDOW_HEIGHT: int

    cursor_visible: bool

    cursor_left: int

    cursor_top: int

    title: str

    cancel_key_press: _EventContainer[typing.Callable[[System.Object, System.ConsoleCancelEventArgs], None], None]

    treat_control_c_as_input: bool

    @staticmethod
    @overload
    def beep() -> None:
        ...

    @staticmethod
    @overload
    def beep(frequency: int, duration: int) -> None:
        ...

    @staticmethod
    def clear() -> None:
        ...

    @staticmethod
    def get_cursor_position() -> System.ValueTuple[int, int]:
        """
        Gets the position of the cursor.
        
        :returns: The column and row position of the cursor.
        """
        ...

    @staticmethod
    @overload
    def move_buffer_area(source_left: int, source_top: int, source_width: int, source_height: int, target_left: int, target_top: int) -> None:
        ...

    @staticmethod
    @overload
    def move_buffer_area(source_left: int, source_top: int, source_width: int, source_height: int, target_left: int, target_top: int, source_char: str, source_fore_color: System.ConsoleColor, source_back_color: System.ConsoleColor) -> None:
        ...

    @staticmethod
    @overload
    def open_standard_error() -> System.IO.Stream:
        ...

    @staticmethod
    @overload
    def open_standard_error(buffer_size: int) -> System.IO.Stream:
        ...

    @staticmethod
    @overload
    def open_standard_input() -> System.IO.Stream:
        ...

    @staticmethod
    @overload
    def open_standard_input(buffer_size: int) -> System.IO.Stream:
        ...

    @staticmethod
    @overload
    def open_standard_output() -> System.IO.Stream:
        ...

    @staticmethod
    @overload
    def open_standard_output(buffer_size: int) -> System.IO.Stream:
        ...

    @staticmethod
    def read() -> int:
        ...

    @staticmethod
    @overload
    def read_key() -> System.ConsoleKeyInfo:
        ...

    @staticmethod
    @overload
    def read_key(intercept: bool) -> System.ConsoleKeyInfo:
        ...

    @staticmethod
    def read_line() -> str:
        ...

    @staticmethod
    def reset_color() -> None:
        ...

    @staticmethod
    def set_buffer_size(width: int, height: int) -> None:
        ...

    @staticmethod
    def set_cursor_position(left: int, top: int) -> None:
        ...

    @staticmethod
    def set_error(new_error: System.IO.TextWriter) -> None:
        ...

    @staticmethod
    def set_in(new_in: System.IO.TextReader) -> None:
        ...

    @staticmethod
    def set_out(new_out: System.IO.TextWriter) -> None:
        ...

    @staticmethod
    def set_window_position(left: int, top: int) -> None:
        ...

    @staticmethod
    def set_window_size(width: int, height: int) -> None:
        ...

    @staticmethod
    @overload
    def write(format: str, arg_0: typing.Any) -> None:
        ...

    @staticmethod
    @overload
    def write(format: str, arg_0: typing.Any, arg_1: typing.Any) -> None:
        ...

    @staticmethod
    @overload
    def write(format: str, arg_0: typing.Any, arg_1: typing.Any, arg_2: typing.Any) -> None:
        ...

    @staticmethod
    @overload
    def write(value: typing.Any) -> None:
        ...

    @staticmethod
    @overload
    def write(format: str, *arg: typing.Union[System.Object, typing.Iterable[System.Object]]) -> None:
        ...

    @staticmethod
    @overload
    def write(value: bool) -> None:
        ...

    @staticmethod
    @overload
    def write(value: str) -> None:
        ...

    @staticmethod
    @overload
    def write(buffer: typing.List[str]) -> None:
        ...

    @staticmethod
    @overload
    def write(buffer: typing.List[str], index: int, count: int) -> None:
        ...

    @staticmethod
    @overload
    def write(value: float) -> None:
        ...

    @staticmethod
    @overload
    def write(value: int) -> None:
        ...

    @staticmethod
    @overload
    def write(value: System.ReadOnlySpan[str]) -> None:
        ...

    @staticmethod
    @overload
    def write_line(value: typing.Any) -> None:
        ...

    @staticmethod
    @overload
    def write_line(format: str, arg_0: typing.Any) -> None:
        ...

    @staticmethod
    @overload
    def write_line(format: str, arg_0: typing.Any, arg_1: typing.Any) -> None:
        ...

    @staticmethod
    @overload
    def write_line(format: str, arg_0: typing.Any, arg_1: typing.Any, arg_2: typing.Any) -> None:
        ...

    @staticmethod
    @overload
    def write_line() -> None:
        ...

    @staticmethod
    @overload
    def write_line(value: bool) -> None:
        ...

    @staticmethod
    @overload
    def write_line(value: str) -> None:
        ...

    @staticmethod
    @overload
    def write_line(buffer: typing.List[str]) -> None:
        ...

    @staticmethod
    @overload
    def write_line(buffer: typing.List[str], index: int, count: int) -> None:
        ...

    @staticmethod
    @overload
    def write_line(value: float) -> None:
        ...

    @staticmethod
    @overload
    def write_line(value: int) -> None:
        ...

    @staticmethod
    @overload
    def write_line(value: System.ReadOnlySpan[str]) -> None:
        ...

    @staticmethod
    @overload
    def write_line(format: str, *arg: typing.Union[System.Object, typing.Iterable[System.Object]]) -> None:
        ...


class _EventContainer(typing.Generic[System__EventContainer_Callable, System__EventContainer_ReturnType]):
    """This class is used to provide accurate autocomplete on events and cannot be imported."""

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> System__EventContainer_ReturnType:
        """Fires the event."""
        ...

    def __iadd__(self, item: System__EventContainer_Callable) -> typing.Self:
        """Registers an event handler."""
        ...

    def __isub__(self, item: System__EventContainer_Callable) -> typing.Self:
        """Unregisters an event handler."""
        ...


