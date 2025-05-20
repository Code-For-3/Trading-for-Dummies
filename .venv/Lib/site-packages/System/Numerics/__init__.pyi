from typing import overload
from enum import Enum
import abc
import typing

import System
import System.Collections.Generic
import System.Numerics
import System.Runtime.Intrinsics

System_Numerics_Matrix3x2 = typing.Any
System_Numerics_Matrix4x4 = typing.Any
System_Numerics_Vector = typing.Any
System_Numerics_Vector2 = typing.Any
System_Numerics_TotalOrderIeee754Comparer = typing.Any
System_Numerics_Plane = typing.Any
System_Numerics_Vector3 = typing.Any
System_Numerics_Quaternion = typing.Any
System_Numerics_Vector4 = typing.Any

System_Numerics_IMultiplyOperators_TSelf = typing.TypeVar("System_Numerics_IMultiplyOperators_TSelf")
System_Numerics_IMultiplyOperators_TOther = typing.TypeVar("System_Numerics_IMultiplyOperators_TOther")
System_Numerics_IMultiplyOperators_TResult = typing.TypeVar("System_Numerics_IMultiplyOperators_TResult")
System_Numerics_Vector_T = typing.TypeVar("System_Numerics_Vector_T")
System_Numerics_IUnaryNegationOperators_TSelf = typing.TypeVar("System_Numerics_IUnaryNegationOperators_TSelf")
System_Numerics_IUnaryNegationOperators_TResult = typing.TypeVar("System_Numerics_IUnaryNegationOperators_TResult")
System_Numerics_IRootFunctions_TSelf = typing.TypeVar("System_Numerics_IRootFunctions_TSelf")
System_Numerics_IBinaryFloatingPointIeee754_TSelf = typing.TypeVar("System_Numerics_IBinaryFloatingPointIeee754_TSelf")
System_Numerics_ISubtractionOperators_TSelf = typing.TypeVar("System_Numerics_ISubtractionOperators_TSelf")
System_Numerics_ISubtractionOperators_TOther = typing.TypeVar("System_Numerics_ISubtractionOperators_TOther")
System_Numerics_ISubtractionOperators_TResult = typing.TypeVar("System_Numerics_ISubtractionOperators_TResult")
System_Numerics_IFloatingPoint_TSelf = typing.TypeVar("System_Numerics_IFloatingPoint_TSelf")
System_Numerics_IUnaryPlusOperators_TSelf = typing.TypeVar("System_Numerics_IUnaryPlusOperators_TSelf")
System_Numerics_IUnaryPlusOperators_TResult = typing.TypeVar("System_Numerics_IUnaryPlusOperators_TResult")
System_Numerics_IDecrementOperators_TSelf = typing.TypeVar("System_Numerics_IDecrementOperators_TSelf")
System_Numerics_TotalOrderIeee754Comparer_T = typing.TypeVar("System_Numerics_TotalOrderIeee754Comparer_T")
System_Numerics_ITrigonometricFunctions_TSelf = typing.TypeVar("System_Numerics_ITrigonometricFunctions_TSelf")
System_Numerics_IMinMaxValue_TSelf = typing.TypeVar("System_Numerics_IMinMaxValue_TSelf")
System_Numerics_IEqualityOperators_TSelf = typing.TypeVar("System_Numerics_IEqualityOperators_TSelf")
System_Numerics_IEqualityOperators_TOther = typing.TypeVar("System_Numerics_IEqualityOperators_TOther")
System_Numerics_IEqualityOperators_TResult = typing.TypeVar("System_Numerics_IEqualityOperators_TResult")
System_Numerics_IDivisionOperators_TSelf = typing.TypeVar("System_Numerics_IDivisionOperators_TSelf")
System_Numerics_IDivisionOperators_TOther = typing.TypeVar("System_Numerics_IDivisionOperators_TOther")
System_Numerics_IDivisionOperators_TResult = typing.TypeVar("System_Numerics_IDivisionOperators_TResult")
System_Numerics_IIncrementOperators_TSelf = typing.TypeVar("System_Numerics_IIncrementOperators_TSelf")
System_Numerics_IModulusOperators_TSelf = typing.TypeVar("System_Numerics_IModulusOperators_TSelf")
System_Numerics_IModulusOperators_TOther = typing.TypeVar("System_Numerics_IModulusOperators_TOther")
System_Numerics_IModulusOperators_TResult = typing.TypeVar("System_Numerics_IModulusOperators_TResult")
System_Numerics_ISignedNumber_TSelf = typing.TypeVar("System_Numerics_ISignedNumber_TSelf")
System_Numerics_IAdditionOperators_TSelf = typing.TypeVar("System_Numerics_IAdditionOperators_TSelf")
System_Numerics_IAdditionOperators_TOther = typing.TypeVar("System_Numerics_IAdditionOperators_TOther")
System_Numerics_IAdditionOperators_TResult = typing.TypeVar("System_Numerics_IAdditionOperators_TResult")
System_Numerics_IBitwiseOperators_TSelf = typing.TypeVar("System_Numerics_IBitwiseOperators_TSelf")
System_Numerics_IBitwiseOperators_TOther = typing.TypeVar("System_Numerics_IBitwiseOperators_TOther")
System_Numerics_IBitwiseOperators_TResult = typing.TypeVar("System_Numerics_IBitwiseOperators_TResult")
System_Numerics_IBinaryInteger_TSelf = typing.TypeVar("System_Numerics_IBinaryInteger_TSelf")
System_Numerics_ILogarithmicFunctions_TSelf = typing.TypeVar("System_Numerics_ILogarithmicFunctions_TSelf")
System_Numerics_IUnsignedNumber_TSelf = typing.TypeVar("System_Numerics_IUnsignedNumber_TSelf")
System_Numerics_IBinaryNumber_TSelf = typing.TypeVar("System_Numerics_IBinaryNumber_TSelf")
System_Numerics_INumber_TSelf = typing.TypeVar("System_Numerics_INumber_TSelf")
System_Numerics_IMultiplicativeIdentity_TSelf = typing.TypeVar("System_Numerics_IMultiplicativeIdentity_TSelf")
System_Numerics_IMultiplicativeIdentity_TResult = typing.TypeVar("System_Numerics_IMultiplicativeIdentity_TResult")
System_Numerics_IShiftOperators_TSelf = typing.TypeVar("System_Numerics_IShiftOperators_TSelf")
System_Numerics_IShiftOperators_TOther = typing.TypeVar("System_Numerics_IShiftOperators_TOther")
System_Numerics_IShiftOperators_TResult = typing.TypeVar("System_Numerics_IShiftOperators_TResult")
System_Numerics_IPowerFunctions_TSelf = typing.TypeVar("System_Numerics_IPowerFunctions_TSelf")
System_Numerics_IHyperbolicFunctions_TSelf = typing.TypeVar("System_Numerics_IHyperbolicFunctions_TSelf")
System_Numerics_IFloatingPointIeee754_TSelf = typing.TypeVar("System_Numerics_IFloatingPointIeee754_TSelf")
System_Numerics_IComparisonOperators_TSelf = typing.TypeVar("System_Numerics_IComparisonOperators_TSelf")
System_Numerics_IComparisonOperators_TOther = typing.TypeVar("System_Numerics_IComparisonOperators_TOther")
System_Numerics_IComparisonOperators_TResult = typing.TypeVar("System_Numerics_IComparisonOperators_TResult")
System_Numerics_INumberBase_TSelf = typing.TypeVar("System_Numerics_INumberBase_TSelf")
System_Numerics_IFloatingPointConstants_TSelf = typing.TypeVar("System_Numerics_IFloatingPointConstants_TSelf")
System_Numerics_IExponentialFunctions_TSelf = typing.TypeVar("System_Numerics_IExponentialFunctions_TSelf")
System_Numerics_IAdditiveIdentity_TSelf = typing.TypeVar("System_Numerics_IAdditiveIdentity_TSelf")
System_Numerics_IAdditiveIdentity_TResult = typing.TypeVar("System_Numerics_IAdditiveIdentity_TResult")


class Quaternion(System.IEquatable[System_Numerics_Quaternion]):
    """Represents a vector that is used to encode three-dimensional physical rotations."""

    @property
    def x(self) -> float:
        """The X value of the vector component of the quaternion."""
        ...

    @x.setter
    def x(self, value: float) -> None:
        ...

    @property
    def y(self) -> float:
        """The Y value of the vector component of the quaternion."""
        ...

    @y.setter
    def y(self, value: float) -> None:
        ...

    @property
    def z(self) -> float:
        """The Z value of the vector component of the quaternion."""
        ...

    @z.setter
    def z(self, value: float) -> None:
        ...

    @property
    def w(self) -> float:
        """The rotation component of the quaternion."""
        ...

    @w.setter
    def w(self, value: float) -> None:
        ...

    ZERO: System.Numerics.Quaternion
    """Gets a quaternion that represents a zero."""

    IDENTITY: System.Numerics.Quaternion
    """Gets a quaternion that represents no rotation."""

    @property
    def is_identity(self) -> bool:
        """Gets a value that indicates whether the current instance is the identity quaternion."""
        ...

    def __add__(self, value_2: System.Numerics.Quaternion) -> System.Numerics.Quaternion:
        """
        Adds each element in one quaternion with its corresponding element in a second quaternion.
        
        :param value1: The first quaternion.
        :param value_2: The second quaternion.
        :returns: The quaternion that contains the summed values of  and .
        """
        ...

    def __eq__(self, value_2: System.Numerics.Quaternion) -> bool:
        """
        Returns a value that indicates whether two quaternions are equal.
        
        :param value1: The first quaternion to compare.
        :param value_2: The second quaternion to compare.
        :returns: true if the two quaternions are equal; otherwise, false.
        """
        ...

    def __getitem__(self, index: int) -> float:
        """
        Gets or sets the element at the specified index.
        
        :param index: The index of the element to get or set.
        :returns: The element at .
        """
        ...

    def __iadd__(self, value_2: System.Numerics.Quaternion) -> System.Numerics.Quaternion:
        """
        Adds each element in one quaternion with its corresponding element in a second quaternion.
        
        :param value1: The first quaternion.
        :param value_2: The second quaternion.
        :returns: The quaternion that contains the summed values of  and .
        """
        ...

    @overload
    def __imul__(self, value_2: System.Numerics.Quaternion) -> System.Numerics.Quaternion:
        """
        Returns the quaternion that results from multiplying two quaternions together.
        
        :param value1: The first quaternion.
        :param value_2: The second quaternion.
        :returns: The product quaternion.
        """
        ...

    @overload
    def __imul__(self, value_2: float) -> System.Numerics.Quaternion:
        """
        Returns the quaternion that results from scaling all the components of a specified quaternion by a scalar factor.
        
        :param value1: The source quaternion.
        :param value_2: The scalar value.
        :returns: The scaled quaternion.
        """
        ...

    @overload
    def __init__(self, x: float, y: float, z: float, w: float) -> None:
        """
        Constructs a quaternion from the specified components.
        
        :param x: The value to assign to the X component of the quaternion.
        :param y: The value to assign to the Y component of the quaternion.
        :param z: The value to assign to the Z component of the quaternion.
        :param w: The value to assign to the W component of the quaternion.
        """
        ...

    @overload
    def __init__(self, vector_part: System.Numerics.Vector3, scalar_part: float) -> None:
        """
        Creates a quaternion from the specified vector and rotation parts.
        
        :param vector_part: The vector part of the quaternion.
        :param scalar_part: The rotation part of the quaternion.
        """
        ...

    @overload
    def __isub__(self, value_2: System.Numerics.Quaternion) -> System.Numerics.Quaternion:
        """
        Subtracts each element in a second quaternion from its corresponding element in a first quaternion.
        
        :param value1: The first quaternion.
        :param value_2: The second quaternion.
        :returns: The quaternion containing the values that result from subtracting each element in  from its corresponding element in .
        """
        ...

    @overload
    def __isub__(self) -> System.Numerics.Quaternion:
        """
        Reverses the sign of each component of the quaternion.
        
        :param value: The quaternion to negate.
        :returns: The negated quaternion.
        """
        ...

    def __itruediv__(self, value_2: System.Numerics.Quaternion) -> System.Numerics.Quaternion:
        """
        Divides one quaternion by a second quaternion.
        
        :param value1: The dividend.
        :param value_2: The divisor.
        :returns: The quaternion that results from dividing  by .
        """
        ...

    @overload
    def __mul__(self, value_2: System.Numerics.Quaternion) -> System.Numerics.Quaternion:
        """
        Returns the quaternion that results from multiplying two quaternions together.
        
        :param value1: The first quaternion.
        :param value_2: The second quaternion.
        :returns: The product quaternion.
        """
        ...

    @overload
    def __mul__(self, value_2: float) -> System.Numerics.Quaternion:
        """
        Returns the quaternion that results from scaling all the components of a specified quaternion by a scalar factor.
        
        :param value1: The source quaternion.
        :param value_2: The scalar value.
        :returns: The scaled quaternion.
        """
        ...

    def __ne__(self, value_2: System.Numerics.Quaternion) -> bool:
        """
        Returns a value that indicates whether two quaternions are not equal.
        
        :param value1: The first quaternion to compare.
        :param value_2: The second quaternion to compare.
        :returns: true if  and  are not equal; otherwise, false.
        """
        ...

    def __setitem__(self, index: int, value: float) -> None:
        """
        Gets or sets the element at the specified index.
        
        :param index: The index of the element to get or set.
        :returns: The element at .
        """
        ...

    @overload
    def __sub__(self, value_2: System.Numerics.Quaternion) -> System.Numerics.Quaternion:
        """
        Subtracts each element in a second quaternion from its corresponding element in a first quaternion.
        
        :param value1: The first quaternion.
        :param value_2: The second quaternion.
        :returns: The quaternion containing the values that result from subtracting each element in  from its corresponding element in .
        """
        ...

    @overload
    def __sub__(self) -> System.Numerics.Quaternion:
        """
        Reverses the sign of each component of the quaternion.
        
        :param value: The quaternion to negate.
        :returns: The negated quaternion.
        """
        ...

    def __truediv__(self, value_2: System.Numerics.Quaternion) -> System.Numerics.Quaternion:
        """
        Divides one quaternion by a second quaternion.
        
        :param value1: The dividend.
        :param value_2: The divisor.
        :returns: The quaternion that results from dividing  by .
        """
        ...

    @staticmethod
    def add(value_1: System.Numerics.Quaternion, value_2: System.Numerics.Quaternion) -> System.Numerics.Quaternion:
        """
        Adds each element in one quaternion with its corresponding element in a second quaternion.
        
        :param value_1: The first quaternion.
        :param value_2: The second quaternion.
        :returns: The quaternion that contains the summed values of  and .
        """
        ...

    @staticmethod
    def concatenate(value_1: System.Numerics.Quaternion, value_2: System.Numerics.Quaternion) -> System.Numerics.Quaternion:
        """
        Concatenates two quaternions.
        
        :param value_1: The first quaternion rotation in the series.
        :param value_2: The second quaternion rotation in the series.
        :returns: A new quaternion representing the concatenation of the  rotation followed by the  rotation.
        """
        ...

    @staticmethod
    def conjugate(value: System.Numerics.Quaternion) -> System.Numerics.Quaternion:
        """
        Returns the conjugate of a specified quaternion.
        
        :param value: The quaternion.
        :returns: A new quaternion that is the conjugate of value.
        """
        ...

    @staticmethod
    def create_from_axis_angle(axis: System.Numerics.Vector3, angle: float) -> System.Numerics.Quaternion:
        """
        Creates a quaternion from a unit vector and an angle to rotate around the vector.
        
        :param axis: The unit vector to rotate around.
        :param angle: The angle, in radians, to rotate around the vector.
        :returns: The newly created quaternion.
        """
        ...

    @staticmethod
    def create_from_rotation_matrix(matrix: System.Numerics.Matrix4x4) -> System.Numerics.Quaternion:
        """
        Creates a quaternion from the specified rotation matrix.
        
        :param matrix: The rotation matrix.
        :returns: The newly created quaternion.
        """
        ...

    @staticmethod
    def create_from_yaw_pitch_roll(yaw: float, pitch: float, roll: float) -> System.Numerics.Quaternion:
        """
        Creates a new quaternion from the given yaw, pitch, and roll.
        
        :param yaw: The yaw angle, in radians, around the Y axis.
        :param pitch: The pitch angle, in radians, around the X axis.
        :param roll: The roll angle, in radians, around the Z axis.
        :returns: The resulting quaternion.
        """
        ...

    @staticmethod
    def divide(value_1: System.Numerics.Quaternion, value_2: System.Numerics.Quaternion) -> System.Numerics.Quaternion:
        """
        Divides one quaternion by a second quaternion.
        
        :param value_1: The dividend.
        :param value_2: The divisor.
        :returns: The quaternion that results from dividing  by .
        """
        ...

    @staticmethod
    def dot(quaternion_1: System.Numerics.Quaternion, quaternion_2: System.Numerics.Quaternion) -> float:
        """
        Calculates the dot product of two quaternions.
        
        :param quaternion_1: The first quaternion.
        :param quaternion_2: The second quaternion.
        :returns: The dot product.
        """
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        """
        Returns a value that indicates whether this instance and a specified object are equal.
        
        :param obj: The object to compare with the current instance.
        :returns: true if the current instance and  are equal; otherwise, false. If  is null, the method returns false.
        """
        ...

    @overload
    def equals(self, other: System.Numerics.Quaternion) -> bool:
        """
        Returns a value that indicates whether this instance and another quaternion are equal.
        
        :param other: The other quaternion.
        :returns: true if the two quaternions are equal; otherwise, false.
        """
        ...

    def get_hash_code(self) -> int:
        """
        Returns the hash code for this instance.
        
        :returns: The hash code.
        """
        ...

    @staticmethod
    def inverse(value: System.Numerics.Quaternion) -> System.Numerics.Quaternion:
        """
        Returns the inverse of a quaternion.
        
        :param value: The quaternion.
        :returns: The inverted quaternion.
        """
        ...

    def length(self) -> float:
        """
        Calculates the length of the quaternion.
        
        :returns: The computed length of the quaternion.
        """
        ...

    def length_squared(self) -> float:
        """
        Calculates the squared length of the quaternion.
        
        :returns: The length squared of the quaternion.
        """
        ...

    @staticmethod
    def lerp(quaternion_1: System.Numerics.Quaternion, quaternion_2: System.Numerics.Quaternion, amount: float) -> System.Numerics.Quaternion:
        """
        Performs a linear interpolation between two quaternions based on a value that specifies the weighting of the second quaternion.
        
        :param quaternion_1: The first quaternion.
        :param quaternion_2: The second quaternion.
        :param amount: The relative weight of  in the interpolation.
        :returns: The interpolated quaternion.
        """
        ...

    @staticmethod
    @overload
    def multiply(value_1: System.Numerics.Quaternion, value_2: System.Numerics.Quaternion) -> System.Numerics.Quaternion:
        """
        Returns the quaternion that results from multiplying two quaternions together.
        
        :param value_1: The first quaternion.
        :param value_2: The second quaternion.
        :returns: The product quaternion.
        """
        ...

    @staticmethod
    @overload
    def multiply(value_1: System.Numerics.Quaternion, value_2: float) -> System.Numerics.Quaternion:
        """
        Returns the quaternion that results from scaling all the components of a specified quaternion by a scalar factor.
        
        :param value_1: The source quaternion.
        :param value_2: The scalar value.
        :returns: The scaled quaternion.
        """
        ...

    @staticmethod
    def negate(value: System.Numerics.Quaternion) -> System.Numerics.Quaternion:
        """
        Reverses the sign of each component of the quaternion.
        
        :param value: The quaternion to negate.
        :returns: The negated quaternion.
        """
        ...

    @staticmethod
    def normalize(value: System.Numerics.Quaternion) -> System.Numerics.Quaternion:
        """
        Divides each component of a specified Quaternion by its length.
        
        :param value: The quaternion to normalize.
        :returns: The normalized quaternion.
        """
        ...

    @staticmethod
    def slerp(quaternion_1: System.Numerics.Quaternion, quaternion_2: System.Numerics.Quaternion, amount: float) -> System.Numerics.Quaternion:
        """
        Interpolates between two quaternions, using spherical linear interpolation.
        
        :param quaternion_1: The first quaternion.
        :param quaternion_2: The second quaternion.
        :param amount: The relative weight of the second quaternion in the interpolation.
        :returns: The interpolated quaternion.
        """
        ...

    @staticmethod
    def subtract(value_1: System.Numerics.Quaternion, value_2: System.Numerics.Quaternion) -> System.Numerics.Quaternion:
        """
        Subtracts each element in a second quaternion from its corresponding element in a first quaternion.
        
        :param value_1: The first quaternion.
        :param value_2: The second quaternion.
        :returns: The quaternion containing the values that result from subtracting each element in  from its corresponding element in .
        """
        ...

    def to_string(self) -> str:
        """
        Returns a string that represents this quaternion.
        
        :returns: The string representation of this quaternion.
        """
        ...


class Vector2(System.IEquatable[System_Numerics_Vector2], System.IFormattable):
    """Represents a vector with two single-precision floating-point values."""

    @property
    def x(self) -> float:
        """The X component of the vector."""
        ...

    @x.setter
    def x(self, value: float) -> None:
        ...

    @property
    def y(self) -> float:
        """The Y component of the vector."""
        ...

    @y.setter
    def y(self, value: float) -> None:
        ...

    ALL_BITS_SET: System.Numerics.Vector2

    E: System.Numerics.Vector2

    EPSILON: System.Numerics.Vector2

    NA_N: System.Numerics.Vector2

    NEGATIVE_INFINITY: System.Numerics.Vector2

    NEGATIVE_ZERO: System.Numerics.Vector2

    ONE: System.Numerics.Vector2

    PI: System.Numerics.Vector2

    POSITIVE_INFINITY: System.Numerics.Vector2

    TAU: System.Numerics.Vector2

    UNIT_X: System.Numerics.Vector2
    """Gets the vector (1,0)."""

    UNIT_Y: System.Numerics.Vector2
    """Gets the vector (0,1)."""

    ZERO: System.Numerics.Vector2

    @overload
    def __add__(self, right: System.Numerics.Vector2) -> System.Numerics.Vector2:
        """
        Adds two vectors together.
        
        :param left: The first vector to add.
        :param right: The second vector to add.
        :returns: The summed vector.
        """
        ...

    @overload
    def __add__(self) -> System.Numerics.Vector2:
        ...

    def __and__(self, right: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    def __eq__(self, right: System.Numerics.Vector2) -> bool:
        """
        Returns a value that indicates whether each pair of elements in two specified vectors is equal.
        
        :param left: The first vector to compare.
        :param right: The second vector to compare.
        :returns: true if  and  are equal; otherwise, false.
        """
        ...

    def __getitem__(self, index: int) -> float:
        """
        Gets or sets the element at the specified index.
        
        :param index: The index of the element to get or set.
        :returns: The the element at .
        """
        ...

    @overload
    def __iadd__(self, right: System.Numerics.Vector2) -> System.Numerics.Vector2:
        """
        Adds two vectors together.
        
        :param left: The first vector to add.
        :param right: The second vector to add.
        :returns: The summed vector.
        """
        ...

    @overload
    def __iadd__(self) -> System.Numerics.Vector2:
        ...

    def __iand__(self, right: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    def __ilshift__(self, shift_amount: int) -> System.Numerics.Vector2:
        ...

    @overload
    def __imul__(self, right: System.Numerics.Vector2) -> System.Numerics.Vector2:
        """
        Returns a new vector whose values are the product of each pair of elements in two specified vectors.
        
        :param left: The first vector.
        :param right: The second vector.
        :returns: The element-wise product vector.
        """
        ...

    @overload
    def __imul__(self, right: float) -> System.Numerics.Vector2:
        """
        Multiplies the specified vector by the specified scalar value.
        
        :param left: The vector.
        :param right: The scalar value.
        :returns: The scaled vector.
        """
        ...

    @overload
    def __imul__(self, right: System.Numerics.Vector2) -> System.Numerics.Vector2:
        """
        Multiplies the scalar value by the specified vector.
        
        :param left: The vector.
        :param right: The scalar value.
        :returns: The scaled vector.
        """
        ...

    @overload
    def __init__(self, value: float) -> None:
        """
        Creates a new Vector2 object whose two elements have the same value.
        
        :param value: The value to assign to both elements.
        """
        ...

    @overload
    def __init__(self, x: float, y: float) -> None:
        """
        Creates a vector whose elements have the specified values.
        
        :param x: The value to assign to the X field.
        :param y: The value to assign to the Y field.
        """
        ...

    @overload
    def __init__(self, values: System.ReadOnlySpan[float]) -> None:
        """
        Constructs a vector from the given ReadOnlySpan{Single}. The span must contain at least 2 elements.
        
        :param values: The span of elements to assign to the vector.
        """
        ...

    def __invert__(self) -> System.Numerics.Vector2:
        ...

    def __ior__(self, right: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    def __irshift__(self, shift_amount: int) -> System.Numerics.Vector2:
        ...

    @overload
    def __isub__(self, right: System.Numerics.Vector2) -> System.Numerics.Vector2:
        """
        Subtracts the second vector from the first.
        
        :param left: The first vector.
        :param right: The second vector.
        :returns: The vector that results from subtracting  from .
        """
        ...

    @overload
    def __isub__(self) -> System.Numerics.Vector2:
        """
        Negates the specified vector.
        
        :param value: The vector to negate.
        :returns: The negated vector.
        """
        ...

    @overload
    def __itruediv__(self, right: System.Numerics.Vector2) -> System.Numerics.Vector2:
        """
        Divides the first vector by the second.
        
        :param left: The first vector.
        :param right: The second vector.
        :returns: The vector that results from dividing  by .
        """
        ...

    @overload
    def __itruediv__(self, value_2: float) -> System.Numerics.Vector2:
        """
        Divides the specified vector by a specified scalar value.
        
        :param value1: The vector.
        :param value_2: The scalar value.
        :returns: The result of the division.
        """
        ...

    def __ixor__(self, right: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    def __lshift__(self, shift_amount: int) -> System.Numerics.Vector2:
        ...

    @overload
    def __mul__(self, right: System.Numerics.Vector2) -> System.Numerics.Vector2:
        """
        Returns a new vector whose values are the product of each pair of elements in two specified vectors.
        
        :param left: The first vector.
        :param right: The second vector.
        :returns: The element-wise product vector.
        """
        ...

    @overload
    def __mul__(self, right: float) -> System.Numerics.Vector2:
        """
        Multiplies the specified vector by the specified scalar value.
        
        :param left: The vector.
        :param right: The scalar value.
        :returns: The scaled vector.
        """
        ...

    @overload
    def __mul__(self, right: System.Numerics.Vector2) -> System.Numerics.Vector2:
        """
        Multiplies the scalar value by the specified vector.
        
        :param left: The vector.
        :param right: The scalar value.
        :returns: The scaled vector.
        """
        ...

    def __ne__(self, right: System.Numerics.Vector2) -> bool:
        """
        Returns a value that indicates whether two specified vectors are not equal.
        
        :param left: The first vector to compare.
        :param right: The second vector to compare.
        :returns: true if  and  are not equal; otherwise, false.
        """
        ...

    def __or__(self, right: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    def __rshift__(self, shift_amount: int) -> System.Numerics.Vector2:
        ...

    def __setitem__(self, index: int, value: float) -> None:
        """
        Gets or sets the element at the specified index.
        
        :param index: The index of the element to get or set.
        :returns: The the element at .
        """
        ...

    @overload
    def __sub__(self, right: System.Numerics.Vector2) -> System.Numerics.Vector2:
        """
        Subtracts the second vector from the first.
        
        :param left: The first vector.
        :param right: The second vector.
        :returns: The vector that results from subtracting  from .
        """
        ...

    @overload
    def __sub__(self) -> System.Numerics.Vector2:
        """
        Negates the specified vector.
        
        :param value: The vector to negate.
        :returns: The negated vector.
        """
        ...

    @overload
    def __truediv__(self, right: System.Numerics.Vector2) -> System.Numerics.Vector2:
        """
        Divides the first vector by the second.
        
        :param left: The first vector.
        :param right: The second vector.
        :returns: The vector that results from dividing  by .
        """
        ...

    @overload
    def __truediv__(self, value_2: float) -> System.Numerics.Vector2:
        """
        Divides the specified vector by a specified scalar value.
        
        :param value1: The vector.
        :param value_2: The scalar value.
        :returns: The result of the division.
        """
        ...

    def __xor__(self, right: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def abs(value: System.Numerics.Vector2) -> System.Numerics.Vector2:
        """
        Returns a vector whose elements are the absolute values of each of the specified vector's elements.
        
        :param value: A vector.
        :returns: The absolute value vector.
        """
        ...

    @staticmethod
    def add(left: System.Numerics.Vector2, right: System.Numerics.Vector2) -> System.Numerics.Vector2:
        """
        Adds two vectors together.
        
        :param left: The first vector to add.
        :param right: The second vector to add.
        :returns: The summed vector.
        """
        ...

    @staticmethod
    def all(vector: System.Numerics.Vector2, value: float) -> bool:
        ...

    @staticmethod
    def all_where_all_bits_set(vector: System.Numerics.Vector2) -> bool:
        ...

    @staticmethod
    def and_not(left: System.Numerics.Vector2, right: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def any(vector: System.Numerics.Vector2, value: float) -> bool:
        ...

    @staticmethod
    def any_where_all_bits_set(vector: System.Numerics.Vector2) -> bool:
        ...

    @staticmethod
    def bitwise_and(left: System.Numerics.Vector2, right: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def bitwise_or(left: System.Numerics.Vector2, right: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def clamp(value_1: System.Numerics.Vector2, min: System.Numerics.Vector2, max: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def clamp_native(value_1: System.Numerics.Vector2, min: System.Numerics.Vector2, max: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def conditional_select(condition: System.Numerics.Vector2, left: System.Numerics.Vector2, right: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def copy_sign(value: System.Numerics.Vector2, sign: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @overload
    def copy_to(self, array: typing.List[float]) -> None:
        """
        Copies the elements of the vector to a specified array.
        
        :param array: The destination array.
        """
        ...

    @overload
    def copy_to(self, array: typing.List[float], index: int) -> None:
        """
        Copies the elements of the vector to a specified array starting at a specified index position.
        
        :param array: The destination array.
        :param index: The index at which to copy the first element of the vector.
        """
        ...

    @overload
    def copy_to(self, destination: System.Span[float]) -> None:
        """
        Copies the vector to the given Span{T}.The length of the destination span must be at least 2.
        
        :param destination: The destination span which the values are copied into.
        """
        ...

    @staticmethod
    def cos(vector: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def count(vector: System.Numerics.Vector2, value: float) -> int:
        ...

    @staticmethod
    def count_where_all_bits_set(vector: System.Numerics.Vector2) -> int:
        ...

    @staticmethod
    @overload
    def create(value: float) -> System.Numerics.Vector2:
        """
        Creates a new Vector2 object whose two elements have the same value.
        
        :param value: The value to assign to all two elements.
        :returns: A new Vector2 whose two elements have the same value.
        """
        ...

    @staticmethod
    @overload
    def create(x: float, y: float) -> System.Numerics.Vector2:
        """
        Creates a vector whose elements have the specified values.
        
        :param x: The value to assign to the X field.
        :param y: The value to assign to the Y field.
        :returns: A new Vector2 whose elements have the specified values.
        """
        ...

    @staticmethod
    @overload
    def create(values: System.ReadOnlySpan[float]) -> System.Numerics.Vector2:
        """
        Constructs a vector from the given ReadOnlySpan{Single}. The span must contain at least 2 elements.
        
        :param values: The span of elements to assign to the vector.
        :returns: A new Vector2 whose elements have the specified values.
        """
        ...

    @staticmethod
    def cross(value_1: System.Numerics.Vector2, value_2: System.Numerics.Vector2) -> float:
        """
        Returns the z-value of the cross product of two vectors.
        Since the Vector2 is in the x-y plane, a 3D cross product only produces the z-value.
        
        :param value_1: The first vector.
        :param value_2: The second vector.
        :returns: The value of the z-coordinate from the cross product.
        """
        ...

    @staticmethod
    def degrees_to_radians(degrees: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def distance(value_1: System.Numerics.Vector2, value_2: System.Numerics.Vector2) -> float:
        """
        Computes the Euclidean distance between the two given points.
        
        :param value_1: The first point.
        :param value_2: The second point.
        :returns: The distance.
        """
        ...

    @staticmethod
    def distance_squared(value_1: System.Numerics.Vector2, value_2: System.Numerics.Vector2) -> float:
        """
        Returns the Euclidean distance squared between two specified points.
        
        :param value_1: The first point.
        :param value_2: The second point.
        :returns: The distance squared.
        """
        ...

    @staticmethod
    @overload
    def divide(left: System.Numerics.Vector2, right: System.Numerics.Vector2) -> System.Numerics.Vector2:
        """
        Divides the first vector by the second.
        
        :param left: The first vector.
        :param right: The second vector.
        :returns: The vector resulting from the division.
        """
        ...

    @staticmethod
    @overload
    def divide(left: System.Numerics.Vector2, divisor: float) -> System.Numerics.Vector2:
        """
        Divides the specified vector by a specified scalar value.
        
        :param left: The vector.
        :param divisor: The scalar value.
        :returns: The vector that results from the division.
        """
        ...

    @staticmethod
    def dot(value_1: System.Numerics.Vector2, value_2: System.Numerics.Vector2) -> float:
        """
        Returns the dot product of two vectors.
        
        :param value_1: The first vector.
        :param value_2: The second vector.
        :returns: The dot product.
        """
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        """
        Returns a value that indicates whether this instance and a specified object are equal.
        
        :param obj: The object to compare with the current instance.
        :returns: true if the current instance and  are equal; otherwise, false. If  is null, the method returns false.
        """
        ...

    @staticmethod
    @overload
    def equals(left: System.Numerics.Vector2, right: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @overload
    def equals(self, other: System.Numerics.Vector2) -> bool:
        """
        Returns a value that indicates whether this instance and another vector are equal.
        
        :param other: The other vector.
        :returns: true if the two vectors are equal; otherwise, false.
        """
        ...

    @staticmethod
    def equals_all(left: System.Numerics.Vector2, right: System.Numerics.Vector2) -> bool:
        ...

    @staticmethod
    def equals_any(left: System.Numerics.Vector2, right: System.Numerics.Vector2) -> bool:
        ...

    @staticmethod
    def exp(vector: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def fused_multiply_add(left: System.Numerics.Vector2, right: System.Numerics.Vector2, addend: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    def get_hash_code(self) -> int:
        """
        Returns the hash code for this instance.
        
        :returns: The hash code.
        """
        ...

    @staticmethod
    def greater_than(left: System.Numerics.Vector2, right: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def greater_than_all(left: System.Numerics.Vector2, right: System.Numerics.Vector2) -> bool:
        ...

    @staticmethod
    def greater_than_any(left: System.Numerics.Vector2, right: System.Numerics.Vector2) -> bool:
        ...

    @staticmethod
    def greater_than_or_equal(left: System.Numerics.Vector2, right: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def greater_than_or_equal_all(left: System.Numerics.Vector2, right: System.Numerics.Vector2) -> bool:
        ...

    @staticmethod
    def greater_than_or_equal_any(left: System.Numerics.Vector2, right: System.Numerics.Vector2) -> bool:
        ...

    @staticmethod
    def hypot(x: System.Numerics.Vector2, y: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def index_of(vector: System.Numerics.Vector2, value: float) -> int:
        ...

    @staticmethod
    def index_of_where_all_bits_set(vector: System.Numerics.Vector2) -> int:
        ...

    @staticmethod
    def is_even_integer(vector: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def is_finite(vector: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def is_infinity(vector: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def is_integer(vector: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def is_na_n(vector: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def is_negative(vector: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def is_negative_infinity(vector: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def is_normal(vector: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def is_odd_integer(vector: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def is_positive(vector: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def is_positive_infinity(vector: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def is_subnormal(vector: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def is_zero(vector: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def last_index_of(vector: System.Numerics.Vector2, value: float) -> int:
        ...

    @staticmethod
    def last_index_of_where_all_bits_set(vector: System.Numerics.Vector2) -> int:
        ...

    def length(self) -> float:
        """
        Returns the length of the vector.
        
        :returns: The vector's length.
        """
        ...

    def length_squared(self) -> float:
        """
        Returns the length of the vector squared.
        
        :returns: The vector's length squared.
        """
        ...

    @staticmethod
    @overload
    def lerp(value_1: System.Numerics.Vector2, value_2: System.Numerics.Vector2, amount: float) -> System.Numerics.Vector2:
        ...

    @staticmethod
    @overload
    def lerp(value_1: System.Numerics.Vector2, value_2: System.Numerics.Vector2, amount: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def less_than(left: System.Numerics.Vector2, right: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def less_than_all(left: System.Numerics.Vector2, right: System.Numerics.Vector2) -> bool:
        ...

    @staticmethod
    def less_than_any(left: System.Numerics.Vector2, right: System.Numerics.Vector2) -> bool:
        ...

    @staticmethod
    def less_than_or_equal(left: System.Numerics.Vector2, right: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def less_than_or_equal_all(left: System.Numerics.Vector2, right: System.Numerics.Vector2) -> bool:
        ...

    @staticmethod
    def less_than_or_equal_any(left: System.Numerics.Vector2, right: System.Numerics.Vector2) -> bool:
        ...

    @staticmethod
    def load(source: typing.Any) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def load_aligned(source: typing.Any) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def load_aligned_non_temporal(source: typing.Any) -> System.Numerics.Vector2:
        ...

    @staticmethod
    @overload
    def load_unsafe(source: float) -> System.Numerics.Vector2:
        ...

    @staticmethod
    @overload
    def load_unsafe(source: float, element_offset: System.UIntPtr) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def log(vector: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def log_2(vector: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def max(value_1: System.Numerics.Vector2, value_2: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def max_magnitude(value_1: System.Numerics.Vector2, value_2: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def max_magnitude_number(value_1: System.Numerics.Vector2, value_2: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def max_native(value_1: System.Numerics.Vector2, value_2: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def max_number(value_1: System.Numerics.Vector2, value_2: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def min(value_1: System.Numerics.Vector2, value_2: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def min_magnitude(value_1: System.Numerics.Vector2, value_2: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def min_magnitude_number(value_1: System.Numerics.Vector2, value_2: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def min_native(value_1: System.Numerics.Vector2, value_2: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def min_number(value_1: System.Numerics.Vector2, value_2: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    @overload
    def multiply(left: System.Numerics.Vector2, right: System.Numerics.Vector2) -> System.Numerics.Vector2:
        """
        Returns a new vector whose values are the product of each pair of elements in two specified vectors.
        
        :param left: The first vector.
        :param right: The second vector.
        :returns: The element-wise product vector.
        """
        ...

    @staticmethod
    @overload
    def multiply(left: System.Numerics.Vector2, right: float) -> System.Numerics.Vector2:
        """
        Multiplies a vector by a specified scalar.
        
        :param left: The vector to multiply.
        :param right: The scalar value.
        :returns: The scaled vector.
        """
        ...

    @staticmethod
    @overload
    def multiply(left: float, right: System.Numerics.Vector2) -> System.Numerics.Vector2:
        """
        Multiplies a scalar value by a specified vector.
        
        :param left: The scaled value.
        :param right: The vector.
        :returns: The scaled vector.
        """
        ...

    @staticmethod
    def multiply_add_estimate(left: System.Numerics.Vector2, right: System.Numerics.Vector2, addend: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def negate(value: System.Numerics.Vector2) -> System.Numerics.Vector2:
        """
        Negates a specified vector.
        
        :param value: The vector to negate.
        :returns: The negated vector.
        """
        ...

    @staticmethod
    def none(vector: System.Numerics.Vector2, value: float) -> bool:
        ...

    @staticmethod
    def none_where_all_bits_set(vector: System.Numerics.Vector2) -> bool:
        ...

    @staticmethod
    def normalize(value: System.Numerics.Vector2) -> System.Numerics.Vector2:
        """
        Returns a vector with the same direction as the specified vector, but with a length of one.
        
        :param value: The vector to normalize.
        :returns: The normalized vector.
        """
        ...

    @staticmethod
    def ones_complement(value: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def radians_to_degrees(radians: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def reflect(vector: System.Numerics.Vector2, normal: System.Numerics.Vector2) -> System.Numerics.Vector2:
        """
        Returns the reflection of a vector off a surface that has the specified normal.
        
        :param vector: The source vector.
        :param normal: The normal of the surface being reflected off.
        :returns: The reflected vector.
        """
        ...

    @staticmethod
    @overload
    def round(vector: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    @overload
    def round(vector: System.Numerics.Vector2, mode: System.MidpointRounding) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def shuffle(vector: System.Numerics.Vector2, x_index: int, y_index: int) -> System.Numerics.Vector2:
        """
        Creates a new vector by selecting values from an input vector using a set of indices.
        
        :param vector: The input vector from which values are selected.
        :param x_index: The index used to select a value from  to be used as the value of X in the result.
        :param y_index: The index used to select a value from  to be used as the value of Y in the result
        :returns: A new vector containing the values from  selected by the given indices.
        """
        ...

    @staticmethod
    def sin(vector: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    @staticmethod
    def sin_cos(vector: System.Numerics.Vector2) -> System.ValueTuple[System.Numerics.Vector2, System.Numerics.Vector2]:
        ...

    @staticmethod
    def square_root(value: System.Numerics.Vector2) -> System.Numerics.Vector2:
        """
        Returns a vector whose elements are the square root of each of a specified vector's elements.
        
        :param value: A vector.
        :returns: The square root vector.
        """
        ...

    @staticmethod
    def subtract(left: System.Numerics.Vector2, right: System.Numerics.Vector2) -> System.Numerics.Vector2:
        """
        Subtracts the second vector from the first.
        
        :param left: The first vector.
        :param right: The second vector.
        :returns: The difference vector.
        """
        ...

    @staticmethod
    def sum(value: System.Numerics.Vector2) -> float:
        ...

    @overload
    def to_string(self) -> str:
        """
        Returns the string representation of the current instance using default formatting.
        
        :returns: The string representation of the current instance.
        """
        ...

    @overload
    def to_string(self, format: str) -> str:
        """
        Returns the string representation of the current instance using the specified format string to format individual elements.
        
        :param format: A standard or custom numeric format string that defines the format of individual elements.
        :returns: The string representation of the current instance.
        """
        ...

    @overload
    def to_string(self, format: str, format_provider: System.IFormatProvider) -> str:
        """
        Returns the string representation of the current instance using the specified format string to format individual elements and the specified format provider to define culture-specific formatting.
        
        :param format: A standard or custom numeric format string that defines the format of individual elements.
        :param format_provider: A format provider that supplies culture-specific formatting information.
        :returns: The string representation of the current instance.
        """
        ...

    @staticmethod
    @overload
    def transform(position: System.Numerics.Vector2, matrix: System.Numerics.Matrix3x2) -> System.Numerics.Vector2:
        """
        Transforms a vector by a specified 3x2 matrix.
        
        :param position: The vector to transform.
        :param matrix: The transformation matrix.
        :returns: The transformed vector.
        """
        ...

    @staticmethod
    @overload
    def transform(position: System.Numerics.Vector2, matrix: System.Numerics.Matrix4x4) -> System.Numerics.Vector2:
        """
        Transforms a vector by a specified 4x4 matrix.
        
        :param position: The vector to transform.
        :param matrix: The transformation matrix.
        :returns: The transformed vector.
        """
        ...

    @staticmethod
    @overload
    def transform(value: System.Numerics.Vector2, rotation: System.Numerics.Quaternion) -> System.Numerics.Vector2:
        """
        Transforms a vector by the specified Quaternion rotation value.
        
        :param value: The vector to rotate.
        :param rotation: The rotation to apply.
        :returns: The transformed vector.
        """
        ...

    @staticmethod
    @overload
    def transform_normal(normal: System.Numerics.Vector2, matrix: System.Numerics.Matrix3x2) -> System.Numerics.Vector2:
        """
        Transforms a vector normal by the given 3x2 matrix.
        
        :param normal: The source vector.
        :param matrix: The matrix.
        :returns: The transformed vector.
        """
        ...

    @staticmethod
    @overload
    def transform_normal(normal: System.Numerics.Vector2, matrix: System.Numerics.Matrix4x4) -> System.Numerics.Vector2:
        """
        Transforms a vector normal by the given 4x4 matrix.
        
        :param normal: The source vector.
        :param matrix: The matrix.
        :returns: The transformed vector.
        """
        ...

    @staticmethod
    def truncate(vector: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...

    def try_copy_to(self, destination: System.Span[float]) -> bool:
        """
        Attempts to copy the vector to the given Span{Single}. The length of the destination span must be at least 2.
        
        :param destination: The destination span which the values are copied into.
        :returns: true if the source vector was successfully copied to . false if  is not large enough to hold the source vector.
        """
        ...

    @staticmethod
    def xor(left: System.Numerics.Vector2, right: System.Numerics.Vector2) -> System.Numerics.Vector2:
        ...


class Matrix3x2(System.IEquatable[System_Numerics_Matrix3x2]):
    """Represents a 3x2 matrix."""

    @property
    def m_11(self) -> float:
        """The first element of the first row."""
        ...

    @m_11.setter
    def m_11(self, value: float) -> None:
        ...

    @property
    def m_12(self) -> float:
        """The second element of the first row."""
        ...

    @m_12.setter
    def m_12(self, value: float) -> None:
        ...

    @property
    def m_21(self) -> float:
        """The first element of the second row."""
        ...

    @m_21.setter
    def m_21(self, value: float) -> None:
        ...

    @property
    def m_22(self) -> float:
        """The second element of the second row."""
        ...

    @m_22.setter
    def m_22(self, value: float) -> None:
        ...

    @property
    def m_31(self) -> float:
        """The first element of the third row."""
        ...

    @m_31.setter
    def m_31(self, value: float) -> None:
        ...

    @property
    def m_32(self) -> float:
        """The second element of the third row."""
        ...

    @m_32.setter
    def m_32(self, value: float) -> None:
        ...

    IDENTITY: System.Numerics.Matrix3x2
    """Gets the multiplicative identity matrix."""

    @property
    def is_identity(self) -> bool:
        """Gets a value that indicates whether the current matrix is the identity matrix."""
        ...

    @property
    def translation(self) -> System.Numerics.Vector2:
        """Gets or sets the translation component of this matrix."""
        ...

    @translation.setter
    def translation(self, value: System.Numerics.Vector2) -> None:
        ...

    def __add__(self, value_2: System.Numerics.Matrix3x2) -> System.Numerics.Matrix3x2:
        """
        Adds each element in one matrix with its corresponding element in a second matrix.
        
        :param value1: The first matrix.
        :param value_2: The second matrix.
        :returns: The matrix that contains the summed values.
        """
        ...

    def __eq__(self, value_2: System.Numerics.Matrix3x2) -> bool:
        """
        Returns a value that indicates whether the specified matrices are equal.
        
        :param value1: The first matrix to compare.
        :param value_2: The second matrix to compare.
        :returns: true if  and  are equal; otherwise, false.
        """
        ...

    def __getitem__(self, row: int, column: int) -> float:
        """
        Gets or sets the element at the specified indices.
        
        :param row: The index of the row containing the element to get or set.
        :param column: The index of the column containing the element to get or set.
        :returns: The element at [][].
        """
        ...

    def __iadd__(self, value_2: System.Numerics.Matrix3x2) -> System.Numerics.Matrix3x2:
        """
        Adds each element in one matrix with its corresponding element in a second matrix.
        
        :param value1: The first matrix.
        :param value_2: The second matrix.
        :returns: The matrix that contains the summed values.
        """
        ...

    @overload
    def __imul__(self, value_2: System.Numerics.Matrix3x2) -> System.Numerics.Matrix3x2:
        """
        Multiplies two matrices together to compute the product.
        
        :param value1: The first matrix.
        :param value_2: The second matrix.
        :returns: The product matrix.
        """
        ...

    @overload
    def __imul__(self, value_2: float) -> System.Numerics.Matrix3x2:
        """
        Multiplies a matrix by a float to compute the product.
        
        :param value1: The matrix to scale.
        :param value_2: The scaling value to use.
        :returns: The scaled matrix.
        """
        ...

    def __init__(self, m_11: float, m_12: float, m_21: float, m_22: float, m_31: float, m_32: float) -> None:
        """
        Creates a 3x2 matrix from the specified components.
        
        :param m_11: The value to assign to the first element in the first row.
        :param m_12: The value to assign to the second element in the first row.
        :param m_21: The value to assign to the first element in the second row.
        :param m_22: The value to assign to the second element in the second row.
        :param m_31: The value to assign to the first element in the third row.
        :param m_32: The value to assign to the second element in the third row.
        """
        ...

    @overload
    def __isub__(self, value_2: System.Numerics.Matrix3x2) -> System.Numerics.Matrix3x2:
        """
        Subtracts each element in a second matrix from its corresponding element in a first matrix.
        
        :param value1: The first matrix.
        :param value_2: The second matrix.
        :returns: The matrix containing the values that result from subtracting each element in  from its corresponding element in .
        """
        ...

    @overload
    def __isub__(self) -> System.Numerics.Matrix3x2:
        """
        Negates the specified matrix by multiplying all its values by -1.
        
        :param value: The matrix to negate.
        :returns: The negated matrix.
        """
        ...

    @overload
    def __mul__(self, value_2: System.Numerics.Matrix3x2) -> System.Numerics.Matrix3x2:
        """
        Multiplies two matrices together to compute the product.
        
        :param value1: The first matrix.
        :param value_2: The second matrix.
        :returns: The product matrix.
        """
        ...

    @overload
    def __mul__(self, value_2: float) -> System.Numerics.Matrix3x2:
        """
        Multiplies a matrix by a float to compute the product.
        
        :param value1: The matrix to scale.
        :param value_2: The scaling value to use.
        :returns: The scaled matrix.
        """
        ...

    def __ne__(self, value_2: System.Numerics.Matrix3x2) -> bool:
        """
        Returns a value that indicates whether the specified matrices are not equal.
        
        :param value1: The first matrix to compare.
        :param value_2: The second matrix to compare.
        :returns: true if  and  are not equal; otherwise, false.
        """
        ...

    def __setitem__(self, row: int, column: int, value: float) -> None:
        """
        Gets or sets the element at the specified indices.
        
        :param row: The index of the row containing the element to get or set.
        :param column: The index of the column containing the element to get or set.
        :returns: The element at [][].
        """
        ...

    @overload
    def __sub__(self, value_2: System.Numerics.Matrix3x2) -> System.Numerics.Matrix3x2:
        """
        Subtracts each element in a second matrix from its corresponding element in a first matrix.
        
        :param value1: The first matrix.
        :param value_2: The second matrix.
        :returns: The matrix containing the values that result from subtracting each element in  from its corresponding element in .
        """
        ...

    @overload
    def __sub__(self) -> System.Numerics.Matrix3x2:
        """
        Negates the specified matrix by multiplying all its values by -1.
        
        :param value: The matrix to negate.
        :returns: The negated matrix.
        """
        ...

    @staticmethod
    def add(value_1: System.Numerics.Matrix3x2, value_2: System.Numerics.Matrix3x2) -> System.Numerics.Matrix3x2:
        """
        Adds each element in one matrix with its corresponding element in a second matrix.
        
        :param value_1: The first matrix.
        :param value_2: The second matrix.
        :returns: The matrix that contains the summed values of  and .
        """
        ...

    @staticmethod
    @overload
    def create_rotation(radians: float) -> System.Numerics.Matrix3x2:
        """
        Creates a rotation matrix using the given rotation in radians.
        
        :param radians: The amount of rotation, in radians.
        :returns: The rotation matrix.
        """
        ...

    @staticmethod
    @overload
    def create_rotation(radians: float, center_point: System.Numerics.Vector2) -> System.Numerics.Matrix3x2:
        """
        Creates a rotation matrix using the specified rotation in radians and a center point.
        
        :param radians: The amount of rotation, in radians.
        :param center_point: The center point.
        :returns: The rotation matrix.
        """
        ...

    @staticmethod
    @overload
    def create_scale(scales: System.Numerics.Vector2) -> System.Numerics.Matrix3x2:
        """
        Creates a scaling matrix from the specified vector scale.
        
        :param scales: The scale to use.
        :returns: The scaling matrix.
        """
        ...

    @staticmethod
    @overload
    def create_scale(x_scale: float, y_scale: float) -> System.Numerics.Matrix3x2:
        """
        Creates a scaling matrix from the specified X and Y components.
        
        :param x_scale: The value to scale by on the X axis.
        :param y_scale: The value to scale by on the Y axis.
        :returns: The scaling matrix.
        """
        ...

    @staticmethod
    @overload
    def create_scale(x_scale: float, y_scale: float, center_point: System.Numerics.Vector2) -> System.Numerics.Matrix3x2:
        """
        Creates a scaling matrix that is offset by a given center point.
        
        :param x_scale: The value to scale by on the X axis.
        :param y_scale: The value to scale by on the Y axis.
        :param center_point: The center point.
        :returns: The scaling matrix.
        """
        ...

    @staticmethod
    @overload
    def create_scale(scales: System.Numerics.Vector2, center_point: System.Numerics.Vector2) -> System.Numerics.Matrix3x2:
        """
        Creates a scaling matrix from the specified vector scale with an offset from the specified center point.
        
        :param scales: The scale to use.
        :param center_point: The center offset.
        :returns: The scaling matrix.
        """
        ...

    @staticmethod
    @overload
    def create_scale(scale: float) -> System.Numerics.Matrix3x2:
        """
        Creates a scaling matrix that scales uniformly with the given scale.
        
        :param scale: The uniform scale to use.
        :returns: The scaling matrix.
        """
        ...

    @staticmethod
    @overload
    def create_scale(scale: float, center_point: System.Numerics.Vector2) -> System.Numerics.Matrix3x2:
        """
        Creates a scaling matrix that scales uniformly with the specified scale with an offset from the specified center.
        
        :param scale: The uniform scale to use.
        :param center_point: The center offset.
        :returns: The scaling matrix.
        """
        ...

    @staticmethod
    @overload
    def create_skew(radians_x: float, radians_y: float) -> System.Numerics.Matrix3x2:
        """
        Creates a skew matrix from the specified angles in radians.
        
        :param radians_x: The X angle, in radians.
        :param radians_y: The Y angle, in radians.
        :returns: The skew matrix.
        """
        ...

    @staticmethod
    @overload
    def create_skew(radians_x: float, radians_y: float, center_point: System.Numerics.Vector2) -> System.Numerics.Matrix3x2:
        """
        Creates a skew matrix from the specified angles in radians and a center point.
        
        :param radians_x: The X angle, in radians.
        :param radians_y: The Y angle, in radians.
        :param center_point: The center point.
        :returns: The skew matrix.
        """
        ...

    @staticmethod
    @overload
    def create_translation(position: System.Numerics.Vector2) -> System.Numerics.Matrix3x2:
        """
        Creates a translation matrix from the specified 2-dimensional vector.
        
        :param position: The translation position.
        :returns: The translation matrix.
        """
        ...

    @staticmethod
    @overload
    def create_translation(x_position: float, y_position: float) -> System.Numerics.Matrix3x2:
        """
        Creates a translation matrix from the specified X and Y components.
        
        :param x_position: The X position.
        :param y_position: The Y position.
        :returns: The translation matrix.
        """
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        """
        Returns a value that indicates whether this instance and a specified object are equal.
        
        :param obj: The object to compare with the current instance.
        :returns: true if the current instance and  are equal; otherwise, false. If  is null, the method returns false.
        """
        ...

    @overload
    def equals(self, other: System.Numerics.Matrix3x2) -> bool:
        """
        Returns a value that indicates whether this instance and another 3x2 matrix are equal.
        
        :param other: The other matrix.
        :returns: true if the two matrices are equal; otherwise, false.
        """
        ...

    def get_determinant(self) -> float:
        """
        Calculates the determinant for this matrix.
        
        :returns: The determinant.
        """
        ...

    def get_hash_code(self) -> int:
        """
        Returns the hash code for this instance.
        
        :returns: The hash code.
        """
        ...

    @staticmethod
    def invert(matrix: System.Numerics.Matrix3x2, result: typing.Optional[System.Numerics.Matrix3x2]) -> typing.Tuple[bool, System.Numerics.Matrix3x2]:
        """
        Tries to invert the specified matrix. The return value indicates whether the operation succeeded.
        
        :param matrix: The matrix to invert.
        :param result: When this method returns, contains the inverted matrix if the operation succeeded.
        :returns: true if  was converted successfully; otherwise,  false.
        """
        ...

    @staticmethod
    def lerp(matrix_1: System.Numerics.Matrix3x2, matrix_2: System.Numerics.Matrix3x2, amount: float) -> System.Numerics.Matrix3x2:
        """
        Performs a linear interpolation from one matrix to a second matrix based on a value that specifies the weighting of the second matrix.
        
        :param matrix_1: The first matrix.
        :param matrix_2: The second matrix.
        :param amount: The relative weighting of .
        :returns: The interpolated matrix.
        """
        ...

    @staticmethod
    @overload
    def multiply(value_1: System.Numerics.Matrix3x2, value_2: System.Numerics.Matrix3x2) -> System.Numerics.Matrix3x2:
        """
        Multiplies two matrices together to compute the product.
        
        :param value_1: The first matrix.
        :param value_2: The second matrix.
        :returns: The product matrix.
        """
        ...

    @staticmethod
    @overload
    def multiply(value_1: System.Numerics.Matrix3x2, value_2: float) -> System.Numerics.Matrix3x2:
        """
        Multiplies a matrix by a float to compute the product.
        
        :param value_1: The matrix to scale.
        :param value_2: The scaling value to use.
        :returns: The scaled matrix.
        """
        ...

    @staticmethod
    def negate(value: System.Numerics.Matrix3x2) -> System.Numerics.Matrix3x2:
        """
        Negates the specified matrix by multiplying all its values by -1.
        
        :param value: The matrix to negate.
        :returns: The negated matrix.
        """
        ...

    @staticmethod
    def subtract(value_1: System.Numerics.Matrix3x2, value_2: System.Numerics.Matrix3x2) -> System.Numerics.Matrix3x2:
        """
        Subtracts each element in a second matrix from its corresponding element in a first matrix.
        
        :param value_1: The first matrix.
        :param value_2: The second matrix.
        :returns: The matrix containing the values that result from subtracting each element in  from its corresponding element in .
        """
        ...

    def to_string(self) -> str:
        """
        Returns a string that represents this matrix.
        
        :returns: The string representation of this matrix.
        """
        ...


class IMultiplyOperators(typing.Generic[System_Numerics_IMultiplyOperators_TSelf, System_Numerics_IMultiplyOperators_TOther, System_Numerics_IMultiplyOperators_TResult], metaclass=abc.ABCMeta):
    """Defines a mechanism for computing the product of two values."""


class Vector3(System.IEquatable[System_Numerics_Vector3], System.IFormattable):
    """Represents a vector with three  single-precision floating-point values."""

    @property
    def x(self) -> float:
        """The X component of the vector."""
        ...

    @x.setter
    def x(self, value: float) -> None:
        ...

    @property
    def y(self) -> float:
        """The Y component of the vector."""
        ...

    @y.setter
    def y(self, value: float) -> None:
        ...

    @property
    def z(self) -> float:
        """The Z component of the vector."""
        ...

    @z.setter
    def z(self, value: float) -> None:
        ...

    ALL_BITS_SET: System.Numerics.Vector3

    E: System.Numerics.Vector3

    EPSILON: System.Numerics.Vector3

    NA_N: System.Numerics.Vector3

    NEGATIVE_INFINITY: System.Numerics.Vector3

    NEGATIVE_ZERO: System.Numerics.Vector3

    ONE: System.Numerics.Vector3

    PI: System.Numerics.Vector3

    POSITIVE_INFINITY: System.Numerics.Vector3

    TAU: System.Numerics.Vector3

    UNIT_X: System.Numerics.Vector3
    """Gets the vector (1,0,0)."""

    UNIT_Y: System.Numerics.Vector3
    """Gets the vector (0,1,0)."""

    UNIT_Z: System.Numerics.Vector3
    """Gets the vector (0,0,1)."""

    ZERO: System.Numerics.Vector3

    @overload
    def __add__(self, right: System.Numerics.Vector3) -> System.Numerics.Vector3:
        """
        Adds two vectors together.
        
        :param left: The first vector to add.
        :param right: The second vector to add.
        :returns: The summed vector.
        """
        ...

    @overload
    def __add__(self) -> System.Numerics.Vector3:
        ...

    def __and__(self, right: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    def __eq__(self, right: System.Numerics.Vector3) -> bool:
        """
        Returns a value that indicates whether each pair of elements in two specified vectors is equal.
        
        :param left: The first vector to compare.
        :param right: The second vector to compare.
        :returns: true if  and  are equal; otherwise, false.
        """
        ...

    def __getitem__(self, index: int) -> float:
        """
        Gets or sets the element at the specified index.
        
        :param index: The index of the element to get or set.
        :returns: The the element at .
        """
        ...

    @overload
    def __iadd__(self, right: System.Numerics.Vector3) -> System.Numerics.Vector3:
        """
        Adds two vectors together.
        
        :param left: The first vector to add.
        :param right: The second vector to add.
        :returns: The summed vector.
        """
        ...

    @overload
    def __iadd__(self) -> System.Numerics.Vector3:
        ...

    def __iand__(self, right: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    def __ilshift__(self, shift_amount: int) -> System.Numerics.Vector3:
        ...

    @overload
    def __imul__(self, right: System.Numerics.Vector3) -> System.Numerics.Vector3:
        """
        Returns a new vector whose values are the product of each pair of elements in two specified vectors.
        
        :param left: The first vector.
        :param right: The second vector.
        :returns: The element-wise product vector.
        """
        ...

    @overload
    def __imul__(self, right: float) -> System.Numerics.Vector3:
        """
        Multiplies the specified vector by the specified scalar value.
        
        :param left: The vector.
        :param right: The scalar value.
        :returns: The scaled vector.
        """
        ...

    @overload
    def __imul__(self, right: System.Numerics.Vector3) -> System.Numerics.Vector3:
        """
        Multiplies the scalar value by the specified vector.
        
        :param left: The vector.
        :param right: The scalar value.
        :returns: The scaled vector.
        """
        ...

    @overload
    def __init__(self, value: float) -> None:
        """
        Creates a new Vector3 object whose three elements have the same value.
        
        :param value: The value to assign to all three elements.
        """
        ...

    @overload
    def __init__(self, value: System.Numerics.Vector2, z: float) -> None:
        """
        Creates a   new Vector3 object from the specified Vector2 object and the specified value.
        
        :param value: The vector with two elements.
        :param z: The additional value to assign to the Z field.
        """
        ...

    @overload
    def __init__(self, x: float, y: float, z: float) -> None:
        """
        Creates a vector whose elements have the specified values.
        
        :param x: The value to assign to the X field.
        :param y: The value to assign to the Y field.
        :param z: The value to assign to the Z field.
        """
        ...

    @overload
    def __init__(self, values: System.ReadOnlySpan[float]) -> None:
        """
        Constructs a vector from the given ReadOnlySpan{Single}. The span must contain at least 3 elements.
        
        :param values: The span of elements to assign to the vector.
        """
        ...

    def __invert__(self) -> System.Numerics.Vector3:
        ...

    def __ior__(self, right: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    def __irshift__(self, shift_amount: int) -> System.Numerics.Vector3:
        ...

    @overload
    def __isub__(self, right: System.Numerics.Vector3) -> System.Numerics.Vector3:
        """
        Subtracts the second vector from the first.
        
        :param left: The first vector.
        :param right: The second vector.
        :returns: The vector that results from subtracting  from .
        """
        ...

    @overload
    def __isub__(self) -> System.Numerics.Vector3:
        """
        Negates the specified vector.
        
        :param value: The vector to negate.
        :returns: The negated vector.
        """
        ...

    @overload
    def __itruediv__(self, right: System.Numerics.Vector3) -> System.Numerics.Vector3:
        """
        Divides the first vector by the second.
        
        :param left: The first vector.
        :param right: The second vector.
        :returns: The vector that results from dividing  by .
        """
        ...

    @overload
    def __itruediv__(self, value_2: float) -> System.Numerics.Vector3:
        """
        Divides the specified vector by a specified scalar value.
        
        :param value1: The vector.
        :param value_2: The scalar value.
        :returns: The result of the division.
        """
        ...

    def __ixor__(self, right: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    def __lshift__(self, shift_amount: int) -> System.Numerics.Vector3:
        ...

    @overload
    def __mul__(self, right: System.Numerics.Vector3) -> System.Numerics.Vector3:
        """
        Returns a new vector whose values are the product of each pair of elements in two specified vectors.
        
        :param left: The first vector.
        :param right: The second vector.
        :returns: The element-wise product vector.
        """
        ...

    @overload
    def __mul__(self, right: float) -> System.Numerics.Vector3:
        """
        Multiplies the specified vector by the specified scalar value.
        
        :param left: The vector.
        :param right: The scalar value.
        :returns: The scaled vector.
        """
        ...

    @overload
    def __mul__(self, right: System.Numerics.Vector3) -> System.Numerics.Vector3:
        """
        Multiplies the scalar value by the specified vector.
        
        :param left: The vector.
        :param right: The scalar value.
        :returns: The scaled vector.
        """
        ...

    def __ne__(self, right: System.Numerics.Vector3) -> bool:
        """
        Returns a value that indicates whether two specified vectors are not equal.
        
        :param left: The first vector to compare.
        :param right: The second vector to compare.
        :returns: true if  and  are not equal; otherwise, false.
        """
        ...

    def __or__(self, right: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    def __rshift__(self, shift_amount: int) -> System.Numerics.Vector3:
        ...

    def __setitem__(self, index: int, value: float) -> None:
        """
        Gets or sets the element at the specified index.
        
        :param index: The index of the element to get or set.
        :returns: The the element at .
        """
        ...

    @overload
    def __sub__(self, right: System.Numerics.Vector3) -> System.Numerics.Vector3:
        """
        Subtracts the second vector from the first.
        
        :param left: The first vector.
        :param right: The second vector.
        :returns: The vector that results from subtracting  from .
        """
        ...

    @overload
    def __sub__(self) -> System.Numerics.Vector3:
        """
        Negates the specified vector.
        
        :param value: The vector to negate.
        :returns: The negated vector.
        """
        ...

    @overload
    def __truediv__(self, right: System.Numerics.Vector3) -> System.Numerics.Vector3:
        """
        Divides the first vector by the second.
        
        :param left: The first vector.
        :param right: The second vector.
        :returns: The vector that results from dividing  by .
        """
        ...

    @overload
    def __truediv__(self, value_2: float) -> System.Numerics.Vector3:
        """
        Divides the specified vector by a specified scalar value.
        
        :param value1: The vector.
        :param value_2: The scalar value.
        :returns: The result of the division.
        """
        ...

    def __xor__(self, right: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def abs(value: System.Numerics.Vector3) -> System.Numerics.Vector3:
        """
        Returns a vector whose elements are the absolute values of each of the specified vector's elements.
        
        :param value: A vector.
        :returns: The absolute value vector.
        """
        ...

    @staticmethod
    def add(left: System.Numerics.Vector3, right: System.Numerics.Vector3) -> System.Numerics.Vector3:
        """
        Adds two vectors together.
        
        :param left: The first vector to add.
        :param right: The second vector to add.
        :returns: The summed vector.
        """
        ...

    @staticmethod
    def all(vector: System.Numerics.Vector3, value: float) -> bool:
        ...

    @staticmethod
    def all_where_all_bits_set(vector: System.Numerics.Vector3) -> bool:
        ...

    @staticmethod
    def and_not(left: System.Numerics.Vector3, right: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def any(vector: System.Numerics.Vector3, value: float) -> bool:
        ...

    @staticmethod
    def any_where_all_bits_set(vector: System.Numerics.Vector3) -> bool:
        ...

    @staticmethod
    def bitwise_and(left: System.Numerics.Vector3, right: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def bitwise_or(left: System.Numerics.Vector3, right: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def clamp(value_1: System.Numerics.Vector3, min: System.Numerics.Vector3, max: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def clamp_native(value_1: System.Numerics.Vector3, min: System.Numerics.Vector3, max: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def conditional_select(condition: System.Numerics.Vector3, left: System.Numerics.Vector3, right: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def copy_sign(value: System.Numerics.Vector3, sign: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @overload
    def copy_to(self, array: typing.List[float]) -> None:
        """
        Copies the elements of the vector to a specified array.
        
        :param array: The destination array.
        """
        ...

    @overload
    def copy_to(self, array: typing.List[float], index: int) -> None:
        """
        Copies the elements of the vector to a specified array starting at a specified index position.
        
        :param array: The destination array.
        :param index: The index at which to copy the first element of the vector.
        """
        ...

    @overload
    def copy_to(self, destination: System.Span[float]) -> None:
        """
        Copies the vector to the given Span{T}. The length of the destination span must be at least 3.
        
        :param destination: The destination span which the values are copied into.
        """
        ...

    @staticmethod
    def cos(vector: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def count(vector: System.Numerics.Vector3, value: float) -> int:
        ...

    @staticmethod
    def count_where_all_bits_set(vector: System.Numerics.Vector3) -> int:
        ...

    @staticmethod
    @overload
    def create(value: float) -> System.Numerics.Vector3:
        """
        Creates a new Vector3 object whose three elements have the same value.
        
        :param value: The value to assign to all three elements.
        :returns: A new Vector3 whose three elements have the same value.
        """
        ...

    @staticmethod
    @overload
    def create(vector: System.Numerics.Vector2, z: float) -> System.Numerics.Vector3:
        """
        Creates a new Vector3 object from the specified Vector2 object and a Z and a W component.
        
        :param vector: The vector to use for the X and Y components.
        :param z: The Z component.
        :returns: A new Vector3 from the specified Vector2 object and a Z and a W component.
        """
        ...

    @staticmethod
    @overload
    def create(x: float, y: float, z: float) -> System.Numerics.Vector3:
        """
        Creates a vector whose elements have the specified values.
        
        :param x: The value to assign to the X field.
        :param y: The value to assign to the Y field.
        :param z: The value to assign to the Z field.
        :returns: A new Vector3 whose elements have the specified values.
        """
        ...

    @staticmethod
    @overload
    def create(values: System.ReadOnlySpan[float]) -> System.Numerics.Vector3:
        """
        Constructs a vector from the given ReadOnlySpan{Single}. The span must contain at least 3 elements.
        
        :param values: The span of elements to assign to the vector.
        :returns: A new Vector3 whose elements have the specified values.
        """
        ...

    @staticmethod
    def cross(vector_1: System.Numerics.Vector3, vector_2: System.Numerics.Vector3) -> System.Numerics.Vector3:
        """
        Computes the cross product of two vectors.
        
        :param vector_1: The first vector.
        :param vector_2: The second vector.
        :returns: The cross product.
        """
        ...

    @staticmethod
    def degrees_to_radians(degrees: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def distance(value_1: System.Numerics.Vector3, value_2: System.Numerics.Vector3) -> float:
        """
        Computes the Euclidean distance between the two given points.
        
        :param value_1: The first point.
        :param value_2: The second point.
        :returns: The distance.
        """
        ...

    @staticmethod
    def distance_squared(value_1: System.Numerics.Vector3, value_2: System.Numerics.Vector3) -> float:
        """
        Returns the Euclidean distance squared between two specified points.
        
        :param value_1: The first point.
        :param value_2: The second point.
        :returns: The distance squared.
        """
        ...

    @staticmethod
    @overload
    def divide(left: System.Numerics.Vector3, right: System.Numerics.Vector3) -> System.Numerics.Vector3:
        """
        Divides the first vector by the second.
        
        :param left: The first vector.
        :param right: The second vector.
        :returns: The vector resulting from the division.
        """
        ...

    @staticmethod
    @overload
    def divide(left: System.Numerics.Vector3, divisor: float) -> System.Numerics.Vector3:
        """
        Divides the specified vector by a specified scalar value.
        
        :param left: The vector.
        :param divisor: The scalar value.
        :returns: The vector that results from the division.
        """
        ...

    @staticmethod
    def dot(vector_1: System.Numerics.Vector3, vector_2: System.Numerics.Vector3) -> float:
        """
        Returns the dot product of two vectors.
        
        :param vector_1: The first vector.
        :param vector_2: The second vector.
        :returns: The dot product.
        """
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        """
        Returns a value that indicates whether this instance and a specified object are equal.
        
        :param obj: The object to compare with the current instance.
        :returns: true if the current instance and  are equal; otherwise, false. If  is null, the method returns false.
        """
        ...

    @staticmethod
    @overload
    def equals(left: System.Numerics.Vector3, right: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @overload
    def equals(self, other: System.Numerics.Vector3) -> bool:
        """
        Returns a value that indicates whether this instance and another vector are equal.
        
        :param other: The other vector.
        :returns: true if the two vectors are equal; otherwise, false.
        """
        ...

    @staticmethod
    def equals_all(left: System.Numerics.Vector3, right: System.Numerics.Vector3) -> bool:
        ...

    @staticmethod
    def equals_any(left: System.Numerics.Vector3, right: System.Numerics.Vector3) -> bool:
        ...

    @staticmethod
    def exp(vector: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def fused_multiply_add(left: System.Numerics.Vector3, right: System.Numerics.Vector3, addend: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    def get_hash_code(self) -> int:
        """
        Returns the hash code for this instance.
        
        :returns: The hash code.
        """
        ...

    @staticmethod
    def greater_than(left: System.Numerics.Vector3, right: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def greater_than_all(left: System.Numerics.Vector3, right: System.Numerics.Vector3) -> bool:
        ...

    @staticmethod
    def greater_than_any(left: System.Numerics.Vector3, right: System.Numerics.Vector3) -> bool:
        ...

    @staticmethod
    def greater_than_or_equal(left: System.Numerics.Vector3, right: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def greater_than_or_equal_all(left: System.Numerics.Vector3, right: System.Numerics.Vector3) -> bool:
        ...

    @staticmethod
    def greater_than_or_equal_any(left: System.Numerics.Vector3, right: System.Numerics.Vector3) -> bool:
        ...

    @staticmethod
    def hypot(x: System.Numerics.Vector3, y: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def index_of(vector: System.Numerics.Vector3, value: float) -> int:
        ...

    @staticmethod
    def index_of_where_all_bits_set(vector: System.Numerics.Vector3) -> int:
        ...

    @staticmethod
    def is_even_integer(vector: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def is_finite(vector: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def is_infinity(vector: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def is_integer(vector: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def is_na_n(vector: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def is_negative(vector: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def is_negative_infinity(vector: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def is_normal(vector: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def is_odd_integer(vector: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def is_positive(vector: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def is_positive_infinity(vector: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def is_subnormal(vector: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def is_zero(vector: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def last_index_of(vector: System.Numerics.Vector3, value: float) -> int:
        ...

    @staticmethod
    def last_index_of_where_all_bits_set(vector: System.Numerics.Vector3) -> int:
        ...

    def length(self) -> float:
        """
        Returns the length of this vector object.
        
        :returns: The vector's length.
        """
        ...

    def length_squared(self) -> float:
        """
        Returns the length of the vector squared.
        
        :returns: The vector's length squared.
        """
        ...

    @staticmethod
    @overload
    def lerp(value_1: System.Numerics.Vector3, value_2: System.Numerics.Vector3, amount: float) -> System.Numerics.Vector3:
        ...

    @staticmethod
    @overload
    def lerp(value_1: System.Numerics.Vector3, value_2: System.Numerics.Vector3, amount: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def less_than(left: System.Numerics.Vector3, right: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def less_than_all(left: System.Numerics.Vector3, right: System.Numerics.Vector3) -> bool:
        ...

    @staticmethod
    def less_than_any(left: System.Numerics.Vector3, right: System.Numerics.Vector3) -> bool:
        ...

    @staticmethod
    def less_than_or_equal(left: System.Numerics.Vector3, right: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def less_than_or_equal_all(left: System.Numerics.Vector3, right: System.Numerics.Vector3) -> bool:
        ...

    @staticmethod
    def less_than_or_equal_any(left: System.Numerics.Vector3, right: System.Numerics.Vector3) -> bool:
        ...

    @staticmethod
    def load(source: typing.Any) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def load_aligned(source: typing.Any) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def load_aligned_non_temporal(source: typing.Any) -> System.Numerics.Vector3:
        ...

    @staticmethod
    @overload
    def load_unsafe(source: float) -> System.Numerics.Vector3:
        ...

    @staticmethod
    @overload
    def load_unsafe(source: float, element_offset: System.UIntPtr) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def log(vector: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def log_2(vector: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def max(value_1: System.Numerics.Vector3, value_2: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def max_magnitude(value_1: System.Numerics.Vector3, value_2: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def max_magnitude_number(value_1: System.Numerics.Vector3, value_2: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def max_native(value_1: System.Numerics.Vector3, value_2: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def max_number(value_1: System.Numerics.Vector3, value_2: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def min(value_1: System.Numerics.Vector3, value_2: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def min_magnitude(value_1: System.Numerics.Vector3, value_2: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def min_magnitude_number(value_1: System.Numerics.Vector3, value_2: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def min_native(value_1: System.Numerics.Vector3, value_2: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def min_number(value_1: System.Numerics.Vector3, value_2: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    @overload
    def multiply(left: System.Numerics.Vector3, right: System.Numerics.Vector3) -> System.Numerics.Vector3:
        """
        Returns a new vector whose values are the product of each pair of elements in two specified vectors.
        
        :param left: The first vector.
        :param right: The second vector.
        :returns: The element-wise product vector.
        """
        ...

    @staticmethod
    @overload
    def multiply(left: System.Numerics.Vector3, right: float) -> System.Numerics.Vector3:
        """
        Multiplies a vector by a specified scalar.
        
        :param left: The vector to multiply.
        :param right: The scalar value.
        :returns: The scaled vector.
        """
        ...

    @staticmethod
    @overload
    def multiply(left: float, right: System.Numerics.Vector3) -> System.Numerics.Vector3:
        """
        Multiplies a scalar value by a specified vector.
        
        :param left: The scaled value.
        :param right: The vector.
        :returns: The scaled vector.
        """
        ...

    @staticmethod
    def multiply_add_estimate(left: System.Numerics.Vector3, right: System.Numerics.Vector3, addend: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def negate(value: System.Numerics.Vector3) -> System.Numerics.Vector3:
        """
        Negates a specified vector.
        
        :param value: The vector to negate.
        :returns: The negated vector.
        """
        ...

    @staticmethod
    def none(vector: System.Numerics.Vector3, value: float) -> bool:
        ...

    @staticmethod
    def none_where_all_bits_set(vector: System.Numerics.Vector3) -> bool:
        ...

    @staticmethod
    def normalize(value: System.Numerics.Vector3) -> System.Numerics.Vector3:
        """
        Returns a vector with the same direction as the specified vector, but with a length of one.
        
        :param value: The vector to normalize.
        :returns: The normalized vector.
        """
        ...

    @staticmethod
    def ones_complement(value: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def radians_to_degrees(radians: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def reflect(vector: System.Numerics.Vector3, normal: System.Numerics.Vector3) -> System.Numerics.Vector3:
        """
        Returns the reflection of a vector off a surface that has the specified normal.
        
        :param vector: The source vector.
        :param normal: The normal of the surface being reflected off.
        :returns: The reflected vector.
        """
        ...

    @staticmethod
    @overload
    def round(vector: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    @overload
    def round(vector: System.Numerics.Vector3, mode: System.MidpointRounding) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def shuffle(vector: System.Numerics.Vector3, x_index: int, y_index: int, z_index: int) -> System.Numerics.Vector3:
        """
        Creates a new vector by selecting values from an input vector using a set of indices.
        
        :param vector: The input vector from which values are selected.
        :param x_index: The index used to select a value from  to be used as the value of X in the result.
        :param y_index: The index used to select a value from  to be used as the value of Y in the result
        :param z_index: The index used to select a value from  to be used as the value of Z in the result
        :returns: A new vector containing the values from  selected by the given indices.
        """
        ...

    @staticmethod
    def sin(vector: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    @staticmethod
    def sin_cos(vector: System.Numerics.Vector3) -> System.ValueTuple[System.Numerics.Vector3, System.Numerics.Vector3]:
        ...

    @staticmethod
    def square_root(value: System.Numerics.Vector3) -> System.Numerics.Vector3:
        """
        Returns a vector whose elements are the square root of each of a specified vector's elements.
        
        :param value: A vector.
        :returns: The square root vector.
        """
        ...

    @staticmethod
    def subtract(left: System.Numerics.Vector3, right: System.Numerics.Vector3) -> System.Numerics.Vector3:
        """
        Subtracts the second vector from the first.
        
        :param left: The first vector.
        :param right: The second vector.
        :returns: The difference vector.
        """
        ...

    @staticmethod
    def sum(value: System.Numerics.Vector3) -> float:
        ...

    @overload
    def to_string(self) -> str:
        """
        Returns the string representation of the current instance using default formatting.
        
        :returns: The string representation of the current instance.
        """
        ...

    @overload
    def to_string(self, format: str) -> str:
        """
        Returns the string representation of the current instance using the specified format string to format individual elements.
        
        :param format: A standard or custom numeric format string that defines the format of individual elements.
        :returns: The string representation of the current instance.
        """
        ...

    @overload
    def to_string(self, format: str, format_provider: System.IFormatProvider) -> str:
        """
        Returns the string representation of the current instance using the specified format string to format individual elements and the specified format provider to define culture-specific formatting.
        
        :param format: A standard or custom numeric format string that defines the format of individual elements.
        :param format_provider: A format provider that supplies culture-specific formatting information.
        :returns: The string representation of the current instance.
        """
        ...

    @staticmethod
    @overload
    def transform(position: System.Numerics.Vector3, matrix: System.Numerics.Matrix4x4) -> System.Numerics.Vector3:
        """
        Transforms a vector by a specified 4x4 matrix.
        
        :param position: The vector to transform.
        :param matrix: The transformation matrix.
        :returns: The transformed vector.
        """
        ...

    @staticmethod
    @overload
    def transform(value: System.Numerics.Vector3, rotation: System.Numerics.Quaternion) -> System.Numerics.Vector3:
        """
        Transforms a vector by the specified Quaternion rotation value.
        
        :param value: The vector to rotate.
        :param rotation: The rotation to apply.
        :returns: The transformed vector.
        """
        ...

    @staticmethod
    def transform_normal(normal: System.Numerics.Vector3, matrix: System.Numerics.Matrix4x4) -> System.Numerics.Vector3:
        """
        Transforms a vector normal by the given 4x4 matrix.
        
        :param normal: The source vector.
        :param matrix: The matrix.
        :returns: The transformed vector.
        """
        ...

    @staticmethod
    def truncate(vector: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...

    def try_copy_to(self, destination: System.Span[float]) -> bool:
        """
        Attempts to copy the vector to the given Span{Single}. The length of the destination span must be at least 3.
        
        :param destination: The destination span which the values are copied into.
        :returns: true if the source vector was successfully copied to . false if  is not large enough to hold the source vector.
        """
        ...

    @staticmethod
    def xor(left: System.Numerics.Vector3, right: System.Numerics.Vector3) -> System.Numerics.Vector3:
        ...


class Vector4(System.IEquatable[System_Numerics_Vector4], System.IFormattable):
    """Represents a vector with four single-precision floating-point values."""

    @property
    def x(self) -> float:
        """The X component of the vector."""
        ...

    @x.setter
    def x(self, value: float) -> None:
        ...

    @property
    def y(self) -> float:
        """The Y component of the vector."""
        ...

    @y.setter
    def y(self, value: float) -> None:
        ...

    @property
    def z(self) -> float:
        """The Z component of the vector."""
        ...

    @z.setter
    def z(self, value: float) -> None:
        ...

    @property
    def w(self) -> float:
        """The W component of the vector."""
        ...

    @w.setter
    def w(self, value: float) -> None:
        ...

    ALL_BITS_SET: System.Numerics.Vector4
    """Gets a vector where all bits are set to 1."""

    E: System.Numerics.Vector4
    """Gets a vector whose elements are equal to float.E."""

    EPSILON: System.Numerics.Vector4
    """Gets a vector whose elements are equal to float.Epsilon."""

    NA_N: System.Numerics.Vector4
    """Gets a vector whose elements are equal to float.NaN."""

    NEGATIVE_INFINITY: System.Numerics.Vector4
    """Gets a vector whose elements are equal to float.NegativeInfinity."""

    NEGATIVE_ZERO: System.Numerics.Vector4
    """Gets a vector whose elements are equal to float.NegativeZero."""

    ONE: System.Numerics.Vector4
    """Gets a vector whose elements are equal to one."""

    PI: System.Numerics.Vector4
    """Gets a vector whose elements are equal to float.Pi."""

    POSITIVE_INFINITY: System.Numerics.Vector4
    """Gets a vector whose elements are equal to float.PositiveInfinity."""

    TAU: System.Numerics.Vector4
    """Gets a vector whose elements are equal to float.Tau."""

    UNIT_X: System.Numerics.Vector4
    """Gets the vector (1,0,0,0)."""

    UNIT_Y: System.Numerics.Vector4
    """Gets the vector (0,1,0,0)."""

    UNIT_Z: System.Numerics.Vector4
    """Gets the vector (0,0,1,0)."""

    UNIT_W: System.Numerics.Vector4
    """Gets the vector (0,0,0,1)."""

    ZERO: System.Numerics.Vector4
    """Gets a vector whose elements are equal to zero."""

    @overload
    def __add__(self, right: System.Numerics.Vector4) -> System.Numerics.Vector4:
        """
        Adds two vectors together.
        
        :param left: The first vector to add.
        :param right: The second vector to add.
        :returns: The summed vector.
        """
        ...

    @overload
    def __add__(self) -> System.Numerics.Vector4:
        ...

    def __and__(self, right: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    def __eq__(self, right: System.Numerics.Vector4) -> bool:
        """
        Returns a value that indicates whether each pair of elements in two specified vectors is equal.
        
        :param left: The first vector to compare.
        :param right: The second vector to compare.
        :returns: true if  and  are equal; otherwise, false.
        """
        ...

    def __getitem__(self, index: int) -> float:
        """
        Gets or sets the element at the specified index.
        
        :param index: The index of the element to get or set.
        :returns: The the element at .
        """
        ...

    @overload
    def __iadd__(self, right: System.Numerics.Vector4) -> System.Numerics.Vector4:
        """
        Adds two vectors together.
        
        :param left: The first vector to add.
        :param right: The second vector to add.
        :returns: The summed vector.
        """
        ...

    @overload
    def __iadd__(self) -> System.Numerics.Vector4:
        ...

    def __iand__(self, right: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    def __ilshift__(self, shift_amount: int) -> System.Numerics.Vector4:
        ...

    @overload
    def __imul__(self, right: System.Numerics.Vector4) -> System.Numerics.Vector4:
        """
        Returns a new vector whose values are the product of each pair of elements in two specified vectors.
        
        :param left: The first vector.
        :param right: The second vector.
        :returns: The element-wise product vector.
        """
        ...

    @overload
    def __imul__(self, right: float) -> System.Numerics.Vector4:
        """
        Multiplies the specified vector by the specified scalar value.
        
        :param left: The vector.
        :param right: The scalar value.
        :returns: The scaled vector.
        """
        ...

    @overload
    def __imul__(self, right: System.Numerics.Vector4) -> System.Numerics.Vector4:
        """
        Multiplies the scalar value by the specified vector.
        
        :param left: The vector.
        :param right: The scalar value.
        :returns: The scaled vector.
        """
        ...

    @overload
    def __init__(self, value: float) -> None:
        """
        Creates a new Vector4 object whose four elements have the same value.
        
        :param value: The value to assign to all four elements.
        """
        ...

    @overload
    def __init__(self, value: System.Numerics.Vector2, z: float, w: float) -> None:
        """
        Creates a   new Vector4 object from the specified Vector2 object and a Z and a W component.
        
        :param value: The vector to use for the X and Y components.
        :param z: The Z component.
        :param w: The W component.
        """
        ...

    @overload
    def __init__(self, value: System.Numerics.Vector3, w: float) -> None:
        """
        Constructs a new Vector4 object from the specified Vector3 object and a W component.
        
        :param value: The vector to use for the X, Y, and Z components.
        :param w: The W component.
        """
        ...

    @overload
    def __init__(self, x: float, y: float, z: float, w: float) -> None:
        """
        Creates a vector whose elements have the specified values.
        
        :param x: The value to assign to the X field.
        :param y: The value to assign to the Y field.
        :param z: The value to assign to the Z field.
        :param w: The value to assign to the W field.
        """
        ...

    @overload
    def __init__(self, values: System.ReadOnlySpan[float]) -> None:
        """
        Constructs a vector from the given ReadOnlySpan{Single}. The span must contain at least 4 elements.
        
        :param values: The span of elements to assign to the vector.
        """
        ...

    def __invert__(self) -> System.Numerics.Vector4:
        ...

    def __ior__(self, right: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    def __irshift__(self, shift_amount: int) -> System.Numerics.Vector4:
        ...

    @overload
    def __isub__(self, right: System.Numerics.Vector4) -> System.Numerics.Vector4:
        """
        Subtracts the second vector from the first.
        
        :param left: The first vector.
        :param right: The second vector.
        :returns: The vector that results from subtracting  from .
        """
        ...

    @overload
    def __isub__(self) -> System.Numerics.Vector4:
        """
        Negates the specified vector.
        
        :param value: The vector to negate.
        :returns: The negated vector.
        """
        ...

    @overload
    def __itruediv__(self, right: System.Numerics.Vector4) -> System.Numerics.Vector4:
        """
        Divides the first vector by the second.
        
        :param left: The first vector.
        :param right: The second vector.
        :returns: The vector that results from dividing  by .
        """
        ...

    @overload
    def __itruediv__(self, value_2: float) -> System.Numerics.Vector4:
        """
        Divides the specified vector by a specified scalar value.
        
        :param value1: The vector.
        :param value_2: The scalar value.
        :returns: The result of the division.
        """
        ...

    def __ixor__(self, right: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    def __lshift__(self, shift_amount: int) -> System.Numerics.Vector4:
        ...

    @overload
    def __mul__(self, right: System.Numerics.Vector4) -> System.Numerics.Vector4:
        """
        Returns a new vector whose values are the product of each pair of elements in two specified vectors.
        
        :param left: The first vector.
        :param right: The second vector.
        :returns: The element-wise product vector.
        """
        ...

    @overload
    def __mul__(self, right: float) -> System.Numerics.Vector4:
        """
        Multiplies the specified vector by the specified scalar value.
        
        :param left: The vector.
        :param right: The scalar value.
        :returns: The scaled vector.
        """
        ...

    @overload
    def __mul__(self, right: System.Numerics.Vector4) -> System.Numerics.Vector4:
        """
        Multiplies the scalar value by the specified vector.
        
        :param left: The vector.
        :param right: The scalar value.
        :returns: The scaled vector.
        """
        ...

    def __ne__(self, right: System.Numerics.Vector4) -> bool:
        """
        Returns a value that indicates whether two specified vectors are not equal.
        
        :param left: The first vector to compare.
        :param right: The second vector to compare.
        :returns: true if  and  are not equal; otherwise, false.
        """
        ...

    def __or__(self, right: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    def __rshift__(self, shift_amount: int) -> System.Numerics.Vector4:
        ...

    def __setitem__(self, index: int, value: float) -> None:
        """
        Gets or sets the element at the specified index.
        
        :param index: The index of the element to get or set.
        :returns: The the element at .
        """
        ...

    @overload
    def __sub__(self, right: System.Numerics.Vector4) -> System.Numerics.Vector4:
        """
        Subtracts the second vector from the first.
        
        :param left: The first vector.
        :param right: The second vector.
        :returns: The vector that results from subtracting  from .
        """
        ...

    @overload
    def __sub__(self) -> System.Numerics.Vector4:
        """
        Negates the specified vector.
        
        :param value: The vector to negate.
        :returns: The negated vector.
        """
        ...

    @overload
    def __truediv__(self, right: System.Numerics.Vector4) -> System.Numerics.Vector4:
        """
        Divides the first vector by the second.
        
        :param left: The first vector.
        :param right: The second vector.
        :returns: The vector that results from dividing  by .
        """
        ...

    @overload
    def __truediv__(self, value_2: float) -> System.Numerics.Vector4:
        """
        Divides the specified vector by a specified scalar value.
        
        :param value1: The vector.
        :param value_2: The scalar value.
        :returns: The result of the division.
        """
        ...

    def __xor__(self, right: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def abs(value: System.Numerics.Vector4) -> System.Numerics.Vector4:
        """
        Returns a vector whose elements are the absolute values of each of the specified vector's elements.
        
        :param value: A vector.
        :returns: The absolute value vector.
        """
        ...

    @staticmethod
    def add(left: System.Numerics.Vector4, right: System.Numerics.Vector4) -> System.Numerics.Vector4:
        """
        Adds two vectors together.
        
        :param left: The first vector to add.
        :param right: The second vector to add.
        :returns: The summed vector.
        """
        ...

    @staticmethod
    def all(vector: System.Numerics.Vector4, value: float) -> bool:
        ...

    @staticmethod
    def all_where_all_bits_set(vector: System.Numerics.Vector4) -> bool:
        ...

    @staticmethod
    def and_not(left: System.Numerics.Vector4, right: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def any(vector: System.Numerics.Vector4, value: float) -> bool:
        ...

    @staticmethod
    def any_where_all_bits_set(vector: System.Numerics.Vector4) -> bool:
        ...

    @staticmethod
    def bitwise_and(left: System.Numerics.Vector4, right: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def bitwise_or(left: System.Numerics.Vector4, right: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def clamp(value_1: System.Numerics.Vector4, min: System.Numerics.Vector4, max: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def clamp_native(value_1: System.Numerics.Vector4, min: System.Numerics.Vector4, max: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def conditional_select(condition: System.Numerics.Vector4, left: System.Numerics.Vector4, right: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def copy_sign(value: System.Numerics.Vector4, sign: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @overload
    def copy_to(self, array: typing.List[float]) -> None:
        """
        Copies the elements of the vector to a specified array.
        
        :param array: The destination array.
        """
        ...

    @overload
    def copy_to(self, array: typing.List[float], index: int) -> None:
        """
        Copies the elements of the vector to a specified array starting at a specified index position.
        
        :param array: The destination array.
        :param index: The index at which to copy the first element of the vector.
        """
        ...

    @overload
    def copy_to(self, destination: System.Span[float]) -> None:
        """
        Copies the vector to the given Span{T}. The length of the destination span must be at least 4.
        
        :param destination: The destination span which the values are copied into.
        """
        ...

    @staticmethod
    def cos(vector: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def count(vector: System.Numerics.Vector4, value: float) -> int:
        ...

    @staticmethod
    def count_where_all_bits_set(vector: System.Numerics.Vector4) -> int:
        ...

    @staticmethod
    @overload
    def create(value: float) -> System.Numerics.Vector4:
        """
        Creates a new Vector4 object whose four elements have the same value.
        
        :param value: The value to assign to all four elements.
        :returns: A new Vector4 whose four elements have the same value.
        """
        ...

    @staticmethod
    @overload
    def create(vector: System.Numerics.Vector2, z: float, w: float) -> System.Numerics.Vector4:
        """
        Creates a new Vector4 object from the specified Vector2 object and a Z and a W component.
        
        :param vector: The vector to use for the X and Y components.
        :param z: The Z component.
        :param w: The W component.
        :returns: A new Vector4 from the specified Vector2 object and a Z and a W component.
        """
        ...

    @staticmethod
    @overload
    def create(vector: System.Numerics.Vector3, w: float) -> System.Numerics.Vector4:
        """
        Constructs a new Vector4 object from the specified Vector3 object and a W component.
        
        :param vector: The vector to use for the X, Y, and Z components.
        :param w: The W component.
        :returns: A new Vector4 from the specified Vector3 object and a W component.
        """
        ...

    @staticmethod
    @overload
    def create(x: float, y: float, z: float, w: float) -> System.Numerics.Vector4:
        """
        Creates a vector whose elements have the specified values.
        
        :param x: The value to assign to the X field.
        :param y: The value to assign to the Y field.
        :param z: The value to assign to the Z field.
        :param w: The value to assign to the W field.
        :returns: A new Vector4 whose elements have the specified values.
        """
        ...

    @staticmethod
    @overload
    def create(values: System.ReadOnlySpan[float]) -> System.Numerics.Vector4:
        """
        Constructs a vector from the given ReadOnlySpan{Single}. The span must contain at least 4 elements.
        
        :param values: The span of elements to assign to the vector.
        :returns: A new Vector4 whose elements have the specified values.
        """
        ...

    @staticmethod
    def cross(vector_1: System.Numerics.Vector4, vector_2: System.Numerics.Vector4) -> System.Numerics.Vector4:
        """
        Computes the cross product of two vectors. For homogeneous coordinates,
        the product of the weights is the new weight for the resulting product.
        
        :param vector_1: The first vector.
        :param vector_2: The second vector.
        :returns: The cross product.
        """
        ...

    @staticmethod
    def degrees_to_radians(degrees: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def distance(value_1: System.Numerics.Vector4, value_2: System.Numerics.Vector4) -> float:
        """
        Computes the Euclidean distance between the two given points.
        
        :param value_1: The first point.
        :param value_2: The second point.
        :returns: The distance.
        """
        ...

    @staticmethod
    def distance_squared(value_1: System.Numerics.Vector4, value_2: System.Numerics.Vector4) -> float:
        """
        Returns the Euclidean distance squared between two specified points.
        
        :param value_1: The first point.
        :param value_2: The second point.
        :returns: The distance squared.
        """
        ...

    @staticmethod
    @overload
    def divide(left: System.Numerics.Vector4, right: System.Numerics.Vector4) -> System.Numerics.Vector4:
        """
        Divides the first vector by the second.
        
        :param left: The first vector.
        :param right: The second vector.
        :returns: The vector resulting from the division.
        """
        ...

    @staticmethod
    @overload
    def divide(left: System.Numerics.Vector4, divisor: float) -> System.Numerics.Vector4:
        """
        Divides the specified vector by a specified scalar value.
        
        :param left: The vector.
        :param divisor: The scalar value.
        :returns: The vector that results from the division.
        """
        ...

    @staticmethod
    def dot(vector_1: System.Numerics.Vector4, vector_2: System.Numerics.Vector4) -> float:
        """
        Returns the dot product of two vectors.
        
        :param vector_1: The first vector.
        :param vector_2: The second vector.
        :returns: The dot product.
        """
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        """
        Returns a value that indicates whether this instance and a specified object are equal.
        
        :param obj: The object to compare with the current instance.
        :returns: true if the current instance and  are equal; otherwise, false. If  is null, the method returns false.
        """
        ...

    @staticmethod
    @overload
    def equals(left: System.Numerics.Vector4, right: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @overload
    def equals(self, other: System.Numerics.Vector4) -> bool:
        """
        Returns a value that indicates whether this instance and another vector are equal.
        
        :param other: The other vector.
        :returns: true if the two vectors are equal; otherwise, false.
        """
        ...

    @staticmethod
    def equals_all(left: System.Numerics.Vector4, right: System.Numerics.Vector4) -> bool:
        ...

    @staticmethod
    def equals_any(left: System.Numerics.Vector4, right: System.Numerics.Vector4) -> bool:
        ...

    @staticmethod
    def exp(vector: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def fused_multiply_add(left: System.Numerics.Vector4, right: System.Numerics.Vector4, addend: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    def get_hash_code(self) -> int:
        """
        Returns the hash code for this instance.
        
        :returns: The hash code.
        """
        ...

    @staticmethod
    def greater_than(left: System.Numerics.Vector4, right: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def greater_than_all(left: System.Numerics.Vector4, right: System.Numerics.Vector4) -> bool:
        ...

    @staticmethod
    def greater_than_any(left: System.Numerics.Vector4, right: System.Numerics.Vector4) -> bool:
        ...

    @staticmethod
    def greater_than_or_equal(left: System.Numerics.Vector4, right: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def greater_than_or_equal_all(left: System.Numerics.Vector4, right: System.Numerics.Vector4) -> bool:
        ...

    @staticmethod
    def greater_than_or_equal_any(left: System.Numerics.Vector4, right: System.Numerics.Vector4) -> bool:
        ...

    @staticmethod
    def hypot(x: System.Numerics.Vector4, y: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def index_of(vector: System.Numerics.Vector4, value: float) -> int:
        ...

    @staticmethod
    def index_of_where_all_bits_set(vector: System.Numerics.Vector4) -> int:
        ...

    @staticmethod
    def is_even_integer(vector: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def is_finite(vector: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def is_infinity(vector: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def is_integer(vector: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def is_na_n(vector: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def is_negative(vector: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def is_negative_infinity(vector: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def is_normal(vector: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def is_odd_integer(vector: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def is_positive(vector: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def is_positive_infinity(vector: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def is_subnormal(vector: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def is_zero(vector: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def last_index_of(vector: System.Numerics.Vector4, value: float) -> int:
        ...

    @staticmethod
    def last_index_of_where_all_bits_set(vector: System.Numerics.Vector4) -> int:
        ...

    def length(self) -> float:
        """
        Returns the length of this vector object.
        
        :returns: The vector's length.
        """
        ...

    def length_squared(self) -> float:
        """
        Returns the length of the vector squared.
        
        :returns: The vector's length squared.
        """
        ...

    @staticmethod
    @overload
    def lerp(value_1: System.Numerics.Vector4, value_2: System.Numerics.Vector4, amount: float) -> System.Numerics.Vector4:
        ...

    @staticmethod
    @overload
    def lerp(value_1: System.Numerics.Vector4, value_2: System.Numerics.Vector4, amount: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def less_than(left: System.Numerics.Vector4, right: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def less_than_all(left: System.Numerics.Vector4, right: System.Numerics.Vector4) -> bool:
        ...

    @staticmethod
    def less_than_any(left: System.Numerics.Vector4, right: System.Numerics.Vector4) -> bool:
        ...

    @staticmethod
    def less_than_or_equal(left: System.Numerics.Vector4, right: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def less_than_or_equal_all(left: System.Numerics.Vector4, right: System.Numerics.Vector4) -> bool:
        ...

    @staticmethod
    def less_than_or_equal_any(left: System.Numerics.Vector4, right: System.Numerics.Vector4) -> bool:
        ...

    @staticmethod
    def load(source: typing.Any) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def load_aligned(source: typing.Any) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def load_aligned_non_temporal(source: typing.Any) -> System.Numerics.Vector4:
        ...

    @staticmethod
    @overload
    def load_unsafe(source: float) -> System.Numerics.Vector4:
        ...

    @staticmethod
    @overload
    def load_unsafe(source: float, element_offset: System.UIntPtr) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def log(vector: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def log_2(vector: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def max(value_1: System.Numerics.Vector4, value_2: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def max_magnitude(value_1: System.Numerics.Vector4, value_2: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def max_magnitude_number(value_1: System.Numerics.Vector4, value_2: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def max_native(value_1: System.Numerics.Vector4, value_2: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def max_number(value_1: System.Numerics.Vector4, value_2: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def min(value_1: System.Numerics.Vector4, value_2: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def min_magnitude(value_1: System.Numerics.Vector4, value_2: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def min_magnitude_number(value_1: System.Numerics.Vector4, value_2: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def min_native(value_1: System.Numerics.Vector4, value_2: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def min_number(value_1: System.Numerics.Vector4, value_2: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    @overload
    def multiply(left: System.Numerics.Vector4, right: System.Numerics.Vector4) -> System.Numerics.Vector4:
        """
        Returns a new vector whose values are the product of each pair of elements in two specified vectors.
        
        :param left: The first vector.
        :param right: The second vector.
        :returns: The element-wise product vector.
        """
        ...

    @staticmethod
    @overload
    def multiply(left: System.Numerics.Vector4, right: float) -> System.Numerics.Vector4:
        """
        Multiplies a vector by a specified scalar.
        
        :param left: The vector to multiply.
        :param right: The scalar value.
        :returns: The scaled vector.
        """
        ...

    @staticmethod
    @overload
    def multiply(left: float, right: System.Numerics.Vector4) -> System.Numerics.Vector4:
        """
        Multiplies a scalar value by a specified vector.
        
        :param left: The scaled value.
        :param right: The vector.
        :returns: The scaled vector.
        """
        ...

    @staticmethod
    def multiply_add_estimate(left: System.Numerics.Vector4, right: System.Numerics.Vector4, addend: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def negate(value: System.Numerics.Vector4) -> System.Numerics.Vector4:
        """
        Negates a specified vector.
        
        :param value: The vector to negate.
        :returns: The negated vector.
        """
        ...

    @staticmethod
    def none(vector: System.Numerics.Vector4, value: float) -> bool:
        ...

    @staticmethod
    def none_where_all_bits_set(vector: System.Numerics.Vector4) -> bool:
        ...

    @staticmethod
    def normalize(vector: System.Numerics.Vector4) -> System.Numerics.Vector4:
        """
        Returns a vector with the same direction as the specified vector, but with a length of one.
        
        :param vector: The vector to normalize.
        :returns: The normalized vector.
        """
        ...

    @staticmethod
    def ones_complement(value: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def radians_to_degrees(radians: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    @overload
    def round(vector: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    @overload
    def round(vector: System.Numerics.Vector4, mode: System.MidpointRounding) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def shuffle(vector: System.Numerics.Vector4, x_index: int, y_index: int, z_index: int, w_index: int) -> System.Numerics.Vector4:
        """
        Creates a new vector by selecting values from an input vector using a set of indices.
        
        :param vector: The input vector from which values are selected.
        :param x_index: The index used to select a value from  to be used as the value of X in the result.
        :param y_index: The index used to select a value from  to be used as the value of Y in the result
        :param z_index: The index used to select a value from  to be used as the value of Z in the result
        :param w_index: The index used to select a value from  to be used as the value of W in the result
        :returns: A new vector containing the values from  selected by the given indices.
        """
        ...

    @staticmethod
    def sin(vector: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    @staticmethod
    def sin_cos(vector: System.Numerics.Vector4) -> System.ValueTuple[System.Numerics.Vector4, System.Numerics.Vector4]:
        ...

    @staticmethod
    def square_root(value: System.Numerics.Vector4) -> System.Numerics.Vector4:
        """
        Returns a vector whose elements are the square root of each of a specified vector's elements.
        
        :param value: A vector.
        :returns: The square root vector.
        """
        ...

    @staticmethod
    def subtract(left: System.Numerics.Vector4, right: System.Numerics.Vector4) -> System.Numerics.Vector4:
        """
        Subtracts the second vector from the first.
        
        :param left: The first vector.
        :param right: The second vector.
        :returns: The difference vector.
        """
        ...

    @staticmethod
    def sum(value: System.Numerics.Vector4) -> float:
        ...

    @overload
    def to_string(self) -> str:
        """
        Returns the string representation of the current instance using default formatting.
        
        :returns: The string representation of the current instance.
        """
        ...

    @overload
    def to_string(self, format: str) -> str:
        """
        Returns the string representation of the current instance using the specified format string to format individual elements.
        
        :param format: A standard or custom numeric format string that defines the format of individual elements.
        :returns: The string representation of the current instance.
        """
        ...

    @overload
    def to_string(self, format: str, format_provider: System.IFormatProvider) -> str:
        """
        Returns the string representation of the current instance using the specified format string to format individual elements and the specified format provider to define culture-specific formatting.
        
        :param format: A standard or custom numeric format string that defines the format of individual elements.
        :param format_provider: A format provider that supplies culture-specific formatting information.
        :returns: The string representation of the current instance.
        """
        ...

    @staticmethod
    @overload
    def transform(position: System.Numerics.Vector2, matrix: System.Numerics.Matrix4x4) -> System.Numerics.Vector4:
        """
        Transforms a two-dimensional vector by a specified 4x4 matrix.
        
        :param position: The vector to transform.
        :param matrix: The transformation matrix.
        :returns: The transformed vector.
        """
        ...

    @staticmethod
    @overload
    def transform(value: System.Numerics.Vector2, rotation: System.Numerics.Quaternion) -> System.Numerics.Vector4:
        """
        Transforms a two-dimensional vector by the specified Quaternion rotation value.
        
        :param value: The vector to rotate.
        :param rotation: The rotation to apply.
        :returns: The transformed vector.
        """
        ...

    @staticmethod
    @overload
    def transform(position: System.Numerics.Vector3, matrix: System.Numerics.Matrix4x4) -> System.Numerics.Vector4:
        """
        Transforms a three-dimensional vector by a specified 4x4 matrix.
        
        :param position: The vector to transform.
        :param matrix: The transformation matrix.
        :returns: The transformed vector.
        """
        ...

    @staticmethod
    @overload
    def transform(value: System.Numerics.Vector3, rotation: System.Numerics.Quaternion) -> System.Numerics.Vector4:
        """
        Transforms a three-dimensional vector by the specified Quaternion rotation value.
        
        :param value: The vector to rotate.
        :param rotation: The rotation to apply.
        :returns: The transformed vector.
        """
        ...

    @staticmethod
    @overload
    def transform(vector: System.Numerics.Vector4, matrix: System.Numerics.Matrix4x4) -> System.Numerics.Vector4:
        """
        Transforms a four-dimensional vector by a specified 4x4 matrix.
        
        :param vector: The vector to transform.
        :param matrix: The transformation matrix.
        :returns: The transformed vector.
        """
        ...

    @staticmethod
    @overload
    def transform(value: System.Numerics.Vector4, rotation: System.Numerics.Quaternion) -> System.Numerics.Vector4:
        """
        Transforms a four-dimensional vector by the specified Quaternion rotation value.
        
        :param value: The vector to rotate.
        :param rotation: The rotation to apply.
        :returns: The transformed vector.
        """
        ...

    @staticmethod
    def truncate(vector: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...

    def try_copy_to(self, destination: System.Span[float]) -> bool:
        """
        Attempts to copy the vector to the given Span{Single}. The length of the destination span must be at least 4.
        
        :param destination: The destination span which the values are copied into.
        :returns: true if the source vector was successfully copied to . false if  is not large enough to hold the source vector.
        """
        ...

    @staticmethod
    def xor(left: System.Numerics.Vector4, right: System.Numerics.Vector4) -> System.Numerics.Vector4:
        ...


class Plane(System.IEquatable[System_Numerics_Plane]):
    """Represents a plane in three-dimensional space."""

    @property
    def normal(self) -> System.Numerics.Vector3:
        """The normal vector of the plane."""
        ...

    @normal.setter
    def normal(self, value: System.Numerics.Vector3) -> None:
        ...

    @property
    def d(self) -> float:
        """The distance of the plane along its normal from the origin."""
        ...

    @d.setter
    def d(self, value: float) -> None:
        ...

    def __eq__(self, value_2: System.Numerics.Plane) -> bool:
        """
        Returns a value that indicates whether two planes are equal.
        
        :param value1: The first plane to compare.
        :param value_2: The second plane to compare.
        :returns: true if  and  are equal; otherwise, false.
        """
        ...

    @overload
    def __init__(self, x: float, y: float, z: float, d: float) -> None:
        """
        Creates a Plane object from the X, Y, and Z components of its normal, and its distance from the origin on that normal.
        
        :param x: The X component of the normal.
        :param y: The Y component of the normal.
        :param z: The Z component of the normal.
        :param d: The distance of the plane along its normal from the origin.
        """
        ...

    @overload
    def __init__(self, normal: System.Numerics.Vector3, d: float) -> None:
        """
        Creates a Plane object from a specified normal and the distance along the normal from the origin.
        
        :param normal: The plane's normal vector.
        :param d: The plane's distance from the origin along its normal vector.
        """
        ...

    @overload
    def __init__(self, value: System.Numerics.Vector4) -> None:
        """
        Creates a Plane object from a specified four-dimensional vector.
        
        :param value: A vector whose first three elements describe the normal vector, and whose Vector4.W defines the distance along that normal from the origin.
        """
        ...

    def __ne__(self, value_2: System.Numerics.Plane) -> bool:
        """
        Returns a value that indicates whether two planes are not equal.
        
        :param value1: The first plane to compare.
        :param value_2: The second plane to compare.
        :returns: true if  and  are not equal; otherwise, false.
        """
        ...

    @staticmethod
    def create_from_vertices(point_1: System.Numerics.Vector3, point_2: System.Numerics.Vector3, point_3: System.Numerics.Vector3) -> System.Numerics.Plane:
        """
        Creates a Plane object that contains three specified points.
        
        :param point_1: The first point defining the plane.
        :param point_2: The second point defining the plane.
        :param point_3: The third point defining the plane.
        :returns: The plane containing the three points.
        """
        ...

    @staticmethod
    def dot(plane: System.Numerics.Plane, value: System.Numerics.Vector4) -> float:
        """
        Calculates the dot product of a plane and a 4-dimensional vector.
        
        :param plane: The plane.
        :param value: The four-dimensional vector.
        :returns: The dot product.
        """
        ...

    @staticmethod
    def dot_coordinate(plane: System.Numerics.Plane, value: System.Numerics.Vector3) -> float:
        """
        Returns the dot product of a specified three-dimensional vector and the normal vector of this plane plus the distance (D) value of the plane.
        
        :param plane: The plane.
        :param value: The 3-dimensional vector.
        :returns: The dot product.
        """
        ...

    @staticmethod
    def dot_normal(plane: System.Numerics.Plane, value: System.Numerics.Vector3) -> float:
        """
        Returns the dot product of a specified three-dimensional vector and the Normal vector of this plane.
        
        :param plane: The plane.
        :param value: The three-dimensional vector.
        :returns: The dot product.
        """
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        """
        Returns a value that indicates whether this instance and a specified object are equal.
        
        :param obj: The object to compare with the current instance.
        :returns: true if the current instance and  are equal; otherwise, false. If  is null, the method returns false.
        """
        ...

    @overload
    def equals(self, other: System.Numerics.Plane) -> bool:
        """
        Returns a value that indicates whether this instance and another plane object are equal.
        
        :param other: The other plane.
        :returns: true if the two planes are equal; otherwise, false.
        """
        ...

    def get_hash_code(self) -> int:
        """
        Returns the hash code for this instance.
        
        :returns: The hash code.
        """
        ...

    @staticmethod
    def normalize(value: System.Numerics.Plane) -> System.Numerics.Plane:
        """
        Creates a new Plane object whose normal vector is the source plane's normal vector normalized.
        
        :param value: The source plane.
        :returns: The normalized plane.
        """
        ...

    def to_string(self) -> str:
        """
        Returns the string representation of this plane object.
        
        :returns: A string that represents this Plane object.
        """
        ...

    @staticmethod
    @overload
    def transform(plane: System.Numerics.Plane, matrix: System.Numerics.Matrix4x4) -> System.Numerics.Plane:
        """
        Transforms a normalized plane by a 4x4 matrix.
        
        :param plane: The normalized plane to transform.
        :param matrix: The transformation matrix to apply to .
        :returns: The transformed plane.
        """
        ...

    @staticmethod
    @overload
    def transform(plane: System.Numerics.Plane, rotation: System.Numerics.Quaternion) -> System.Numerics.Plane:
        """
        Transforms a normalized plane by a Quaternion rotation.
        
        :param plane: The normalized plane to transform.
        :param rotation: The Quaternion rotation to apply to the plane.
        :returns: A new plane that results from applying the Quaternion rotation.
        """
        ...


class Matrix4x4(System.IEquatable[System_Numerics_Matrix4x4]):
    """Represents a 4x4 matrix."""

    @property
    def m_11(self) -> float:
        """The first element of the first row."""
        ...

    @m_11.setter
    def m_11(self, value: float) -> None:
        ...

    @property
    def m_12(self) -> float:
        """The second element of the first row."""
        ...

    @m_12.setter
    def m_12(self, value: float) -> None:
        ...

    @property
    def m_13(self) -> float:
        """The third element of the first row."""
        ...

    @m_13.setter
    def m_13(self, value: float) -> None:
        ...

    @property
    def m_14(self) -> float:
        """The fourth element of the first row."""
        ...

    @m_14.setter
    def m_14(self, value: float) -> None:
        ...

    @property
    def m_21(self) -> float:
        """The first element of the second row."""
        ...

    @m_21.setter
    def m_21(self, value: float) -> None:
        ...

    @property
    def m_22(self) -> float:
        """The second element of the second row."""
        ...

    @m_22.setter
    def m_22(self, value: float) -> None:
        ...

    @property
    def m_23(self) -> float:
        """The third element of the second row."""
        ...

    @m_23.setter
    def m_23(self, value: float) -> None:
        ...

    @property
    def m_24(self) -> float:
        """The fourth element of the second row."""
        ...

    @m_24.setter
    def m_24(self, value: float) -> None:
        ...

    @property
    def m_31(self) -> float:
        """The first element of the third row."""
        ...

    @m_31.setter
    def m_31(self, value: float) -> None:
        ...

    @property
    def m_32(self) -> float:
        """The second element of the third row."""
        ...

    @m_32.setter
    def m_32(self, value: float) -> None:
        ...

    @property
    def m_33(self) -> float:
        """The third element of the third row."""
        ...

    @m_33.setter
    def m_33(self, value: float) -> None:
        ...

    @property
    def m_34(self) -> float:
        """The fourth element of the third row."""
        ...

    @m_34.setter
    def m_34(self, value: float) -> None:
        ...

    @property
    def m_41(self) -> float:
        """The first element of the fourth row."""
        ...

    @m_41.setter
    def m_41(self, value: float) -> None:
        ...

    @property
    def m_42(self) -> float:
        """The second element of the fourth row."""
        ...

    @m_42.setter
    def m_42(self, value: float) -> None:
        ...

    @property
    def m_43(self) -> float:
        """The third element of the fourth row."""
        ...

    @m_43.setter
    def m_43(self, value: float) -> None:
        ...

    @property
    def m_44(self) -> float:
        """The fourth element of the fourth row."""
        ...

    @m_44.setter
    def m_44(self, value: float) -> None:
        ...

    IDENTITY: System.Numerics.Matrix4x4
    """Gets the multiplicative identity matrix."""

    @property
    def is_identity(self) -> bool:
        """Indicates whether the current matrix is the identity matrix."""
        ...

    @property
    def translation(self) -> System.Numerics.Vector3:
        """Gets or sets the translation component of this matrix."""
        ...

    @translation.setter
    def translation(self, value: System.Numerics.Vector3) -> None:
        ...

    def __add__(self, value_2: System.Numerics.Matrix4x4) -> System.Numerics.Matrix4x4:
        """
        Adds each element in one matrix with its corresponding element in a second matrix.
        
        :param value1: The first matrix.
        :param value_2: The second matrix.
        :returns: The matrix that contains the summed values.
        """
        ...

    def __eq__(self, value_2: System.Numerics.Matrix4x4) -> bool:
        """
        Returns a value that indicates whether the specified matrices are equal.
        
        :param value1: The first matrix to compare.
        :param value_2: The second matrix to care
        :returns: true if  and  are equal; otherwise, false.
        """
        ...

    def __getitem__(self, row: int, column: int) -> float:
        """
        Gets or sets the element at the specified indices.
        
        :param row: The index of the row containing the element to get or set.
        :param column: The index of the column containing the element to get or set.
        :returns: The element at [][].
        """
        ...

    def __iadd__(self, value_2: System.Numerics.Matrix4x4) -> System.Numerics.Matrix4x4:
        """
        Adds each element in one matrix with its corresponding element in a second matrix.
        
        :param value1: The first matrix.
        :param value_2: The second matrix.
        :returns: The matrix that contains the summed values.
        """
        ...

    @overload
    def __imul__(self, value_2: System.Numerics.Matrix4x4) -> System.Numerics.Matrix4x4:
        """
        Multiplies two matrices together to compute the product.
        
        :param value1: The first matrix.
        :param value_2: The second matrix.
        :returns: The product matrix.
        """
        ...

    @overload
    def __imul__(self, value_2: float) -> System.Numerics.Matrix4x4:
        """
        Multiplies a matrix by a float to compute the product.
        
        :param value1: The matrix to scale.
        :param value_2: The scaling value to use.
        :returns: The scaled matrix.
        """
        ...

    @overload
    def __init__(self, m_11: float, m_12: float, m_13: float, m_14: float, m_21: float, m_22: float, m_23: float, m_24: float, m_31: float, m_32: float, m_33: float, m_34: float, m_41: float, m_42: float, m_43: float, m_44: float) -> None:
        """
        Creates a 4x4 matrix from the specified components.
        
        :param m_11: The value to assign to the first element in the first row.
        :param m_12: The value to assign to the second element in the first row.
        :param m_13: The value to assign to the third element in the first row.
        :param m_14: The value to assign to the fourth element in the first row.
        :param m_21: The value to assign to the first element in the second row.
        :param m_22: The value to assign to the second element in the second row.
        :param m_23: The value to assign to the third element in the second row.
        :param m_24: The value to assign to the third element in the second row.
        :param m_31: The value to assign to the first element in the third row.
        :param m_32: The value to assign to the second element in the third row.
        :param m_33: The value to assign to the third element in the third row.
        :param m_34: The value to assign to the fourth element in the third row.
        :param m_41: The value to assign to the first element in the fourth row.
        :param m_42: The value to assign to the second element in the fourth row.
        :param m_43: The value to assign to the third element in the fourth row.
        :param m_44: The value to assign to the fourth element in the fourth row.
        """
        ...

    @overload
    def __init__(self, value: System.Numerics.Matrix3x2) -> None:
        """
        Creates a Matrix4x4 object from a specified Matrix3x2 object.
        
        :param value: A 3x2 matrix.
        """
        ...

    @overload
    def __isub__(self, value_2: System.Numerics.Matrix4x4) -> System.Numerics.Matrix4x4:
        """
        Subtracts each element in a second matrix from its corresponding element in a first matrix.
        
        :param value1: The first matrix.
        :param value_2: The second matrix.
        :returns: The matrix containing the values that result from subtracting each element in  from its corresponding element in .
        """
        ...

    @overload
    def __isub__(self) -> System.Numerics.Matrix4x4:
        """
        Negates the specified matrix by multiplying all its values by -1.
        
        :param value: The matrix to negate.
        :returns: The negated matrix.
        """
        ...

    @overload
    def __mul__(self, value_2: System.Numerics.Matrix4x4) -> System.Numerics.Matrix4x4:
        """
        Multiplies two matrices together to compute the product.
        
        :param value1: The first matrix.
        :param value_2: The second matrix.
        :returns: The product matrix.
        """
        ...

    @overload
    def __mul__(self, value_2: float) -> System.Numerics.Matrix4x4:
        """
        Multiplies a matrix by a float to compute the product.
        
        :param value1: The matrix to scale.
        :param value_2: The scaling value to use.
        :returns: The scaled matrix.
        """
        ...

    def __ne__(self, value_2: System.Numerics.Matrix4x4) -> bool:
        """
        Returns a value that indicates whether the specified matrices are not equal.
        
        :param value1: The first matrix to compare.
        :param value_2: The second matrix to compare.
        :returns: true if  and  are not equal; otherwise, false.
        """
        ...

    def __setitem__(self, row: int, column: int, value: float) -> None:
        """
        Gets or sets the element at the specified indices.
        
        :param row: The index of the row containing the element to get or set.
        :param column: The index of the column containing the element to get or set.
        :returns: The element at [][].
        """
        ...

    @overload
    def __sub__(self, value_2: System.Numerics.Matrix4x4) -> System.Numerics.Matrix4x4:
        """
        Subtracts each element in a second matrix from its corresponding element in a first matrix.
        
        :param value1: The first matrix.
        :param value_2: The second matrix.
        :returns: The matrix containing the values that result from subtracting each element in  from its corresponding element in .
        """
        ...

    @overload
    def __sub__(self) -> System.Numerics.Matrix4x4:
        """
        Negates the specified matrix by multiplying all its values by -1.
        
        :param value: The matrix to negate.
        :returns: The negated matrix.
        """
        ...

    @staticmethod
    def add(value_1: System.Numerics.Matrix4x4, value_2: System.Numerics.Matrix4x4) -> System.Numerics.Matrix4x4:
        """
        Adds each element in one matrix with its corresponding element in a second matrix.
        
        :param value_1: The first matrix.
        :param value_2: The second matrix.
        :returns: The matrix that contains the summed values of  and .
        """
        ...

    @staticmethod
    def create_billboard(object_position: System.Numerics.Vector3, camera_position: System.Numerics.Vector3, camera_up_vector: System.Numerics.Vector3, camera_forward_vector: System.Numerics.Vector3) -> System.Numerics.Matrix4x4:
        """
        Creates a right-handed spherical billboard matrix that rotates around a specified object position.
        
        :param object_position: The position of the object that the billboard will rotate around.
        :param camera_position: The position of the camera.
        :param camera_up_vector: The up vector of the camera.
        :param camera_forward_vector: The forward vector of the camera.
        :returns: The created billboard.
        """
        ...

    @staticmethod
    def create_billboard_left_handed(object_position: System.Numerics.Vector3, camera_position: System.Numerics.Vector3, camera_up_vector: System.Numerics.Vector3, camera_forward_vector: System.Numerics.Vector3) -> System.Numerics.Matrix4x4:
        """
        Creates a left-handed spherical billboard matrix that rotates around a specified object position.
        
        :param object_position: The position of the object that the billboard will rotate around.
        :param camera_position: The position of the camera.
        :param camera_up_vector: The up vector of the camera.
        :param camera_forward_vector: The forward vector of the camera.
        :returns: The created billboard.
        """
        ...

    @staticmethod
    def create_constrained_billboard(object_position: System.Numerics.Vector3, camera_position: System.Numerics.Vector3, rotate_axis: System.Numerics.Vector3, camera_forward_vector: System.Numerics.Vector3, object_forward_vector: System.Numerics.Vector3) -> System.Numerics.Matrix4x4:
        """
        Creates a right-handed cylindrical billboard matrix that rotates around a specified axis.
        
        :param object_position: The position of the object that the billboard will rotate around.
        :param camera_position: The position of the camera.
        :param rotate_axis: The axis to rotate the billboard around.
        :param camera_forward_vector: The forward vector of the camera.
        :param object_forward_vector: The forward vector of the object.
        :returns: The billboard matrix.
        """
        ...

    @staticmethod
    def create_constrained_billboard_left_handed(object_position: System.Numerics.Vector3, camera_position: System.Numerics.Vector3, rotate_axis: System.Numerics.Vector3, camera_forward_vector: System.Numerics.Vector3, object_forward_vector: System.Numerics.Vector3) -> System.Numerics.Matrix4x4:
        """
        Creates a left-handed cylindrical billboard matrix that rotates around a specified axis.
        
        :param object_position: The position of the object that the billboard will rotate around.
        :param camera_position: The position of the camera.
        :param rotate_axis: The axis to rotate the billboard around.
        :param camera_forward_vector: The forward vector of the camera.
        :param object_forward_vector: The forward vector of the object.
        :returns: The billboard matrix.
        """
        ...

    @staticmethod
    def create_from_axis_angle(axis: System.Numerics.Vector3, angle: float) -> System.Numerics.Matrix4x4:
        """
        Creates a matrix that rotates around an arbitrary vector.
        
        :param axis: The axis to rotate around.
        :param angle: The angle to rotate around , in radians.
        :returns: The rotation matrix.
        """
        ...

    @staticmethod
    def create_from_quaternion(quaternion: System.Numerics.Quaternion) -> System.Numerics.Matrix4x4:
        """
        Creates a rotation matrix from the specified Quaternion rotation value.
        
        :param quaternion: The source Quaternion.
        :returns: The rotation matrix.
        """
        ...

    @staticmethod
    def create_from_yaw_pitch_roll(yaw: float, pitch: float, roll: float) -> System.Numerics.Matrix4x4:
        """
        Creates a rotation matrix from the specified yaw, pitch, and roll.
        
        :param yaw: The angle of rotation, in radians, around the Y axis.
        :param pitch: The angle of rotation, in radians, around the X axis.
        :param roll: The angle of rotation, in radians, around the Z axis.
        :returns: The rotation matrix.
        """
        ...

    @staticmethod
    def create_look_at(camera_position: System.Numerics.Vector3, camera_target: System.Numerics.Vector3, camera_up_vector: System.Numerics.Vector3) -> System.Numerics.Matrix4x4:
        """
        Creates a right-handed view matrix.
        
        :param camera_position: The position of the camera.
        :param camera_target: The target towards which the camera is pointing.
        :param camera_up_vector: The direction that is "up" from the camera's point of view.
        :returns: The right-handed view matrix.
        """
        ...

    @staticmethod
    def create_look_at_left_handed(camera_position: System.Numerics.Vector3, camera_target: System.Numerics.Vector3, camera_up_vector: System.Numerics.Vector3) -> System.Numerics.Matrix4x4:
        """
        Creates a left-handed view matrix.
        
        :param camera_position: The position of the camera.
        :param camera_target: The target towards which the camera is pointing.
        :param camera_up_vector: The direction that is "up" from the camera's point of view.
        :returns: The left-handed view matrix.
        """
        ...

    @staticmethod
    def create_look_to(camera_position: System.Numerics.Vector3, camera_direction: System.Numerics.Vector3, camera_up_vector: System.Numerics.Vector3) -> System.Numerics.Matrix4x4:
        """
        Creates a right-handed view matrix.
        
        :param camera_position: The position of the camera.
        :param camera_direction: The direction in which the camera is pointing.
        :param camera_up_vector: The direction that is "up" from the camera's point of view.
        :returns: The right-handed view matrix.
        """
        ...

    @staticmethod
    def create_look_to_left_handed(camera_position: System.Numerics.Vector3, camera_direction: System.Numerics.Vector3, camera_up_vector: System.Numerics.Vector3) -> System.Numerics.Matrix4x4:
        """
        Creates a left-handed view matrix.
        
        :param camera_position: The position of the camera.
        :param camera_direction: The direction in which the camera is pointing.
        :param camera_up_vector: The direction that is "up" from the camera's point of view.
        :returns: The left-handed view matrix.
        """
        ...

    @staticmethod
    def create_orthographic(width: float, height: float, z_near_plane: float, z_far_plane: float) -> System.Numerics.Matrix4x4:
        """
        Creates a right-handed orthographic perspective matrix from the given view volume dimensions.
        
        :param width: The width of the view volume.
        :param height: The height of the view volume.
        :param z_near_plane: The minimum Z-value of the view volume.
        :param z_far_plane: The maximum Z-value of the view volume.
        :returns: The right-handed orthographic projection matrix.
        """
        ...

    @staticmethod
    def create_orthographic_left_handed(width: float, height: float, z_near_plane: float, z_far_plane: float) -> System.Numerics.Matrix4x4:
        """
        Creates a left-handed orthographic perspective matrix from the given view volume dimensions.
        
        :param width: The width of the view volume.
        :param height: The height of the view volume.
        :param z_near_plane: The minimum Z-value of the view volume.
        :param z_far_plane: The maximum Z-value of the view volume.
        :returns: The left-handed orthographic projection matrix.
        """
        ...

    @staticmethod
    def create_orthographic_off_center(left: float, right: float, bottom: float, top: float, z_near_plane: float, z_far_plane: float) -> System.Numerics.Matrix4x4:
        """
        Creates a right-handed customized orthographic projection matrix.
        
        :param left: The minimum X-value of the view volume.
        :param right: The maximum X-value of the view volume.
        :param bottom: The minimum Y-value of the view volume.
        :param top: The maximum Y-value of the view volume.
        :param z_near_plane: The minimum Z-value of the view volume.
        :param z_far_plane: The maximum Z-value of the view volume.
        :returns: The right-handed orthographic projection matrix.
        """
        ...

    @staticmethod
    def create_orthographic_off_center_left_handed(left: float, right: float, bottom: float, top: float, z_near_plane: float, z_far_plane: float) -> System.Numerics.Matrix4x4:
        """
        Creates a left-handed customized orthographic projection matrix.
        
        :param left: The minimum X-value of the view volume.
        :param right: The maximum X-value of the view volume.
        :param bottom: The minimum Y-value of the view volume.
        :param top: The maximum Y-value of the view volume.
        :param z_near_plane: The minimum Z-value of the view volume.
        :param z_far_plane: The maximum Z-value of the view volume.
        :returns: The left-handed orthographic projection matrix.
        """
        ...

    @staticmethod
    def create_perspective(width: float, height: float, near_plane_distance: float, far_plane_distance: float) -> System.Numerics.Matrix4x4:
        """
        Creates a right-handed perspective projection matrix from the given view volume dimensions.
        
        :param width: The width of the view volume at the near view plane.
        :param height: The height of the view volume at the near view plane.
        :param near_plane_distance: The distance to the near view plane.
        :param far_plane_distance: The distance to the far view plane.
        :returns: The right-handed perspective projection matrix.
        """
        ...

    @staticmethod
    def create_perspective_field_of_view(field_of_view: float, aspect_ratio: float, near_plane_distance: float, far_plane_distance: float) -> System.Numerics.Matrix4x4:
        """
        Creates a right-handed perspective projection matrix based on a field of view, aspect ratio, and near and far view plane distances.
        
        :param field_of_view: The field of view in the y direction, in radians.
        :param aspect_ratio: The aspect ratio, defined as view space width divided by height.
        :param near_plane_distance: The distance to the near view plane.
        :param far_plane_distance: The distance to the far view plane.
        :returns: The right-handed perspective projection matrix.
        """
        ...

    @staticmethod
    def create_perspective_field_of_view_left_handed(field_of_view: float, aspect_ratio: float, near_plane_distance: float, far_plane_distance: float) -> System.Numerics.Matrix4x4:
        """
        Creates a left-handed perspective projection matrix based on a field of view, aspect ratio, and near and far view plane distances.
        
        :param field_of_view: The field of view in the y direction, in radians.
        :param aspect_ratio: The aspect ratio, defined as view space width divided by height.
        :param near_plane_distance: The distance to the near view plane.
        :param far_plane_distance: The distance to the far view plane.
        :returns: The left-handed perspective projection matrix.
        """
        ...

    @staticmethod
    def create_perspective_left_handed(width: float, height: float, near_plane_distance: float, far_plane_distance: float) -> System.Numerics.Matrix4x4:
        """
        Creates a left-handed perspective projection matrix from the given view volume dimensions.
        
        :param width: The width of the view volume at the near view plane.
        :param height: The height of the view volume at the near view plane.
        :param near_plane_distance: The distance to the near view plane.
        :param far_plane_distance: The distance to the far view plane.
        :returns: The left-handed perspective projection matrix.
        """
        ...

    @staticmethod
    def create_perspective_off_center(left: float, right: float, bottom: float, top: float, near_plane_distance: float, far_plane_distance: float) -> System.Numerics.Matrix4x4:
        """
        Creates a right-handed customized perspective projection matrix.
        
        :param left: The minimum x-value of the view volume at the near view plane.
        :param right: The maximum x-value of the view volume at the near view plane.
        :param bottom: The minimum y-value of the view volume at the near view plane.
        :param top: The maximum y-value of the view volume at the near view plane.
        :param near_plane_distance: The distance to the near view plane.
        :param far_plane_distance: The distance to the far view plane.
        :returns: The right-handed perspective projection matrix.
        """
        ...

    @staticmethod
    def create_perspective_off_center_left_handed(left: float, right: float, bottom: float, top: float, near_plane_distance: float, far_plane_distance: float) -> System.Numerics.Matrix4x4:
        """
        Creates a left-handed customized perspective projection matrix.
        
        :param left: The minimum x-value of the view volume at the near view plane.
        :param right: The maximum x-value of the view volume at the near view plane.
        :param bottom: The minimum y-value of the view volume at the near view plane.
        :param top: The maximum y-value of the view volume at the near view plane.
        :param near_plane_distance: The distance to the near view plane.
        :param far_plane_distance: The distance to the far view plane.
        :returns: The left-handed perspective projection matrix.
        """
        ...

    @staticmethod
    def create_reflection(value: System.Numerics.Plane) -> System.Numerics.Matrix4x4:
        """
        Creates a matrix that reflects the coordinate system about a specified plane.
        
        :param value: The plane about which to create a reflection.
        :returns: A new matrix expressing the reflection.
        """
        ...

    @staticmethod
    @overload
    def create_rotation_x(radians: float) -> System.Numerics.Matrix4x4:
        """
        Creates a matrix for rotating points around the X axis.
        
        :param radians: The amount, in radians, by which to rotate around the X axis.
        :returns: The rotation matrix.
        """
        ...

    @staticmethod
    @overload
    def create_rotation_x(radians: float, center_point: System.Numerics.Vector3) -> System.Numerics.Matrix4x4:
        """
        Creates a matrix for rotating points around the X axis from a center point.
        
        :param radians: The amount, in radians, by which to rotate around the X axis.
        :param center_point: The center point.
        :returns: The rotation matrix.
        """
        ...

    @staticmethod
    @overload
    def create_rotation_y(radians: float) -> System.Numerics.Matrix4x4:
        """
        Creates a matrix for rotating points around the Y axis.
        
        :param radians: The amount, in radians, by which to rotate around the Y-axis.
        :returns: The rotation matrix.
        """
        ...

    @staticmethod
    @overload
    def create_rotation_y(radians: float, center_point: System.Numerics.Vector3) -> System.Numerics.Matrix4x4:
        """
        The amount, in radians, by which to rotate around the Y axis from a center point.
        
        :param radians: The amount, in radians, by which to rotate around the Y-axis.
        :param center_point: The center point.
        :returns: The rotation matrix.
        """
        ...

    @staticmethod
    @overload
    def create_rotation_z(radians: float) -> System.Numerics.Matrix4x4:
        """
        Creates a matrix for rotating points around the Z axis.
        
        :param radians: The amount, in radians, by which to rotate around the Z-axis.
        :returns: The rotation matrix.
        """
        ...

    @staticmethod
    @overload
    def create_rotation_z(radians: float, center_point: System.Numerics.Vector3) -> System.Numerics.Matrix4x4:
        """
        Creates a matrix for rotating points around the Z axis from a center point.
        
        :param radians: The amount, in radians, by which to rotate around the Z-axis.
        :param center_point: The center point.
        :returns: The rotation matrix.
        """
        ...

    @staticmethod
    @overload
    def create_scale(x_scale: float, y_scale: float, z_scale: float) -> System.Numerics.Matrix4x4:
        """
        Creates a scaling matrix from the specified X, Y, and Z components.
        
        :param x_scale: The value to scale by on the X axis.
        :param y_scale: The value to scale by on the Y axis.
        :param z_scale: The value to scale by on the Z axis.
        :returns: The scaling matrix.
        """
        ...

    @staticmethod
    @overload
    def create_scale(x_scale: float, y_scale: float, z_scale: float, center_point: System.Numerics.Vector3) -> System.Numerics.Matrix4x4:
        """
        Creates a scaling matrix that is offset by a given center point.
        
        :param x_scale: The value to scale by on the X axis.
        :param y_scale: The value to scale by on the Y axis.
        :param z_scale: The value to scale by on the Z axis.
        :param center_point: The center point.
        :returns: The scaling matrix.
        """
        ...

    @staticmethod
    @overload
    def create_scale(scales: System.Numerics.Vector3) -> System.Numerics.Matrix4x4:
        """
        Creates a scaling matrix from the specified vector scale.
        
        :param scales: The scale to use.
        :returns: The scaling matrix.
        """
        ...

    @staticmethod
    @overload
    def create_scale(scales: System.Numerics.Vector3, center_point: System.Numerics.Vector3) -> System.Numerics.Matrix4x4:
        """
        Creates a scaling matrix with a center point.
        
        :param scales: The vector that contains the amount to scale on each axis.
        :param center_point: The center point.
        :returns: The scaling matrix.
        """
        ...

    @staticmethod
    @overload
    def create_scale(scale: float) -> System.Numerics.Matrix4x4:
        """
        Creates a uniform scaling matrix that scale equally on each axis.
        
        :param scale: The uniform scaling factor.
        :returns: The scaling matrix.
        """
        ...

    @staticmethod
    @overload
    def create_scale(scale: float, center_point: System.Numerics.Vector3) -> System.Numerics.Matrix4x4:
        """
        Creates a uniform scaling matrix that scales equally on each axis with a center point.
        
        :param scale: The uniform scaling factor.
        :param center_point: The center point.
        :returns: The scaling matrix.
        """
        ...

    @staticmethod
    def create_shadow(light_direction: System.Numerics.Vector3, plane: System.Numerics.Plane) -> System.Numerics.Matrix4x4:
        """
        Creates a matrix that flattens geometry into a specified plane as if casting a shadow from a specified light source.
        
        :param light_direction: The direction from which the light that will cast the shadow is coming.
        :param plane: The plane onto which the new matrix should flatten geometry so as to cast a shadow.
        :returns: A new matrix that can be used to flatten geometry onto the specified plane from the specified direction.
        """
        ...

    @staticmethod
    @overload
    def create_translation(position: System.Numerics.Vector3) -> System.Numerics.Matrix4x4:
        """
        Creates a translation matrix from the specified 3-dimensional vector.
        
        :param position: The amount to translate in each axis.
        :returns: The translation matrix.
        """
        ...

    @staticmethod
    @overload
    def create_translation(x_position: float, y_position: float, z_position: float) -> System.Numerics.Matrix4x4:
        """
        Creates a translation matrix from the specified X, Y, and Z components.
        
        :param x_position: The amount to translate on the X axis.
        :param y_position: The amount to translate on the Y axis.
        :param z_position: The amount to translate on the Z axis.
        :returns: The translation matrix.
        """
        ...

    @staticmethod
    def create_viewport(x: float, y: float, width: float, height: float, min_depth: float, max_depth: float) -> System.Numerics.Matrix4x4:
        """
        Creates a right-handed viewport matrix from the specified parameters.
        
        :param x: X coordinate of the viewport upper left corner.
        :param y: Y coordinate of the viewport upper left corner.
        :param width: Viewport width.
        :param height: Viewport height.
        :param min_depth: Viewport minimum depth.
        :param max_depth: Viewport maximum depth.
        :returns: The right-handed viewport matrix.
        """
        ...

    @staticmethod
    def create_viewport_left_handed(x: float, y: float, width: float, height: float, min_depth: float, max_depth: float) -> System.Numerics.Matrix4x4:
        """
        Creates a left-handed viewport matrix from the specified parameters.
        
        :param x: X coordinate of the viewport upper left corner.
        :param y: Y coordinate of the viewport upper left corner.
        :param width: Viewport width.
        :param height: Viewport height.
        :param min_depth: Viewport minimum depth.
        :param max_depth: Viewport maximum depth.
        :returns: The left-handed viewport matrix.
        """
        ...

    @staticmethod
    def create_world(position: System.Numerics.Vector3, forward: System.Numerics.Vector3, up: System.Numerics.Vector3) -> System.Numerics.Matrix4x4:
        """
        Creates a world matrix with the specified parameters.
        
        :param position: The position of the object.
        :param forward: The forward direction of the object.
        :param up: The upward direction of the object. Its value is usually [0, 1, 0].
        :returns: The world matrix.
        """
        ...

    @staticmethod
    def decompose(matrix: System.Numerics.Matrix4x4, scale: typing.Optional[System.Numerics.Vector3], rotation: typing.Optional[System.Numerics.Quaternion], translation: typing.Optional[System.Numerics.Vector3]) -> typing.Tuple[bool, System.Numerics.Vector3, System.Numerics.Quaternion, System.Numerics.Vector3]:
        """
        Attempts to extract the scale, translation, and rotation components from the given scale, rotation, or translation matrix. The return value indicates whether the operation succeeded.
        
        :param matrix: The source matrix.
        :param scale: When this method returns, contains the scaling component of the transformation matrix if the operation succeeded.
        :param rotation: When this method returns, contains the rotation component of the transformation matrix if the operation succeeded.
        :param translation: When the method returns, contains the translation component of the transformation matrix if the operation succeeded.
        :returns: true if  was decomposed successfully; otherwise,  false.
        """
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        """
        Returns a value that indicates whether this instance and a specified object are equal.
        
        :param obj: The object to compare with the current instance.
        :returns: true if the current instance and  are equal; otherwise, false. If  is null, the method returns false.
        """
        ...

    @overload
    def equals(self, other: System.Numerics.Matrix4x4) -> bool:
        """
        Returns a value that indicates whether this instance and another 4x4 matrix are equal.
        
        :param other: The other matrix.
        :returns: true if the two matrices are equal; otherwise, false.
        """
        ...

    def get_determinant(self) -> float:
        """
        Calculates the determinant of the current 4x4 matrix.
        
        :returns: The determinant.
        """
        ...

    def get_hash_code(self) -> int:
        """
        Returns the hash code for this instance.
        
        :returns: The hash code.
        """
        ...

    @staticmethod
    def invert(matrix: System.Numerics.Matrix4x4, result: typing.Optional[System.Numerics.Matrix4x4]) -> typing.Tuple[bool, System.Numerics.Matrix4x4]:
        """
        Tries to invert the specified matrix. The return value indicates whether the operation succeeded.
        
        :param matrix: The matrix to invert.
        :param result: When this method returns, contains the inverted matrix if the operation succeeded.
        :returns: true if  was converted successfully; otherwise,  false.
        """
        ...

    @staticmethod
    def lerp(matrix_1: System.Numerics.Matrix4x4, matrix_2: System.Numerics.Matrix4x4, amount: float) -> System.Numerics.Matrix4x4:
        """
        Performs a linear interpolation from one matrix to a second matrix based on a value that specifies the weighting of the second matrix.
        
        :param matrix_1: The first matrix.
        :param matrix_2: The second matrix.
        :param amount: The relative weighting of .
        :returns: The interpolated matrix.
        """
        ...

    @staticmethod
    @overload
    def multiply(value_1: System.Numerics.Matrix4x4, value_2: System.Numerics.Matrix4x4) -> System.Numerics.Matrix4x4:
        """
        Multiplies two matrices together to compute the product.
        
        :param value_1: The first matrix.
        :param value_2: The second matrix.
        :returns: The product matrix.
        """
        ...

    @staticmethod
    @overload
    def multiply(value_1: System.Numerics.Matrix4x4, value_2: float) -> System.Numerics.Matrix4x4:
        """
        Multiplies a matrix by a float to compute the product.
        
        :param value_1: The matrix to scale.
        :param value_2: The scaling value to use.
        :returns: The scaled matrix.
        """
        ...

    @staticmethod
    def negate(value: System.Numerics.Matrix4x4) -> System.Numerics.Matrix4x4:
        """
        Negates the specified matrix by multiplying all its values by -1.
        
        :param value: The matrix to negate.
        :returns: The negated matrix.
        """
        ...

    @staticmethod
    def subtract(value_1: System.Numerics.Matrix4x4, value_2: System.Numerics.Matrix4x4) -> System.Numerics.Matrix4x4:
        """
        Subtracts each element in a second matrix from its corresponding element in a first matrix.
        
        :param value_1: The first matrix.
        :param value_2: The second matrix.
        :returns: The matrix containing the values that result from subtracting each element in  from its corresponding element in .
        """
        ...

    def to_string(self) -> str:
        """
        Returns a string that represents this matrix.
        
        :returns: The string representation of this matrix.
        """
        ...

    @staticmethod
    def transform(value: System.Numerics.Matrix4x4, rotation: System.Numerics.Quaternion) -> System.Numerics.Matrix4x4:
        """
        Transforms the specified matrix by applying the specified Quaternion rotation.
        
        :param value: The matrix to transform.
        :param rotation: The rotation t apply.
        :returns: The transformed matrix.
        """
        ...

    @staticmethod
    def transpose(matrix: System.Numerics.Matrix4x4) -> System.Numerics.Matrix4x4:
        """
        Transposes the rows and columns of a matrix.
        
        :param matrix: The matrix to transpose.
        :returns: The transposed matrix.
        """
        ...


class Vector(typing.Generic[System_Numerics_Vector_T], System.Runtime.Intrinsics.ISimdVector[System_Numerics_Vector, System_Numerics_Vector_T], System.IFormattable):
    """Represents a single vector of a specified numeric type that is suitable for low-level optimization of parallel algorithms."""

    IS_HARDWARE_ACCELERATED: bool
    """Gets a value that indicates whether vector operations are subject to hardware acceleration through JIT intrinsic support."""

    ALL_BITS_SET: System.Numerics.Vector[System_Numerics_Vector_T]
    """Gets a new Vector{T} with all bits set to 1."""

    COUNT: int
    """Gets the number of T that are in a Vector{T}."""

    INDICES: System.Numerics.Vector[System_Numerics_Vector_T]
    """Gets a new Vector{T} with the elements set to their index."""

    IS_SUPPORTED: bool
    """Gets true if T is supported; otherwise, false."""

    ONE: System.Numerics.Vector[System_Numerics_Vector_T]
    """Gets a new Vector{T} with all elements initialized to one."""

    ZERO: System.Numerics.Vector[System_Numerics_Vector_T]
    """Gets a new Vector{T} with all elements initialized to zero."""

    @overload
    def __add__(self, right: System.Numerics.Vector[System_Numerics_Vector_T]) -> System.Numerics.Vector[System_Numerics_Vector_T]:
        """
        Adds two vectors to compute their sum.
        
        :param left: The vector to add with .
        :param right: The vector to add with .
        :returns: The sum of  and .
        """
        ...

    @overload
    def __add__(self) -> System.Numerics.Vector[System_Numerics_Vector_T]:
        """
        Returns a given vector unchanged.
        
        :param value: The vector.
        """
        ...

    def __and__(self, right: System.Numerics.Vector[System_Numerics_Vector_T]) -> System.Numerics.Vector[System_Numerics_Vector_T]:
        """
        Computes the bitwise-and of two vectors.
        
        :param left: The vector to bitwise-and with .
        :param right: The vector to bitwise-and with .
        :returns: The bitwise-and of  and .
        """
        ...

    def __eq__(self, right: System.Numerics.Vector[System_Numerics_Vector_T]) -> bool:
        """
        Compares two vectors to determine if all elements are equal.
        
        :param left: The vector to compare with .
        :param right: The vector to compare with .
        :returns: true if all elements in  were equal to the corresponding element in .
        """
        ...

    def __getitem__(self, index: int) -> System_Numerics_Vector_T:
        """
        Gets the element at the specified index.
        
        :param index: The index of the element to get.
        :returns: The value of the element at .
        """
        ...

    @overload
    def __iadd__(self, right: System.Numerics.Vector[System_Numerics_Vector_T]) -> System.Numerics.Vector[System_Numerics_Vector_T]:
        """
        Adds two vectors to compute their sum.
        
        :param left: The vector to add with .
        :param right: The vector to add with .
        :returns: The sum of  and .
        """
        ...

    @overload
    def __iadd__(self) -> System.Numerics.Vector[System_Numerics_Vector_T]:
        """
        Returns a given vector unchanged.
        
        :param value: The vector.
        """
        ...

    def __iand__(self, right: System.Numerics.Vector[System_Numerics_Vector_T]) -> System.Numerics.Vector[System_Numerics_Vector_T]:
        """
        Computes the bitwise-and of two vectors.
        
        :param left: The vector to bitwise-and with .
        :param right: The vector to bitwise-and with .
        :returns: The bitwise-and of  and .
        """
        ...

    def __ilshift__(self, shift_count: int) -> System.Numerics.Vector[System_Numerics_Vector_T]:
        """
        Shifts each element of a vector left by the specified amount.
        
        :param value: The vector whose elements are to be shifted.
        :param shift_count: The number of bits by which to shift each element.
        :returns: A vector whose elements where shifted left by .
        """
        ...

    @overload
    def __imul__(self, right: System.Numerics.Vector[System_Numerics_Vector_T]) -> System.Numerics.Vector[System_Numerics_Vector_T]:
        """
        Multiplies two vectors to compute their element-wise product.
        
        :param left: The vector to multiply with .
        :param right: The vector to multiply with .
        :returns: The element-wise product of  and .
        """
        ...

    @overload
    def __imul__(self, factor: System_Numerics_Vector_T) -> System.Numerics.Vector[System_Numerics_Vector_T]:
        """
        Multiplies a vector by a scalar to compute their product.
        
        :param value: The vector to multiply with .
        :param factor: The scalar to multiply with .
        :returns: The product of  and .
        """
        ...

    @overload
    def __imul__(self, value: System.Numerics.Vector[System_Numerics_Vector_T]) -> System.Numerics.Vector[System_Numerics_Vector_T]:
        """
        Multiplies a vector by a scalar to compute their product.
        
        :param factor: The scalar to multiply with .
        :param value: The vector to multiply with .
        :returns: The product of  and .
        """
        ...

    @overload
    def __init__(self, value: System_Numerics_Vector_T) -> None:
        """
        Creates a new Vector{T} instance with all elements initialized to the specified value.
        
        :param value: The value that all elements will be initialized to.
        :returns: A new Vector{T} with all elements initialized to .
        """
        ...

    @overload
    def __init__(self, values: typing.List[System_Numerics_Vector_T]) -> None:
        """
        Creates a new Vector{T} from a given array.
        
        :param values: The array from which the vector is created.
        :returns: A new Vector{T} with its elements set to the first Vector{T}.Count elements from .
        """
        ...

    @overload
    def __init__(self, values: typing.List[System_Numerics_Vector_T], index: int) -> None:
        """
        Creates a new Vector{T} from a given array.
        
        :param values: The array from which the vector is created.
        :param index: The index in  at which to being reading elements.
        :returns: A new Vector{T} with its elements set to the first Vector{T}.Count elements from .
        """
        ...

    @overload
    def __init__(self, values: System.ReadOnlySpan[System_Numerics_Vector_T]) -> None:
        """
        Creates a new Vector{T} from a given readonly span.
        
        :param values: The readonly span from which the vector is created.
        :returns: A new Vector{T} with its elements set to the first Vector{T}.Count elements from .
        """
        ...

    @overload
    def __init__(self, values: System.ReadOnlySpan[int]) -> None:
        """
        Creates a new Vector{T} from a given readonly span.
        
        :param values: The readonly span from which the vector is created.
        :returns: A new Vector{T} with its elements set to the first sizeof() elements from .
        """
        ...

    @overload
    def __init__(self, values: System.Span[System_Numerics_Vector_T]) -> None:
        """
        Creates a new Vector{T} from a given span.
        
        :param values: The span from which the vector is created.
        :returns: A new Vector{T} with its elements set to the first Vector{T}.Count elements from .
        """
        ...

    def __invert__(self) -> System.Numerics.Vector[System_Numerics_Vector_T]:
        """
        Computes the ones-complement of a vector.
        
        :param value: The vector whose ones-complement is to be computed.
        :returns: A vector whose elements are the ones-complement of the corresponding elements in .
        """
        ...

    def __ior__(self, right: System.Numerics.Vector[System_Numerics_Vector_T]) -> System.Numerics.Vector[System_Numerics_Vector_T]:
        """
        Computes the bitwise-or of two vectors.
        
        :param left: The vector to bitwise-or with .
        :param right: The vector to bitwise-or with .
        :returns: The bitwise-or of  and .
        """
        ...

    def __irshift__(self, shift_count: int) -> System.Numerics.Vector[System_Numerics_Vector_T]:
        """
        Shifts (signed) each element of a vector right by the specified amount.
        
        :param value: The vector whose elements are to be shifted.
        :param shift_count: The number of bits by which to shift each element.
        :returns: A vector whose elements where shifted right by .
        """
        ...

    @overload
    def __isub__(self, right: System.Numerics.Vector[System_Numerics_Vector_T]) -> System.Numerics.Vector[System_Numerics_Vector_T]:
        """
        Subtracts two vectors to compute their difference.
        
        :param left: The vector from which  will be subtracted.
        :param right: The vector to subtract from .
        :returns: The difference of  and .
        """
        ...

    @overload
    def __isub__(self) -> System.Numerics.Vector[System_Numerics_Vector_T]:
        """
        Computes the unary negation of a vector.
        
        :param value: The vector to negate.
        :returns: A vector whose elements are the unary negation of the corresponding elements in .
        """
        ...

    @overload
    def __itruediv__(self, right: System.Numerics.Vector[System_Numerics_Vector_T]) -> System.Numerics.Vector[System_Numerics_Vector_T]:
        """
        Divides two vectors to compute their quotient.
        
        :param left: The vector that will be divided by .
        :param right: The vector that will divide .
        :returns: The quotient of  divided by .
        """
        ...

    @overload
    def __itruediv__(self, right: System_Numerics_Vector_T) -> System.Numerics.Vector[System_Numerics_Vector_T]:
        """
        Divides a vector by a scalar to compute the per-element quotient.
        
        :param left: The vector that will be divided by .
        :param right: The scalar that will divide .
        :returns: The quotient of  divided by .
        """
        ...

    def __ixor__(self, right: System.Numerics.Vector[System_Numerics_Vector_T]) -> System.Numerics.Vector[System_Numerics_Vector_T]:
        """
        Computes the exclusive-or of two vectors.
        
        :param left: The vector to exclusive-or with .
        :param right: The vector to exclusive-or with .
        :returns: The exclusive-or of  and .
        """
        ...

    def __lshift__(self, shift_count: int) -> System.Numerics.Vector[System_Numerics_Vector_T]:
        """
        Shifts each element of a vector left by the specified amount.
        
        :param value: The vector whose elements are to be shifted.
        :param shift_count: The number of bits by which to shift each element.
        :returns: A vector whose elements where shifted left by .
        """
        ...

    @overload
    def __mul__(self, right: System.Numerics.Vector[System_Numerics_Vector_T]) -> System.Numerics.Vector[System_Numerics_Vector_T]:
        """
        Multiplies two vectors to compute their element-wise product.
        
        :param left: The vector to multiply with .
        :param right: The vector to multiply with .
        :returns: The element-wise product of  and .
        """
        ...

    @overload
    def __mul__(self, factor: System_Numerics_Vector_T) -> System.Numerics.Vector[System_Numerics_Vector_T]:
        """
        Multiplies a vector by a scalar to compute their product.
        
        :param value: The vector to multiply with .
        :param factor: The scalar to multiply with .
        :returns: The product of  and .
        """
        ...

    @overload
    def __mul__(self, value: System.Numerics.Vector[System_Numerics_Vector_T]) -> System.Numerics.Vector[System_Numerics_Vector_T]:
        """
        Multiplies a vector by a scalar to compute their product.
        
        :param factor: The scalar to multiply with .
        :param value: The vector to multiply with .
        :returns: The product of  and .
        """
        ...

    def __ne__(self, right: System.Numerics.Vector[System_Numerics_Vector_T]) -> bool:
        """
        Compares two vectors to determine if any elements are not equal.
        
        :param left: The vector to compare with .
        :param right: The vector to compare with .
        :returns: true if any elements in  was not equal to the corresponding element in .
        """
        ...

    def __or__(self, right: System.Numerics.Vector[System_Numerics_Vector_T]) -> System.Numerics.Vector[System_Numerics_Vector_T]:
        """
        Computes the bitwise-or of two vectors.
        
        :param left: The vector to bitwise-or with .
        :param right: The vector to bitwise-or with .
        :returns: The bitwise-or of  and .
        """
        ...

    def __rshift__(self, shift_count: int) -> System.Numerics.Vector[System_Numerics_Vector_T]:
        """
        Shifts (signed) each element of a vector right by the specified amount.
        
        :param value: The vector whose elements are to be shifted.
        :param shift_count: The number of bits by which to shift each element.
        :returns: A vector whose elements where shifted right by .
        """
        ...

    @overload
    def __sub__(self, right: System.Numerics.Vector[System_Numerics_Vector_T]) -> System.Numerics.Vector[System_Numerics_Vector_T]:
        """
        Subtracts two vectors to compute their difference.
        
        :param left: The vector from which  will be subtracted.
        :param right: The vector to subtract from .
        :returns: The difference of  and .
        """
        ...

    @overload
    def __sub__(self) -> System.Numerics.Vector[System_Numerics_Vector_T]:
        """
        Computes the unary negation of a vector.
        
        :param value: The vector to negate.
        :returns: A vector whose elements are the unary negation of the corresponding elements in .
        """
        ...

    @overload
    def __truediv__(self, right: System.Numerics.Vector[System_Numerics_Vector_T]) -> System.Numerics.Vector[System_Numerics_Vector_T]:
        """
        Divides two vectors to compute their quotient.
        
        :param left: The vector that will be divided by .
        :param right: The vector that will divide .
        :returns: The quotient of  divided by .
        """
        ...

    @overload
    def __truediv__(self, right: System_Numerics_Vector_T) -> System.Numerics.Vector[System_Numerics_Vector_T]:
        """
        Divides a vector by a scalar to compute the per-element quotient.
        
        :param left: The vector that will be divided by .
        :param right: The scalar that will divide .
        :returns: The quotient of  divided by .
        """
        ...

    def __xor__(self, right: System.Numerics.Vector[System_Numerics_Vector_T]) -> System.Numerics.Vector[System_Numerics_Vector_T]:
        """
        Computes the exclusive-or of two vectors.
        
        :param left: The vector to exclusive-or with .
        :param right: The vector to exclusive-or with .
        :returns: The exclusive-or of  and .
        """
        ...

    @staticmethod
    def as_plane(value: System.Numerics.Vector4) -> System.Numerics.Plane:
        """
        Reinterprets a Vector4 as a new Plane.
        
        :param value: The vector to reinterpret.
        :returns: reinterpreted as a new Plane.
        """
        ...

    @staticmethod
    def as_quaternion(value: System.Numerics.Vector4) -> System.Numerics.Quaternion:
        """
        Reinterprets a Vector4 as a new Quaternion.
        
        :param value: The vector to reinterpret.
        :returns: reinterpreted as a new Quaternion.
        """
        ...

    @staticmethod
    def as_vector_2(value: System.Numerics.Vector4) -> System.Numerics.Vector2:
        """
        Reinterprets a Vector4 as a new Vector2.
        
        :param value: The vector to reinterpret.
        :returns: reinterpreted as a new Vector2.
        """
        ...

    @staticmethod
    def as_vector_3(value: System.Numerics.Vector4) -> System.Numerics.Vector3:
        """
        Reinterprets a Vector4 as a new Vector3.
        
        :param value: The vector to reinterpret.
        :returns: reinterpreted as a new Vector3.
        """
        ...

    @staticmethod
    @overload
    def as_vector_4(value: System.Numerics.Quaternion) -> System.Numerics.Vector4:
        """
        Reinterprets a Quaternion as a new Vector4.
        
        :param value: The quaternion to reinterpret.
        :returns: reinterpreted as a new Quaternion.
        """
        ...

    @staticmethod
    @overload
    def as_vector_4(value: System.Numerics.Plane) -> System.Numerics.Vector4:
        """
        Reinterprets a Plane as a new Vector4.
        
        :param value: The plane to reinterpret.
        :returns: reinterpreted as a new Vector4.
        """
        ...

    @staticmethod
    @overload
    def as_vector_4(value: System.Numerics.Vector2) -> System.Numerics.Vector4:
        """
        Reinterprets a Vector2 to a new Vector4 with the new elements zeroed.
        
        :param value: The vector to reinterpret.
        :returns: reinterpreted to a new Vector4 with the new elements zeroed.
        """
        ...

    @staticmethod
    @overload
    def as_vector_4(value: System.Numerics.Vector3) -> System.Numerics.Vector4:
        """
        Converts a Vector3 to a new Vector4 with the new elements zeroed.
        
        :param value: The vector to convert.
        :returns: converted to a new Vector4 with the new elements zeroed.
        """
        ...

    @staticmethod
    @overload
    def as_vector_4_unsafe(value: System.Numerics.Vector2) -> System.Numerics.Vector4:
        """
        Reinterprets a Vector2 to a new Vector4 with the new elements undefined.
        
        :param value: The vector to reinterpret.
        :returns: reinterpreted to a new Vector4 with the new elements undefined.
        """
        ...

    @staticmethod
    @overload
    def as_vector_4_unsafe(value: System.Numerics.Vector3) -> System.Numerics.Vector4:
        """
        Converts a Vector3 to a new Vector4 with the new elements undefined.
        
        :param value: The vector to convert.
        :returns: converted to a new Vector4 with the new elements undefined.
        """
        ...

    @staticmethod
    def ceiling(value: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        """
        Computes the ceiling of each element in a vector.
        
        :param value: The vector that will have its ceiling computed.
        :returns: A vector whose elements are the ceiling of the elements in .
        """
        ...

    @staticmethod
    def conditional_select(condition: System.Numerics.Vector[int], left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        """
        Conditionally selects a value from two vectors on a bitwise basis.
        
        :param condition: The mask that is used to select a value from  or .
        :param left: The vector that is selected when the corresponding bit in  is one.
        :param right: The vector that is selected when the corresponding bit in  is zero.
        :returns: A vector whose bits come from  or  based on the value of .
        """
        ...

    @staticmethod
    def convert_to_double(value: System.Numerics.Vector[int]) -> System.Numerics.Vector[float]:
        """
        Converts a Vector<Int64> to a Vector<Double>.
        
        :param value: The vector to convert.
        :returns: The converted vector.
        """
        ...

    @staticmethod
    def convert_to_int_32(value: System.Numerics.Vector[float]) -> System.Numerics.Vector[int]:
        """
        Converts a Vector<Single> to a Vector<Int32> using saturation on overflow.
        
        :param value: The vector to convert.
        :returns: The converted vector.
        """
        ...

    @staticmethod
    def convert_to_int_32_native(value: System.Numerics.Vector[float]) -> System.Numerics.Vector[int]:
        """
        Converts a Vector<Single> to a Vector<Int32> using platform specific behavior on overflow.
        
        :param value: The vector to convert.
        :returns: The converted vector.
        """
        ...

    @staticmethod
    def convert_to_int_64(value: System.Numerics.Vector[float]) -> System.Numerics.Vector[int]:
        """
        Converts a Vector<Double> to a Vector<Int64> using saturation on overflow.
        
        :param value: The vector to convert.
        :returns: The converted vector.
        """
        ...

    @staticmethod
    def convert_to_int_64_native(value: System.Numerics.Vector[float]) -> System.Numerics.Vector[int]:
        """
        Converts a Vector<Double> to a Vector<Int64> using platform specific behavior on overflow.
        
        :param value: The vector to convert.
        :returns: The converted vector.
        """
        ...

    @staticmethod
    def convert_to_single(value: System.Numerics.Vector[int]) -> System.Numerics.Vector[float]:
        """
        Converts a Vector<Int32> to a Vector<Single>.
        
        :param value: The vector to convert.
        :returns: The converted vector.
        """
        ...

    @staticmethod
    def convert_to_u_int_32(value: System.Numerics.Vector[float]) -> System.Numerics.Vector[int]:
        """
        Converts a Vector<Single> to a Vector<UInt32> using saturation on overflow.
        
        :param value: The vector to convert.
        :returns: The converted vector.
        """
        ...

    @staticmethod
    def convert_to_u_int_32_native(value: System.Numerics.Vector[float]) -> System.Numerics.Vector[int]:
        """
        Converts a Vector<Single> to a Vector<UInt32> using platform specific behavior on overflow.
        
        :param value: The vector to convert.
        :returns: The converted vector.
        """
        ...

    @staticmethod
    def convert_to_u_int_64(value: System.Numerics.Vector[float]) -> System.Numerics.Vector[int]:
        """
        Converts a Vector<Double> to a Vector<UInt64> using saturation on overflow.
        
        :param value: The vector to convert.
        :returns: The converted vector.
        """
        ...

    @staticmethod
    def convert_to_u_int_64_native(value: System.Numerics.Vector[float]) -> System.Numerics.Vector[int]:
        """
        Converts a Vector<Double> to a Vector<UInt64> using platform specific behavior on overflow.
        
        :param value: The vector to convert.
        :returns: The converted vector.
        """
        ...

    @overload
    def copy_to(self, destination: typing.List[System_Numerics_Vector_T]) -> None:
        """
        Copies a Vector{T} to a given array.
        
        :param destination: The array to which the current instance is copied.
        """
        ...

    @overload
    def copy_to(self, destination: typing.List[System_Numerics_Vector_T], start_index: int) -> None:
        """
        Copies a Vector{T} to a given array starting at the specified index.
        
        :param destination: The array to which the current instance is copied.
        :param start_index: The starting index of  which current instance will be copied to.
        """
        ...

    @overload
    def copy_to(self, destination: System.Span[int]) -> None:
        """
        Copies a Vector{T} to a given span.
        
        :param destination: The span to which the current instance is copied.
        """
        ...

    @overload
    def copy_to(self, destination: System.Span[System_Numerics_Vector_T]) -> None:
        """
        Copies a Vector{T} to a given span.
        
        :param destination: The span to which the current instance is copied.
        """
        ...

    @staticmethod
    def cos(vector: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    def degrees_to_radians(degrees: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        """
        Returns a boolean indicating whether the given Object is equal to this vector instance.
        
        :param obj: The Object to compare against.
        :returns: True if the Object is equal to this vector; False otherwise.
        """
        ...

    @staticmethod
    @overload
    def equals(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[int]:
        """
        Compares two vectors to determine if they are equal on a per-element basis.
        
        :param left: The vector to compare with .
        :param right: The vector to compare with .
        :returns: A vector whose elements are all-bits-set or zero, depending on if the corresponding elements in  and  were equal.
        """
        ...

    @staticmethod
    @overload
    def equals(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """
        Compares two vectors to determine if they are equal on a per-element basis.
        
        :param left: The vector to compare with .
        :param right: The vector to compare with .
        :returns: A vector whose elements are all-bits-set or zero, depending on if the corresponding elements in  and  were equal.
        """
        ...

    @overload
    def equals(self, other: System.Numerics.Vector[System_Numerics_Vector_T]) -> bool:
        """
        Returns a boolean indicating whether the given vector is equal to this vector instance.
        
        :param other: The vector to compare this instance to.
        :returns: True if the other vector is equal to this instance; False otherwise.
        """
        ...

    @staticmethod
    def exp(vector: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    @overload
    def extract_most_significant_bits(vector: System.Numerics.Vector4) -> int:
        ...

    @staticmethod
    @overload
    def extract_most_significant_bits(vector: System.Numerics.Vector2) -> int:
        ...

    @staticmethod
    @overload
    def extract_most_significant_bits(vector: System.Numerics.Vector3) -> int:
        ...

    @staticmethod
    def floor(value: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        """
        Computes the floor of each element in a vector.
        
        :param value: The vector that will have its floor computed.
        :returns: A vector whose elements are the floor of the elements in .
        """
        ...

    @staticmethod
    def fused_multiply_add(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float], addend: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        """
        Computes ( * ) + , rounded as one ternary operation.
        
        :param left: The vector to be multiplied with .
        :param right: The vector to be multiplied with .
        :param addend: The vector to be added to the result of  multiplied by .
        :returns: ( * ) + , rounded as one ternary operation.
        """
        ...

    @staticmethod
    @overload
    def get_element(vector: System.Numerics.Vector4, index: int) -> float:
        ...

    @staticmethod
    @overload
    def get_element(vector: System.Numerics.Vector2, index: int) -> float:
        ...

    @staticmethod
    @overload
    def get_element(vector: System.Numerics.Vector3, index: int) -> float:
        ...

    def get_hash_code(self) -> int:
        """
        Returns the hash code for this instance.
        
        :returns: The hash code.
        """
        ...

    @staticmethod
    @overload
    def greater_than(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[int]:
        """
        Compares two vectors to determine which is greater on a per-element basis.
        
        :param left: The vector to compare with .
        :param right: The vector to compare with .
        :returns: A vector whose elements are all-bits-set or zero, depending on if which of the corresponding elements in  and  were greater.
        """
        ...

    @staticmethod
    @overload
    def greater_than(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """
        Compares two vectors to determine which is greater on a per-element basis.
        
        :param left: The vector to compare with .
        :param right: The vector to compare with .
        :returns: A vector whose elements are all-bits-set or zero, depending on if which of the corresponding elements in  and  were greater.
        """
        ...

    @staticmethod
    @overload
    def greater_than_or_equal(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[int]:
        """
        Compares two vectors to determine which is greater or equal on a per-element basis.
        
        :param left: The vector to compare with .
        :param right: The vector to compare with .
        :returns: A vector whose elements are all-bits-set or zero, depending on if which of the corresponding elements in  and  were greater or equal.
        """
        ...

    @staticmethod
    @overload
    def greater_than_or_equal(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """
        Compares two vectors to determine which is greater or equal on a per-element basis.
        
        :param left: The vector to compare with .
        :param right: The vector to compare with .
        :returns: A vector whose elements are all-bits-set or zero, depending on if which of the corresponding elements in  and  were greater or equal.
        """
        ...

    @staticmethod
    def hypot(x: System.Numerics.Vector[float], y: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    def lerp(x: System.Numerics.Vector[float], y: System.Numerics.Vector[float], amount: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        """
        Performs a linear interpolation between two vectors based on the given weighting.
        
        :param x: The first vector.
        :param y: The second vector.
        :param amount: A value between 0 and 1 that indicates the weight of .
        :returns: The interpolated vector.
        """
        ...

    @staticmethod
    @overload
    def less_than(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[int]:
        """
        Compares two vectors to determine which is less on a per-element basis.
        
        :param left: The vector to compare with .
        :param right: The vector to compare with .
        :returns: A vector whose elements are all-bits-set or zero, depending on if which of the corresponding elements in  and  were less.
        """
        ...

    @staticmethod
    @overload
    def less_than(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """
        Compares two vectors to determine which is less on a per-element basis.
        
        :param left: The vector to compare with .
        :param right: The vector to compare with .
        :returns: A vector whose elements are all-bits-set or zero, depending on if which of the corresponding elements in  and  were less.
        """
        ...

    @staticmethod
    @overload
    def less_than_or_equal(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float]) -> System.Numerics.Vector[int]:
        """
        Compares two vectors to determine which is less or equal on a per-element basis.
        
        :param left: The vector to compare with .
        :param right: The vector to compare with .
        :returns: A vector whose elements are all-bits-set or zero, depending on if which of the corresponding elements in  and  were less or equal.
        """
        ...

    @staticmethod
    @overload
    def less_than_or_equal(left: System.Numerics.Vector[int], right: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """
        Compares two vectors to determine which is less or equal on a per-element basis.
        
        :param left: The vector to compare with .
        :param right: The vector to compare with .
        :returns: A vector whose elements are all-bits-set or zero, depending on if which of the corresponding elements in  and  were less or equal.
        """
        ...

    @staticmethod
    def log(vector: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    def log_2(vector: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    def multiply_add_estimate(left: System.Numerics.Vector[float], right: System.Numerics.Vector[float], addend: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    @overload
    def narrow(low: System.Numerics.Vector[float], high: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        """
        Narrows two Vector<Double> instances into one Vector<Single>.
        
        :param low: The vector that will be narrowed to the lower half of the result vector.
        :param high: The vector that will be narrowed to the upper half of the result vector.
        :returns: A Vector<Single> containing elements narrowed from  and .
        """
        ...

    @staticmethod
    @overload
    def narrow(low: System.Numerics.Vector[int], high: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """
        Narrows two Vector<Int16> instances into one Vector<SByte>.
        
        :param low: The vector that will be narrowed to the lower half of the result vector.
        :param high: The vector that will be narrowed to the upper half of the result vector.
        :returns: A Vector<SByte> containing elements narrowed from  and .
        """
        ...

    @staticmethod
    def radians_to_degrees(radians: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    @overload
    def round(vector: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    @overload
    def round(vector: System.Numerics.Vector[float], mode: System.MidpointRounding) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    @overload
    def shift_left(value: System.Numerics.Vector[int], shift_count: int) -> System.Numerics.Vector[int]:
        """
        Shifts each element of a vector left by the specified amount.
        
        :param value: The vector whose elements are to be shifted.
        :param shift_count: The number of bits by which to shift each element.
        :returns: A vector whose elements where shifted left by .
        """
        ...

    @staticmethod
    @overload
    def shift_left(value: System.Numerics.Vector[System.IntPtr], shift_count: int) -> System.Numerics.Vector[System.IntPtr]:
        """
        Shifts each element of a vector left by the specified amount.
        
        :param value: The vector whose elements are to be shifted.
        :param shift_count: The number of bits by which to shift each element.
        :returns: A vector whose elements where shifted left by .
        """
        ...

    @staticmethod
    @overload
    def shift_left(value: System.Numerics.Vector[System.UIntPtr], shift_count: int) -> System.Numerics.Vector[System.UIntPtr]:
        """
        Shifts each element of a vector left by the specified amount.
        
        :param value: The vector whose elements are to be shifted.
        :param shift_count: The number of bits by which to shift each element.
        :returns: A vector whose elements where shifted left by .
        """
        ...

    @staticmethod
    @overload
    def shift_right_arithmetic(value: System.Numerics.Vector[int], shift_count: int) -> System.Numerics.Vector[int]:
        """
        Shifts (signed) each element of a vector right by the specified amount.
        
        :param value: The vector whose elements are to be shifted.
        :param shift_count: The number of bits by which to shift each element.
        :returns: A vector whose elements where shifted right by .
        """
        ...

    @staticmethod
    @overload
    def shift_right_arithmetic(value: System.Numerics.Vector[System.IntPtr], shift_count: int) -> System.Numerics.Vector[System.IntPtr]:
        """
        Shifts (signed) each element of a vector right by the specified amount.
        
        :param value: The vector whose elements are to be shifted.
        :param shift_count: The number of bits by which to shift each element.
        :returns: A vector whose elements where shifted right by .
        """
        ...

    @staticmethod
    @overload
    def shift_right_logical(value: System.Numerics.Vector[int], shift_count: int) -> System.Numerics.Vector[int]:
        """
        Shifts (unsigned) each element of a vector right by the specified amount.
        
        :param value: The vector whose elements are to be shifted.
        :param shift_count: The number of bits by which to shift each element.
        :returns: A vector whose elements where shifted right by .
        """
        ...

    @staticmethod
    @overload
    def shift_right_logical(value: System.Numerics.Vector[System.IntPtr], shift_count: int) -> System.Numerics.Vector[System.IntPtr]:
        """
        Shifts (unsigned) each element of a vector right by the specified amount.
        
        :param value: The vector whose elements are to be shifted.
        :param shift_count: The number of bits by which to shift each element.
        :returns: A vector whose elements where shifted right by .
        """
        ...

    @staticmethod
    @overload
    def shift_right_logical(value: System.Numerics.Vector[System.UIntPtr], shift_count: int) -> System.Numerics.Vector[System.UIntPtr]:
        """
        Shifts (unsigned) each element of a vector right by the specified amount.
        
        :param value: The vector whose elements are to be shifted.
        :param shift_count: The number of bits by which to shift each element.
        :returns: A vector whose elements where shifted right by .
        """
        ...

    @staticmethod
    def sin(vector: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @staticmethod
    def sin_cos(vector: System.Numerics.Vector[float]) -> System.ValueTuple[System.Numerics.Vector[float], System.Numerics.Vector[float]]:
        ...

    @staticmethod
    @overload
    def store(source: System.Numerics.Vector4, destination: typing.Any) -> None:
        """
        Stores a vector at the given destination.
        
        :param source: The vector that will be stored.
        :param destination: The destination at which  will be stored.
        """
        ...

    @staticmethod
    @overload
    def store(source: System.Numerics.Vector2, destination: typing.Any) -> None:
        """
        Stores a vector at the given destination.
        
        :param source: The vector that will be stored.
        :param destination: The destination at which  will be stored.
        """
        ...

    @staticmethod
    @overload
    def store(source: System.Numerics.Vector3, destination: typing.Any) -> None:
        """
        Stores a vector at the given destination.
        
        :param source: The vector that will be stored.
        :param destination: The destination at which  will be stored.
        """
        ...

    @staticmethod
    @overload
    def store_aligned(source: System.Numerics.Vector4, destination: typing.Any) -> None:
        """
        Stores a vector at the given 16-byte aligned destination.
        
        :param source: The vector that will be stored.
        :param destination: The aligned destination at which  will be stored.
        """
        ...

    @staticmethod
    @overload
    def store_aligned(source: System.Numerics.Vector2, destination: typing.Any) -> None:
        """
        Stores a vector at the given 8-byte aligned destination.
        
        :param source: The vector that will be stored.
        :param destination: The aligned destination at which  will be stored.
        """
        ...

    @staticmethod
    @overload
    def store_aligned(source: System.Numerics.Vector3, destination: typing.Any) -> None:
        """
        Stores a vector at the given 8-byte aligned destination.
        
        :param source: The vector that will be stored.
        :param destination: The aligned destination at which  will be stored.
        """
        ...

    @staticmethod
    @overload
    def store_aligned_non_temporal(source: System.Numerics.Vector4, destination: typing.Any) -> None:
        """
        Stores a vector at the given 16-byte aligned destination.
        
        :param source: The vector that will be stored.
        :param destination: The aligned destination at which  will be stored.
        """
        ...

    @staticmethod
    @overload
    def store_aligned_non_temporal(source: System.Numerics.Vector2, destination: typing.Any) -> None:
        """
        Stores a vector at the given 8-byte aligned destination.
        
        :param source: The vector that will be stored.
        :param destination: The aligned destination at which  will be stored.
        """
        ...

    @staticmethod
    @overload
    def store_aligned_non_temporal(source: System.Numerics.Vector3, destination: typing.Any) -> None:
        """
        Stores a vector at the given 8-byte aligned destination.
        
        :param source: The vector that will be stored.
        :param destination: The aligned destination at which  will be stored.
        """
        ...

    @staticmethod
    @overload
    def store_unsafe(source: System.Numerics.Vector4, destination: float) -> None:
        """
        Stores a vector at the given destination.
        
        :param source: The vector that will be stored.
        :param destination: The destination at which  will be stored.
        """
        ...

    @staticmethod
    @overload
    def store_unsafe(source: System.Numerics.Vector4, destination: float, element_offset: System.UIntPtr) -> None:
        """
        Stores a vector at the given destination.
        
        :param source: The vector that will be stored.
        :param destination: The destination to which  will be added before the vector will be stored.
        :param element_offset: The element offset from  from which the vector will be stored.
        """
        ...

    @staticmethod
    @overload
    def store_unsafe(source: System.Numerics.Vector2, destination: float) -> None:
        """
        Stores a vector at the given destination.
        
        :param source: The vector that will be stored.
        :param destination: The destination at which  will be stored.
        """
        ...

    @staticmethod
    @overload
    def store_unsafe(source: System.Numerics.Vector2, destination: float, element_offset: System.UIntPtr) -> None:
        """
        Stores a vector at the given destination.
        
        :param source: The vector that will be stored.
        :param destination: The destination to which  will be added before the vector will be stored.
        :param element_offset: The element offset from  from which the vector will be stored.
        """
        ...

    @staticmethod
    @overload
    def store_unsafe(source: System.Numerics.Vector3, destination: float) -> None:
        """
        Stores a vector at the given destination.
        
        :param source: The vector that will be stored.
        :param destination: The destination at which  will be stored.
        """
        ...

    @staticmethod
    @overload
    def store_unsafe(source: System.Numerics.Vector3, destination: float, element_offset: System.UIntPtr) -> None:
        """
        Stores a vector at the given destination.
        
        :param source: The vector that will be stored.
        :param destination: The destination to which  will be added before the vector will be stored.
        :param element_offset: The element offset from  from which the vector will be stored.
        """
        ...

    @staticmethod
    @overload
    def to_scalar(vector: System.Numerics.Vector4) -> float:
        ...

    @staticmethod
    @overload
    def to_scalar(vector: System.Numerics.Vector2) -> float:
        ...

    @staticmethod
    @overload
    def to_scalar(vector: System.Numerics.Vector3) -> float:
        ...

    @overload
    def to_string(self) -> str:
        """
        Returns a String representing this vector.
        
        :returns: The string representation.
        """
        ...

    @overload
    def to_string(self, format: str) -> str:
        """
        Returns a String representing this vector, using the specified format string to format individual elements.
        
        :param format: The format of individual elements.
        :returns: The string representation.
        """
        ...

    @overload
    def to_string(self, format: str, format_provider: System.IFormatProvider) -> str:
        """
        Returns a String representing this vector, using the specified format string to format individual elements and the given IFormatProvider.
        
        :param format: The format of individual elements.
        :param format_provider: The format provider to use when formatting elements.
        :returns: The string representation.
        """
        ...

    @staticmethod
    def truncate(vector: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        ...

    @overload
    def try_copy_to(self, destination: System.Span[int]) -> bool:
        """
        Tries to copy a Vector{T} to a given span.
        
        :param destination: The span to which the current instance is copied.
        :returns: true if the current instance was successfully copied to ; otherwise, false if the length of  is less than sizeof().
        """
        ...

    @overload
    def try_copy_to(self, destination: System.Span[System_Numerics_Vector_T]) -> bool:
        """
        Tries to copy a Vector{T} to a given span.
        
        :param destination: The span to which the current instance is copied.
        :returns: true if the current instance was successfully copied to ; otherwise, false if the length of  is less than Vector{T}.Count.
        """
        ...

    @staticmethod
    @overload
    def widen(source: System.Numerics.Vector[int], low: typing.Optional[System.Numerics.Vector[int]], high: typing.Optional[System.Numerics.Vector[int]]) -> typing.Tuple[None, System.Numerics.Vector[int], System.Numerics.Vector[int]]:
        """
        Widens a Vector<Byte> into two Vector{UInt16} .
        
        :param source: The vector whose elements are to be widened.
        :param low: A vector that will contain the widened result of the lower half of .
        :param high: A vector that will contain the widened result of the upper half of .
        """
        ...

    @staticmethod
    @overload
    def widen(source: System.Numerics.Vector[float], low: typing.Optional[System.Numerics.Vector[float]], high: typing.Optional[System.Numerics.Vector[float]]) -> typing.Tuple[None, System.Numerics.Vector[float], System.Numerics.Vector[float]]:
        """
        Widens a Vector<Single> into two Vector{Double} .
        
        :param source: The vector whose elements are to be widened.
        :param low: A vector that will contain the widened result of the lower half of .
        :param high: A vector that will contain the widened result of the upper half of .
        """
        ...

    @staticmethod
    @overload
    def widen_lower(source: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """
        Widens the lower half of a Vector<Byte> into a Vector{UInt16} .
        
        :param source: The vector whose elements are to be widened.
        :returns: A vector that contain the widened lower half of .
        """
        ...

    @staticmethod
    @overload
    def widen_lower(source: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        """
        Widens the lower half of a Vector<Single> into a Vector{Double} .
        
        :param source: The vector whose elements are to be widened.
        :returns: A vector that contain the widened lower half of .
        """
        ...

    @staticmethod
    @overload
    def widen_upper(source: System.Numerics.Vector[int]) -> System.Numerics.Vector[int]:
        """
        Widens the upper half of a Vector<Byte> into a Vector{UInt16} .
        
        :param source: The vector whose elements are to be widened.
        :returns: A vector that contain the widened upper half of .
        """
        ...

    @staticmethod
    @overload
    def widen_upper(source: System.Numerics.Vector[float]) -> System.Numerics.Vector[float]:
        """
        Widens the upper half of a Vector<Single> into a Vector{Double} .
        
        :param source: The vector whose elements are to be widened.
        :returns: A vector that contain the widened upper half of .
        """
        ...

    @staticmethod
    @overload
    def with_element(vector: System.Numerics.Vector4, index: int, value: float) -> System.Numerics.Vector4:
        ...

    @staticmethod
    @overload
    def with_element(vector: System.Numerics.Vector2, index: int, value: float) -> System.Numerics.Vector2:
        ...

    @staticmethod
    @overload
    def with_element(vector: System.Numerics.Vector3, index: int, value: float) -> System.Numerics.Vector3:
        ...


class IUnaryNegationOperators(typing.Generic[System_Numerics_IUnaryNegationOperators_TSelf, System_Numerics_IUnaryNegationOperators_TResult], metaclass=abc.ABCMeta):
    """Defines a mechanism for computing the unary negation of a value."""


class IRootFunctions(typing.Generic[System_Numerics_IRootFunctions_TSelf], System.Numerics.IFloatingPointConstants[System_Numerics_IRootFunctions_TSelf], metaclass=abc.ABCMeta):
    """Defines support for root functions."""


class IBinaryFloatingPointIeee754(typing.Generic[System_Numerics_IBinaryFloatingPointIeee754_TSelf], System.Numerics.IBinaryNumber[System_Numerics_IBinaryFloatingPointIeee754_TSelf], System.Numerics.IFloatingPointIeee754[System_Numerics_IBinaryFloatingPointIeee754_TSelf], metaclass=abc.ABCMeta):
    """Defines an IEEE 754 floating-point type that is represented in a base-2 format."""


class ISubtractionOperators(typing.Generic[System_Numerics_ISubtractionOperators_TSelf, System_Numerics_ISubtractionOperators_TOther, System_Numerics_ISubtractionOperators_TResult], metaclass=abc.ABCMeta):
    """Defines a mechanism for computing the difference of two values."""


class IFloatingPoint(typing.Generic[System_Numerics_IFloatingPoint_TSelf], System.Numerics.IFloatingPointConstants[System_Numerics_IFloatingPoint_TSelf], System.Numerics.INumber[System_Numerics_IFloatingPoint_TSelf], System.Numerics.ISignedNumber[System_Numerics_IFloatingPoint_TSelf], metaclass=abc.ABCMeta):
    """Defines a floating-point type."""

    def get_exponent_byte_count(self) -> int:
        """
        Gets the number of bytes that will be written as part of TryWriteExponentLittleEndian(Span{byte}, out int).
        
        :returns: The number of bytes that will be written as part of TryWriteExponentLittleEndian(Span{byte}, out int).
        """
        ...

    def get_exponent_shortest_bit_length(self) -> int:
        """
        Gets the length, in bits, of the shortest two's complement representation of the current exponent.
        
        :returns: The length, in bits, of the shortest two's complement representation of the current exponent.
        """
        ...

    def get_significand_bit_length(self) -> int:
        """
        Gets the length, in bits, of the current significand.
        
        :returns: The length, in bits, of the current significand.
        """
        ...

    def get_significand_byte_count(self) -> int:
        """
        Gets the number of bytes that will be written as part of TryWriteSignificandLittleEndian(Span{byte}, out int).
        
        :returns: The number of bytes that will be written as part of TryWriteSignificandLittleEndian(Span{byte}, out int).
        """
        ...

    def try_write_exponent_big_endian(self, destination: System.Span[int], bytes_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        """
        Tries to write the current exponent, in big-endian format, to a given span.
        
        :param destination: The span to which the current exponent should be written.
        :param bytes_written: The number of bytes written to .
        :returns: true if the exponent was successfully written to ; otherwise, false.
        """
        ...

    def try_write_exponent_little_endian(self, destination: System.Span[int], bytes_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        """
        Tries to write the current exponent, in little-endian format, to a given span.
        
        :param destination: The span to which the current exponent should be written.
        :param bytes_written: The number of bytes written to .
        :returns: true if the exponent was successfully written to ; otherwise, false.
        """
        ...

    def try_write_significand_big_endian(self, destination: System.Span[int], bytes_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        """
        Tries to write the current significand, in big-endian format, to a given span.
        
        :param destination: The span to which the current significand should be written.
        :param bytes_written: The number of bytes written to .
        :returns: true if the significand was successfully written to ; otherwise, false.
        """
        ...

    def try_write_significand_little_endian(self, destination: System.Span[int], bytes_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        """
        Tries to write the current significand, in little-endian format, to a given span.
        
        :param destination: The span to which the current significand should be written.
        :param bytes_written: The number of bytes written to .
        :returns: true if the significand was successfully written to ; otherwise, false.
        """
        ...

    @overload
    def write_exponent_big_endian(self, destination: typing.List[int]) -> int:
        """
        Writes the current exponent, in big-endian format, to a given array.
        
        :param destination: The array to which the current exponent should be written.
        :returns: The number of bytes written to .
        """
        ...

    @overload
    def write_exponent_big_endian(self, destination: typing.List[int], start_index: int) -> int:
        """
        Writes the current exponent, in big-endian format, to a given array.
        
        :param destination: The array to which the current exponent should be written.
        :param start_index: The starting index at which the exponent should be written.
        :returns: The number of bytes written to  starting at .
        """
        ...

    @overload
    def write_exponent_big_endian(self, destination: System.Span[int]) -> int:
        """
        Writes the current exponent, in big-endian format, to a given span.
        
        :param destination: The span to which the current exponent should be written.
        :returns: The number of bytes written to .
        """
        ...

    @overload
    def write_exponent_little_endian(self, destination: typing.List[int]) -> int:
        """
        Writes the current exponent, in little-endian format, to a given array.
        
        :param destination: The array to which the current exponent should be written.
        :returns: The number of bytes written to .
        """
        ...

    @overload
    def write_exponent_little_endian(self, destination: typing.List[int], start_index: int) -> int:
        """
        Writes the current exponent, in little-endian format, to a given array.
        
        :param destination: The array to which the current exponent should be written.
        :param start_index: The starting index at which the exponent should be written.
        :returns: The number of bytes written to  starting at .
        """
        ...

    @overload
    def write_exponent_little_endian(self, destination: System.Span[int]) -> int:
        """
        Writes the current exponent, in little-endian format, to a given span.
        
        :param destination: The span to which the current exponent should be written.
        :returns: The number of bytes written to .
        """
        ...

    @overload
    def write_significand_big_endian(self, destination: typing.List[int]) -> int:
        """
        Writes the current significand, in big-endian format, to a given array.
        
        :param destination: The array to which the current significand should be written.
        :returns: The number of bytes written to .
        """
        ...

    @overload
    def write_significand_big_endian(self, destination: typing.List[int], start_index: int) -> int:
        """
        Writes the current significand, in big-endian format, to a given array.
        
        :param destination: The array to which the current significand should be written.
        :param start_index: The starting index at which the significand should be written.
        :returns: The number of bytes written to  starting at .
        """
        ...

    @overload
    def write_significand_big_endian(self, destination: System.Span[int]) -> int:
        """
        Writes the current significand, in big-endian format, to a given span.
        
        :param destination: The span to which the current significand should be written.
        :returns: The number of bytes written to .
        """
        ...

    @overload
    def write_significand_little_endian(self, destination: typing.List[int]) -> int:
        """
        Writes the current significand, in little-endian format, to a given array.
        
        :param destination: The array to which the current significand should be written.
        :returns: The number of bytes written to .
        """
        ...

    @overload
    def write_significand_little_endian(self, destination: typing.List[int], start_index: int) -> int:
        """
        Writes the current significand, in little-endian format, to a given array.
        
        :param destination: The array to which the current significand should be written.
        :param start_index: The starting index at which the significand should be written.
        :returns: The number of bytes written to  starting at .
        """
        ...

    @overload
    def write_significand_little_endian(self, destination: System.Span[int]) -> int:
        """
        Writes the current significand, in little-endian format, to a given span.
        
        :param destination: The span to which the current significand should be written.
        :returns: The number of bytes written to .
        """
        ...


class IUnaryPlusOperators(typing.Generic[System_Numerics_IUnaryPlusOperators_TSelf, System_Numerics_IUnaryPlusOperators_TResult], metaclass=abc.ABCMeta):
    """Defines a mechanism for computing the unary plus of a value."""


class IDecrementOperators(typing.Generic[System_Numerics_IDecrementOperators_TSelf], metaclass=abc.ABCMeta):
    """Defines a mechanism for decrementing a given value."""


class TotalOrderIeee754Comparer(typing.Generic[System_Numerics_TotalOrderIeee754Comparer_T], System.Collections.Generic.IComparer[System_Numerics_TotalOrderIeee754Comparer_T], System.Collections.Generic.IEqualityComparer[System_Numerics_TotalOrderIeee754Comparer_T], System.IEquatable[System_Numerics_TotalOrderIeee754Comparer]):
    """
    Represents a comparison operation that compares floating-point numbers
    with IEEE 754 totalOrder semantic.
    """

    def compare(self, x: System_Numerics_TotalOrderIeee754Comparer_T, y: System_Numerics_TotalOrderIeee754Comparer_T) -> int:
        """
        Compares two numbers with IEEE 754 totalOrder semantic and returns
        a value indicating whether one is less than, equal to, or greater than the other.
        
        :param x: The first number to compare.
        :param y: The second number to compare.
        :returns: A signed integer that indicates the relative values of  and , as shown in the following table.  Value Meaning Less than zero is less than  Zero equals  Greater than zero is greater than.
        """
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        """
        Determines whether this instance and a specified object are equal.
        
        :param obj: The object to compare with the current instance.
        :returns: true if the current instance and  are equal; otherwise, false. If  is null, the method returns false.
        """
        ...

    @overload
    def equals(self, x: System_Numerics_TotalOrderIeee754Comparer_T, y: System_Numerics_TotalOrderIeee754Comparer_T) -> bool:
        """
        Determines whether the specified numbers are equal.
        
        :param x: The first number of type T to compare.
        :param y: The second number of type T to compare.
        :returns: true if the specified numbers are equal; otherwise, false.
        """
        ...

    @overload
    def equals(self, other: System.Numerics.TotalOrderIeee754Comparer[System_Numerics_TotalOrderIeee754Comparer_T]) -> bool:
        ...

    @overload
    def get_hash_code(self, obj: System_Numerics_TotalOrderIeee754Comparer_T) -> int:
        """
        Returns a hash code for the specified number.
        
        :param obj: The number for which a hash code is to be returned.
        :returns: A hash code for the specified number.
        """
        ...

    @overload
    def get_hash_code(self) -> int:
        """
        Returns the hash code for this instance.
        
        :returns: The hash code.
        """
        ...


class ITrigonometricFunctions(typing.Generic[System_Numerics_ITrigonometricFunctions_TSelf], System.Numerics.IFloatingPointConstants[System_Numerics_ITrigonometricFunctions_TSelf], metaclass=abc.ABCMeta):
    """Defines support for trigonometric functions."""


class IMinMaxValue(typing.Generic[System_Numerics_IMinMaxValue_TSelf], metaclass=abc.ABCMeta):
    """Defines a mechanism for getting the minimum and maximum value of a type."""


class IEqualityOperators(typing.Generic[System_Numerics_IEqualityOperators_TSelf, System_Numerics_IEqualityOperators_TOther, System_Numerics_IEqualityOperators_TResult], metaclass=abc.ABCMeta):
    """Defines a mechanism for comparing two values to determine equality."""


class IDivisionOperators(typing.Generic[System_Numerics_IDivisionOperators_TSelf, System_Numerics_IDivisionOperators_TOther, System_Numerics_IDivisionOperators_TResult], metaclass=abc.ABCMeta):
    """Defines a mechanism for computing the quotient of two values."""


class IIncrementOperators(typing.Generic[System_Numerics_IIncrementOperators_TSelf], metaclass=abc.ABCMeta):
    """Defines a mechanism for incrementing a given value."""


class BitOperations(System.Object):
    """
    Utility methods for intrinsic bit-twiddling operations.
    The methods use hardware intrinsics when available on the underlying platform,
    otherwise they use optimized software fallbacks.
    """

    @staticmethod
    def crc_32c(crc: int, data: int) -> int:
        """
        Accumulates the CRC (Cyclic redundancy check) checksum.
        
        :param crc: The base value to calculate checksum on
        :param data: The data for which to compute the checksum
        :returns: The CRC-checksum.
        """
        ...

    @staticmethod
    @overload
    def is_pow_2(value: int) -> bool:
        """
        Evaluate whether a given integral value is a power of 2.
        
        :param value: The value.
        """
        ...

    @staticmethod
    @overload
    def is_pow_2(value: System.IntPtr) -> bool:
        """
        Evaluate whether a given integral value is a power of 2.
        
        :param value: The value.
        """
        ...

    @staticmethod
    @overload
    def is_pow_2(value: System.UIntPtr) -> bool:
        """
        Evaluate whether a given integral value is a power of 2.
        
        :param value: The value.
        """
        ...

    @staticmethod
    @overload
    def leading_zero_count(value: int) -> int:
        """
        Count the number of leading zero bits in a mask.
        Similar in behavior to the x86 instruction LZCNT.
        
        :param value: The value.
        """
        ...

    @staticmethod
    @overload
    def leading_zero_count(value: System.UIntPtr) -> int:
        """
        Count the number of leading zero bits in a mask.
        Similar in behavior to the x86 instruction LZCNT.
        
        :param value: The value.
        """
        ...

    @staticmethod
    @overload
    def log_2(value: int) -> int:
        """
        Returns the integer (floor) log of the specified value, base 2.
        Note that by convention, input value 0 returns 0 since log(0) is undefined.
        
        :param value: The value.
        """
        ...

    @staticmethod
    @overload
    def log_2(value: System.UIntPtr) -> int:
        """
        Returns the integer (floor) log of the specified value, base 2.
        Note that by convention, input value 0 returns 0 since log(0) is undefined.
        
        :param value: The value.
        """
        ...

    @staticmethod
    @overload
    def pop_count(value: int) -> int:
        """
        Returns the population count (number of bits set) of a mask.
        Similar in behavior to the x86 instruction POPCNT.
        
        :param value: The value.
        """
        ...

    @staticmethod
    @overload
    def pop_count(value: System.UIntPtr) -> int:
        """
        Returns the population count (number of bits set) of a mask.
        Similar in behavior to the x86 instruction POPCNT.
        
        :param value: The value.
        """
        ...

    @staticmethod
    @overload
    def rotate_left(value: int, offset: int) -> int:
        """
        Rotates the specified value left by the specified number of bits.
        Similar in behavior to the x86 instruction ROL.
        
        :param value: The value to rotate.
        :param offset: The number of bits to rotate by. Any value outside the range [0..31] is treated as congruent mod 32.
        :returns: The rotated value.
        """
        ...

    @staticmethod
    @overload
    def rotate_left(value: System.UIntPtr, offset: int) -> System.UIntPtr:
        """
        Rotates the specified value left by the specified number of bits.
        Similar in behavior to the x86 instruction ROL.
        
        :param value: The value to rotate.
        :param offset: The number of bits to rotate by. Any value outside the range [0..31] is treated as congruent mod 32 on a 32-bit process, and any value outside the range [0..63] is treated as congruent mod 64 on a 64-bit process.
        :returns: The rotated value.
        """
        ...

    @staticmethod
    @overload
    def rotate_right(value: int, offset: int) -> int:
        """
        Rotates the specified value right by the specified number of bits.
        Similar in behavior to the x86 instruction ROR.
        
        :param value: The value to rotate.
        :param offset: The number of bits to rotate by. Any value outside the range [0..31] is treated as congruent mod 32.
        :returns: The rotated value.
        """
        ...

    @staticmethod
    @overload
    def rotate_right(value: System.UIntPtr, offset: int) -> System.UIntPtr:
        """
        Rotates the specified value right by the specified number of bits.
        Similar in behavior to the x86 instruction ROR.
        
        :param value: The value to rotate.
        :param offset: The number of bits to rotate by. Any value outside the range [0..31] is treated as congruent mod 32 on a 32-bit process, and any value outside the range [0..63] is treated as congruent mod 64 on a 64-bit process.
        :returns: The rotated value.
        """
        ...

    @staticmethod
    @overload
    def round_up_to_power_of_2(value: int) -> int:
        """
        Round the given integral value up to a power of 2.
        
        :param value: The value.
        :returns: The smallest power of 2 which is greater than or equal to . If  is 0 or the result overflows, returns 0.
        """
        ...

    @staticmethod
    @overload
    def round_up_to_power_of_2(value: System.UIntPtr) -> System.UIntPtr:
        """
        Round the given integral value up to a power of 2.
        
        :param value: The value.
        :returns: The smallest power of 2 which is greater than or equal to . If  is 0 or the result overflows, returns 0.
        """
        ...

    @staticmethod
    @overload
    def trailing_zero_count(value: int) -> int:
        """
        Count the number of trailing zero bits in an integer value.
        Similar in behavior to the x86 instruction TZCNT.
        
        :param value: The value.
        """
        ...

    @staticmethod
    @overload
    def trailing_zero_count(value: System.IntPtr) -> int:
        """
        Count the number of trailing zero bits in a mask.
        Similar in behavior to the x86 instruction TZCNT.
        
        :param value: The value.
        """
        ...

    @staticmethod
    @overload
    def trailing_zero_count(value: System.UIntPtr) -> int:
        """
        Count the number of trailing zero bits in a mask.
        Similar in behavior to the x86 instruction TZCNT.
        
        :param value: The value.
        """
        ...


class IModulusOperators(typing.Generic[System_Numerics_IModulusOperators_TSelf, System_Numerics_IModulusOperators_TOther, System_Numerics_IModulusOperators_TResult], metaclass=abc.ABCMeta):
    """Defines a mechanism for computing the modulus or remainder of two values."""


class ISignedNumber(typing.Generic[System_Numerics_ISignedNumber_TSelf], System.Numerics.INumberBase[System_Numerics_ISignedNumber_TSelf], metaclass=abc.ABCMeta):
    """Defines a number type which can represent both positive and negative values."""


class IAdditionOperators(typing.Generic[System_Numerics_IAdditionOperators_TSelf, System_Numerics_IAdditionOperators_TOther, System_Numerics_IAdditionOperators_TResult], metaclass=abc.ABCMeta):
    """Defines a mechanism for computing the sum of two values."""


class IBitwiseOperators(typing.Generic[System_Numerics_IBitwiseOperators_TSelf, System_Numerics_IBitwiseOperators_TOther, System_Numerics_IBitwiseOperators_TResult], metaclass=abc.ABCMeta):
    """Defines a mechanism for performing bitwise operations over two values."""


class IBinaryInteger(typing.Generic[System_Numerics_IBinaryInteger_TSelf], System.Numerics.IBinaryNumber[System_Numerics_IBinaryInteger_TSelf], System.Numerics.IShiftOperators[System_Numerics_IBinaryInteger_TSelf, int, System_Numerics_IBinaryInteger_TSelf], metaclass=abc.ABCMeta):
    """Defines an integer type that is represented in a base-2 format."""

    def get_byte_count(self) -> int:
        """
        Gets the number of bytes that will be written as part of TryWriteLittleEndian(Span{byte}, out int).
        
        :returns: The number of bytes that will be written as part of TryWriteLittleEndian(Span{byte}, out int).
        """
        ...

    def get_shortest_bit_length(self) -> int:
        """
        Gets the length, in bits, of the shortest two's complement representation of the current value.
        
        :returns: The length, in bits, of the shortest two's complement representation of the current value.
        """
        ...

    def try_write_big_endian(self, destination: System.Span[int], bytes_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        """
        Tries to write the current value, in big-endian format, to a given span.
        
        :param destination: The span to which the current value should be written.
        :param bytes_written: The number of bytes written to .
        :returns: true if the value was successfully written to ; otherwise, false.
        """
        ...

    def try_write_little_endian(self, destination: System.Span[int], bytes_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        """
        Tries to write the current value, in little-endian format, to a given span.
        
        :param destination: The span to which the current value should be written.
        :param bytes_written: The number of bytes written to .
        :returns: true if the value was successfully written to ; otherwise, false.
        """
        ...

    @overload
    def write_big_endian(self, destination: typing.List[int]) -> int:
        """
        Writes the current value, in big-endian format, to a given array.
        
        :param destination: The array to which the current value should be written.
        :returns: The number of bytes written to .
        """
        ...

    @overload
    def write_big_endian(self, destination: typing.List[int], start_index: int) -> int:
        """
        Writes the current value, in big-endian format, to a given array.
        
        :param destination: The array to which the current value should be written.
        :param start_index: The starting index at which the value should be written.
        :returns: The number of bytes written to  starting at .
        """
        ...

    @overload
    def write_big_endian(self, destination: System.Span[int]) -> int:
        """
        Writes the current value, in big-endian format, to a given span.
        
        :param destination: The span to which the current value should be written.
        :returns: The number of bytes written to .
        """
        ...

    @overload
    def write_little_endian(self, destination: typing.List[int]) -> int:
        """
        Writes the current value, in little-endian format, to a given array.
        
        :param destination: The array to which the current value should be written.
        :returns: The number of bytes written to .
        """
        ...

    @overload
    def write_little_endian(self, destination: typing.List[int], start_index: int) -> int:
        """
        Writes the current value, in little-endian format, to a given array.
        
        :param destination: The array to which the current value should be written.
        :param start_index: The starting index at which the value should be written.
        :returns: The number of bytes written to  starting at .
        """
        ...

    @overload
    def write_little_endian(self, destination: System.Span[int]) -> int:
        """
        Writes the current value, in little-endian format, to a given span.
        
        :param destination: The span to which the current value should be written.
        :returns: The number of bytes written to .
        """
        ...


class ILogarithmicFunctions(typing.Generic[System_Numerics_ILogarithmicFunctions_TSelf], System.Numerics.IFloatingPointConstants[System_Numerics_ILogarithmicFunctions_TSelf], metaclass=abc.ABCMeta):
    """Defines support for logarithmic functions."""


class IUnsignedNumber(typing.Generic[System_Numerics_IUnsignedNumber_TSelf], System.Numerics.INumberBase[System_Numerics_IUnsignedNumber_TSelf], metaclass=abc.ABCMeta):
    """Defines a number type which can only represent positive values, that is it cannot represent negative values."""


class IBinaryNumber(typing.Generic[System_Numerics_IBinaryNumber_TSelf], System.Numerics.IBitwiseOperators[System_Numerics_IBinaryNumber_TSelf, System_Numerics_IBinaryNumber_TSelf, System_Numerics_IBinaryNumber_TSelf], System.Numerics.INumber[System_Numerics_IBinaryNumber_TSelf], metaclass=abc.ABCMeta):
    """Defines a number that is represented in a base-2 format."""


class INumber(typing.Generic[System_Numerics_INumber_TSelf], System.IComparable[System_Numerics_INumber_TSelf], System.Numerics.IComparisonOperators[System_Numerics_INumber_TSelf, System_Numerics_INumber_TSelf, bool], System.Numerics.IModulusOperators[System_Numerics_INumber_TSelf, System_Numerics_INumber_TSelf, System_Numerics_INumber_TSelf], System.Numerics.INumberBase[System_Numerics_INumber_TSelf], metaclass=abc.ABCMeta):
    """Defines a number type."""


class IMultiplicativeIdentity(typing.Generic[System_Numerics_IMultiplicativeIdentity_TSelf, System_Numerics_IMultiplicativeIdentity_TResult], metaclass=abc.ABCMeta):
    """Defines a mechanism for getting the multiplicative identity of a given type."""


class IShiftOperators(typing.Generic[System_Numerics_IShiftOperators_TSelf, System_Numerics_IShiftOperators_TOther, System_Numerics_IShiftOperators_TResult], metaclass=abc.ABCMeta):
    """Defines a mechanism for shifting a value by another value."""


class IPowerFunctions(typing.Generic[System_Numerics_IPowerFunctions_TSelf], System.Numerics.INumberBase[System_Numerics_IPowerFunctions_TSelf], metaclass=abc.ABCMeta):
    """Defines support for power functions."""


class IHyperbolicFunctions(typing.Generic[System_Numerics_IHyperbolicFunctions_TSelf], System.Numerics.IFloatingPointConstants[System_Numerics_IHyperbolicFunctions_TSelf], metaclass=abc.ABCMeta):
    """Defines support for hyperbolic functions."""


class IFloatingPointIeee754(typing.Generic[System_Numerics_IFloatingPointIeee754_TSelf], System.Numerics.IExponentialFunctions[System_Numerics_IFloatingPointIeee754_TSelf], System.Numerics.IFloatingPoint[System_Numerics_IFloatingPointIeee754_TSelf], System.Numerics.IHyperbolicFunctions[System_Numerics_IFloatingPointIeee754_TSelf], System.Numerics.ILogarithmicFunctions[System_Numerics_IFloatingPointIeee754_TSelf], System.Numerics.IPowerFunctions[System_Numerics_IFloatingPointIeee754_TSelf], System.Numerics.IRootFunctions[System_Numerics_IFloatingPointIeee754_TSelf], System.Numerics.ITrigonometricFunctions[System_Numerics_IFloatingPointIeee754_TSelf], metaclass=abc.ABCMeta):
    """Defines an IEEE 754 floating-point type."""


class IComparisonOperators(typing.Generic[System_Numerics_IComparisonOperators_TSelf, System_Numerics_IComparisonOperators_TOther, System_Numerics_IComparisonOperators_TResult], System.Numerics.IEqualityOperators[System_Numerics_IComparisonOperators_TSelf, System_Numerics_IComparisonOperators_TOther, System_Numerics_IComparisonOperators_TResult], metaclass=abc.ABCMeta):
    """Defines a mechanism for comparing two values to determine relative order."""


class INumberBase(typing.Generic[System_Numerics_INumberBase_TSelf], System.Numerics.IAdditionOperators[System_Numerics_INumberBase_TSelf, System_Numerics_INumberBase_TSelf, System_Numerics_INumberBase_TSelf], System.Numerics.IAdditiveIdentity[System_Numerics_INumberBase_TSelf, System_Numerics_INumberBase_TSelf], System.Numerics.IDecrementOperators[System_Numerics_INumberBase_TSelf], System.Numerics.IDivisionOperators[System_Numerics_INumberBase_TSelf, System_Numerics_INumberBase_TSelf, System_Numerics_INumberBase_TSelf], System.IEquatable[System_Numerics_INumberBase_TSelf], System.Numerics.IEqualityOperators[System_Numerics_INumberBase_TSelf, System_Numerics_INumberBase_TSelf, bool], System.Numerics.IIncrementOperators[System_Numerics_INumberBase_TSelf], System.Numerics.IMultiplicativeIdentity[System_Numerics_INumberBase_TSelf, System_Numerics_INumberBase_TSelf], System.Numerics.IMultiplyOperators[System_Numerics_INumberBase_TSelf, System_Numerics_INumberBase_TSelf, System_Numerics_INumberBase_TSelf], System.ISpanFormattable, System.ISpanParsable[System_Numerics_INumberBase_TSelf], System.Numerics.ISubtractionOperators[System_Numerics_INumberBase_TSelf, System_Numerics_INumberBase_TSelf, System_Numerics_INumberBase_TSelf], System.Numerics.IUnaryPlusOperators[System_Numerics_INumberBase_TSelf, System_Numerics_INumberBase_TSelf], System.Numerics.IUnaryNegationOperators[System_Numerics_INumberBase_TSelf, System_Numerics_INumberBase_TSelf], System.IUtf8SpanFormattable, System.IUtf8SpanParsable[System_Numerics_INumberBase_TSelf], metaclass=abc.ABCMeta):
    """Defines the base of other number types."""

    def try_format(self, utf_8_destination: System.Span[int], bytes_written: typing.Optional[int], format: System.ReadOnlySpan[str], provider: System.IFormatProvider) -> typing.Tuple[bool, int]:
        ...


class IFloatingPointConstants(typing.Generic[System_Numerics_IFloatingPointConstants_TSelf], System.Numerics.INumberBase[System_Numerics_IFloatingPointConstants_TSelf], metaclass=abc.ABCMeta):
    """Defines support for floating-point constants."""


class IExponentialFunctions(typing.Generic[System_Numerics_IExponentialFunctions_TSelf], System.Numerics.IFloatingPointConstants[System_Numerics_IExponentialFunctions_TSelf], metaclass=abc.ABCMeta):
    """Defines support for exponential functions."""


class IAdditiveIdentity(typing.Generic[System_Numerics_IAdditiveIdentity_TSelf, System_Numerics_IAdditiveIdentity_TResult], metaclass=abc.ABCMeta):
    """Defines a mechanism for getting the additive identity of a given type."""


