from typing import overload
from enum import Enum
import typing

import System
import System.Buffers.Binary


class BinaryPrimitives(System.Object):
    """This class has no documentation."""

    @staticmethod
    def read_double_big_endian(source: System.ReadOnlySpan[int]) -> float:
        """
        Reads a double from the beginning of a read-only span of bytes, as big endian.
        
        :param source: The read-only span to read.
        :returns: The big endian value.
        """
        ...

    @staticmethod
    def read_double_little_endian(source: System.ReadOnlySpan[int]) -> float:
        """
        Reads a double from the beginning of a read-only span of bytes, as little endian.
        
        :param source: The read-only span to read.
        :returns: The little endian value.
        """
        ...

    @staticmethod
    def read_half_big_endian(source: System.ReadOnlySpan[int]) -> System.Half:
        """
        Reads a Half from the beginning of a read-only span of bytes, as big endian.
        
        :param source: The read-only span to read.
        :returns: The big endian value.
        """
        ...

    @staticmethod
    def read_half_little_endian(source: System.ReadOnlySpan[int]) -> System.Half:
        """
        Reads a Half from the beginning of a read-only span of bytes, as little endian.
        
        :param source: The read-only span to read.
        :returns: The little endian value.
        """
        ...

    @staticmethod
    def read_int_128_big_endian(source: System.ReadOnlySpan[int]) -> System.Int128:
        """
        Reads a Int128 from the beginning of a read-only span of bytes, as big endian.
        
        :param source: The read-only span to read.
        :returns: The big endian value.
        """
        ...

    @staticmethod
    def read_int_128_little_endian(source: System.ReadOnlySpan[int]) -> System.Int128:
        """
        Reads a Int128 from the beginning of a read-only span of bytes, as little endian.
        
        :param source: The read-only span to read.
        :returns: The little endian value.
        """
        ...

    @staticmethod
    def read_int_16_big_endian(source: System.ReadOnlySpan[int]) -> int:
        """
        Reads a short from the beginning of a read-only span of bytes, as big endian.
        
        :param source: The read-only span to read.
        :returns: The big endian value.
        """
        ...

    @staticmethod
    def read_int_16_little_endian(source: System.ReadOnlySpan[int]) -> int:
        """
        Reads a short from the beginning of a read-only span of bytes, as little endian.
        
        :param source: The read-only span to read.
        :returns: The little endian value.
        """
        ...

    @staticmethod
    def read_int_32_big_endian(source: System.ReadOnlySpan[int]) -> int:
        """
        Reads a int from the beginning of a read-only span of bytes, as big endian.
        
        :param source: The read-only span to read.
        :returns: The big endian value.
        """
        ...

    @staticmethod
    def read_int_32_little_endian(source: System.ReadOnlySpan[int]) -> int:
        """
        Reads a int from the beginning of a read-only span of bytes, as little endian.
        
        :param source: The read-only span to read.
        :returns: The little endian value.
        """
        ...

    @staticmethod
    def read_int_64_big_endian(source: System.ReadOnlySpan[int]) -> int:
        """
        Reads a long from the beginning of a read-only span of bytes, as big endian.
        
        :param source: The read-only span to read.
        :returns: The big endian value.
        """
        ...

    @staticmethod
    def read_int_64_little_endian(source: System.ReadOnlySpan[int]) -> int:
        """
        Reads a long from the beginning of a read-only span of bytes, as little endian.
        
        :param source: The read-only span to read.
        :returns: The little endian value.
        """
        ...

    @staticmethod
    def read_int_ptr_big_endian(source: System.ReadOnlySpan[int]) -> System.IntPtr:
        """
        Reads a nint from the beginning of a read-only span of bytes, as big endian.
        
        :param source: The read-only span to read.
        :returns: The big endian value.
        """
        ...

    @staticmethod
    def read_int_ptr_little_endian(source: System.ReadOnlySpan[int]) -> System.IntPtr:
        """
        Reads a nint from the beginning of a read-only span of bytes, as little endian.
        
        :param source: The read-only span to read.
        :returns: The little endian value.
        """
        ...

    @staticmethod
    def read_single_big_endian(source: System.ReadOnlySpan[int]) -> float:
        """
        Reads a float from the beginning of a read-only span of bytes, as big endian.
        
        :param source: The read-only span to read.
        :returns: The big endian value.
        """
        ...

    @staticmethod
    def read_single_little_endian(source: System.ReadOnlySpan[int]) -> float:
        """
        Reads a float from the beginning of a read-only span of bytes, as little endian.
        
        :param source: The read-only span to read.
        :returns: The little endian value.
        """
        ...

    @staticmethod
    def read_u_int_128_big_endian(source: System.ReadOnlySpan[int]) -> System.UInt128:
        """
        Reads a UInt128 from the beginning of a read-only span of bytes, as big endian.
        
        :param source: The read-only span to read.
        :returns: The big endian value.
        """
        ...

    @staticmethod
    def read_u_int_128_little_endian(source: System.ReadOnlySpan[int]) -> System.UInt128:
        """
        Reads a UInt128 from the beginning of a read-only span of bytes, as little endian.
        
        :param source: The read-only span to read.
        :returns: The little endian value.
        """
        ...

    @staticmethod
    def read_u_int_16_big_endian(source: System.ReadOnlySpan[int]) -> int:
        """
        Reads a ushort from the beginning of a read-only span of bytes, as big endian.
        
        :param source: The read-only span to read.
        :returns: The big endian value.
        """
        ...

    @staticmethod
    def read_u_int_16_little_endian(source: System.ReadOnlySpan[int]) -> int:
        """
        Reads a ushort from the beginning of a read-only span of bytes, as little endian.
        
        :param source: The read-only span to read.
        :returns: The little endian value.
        """
        ...

    @staticmethod
    def read_u_int_32_big_endian(source: System.ReadOnlySpan[int]) -> int:
        """
        Reads a uint from the beginning of a read-only span of bytes, as big endian.
        
        :param source: The read-only span to read.
        :returns: The big endian value.
        """
        ...

    @staticmethod
    def read_u_int_32_little_endian(source: System.ReadOnlySpan[int]) -> int:
        """
        Reads a uint from the beginning of a read-only span of bytes, as little endian.
        
        :param source: The read-only span to read.
        :returns: The little endian value.
        """
        ...

    @staticmethod
    def read_u_int_64_big_endian(source: System.ReadOnlySpan[int]) -> int:
        """
        Reads a ulong from the beginning of a read-only span of bytes, as big endian.
        
        :param source: The read-only span to read.
        :returns: The big endian value.
        """
        ...

    @staticmethod
    def read_u_int_64_little_endian(source: System.ReadOnlySpan[int]) -> int:
        """
        Reads a ulong from the beginning of a read-only span of bytes, as little endian.
        
        :param source: The read-only span to read.
        :returns: The little endian value.
        """
        ...

    @staticmethod
    def read_u_int_ptr_big_endian(source: System.ReadOnlySpan[int]) -> System.UIntPtr:
        """
        Reads a nuint from the beginning of a read-only span of bytes, as big endian.
        
        :param source: The read-only span to read.
        :returns: The big endian value.
        """
        ...

    @staticmethod
    def read_u_int_ptr_little_endian(source: System.ReadOnlySpan[int]) -> System.UIntPtr:
        """
        Reads a nuint from the beginning of a read-only span of bytes, as little endian.
        
        :param source: The read-only span to read.
        :returns: The little endian value.
        """
        ...

    @staticmethod
    @overload
    def reverse_endianness(value: int) -> int:
        """
        Reverses a primitive value by performing an endianness swap of the specified sbyte value, which effectively does nothing for an sbyte.
        
        :param value: The value to reverse.
        :returns: The passed-in value, unmodified.
        """
        ...

    @staticmethod
    @overload
    def reverse_endianness(value: System.IntPtr) -> System.IntPtr:
        """
        Reverses a primitive value by performing an endianness swap of the specified nint value.
        
        :param value: The value to reverse.
        :returns: The reversed value.
        """
        ...

    @staticmethod
    @overload
    def reverse_endianness(value: System.Int128) -> System.Int128:
        """
        Reverses a primitive value by performing an endianness swap of the specified Int128 value.
        
        :param value: The value to reverse.
        :returns: The reversed value.
        """
        ...

    @staticmethod
    @overload
    def reverse_endianness(value: System.UIntPtr) -> System.UIntPtr:
        """
        Reverses a primitive value by performing an endianness swap of the specified nuint value.
        
        :param value: The value to reverse.
        :returns: The reversed value.
        """
        ...

    @staticmethod
    @overload
    def reverse_endianness(value: System.UInt128) -> System.UInt128:
        """
        Reverses a primitive value by performing an endianness swap of the specified UInt128 value.
        
        :param value: The value to reverse.
        :returns: The reversed value.
        """
        ...

    @staticmethod
    @overload
    def reverse_endianness(source: System.ReadOnlySpan[int], destination: System.Span[int]) -> None:
        """
        Copies every primitive value from  to , reversing each primitive by performing an endianness swap as part of writing each.
        
        :param source: The source span to copy.
        :param destination: The destination to which the source elements should be copied.
        """
        ...

    @staticmethod
    @overload
    def reverse_endianness(source: System.ReadOnlySpan[System.UIntPtr], destination: System.Span[System.UIntPtr]) -> None:
        ...

    @staticmethod
    @overload
    def reverse_endianness(source: System.ReadOnlySpan[System.IntPtr], destination: System.Span[System.IntPtr]) -> None:
        ...

    @staticmethod
    @overload
    def reverse_endianness(source: System.ReadOnlySpan[System.UInt128], destination: System.Span[System.UInt128]) -> None:
        ...

    @staticmethod
    @overload
    def reverse_endianness(source: System.ReadOnlySpan[System.Int128], destination: System.Span[System.Int128]) -> None:
        ...

    @staticmethod
    def try_read_double_big_endian(source: System.ReadOnlySpan[int], value: typing.Optional[float]) -> typing.Tuple[bool, float]:
        """
        Reads a double from the beginning of a read-only span of bytes, as big endian.
        
        :param source: The read-only span of bytes to read.
        :param value: When this method returns, contains the value read out of the read-only span of bytes, as big endian.
        :returns: true if the span is large enough to contain a double; otherwise, false.
        """
        ...

    @staticmethod
    def try_read_double_little_endian(source: System.ReadOnlySpan[int], value: typing.Optional[float]) -> typing.Tuple[bool, float]:
        """
        Reads a double from the beginning of a read-only span of bytes, as little endian.
        
        :param source: The read-only span of bytes to read.
        :param value: When this method returns, contains the value read out of the read-only span of bytes, as little endian.
        :returns: true if the span is large enough to contain a double; otherwise, false.
        """
        ...

    @staticmethod
    def try_read_half_big_endian(source: System.ReadOnlySpan[int], value: typing.Optional[System.Half]) -> typing.Tuple[bool, System.Half]:
        """
        Reads a Half from the beginning of a read-only span of bytes, as big endian.
        
        :param source: The read-only span of bytes to read.
        :param value: When this method returns, contains the value read out of the read-only span of bytes, as big endian.
        :returns: true if the span is large enough to contain a Half; otherwise, false.
        """
        ...

    @staticmethod
    def try_read_half_little_endian(source: System.ReadOnlySpan[int], value: typing.Optional[System.Half]) -> typing.Tuple[bool, System.Half]:
        """
        Reads a Half from the beginning of a read-only span of bytes, as little endian.
        
        :param source: The read-only span of bytes to read.
        :param value: When this method returns, contains the value read out of the read-only span of bytes, as little endian.
        :returns: true if the span is large enough to contain a Half; otherwise, false.
        """
        ...

    @staticmethod
    def try_read_int_128_big_endian(source: System.ReadOnlySpan[int], value: typing.Optional[System.Int128]) -> typing.Tuple[bool, System.Int128]:
        """
        Reads a Int128 from the beginning of a read-only span of bytes, as big endian.
        
        :param source: The read-only span of bytes to read.
        :param value: When this method returns, contains the value read out of the read-only span of bytes, as big endian.
        :returns: true if the span is large enough to contain a Int128; otherwise, false.
        """
        ...

    @staticmethod
    def try_read_int_128_little_endian(source: System.ReadOnlySpan[int], value: typing.Optional[System.Int128]) -> typing.Tuple[bool, System.Int128]:
        """
        Reads a Int128 from the beginning of a read-only span of bytes, as little endian.
        
        :param source: The read-only span of bytes to read.
        :param value: When this method returns, contains the value read out of the read-only span of bytes, as little endian.
        :returns: true if the span is large enough to contain a Int128; otherwise, false.
        """
        ...

    @staticmethod
    def try_read_int_16_big_endian(source: System.ReadOnlySpan[int], value: typing.Optional[int]) -> typing.Tuple[bool, int]:
        """
        Reads a short from the beginning of a read-only span of bytes, as big endian.
        
        :param source: The read-only span of bytes to read.
        :param value: When this method returns, contains the value read out of the read-only span of bytes, as big endian.
        :returns: true if the span is large enough to contain a short; otherwise, false.
        """
        ...

    @staticmethod
    def try_read_int_16_little_endian(source: System.ReadOnlySpan[int], value: typing.Optional[int]) -> typing.Tuple[bool, int]:
        """
        Reads a short from the beginning of a read-only span of bytes, as little endian.
        
        :param source: The read-only span of bytes to read.
        :param value: When this method returns, contains the value read out of the read-only span of bytes, as little endian.
        :returns: true if the span is large enough to contain a short; otherwise, false.
        """
        ...

    @staticmethod
    def try_read_int_32_big_endian(source: System.ReadOnlySpan[int], value: typing.Optional[int]) -> typing.Tuple[bool, int]:
        """
        Reads a int from the beginning of a read-only span of bytes, as big endian.
        
        :param source: The read-only span of bytes to read.
        :param value: When this method returns, contains the value read out of the read-only span of bytes, as big endian.
        :returns: true if the span is large enough to contain a int; otherwise, false.
        """
        ...

    @staticmethod
    def try_read_int_32_little_endian(source: System.ReadOnlySpan[int], value: typing.Optional[int]) -> typing.Tuple[bool, int]:
        """
        Reads a int from the beginning of a read-only span of bytes, as little endian.
        
        :param source: The read-only span of bytes to read.
        :param value: When this method returns, contains the value read out of the read-only span of bytes, as little endian.
        :returns: true if the span is large enough to contain a int; otherwise, false.
        """
        ...

    @staticmethod
    def try_read_int_64_big_endian(source: System.ReadOnlySpan[int], value: typing.Optional[int]) -> typing.Tuple[bool, int]:
        """
        Reads a long from the beginning of a read-only span of bytes, as big endian.
        
        :param source: The read-only span of bytes to read.
        :param value: When this method returns, contains the value read out of the read-only span of bytes, as big endian.
        :returns: true if the span is large enough to contain a long; otherwise, false.
        """
        ...

    @staticmethod
    def try_read_int_64_little_endian(source: System.ReadOnlySpan[int], value: typing.Optional[int]) -> typing.Tuple[bool, int]:
        """
        Reads a long from the beginning of a read-only span of bytes, as little endian.
        
        :param source: The read-only span of bytes to read.
        :param value: When this method returns, contains the value read out of the read-only span of bytes, as little endian.
        :returns: true if the span is large enough to contain a long; otherwise, false.
        """
        ...

    @staticmethod
    def try_read_int_ptr_big_endian(source: System.ReadOnlySpan[int], value: typing.Optional[System.IntPtr]) -> typing.Tuple[bool, System.IntPtr]:
        """
        Reads a nint from the beginning of a read-only span of bytes, as big endian.
        
        :param source: The read-only span of bytes to read.
        :param value: When this method returns, contains the value read out of the read-only span of bytes, as big endian.
        :returns: true if the span is large enough to contain a nint; otherwise, false.
        """
        ...

    @staticmethod
    def try_read_int_ptr_little_endian(source: System.ReadOnlySpan[int], value: typing.Optional[System.IntPtr]) -> typing.Tuple[bool, System.IntPtr]:
        """
        Reads a nint from the beginning of a read-only span of bytes, as little endian.
        
        :param source: The read-only span of bytes to read.
        :param value: When this method returns, contains the value read out of the read-only span of bytes, as little endian.
        :returns: true if the span is large enough to contain a nint; otherwise, false.
        """
        ...

    @staticmethod
    def try_read_single_big_endian(source: System.ReadOnlySpan[int], value: typing.Optional[float]) -> typing.Tuple[bool, float]:
        """
        Reads a float from the beginning of a read-only span of bytes, as big endian.
        
        :param source: The read-only span of bytes to read.
        :param value: When this method returns, contains the value read out of the read-only span of bytes, as big endian.
        :returns: true if the span is large enough to contain a float; otherwise, false.
        """
        ...

    @staticmethod
    def try_read_single_little_endian(source: System.ReadOnlySpan[int], value: typing.Optional[float]) -> typing.Tuple[bool, float]:
        """
        Reads a float from the beginning of a read-only span of bytes, as little endian.
        
        :param source: The read-only span of bytes to read.
        :param value: When this method returns, contains the value read out of the read-only span of bytes, as little endian.
        :returns: true if the span is large enough to contain a float; otherwise, false.
        """
        ...

    @staticmethod
    def try_read_u_int_128_big_endian(source: System.ReadOnlySpan[int], value: typing.Optional[System.UInt128]) -> typing.Tuple[bool, System.UInt128]:
        """
        Reads a UInt128 from the beginning of a read-only span of bytes, as big endian.
        
        :param source: The read-only span of bytes to read.
        :param value: When this method returns, contains the value read out of the read-only span of bytes, as big endian.
        :returns: true if the span is large enough to contain a UInt128; otherwise, false.
        """
        ...

    @staticmethod
    def try_read_u_int_128_little_endian(source: System.ReadOnlySpan[int], value: typing.Optional[System.UInt128]) -> typing.Tuple[bool, System.UInt128]:
        """
        Reads a UInt128 from the beginning of a read-only span of bytes, as little endian.
        
        :param source: The read-only span of bytes to read.
        :param value: When this method returns, contains the value read out of the read-only span of bytes, as little endian.
        :returns: true if the span is large enough to contain a UInt128; otherwise, false.
        """
        ...

    @staticmethod
    def try_read_u_int_16_big_endian(source: System.ReadOnlySpan[int], value: typing.Optional[int]) -> typing.Tuple[bool, int]:
        """
        Reads a ushort from the beginning of a read-only span of bytes, as big endian.
        
        :param source: The read-only span of bytes to read.
        :param value: When this method returns, contains the value read out of the read-only span of bytes, as big endian.
        :returns: true if the span is large enough to contain a ushort; otherwise, false.
        """
        ...

    @staticmethod
    def try_read_u_int_16_little_endian(source: System.ReadOnlySpan[int], value: typing.Optional[int]) -> typing.Tuple[bool, int]:
        """
        Reads a ushort from the beginning of a read-only span of bytes, as little endian.
        
        :param source: The read-only span of bytes to read.
        :param value: When this method returns, contains the value read out of the read-only span of bytes, as little endian.
        :returns: true if the span is large enough to contain a ushort; otherwise, false.
        """
        ...

    @staticmethod
    def try_read_u_int_32_big_endian(source: System.ReadOnlySpan[int], value: typing.Optional[int]) -> typing.Tuple[bool, int]:
        """
        Reads a uint from the beginning of a read-only span of bytes, as big endian.
        
        :param source: The read-only span of bytes to read.
        :param value: When this method returns, contains the value read out of the read-only span of bytes, as big endian.
        :returns: true if the span is large enough to contain a uint; otherwise, false.
        """
        ...

    @staticmethod
    def try_read_u_int_32_little_endian(source: System.ReadOnlySpan[int], value: typing.Optional[int]) -> typing.Tuple[bool, int]:
        """
        Reads a uint from the beginning of a read-only span of bytes, as little endian.
        
        :param source: The read-only span of bytes to read.
        :param value: When this method returns, contains the value read out of the read-only span of bytes, as little endian.
        :returns: true if the span is large enough to contain a uint; otherwise, false.
        """
        ...

    @staticmethod
    def try_read_u_int_64_big_endian(source: System.ReadOnlySpan[int], value: typing.Optional[int]) -> typing.Tuple[bool, int]:
        """
        Reads a ulong from the beginning of a read-only span of bytes, as big endian.
        
        :param source: The read-only span of bytes to read.
        :param value: When this method returns, contains the value read out of the read-only span of bytes, as big endian.
        :returns: true if the span is large enough to contain a ulong; otherwise, false.
        """
        ...

    @staticmethod
    def try_read_u_int_64_little_endian(source: System.ReadOnlySpan[int], value: typing.Optional[int]) -> typing.Tuple[bool, int]:
        """
        Reads a ulong from the beginning of a read-only span of bytes, as little endian.
        
        :param source: The read-only span of bytes to read.
        :param value: When this method returns, contains the value read out of the read-only span of bytes, as little endian.
        :returns: true if the span is large enough to contain a ulong; otherwise, false.
        """
        ...

    @staticmethod
    def try_read_u_int_ptr_big_endian(source: System.ReadOnlySpan[int], value: typing.Optional[System.UIntPtr]) -> typing.Tuple[bool, System.UIntPtr]:
        """
        :param source: The read-only span of bytes to read.
        :param value: When this method returns, contains the value read out of the read-only span of bytes, as big endian.
        :returns: true if the span is large enough to contain a nuint; otherwise, false.
        """
        ...

    @staticmethod
    def try_read_u_int_ptr_little_endian(source: System.ReadOnlySpan[int], value: typing.Optional[System.UIntPtr]) -> typing.Tuple[bool, System.UIntPtr]:
        """
        Reads a nuint from the beginning of a read-only span of bytes, as little endian.
        
        :param source: The read-only span of bytes to read.
        :param value: When this method returns, contains the value read out of the read-only span of bytes, as little endian.
        :returns: true if the span is large enough to contain a nuint; otherwise, false.
        """
        ...

    @staticmethod
    def try_write_double_big_endian(destination: System.Span[int], value: float) -> bool:
        """
        Writes a double into a span of bytes, as big endian.
        
        :param destination: The span of bytes where the value is to be written, as big endian.
        :param value: The value to write into the span of bytes.
        :returns: true if the span is large enough to contain a double; otherwise, false.
        """
        ...

    @staticmethod
    def try_write_double_little_endian(destination: System.Span[int], value: float) -> bool:
        """
        Writes a double into a span of bytes, as little endian.
        
        :param destination: The span of bytes where the value is to be written, as little endian.
        :param value: The value to write into the span of bytes.
        :returns: true if the span is large enough to contain a double; otherwise, false.
        """
        ...

    @staticmethod
    def try_write_half_big_endian(destination: System.Span[int], value: System.Half) -> bool:
        """
        Writes a Half into a span of bytes, as big endian.
        
        :param destination: The span of bytes where the value is to be written, as big endian.
        :param value: The value to write into the span of bytes.
        :returns: true if the span is large enough to contain a Half; otherwise, false.
        """
        ...

    @staticmethod
    def try_write_half_little_endian(destination: System.Span[int], value: System.Half) -> bool:
        """
        Writes a Half into a span of bytes, as little endian.
        
        :param destination: The span of bytes where the value is to be written, as little endian.
        :param value: The value to write into the span of bytes.
        :returns: true if the span is large enough to contain a Half; otherwise, false.
        """
        ...

    @staticmethod
    def try_write_int_128_big_endian(destination: System.Span[int], value: System.Int128) -> bool:
        """
        Writes a Int128 into a span of bytes, as big endian.
        
        :param destination: The span of bytes where the value is to be written, as big endian.
        :param value: The value to write into the span of bytes.
        :returns: true if the span is large enough to contain a Int128; otherwise, false.
        """
        ...

    @staticmethod
    def try_write_int_128_little_endian(destination: System.Span[int], value: System.Int128) -> bool:
        """
        Writes a Int128 into a span of bytes, as little endian.
        
        :param destination: The span of bytes where the value is to be written, as little endian.
        :param value: The value to write into the span of bytes.
        :returns: true if the span is large enough to contain a Int128; otherwise, false.
        """
        ...

    @staticmethod
    def try_write_int_16_big_endian(destination: System.Span[int], value: int) -> bool:
        """
        Writes a short into a span of bytes, as big endian.
        
        :param destination: The span of bytes where the value is to be written, as big endian.
        :param value: The value to write into the span of bytes.
        :returns: true if the span is large enough to contain a short; otherwise, false.
        """
        ...

    @staticmethod
    def try_write_int_16_little_endian(destination: System.Span[int], value: int) -> bool:
        """
        Writes a short into a span of bytes, as little endian.
        
        :param destination: The span of bytes where the value is to be written, as little endian.
        :param value: The value to write into the span of bytes.
        :returns: true if the span is large enough to contain a short; otherwise, false.
        """
        ...

    @staticmethod
    def try_write_int_32_big_endian(destination: System.Span[int], value: int) -> bool:
        """
        Writes a int into a span of bytes, as big endian.
        
        :param destination: The span of bytes where the value is to be written, as big endian.
        :param value: The value to write into the span of bytes.
        :returns: true if the span is large enough to contain a int; otherwise, false.
        """
        ...

    @staticmethod
    def try_write_int_32_little_endian(destination: System.Span[int], value: int) -> bool:
        """
        Writes a int into a span of bytes, as little endian.
        
        :param destination: The span of bytes where the value is to be written, as little endian.
        :param value: The value to write into the span of bytes.
        :returns: true if the span is large enough to contain a int; otherwise, false.
        """
        ...

    @staticmethod
    def try_write_int_64_big_endian(destination: System.Span[int], value: int) -> bool:
        """
        Writes a long into a span of bytes, as big endian.
        
        :param destination: The span of bytes where the value is to be written, as big endian.
        :param value: The value to write into the span of bytes.
        :returns: true if the span is large enough to contain a long; otherwise, false.
        """
        ...

    @staticmethod
    def try_write_int_64_little_endian(destination: System.Span[int], value: int) -> bool:
        """
        Writes a long into a span of bytes, as little endian.
        
        :param destination: The span of bytes where the value is to be written, as little endian.
        :param value: The value to write into the span of bytes.
        :returns: true if the span is large enough to contain a long; otherwise, false.
        """
        ...

    @staticmethod
    def try_write_int_ptr_big_endian(destination: System.Span[int], value: System.IntPtr) -> bool:
        """
        Writes a nint into a span of bytes, as big endian.
        
        :param destination: The span of bytes where the value is to be written, as big endian.
        :param value: The value to write into the span of bytes.
        :returns: true if the span is large enough to contain a nint; otherwise, false.
        """
        ...

    @staticmethod
    def try_write_int_ptr_little_endian(destination: System.Span[int], value: System.IntPtr) -> bool:
        """
        Writes a nint into a span of bytes, as little endian.
        
        :param destination: The span of bytes where the value is to be written, as little endian.
        :param value: The value to write into the span of bytes.
        :returns: true if the span is large enough to contain a nint; otherwise, false.
        """
        ...

    @staticmethod
    def try_write_single_big_endian(destination: System.Span[int], value: float) -> bool:
        """
        Writes a float into a span of bytes, as big endian.
        
        :param destination: The span of bytes where the value is to be written, as big endian.
        :param value: The value to write into the span of bytes.
        :returns: true if the span is large enough to contain a float; otherwise, false.
        """
        ...

    @staticmethod
    def try_write_single_little_endian(destination: System.Span[int], value: float) -> bool:
        """
        Writes a float into a span of bytes, as little endian.
        
        :param destination: The span of bytes where the value is to be written, as little endian.
        :param value: The value to write into the span of bytes.
        :returns: true if the span is large enough to contain a float; otherwise, false.
        """
        ...

    @staticmethod
    def try_write_u_int_128_big_endian(destination: System.Span[int], value: System.UInt128) -> bool:
        """
        Writes a UInt128 into a span of bytes, as big endian.
        
        :param destination: The span of bytes where the value is to be written, as big endian.
        :param value: The value to write into the span of bytes.
        :returns: true if the span is large enough to contain a UInt128; otherwise, false.
        """
        ...

    @staticmethod
    def try_write_u_int_128_little_endian(destination: System.Span[int], value: System.UInt128) -> bool:
        """
        Writes a UInt128 into a span of bytes, as little endian.
        
        :param destination: The span of bytes where the value is to be written, as little endian.
        :param value: The value to write into the span of bytes.
        :returns: true if the span is large enough to contain a UInt128; otherwise, false.
        """
        ...

    @staticmethod
    def try_write_u_int_16_big_endian(destination: System.Span[int], value: int) -> bool:
        """
        Write a ushort into a span of bytes, as big endian.
        
        :param destination: The span of bytes where the value is to be written, as big endian.
        :param value: The value to write into the span of bytes.
        :returns: true if the span is large enough to contain a ushort; otherwise, false.
        """
        ...

    @staticmethod
    def try_write_u_int_16_little_endian(destination: System.Span[int], value: int) -> bool:
        """
        Write a ushort into a span of bytes, as little endian.
        
        :param destination: The span of bytes where the value is to be written, as little endian.
        :param value: The value to write into the span of bytes.
        :returns: true if the span is large enough to contain a ushort; otherwise, false.
        """
        ...

    @staticmethod
    def try_write_u_int_32_big_endian(destination: System.Span[int], value: int) -> bool:
        """
        Write a uint into a span of bytes, as big endian.
        
        :param destination: The span of bytes where the value is to be written, as big endian.
        :param value: The value to write into the span of bytes.
        :returns: true if the span is large enough to contain a uint; otherwise, false.
        """
        ...

    @staticmethod
    def try_write_u_int_32_little_endian(destination: System.Span[int], value: int) -> bool:
        """
        Write a uint into a span of bytes, as little endian.
        
        :param destination: The span of bytes where the value is to be written, as little endian.
        :param value: The value to write into the span of bytes.
        :returns: true if the span is large enough to contain a uint; otherwise, false.
        """
        ...

    @staticmethod
    def try_write_u_int_64_big_endian(destination: System.Span[int], value: int) -> bool:
        """
        Write a ulong into a span of bytes, as big endian.
        
        :param destination: The span of bytes where the value is to be written, as big endian.
        :param value: The value to write into the span of bytes.
        :returns: true if the span is large enough to contain a ulong; otherwise, false.
        """
        ...

    @staticmethod
    def try_write_u_int_64_little_endian(destination: System.Span[int], value: int) -> bool:
        """
        Write a ulong into a span of bytes, as little endian.
        
        :param destination: The span of bytes where the value is to be written, as little endian.
        :param value: The value to write into the span of bytes.
        :returns: true if the span is large enough to contain a ulong; otherwise, false.
        """
        ...

    @staticmethod
    def try_write_u_int_ptr_big_endian(destination: System.Span[int], value: System.UIntPtr) -> bool:
        """
        Writes a nuint into a span of bytes, as big endian.
        
        :param destination: The span of bytes where the value is to be written, as big endian.
        :param value: The value to write into the span of bytes.
        :returns: true if the span is large enough to contain a nuint; otherwise, false.
        """
        ...

    @staticmethod
    def try_write_u_int_ptr_little_endian(destination: System.Span[int], value: System.UIntPtr) -> bool:
        """
        Writes a nuint into a span of bytes, as little endian.
        
        :param destination: The span of bytes where the value is to be written, as little endian.
        :param value: The value to write into the span of bytes.
        :returns: true if the span is large enough to contain a nuint; otherwise, false.
        """
        ...

    @staticmethod
    def write_double_big_endian(destination: System.Span[int], value: float) -> None:
        """
        Writes a double into a span of bytes, as big endian.
        
        :param destination: The span of bytes where the value is to be written, as big endian.
        :param value: The value to write into the span of bytes.
        """
        ...

    @staticmethod
    def write_double_little_endian(destination: System.Span[int], value: float) -> None:
        """
        Writes a double into a span of bytes, as little endian.
        
        :param destination: The span of bytes where the value is to be written, as little endian.
        :param value: The value to write into the span of bytes.
        """
        ...

    @staticmethod
    def write_half_big_endian(destination: System.Span[int], value: System.Half) -> None:
        """
        Writes a Half into a span of bytes, as big endian.
        
        :param destination: The span of bytes where the value is to be written, as big endian.
        :param value: The value to write into the span of bytes.
        """
        ...

    @staticmethod
    def write_half_little_endian(destination: System.Span[int], value: System.Half) -> None:
        """
        Writes a Half into a span of bytes, as little endian.
        
        :param destination: The span of bytes where the value is to be written, as little endian.
        :param value: The value to write into the span of bytes.
        """
        ...

    @staticmethod
    def write_int_128_big_endian(destination: System.Span[int], value: System.Int128) -> None:
        """
        Writes a Int128 into a span of bytes, as big endian.
        
        :param destination: The span of bytes where the value is to be written, as big endian.
        :param value: The value to write into the span of bytes.
        """
        ...

    @staticmethod
    def write_int_128_little_endian(destination: System.Span[int], value: System.Int128) -> None:
        """
        Writes a Int128 into a span of bytes, as little endian.
        
        :param destination: The span of bytes where the value is to be written, as little endian.
        :param value: The value to write into the span of bytes.
        """
        ...

    @staticmethod
    def write_int_16_big_endian(destination: System.Span[int], value: int) -> None:
        """
        Writes a short into a span of bytes, as big endian.
        
        :param destination: The span of bytes where the value is to be written, as big endian.
        :param value: The value to write into the span of bytes.
        """
        ...

    @staticmethod
    def write_int_16_little_endian(destination: System.Span[int], value: int) -> None:
        """
        Writes a short into a span of bytes, as little endian.
        
        :param destination: The span of bytes where the value is to be written, as little endian.
        :param value: The value to write into the span of bytes.
        """
        ...

    @staticmethod
    def write_int_32_big_endian(destination: System.Span[int], value: int) -> None:
        """
        Writes a int into a span of bytes, as big endian.
        
        :param destination: The span of bytes where the value is to be written, as big endian.
        :param value: The value to write into the span of bytes.
        """
        ...

    @staticmethod
    def write_int_32_little_endian(destination: System.Span[int], value: int) -> None:
        """
        Writes a int into a span of bytes, as little endian.
        
        :param destination: The span of bytes where the value is to be written, as little endian.
        :param value: The value to write into the span of bytes.
        """
        ...

    @staticmethod
    def write_int_64_big_endian(destination: System.Span[int], value: int) -> None:
        """
        Writes a long into a span of bytes, as big endian.
        
        :param destination: The span of bytes where the value is to be written, as big endian.
        :param value: The value to write into the span of bytes.
        """
        ...

    @staticmethod
    def write_int_64_little_endian(destination: System.Span[int], value: int) -> None:
        """
        Writes a long into a span of bytes, as little endian.
        
        :param destination: The span of bytes where the value is to be written, as little endian.
        :param value: The value to write into the span of bytes.
        """
        ...

    @staticmethod
    def write_int_ptr_big_endian(destination: System.Span[int], value: System.IntPtr) -> None:
        """
        Writes a nint into a span of bytes, as big endian.
        
        :param destination: The span of bytes where the value is to be written, as big endian.
        :param value: The value to write into the span of bytes.
        """
        ...

    @staticmethod
    def write_int_ptr_little_endian(destination: System.Span[int], value: System.IntPtr) -> None:
        """
        Writes a nint into a span of bytes, as little endian.
        
        :param destination: The span of bytes where the value is to be written, as little endian.
        :param value: The value to write into the span of bytes.
        """
        ...

    @staticmethod
    def write_single_big_endian(destination: System.Span[int], value: float) -> None:
        """
        Writes a float into a span of bytes, as big endian.
        
        :param destination: The span of bytes where the value is to be written, as big endian.
        :param value: The value to write into the span of bytes.
        """
        ...

    @staticmethod
    def write_single_little_endian(destination: System.Span[int], value: float) -> None:
        """
        Writes a float into a span of bytes, as little endian.
        
        :param destination: The span of bytes where the value is to be written, as little endian.
        :param value: The value to write into the span of bytes.
        """
        ...

    @staticmethod
    def write_u_int_128_big_endian(destination: System.Span[int], value: System.UInt128) -> None:
        """
        Writes a UInt128 into a span of bytes, as big endian.
        
        :param destination: The span of bytes where the value is to be written, as big endian.
        :param value: The value to write into the span of bytes.
        """
        ...

    @staticmethod
    def write_u_int_128_little_endian(destination: System.Span[int], value: System.UInt128) -> None:
        """
        Writes a UInt128 into a span of bytes, as little endian.
        
        :param destination: The span of bytes where the value is to be written, as little endian.
        :param value: The value to write into the span of bytes.
        """
        ...

    @staticmethod
    def write_u_int_16_big_endian(destination: System.Span[int], value: int) -> None:
        """
        Write a ushort into a span of bytes, as big endian.
        
        :param destination: The span of bytes where the value is to be written, as big endian.
        :param value: The value to write into the span of bytes.
        """
        ...

    @staticmethod
    def write_u_int_16_little_endian(destination: System.Span[int], value: int) -> None:
        """
        Write a ushort into a span of bytes, as little endian.
        
        :param destination: The span of bytes where the value is to be written, as little endian.
        :param value: The value to write into the span of bytes.
        """
        ...

    @staticmethod
    def write_u_int_32_big_endian(destination: System.Span[int], value: int) -> None:
        """
        Write a uint into a span of bytes, as big endian.
        
        :param destination: The span of bytes where the value is to be written, as big endian.
        :param value: The value to write into the span of bytes.
        """
        ...

    @staticmethod
    def write_u_int_32_little_endian(destination: System.Span[int], value: int) -> None:
        """
        Write a uint into a span of bytes, as little endian.
        
        :param destination: The span of bytes where the value is to be written, as little endian.
        :param value: The value to write into the span of bytes.
        """
        ...

    @staticmethod
    def write_u_int_64_big_endian(destination: System.Span[int], value: int) -> None:
        """
        Write a ulong into a span of bytes, as big endian.
        
        :param destination: The span of bytes where the value is to be written, as big endian.
        :param value: The value to write into the span of bytes.
        """
        ...

    @staticmethod
    def write_u_int_64_little_endian(destination: System.Span[int], value: int) -> None:
        """
        Write a ulong into a span of bytes, as little endian.
        
        :param destination: The span of bytes where the value is to be written, as little endian.
        :param value: The value to write into the span of bytes.
        """
        ...

    @staticmethod
    def write_u_int_ptr_big_endian(destination: System.Span[int], value: System.UIntPtr) -> None:
        """
        Writes a nuint into a span of bytes, as big endian.
        
        :param destination: The span of bytes where the value is to be written, as big endian.
        :param value: The value to write into the span of bytes.
        """
        ...

    @staticmethod
    def write_u_int_ptr_little_endian(destination: System.Span[int], value: System.UIntPtr) -> None:
        """
        Writes a nuint into a span of bytes, as little endian.
        
        :param destination: The span of bytes where the value is to be written, as little endian.
        :param value: The value to write into the span of bytes.
        """
        ...


