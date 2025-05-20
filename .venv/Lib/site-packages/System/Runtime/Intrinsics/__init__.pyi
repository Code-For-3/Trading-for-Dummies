from typing import overload
from enum import Enum
import typing

import System
import System.Numerics
import System.Runtime.Intrinsics

System_Runtime_Intrinsics_Vector128 = typing.Any
System_Runtime_Intrinsics_Vector512 = typing.Any
System_Runtime_Intrinsics_Vector64 = typing.Any
System_Runtime_Intrinsics_Vector256 = typing.Any

System_Runtime_Intrinsics_Vector128_T = typing.TypeVar("System_Runtime_Intrinsics_Vector128_T")
System_Runtime_Intrinsics_Vector512_T = typing.TypeVar("System_Runtime_Intrinsics_Vector512_T")
System_Runtime_Intrinsics_Vector64_T = typing.TypeVar("System_Runtime_Intrinsics_Vector64_T")
System_Runtime_Intrinsics_Vector256_T = typing.TypeVar("System_Runtime_Intrinsics_Vector256_T")


class Vector128(typing.Generic[System_Runtime_Intrinsics_Vector128_T], System.Runtime.Intrinsics.ISimdVector[System_Runtime_Intrinsics_Vector128, System_Runtime_Intrinsics_Vector128_T]):
    """Represents a 128-bit vector of a specified numeric type that is suitable for low-level optimization of parallel algorithms."""

    IS_HARDWARE_ACCELERATED: bool
    """Gets a value that indicates whether 128-bit vector operations are subject to hardware acceleration through JIT intrinsic support."""

    ALL_BITS_SET: System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]
    """Gets a new Vector128{T} with all bits set to 1."""

    COUNT: int
    """Gets the number of T that are in a Vector128{T}."""

    INDICES: System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]
    """Gets a new Vector128{T} with the elements set to their index."""

    IS_SUPPORTED: bool
    """Gets true if T is supported; otherwise, false."""

    ONE: System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]
    """Gets a new Vector128{T} with all elements initialized to one."""

    ZERO: System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]
    """Gets a new Vector128{T} with all elements initialized to zero."""

    @overload
    def __add__(self, right: System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]) -> System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]:
        """
        Adds two vectors to compute their sum.
        
        :param left: The vector to add with .
        :param right: The vector to add with .
        :returns: The sum of  and .
        """
        ...

    @overload
    def __add__(self) -> System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]:
        """
        Returns a given vector unchanged.
        
        :param value: The vector.
        """
        ...

    def __and__(self, right: System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]) -> System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]:
        """
        Computes the bitwise-and of two vectors.
        
        :param left: The vector to bitwise-and with .
        :param right: The vector to bitwise-and with .
        :returns: The bitwise-and of  and .
        """
        ...

    def __eq__(self, right: System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]) -> bool:
        """
        Compares two vectors to determine if all elements are equal.
        
        :param left: The vector to compare with .
        :param right: The vector to compare with .
        :returns: true if all elements in  were equal to the corresponding element in .
        """
        ...

    def __getitem__(self, index: int) -> System_Runtime_Intrinsics_Vector128_T:
        """
        Gets the element at the specified index.
        
        :param index: The index of the element to get.
        :returns: The value of the element at .
        """
        ...

    @overload
    def __iadd__(self, right: System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]) -> System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]:
        """
        Adds two vectors to compute their sum.
        
        :param left: The vector to add with .
        :param right: The vector to add with .
        :returns: The sum of  and .
        """
        ...

    @overload
    def __iadd__(self) -> System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]:
        """
        Returns a given vector unchanged.
        
        :param value: The vector.
        """
        ...

    def __iand__(self, right: System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]) -> System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]:
        """
        Computes the bitwise-and of two vectors.
        
        :param left: The vector to bitwise-and with .
        :param right: The vector to bitwise-and with .
        :returns: The bitwise-and of  and .
        """
        ...

    def __ilshift__(self, shift_count: int) -> System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]:
        """
        Shifts each element of a vector left by the specified amount.
        
        :param value: The vector whose elements are to be shifted.
        :param shift_count: The number of bits by which to shift each element.
        :returns: A vector whose elements where shifted left by .
        """
        ...

    @overload
    def __imul__(self, right: System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]) -> System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]:
        """
        Multiplies two vectors to compute their element-wise product.
        
        :param left: The vector to multiply with .
        :param right: The vector to multiply with .
        :returns: The element-wise product of  and .
        """
        ...

    @overload
    def __imul__(self, right: System_Runtime_Intrinsics_Vector128_T) -> System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]:
        """
        Multiplies a vector by a scalar to compute their product.
        
        :param left: The vector to multiply with .
        :param right: The scalar to multiply with .
        :returns: The product of  and .
        """
        ...

    @overload
    def __imul__(self, right: System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]) -> System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]:
        """
        Multiplies a vector by a scalar to compute their product.
        
        :param left: The scalar to multiply with .
        :param right: The vector to multiply with .
        :returns: The product of  and .
        """
        ...

    def __invert__(self) -> System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]:
        """
        Computes the ones-complement of a vector.
        
        :param vector: The vector whose ones-complement is to be computed.
        :returns: A vector whose elements are the ones-complement of the corresponding elements in .
        """
        ...

    def __ior__(self, right: System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]) -> System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]:
        """
        Computes the bitwise-or of two vectors.
        
        :param left: The vector to bitwise-or with .
        :param right: The vector to bitwise-or with .
        :returns: The bitwise-or of  and .
        """
        ...

    def __irshift__(self, shift_count: int) -> System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]:
        """
        Shifts (signed) each element of a vector right by the specified amount.
        
        :param value: The vector whose elements are to be shifted.
        :param shift_count: The number of bits by which to shift each element.
        :returns: A vector whose elements where shifted right by .
        """
        ...

    @overload
    def __isub__(self, right: System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]) -> System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]:
        """
        Subtracts two vectors to compute their difference.
        
        :param left: The vector from which  will be subtracted.
        :param right: The vector to subtract from .
        :returns: The difference of  and .
        """
        ...

    @overload
    def __isub__(self) -> System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]:
        """
        Computes the unary negation of a vector.
        
        :param vector: The vector to negate.
        :returns: A vector whose elements are the unary negation of the corresponding elements in .
        """
        ...

    @overload
    def __itruediv__(self, right: System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]) -> System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]:
        """
        Divides two vectors to compute their quotient.
        
        :param left: The vector that will be divided by .
        :param right: The vector that will divide .
        :returns: The quotient of  divided by .
        """
        ...

    @overload
    def __itruediv__(self, right: System_Runtime_Intrinsics_Vector128_T) -> System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]:
        """
        Divides a vector by a scalar to compute the per-element quotient.
        
        :param left: The vector that will be divided by .
        :param right: The scalar that will divide .
        :returns: The quotient of  divided by .
        """
        ...

    def __ixor__(self, right: System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]) -> System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]:
        """
        Computes the exclusive-or of two vectors.
        
        :param left: The vector to exclusive-or with .
        :param right: The vector to exclusive-or with .
        :returns: The exclusive-or of  and .
        """
        ...

    def __lshift__(self, shift_count: int) -> System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]:
        """
        Shifts each element of a vector left by the specified amount.
        
        :param value: The vector whose elements are to be shifted.
        :param shift_count: The number of bits by which to shift each element.
        :returns: A vector whose elements where shifted left by .
        """
        ...

    @overload
    def __mul__(self, right: System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]) -> System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]:
        """
        Multiplies two vectors to compute their element-wise product.
        
        :param left: The vector to multiply with .
        :param right: The vector to multiply with .
        :returns: The element-wise product of  and .
        """
        ...

    @overload
    def __mul__(self, right: System_Runtime_Intrinsics_Vector128_T) -> System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]:
        """
        Multiplies a vector by a scalar to compute their product.
        
        :param left: The vector to multiply with .
        :param right: The scalar to multiply with .
        :returns: The product of  and .
        """
        ...

    @overload
    def __mul__(self, right: System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]) -> System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]:
        """
        Multiplies a vector by a scalar to compute their product.
        
        :param left: The scalar to multiply with .
        :param right: The vector to multiply with .
        :returns: The product of  and .
        """
        ...

    def __ne__(self, right: System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]) -> bool:
        """
        Compares two vectors to determine if any elements are not equal.
        
        :param left: The vector to compare with .
        :param right: The vector to compare with .
        :returns: true if any elements in  was not equal to the corresponding element in .
        """
        ...

    def __or__(self, right: System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]) -> System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]:
        """
        Computes the bitwise-or of two vectors.
        
        :param left: The vector to bitwise-or with .
        :param right: The vector to bitwise-or with .
        :returns: The bitwise-or of  and .
        """
        ...

    def __rshift__(self, shift_count: int) -> System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]:
        """
        Shifts (signed) each element of a vector right by the specified amount.
        
        :param value: The vector whose elements are to be shifted.
        :param shift_count: The number of bits by which to shift each element.
        :returns: A vector whose elements where shifted right by .
        """
        ...

    @overload
    def __sub__(self, right: System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]) -> System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]:
        """
        Subtracts two vectors to compute their difference.
        
        :param left: The vector from which  will be subtracted.
        :param right: The vector to subtract from .
        :returns: The difference of  and .
        """
        ...

    @overload
    def __sub__(self) -> System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]:
        """
        Computes the unary negation of a vector.
        
        :param vector: The vector to negate.
        :returns: A vector whose elements are the unary negation of the corresponding elements in .
        """
        ...

    @overload
    def __truediv__(self, right: System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]) -> System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]:
        """
        Divides two vectors to compute their quotient.
        
        :param left: The vector that will be divided by .
        :param right: The vector that will divide .
        :returns: The quotient of  divided by .
        """
        ...

    @overload
    def __truediv__(self, right: System_Runtime_Intrinsics_Vector128_T) -> System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]:
        """
        Divides a vector by a scalar to compute the per-element quotient.
        
        :param left: The vector that will be divided by .
        :param right: The scalar that will divide .
        :returns: The quotient of  divided by .
        """
        ...

    def __xor__(self, right: System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]) -> System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]:
        """
        Computes the exclusive-or of two vectors.
        
        :param left: The vector to exclusive-or with .
        :param right: The vector to exclusive-or with .
        :returns: The exclusive-or of  and .
        """
        ...

    @staticmethod
    @overload
    def as_vector_128(value: System.Numerics.Vector2) -> System.Runtime.Intrinsics.Vector128[float]:
        """
        Reinterprets a Vector2 as a new Vector128<Single> with the new elements zeroed.
        
        :param value: The vector to reinterpret.
        :returns: reinterpreted as a new Vector128<Single> with the new elements zeroed.
        """
        ...

    @staticmethod
    @overload
    def as_vector_128(value: System.Numerics.Vector3) -> System.Runtime.Intrinsics.Vector128[float]:
        """
        Reinterprets a Vector3 as a new Vector128<Single> with the new elements zeroed.
        
        :param value: The vector to reinterpret.
        :returns: reinterpreted as a new Vector128<Single> with the new elements zeroed.
        """
        ...

    @staticmethod
    @overload
    def as_vector_128(value: System.Numerics.Vector4) -> System.Runtime.Intrinsics.Vector128[float]:
        """
        Reinterprets a Vector4 as a new Vector128<Single>.
        
        :param value: The vector to reinterpret.
        :returns: reinterpreted as a new Vector128<Single>.
        """
        ...

    @staticmethod
    @overload
    def as_vector_128_unsafe(value: System.Numerics.Vector2) -> System.Runtime.Intrinsics.Vector128[float]:
        """
        Reinterprets a Vector2 as a new Vector128<Single>, leaving the new elements undefined.
        
        :param value: The vector to reinterpret.
        :returns: reinterpreted as a new Vector128<Single>.
        """
        ...

    @staticmethod
    @overload
    def as_vector_128_unsafe(value: System.Numerics.Vector3) -> System.Runtime.Intrinsics.Vector128[float]:
        """
        Reinterprets a Vector3 as a new Vector128<Single>, leaving the new elements undefined.
        
        :param value: The vector to reinterpret.
        :returns: reinterpreted as a new Vector128<Single>.
        """
        ...

    @staticmethod
    def as_vector_2(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Numerics.Vector2:
        """
        Reinterprets a Vector128<Single> as a new Vector2.
        
        :param value: The vector to reinterpret.
        :returns: reinterpreted as a new Vector2.
        """
        ...

    @staticmethod
    def as_vector_3(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Numerics.Vector3:
        """
        Reinterprets a Vector128<Single> as a new Vector3.
        
        :param value: The vector to reinterpret.
        :returns: reinterpreted as a new Vector3.
        """
        ...

    @staticmethod
    def as_vector_4(value: System.Runtime.Intrinsics.Vector128[float]) -> System.Numerics.Vector4:
        """
        Reinterprets a Vector128<Single> as a new Vector4.
        
        :param value: The vector to reinterpret.
        :returns: reinterpreted as a new Vector4.
        """
        ...

    @staticmethod
    def ceiling(vector: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """
        Computes the ceiling of each element in a vector.
        
        :param vector: The vector that will have its ceiling computed.
        :returns: A vector whose elements are the ceiling of the elements in .
        """
        ...

    @staticmethod
    def convert_to_double(vector: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[float]:
        """
        Converts a Vector128<Int64> to a Vector128<Double>.
        
        :param vector: The vector to convert.
        :returns: The converted vector.
        """
        ...

    @staticmethod
    def convert_to_int_32(vector: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
        """
        Converts a Vector128<Single> to a Vector128<Int32> using saturation on overflow.
        
        :param vector: The vector to convert.
        :returns: The converted vector.
        """
        ...

    @staticmethod
    def convert_to_int_32_native(vector: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
        """
        Converts a Vector128<Single> to a Vector128<Int32> platform specific behavior on overflow.
        
        :param vector: The vector to convert.
        :returns: The converted vector.
        """
        ...

    @staticmethod
    def convert_to_int_64(vector: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
        """
        Converts a Vector128<Double> to a Vector128<Int64> using saturation on overflow.
        
        :param vector: The vector to convert.
        :returns: The converted vector.
        """
        ...

    @staticmethod
    def convert_to_int_64_native(vector: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
        """
        Converts a Vector128<Double> to a Vector128<Int64> using platform specific behavior on overflow.
        
        :param vector: The vector to convert.
        :returns: The converted vector.
        """
        ...

    @staticmethod
    def convert_to_single(vector: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[float]:
        """
        Converts a Vector128<Int32> to a Vector128<Single>.
        
        :param vector: The vector to convert.
        :returns: The converted vector.
        """
        ...

    @staticmethod
    def convert_to_u_int_32(vector: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
        """
        Converts a Vector128<Single> to a Vector128<UInt32> using saturation on overflow.
        
        :param vector: The vector to convert.
        :returns: The converted vector.
        """
        ...

    @staticmethod
    def convert_to_u_int_32_native(vector: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
        """
        Converts a Vector128<Single> to a Vector128<UInt32> using platform specific behavior on overflow.
        
        :param vector: The vector to convert.
        :returns: The converted vector.
        """
        ...

    @staticmethod
    def convert_to_u_int_64(vector: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
        """
        Converts a Vector128<Double> to a Vector128<UInt64> using saturation on overflow.
        
        :param vector: The vector to convert.
        :returns: The converted vector.
        """
        ...

    @staticmethod
    def convert_to_u_int_64_native(vector: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[int]:
        """
        Converts a Vector128<Double> to a Vector128<UInt64> using platform specific behavior on overflow.
        
        :param vector: The vector to convert.
        :returns: The converted vector.
        """
        ...

    @staticmethod
    def cos(vector: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def create(value: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """
        Creates a new Vector128<Byte> instance with all elements initialized to the specified value.
        
        :param value: The value that all elements will be initialized to.
        :returns: A new Vector128<Byte> with all elements initialized to .
        """
        ...

    @staticmethod
    @overload
    def create(value: float) -> System.Runtime.Intrinsics.Vector128[float]:
        """
        Creates a new Vector128<Double> instance with all elements initialized to the specified value.
        
        :param value: The value that all elements will be initialized to.
        :returns: A new Vector128<Double> with all elements initialized to .
        """
        ...

    @staticmethod
    @overload
    def create(value: System.IntPtr) -> System.Runtime.Intrinsics.Vector128[System.IntPtr]:
        """
        Creates a new Vector128<IntPtr> instance with all elements initialized to the specified value.
        
        :param value: The value that all elements will be initialized to.
        :returns: A new Vector128<IntPtr> with all elements initialized to .
        """
        ...

    @staticmethod
    @overload
    def create(value: System.UIntPtr) -> System.Runtime.Intrinsics.Vector128[System.UIntPtr]:
        """
        Creates a new Vector128<UIntPtr> instance with all elements initialized to the specified value.
        
        :param value: The value that all elements will be initialized to.
        :returns: A new Vector128<UIntPtr> with all elements initialized to .
        """
        ...

    @staticmethod
    @overload
    def create(e_0: int, e_1: int, e_2: int, e_3: int, e_4: int, e_5: int, e_6: int, e_7: int, e_8: int, e_9: int, e_10: int, e_11: int, e_12: int, e_13: int, e_14: int, e_15: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """
        Creates a new Vector128<Byte> instance with each element initialized to the corresponding specified value.
        
        :param e_0: The value that element 0 will be initialized to.
        :param e_1: The value that element 1 will be initialized to.
        :param e_2: The value that element 2 will be initialized to.
        :param e_3: The value that element 3 will be initialized to.
        :param e_4: The value that element 4 will be initialized to.
        :param e_5: The value that element 5 will be initialized to.
        :param e_6: The value that element 6 will be initialized to.
        :param e_7: The value that element 7 will be initialized to.
        :param e_8: The value that element 8 will be initialized to.
        :param e_9: The value that element 9 will be initialized to.
        :param e_10: The value that element 10 will be initialized to.
        :param e_11: The value that element 11 will be initialized to.
        :param e_12: The value that element 12 will be initialized to.
        :param e_13: The value that element 13 will be initialized to.
        :param e_14: The value that element 14 will be initialized to.
        :param e_15: The value that element 15 will be initialized to.
        :returns: A new Vector128<Byte> with each element initialized to corresponding specified value.
        """
        ...

    @staticmethod
    @overload
    def create(e_0: float, e_1: float) -> System.Runtime.Intrinsics.Vector128[float]:
        """
        Creates a new Vector128<Double> instance with each element initialized to the corresponding specified value.
        
        :param e_0: The value that element 0 will be initialized to.
        :param e_1: The value that element 1 will be initialized to.
        :returns: A new Vector128<Double> with each element initialized to corresponding specified value.
        """
        ...

    @staticmethod
    @overload
    def create(e_0: int, e_1: int, e_2: int, e_3: int, e_4: int, e_5: int, e_6: int, e_7: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """
        Creates a new Vector128<Int16> instance with each element initialized to the corresponding specified value.
        
        :param e_0: The value that element 0 will be initialized to.
        :param e_1: The value that element 1 will be initialized to.
        :param e_2: The value that element 2 will be initialized to.
        :param e_3: The value that element 3 will be initialized to.
        :param e_4: The value that element 4 will be initialized to.
        :param e_5: The value that element 5 will be initialized to.
        :param e_6: The value that element 6 will be initialized to.
        :param e_7: The value that element 7 will be initialized to.
        :returns: A new Vector128<Int16> with each element initialized to corresponding specified value.
        """
        ...

    @staticmethod
    @overload
    def create(e_0: int, e_1: int, e_2: int, e_3: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """
        Creates a new Vector128<Int32> instance with each element initialized to the corresponding specified value.
        
        :param e_0: The value that element 0 will be initialized to.
        :param e_1: The value that element 1 will be initialized to.
        :param e_2: The value that element 2 will be initialized to.
        :param e_3: The value that element 3 will be initialized to.
        :returns: A new Vector128<Int32> with each element initialized to corresponding specified value.
        """
        ...

    @staticmethod
    @overload
    def create(e_0: int, e_1: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """
        Creates a new Vector128<Int64> instance with each element initialized to the corresponding specified value.
        
        :param e_0: The value that element 0 will be initialized to.
        :param e_1: The value that element 1 will be initialized to.
        :returns: A new Vector128<Int64> with each element initialized to corresponding specified value.
        """
        ...

    @staticmethod
    @overload
    def create(e_0: float, e_1: float, e_2: float, e_3: float) -> System.Runtime.Intrinsics.Vector128[float]:
        """
        Creates a new Vector128<Single> instance with each element initialized to the corresponding specified value.
        
        :param e_0: The value that element 0 will be initialized to.
        :param e_1: The value that element 1 will be initialized to.
        :param e_2: The value that element 2 will be initialized to.
        :param e_3: The value that element 3 will be initialized to.
        :returns: A new Vector128<Single> with each element initialized to corresponding specified value.
        """
        ...

    @staticmethod
    @overload
    def create(lower: System.Runtime.Intrinsics.Vector64[int], upper: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """
        Creates a new Vector128<Byte> instance from two Vector64<Byte> instances.
        
        :param lower: The value that the lower 64-bits will be initialized to.
        :param upper: The value that the upper 64-bits will be initialized to.
        :returns: A new Vector128<Byte> initialized from  and .
        """
        ...

    @staticmethod
    @overload
    def create(lower: System.Runtime.Intrinsics.Vector64[float], upper: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """
        Creates a new Vector128<Double> instance from two Vector64<Double> instances.
        
        :param lower: The value that the lower 64-bits will be initialized to.
        :param upper: The value that the upper 64-bits will be initialized to.
        :returns: A new Vector128<Double> initialized from  and .
        """
        ...

    @staticmethod
    @overload
    def create(lower: System.Runtime.Intrinsics.Vector64[System.IntPtr], upper: System.Runtime.Intrinsics.Vector64[System.IntPtr]) -> System.Runtime.Intrinsics.Vector128[System.IntPtr]:
        """
        Creates a new Vector128<IntPtr> instance from two Vector64<IntPtr> instances.
        
        :param lower: The value that the lower 64-bits will be initialized to.
        :param upper: The value that the upper 64-bits will be initialized to.
        :returns: A new Vector128<IntPtr> initialized from  and .
        """
        ...

    @staticmethod
    @overload
    def create(lower: System.Runtime.Intrinsics.Vector64[System.UIntPtr], upper: System.Runtime.Intrinsics.Vector64[System.UIntPtr]) -> System.Runtime.Intrinsics.Vector128[System.UIntPtr]:
        """
        Creates a new Vector128<UIntPtr> instance from two Vector64<UIntPtr> instances.
        
        :param lower: The value that the lower 64-bits will be initialized to.
        :param upper: The value that the upper 64-bits will be initialized to.
        :returns: A new Vector128<UIntPtr> initialized from  and .
        """
        ...

    @staticmethod
    @overload
    def create_scalar(value: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """
        Creates a new Vector128<Byte> instance with the first element initialized to the specified value and the remaining elements initialized to zero.
        
        :param value: The value that element 0 will be initialized to.
        :returns: A new Vector128<Byte> instance with the first element initialized to  and the remaining elements initialized to zero.
        """
        ...

    @staticmethod
    @overload
    def create_scalar(value: float) -> System.Runtime.Intrinsics.Vector128[float]:
        """
        Creates a new Vector128<Double> instance with the first element initialized to the specified value and the remaining elements initialized to zero.
        
        :param value: The value that element 0 will be initialized to.
        :returns: A new Vector128<Double> instance with the first element initialized to  and the remaining elements initialized to zero.
        """
        ...

    @staticmethod
    @overload
    def create_scalar(value: System.IntPtr) -> System.Runtime.Intrinsics.Vector128[System.IntPtr]:
        """
        Creates a new Vector128<IntPtr> instance with the first element initialized to the specified value and the remaining elements initialized to zero.
        
        :param value: The value that element 0 will be initialized to.
        :returns: A new Vector128<IntPtr> instance with the first element initialized to  and the remaining elements initialized to zero.
        """
        ...

    @staticmethod
    @overload
    def create_scalar(value: System.UIntPtr) -> System.Runtime.Intrinsics.Vector128[System.UIntPtr]:
        """
        Creates a new Vector128<UIntPtr> instance with the first element initialized to the specified value and the remaining elements initialized to zero.
        
        :param value: The value that element 0 will be initialized to.
        :returns: A new Vector128<UIntPtr> instance with the first element initialized to  and the remaining elements initialized to zero.
        """
        ...

    @staticmethod
    @overload
    def create_scalar_unsafe(value: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """
        Creates a new Vector128<Byte> instance with the first element initialized to the specified value and the remaining elements left uninitialized.
        
        :param value: The value that element 0 will be initialized to.
        :returns: A new Vector128<Byte> instance with the first element initialized to  and the remaining elements left uninitialized.
        """
        ...

    @staticmethod
    @overload
    def create_scalar_unsafe(value: float) -> System.Runtime.Intrinsics.Vector128[float]:
        """
        Creates a new Vector128<Double> instance with the first element initialized to the specified value and the remaining elements left uninitialized.
        
        :param value: The value that element 0 will be initialized to.
        :returns: A new Vector128<Double> instance with the first element initialized to  and the remaining elements left uninitialized.
        """
        ...

    @staticmethod
    @overload
    def create_scalar_unsafe(value: System.IntPtr) -> System.Runtime.Intrinsics.Vector128[System.IntPtr]:
        """
        Creates a new Vector128<IntPtr> instance with the first element initialized to the specified value and the remaining elements left uninitialized.
        
        :param value: The value that element 0 will be initialized to.
        :returns: A new Vector128<IntPtr> instance with the first element initialized to  and the remaining elements left uninitialized.
        """
        ...

    @staticmethod
    @overload
    def create_scalar_unsafe(value: System.UIntPtr) -> System.Runtime.Intrinsics.Vector128[System.UIntPtr]:
        """
        Creates a new Vector128<UIntPtr> instance with the first element initialized to the specified value and the remaining elements left uninitialized.
        
        :param value: The value that element 0 will be initialized to.
        :returns: A new Vector128<UIntPtr> instance with the first element initialized to  and the remaining elements left uninitialized.
        """
        ...

    @staticmethod
    def degrees_to_radians(degrees: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        """
        Determines whether the specified object is equal to the current instance.
        
        :param obj: The object to compare with the current instance.
        :returns: true if  is a Vector128{T} and is equal to the current instance; otherwise, false.
        """
        ...

    @overload
    def equals(self, other: System.Runtime.Intrinsics.Vector128[System_Runtime_Intrinsics_Vector128_T]) -> bool:
        """
        Determines whether the specified Vector128{T} is equal to the current instance.
        
        :param other: The Vector128{T} to compare with the current instance.
        :returns: true if  is equal to the current instance; otherwise, false.
        """
        ...

    @staticmethod
    def exp(vector: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def floor(vector: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """
        Computes the floor of each element in a vector.
        
        :param vector: The vector that will have its floor computed.
        :returns: A vector whose elements are the floor of the elements in .
        """
        ...

    @staticmethod
    def fused_multiply_add(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float], addend: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    def get_hash_code(self) -> int:
        """
        Gets the hash code for the instance.
        
        :returns: The hash code for the instance.
        """
        ...

    @staticmethod
    def hypot(x: System.Runtime.Intrinsics.Vector128[float], y: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def lerp(x: System.Runtime.Intrinsics.Vector128[float], y: System.Runtime.Intrinsics.Vector128[float], amount: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def log(vector: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def log_2(vector: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def multiply_add_estimate(left: System.Runtime.Intrinsics.Vector128[float], right: System.Runtime.Intrinsics.Vector128[float], addend: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def narrow(lower: System.Runtime.Intrinsics.Vector128[float], upper: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """
        Narrows two Vector128<Double> instances into one Vector128<Single>.
        
        :param lower: The vector that will be narrowed to the lower half of the result vector.
        :param upper: The vector that will be narrowed to the upper half of the result vector.
        :returns: A Vector128<Single> containing elements narrowed from  and .
        """
        ...

    @staticmethod
    @overload
    def narrow(lower: System.Runtime.Intrinsics.Vector128[int], upper: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """
        Narrows two Vector128<Int16> instances into one Vector128<SByte>.
        
        :param lower: The vector that will be narrowed to the lower half of the result vector.
        :param upper: The vector that will be narrowed to the upper half of the result vector.
        :returns: A Vector128<SByte> containing elements narrowed from  and .
        """
        ...

    @staticmethod
    def radians_to_degrees(radians: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def round(vector: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def round(vector: System.Runtime.Intrinsics.Vector128[float], mode: System.MidpointRounding) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def shift_left(vector: System.Runtime.Intrinsics.Vector128[int], shift_count: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """
        Shifts each element of a vector left by the specified amount.
        
        :param vector: The vector whose elements are to be shifted.
        :param shift_count: The number of bits by which to shift each element.
        :returns: A vector whose elements where shifted left by .
        """
        ...

    @staticmethod
    @overload
    def shift_left(vector: System.Runtime.Intrinsics.Vector128[System.IntPtr], shift_count: int) -> System.Runtime.Intrinsics.Vector128[System.IntPtr]:
        """
        Shifts each element of a vector left by the specified amount.
        
        :param vector: The vector whose elements are to be shifted.
        :param shift_count: The number of bits by which to shift each element.
        :returns: A vector whose elements where shifted left by .
        """
        ...

    @staticmethod
    @overload
    def shift_left(vector: System.Runtime.Intrinsics.Vector128[System.UIntPtr], shift_count: int) -> System.Runtime.Intrinsics.Vector128[System.UIntPtr]:
        """
        Shifts each element of a vector left by the specified amount.
        
        :param vector: The vector whose elements are to be shifted.
        :param shift_count: The number of bits by which to shift each element.
        :returns: A vector whose elements where shifted left by .
        """
        ...

    @staticmethod
    @overload
    def shift_right_arithmetic(vector: System.Runtime.Intrinsics.Vector128[int], shift_count: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """
        Shifts (signed) each element of a vector right by the specified amount.
        
        :param vector: The vector whose elements are to be shifted.
        :param shift_count: The number of bits by which to shift each element.
        :returns: A vector whose elements where shifted right by .
        """
        ...

    @staticmethod
    @overload
    def shift_right_arithmetic(vector: System.Runtime.Intrinsics.Vector128[System.IntPtr], shift_count: int) -> System.Runtime.Intrinsics.Vector128[System.IntPtr]:
        """
        Shifts (signed) each element of a vector right by the specified amount.
        
        :param vector: The vector whose elements are to be shifted.
        :param shift_count: The number of bits by which to shift each element.
        :returns: A vector whose elements where shifted right by .
        """
        ...

    @staticmethod
    @overload
    def shift_right_logical(vector: System.Runtime.Intrinsics.Vector128[int], shift_count: int) -> System.Runtime.Intrinsics.Vector128[int]:
        """
        Shifts (unsigned) each element of a vector right by the specified amount.
        
        :param vector: The vector whose elements are to be shifted.
        :param shift_count: The number of bits by which to shift each element.
        :returns: A vector whose elements where shifted right by .
        """
        ...

    @staticmethod
    @overload
    def shift_right_logical(vector: System.Runtime.Intrinsics.Vector128[System.IntPtr], shift_count: int) -> System.Runtime.Intrinsics.Vector128[System.IntPtr]:
        """
        Shifts (unsigned) each element of a vector right by the specified amount.
        
        :param vector: The vector whose elements are to be shifted.
        :param shift_count: The number of bits by which to shift each element.
        :returns: A vector whose elements where shifted right by .
        """
        ...

    @staticmethod
    @overload
    def shift_right_logical(vector: System.Runtime.Intrinsics.Vector128[System.UIntPtr], shift_count: int) -> System.Runtime.Intrinsics.Vector128[System.UIntPtr]:
        """
        Shifts (unsigned) each element of a vector right by the specified amount.
        
        :param vector: The vector whose elements are to be shifted.
        :param shift_count: The number of bits by which to shift each element.
        :returns: A vector whose elements where shifted right by .
        """
        ...

    @staticmethod
    @overload
    def shuffle(vector: System.Runtime.Intrinsics.Vector128[int], indices: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """
        Creates a new vector by selecting values from an input vector using a set of indices.
        
        :param vector: The input vector from which values are selected.
        :param indices: The per-element indices used to select a value from .
        :returns: A new vector containing the values from  selected by the given .
        """
        ...

    @staticmethod
    @overload
    def shuffle(vector: System.Runtime.Intrinsics.Vector128[float], indices: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[float]:
        """
        Creates a new vector by selecting values from an input vector using a set of indices.
        
        :param vector: The input vector from which values are selected.
        :param indices: The per-element indices used to select a value from .
        :returns: A new vector containing the values from  selected by the given .
        """
        ...

    @staticmethod
    @overload
    def shuffle_native(vector: System.Runtime.Intrinsics.Vector128[int], indices: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """
        Creates a new vector by selecting values from an input vector using a set of indices.
        Behavior is platform-dependent for out-of-range indices.
        
        :param vector: The input vector from which values are selected.
        :param indices: The per-element indices used to select a value from .
        :returns: A new vector containing the values from  selected by the given .
        """
        ...

    @staticmethod
    @overload
    def shuffle_native(vector: System.Runtime.Intrinsics.Vector128[float], indices: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[float]:
        """
        Creates a new vector by selecting values from an input vector using a set of indices.
        
        :param vector: The input vector from which values are selected.
        :param indices: The per-element indices used to select a value from .
        :returns: A new vector containing the values from  selected by the given .
        """
        ...

    @staticmethod
    def sin(vector: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    def sin_cos(vector: System.Runtime.Intrinsics.Vector128[float]) -> System.ValueTuple[System.Runtime.Intrinsics.Vector128[float], System.Runtime.Intrinsics.Vector128[float]]:
        ...

    def to_string(self) -> str:
        """
        Converts the current instance to an equivalent string representation.
        
        :returns: An equivalent string representation of the current instance.
        """
        ...

    @staticmethod
    def truncate(vector: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        ...

    @staticmethod
    @overload
    def widen(source: System.Runtime.Intrinsics.Vector128[int]) -> System.ValueTuple[System.Runtime.Intrinsics.Vector128[int], System.Runtime.Intrinsics.Vector128[int]]:
        """
        Widens a Vector128<Byte> into two Vector128{UInt16} .
        
        :param source: The vector whose elements are to be widened.
        :returns: A pair of vectors that contain the widened lower and upper halves of .
        """
        ...

    @staticmethod
    @overload
    def widen(source: System.Runtime.Intrinsics.Vector128[float]) -> System.ValueTuple[System.Runtime.Intrinsics.Vector128[float], System.Runtime.Intrinsics.Vector128[float]]:
        """
        Widens a Vector128<Single> into two Vector128{Double} .
        
        :param source: The vector whose elements are to be widened.
        :returns: A pair of vectors that contain the widened lower and upper halves of .
        """
        ...

    @staticmethod
    @overload
    def widen_lower(source: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """
        Widens the lower half of a Vector128<Byte> into a Vector128{UInt16} .
        
        :param source: The vector whose elements are to be widened.
        :returns: A vector that contain the widened lower half of .
        """
        ...

    @staticmethod
    @overload
    def widen_lower(source: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """
        Widens the lower half of a Vector128<Single> into a Vector128{Double} .
        
        :param source: The vector whose elements are to be widened.
        :returns: A vector that contain the widened lower half of .
        """
        ...

    @staticmethod
    @overload
    def widen_upper(source: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector128[int]:
        """
        Widens the upper half of a Vector128<Byte> into a Vector128{UInt16} .
        
        :param source: The vector whose elements are to be widened.
        :returns: A vector that contain the widened upper half of .
        """
        ...

    @staticmethod
    @overload
    def widen_upper(source: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector128[float]:
        """
        Widens the upper half of a Vector128<Single> into a Vector128{Double} .
        
        :param source: The vector whose elements are to be widened.
        :returns: A vector that contain the widened upper half of .
        """
        ...


class Vector512(typing.Generic[System_Runtime_Intrinsics_Vector512_T], System.Runtime.Intrinsics.ISimdVector[System_Runtime_Intrinsics_Vector512, System_Runtime_Intrinsics_Vector512_T]):
    """Represents a 512-bit vector of a specified numeric type that is suitable for low-level optimization of parallel algorithms."""

    IS_HARDWARE_ACCELERATED: bool
    """Gets a value that indicates whether 512-bit vector operations are subject to hardware acceleration through JIT intrinsic support."""

    ALL_BITS_SET: System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]
    """Gets a new Vector512{T} with all bits set to 1."""

    COUNT: int
    """Gets the number of T that are in a Vector512{T}."""

    INDICES: System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]
    """Gets a new Vector512{T} with the elements set to their index."""

    IS_SUPPORTED: bool
    """Gets true if T is supported; otherwise, false."""

    ONE: System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]
    """Gets a new Vector512{T} with all elements initialized to one."""

    ZERO: System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]
    """Gets a new Vector512{T} with all elements initialized to zero."""

    @overload
    def __add__(self, right: System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]) -> System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]:
        """
        Adds two vectors to compute their sum.
        
        :param left: The vector to add with .
        :param right: The vector to add with .
        :returns: The sum of  and .
        """
        ...

    @overload
    def __add__(self) -> System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]:
        """
        Returns a given vector unchanged.
        
        :param value: The vector.
        """
        ...

    def __and__(self, right: System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]) -> System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]:
        """
        Computes the bitwise-and of two vectors.
        
        :param left: The vector to bitwise-and with .
        :param right: The vector to bitwise-and with .
        :returns: The bitwise-and of  and .
        """
        ...

    def __eq__(self, right: System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]) -> bool:
        """
        Compares two vectors to determine if all elements are equal.
        
        :param left: The vector to compare with .
        :param right: The vector to compare with .
        :returns: true if all elements in  were equal to the corresponding element in .
        """
        ...

    def __getitem__(self, index: int) -> System_Runtime_Intrinsics_Vector512_T:
        """
        Gets the element at the specified index.
        
        :param index: The index of the element to get.
        :returns: The value of the element at .
        """
        ...

    @overload
    def __iadd__(self, right: System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]) -> System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]:
        """
        Adds two vectors to compute their sum.
        
        :param left: The vector to add with .
        :param right: The vector to add with .
        :returns: The sum of  and .
        """
        ...

    @overload
    def __iadd__(self) -> System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]:
        """
        Returns a given vector unchanged.
        
        :param value: The vector.
        """
        ...

    def __iand__(self, right: System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]) -> System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]:
        """
        Computes the bitwise-and of two vectors.
        
        :param left: The vector to bitwise-and with .
        :param right: The vector to bitwise-and with .
        :returns: The bitwise-and of  and .
        """
        ...

    def __ilshift__(self, shift_count: int) -> System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]:
        """
        Shifts each element of a vector left by the specified amount.
        
        :param value: The vector whose elements are to be shifted.
        :param shift_count: The number of bits by which to shift each element.
        :returns: A vector whose elements where shifted left by .
        """
        ...

    @overload
    def __imul__(self, right: System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]) -> System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]:
        """
        Multiplies two vectors to compute their element-wise product.
        
        :param left: The vector to multiply with .
        :param right: The vector to multiply with .
        :returns: The element-wise product of  and .
        """
        ...

    @overload
    def __imul__(self, right: System_Runtime_Intrinsics_Vector512_T) -> System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]:
        """
        Multiplies a vector by a scalar to compute their product.
        
        :param left: The vector to multiply with .
        :param right: The scalar to multiply with .
        :returns: The product of  and .
        """
        ...

    @overload
    def __imul__(self, right: System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]) -> System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]:
        """
        Multiplies a vector by a scalar to compute their product.
        
        :param left: The scalar to multiply with .
        :param right: The vector to multiply with .
        :returns: The product of  and .
        """
        ...

    def __invert__(self) -> System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]:
        """
        Computes the ones-complement of a vector.
        
        :param vector: The vector whose ones-complement is to be computed.
        :returns: A vector whose elements are the ones-complement of the corresponding elements in .
        """
        ...

    def __ior__(self, right: System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]) -> System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]:
        """
        Computes the bitwise-or of two vectors.
        
        :param left: The vector to bitwise-or with .
        :param right: The vector to bitwise-or with .
        :returns: The bitwise-or of  and .
        """
        ...

    def __irshift__(self, shift_count: int) -> System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]:
        """
        Shifts (signed) each element of a vector right by the specified amount.
        
        :param value: The vector whose elements are to be shifted.
        :param shift_count: The number of bits by which to shift each element.
        :returns: A vector whose elements where shifted right by .
        """
        ...

    @overload
    def __isub__(self, right: System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]) -> System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]:
        """
        Subtracts two vectors to compute their difference.
        
        :param left: The vector from which  will be subtracted.
        :param right: The vector to subtract from .
        :returns: The difference of  and .
        """
        ...

    @overload
    def __isub__(self) -> System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]:
        """
        Computes the unary negation of a vector.
        
        :param vector: The vector to negate.
        :returns: A vector whose elements are the unary negation of the corresponding elements in .
        """
        ...

    @overload
    def __itruediv__(self, right: System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]) -> System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]:
        """
        Divides two vectors to compute their quotient.
        
        :param left: The vector that will be divided by .
        :param right: The vector that will divide .
        :returns: The quotient of  divided by .
        """
        ...

    @overload
    def __itruediv__(self, right: System_Runtime_Intrinsics_Vector512_T) -> System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]:
        """
        Divides a vector by a scalar to compute the per-element quotient.
        
        :param left: The vector that will be divided by .
        :param right: The scalar that will divide .
        :returns: The quotient of  divided by .
        """
        ...

    def __ixor__(self, right: System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]) -> System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]:
        """
        Computes the exclusive-or of two vectors.
        
        :param left: The vector to exclusive-or with .
        :param right: The vector to exclusive-or with .
        :returns: The exclusive-or of  and .
        """
        ...

    def __lshift__(self, shift_count: int) -> System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]:
        """
        Shifts each element of a vector left by the specified amount.
        
        :param value: The vector whose elements are to be shifted.
        :param shift_count: The number of bits by which to shift each element.
        :returns: A vector whose elements where shifted left by .
        """
        ...

    @overload
    def __mul__(self, right: System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]) -> System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]:
        """
        Multiplies two vectors to compute their element-wise product.
        
        :param left: The vector to multiply with .
        :param right: The vector to multiply with .
        :returns: The element-wise product of  and .
        """
        ...

    @overload
    def __mul__(self, right: System_Runtime_Intrinsics_Vector512_T) -> System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]:
        """
        Multiplies a vector by a scalar to compute their product.
        
        :param left: The vector to multiply with .
        :param right: The scalar to multiply with .
        :returns: The product of  and .
        """
        ...

    @overload
    def __mul__(self, right: System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]) -> System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]:
        """
        Multiplies a vector by a scalar to compute their product.
        
        :param left: The scalar to multiply with .
        :param right: The vector to multiply with .
        :returns: The product of  and .
        """
        ...

    def __ne__(self, right: System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]) -> bool:
        """
        Compares two vectors to determine if any elements are not equal.
        
        :param left: The vector to compare with .
        :param right: The vector to compare with .
        :returns: true if any elements in  was not equal to the corresponding element in .
        """
        ...

    def __or__(self, right: System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]) -> System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]:
        """
        Computes the bitwise-or of two vectors.
        
        :param left: The vector to bitwise-or with .
        :param right: The vector to bitwise-or with .
        :returns: The bitwise-or of  and .
        """
        ...

    def __rshift__(self, shift_count: int) -> System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]:
        """
        Shifts (signed) each element of a vector right by the specified amount.
        
        :param value: The vector whose elements are to be shifted.
        :param shift_count: The number of bits by which to shift each element.
        :returns: A vector whose elements where shifted right by .
        """
        ...

    @overload
    def __sub__(self, right: System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]) -> System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]:
        """
        Subtracts two vectors to compute their difference.
        
        :param left: The vector from which  will be subtracted.
        :param right: The vector to subtract from .
        :returns: The difference of  and .
        """
        ...

    @overload
    def __sub__(self) -> System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]:
        """
        Computes the unary negation of a vector.
        
        :param vector: The vector to negate.
        :returns: A vector whose elements are the unary negation of the corresponding elements in .
        """
        ...

    @overload
    def __truediv__(self, right: System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]) -> System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]:
        """
        Divides two vectors to compute their quotient.
        
        :param left: The vector that will be divided by .
        :param right: The vector that will divide .
        :returns: The quotient of  divided by .
        """
        ...

    @overload
    def __truediv__(self, right: System_Runtime_Intrinsics_Vector512_T) -> System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]:
        """
        Divides a vector by a scalar to compute the per-element quotient.
        
        :param left: The vector that will be divided by .
        :param right: The scalar that will divide .
        :returns: The quotient of  divided by .
        """
        ...

    def __xor__(self, right: System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]) -> System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]:
        """
        Computes the exclusive-or of two vectors.
        
        :param left: The vector to exclusive-or with .
        :param right: The vector to exclusive-or with .
        :returns: The exclusive-or of  and .
        """
        ...

    @staticmethod
    def ceiling(vector: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        """
        Computes the ceiling of each element in a vector.
        
        :param vector: The vector that will have its ceiling computed.
        :returns: A vector whose elements are the ceiling of the elements in .
        """
        ...

    @staticmethod
    def convert_to_double(vector: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[float]:
        """
        Converts a Vector512<Int64> to a Vector512<Double>.
        
        :param vector: The vector to convert.
        :returns: The converted vector.
        """
        ...

    @staticmethod
    def convert_to_int_32(vector: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[int]:
        """
        Converts a Vector512<Single> to a Vector512<Int32> using saturation on overflow.
        
        :param vector: The vector to convert.
        :returns: The converted vector.
        """
        ...

    @staticmethod
    def convert_to_int_32_native(vector: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[int]:
        """
        Converts a Vector512<Single> to a Vector512<Int32> using platform specific behavior on overflow.
        
        :param vector: The vector to convert.
        :returns: The converted vector.
        """
        ...

    @staticmethod
    def convert_to_int_64(vector: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[int]:
        """
        Converts a Vector512<Double> to a Vector512<Int64> using saturation on overflow.
        
        :param vector: The vector to convert.
        :returns: The converted vector.
        """
        ...

    @staticmethod
    def convert_to_int_64_native(vector: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[int]:
        """
        Converts a Vector512<Double> to a Vector512<Int64> using platform specific behavior on overflow.
        
        :param vector: The vector to convert.
        :returns: The converted vector.
        """
        ...

    @staticmethod
    def convert_to_single(vector: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[float]:
        """
        Converts a Vector512<Int32> to a Vector512<Single>.
        
        :param vector: The vector to convert.
        :returns: The converted vector.
        """
        ...

    @staticmethod
    def convert_to_u_int_32(vector: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[int]:
        """
        Converts a Vector512<Single> to a Vector512<UInt32> using saturation on overflow.
        
        :param vector: The vector to convert.
        :returns: The converted vector.
        """
        ...

    @staticmethod
    def convert_to_u_int_32_native(vector: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[int]:
        """
        Converts a Vector512<Single> to a Vector512<UInt32> using platform specific behavior on overflow.
        
        :param vector: The vector to convert.
        :returns: The converted vector.
        """
        ...

    @staticmethod
    def convert_to_u_int_64(vector: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[int]:
        """
        Converts a Vector512<Double> to a Vector512<UInt64> using saturation on overflow.
        
        :param vector: The vector to convert.
        :returns: The converted vector.
        """
        ...

    @staticmethod
    def convert_to_u_int_64_native(vector: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[int]:
        """
        Converts a Vector512<Double> to a Vector512<UInt64> using platform specific behavior on overflow.
        
        :param vector: The vector to convert.
        :returns: The converted vector.
        """
        ...

    @staticmethod
    def cos(vector: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    @overload
    def create(value: int) -> System.Runtime.Intrinsics.Vector512[int]:
        """
        Creates a new Vector512<Byte> instance with all elements initialized to the specified value.
        
        :param value: The value that all elements will be initialized to.
        :returns: A new Vector512<Byte> with all elements initialized to .
        """
        ...

    @staticmethod
    @overload
    def create(value: float) -> System.Runtime.Intrinsics.Vector512[float]:
        """
        Creates a new Vector512<Double> instance with all elements initialized to the specified value.
        
        :param value: The value that all elements will be initialized to.
        :returns: A new Vector512<Double> with all elements initialized to .
        """
        ...

    @staticmethod
    @overload
    def create(value: System.IntPtr) -> System.Runtime.Intrinsics.Vector512[System.IntPtr]:
        """
        Creates a new Vector512<IntPtr> instance with all elements initialized to the specified value.
        
        :param value: The value that all elements will be initialized to.
        :returns: A new Vector512<IntPtr> with all elements initialized to .
        """
        ...

    @staticmethod
    @overload
    def create(value: System.UIntPtr) -> System.Runtime.Intrinsics.Vector512[System.UIntPtr]:
        """
        Creates a new Vector512<UIntPtr> instance with all elements initialized to the specified value.
        
        :param value: The value that all elements will be initialized to.
        :returns: A new Vector512<UIntPtr> with all elements initialized to .
        """
        ...

    @staticmethod
    @overload
    def create(e_0: int, e_1: int, e_2: int, e_3: int, e_4: int, e_5: int, e_6: int, e_7: int, e_8: int, e_9: int, e_10: int, e_11: int, e_12: int, e_13: int, e_14: int, e_15: int, e_16: int, e_17: int, e_18: int, e_19: int, e_20: int, e_21: int, e_22: int, e_23: int, e_24: int, e_25: int, e_26: int, e_27: int, e_28: int, e_29: int, e_30: int, e_31: int, e_32: int, e_33: int, e_34: int, e_35: int, e_36: int, e_37: int, e_38: int, e_39: int, e_40: int, e_41: int, e_42: int, e_43: int, e_44: int, e_45: int, e_46: int, e_47: int, e_48: int, e_49: int, e_50: int, e_51: int, e_52: int, e_53: int, e_54: int, e_55: int, e_56: int, e_57: int, e_58: int, e_59: int, e_60: int, e_61: int, e_62: int, e_63: int) -> System.Runtime.Intrinsics.Vector512[int]:
        """
        Creates a new Vector512<Byte> instance with each element initialized to the corresponding specified value.
        
        :param e_0: The value that element 0 will be initialized to.
        :param e_1: The value that element 1 will be initialized to.
        :param e_2: The value that element 2 will be initialized to.
        :param e_3: The value that element 3 will be initialized to.
        :param e_4: The value that element 4 will be initialized to.
        :param e_5: The value that element 5 will be initialized to.
        :param e_6: The value that element 6 will be initialized to.
        :param e_7: The value that element 7 will be initialized to.
        :param e_8: The value that element 8 will be initialized to.
        :param e_9: The value that element 9 will be initialized to.
        :param e_10: The value that element 10 will be initialized to.
        :param e_11: The value that element 11 will be initialized to.
        :param e_12: The value that element 12 will be initialized to.
        :param e_13: The value that element 13 will be initialized to.
        :param e_14: The value that element 14 will be initialized to.
        :param e_15: The value that element 15 will be initialized to.
        :param e_16: The value that element 16 will be initialized to.
        :param e_17: The value that element 17 will be initialized to.
        :param e_18: The value that element 18 will be initialized to.
        :param e_19: The value that element 19 will be initialized to.
        :param e_20: The value that element 20 will be initialized to.
        :param e_21: The value that element 21 will be initialized to.
        :param e_22: The value that element 22 will be initialized to.
        :param e_23: The value that element 23 will be initialized to.
        :param e_24: The value that element 24 will be initialized to.
        :param e_25: The value that element 25 will be initialized to.
        :param e_26: The value that element 26 will be initialized to.
        :param e_27: The value that element 27 will be initialized to.
        :param e_28: The value that element 28 will be initialized to.
        :param e_29: The value that element 29 will be initialized to.
        :param e_30: The value that element 30 will be initialized to.
        :param e_31: The value that element 31 will be initialized to.
        :param e_32: The value that element 32 will be initialized to.
        :param e_33: The value that element 33 will be initialized to.
        :param e_34: The value that element 34 will be initialized to.
        :param e_35: The value that element 35 will be initialized to.
        :param e_36: The value that element 36 will be initialized to.
        :param e_37: The value that element 37 will be initialized to.
        :param e_38: The value that element 38 will be initialized to.
        :param e_39: The value that element 39 will be initialized to.
        :param e_40: The value that element 40 will be initialized to.
        :param e_41: The value that element 41 will be initialized to.
        :param e_42: The value that element 42 will be initialized to.
        :param e_43: The value that element 43 will be initialized to.
        :param e_44: The value that element 44 will be initialized to.
        :param e_45: The value that element 45 will be initialized to.
        :param e_46: The value that element 46 will be initialized to.
        :param e_47: The value that element 47 will be initialized to.
        :param e_48: The value that element 48 will be initialized to.
        :param e_49: The value that element 49 will be initialized to.
        :param e_50: The value that element 50 will be initialized to.
        :param e_51: The value that element 51 will be initialized to.
        :param e_52: The value that element 52 will be initialized to.
        :param e_53: The value that element 53 will be initialized to.
        :param e_54: The value that element 54 will be initialized to.
        :param e_55: The value that element 55 will be initialized to.
        :param e_56: The value that element 56 will be initialized to.
        :param e_57: The value that element 57 will be initialized to.
        :param e_58: The value that element 58 will be initialized to.
        :param e_59: The value that element 59 will be initialized to.
        :param e_60: The value that element 60 will be initialized to.
        :param e_61: The value that element 61 will be initialized to.
        :param e_62: The value that element 62 will be initialized to.
        :param e_63: The value that element 63 will be initialized to.
        :returns: A new Vector512<Byte> with each element initialized to corresponding specified value.
        """
        ...

    @staticmethod
    @overload
    def create(e_0: float, e_1: float, e_2: float, e_3: float, e_4: float, e_5: float, e_6: float, e_7: float) -> System.Runtime.Intrinsics.Vector512[float]:
        """
        Creates a new Vector512<Double> instance with each element initialized to the corresponding specified value.
        
        :param e_0: The value that element 0 will be initialized to.
        :param e_1: The value that element 1 will be initialized to.
        :param e_2: The value that element 2 will be initialized to.
        :param e_3: The value that element 3 will be initialized to.
        :param e_4: The value that element 4 will be initialized to.
        :param e_5: The value that element 5 will be initialized to.
        :param e_6: The value that element 6 will be initialized to.
        :param e_7: The value that element 7 will be initialized to.
        :returns: A new Vector512<Double> with each element initialized to corresponding specified value.
        """
        ...

    @staticmethod
    @overload
    def create(e_0: int, e_1: int, e_2: int, e_3: int, e_4: int, e_5: int, e_6: int, e_7: int, e_8: int, e_9: int, e_10: int, e_11: int, e_12: int, e_13: int, e_14: int, e_15: int, e_16: int, e_17: int, e_18: int, e_19: int, e_20: int, e_21: int, e_22: int, e_23: int, e_24: int, e_25: int, e_26: int, e_27: int, e_28: int, e_29: int, e_30: int, e_31: int) -> System.Runtime.Intrinsics.Vector512[int]:
        """
        Creates a new Vector512<Int16> instance with each element initialized to the corresponding specified value.
        
        :param e_0: The value that element 0 will be initialized to.
        :param e_1: The value that element 1 will be initialized to.
        :param e_2: The value that element 2 will be initialized to.
        :param e_3: The value that element 3 will be initialized to.
        :param e_4: The value that element 4 will be initialized to.
        :param e_5: The value that element 5 will be initialized to.
        :param e_6: The value that element 6 will be initialized to.
        :param e_7: The value that element 7 will be initialized to.
        :param e_8: The value that element 8 will be initialized to.
        :param e_9: The value that element 9 will be initialized to.
        :param e_10: The value that element 10 will be initialized to.
        :param e_11: The value that element 11 will be initialized to.
        :param e_12: The value that element 12 will be initialized to.
        :param e_13: The value that element 13 will be initialized to.
        :param e_14: The value that element 14 will be initialized to.
        :param e_15: The value that element 15 will be initialized to.
        :param e_16: The value that element 16 will be initialized to.
        :param e_17: The value that element 17 will be initialized to.
        :param e_18: The value that element 18 will be initialized to.
        :param e_19: The value that element 19 will be initialized to.
        :param e_20: The value that element 20 will be initialized to.
        :param e_21: The value that element 21 will be initialized to.
        :param e_22: The value that element 22 will be initialized to.
        :param e_23: The value that element 23 will be initialized to.
        :param e_24: The value that element 24 will be initialized to.
        :param e_25: The value that element 25 will be initialized to.
        :param e_26: The value that element 26 will be initialized to.
        :param e_27: The value that element 27 will be initialized to.
        :param e_28: The value that element 28 will be initialized to.
        :param e_29: The value that element 29 will be initialized to.
        :param e_30: The value that element 30 will be initialized to.
        :param e_31: The value that element 31 will be initialized to.
        :returns: A new Vector512<Int16> with each element initialized to corresponding specified value.
        """
        ...

    @staticmethod
    @overload
    def create(e_0: int, e_1: int, e_2: int, e_3: int, e_4: int, e_5: int, e_6: int, e_7: int, e_8: int, e_9: int, e_10: int, e_11: int, e_12: int, e_13: int, e_14: int, e_15: int) -> System.Runtime.Intrinsics.Vector512[int]:
        """
        Creates a new Vector512<Int32> instance with each element initialized to the corresponding specified value.
        
        :param e_0: The value that element 0 will be initialized to.
        :param e_1: The value that element 1 will be initialized to.
        :param e_2: The value that element 2 will be initialized to.
        :param e_3: The value that element 3 will be initialized to.
        :param e_4: The value that element 4 will be initialized to.
        :param e_5: The value that element 5 will be initialized to.
        :param e_6: The value that element 6 will be initialized to.
        :param e_7: The value that element 7 will be initialized to.
        :param e_8: The value that element 8 will be initialized to.
        :param e_9: The value that element 9 will be initialized to.
        :param e_10: The value that element 10 will be initialized to.
        :param e_11: The value that element 11 will be initialized to.
        :param e_12: The value that element 12 will be initialized to.
        :param e_13: The value that element 13 will be initialized to.
        :param e_14: The value that element 14 will be initialized to.
        :param e_15: The value that element 15 will be initialized to.
        :returns: A new Vector512<Int32> with each element initialized to corresponding specified value.
        """
        ...

    @staticmethod
    @overload
    def create(e_0: int, e_1: int, e_2: int, e_3: int, e_4: int, e_5: int, e_6: int, e_7: int) -> System.Runtime.Intrinsics.Vector512[int]:
        """
        Creates a new Vector512<Int64> instance with each element initialized to the corresponding specified value.
        
        :param e_0: The value that element 0 will be initialized to.
        :param e_1: The value that element 1 will be initialized to.
        :param e_2: The value that element 2 will be initialized to.
        :param e_3: The value that element 3 will be initialized to.
        :param e_4: The value that element 4 will be initialized to.
        :param e_5: The value that element 5 will be initialized to.
        :param e_6: The value that element 6 will be initialized to.
        :param e_7: The value that element 7 will be initialized to.
        :returns: A new Vector512<Int64> with each element initialized to corresponding specified value.
        """
        ...

    @staticmethod
    @overload
    def create(e_0: float, e_1: float, e_2: float, e_3: float, e_4: float, e_5: float, e_6: float, e_7: float, e_8: float, e_9: float, e_10: float, e_11: float, e_12: float, e_13: float, e_14: float, e_15: float) -> System.Runtime.Intrinsics.Vector512[float]:
        """
        Creates a new Vector512<Single> instance with each element initialized to the corresponding specified value.
        
        :param e_0: The value that element 0 will be initialized to.
        :param e_1: The value that element 1 will be initialized to.
        :param e_2: The value that element 2 will be initialized to.
        :param e_3: The value that element 3 will be initialized to.
        :param e_4: The value that element 4 will be initialized to.
        :param e_5: The value that element 5 will be initialized to.
        :param e_6: The value that element 6 will be initialized to.
        :param e_7: The value that element 7 will be initialized to.
        :param e_8: The value that element 8 will be initialized to.
        :param e_9: The value that element 9 will be initialized to.
        :param e_10: The value that element 10 will be initialized to.
        :param e_11: The value that element 11 will be initialized to.
        :param e_12: The value that element 12 will be initialized to.
        :param e_13: The value that element 13 will be initialized to.
        :param e_14: The value that element 14 will be initialized to.
        :param e_15: The value that element 15 will be initialized to.
        :returns: A new Vector512<Single> with each element initialized to corresponding specified value.
        """
        ...

    @staticmethod
    @overload
    def create(lower: System.Runtime.Intrinsics.Vector256[int], upper: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """
        Creates a new Vector512<Byte> instance from two Vector256<Byte> instances.
        
        :param lower: The value that the lower 256-bits will be initialized to.
        :param upper: The value that the upper 256-bits will be initialized to.
        :returns: A new Vector512<Byte> initialized from  and .
        """
        ...

    @staticmethod
    @overload
    def create(lower: System.Runtime.Intrinsics.Vector256[float], upper: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        """
        Creates a new Vector512<Double> instance from two Vector256<Double> instances.
        
        :param lower: The value that the lower 256-bits will be initialized to.
        :param upper: The value that the upper 256-bits will be initialized to.
        :returns: A new Vector512<Double> initialized from  and .
        """
        ...

    @staticmethod
    @overload
    def create(lower: System.Runtime.Intrinsics.Vector256[System.IntPtr], upper: System.Runtime.Intrinsics.Vector256[System.IntPtr]) -> System.Runtime.Intrinsics.Vector512[System.IntPtr]:
        """
        Creates a new Vector512<IntPtr> instance from two Vector256<IntPtr> instances.
        
        :param lower: The value that the lower 256-bits will be initialized to.
        :param upper: The value that the upper 256-bits will be initialized to.
        :returns: A new Vector512<IntPtr> initialized from  and .
        """
        ...

    @staticmethod
    @overload
    def create(lower: System.Runtime.Intrinsics.Vector256[System.UIntPtr], upper: System.Runtime.Intrinsics.Vector256[System.UIntPtr]) -> System.Runtime.Intrinsics.Vector512[System.UIntPtr]:
        """
        Creates a new Vector512<UIntPtr> instance from two Vector256<UIntPtr> instances.
        
        :param lower: The value that the lower 256-bits will be initialized to.
        :param upper: The value that the upper 256-bits will be initialized to.
        :returns: A new Vector512<UIntPtr> initialized from  and .
        """
        ...

    @staticmethod
    @overload
    def create_scalar(value: int) -> System.Runtime.Intrinsics.Vector512[int]:
        """
        Creates a new Vector512<Byte> instance with the first element initialized to the specified value and the remaining elements initialized to zero.
        
        :param value: The value that element 0 will be initialized to.
        :returns: A new Vector512<Byte> instance with the first element initialized to  and the remaining elements initialized to zero.
        """
        ...

    @staticmethod
    @overload
    def create_scalar(value: float) -> System.Runtime.Intrinsics.Vector512[float]:
        """
        Creates a new Vector512<Double> instance with the first element initialized to the specified value and the remaining elements initialized to zero.
        
        :param value: The value that element 0 will be initialized to.
        :returns: A new Vector512<Double> instance with the first element initialized to  and the remaining elements initialized to zero.
        """
        ...

    @staticmethod
    @overload
    def create_scalar(value: System.IntPtr) -> System.Runtime.Intrinsics.Vector512[System.IntPtr]:
        """
        Creates a new Vector512<IntPtr> instance with the first element initialized to the specified value and the remaining elements initialized to zero.
        
        :param value: The value that element 0 will be initialized to.
        :returns: A new Vector512<IntPtr> instance with the first element initialized to  and the remaining elements initialized to zero.
        """
        ...

    @staticmethod
    @overload
    def create_scalar(value: System.UIntPtr) -> System.Runtime.Intrinsics.Vector512[System.UIntPtr]:
        """
        Creates a new Vector512<UIntPtr> instance with the first element initialized to the specified value and the remaining elements initialized to zero.
        
        :param value: The value that element 0 will be initialized to.
        :returns: A new Vector512<UIntPtr> instance with the first element initialized to  and the remaining elements initialized to zero.
        """
        ...

    @staticmethod
    @overload
    def create_scalar_unsafe(value: int) -> System.Runtime.Intrinsics.Vector512[int]:
        """
        Creates a new Vector512<Byte> instance with the first element initialized to the specified value and the remaining elements left uninitialized.
        
        :param value: The value that element 0 will be initialized to.
        :returns: A new Vector512<Byte> instance with the first element initialized to  and the remaining elements left uninitialized.
        """
        ...

    @staticmethod
    @overload
    def create_scalar_unsafe(value: float) -> System.Runtime.Intrinsics.Vector512[float]:
        """
        Creates a new Vector512<Double> instance with the first element initialized to the specified value and the remaining elements left uninitialized.
        
        :param value: The value that element 0 will be initialized to.
        :returns: A new Vector512<Double> instance with the first element initialized to  and the remaining elements left uninitialized.
        """
        ...

    @staticmethod
    @overload
    def create_scalar_unsafe(value: System.IntPtr) -> System.Runtime.Intrinsics.Vector512[System.IntPtr]:
        """
        Creates a new Vector512<IntPtr> instance with the first element initialized to the specified value and the remaining elements left uninitialized.
        
        :param value: The value that element 0 will be initialized to.
        :returns: A new Vector512<IntPtr> instance with the first element initialized to  and the remaining elements left uninitialized.
        """
        ...

    @staticmethod
    @overload
    def create_scalar_unsafe(value: System.UIntPtr) -> System.Runtime.Intrinsics.Vector512[System.UIntPtr]:
        """
        Creates a new Vector512<UIntPtr> instance with the first element initialized to the specified value and the remaining elements left uninitialized.
        
        :param value: The value that element 0 will be initialized to.
        :returns: A new Vector512<UIntPtr> instance with the first element initialized to  and the remaining elements left uninitialized.
        """
        ...

    @staticmethod
    def degrees_to_radians(degrees: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        """
        Determines whether the specified object is equal to the current instance.
        
        :param obj: The object to compare with the current instance.
        :returns: true if  is a Vector512{T} and is equal to the current instance; otherwise, false.
        """
        ...

    @overload
    def equals(self, other: System.Runtime.Intrinsics.Vector512[System_Runtime_Intrinsics_Vector512_T]) -> bool:
        """
        Determines whether the specified Vector512{T} is equal to the current instance.
        
        :param other: The Vector512{T} to compare with the current instance.
        :returns: true if  is equal to the current instance; otherwise, false.
        """
        ...

    @staticmethod
    def exp(vector: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    def floor(vector: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        """
        Computes the floor of each element in a vector.
        
        :param vector: The vector that will have its floor computed.
        :returns: A vector whose elements are the floor of the elements in .
        """
        ...

    @staticmethod
    def fused_multiply_add(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float], addend: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    def get_hash_code(self) -> int:
        """
        Gets the hash code for the instance.
        
        :returns: The hash code for the instance.
        """
        ...

    @staticmethod
    def hypot(x: System.Runtime.Intrinsics.Vector512[float], y: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    def lerp(x: System.Runtime.Intrinsics.Vector512[float], y: System.Runtime.Intrinsics.Vector512[float], amount: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    def log(vector: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    def log_2(vector: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    def multiply_add_estimate(left: System.Runtime.Intrinsics.Vector512[float], right: System.Runtime.Intrinsics.Vector512[float], addend: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    @overload
    def narrow(lower: System.Runtime.Intrinsics.Vector512[float], upper: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        """
        Narrows two Vector512<Double> instances into one Vector512<Single>.
        
        :param lower: The vector that will be narrowed to the lower half of the result vector.
        :param upper: The vector that will be narrowed to the upper half of the result vector.
        :returns: A Vector512<Single> containing elements narrowed from  and .
        """
        ...

    @staticmethod
    @overload
    def narrow(lower: System.Runtime.Intrinsics.Vector512[int], upper: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """
        Narrows two Vector512<Int16> instances into one Vector512<SByte>.
        
        :param lower: The vector that will be narrowed to the lower half of the result vector.
        :param upper: The vector that will be narrowed to the upper half of the result vector.
        :returns: A Vector512<SByte> containing elements narrowed from  and .
        """
        ...

    @staticmethod
    def radians_to_degrees(radians: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    @overload
    def round(vector: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    @overload
    def round(vector: System.Runtime.Intrinsics.Vector512[float], mode: System.MidpointRounding) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    @overload
    def shift_left(vector: System.Runtime.Intrinsics.Vector512[int], shift_count: int) -> System.Runtime.Intrinsics.Vector512[int]:
        """
        Shifts each element of a vector left by the specified amount.
        
        :param vector: The vector whose elements are to be shifted.
        :param shift_count: The number of bits by which to shift each element.
        :returns: A vector whose elements where shifted left by .
        """
        ...

    @staticmethod
    @overload
    def shift_left(vector: System.Runtime.Intrinsics.Vector512[System.IntPtr], shift_count: int) -> System.Runtime.Intrinsics.Vector512[System.IntPtr]:
        """
        Shifts each element of a vector left by the specified amount.
        
        :param vector: The vector whose elements are to be shifted.
        :param shift_count: The number of bits by which to shift each element.
        :returns: A vector whose elements where shifted left by .
        """
        ...

    @staticmethod
    @overload
    def shift_left(vector: System.Runtime.Intrinsics.Vector512[System.UIntPtr], shift_count: int) -> System.Runtime.Intrinsics.Vector512[System.UIntPtr]:
        """
        Shifts each element of a vector left by the specified amount.
        
        :param vector: The vector whose elements are to be shifted.
        :param shift_count: The number of bits by which to shift each element.
        :returns: A vector whose elements where shifted left by .
        """
        ...

    @staticmethod
    @overload
    def shift_right_arithmetic(vector: System.Runtime.Intrinsics.Vector512[int], shift_count: int) -> System.Runtime.Intrinsics.Vector512[int]:
        """
        Shifts (signed) each element of a vector right by the specified amount.
        
        :param vector: The vector whose elements are to be shifted.
        :param shift_count: The number of bits by which to shift each element.
        :returns: A vector whose elements where shifted right by .
        """
        ...

    @staticmethod
    @overload
    def shift_right_arithmetic(vector: System.Runtime.Intrinsics.Vector512[System.IntPtr], shift_count: int) -> System.Runtime.Intrinsics.Vector512[System.IntPtr]:
        """
        Shifts (signed) each element of a vector right by the specified amount.
        
        :param vector: The vector whose elements are to be shifted.
        :param shift_count: The number of bits by which to shift each element.
        :returns: A vector whose elements where shifted right by .
        """
        ...

    @staticmethod
    @overload
    def shift_right_logical(vector: System.Runtime.Intrinsics.Vector512[int], shift_count: int) -> System.Runtime.Intrinsics.Vector512[int]:
        """
        Shifts (unsigned) each element of a vector right by the specified amount.
        
        :param vector: The vector whose elements are to be shifted.
        :param shift_count: The number of bits by which to shift each element.
        :returns: A vector whose elements where shifted right by .
        """
        ...

    @staticmethod
    @overload
    def shift_right_logical(vector: System.Runtime.Intrinsics.Vector512[System.IntPtr], shift_count: int) -> System.Runtime.Intrinsics.Vector512[System.IntPtr]:
        """
        Shifts (unsigned) each element of a vector right by the specified amount.
        
        :param vector: The vector whose elements are to be shifted.
        :param shift_count: The number of bits by which to shift each element.
        :returns: A vector whose elements where shifted right by .
        """
        ...

    @staticmethod
    @overload
    def shift_right_logical(vector: System.Runtime.Intrinsics.Vector512[System.UIntPtr], shift_count: int) -> System.Runtime.Intrinsics.Vector512[System.UIntPtr]:
        """
        Shifts (unsigned) each element of a vector right by the specified amount.
        
        :param vector: The vector whose elements are to be shifted.
        :param shift_count: The number of bits by which to shift each element.
        :returns: A vector whose elements where shifted right by .
        """
        ...

    @staticmethod
    @overload
    def shuffle(vector: System.Runtime.Intrinsics.Vector512[int], indices: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """
        Creates a new vector by selecting values from an input vector using a set of indices.
        
        :param vector: The input vector from which values are selected.
        :param indices: The per-element indices used to select a value from .
        :returns: A new vector containing the values from  selected by the given .
        """
        ...

    @staticmethod
    @overload
    def shuffle(vector: System.Runtime.Intrinsics.Vector512[float], indices: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[float]:
        """
        Creates a new vector by selecting values from an input vector using a set of indices.
        
        :param vector: The input vector from which values are selected.
        :param indices: The per-element indices used to select a value from .
        :returns: A new vector containing the values from  selected by the given .
        """
        ...

    @staticmethod
    @overload
    def shuffle_native(vector: System.Runtime.Intrinsics.Vector512[int], indices: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """
        Creates a new vector by selecting values from an input vector using a set of indices.
        Behavior is platform-dependent for out-of-range indices.
        
        :param vector: The input vector from which values are selected.
        :param indices: The per-element indices used to select a value from .
        :returns: A new vector containing the values from  selected by the given .
        """
        ...

    @staticmethod
    @overload
    def shuffle_native(vector: System.Runtime.Intrinsics.Vector512[float], indices: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[float]:
        """
        Creates a new vector by selecting values from an input vector using a set of indices.
        
        :param vector: The input vector from which values are selected.
        :param indices: The per-element indices used to select a value from .
        :returns: A new vector containing the values from  selected by the given .
        """
        ...

    @staticmethod
    def sin(vector: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    def sin_cos(vector: System.Runtime.Intrinsics.Vector512[float]) -> System.ValueTuple[System.Runtime.Intrinsics.Vector512[float], System.Runtime.Intrinsics.Vector512[float]]:
        ...

    def to_string(self) -> str:
        """
        Converts the current instance to an equivalent string representation.
        
        :returns: An equivalent string representation of the current instance.
        """
        ...

    @staticmethod
    def truncate(vector: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        ...

    @staticmethod
    @overload
    def widen(source: System.Runtime.Intrinsics.Vector512[int]) -> System.ValueTuple[System.Runtime.Intrinsics.Vector512[int], System.Runtime.Intrinsics.Vector512[int]]:
        """
        Widens a Vector512<Byte> into two Vector512{UInt16} .
        
        :param source: The vector whose elements are to be widened.
        :returns: A pair of vectors that contain the widened lower and upper halves of .
        """
        ...

    @staticmethod
    @overload
    def widen(source: System.Runtime.Intrinsics.Vector512[float]) -> System.ValueTuple[System.Runtime.Intrinsics.Vector512[float], System.Runtime.Intrinsics.Vector512[float]]:
        """
        Widens a Vector512<Single> into two Vector512{Double} .
        
        :param source: The vector whose elements are to be widened.
        :returns: A pair of vectors that contain the widened lower and upper halves of .
        """
        ...

    @staticmethod
    @overload
    def widen_lower(source: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """
        Widens the lower half of a Vector512<Byte> into a Vector512{UInt16} .
        
        :param source: The vector whose elements are to be widened.
        :returns: A vector that contain the widened lower half of .
        """
        ...

    @staticmethod
    @overload
    def widen_lower(source: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        """
        Widens the lower half of a Vector512<Single> into a Vector512{Double} .
        
        :param source: The vector whose elements are to be widened.
        :returns: A vector that contain the widened lower half of .
        """
        ...

    @staticmethod
    @overload
    def widen_upper(source: System.Runtime.Intrinsics.Vector512[int]) -> System.Runtime.Intrinsics.Vector512[int]:
        """
        Widens the upper half of a Vector512<Byte> into a Vector512{UInt16} .
        
        :param source: The vector whose elements are to be widened.
        :returns: A vector that contain the widened upper half of .
        """
        ...

    @staticmethod
    @overload
    def widen_upper(source: System.Runtime.Intrinsics.Vector512[float]) -> System.Runtime.Intrinsics.Vector512[float]:
        """
        Widens the upper half of a Vector512<Single> into a Vector512{Double} .
        
        :param source: The vector whose elements are to be widened.
        :returns: A vector that contain the widened upper half of .
        """
        ...


class Vector64(typing.Generic[System_Runtime_Intrinsics_Vector64_T], System.Runtime.Intrinsics.ISimdVector[System_Runtime_Intrinsics_Vector64, System_Runtime_Intrinsics_Vector64_T]):
    """Represents a 64-bit vector of a specified numeric type that is suitable for low-level optimization of parallel algorithms."""

    IS_HARDWARE_ACCELERATED: bool
    """Gets a value that indicates whether 64-bit vector operations are subject to hardware acceleration through JIT intrinsic support."""

    ALL_BITS_SET: System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]
    """Gets a new Vector64{T} with all bits set to 1."""

    COUNT: int
    """Gets the number of T that are in a Vector64{T}."""

    INDICES: System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]
    """Gets a new Vector64{T} with the elements set to their index."""

    IS_SUPPORTED: bool
    """Gets true if T is supported; otherwise, false."""

    ONE: System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]
    """Gets a new Vector64{T} with all elements initialized to one."""

    ZERO: System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]
    """Gets a new Vector64{T} with all elements initialized to zero."""

    @overload
    def __add__(self, right: System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]) -> System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]:
        """
        Adds two vectors to compute their sum.
        
        :param left: The vector to add with .
        :param right: The vector to add with .
        :returns: The sum of  and .
        """
        ...

    @overload
    def __add__(self) -> System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]:
        """
        Returns a given vector unchanged.
        
        :param value: The vector.
        """
        ...

    def __and__(self, right: System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]) -> System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]:
        """
        Computes the bitwise-and of two vectors.
        
        :param left: The vector to bitwise-and with .
        :param right: The vector to bitwise-and with .
        :returns: The bitwise-and of  and .
        """
        ...

    def __eq__(self, right: System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]) -> bool:
        """
        Compares two vectors to determine if all elements are equal.
        
        :param left: The vector to compare with .
        :param right: The vector to compare with .
        :returns: true if all elements in  were equal to the corresponding element in .
        """
        ...

    def __getitem__(self, index: int) -> System_Runtime_Intrinsics_Vector64_T:
        """
        Gets the element at the specified index.
        
        :param index: The index of the element to get.
        :returns: The value of the element at .
        """
        ...

    @overload
    def __iadd__(self, right: System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]) -> System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]:
        """
        Adds two vectors to compute their sum.
        
        :param left: The vector to add with .
        :param right: The vector to add with .
        :returns: The sum of  and .
        """
        ...

    @overload
    def __iadd__(self) -> System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]:
        """
        Returns a given vector unchanged.
        
        :param value: The vector.
        """
        ...

    def __iand__(self, right: System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]) -> System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]:
        """
        Computes the bitwise-and of two vectors.
        
        :param left: The vector to bitwise-and with .
        :param right: The vector to bitwise-and with .
        :returns: The bitwise-and of  and .
        """
        ...

    def __ilshift__(self, shift_count: int) -> System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]:
        """
        Shifts each element of a vector left by the specified amount.
        
        :param value: The vector whose elements are to be shifted.
        :param shift_count: The number of bits by which to shift each element.
        :returns: A vector whose elements where shifted left by .
        """
        ...

    @overload
    def __imul__(self, right: System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]) -> System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]:
        """
        Multiplies two vectors to compute their element-wise product.
        
        :param left: The vector to multiply with .
        :param right: The vector to multiply with .
        :returns: The element-wise product of  and .
        """
        ...

    @overload
    def __imul__(self, right: System_Runtime_Intrinsics_Vector64_T) -> System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]:
        """
        Multiplies a vector by a scalar to compute their product.
        
        :param left: The vector to multiply with .
        :param right: The scalar to multiply with .
        :returns: The product of  and .
        """
        ...

    @overload
    def __imul__(self, right: System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]) -> System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]:
        """
        Multiplies a vector by a scalar to compute their product.
        
        :param left: The scalar to multiply with .
        :param right: The vector to multiply with .
        :returns: The product of  and .
        """
        ...

    def __invert__(self) -> System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]:
        """
        Computes the ones-complement of a vector.
        
        :param vector: The vector whose ones-complement is to be computed.
        :returns: A vector whose elements are the ones-complement of the corresponding elements in .
        """
        ...

    def __ior__(self, right: System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]) -> System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]:
        """
        Computes the bitwise-or of two vectors.
        
        :param left: The vector to bitwise-or with .
        :param right: The vector to bitwise-or with .
        :returns: The bitwise-or of  and .
        """
        ...

    def __irshift__(self, shift_count: int) -> System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]:
        """
        Shifts (signed) each element of a vector right by the specified amount.
        
        :param value: The vector whose elements are to be shifted.
        :param shift_count: The number of bits by which to shift each element.
        :returns: A vector whose elements where shifted right by .
        """
        ...

    @overload
    def __isub__(self, right: System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]) -> System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]:
        """
        Subtracts two vectors to compute their difference.
        
        :param left: The vector from which  will be subtracted.
        :param right: The vector to subtract from .
        :returns: The difference of  and .
        """
        ...

    @overload
    def __isub__(self) -> System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]:
        """
        Computes the unary negation of a vector.
        
        :param vector: The vector to negate.
        :returns: A vector whose elements are the unary negation of the corresponding elements in .
        """
        ...

    @overload
    def __itruediv__(self, right: System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]) -> System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]:
        """
        Divides two vectors to compute their quotient.
        
        :param left: The vector that will be divided by .
        :param right: The vector that will divide .
        :returns: The quotient of  divided by .
        """
        ...

    @overload
    def __itruediv__(self, right: System_Runtime_Intrinsics_Vector64_T) -> System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]:
        """
        Divides a vector by a scalar to compute the per-element quotient.
        
        :param left: The vector that will be divided by .
        :param right: The scalar that will divide .
        :returns: The quotient of  divided by .
        """
        ...

    def __ixor__(self, right: System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]) -> System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]:
        """
        Computes the exclusive-or of two vectors.
        
        :param left: The vector to exclusive-or with .
        :param right: The vector to exclusive-or with .
        :returns: The exclusive-or of  and .
        """
        ...

    def __lshift__(self, shift_count: int) -> System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]:
        """
        Shifts each element of a vector left by the specified amount.
        
        :param value: The vector whose elements are to be shifted.
        :param shift_count: The number of bits by which to shift each element.
        :returns: A vector whose elements where shifted left by .
        """
        ...

    @overload
    def __mul__(self, right: System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]) -> System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]:
        """
        Multiplies two vectors to compute their element-wise product.
        
        :param left: The vector to multiply with .
        :param right: The vector to multiply with .
        :returns: The element-wise product of  and .
        """
        ...

    @overload
    def __mul__(self, right: System_Runtime_Intrinsics_Vector64_T) -> System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]:
        """
        Multiplies a vector by a scalar to compute their product.
        
        :param left: The vector to multiply with .
        :param right: The scalar to multiply with .
        :returns: The product of  and .
        """
        ...

    @overload
    def __mul__(self, right: System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]) -> System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]:
        """
        Multiplies a vector by a scalar to compute their product.
        
        :param left: The scalar to multiply with .
        :param right: The vector to multiply with .
        :returns: The product of  and .
        """
        ...

    def __ne__(self, right: System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]) -> bool:
        """
        Compares two vectors to determine if any elements are not equal.
        
        :param left: The vector to compare with .
        :param right: The vector to compare with .
        :returns: true if any elements in  was not equal to the corresponding element in .
        """
        ...

    def __or__(self, right: System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]) -> System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]:
        """
        Computes the bitwise-or of two vectors.
        
        :param left: The vector to bitwise-or with .
        :param right: The vector to bitwise-or with .
        :returns: The bitwise-or of  and .
        """
        ...

    def __rshift__(self, shift_count: int) -> System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]:
        """
        Shifts (signed) each element of a vector right by the specified amount.
        
        :param value: The vector whose elements are to be shifted.
        :param shift_count: The number of bits by which to shift each element.
        :returns: A vector whose elements where shifted right by .
        """
        ...

    @overload
    def __sub__(self, right: System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]) -> System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]:
        """
        Subtracts two vectors to compute their difference.
        
        :param left: The vector from which  will be subtracted.
        :param right: The vector to subtract from .
        :returns: The difference of  and .
        """
        ...

    @overload
    def __sub__(self) -> System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]:
        """
        Computes the unary negation of a vector.
        
        :param vector: The vector to negate.
        :returns: A vector whose elements are the unary negation of the corresponding elements in .
        """
        ...

    @overload
    def __truediv__(self, right: System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]) -> System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]:
        """
        Divides two vectors to compute their quotient.
        
        :param left: The vector that will be divided by .
        :param right: The vector that will divide .
        :returns: The quotient of  divided by .
        """
        ...

    @overload
    def __truediv__(self, right: System_Runtime_Intrinsics_Vector64_T) -> System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]:
        """
        Divides a vector by a scalar to compute the per-element quotient.
        
        :param left: The vector that will be divided by .
        :param right: The scalar that will divide .
        :returns: The quotient of  divided by .
        """
        ...

    def __xor__(self, right: System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]) -> System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]:
        """
        Computes the exclusive-or of two vectors.
        
        :param left: The vector to exclusive-or with .
        :param right: The vector to exclusive-or with .
        :returns: The exclusive-or of  and .
        """
        ...

    @staticmethod
    def ceiling(vector: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """
        Computes the ceiling of each element in a vector.
        
        :param vector: The vector that will have its ceiling computed.
        :returns: A vector whose elements are the ceiling of the elements in .
        """
        ...

    @staticmethod
    def convert_to_double(vector: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[float]:
        """
        Converts a Vector64<Int64> to a Vector64<Double>.
        
        :param vector: The vector to convert.
        :returns: The converted vector.
        """
        ...

    @staticmethod
    def convert_to_int_32(vector: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[int]:
        """
        Converts a Vector64<Single> to a Vector64<Int32> using saturation on overflow.
        
        :param vector: The vector to convert.
        :returns: The converted vector.
        """
        ...

    @staticmethod
    def convert_to_int_32_native(vector: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[int]:
        """
        Converts a Vector64<Single> to a Vector64<Int32> using platform specific behavior on overflow.
        
        :param vector: The vector to convert.
        :returns: The converted vector.
        """
        ...

    @staticmethod
    def convert_to_int_64(vector: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[int]:
        """
        Converts a Vector64<Double> to a Vector64<Int64> using saturation on overflow.
        
        :param vector: The vector to convert.
        :returns: The converted vector.
        """
        ...

    @staticmethod
    def convert_to_int_64_native(vector: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[int]:
        """
        Converts a Vector64<Double> to a Vector64<Int64> using platform specific behavior on overflow.
        
        :param vector: The vector to convert.
        :returns: The converted vector.
        """
        ...

    @staticmethod
    def convert_to_single(vector: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[float]:
        """
        Converts a Vector64<Int32> to a Vector64<Single>.
        
        :param vector: The vector to convert.
        :returns: The converted vector.
        """
        ...

    @staticmethod
    def convert_to_u_int_32(vector: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[int]:
        """
        Converts a Vector64<Single> to a Vector64<UInt32> using saturation on overflow.
        
        :param vector: The vector to convert.
        :returns: The converted vector.
        """
        ...

    @staticmethod
    def convert_to_u_int_32_native(vector: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[int]:
        """
        Converts a Vector64<Single> to a Vector64<UInt32> using platform specific behavior on overflow.
        
        :param vector: The vector to convert.
        :returns: The converted vector.
        """
        ...

    @staticmethod
    def convert_to_u_int_64(vector: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[int]:
        """
        Converts a Vector64<Double> to a Vector64<UInt64> using saturation on overflow.
        
        :param vector: The vector to convert.
        :returns: The converted vector.
        """
        ...

    @staticmethod
    def convert_to_u_int_64_native(vector: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[int]:
        """
        Converts a Vector64<Double> to a Vector64<UInt64> using platform specific behavior on overflow.
        
        :param vector: The vector to convert.
        :returns: The converted vector.
        """
        ...

    @staticmethod
    def cos(vector: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """
        Computes the cos of each element in a vector.
        
        :param vector: The vector that will have its Cos computed.
        :returns: A vector whose elements are the cos of the elements in .
        """
        ...

    @staticmethod
    @overload
    def create(value: int) -> System.Runtime.Intrinsics.Vector64[int]:
        """
        Creates a new Vector64<Byte> instance with all elements initialized to the specified value.
        
        :param value: The value that all elements will be initialized to.
        :returns: A new Vector64<Byte> with all elements initialized to .
        """
        ...

    @staticmethod
    @overload
    def create(value: float) -> System.Runtime.Intrinsics.Vector64[float]:
        """
        Creates a new Vector64<Double> instance with all elements initialized to the specified value.
        
        :param value: The value that all elements will be initialized to.
        :returns: A new Vector64<Double> with all elements initialized to .
        """
        ...

    @staticmethod
    @overload
    def create(value: System.IntPtr) -> System.Runtime.Intrinsics.Vector64[System.IntPtr]:
        """
        Creates a new Vector64<IntPtr> instance with all elements initialized to the specified value.
        
        :param value: The value that all elements will be initialized to.
        :returns: A new Vector64<IntPtr> with all elements initialized to .
        """
        ...

    @staticmethod
    @overload
    def create(value: System.UIntPtr) -> System.Runtime.Intrinsics.Vector64[System.UIntPtr]:
        """
        Creates a new Vector64<UIntPtr> instance with all elements initialized to the specified value.
        
        :param value: The value that all elements will be initialized to.
        :returns: A new Vector64<UIntPtr> with all elements initialized to .
        """
        ...

    @staticmethod
    @overload
    def create(e_0: int, e_1: int, e_2: int, e_3: int, e_4: int, e_5: int, e_6: int, e_7: int) -> System.Runtime.Intrinsics.Vector64[int]:
        """
        Creates a new Vector64<Byte> instance with each element initialized to the corresponding specified value.
        
        :param e_0: The value that element 0 will be initialized to.
        :param e_1: The value that element 1 will be initialized to.
        :param e_2: The value that element 2 will be initialized to.
        :param e_3: The value that element 3 will be initialized to.
        :param e_4: The value that element 4 will be initialized to.
        :param e_5: The value that element 5 will be initialized to.
        :param e_6: The value that element 6 will be initialized to.
        :param e_7: The value that element 7 will be initialized to.
        :returns: A new Vector64<Byte> with each element initialized to corresponding specified value.
        """
        ...

    @staticmethod
    @overload
    def create(e_0: int, e_1: int, e_2: int, e_3: int) -> System.Runtime.Intrinsics.Vector64[int]:
        """
        Creates a new Vector64<Int16> instance with each element initialized to the corresponding specified value.
        
        :param e_0: The value that element 0 will be initialized to.
        :param e_1: The value that element 1 will be initialized to.
        :param e_2: The value that element 2 will be initialized to.
        :param e_3: The value that element 3 will be initialized to.
        :returns: A new Vector64<Int16> with each element initialized to corresponding specified value.
        """
        ...

    @staticmethod
    @overload
    def create(e_0: int, e_1: int) -> System.Runtime.Intrinsics.Vector64[int]:
        """
        Creates a new Vector64<Int32> instance with each element initialized to the corresponding specified value.
        
        :param e_0: The value that element 0 will be initialized to.
        :param e_1: The value that element 1 will be initialized to.
        :returns: A new Vector64<Int32> with each element initialized to corresponding specified value.
        """
        ...

    @staticmethod
    @overload
    def create(e_0: float, e_1: float) -> System.Runtime.Intrinsics.Vector64[float]:
        """
        Creates a new Vector64<Single> instance with each element initialized to the corresponding specified value.
        
        :param e_0: The value that element 0 will be initialized to.
        :param e_1: The value that element 1 will be initialized to.
        :returns: A new Vector64<Single> with each element initialized to corresponding specified value.
        """
        ...

    @staticmethod
    @overload
    def create_scalar(value: int) -> System.Runtime.Intrinsics.Vector64[int]:
        """
        Creates a new Vector64<Byte> instance with the first element initialized to the specified value and the remaining elements initialized to zero.
        
        :param value: The value that element 0 will be initialized to.
        :returns: A new Vector64<Byte> instance with the first element initialized to  and the remaining elements initialized to zero.
        """
        ...

    @staticmethod
    @overload
    def create_scalar(value: float) -> System.Runtime.Intrinsics.Vector64[float]:
        """
        Creates a new Vector64<Double> instance with the first element initialized to the specified value and the remaining elements initialized to zero.
        
        :param value: The value that element 0 will be initialized to.
        :returns: A new Vector64<Double> instance with the first element initialized to  and the remaining elements initialized to zero.
        """
        ...

    @staticmethod
    @overload
    def create_scalar(value: System.IntPtr) -> System.Runtime.Intrinsics.Vector64[System.IntPtr]:
        """
        Creates a new Vector64<IntPtr> instance with the first element initialized to the specified value and the remaining elements initialized to zero.
        
        :param value: The value that element 0 will be initialized to.
        :returns: A new Vector64<IntPtr> instance with the first element initialized to  and the remaining elements initialized to zero.
        """
        ...

    @staticmethod
    @overload
    def create_scalar(value: System.UIntPtr) -> System.Runtime.Intrinsics.Vector64[System.UIntPtr]:
        """
        Creates a new Vector64<UIntPtr> instance with the first element initialized to the specified value and the remaining elements initialized to zero.
        
        :param value: The value that element 0 will be initialized to.
        :returns: A new Vector64<UIntPtr> instance with the first element initialized to  and the remaining elements initialized to zero.
        """
        ...

    @staticmethod
    @overload
    def create_scalar_unsafe(value: int) -> System.Runtime.Intrinsics.Vector64[int]:
        """
        Creates a new Vector64<Byte> instance with the first element initialized to the specified value and the remaining elements left uninitialized.
        
        :param value: The value that element 0 will be initialized to.
        :returns: A new Vector64<Byte> instance with the first element initialized to  and the remaining elements left uninitialized.
        """
        ...

    @staticmethod
    @overload
    def create_scalar_unsafe(value: float) -> System.Runtime.Intrinsics.Vector64[float]:
        """
        Creates a new Vector64<Double> instance with the first element initialized to the specified value and the remaining elements left uninitialized.
        
        :param value: The value that element 0 will be initialized to.
        :returns: A new Vector64<Double> instance with the first element initialized to  and the remaining elements left uninitialized.
        """
        ...

    @staticmethod
    @overload
    def create_scalar_unsafe(value: System.IntPtr) -> System.Runtime.Intrinsics.Vector64[System.IntPtr]:
        """
        Creates a new Vector64<IntPtr> instance with the first element initialized to the specified value and the remaining elements left uninitialized.
        
        :param value: The value that element 0 will be initialized to.
        :returns: A new Vector64<IntPtr> instance with the first element initialized to  and the remaining elements left uninitialized.
        """
        ...

    @staticmethod
    @overload
    def create_scalar_unsafe(value: System.UIntPtr) -> System.Runtime.Intrinsics.Vector64[System.UIntPtr]:
        """
        Creates a new Vector64<UIntPtr> instance with the first element initialized to the specified value and the remaining elements left uninitialized.
        
        :param value: The value that element 0 will be initialized to.
        :returns: A new Vector64<UIntPtr> instance with the first element initialized to  and the remaining elements left uninitialized.
        """
        ...

    @staticmethod
    def degrees_to_radians(degrees: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """
        Converts a given vector from degrees to radians.
        
        :param degrees: The vector to convert to radians.
        :returns: The vector of  converted to radians.
        """
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        """
        Determines whether the specified object is equal to the current instance.
        
        :param obj: The object to compare with the current instance.
        :returns: true if  is a Vector64{T} and is equal to the current instance; otherwise, false.
        """
        ...

    @overload
    def equals(self, other: System.Runtime.Intrinsics.Vector64[System_Runtime_Intrinsics_Vector64_T]) -> bool:
        """
        Determines whether the specified Vector64{T} is equal to the current instance.
        
        :param other: The Vector64{T} to compare with the current instance.
        :returns: true if  is equal to the current instance; otherwise, false.
        """
        ...

    @staticmethod
    def exp(vector: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """
        Computes the exp of each element in a vector.
        
        :param vector: The vector that will have its Exp computed.
        :returns: A vector whose elements are the exp of the elements in .
        """
        ...

    @staticmethod
    def floor(vector: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """
        Computes the floor of each element in a vector.
        
        :param vector: The vector that will have its floor computed.
        :returns: A vector whose elements are the floor of the elements in .
        """
        ...

    @staticmethod
    def fused_multiply_add(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float], addend: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """
        Computes ( * ) + , rounded as one ternary operation.
        
        :param left: The vector to be multiplied with .
        :param right: The vector to be multiplied with .
        :param addend: The vector to be added to the result of  multiplied by .
        :returns: ( * ) + , rounded as one ternary operation.
        """
        ...

    def get_hash_code(self) -> int:
        """
        Gets the hash code for the instance.
        
        :returns: The hash code for the instance.
        """
        ...

    @staticmethod
    def hypot(x: System.Runtime.Intrinsics.Vector64[float], y: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """
        Computes the hypotenuse given two vectors representing the lengths of the shorter sides in a right-angled triangle.
        
        :param x: The vector to square and add to .
        :param y: The vector to square and add to .
        :returns: The square root of -squared plus -squared.
        """
        ...

    @staticmethod
    def lerp(x: System.Runtime.Intrinsics.Vector64[float], y: System.Runtime.Intrinsics.Vector64[float], amount: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """
        Performs a linear interpolation between two vectors based on the given weighting.
        
        :param x: The first vector.
        :param y: The second vector.
        :param amount: A value between 0 and 1 that indicates the weight of .
        :returns: The interpolated vector.
        """
        ...

    @staticmethod
    def log(vector: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """
        Computes the log of each element in a vector.
        
        :param vector: The vector that will have its log computed.
        :returns: A vector whose elements are the log of the elements in .
        """
        ...

    @staticmethod
    def log_2(vector: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """
        Computes the log2 of each element in a vector.
        
        :param vector: The vector that will have its log2 computed.
        :returns: A vector whose elements are the log2 of the elements in .
        """
        ...

    @staticmethod
    def multiply_add_estimate(left: System.Runtime.Intrinsics.Vector64[float], right: System.Runtime.Intrinsics.Vector64[float], addend: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """
        Computes an estimate of ( * ) + .
        
        :param left: The vector to be multiplied with .
        :param right: The vector to be multiplied with .
        :param addend: The vector to be added to the result of  multiplied by .
        :returns: An estimate of ( * ) + .
        """
        ...

    @staticmethod
    @overload
    def narrow(lower: System.Runtime.Intrinsics.Vector64[float], upper: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """
        Narrows two Vector64<Double> instances into one Vector64<Single>.
        
        :param lower: The vector that will be narrowed to the lower half of the result vector.
        :param upper: The vector that will be narrowed to the upper half of the result vector.
        :returns: A Vector64<Single> containing elements narrowed from  and .
        """
        ...

    @staticmethod
    @overload
    def narrow(lower: System.Runtime.Intrinsics.Vector64[int], upper: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """
        Narrows two Vector64<Int16> instances into one Vector64<SByte>.
        
        :param lower: The vector that will be narrowed to the lower half of the result vector.
        :param upper: The vector that will be narrowed to the upper half of the result vector.
        :returns: A Vector64<SByte> containing elements narrowed from  and .
        """
        ...

    @staticmethod
    def radians_to_degrees(radians: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """
        Converts a given vector from radians to degrees.
        
        :param radians: The vector to convert to degrees.
        :returns: The vector of  converted to degrees.
        """
        ...

    @staticmethod
    @overload
    def round(vector: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        ...

    @staticmethod
    @overload
    def round(vector: System.Runtime.Intrinsics.Vector64[float], mode: System.MidpointRounding) -> System.Runtime.Intrinsics.Vector64[float]:
        """
        Rounds each element in a vector to the nearest integer using the specified rounding mode.
        
        :param vector: The vector to round.
        :param mode: The mode under which  should be rounded.
        :returns: The result of rounding each element in  to the nearest integer using .
        """
        ...

    @staticmethod
    @overload
    def shift_left(vector: System.Runtime.Intrinsics.Vector64[int], shift_count: int) -> System.Runtime.Intrinsics.Vector64[int]:
        """
        Shifts each element of a vector left by the specified amount.
        
        :param vector: The vector whose elements are to be shifted.
        :param shift_count: The number of bits by which to shift each element.
        :returns: A vector whose elements where shifted left by .
        """
        ...

    @staticmethod
    @overload
    def shift_left(vector: System.Runtime.Intrinsics.Vector64[System.IntPtr], shift_count: int) -> System.Runtime.Intrinsics.Vector64[System.IntPtr]:
        """
        Shifts each element of a vector left by the specified amount.
        
        :param vector: The vector whose elements are to be shifted.
        :param shift_count: The number of bits by which to shift each element.
        :returns: A vector whose elements where shifted left by .
        """
        ...

    @staticmethod
    @overload
    def shift_left(vector: System.Runtime.Intrinsics.Vector64[System.UIntPtr], shift_count: int) -> System.Runtime.Intrinsics.Vector64[System.UIntPtr]:
        """
        Shifts each element of a vector left by the specified amount.
        
        :param vector: The vector whose elements are to be shifted.
        :param shift_count: The number of bits by which to shift each element.
        :returns: A vector whose elements where shifted left by .
        """
        ...

    @staticmethod
    @overload
    def shift_right_arithmetic(vector: System.Runtime.Intrinsics.Vector64[int], shift_count: int) -> System.Runtime.Intrinsics.Vector64[int]:
        """
        Shifts (signed) each element of a vector right by the specified amount.
        
        :param vector: The vector whose elements are to be shifted.
        :param shift_count: The number of bits by which to shift each element.
        :returns: A vector whose elements where shifted right by .
        """
        ...

    @staticmethod
    @overload
    def shift_right_arithmetic(vector: System.Runtime.Intrinsics.Vector64[System.IntPtr], shift_count: int) -> System.Runtime.Intrinsics.Vector64[System.IntPtr]:
        """
        Shifts (signed) each element of a vector right by the specified amount.
        
        :param vector: The vector whose elements are to be shifted.
        :param shift_count: The number of bits by which to shift each element.
        :returns: A vector whose elements where shifted right by .
        """
        ...

    @staticmethod
    @overload
    def shift_right_logical(vector: System.Runtime.Intrinsics.Vector64[int], shift_count: int) -> System.Runtime.Intrinsics.Vector64[int]:
        """
        Shifts (unsigned) each element of a vector right by the specified amount.
        
        :param vector: The vector whose elements are to be shifted.
        :param shift_count: The number of bits by which to shift each element.
        :returns: A vector whose elements where shifted right by .
        """
        ...

    @staticmethod
    @overload
    def shift_right_logical(vector: System.Runtime.Intrinsics.Vector64[System.IntPtr], shift_count: int) -> System.Runtime.Intrinsics.Vector64[System.IntPtr]:
        """
        Shifts (unsigned) each element of a vector right by the specified amount.
        
        :param vector: The vector whose elements are to be shifted.
        :param shift_count: The number of bits by which to shift each element.
        :returns: A vector whose elements where shifted right by .
        """
        ...

    @staticmethod
    @overload
    def shift_right_logical(vector: System.Runtime.Intrinsics.Vector64[System.UIntPtr], shift_count: int) -> System.Runtime.Intrinsics.Vector64[System.UIntPtr]:
        """
        Shifts (unsigned) each element of a vector right by the specified amount.
        
        :param vector: The vector whose elements are to be shifted.
        :param shift_count: The number of bits by which to shift each element.
        :returns: A vector whose elements where shifted right by .
        """
        ...

    @staticmethod
    @overload
    def shuffle(vector: System.Runtime.Intrinsics.Vector64[int], indices: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """
        Creates a new vector by selecting values from an input vector using a set of indices.
        
        :param vector: The input vector from which values are selected.
        :param indices: The per-element indices used to select a value from .
        :returns: A new vector containing the values from  selected by the given .
        """
        ...

    @staticmethod
    @overload
    def shuffle(vector: System.Runtime.Intrinsics.Vector64[float], indices: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[float]:
        """
        Creates a new vector by selecting values from an input vector using a set of indices.
        
        :param vector: The input vector from which values are selected.
        :param indices: The per-element indices used to select a value from .
        :returns: A new vector containing the values from  selected by the given .
        """
        ...

    @staticmethod
    @overload
    def shuffle_native(vector: System.Runtime.Intrinsics.Vector64[int], indices: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """
        Creates a new vector by selecting values from an input vector using a set of indices.
        Behavior is platform-dependent for out-of-range indices.
        
        :param vector: The input vector from which values are selected.
        :param indices: The per-element indices used to select a value from .
        :returns: A new vector containing the values from  selected by the given .
        """
        ...

    @staticmethod
    @overload
    def shuffle_native(vector: System.Runtime.Intrinsics.Vector64[float], indices: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[float]:
        """
        Creates a new vector by selecting values from an input vector using a set of indices.
        
        :param vector: The input vector from which values are selected.
        :param indices: The per-element indices used to select a value from .
        :returns: A new vector containing the values from  selected by the given .
        """
        ...

    @staticmethod
    def sin(vector: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """
        Computes the sin of each element in a vector.
        
        :param vector: The vector that will have its Sin computed.
        :returns: A vector whose elements are the sin of the elements in .
        """
        ...

    @staticmethod
    def sin_cos(vector: System.Runtime.Intrinsics.Vector64[float]) -> System.ValueTuple[System.Runtime.Intrinsics.Vector64[float], System.Runtime.Intrinsics.Vector64[float]]:
        """
        Computes the sincos of each element in a vector.
        
        :param vector: The vector that will have its SinCos computed.
        :returns: A vector whose elements are the sincos of the elements in .
        """
        ...

    def to_string(self) -> str:
        """
        Converts the current instance to an equivalent string representation.
        
        :returns: An equivalent string representation of the current instance.
        """
        ...

    @staticmethod
    def truncate(vector: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        ...

    @staticmethod
    @overload
    def widen(source: System.Runtime.Intrinsics.Vector64[int]) -> System.ValueTuple[System.Runtime.Intrinsics.Vector64[int], System.Runtime.Intrinsics.Vector64[int]]:
        """
        Widens a Vector64<Byte> into two Vector64{UInt16} .
        
        :param source: The vector whose elements are to be widened.
        :returns: A pair of vectors that contain the widened lower and upper halves of .
        """
        ...

    @staticmethod
    @overload
    def widen(source: System.Runtime.Intrinsics.Vector64[float]) -> System.ValueTuple[System.Runtime.Intrinsics.Vector64[float], System.Runtime.Intrinsics.Vector64[float]]:
        """
        Widens a Vector64<Single> into two Vector64{Double} .
        
        :param source: The vector whose elements are to be widened.
        :returns: A pair of vectors that contain the widened lower and upper halves of .
        """
        ...

    @staticmethod
    @overload
    def widen_lower(source: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """
        Widens the lower half of a Vector64<Byte> into a Vector64{UInt16} .
        
        :param source: The vector whose elements are to be widened.
        :returns: A vector that contain the widened lower half of .
        """
        ...

    @staticmethod
    @overload
    def widen_lower(source: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """
        Widens the lower half of a Vector64<Single> into a Vector64{Double} .
        
        :param source: The vector whose elements are to be widened.
        :returns: A vector that contain the widened lower half of .
        """
        ...

    @staticmethod
    @overload
    def widen_upper(source: System.Runtime.Intrinsics.Vector64[int]) -> System.Runtime.Intrinsics.Vector64[int]:
        """
        Widens the upper half of a Vector64<Byte> into a Vector64{UInt16} .
        
        :param source: The vector whose elements are to be widened.
        :returns: A vector that contain the widened upper half of .
        """
        ...

    @staticmethod
    @overload
    def widen_upper(source: System.Runtime.Intrinsics.Vector64[float]) -> System.Runtime.Intrinsics.Vector64[float]:
        """
        Widens the upper half of a Vector64<Single> into a Vector64{Double} .
        
        :param source: The vector whose elements are to be widened.
        :returns: A vector that contain the widened upper half of .
        """
        ...


class Vector256(typing.Generic[System_Runtime_Intrinsics_Vector256_T], System.Runtime.Intrinsics.ISimdVector[System_Runtime_Intrinsics_Vector256, System_Runtime_Intrinsics_Vector256_T]):
    """Represents a 256-bit vector of a specified numeric type that is suitable for low-level optimization of parallel algorithms."""

    ALL_BITS_SET: System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]
    """Gets a new Vector256{T} with all bits set to 1."""

    COUNT: int
    """Gets the number of T that are in a Vector256{T}."""

    INDICES: System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]
    """Gets a new Vector256{T} with the elements set to their index."""

    IS_SUPPORTED: bool
    """Gets true if T is supported; otherwise, false."""

    ONE: System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]
    """Gets a new Vector256{T} with all elements initialized to one."""

    ZERO: System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]
    """Gets a new Vector256{T} with all elements initialized to zero."""

    IS_HARDWARE_ACCELERATED: bool
    """Gets a value that indicates whether 256-bit vector operations are subject to hardware acceleration through JIT intrinsic support."""

    @overload
    def __add__(self, right: System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]) -> System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]:
        """
        Adds two vectors to compute their sum.
        
        :param left: The vector to add with .
        :param right: The vector to add with .
        :returns: The sum of  and .
        """
        ...

    @overload
    def __add__(self) -> System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]:
        """
        Returns a given vector unchanged.
        
        :param value: The vector.
        """
        ...

    def __and__(self, right: System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]) -> System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]:
        """
        Computes the bitwise-and of two vectors.
        
        :param left: The vector to bitwise-and with .
        :param right: The vector to bitwise-and with .
        :returns: The bitwise-and of  and .
        """
        ...

    def __eq__(self, right: System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]) -> bool:
        """
        Compares two vectors to determine if all elements are equal.
        
        :param left: The vector to compare with .
        :param right: The vector to compare with .
        :returns: true if all elements in  were equal to the corresponding element in .
        """
        ...

    def __getitem__(self, index: int) -> System_Runtime_Intrinsics_Vector256_T:
        """
        Gets the element at the specified index.
        
        :param index: The index of the element to get.
        :returns: The value of the element at .
        """
        ...

    @overload
    def __iadd__(self, right: System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]) -> System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]:
        """
        Adds two vectors to compute their sum.
        
        :param left: The vector to add with .
        :param right: The vector to add with .
        :returns: The sum of  and .
        """
        ...

    @overload
    def __iadd__(self) -> System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]:
        """
        Returns a given vector unchanged.
        
        :param value: The vector.
        """
        ...

    def __iand__(self, right: System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]) -> System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]:
        """
        Computes the bitwise-and of two vectors.
        
        :param left: The vector to bitwise-and with .
        :param right: The vector to bitwise-and with .
        :returns: The bitwise-and of  and .
        """
        ...

    def __ilshift__(self, shift_count: int) -> System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]:
        """
        Shifts each element of a vector left by the specified amount.
        
        :param value: The vector whose elements are to be shifted.
        :param shift_count: The number of bits by which to shift each element.
        :returns: A vector whose elements where shifted left by .
        """
        ...

    @overload
    def __imul__(self, right: System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]) -> System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]:
        """
        Multiplies two vectors to compute their element-wise product.
        
        :param left: The vector to multiply with .
        :param right: The vector to multiply with .
        :returns: The element-wise product of  and .
        """
        ...

    @overload
    def __imul__(self, right: System_Runtime_Intrinsics_Vector256_T) -> System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]:
        """
        Multiplies a vector by a scalar to compute their product.
        
        :param left: The vector to multiply with .
        :param right: The scalar to multiply with .
        :returns: The product of  and .
        """
        ...

    @overload
    def __imul__(self, right: System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]) -> System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]:
        """
        Multiplies a vector by a scalar to compute their product.
        
        :param left: The scalar to multiply with .
        :param right: The vector to multiply with .
        :returns: The product of  and .
        """
        ...

    def __invert__(self) -> System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]:
        """
        Computes the ones-complement of a vector.
        
        :param vector: The vector whose ones-complement is to be computed.
        :returns: A vector whose elements are the ones-complement of the corresponding elements in .
        """
        ...

    def __ior__(self, right: System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]) -> System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]:
        """
        Computes the bitwise-or of two vectors.
        
        :param left: The vector to bitwise-or with .
        :param right: The vector to bitwise-or with .
        :returns: The bitwise-or of  and .
        """
        ...

    def __irshift__(self, shift_count: int) -> System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]:
        """
        Shifts (signed) each element of a vector right by the specified amount.
        
        :param value: The vector whose elements are to be shifted.
        :param shift_count: The number of bits by which to shift each element.
        :returns: A vector whose elements where shifted right by .
        """
        ...

    @overload
    def __isub__(self, right: System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]) -> System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]:
        """
        Subtracts two vectors to compute their difference.
        
        :param left: The vector from which  will be subtracted.
        :param right: The vector to subtract from .
        :returns: The difference of  and .
        """
        ...

    @overload
    def __isub__(self) -> System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]:
        """
        Computes the unary negation of a vector.
        
        :param vector: The vector to negate.
        :returns: A vector whose elements are the unary negation of the corresponding elements in .
        """
        ...

    @overload
    def __itruediv__(self, right: System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]) -> System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]:
        """
        Divides two vectors to compute their quotient.
        
        :param left: The vector that will be divided by .
        :param right: The vector that will divide .
        :returns: The quotient of  divided by .
        """
        ...

    @overload
    def __itruediv__(self, right: System_Runtime_Intrinsics_Vector256_T) -> System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]:
        """
        Divides a vector by a scalar to compute the per-element quotient.
        
        :param left: The vector that will be divided by .
        :param right: The scalar that will divide .
        :returns: The quotient of  divided by .
        """
        ...

    def __ixor__(self, right: System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]) -> System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]:
        """
        Computes the exclusive-or of two vectors.
        
        :param left: The vector to exclusive-or with .
        :param right: The vector to exclusive-or with .
        :returns: The exclusive-or of  and .
        """
        ...

    def __lshift__(self, shift_count: int) -> System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]:
        """
        Shifts each element of a vector left by the specified amount.
        
        :param value: The vector whose elements are to be shifted.
        :param shift_count: The number of bits by which to shift each element.
        :returns: A vector whose elements where shifted left by .
        """
        ...

    @overload
    def __mul__(self, right: System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]) -> System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]:
        """
        Multiplies two vectors to compute their element-wise product.
        
        :param left: The vector to multiply with .
        :param right: The vector to multiply with .
        :returns: The element-wise product of  and .
        """
        ...

    @overload
    def __mul__(self, right: System_Runtime_Intrinsics_Vector256_T) -> System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]:
        """
        Multiplies a vector by a scalar to compute their product.
        
        :param left: The vector to multiply with .
        :param right: The scalar to multiply with .
        :returns: The product of  and .
        """
        ...

    @overload
    def __mul__(self, right: System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]) -> System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]:
        """
        Multiplies a vector by a scalar to compute their product.
        
        :param left: The scalar to multiply with .
        :param right: The vector to multiply with .
        :returns: The product of  and .
        """
        ...

    def __ne__(self, right: System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]) -> bool:
        """
        Compares two vectors to determine if any elements are not equal.
        
        :param left: The vector to compare with .
        :param right: The vector to compare with .
        :returns: true if any elements in  was not equal to the corresponding element in .
        """
        ...

    def __or__(self, right: System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]) -> System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]:
        """
        Computes the bitwise-or of two vectors.
        
        :param left: The vector to bitwise-or with .
        :param right: The vector to bitwise-or with .
        :returns: The bitwise-or of  and .
        """
        ...

    def __rshift__(self, shift_count: int) -> System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]:
        """
        Shifts (signed) each element of a vector right by the specified amount.
        
        :param value: The vector whose elements are to be shifted.
        :param shift_count: The number of bits by which to shift each element.
        :returns: A vector whose elements where shifted right by .
        """
        ...

    @overload
    def __sub__(self, right: System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]) -> System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]:
        """
        Subtracts two vectors to compute their difference.
        
        :param left: The vector from which  will be subtracted.
        :param right: The vector to subtract from .
        :returns: The difference of  and .
        """
        ...

    @overload
    def __sub__(self) -> System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]:
        """
        Computes the unary negation of a vector.
        
        :param vector: The vector to negate.
        :returns: A vector whose elements are the unary negation of the corresponding elements in .
        """
        ...

    @overload
    def __truediv__(self, right: System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]) -> System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]:
        """
        Divides two vectors to compute their quotient.
        
        :param left: The vector that will be divided by .
        :param right: The vector that will divide .
        :returns: The quotient of  divided by .
        """
        ...

    @overload
    def __truediv__(self, right: System_Runtime_Intrinsics_Vector256_T) -> System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]:
        """
        Divides a vector by a scalar to compute the per-element quotient.
        
        :param left: The vector that will be divided by .
        :param right: The scalar that will divide .
        :returns: The quotient of  divided by .
        """
        ...

    def __xor__(self, right: System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]) -> System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]:
        """
        Computes the exclusive-or of two vectors.
        
        :param left: The vector to exclusive-or with .
        :param right: The vector to exclusive-or with .
        :returns: The exclusive-or of  and .
        """
        ...

    @staticmethod
    def ceiling(vector: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        """
        Computes the ceiling of each element in a vector.
        
        :param vector: The vector that will have its ceiling computed.
        :returns: A vector whose elements are the ceiling of the elements in .
        """
        ...

    @staticmethod
    def convert_to_double(vector: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[float]:
        """
        Converts a Vector256<Int64> to a Vector256<Double>.
        
        :param vector: The vector to convert.
        :returns: The converted vector.
        """
        ...

    @staticmethod
    def convert_to_int_32(vector: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[int]:
        """
        Converts a Vector256<Single> to a Vector256<Int32> using saturation on overflow.
        
        :param vector: The vector to convert.
        :returns: The converted vector.
        """
        ...

    @staticmethod
    def convert_to_int_32_native(vector: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[int]:
        """
        Converts a Vector256<Single> to a Vector256<Int32> using platform specific behavior on overflow.
        
        :param vector: The vector to convert.
        :returns: The converted vector.
        """
        ...

    @staticmethod
    def convert_to_int_64(vector: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[int]:
        """
        Converts a Vector256<Double> to a Vector256<Int64> using saturation on overflow.
        
        :param vector: The vector to convert.
        :returns: The converted vector.
        """
        ...

    @staticmethod
    def convert_to_int_64_native(vector: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[int]:
        """
        Converts a Vector256<Double> to a Vector256<Int64> using platform specific behavior on overflow.
        
        :param vector: The vector to convert.
        :returns: The converted vector.
        """
        ...

    @staticmethod
    def convert_to_single(vector: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[float]:
        """
        Converts a Vector256<Int32> to a Vector256<Single>.
        
        :param vector: The vector to convert.
        :returns: The converted vector.
        """
        ...

    @staticmethod
    def convert_to_u_int_32(vector: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[int]:
        """
        Converts a Vector256<Single> to a Vector256<UInt32> using saturation on overflow.
        
        :param vector: The vector to convert.
        :returns: The converted vector.
        """
        ...

    @staticmethod
    def convert_to_u_int_32_native(vector: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[int]:
        """
        Converts a Vector256<Single> to a Vector256<UInt32> using platform specific behavior on overflow.
        
        :param vector: The vector to convert.
        :returns: The converted vector.
        """
        ...

    @staticmethod
    def convert_to_u_int_64(vector: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[int]:
        """
        Converts a Vector256<Double> to a Vector256<UInt64> using saturation on overflow.
        
        :param vector: The vector to convert.
        :returns: The converted vector.
        """
        ...

    @staticmethod
    def convert_to_u_int_64_native(vector: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[int]:
        """
        Converts a Vector256<Double> to a Vector256<UInt64> using platform specific behavior on overflow.
        
        :param vector: The vector to convert.
        :returns: The converted vector.
        """
        ...

    @staticmethod
    def cos(vector: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    @overload
    def create(value: int) -> System.Runtime.Intrinsics.Vector256[int]:
        """
        Creates a new Vector256<Byte> instance with all elements initialized to the specified value.
        
        :param value: The value that all elements will be initialized to.
        :returns: A new Vector256<Byte> with all elements initialized to .
        """
        ...

    @staticmethod
    @overload
    def create(value: float) -> System.Runtime.Intrinsics.Vector256[float]:
        """
        Creates a new Vector256<Double> instance with all elements initialized to the specified value.
        
        :param value: The value that all elements will be initialized to.
        :returns: A new Vector256<Double> with all elements initialized to .
        """
        ...

    @staticmethod
    @overload
    def create(value: System.IntPtr) -> System.Runtime.Intrinsics.Vector256[System.IntPtr]:
        """
        Creates a new Vector256<IntPtr> instance with all elements initialized to the specified value.
        
        :param value: The value that all elements will be initialized to.
        :returns: A new Vector256<IntPtr> with all elements initialized to .
        """
        ...

    @staticmethod
    @overload
    def create(value: System.UIntPtr) -> System.Runtime.Intrinsics.Vector256[System.UIntPtr]:
        """
        Creates a new Vector256<UIntPtr> instance with all elements initialized to the specified value.
        
        :param value: The value that all elements will be initialized to.
        :returns: A new Vector256<UIntPtr> with all elements initialized to .
        """
        ...

    @staticmethod
    @overload
    def create(e_0: int, e_1: int, e_2: int, e_3: int, e_4: int, e_5: int, e_6: int, e_7: int, e_8: int, e_9: int, e_10: int, e_11: int, e_12: int, e_13: int, e_14: int, e_15: int, e_16: int, e_17: int, e_18: int, e_19: int, e_20: int, e_21: int, e_22: int, e_23: int, e_24: int, e_25: int, e_26: int, e_27: int, e_28: int, e_29: int, e_30: int, e_31: int) -> System.Runtime.Intrinsics.Vector256[int]:
        """
        Creates a new Vector256<Byte> instance with each element initialized to the corresponding specified value.
        
        :param e_0: The value that element 0 will be initialized to.
        :param e_1: The value that element 1 will be initialized to.
        :param e_2: The value that element 2 will be initialized to.
        :param e_3: The value that element 3 will be initialized to.
        :param e_4: The value that element 4 will be initialized to.
        :param e_5: The value that element 5 will be initialized to.
        :param e_6: The value that element 6 will be initialized to.
        :param e_7: The value that element 7 will be initialized to.
        :param e_8: The value that element 8 will be initialized to.
        :param e_9: The value that element 9 will be initialized to.
        :param e_10: The value that element 10 will be initialized to.
        :param e_11: The value that element 11 will be initialized to.
        :param e_12: The value that element 12 will be initialized to.
        :param e_13: The value that element 13 will be initialized to.
        :param e_14: The value that element 14 will be initialized to.
        :param e_15: The value that element 15 will be initialized to.
        :param e_16: The value that element 16 will be initialized to.
        :param e_17: The value that element 17 will be initialized to.
        :param e_18: The value that element 18 will be initialized to.
        :param e_19: The value that element 19 will be initialized to.
        :param e_20: The value that element 20 will be initialized to.
        :param e_21: The value that element 21 will be initialized to.
        :param e_22: The value that element 22 will be initialized to.
        :param e_23: The value that element 23 will be initialized to.
        :param e_24: The value that element 24 will be initialized to.
        :param e_25: The value that element 25 will be initialized to.
        :param e_26: The value that element 26 will be initialized to.
        :param e_27: The value that element 27 will be initialized to.
        :param e_28: The value that element 28 will be initialized to.
        :param e_29: The value that element 29 will be initialized to.
        :param e_30: The value that element 30 will be initialized to.
        :param e_31: The value that element 31 will be initialized to.
        :returns: A new Vector256<Byte> with each element initialized to corresponding specified value.
        """
        ...

    @staticmethod
    @overload
    def create(e_0: float, e_1: float, e_2: float, e_3: float) -> System.Runtime.Intrinsics.Vector256[float]:
        """
        Creates a new Vector256<Double> instance with each element initialized to the corresponding specified value.
        
        :param e_0: The value that element 0 will be initialized to.
        :param e_1: The value that element 1 will be initialized to.
        :param e_2: The value that element 2 will be initialized to.
        :param e_3: The value that element 3 will be initialized to.
        :returns: A new Vector256<Double> with each element initialized to corresponding specified value.
        """
        ...

    @staticmethod
    @overload
    def create(e_0: int, e_1: int, e_2: int, e_3: int, e_4: int, e_5: int, e_6: int, e_7: int, e_8: int, e_9: int, e_10: int, e_11: int, e_12: int, e_13: int, e_14: int, e_15: int) -> System.Runtime.Intrinsics.Vector256[int]:
        """
        Creates a new Vector256<Int16> instance with each element initialized to the corresponding specified value.
        
        :param e_0: The value that element 0 will be initialized to.
        :param e_1: The value that element 1 will be initialized to.
        :param e_2: The value that element 2 will be initialized to.
        :param e_3: The value that element 3 will be initialized to.
        :param e_4: The value that element 4 will be initialized to.
        :param e_5: The value that element 5 will be initialized to.
        :param e_6: The value that element 6 will be initialized to.
        :param e_7: The value that element 7 will be initialized to.
        :param e_8: The value that element 8 will be initialized to.
        :param e_9: The value that element 9 will be initialized to.
        :param e_10: The value that element 10 will be initialized to.
        :param e_11: The value that element 11 will be initialized to.
        :param e_12: The value that element 12 will be initialized to.
        :param e_13: The value that element 13 will be initialized to.
        :param e_14: The value that element 14 will be initialized to.
        :param e_15: The value that element 15 will be initialized to.
        :returns: A new Vector256<Int16> with each element initialized to corresponding specified value.
        """
        ...

    @staticmethod
    @overload
    def create(e_0: int, e_1: int, e_2: int, e_3: int, e_4: int, e_5: int, e_6: int, e_7: int) -> System.Runtime.Intrinsics.Vector256[int]:
        """
        Creates a new Vector256<Int32> instance with each element initialized to the corresponding specified value.
        
        :param e_0: The value that element 0 will be initialized to.
        :param e_1: The value that element 1 will be initialized to.
        :param e_2: The value that element 2 will be initialized to.
        :param e_3: The value that element 3 will be initialized to.
        :param e_4: The value that element 4 will be initialized to.
        :param e_5: The value that element 5 will be initialized to.
        :param e_6: The value that element 6 will be initialized to.
        :param e_7: The value that element 7 will be initialized to.
        :returns: A new Vector256<Int32> with each element initialized to corresponding specified value.
        """
        ...

    @staticmethod
    @overload
    def create(e_0: int, e_1: int, e_2: int, e_3: int) -> System.Runtime.Intrinsics.Vector256[int]:
        """
        Creates a new Vector256<Int64> instance with each element initialized to the corresponding specified value.
        
        :param e_0: The value that element 0 will be initialized to.
        :param e_1: The value that element 1 will be initialized to.
        :param e_2: The value that element 2 will be initialized to.
        :param e_3: The value that element 3 will be initialized to.
        :returns: A new Vector256<Int64> with each element initialized to corresponding specified value.
        """
        ...

    @staticmethod
    @overload
    def create(e_0: float, e_1: float, e_2: float, e_3: float, e_4: float, e_5: float, e_6: float, e_7: float) -> System.Runtime.Intrinsics.Vector256[float]:
        """
        Creates a new Vector256<Single> instance with each element initialized to the corresponding specified value.
        
        :param e_0: The value that element 0 will be initialized to.
        :param e_1: The value that element 1 will be initialized to.
        :param e_2: The value that element 2 will be initialized to.
        :param e_3: The value that element 3 will be initialized to.
        :param e_4: The value that element 4 will be initialized to.
        :param e_5: The value that element 5 will be initialized to.
        :param e_6: The value that element 6 will be initialized to.
        :param e_7: The value that element 7 will be initialized to.
        :returns: A new Vector256<Single> with each element initialized to corresponding specified value.
        """
        ...

    @staticmethod
    @overload
    def create(lower: System.Runtime.Intrinsics.Vector128[int], upper: System.Runtime.Intrinsics.Vector128[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """
        Creates a new Vector256<Byte> instance from two Vector128<Byte> instances.
        
        :param lower: The value that the lower 128-bits will be initialized to.
        :param upper: The value that the upper 128-bits will be initialized to.
        :returns: A new Vector256<Byte> initialized from  and .
        """
        ...

    @staticmethod
    @overload
    def create(lower: System.Runtime.Intrinsics.Vector128[float], upper: System.Runtime.Intrinsics.Vector128[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        """
        Creates a new Vector256<Double> instance from two Vector128<Double> instances.
        
        :param lower: The value that the lower 128-bits will be initialized to.
        :param upper: The value that the upper 128-bits will be initialized to.
        :returns: A new Vector256<Double> initialized from  and .
        """
        ...

    @staticmethod
    @overload
    def create(lower: System.Runtime.Intrinsics.Vector128[System.IntPtr], upper: System.Runtime.Intrinsics.Vector128[System.IntPtr]) -> System.Runtime.Intrinsics.Vector256[System.IntPtr]:
        """
        Creates a new Vector256<IntPtr> instance from two Vector128<IntPtr> instances.
        
        :param lower: The value that the lower 128-bits will be initialized to.
        :param upper: The value that the upper 128-bits will be initialized to.
        :returns: A new Vector256<IntPtr> initialized from  and .
        """
        ...

    @staticmethod
    @overload
    def create(lower: System.Runtime.Intrinsics.Vector128[System.UIntPtr], upper: System.Runtime.Intrinsics.Vector128[System.UIntPtr]) -> System.Runtime.Intrinsics.Vector256[System.UIntPtr]:
        """
        Creates a new Vector256<UIntPtr> instance from two Vector128<UIntPtr> instances.
        
        :param lower: The value that the lower 128-bits will be initialized to.
        :param upper: The value that the upper 128-bits will be initialized to.
        :returns: A new Vector256<UIntPtr> initialized from  and .
        """
        ...

    @staticmethod
    @overload
    def create_scalar(value: int) -> System.Runtime.Intrinsics.Vector256[int]:
        """
        Creates a new Vector256<Byte> instance with the first element initialized to the specified value and the remaining elements initialized to zero.
        
        :param value: The value that element 0 will be initialized to.
        :returns: A new Vector256<Byte> instance with the first element initialized to  and the remaining elements initialized to zero.
        """
        ...

    @staticmethod
    @overload
    def create_scalar(value: float) -> System.Runtime.Intrinsics.Vector256[float]:
        """
        Creates a new Vector256<Double> instance with the first element initialized to the specified value and the remaining elements initialized to zero.
        
        :param value: The value that element 0 will be initialized to.
        :returns: A new Vector256<Double> instance with the first element initialized to  and the remaining elements initialized to zero.
        """
        ...

    @staticmethod
    @overload
    def create_scalar(value: System.IntPtr) -> System.Runtime.Intrinsics.Vector256[System.IntPtr]:
        """
        Creates a new Vector256<IntPtr> instance with the first element initialized to the specified value and the remaining elements initialized to zero.
        
        :param value: The value that element 0 will be initialized to.
        :returns: A new Vector256<IntPtr> instance with the first element initialized to  and the remaining elements initialized to zero.
        """
        ...

    @staticmethod
    @overload
    def create_scalar(value: System.UIntPtr) -> System.Runtime.Intrinsics.Vector256[System.UIntPtr]:
        """
        Creates a new Vector256<UIntPtr> instance with the first element initialized to the specified value and the remaining elements initialized to zero.
        
        :param value: The value that element 0 will be initialized to.
        :returns: A new Vector256<UIntPtr> instance with the first element initialized to  and the remaining elements initialized to zero.
        """
        ...

    @staticmethod
    @overload
    def create_scalar_unsafe(value: int) -> System.Runtime.Intrinsics.Vector256[int]:
        """
        Creates a new Vector256<Byte> instance with the first element initialized to the specified value and the remaining elements left uninitialized.
        
        :param value: The value that element 0 will be initialized to.
        :returns: A new Vector256<Byte> instance with the first element initialized to  and the remaining elements left uninitialized.
        """
        ...

    @staticmethod
    @overload
    def create_scalar_unsafe(value: float) -> System.Runtime.Intrinsics.Vector256[float]:
        """
        Creates a new Vector256<Double> instance with the first element initialized to the specified value and the remaining elements left uninitialized.
        
        :param value: The value that element 0 will be initialized to.
        :returns: A new Vector256<Double> instance with the first element initialized to  and the remaining elements left uninitialized.
        """
        ...

    @staticmethod
    @overload
    def create_scalar_unsafe(value: System.IntPtr) -> System.Runtime.Intrinsics.Vector256[System.IntPtr]:
        """
        Creates a new Vector256<IntPtr> instance with the first element initialized to the specified value and the remaining elements left uninitialized.
        
        :param value: The value that element 0 will be initialized to.
        :returns: A new Vector256<IntPtr> instance with the first element initialized to  and the remaining elements left uninitialized.
        """
        ...

    @staticmethod
    @overload
    def create_scalar_unsafe(value: System.UIntPtr) -> System.Runtime.Intrinsics.Vector256[System.UIntPtr]:
        """
        Creates a new Vector256<UIntPtr> instance with the first element initialized to the specified value and the remaining elements left uninitialized.
        
        :param value: The value that element 0 will be initialized to.
        :returns: A new Vector256<UIntPtr> instance with the first element initialized to  and the remaining elements left uninitialized.
        """
        ...

    @staticmethod
    def degrees_to_radians(degrees: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        """
        Determines whether the specified object is equal to the current instance.
        
        :param obj: The object to compare with the current instance.
        :returns: true if  is a Vector256{T} and is equal to the current instance; otherwise, false.
        """
        ...

    @overload
    def equals(self, other: System.Runtime.Intrinsics.Vector256[System_Runtime_Intrinsics_Vector256_T]) -> bool:
        """
        Determines whether the specified Vector256{T} is equal to the current instance.
        
        :param other: The Vector256{T} to compare with the current instance.
        :returns: true if  is equal to the current instance; otherwise, false.
        """
        ...

    @staticmethod
    def exp(vector: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    def floor(vector: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        """
        Computes the floor of each element in a vector.
        
        :param vector: The vector that will have its floor computed.
        :returns: A vector whose elements are the floor of the elements in .
        """
        ...

    @staticmethod
    def fused_multiply_add(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float], addend: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    def get_hash_code(self) -> int:
        """
        Gets the hash code for the instance.
        
        :returns: The hash code for the instance.
        """
        ...

    @staticmethod
    def hypot(x: System.Runtime.Intrinsics.Vector256[float], y: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    def lerp(x: System.Runtime.Intrinsics.Vector256[float], y: System.Runtime.Intrinsics.Vector256[float], amount: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    def log(vector: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    def log_2(vector: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    def multiply_add_estimate(left: System.Runtime.Intrinsics.Vector256[float], right: System.Runtime.Intrinsics.Vector256[float], addend: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    @overload
    def narrow(lower: System.Runtime.Intrinsics.Vector256[float], upper: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        """
        Narrows two Vector256<Double> instances into one Vector256<Single>.
        
        :param lower: The vector that will be narrowed to the lower half of the result vector.
        :param upper: The vector that will be narrowed to the upper half of the result vector.
        :returns: A Vector256<Single> containing elements narrowed from  and .
        """
        ...

    @staticmethod
    @overload
    def narrow(lower: System.Runtime.Intrinsics.Vector256[int], upper: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """
        Narrows two Vector256<Int16> instances into one Vector256<SByte>.
        
        :param lower: The vector that will be narrowed to the lower half of the result vector.
        :param upper: The vector that will be narrowed to the upper half of the result vector.
        :returns: A Vector256<SByte> containing elements narrowed from  and .
        """
        ...

    @staticmethod
    def radians_to_degrees(radians: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    @overload
    def round(vector: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    @overload
    def round(vector: System.Runtime.Intrinsics.Vector256[float], mode: System.MidpointRounding) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    @overload
    def shift_left(vector: System.Runtime.Intrinsics.Vector256[int], shift_count: int) -> System.Runtime.Intrinsics.Vector256[int]:
        """
        Shifts each element of a vector left by the specified amount.
        
        :param vector: The vector whose elements are to be shifted.
        :param shift_count: The number of bits by which to shift each element.
        :returns: A vector whose elements where shifted left by .
        """
        ...

    @staticmethod
    @overload
    def shift_left(vector: System.Runtime.Intrinsics.Vector256[System.IntPtr], shift_count: int) -> System.Runtime.Intrinsics.Vector256[System.IntPtr]:
        """
        Shifts each element of a vector left by the specified amount.
        
        :param vector: The vector whose elements are to be shifted.
        :param shift_count: The number of bits by which to shift each element.
        :returns: A vector whose elements where shifted left by .
        """
        ...

    @staticmethod
    @overload
    def shift_left(vector: System.Runtime.Intrinsics.Vector256[System.UIntPtr], shift_count: int) -> System.Runtime.Intrinsics.Vector256[System.UIntPtr]:
        """
        Shifts each element of a vector left by the specified amount.
        
        :param vector: The vector whose elements are to be shifted.
        :param shift_count: The number of bits by which to shift each element.
        :returns: A vector whose elements where shifted left by .
        """
        ...

    @staticmethod
    @overload
    def shift_right_arithmetic(vector: System.Runtime.Intrinsics.Vector256[int], shift_count: int) -> System.Runtime.Intrinsics.Vector256[int]:
        """
        Shifts (signed) each element of a vector right by the specified amount.
        
        :param vector: The vector whose elements are to be shifted.
        :param shift_count: The number of bits by which to shift each element.
        :returns: A vector whose elements where shifted right by .
        """
        ...

    @staticmethod
    @overload
    def shift_right_arithmetic(vector: System.Runtime.Intrinsics.Vector256[System.IntPtr], shift_count: int) -> System.Runtime.Intrinsics.Vector256[System.IntPtr]:
        """
        Shifts (signed) each element of a vector right by the specified amount.
        
        :param vector: The vector whose elements are to be shifted.
        :param shift_count: The number of bits by which to shift each element.
        :returns: A vector whose elements where shifted right by .
        """
        ...

    @staticmethod
    @overload
    def shift_right_logical(vector: System.Runtime.Intrinsics.Vector256[int], shift_count: int) -> System.Runtime.Intrinsics.Vector256[int]:
        """
        Shifts (unsigned) each element of a vector right by the specified amount.
        
        :param vector: The vector whose elements are to be shifted.
        :param shift_count: The number of bits by which to shift each element.
        :returns: A vector whose elements where shifted right by .
        """
        ...

    @staticmethod
    @overload
    def shift_right_logical(vector: System.Runtime.Intrinsics.Vector256[System.IntPtr], shift_count: int) -> System.Runtime.Intrinsics.Vector256[System.IntPtr]:
        """
        Shifts (unsigned) each element of a vector right by the specified amount.
        
        :param vector: The vector whose elements are to be shifted.
        :param shift_count: The number of bits by which to shift each element.
        :returns: A vector whose elements where shifted right by .
        """
        ...

    @staticmethod
    @overload
    def shift_right_logical(vector: System.Runtime.Intrinsics.Vector256[System.UIntPtr], shift_count: int) -> System.Runtime.Intrinsics.Vector256[System.UIntPtr]:
        """
        Shifts (unsigned) each element of a vector right by the specified amount.
        
        :param vector: The vector whose elements are to be shifted.
        :param shift_count: The number of bits by which to shift each element.
        :returns: A vector whose elements where shifted right by .
        """
        ...

    @staticmethod
    @overload
    def shuffle(vector: System.Runtime.Intrinsics.Vector256[int], indices: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """
        Creates a new vector by selecting values from an input vector using a set of indices.
        
        :param vector: The input vector from which values are selected.
        :param indices: The per-element indices used to select a value from .
        :returns: A new vector containing the values from  selected by the given .
        """
        ...

    @staticmethod
    @overload
    def shuffle(vector: System.Runtime.Intrinsics.Vector256[float], indices: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[float]:
        """
        Creates a new vector by selecting values from an input vector using a set of indices.
        
        :param vector: The input vector from which values are selected.
        :param indices: The per-element indices used to select a value from .
        :returns: A new vector containing the values from  selected by the given .
        """
        ...

    @staticmethod
    @overload
    def shuffle_native(vector: System.Runtime.Intrinsics.Vector256[int], indices: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """
        Creates a new vector by selecting values from an input vector using a set of indices.
        Behavior is platform-dependent for out-of-range indices.
        
        :param vector: The input vector from which values are selected.
        :param indices: The per-element indices used to select a value from .
        :returns: A new vector containing the values from  selected by the given .
        """
        ...

    @staticmethod
    @overload
    def shuffle_native(vector: System.Runtime.Intrinsics.Vector256[float], indices: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[float]:
        """
        Creates a new vector by selecting values from an input vector using a set of indices.
        
        :param vector: The input vector from which values are selected.
        :param indices: The per-element indices used to select a value from .
        :returns: A new vector containing the values from  selected by the given .
        """
        ...

    @staticmethod
    def sin(vector: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    def sin_cos(vector: System.Runtime.Intrinsics.Vector256[float]) -> System.ValueTuple[System.Runtime.Intrinsics.Vector256[float], System.Runtime.Intrinsics.Vector256[float]]:
        ...

    def to_string(self) -> str:
        """
        Converts the current instance to an equivalent string representation.
        
        :returns: An equivalent string representation of the current instance.
        """
        ...

    @staticmethod
    def truncate(vector: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        ...

    @staticmethod
    @overload
    def widen(source: System.Runtime.Intrinsics.Vector256[int]) -> System.ValueTuple[System.Runtime.Intrinsics.Vector256[int], System.Runtime.Intrinsics.Vector256[int]]:
        """
        Widens a Vector256<Byte> into two Vector256{UInt16} .
        
        :param source: The vector whose elements are to be widened.
        :returns: A pair of vectors that contain the widened lower and upper halves of .
        """
        ...

    @staticmethod
    @overload
    def widen(source: System.Runtime.Intrinsics.Vector256[float]) -> System.ValueTuple[System.Runtime.Intrinsics.Vector256[float], System.Runtime.Intrinsics.Vector256[float]]:
        """
        Widens a Vector256<Single> into two Vector256{Double} .
        
        :param source: The vector whose elements are to be widened.
        :returns: A pair of vectors that contain the widened lower and upper halves of .
        """
        ...

    @staticmethod
    @overload
    def widen_lower(source: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """
        Widens the lower half of a Vector256<Byte> into a Vector256{UInt16} .
        
        :param source: The vector whose elements are to be widened.
        :returns: A vector that contain the widened lower half of .
        """
        ...

    @staticmethod
    @overload
    def widen_lower(source: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        """
        Widens the lower half of a Vector256<Single> into a Vector256{Double} .
        
        :param source: The vector whose elements are to be widened.
        :returns: A vector that contain the widened lower half of .
        """
        ...

    @staticmethod
    @overload
    def widen_upper(source: System.Runtime.Intrinsics.Vector256[int]) -> System.Runtime.Intrinsics.Vector256[int]:
        """
        Widens the upper half of a Vector256<Byte> into a Vector256{UInt16} .
        
        :param source: The vector whose elements are to be widened.
        :returns: A vector that contain the widened upper half of .
        """
        ...

    @staticmethod
    @overload
    def widen_upper(source: System.Runtime.Intrinsics.Vector256[float]) -> System.Runtime.Intrinsics.Vector256[float]:
        """
        Widens the upper half of a Vector256<Single> into a Vector256{Double} .
        
        :param source: The vector whose elements are to be widened.
        :returns: A vector that contain the widened upper half of .
        """
        ...


