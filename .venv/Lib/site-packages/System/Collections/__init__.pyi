from typing import overload
from enum import Enum
import abc
import typing
import warnings

import System
import System.Collections
import System.Globalization
import System.Runtime.Serialization


class IEnumerator(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def current(self) -> System.Object:
        ...

    def move_next(self) -> bool:
        ...

    def reset(self) -> None:
        ...


class IEnumerable(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def get_enumerator(self) -> System.Collections.IEnumerator:
        ...


class ICollection(System.Collections.IEnumerable, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def count(self) -> int:
        ...

    @property
    @abc.abstractmethod
    def sync_root(self) -> System.Object:
        ...

    @property
    @abc.abstractmethod
    def is_synchronized(self) -> bool:
        ...

    def copy_to(self, array: System.Array, index: int) -> None:
        ...


class IDictionary(System.Collections.ICollection, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def keys(self) -> System.Collections.ICollection:
        ...

    @property
    @abc.abstractmethod
    def values(self) -> System.Collections.ICollection:
        ...

    @property
    @abc.abstractmethod
    def is_read_only(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def is_fixed_size(self) -> bool:
        ...

    def __getitem__(self, key: typing.Any) -> typing.Any:
        ...

    def __setitem__(self, key: typing.Any, value: typing.Any) -> None:
        ...

    def add(self, key: typing.Any, value: typing.Any) -> None:
        ...

    def clear(self) -> None:
        ...

    def contains(self, key: typing.Any) -> bool:
        ...

    def remove(self, key: typing.Any) -> None:
        ...


class DictionaryEntry:
    """This class has no documentation."""

    @property
    def key(self) -> System.Object:
        ...

    @key.setter
    def key(self, value: System.Object) -> None:
        ...

    @property
    def value(self) -> System.Object:
        ...

    @value.setter
    def value(self, value: System.Object) -> None:
        ...

    def __init__(self, key: typing.Any, value: typing.Any) -> None:
        ...

    def deconstruct(self, key: typing.Optional[typing.Any], value: typing.Optional[typing.Any]) -> typing.Tuple[None, typing.Any, typing.Any]:
        ...

    def to_string(self) -> str:
        ...


class IDictionaryEnumerator(System.Collections.IEnumerator, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def key(self) -> System.Object:
        ...

    @property
    @abc.abstractmethod
    def value(self) -> System.Object:
        ...

    @property
    @abc.abstractmethod
    def entry(self) -> System.Collections.DictionaryEntry:
        ...


class ListDictionaryInternal(System.Object, System.Collections.IDictionary):
    """
    Implements IDictionary using a singly linked list.
    Recommended for collections that typically include fewer than 10 items.
    """

    @property
    def count(self) -> int:
        ...

    @property
    def keys(self) -> System.Collections.ICollection:
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

    @property
    def sync_root(self) -> System.Object:
        ...

    @property
    def values(self) -> System.Collections.ICollection:
        ...

    def __getitem__(self, key: typing.Any) -> typing.Any:
        ...

    def __init__(self) -> None:
        ...

    def __setitem__(self, key: typing.Any, value: typing.Any) -> None:
        ...

    def add(self, key: typing.Any, value: typing.Any) -> None:
        ...

    def clear(self) -> None:
        ...

    def contains(self, key: typing.Any) -> bool:
        ...

    def copy_to(self, array: System.Array, index: int) -> None:
        ...

    def get_enumerator(self) -> System.Collections.IDictionaryEnumerator:
        ...

    def remove(self, key: typing.Any) -> None:
        ...


class IList(System.Collections.ICollection, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def is_read_only(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def is_fixed_size(self) -> bool:
        ...

    def __getitem__(self, index: int) -> typing.Any:
        ...

    def __setitem__(self, index: int, value: typing.Any) -> None:
        ...

    def add(self, value: typing.Any) -> int:
        ...

    def clear(self) -> None:
        ...

    def contains(self, value: typing.Any) -> bool:
        ...

    def index_of(self, value: typing.Any) -> int:
        ...

    def insert(self, index: int, value: typing.Any) -> None:
        ...

    def remove(self, value: typing.Any) -> None:
        ...

    def remove_at(self, index: int) -> None:
        ...


class IEqualityComparer(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def equals(self, x: typing.Any, y: typing.Any) -> bool:
        ...

    def get_hash_code(self, obj: typing.Any) -> int:
        ...


class IStructuralEquatable(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def equals(self, other: typing.Any, comparer: System.Collections.IEqualityComparer) -> bool:
        ...

    def get_hash_code(self, comparer: System.Collections.IEqualityComparer) -> int:
        ...


class IHashCodeProvider(metaclass=abc.ABCMeta):
    """
    Provides a mechanism for a Hashtable user to override the default
    GetHashCode() function on Objects, providing their own hash function.
    
    IHashCodeProvider has been deprecated. Use IEqualityComparer instead.
    """

    def get_hash_code(self, obj: typing.Any) -> int:
        """Returns a hash code for the given object."""
        ...


class IComparer(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def compare(self, x: typing.Any, y: typing.Any) -> int:
        ...


class ArrayList(System.Object, System.Collections.IList, System.ICloneable):
    """Implements the IList interface using an array whose size is dynamically increased as required."""

    @property
    def capacity(self) -> int:
        ...

    @capacity.setter
    def capacity(self, value: int) -> None:
        ...

    @property
    def count(self) -> int:
        ...

    @property
    def is_fixed_size(self) -> bool:
        ...

    @property
    def is_read_only(self) -> bool:
        ...

    @property
    def is_synchronized(self) -> bool:
        ...

    @property
    def sync_root(self) -> System.Object:
        ...

    def __getitem__(self, index: int) -> typing.Any:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, capacity: int) -> None:
        ...

    @overload
    def __init__(self, c: System.Collections.ICollection) -> None:
        ...

    def __setitem__(self, index: int, value: typing.Any) -> None:
        ...

    @staticmethod
    def adapter(list: System.Collections.IList) -> System.Collections.ArrayList:
        ...

    def add(self, value: typing.Any) -> int:
        ...

    def add_range(self, c: System.Collections.ICollection) -> None:
        ...

    @overload
    def binary_search(self, index: int, count: int, value: typing.Any, comparer: System.Collections.IComparer) -> int:
        ...

    @overload
    def binary_search(self, value: typing.Any) -> int:
        ...

    @overload
    def binary_search(self, value: typing.Any, comparer: System.Collections.IComparer) -> int:
        ...

    def clear(self) -> None:
        ...

    def clone(self) -> System.Object:
        ...

    def contains(self, item: typing.Any) -> bool:
        ...

    @overload
    def copy_to(self, array: System.Array) -> None:
        ...

    @overload
    def copy_to(self, array: System.Array, array_index: int) -> None:
        ...

    @overload
    def copy_to(self, index: int, array: System.Array, array_index: int, count: int) -> None:
        ...

    @staticmethod
    @overload
    def fixed_size(list: System.Collections.IList) -> System.Collections.IList:
        ...

    @staticmethod
    @overload
    def fixed_size(list: System.Collections.ArrayList) -> System.Collections.ArrayList:
        ...

    @overload
    def get_enumerator(self) -> System.Collections.IEnumerator:
        ...

    @overload
    def get_enumerator(self, index: int, count: int) -> System.Collections.IEnumerator:
        ...

    def get_range(self, index: int, count: int) -> System.Collections.ArrayList:
        ...

    @overload
    def index_of(self, value: typing.Any) -> int:
        ...

    @overload
    def index_of(self, value: typing.Any, start_index: int) -> int:
        ...

    @overload
    def index_of(self, value: typing.Any, start_index: int, count: int) -> int:
        ...

    def insert(self, index: int, value: typing.Any) -> None:
        ...

    def insert_range(self, index: int, c: System.Collections.ICollection) -> None:
        ...

    @overload
    def last_index_of(self, value: typing.Any) -> int:
        ...

    @overload
    def last_index_of(self, value: typing.Any, start_index: int) -> int:
        ...

    @overload
    def last_index_of(self, value: typing.Any, start_index: int, count: int) -> int:
        ...

    @staticmethod
    @overload
    def read_only(list: System.Collections.IList) -> System.Collections.IList:
        ...

    @staticmethod
    @overload
    def read_only(list: System.Collections.ArrayList) -> System.Collections.ArrayList:
        ...

    def remove(self, obj: typing.Any) -> None:
        ...

    def remove_at(self, index: int) -> None:
        ...

    def remove_range(self, index: int, count: int) -> None:
        ...

    @staticmethod
    def repeat(value: typing.Any, count: int) -> System.Collections.ArrayList:
        ...

    @overload
    def reverse(self) -> None:
        ...

    @overload
    def reverse(self, index: int, count: int) -> None:
        ...

    def set_range(self, index: int, c: System.Collections.ICollection) -> None:
        ...

    @overload
    def sort(self) -> None:
        ...

    @overload
    def sort(self, comparer: System.Collections.IComparer) -> None:
        ...

    @overload
    def sort(self, index: int, count: int, comparer: System.Collections.IComparer) -> None:
        ...

    @staticmethod
    @overload
    def synchronized(list: System.Collections.IList) -> System.Collections.IList:
        ...

    @staticmethod
    @overload
    def synchronized(list: System.Collections.ArrayList) -> System.Collections.ArrayList:
        ...

    @overload
    def to_array(self) -> typing.List[System.Object]:
        ...

    @overload
    def to_array(self, type: typing.Type) -> System.Array:
        ...

    def trim_to_size(self) -> None:
        ...


class IStructuralComparable(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def compare_to(self, other: typing.Any, comparer: System.Collections.IComparer) -> int:
        ...


class Hashtable(System.Object, System.Collections.IDictionary, System.Runtime.Serialization.ISerializable, System.Runtime.Serialization.IDeserializationCallback, System.ICloneable):
    """This class has no documentation."""

    @property
    def hcp(self) -> System.Collections.IHashCodeProvider:
        """
        This property is protected.
        
        Hashtable.hcp has been deprecated. Use the EqualityComparer property instead.
        """
        warnings.warn("Hashtable.hcp has been deprecated. Use the EqualityComparer property instead.", DeprecationWarning)

    @hcp.setter
    def hcp(self, value: System.Collections.IHashCodeProvider) -> None:
        warnings.warn("Hashtable.hcp has been deprecated. Use the EqualityComparer property instead.", DeprecationWarning)

    @property
    def comparer(self) -> System.Collections.IComparer:
        """
        This property is protected.
        
        Hashtable.comparer has been deprecated. Use the KeyComparer properties instead.
        """
        warnings.warn("Hashtable.comparer has been deprecated. Use the KeyComparer properties instead.", DeprecationWarning)

    @comparer.setter
    def comparer(self, value: System.Collections.IComparer) -> None:
        warnings.warn("Hashtable.comparer has been deprecated. Use the KeyComparer properties instead.", DeprecationWarning)

    @property
    def equality_comparer(self) -> System.Collections.IEqualityComparer:
        """This property is protected."""
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

    @property
    def keys(self) -> System.Collections.ICollection:
        ...

    @property
    def values(self) -> System.Collections.ICollection:
        ...

    @property
    def sync_root(self) -> System.Object:
        ...

    @property
    def count(self) -> int:
        ...

    def __contains__(self, key: typing.Any) -> bool:
        ...

    def __getitem__(self, key: typing.Any) -> typing.Any:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, capacity: int) -> None:
        ...

    @overload
    def __init__(self, capacity: int, load_factor: float) -> None:
        ...

    @overload
    def __init__(self, capacity: int, load_factor: float, equality_comparer: System.Collections.IEqualityComparer) -> None:
        ...

    @overload
    def __init__(self, equality_comparer: System.Collections.IEqualityComparer) -> None:
        ...

    @overload
    def __init__(self, capacity: int, equality_comparer: System.Collections.IEqualityComparer) -> None:
        ...

    @overload
    def __init__(self, d: System.Collections.IDictionary) -> None:
        ...

    @overload
    def __init__(self, d: System.Collections.IDictionary, load_factor: float) -> None:
        ...

    @overload
    def __init__(self, d: System.Collections.IDictionary, equality_comparer: System.Collections.IEqualityComparer) -> None:
        ...

    @overload
    def __init__(self, d: System.Collections.IDictionary, load_factor: float, equality_comparer: System.Collections.IEqualityComparer) -> None:
        ...

    @overload
    def __init__(self, hcp: System.Collections.IHashCodeProvider, comparer: System.Collections.IComparer) -> None:
        """This constructor has been deprecated. Use Hashtable(IEqualityComparer) instead."""
        ...

    @overload
    def __init__(self, capacity: int, hcp: System.Collections.IHashCodeProvider, comparer: System.Collections.IComparer) -> None:
        """This constructor has been deprecated. Use Hashtable(int, IEqualityComparer) instead."""
        ...

    @overload
    def __init__(self, d: System.Collections.IDictionary, hcp: System.Collections.IHashCodeProvider, comparer: System.Collections.IComparer) -> None:
        """This constructor has been deprecated. Use Hashtable(IDictionary, IEqualityComparer) instead."""
        ...

    @overload
    def __init__(self, capacity: int, load_factor: float, hcp: System.Collections.IHashCodeProvider, comparer: System.Collections.IComparer) -> None:
        """This constructor has been deprecated. Use Hashtable(int, float, IEqualityComparer) instead."""
        ...

    @overload
    def __init__(self, d: System.Collections.IDictionary, load_factor: float, hcp: System.Collections.IHashCodeProvider, comparer: System.Collections.IComparer) -> None:
        """This constructor has been deprecated. Use Hashtable(IDictionary, float, IEqualityComparer) instead."""
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """
        This method is protected.
        
        Obsoletions.LegacyFormatterImplMessage
        """
        ...

    def __len__(self) -> int:
        ...

    def __setitem__(self, key: typing.Any, value: typing.Any) -> None:
        ...

    def add(self, key: typing.Any, value: typing.Any) -> None:
        ...

    def clear(self) -> None:
        ...

    def clone(self) -> System.Object:
        ...

    def contains(self, key: typing.Any) -> bool:
        ...

    def contains_key(self, key: typing.Any) -> bool:
        ...

    def contains_value(self, value: typing.Any) -> bool:
        ...

    def copy_to(self, array: System.Array, array_index: int) -> None:
        ...

    def get_enumerator(self) -> System.Collections.IDictionaryEnumerator:
        ...

    def get_hash(self, key: typing.Any) -> int:
        """This method is protected."""
        ...

    def get_object_data(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """Obsoletions.LegacyFormatterImplMessage"""
        warnings.warn("Obsoletions.LegacyFormatterImplMessage", DeprecationWarning)

    def key_equals(self, item: typing.Any, key: typing.Any) -> bool:
        """This method is protected."""
        ...

    def on_deserialization(self, sender: typing.Any) -> None:
        ...

    def remove(self, key: typing.Any) -> None:
        ...

    @staticmethod
    def synchronized(table: System.Collections.Hashtable) -> System.Collections.Hashtable:
        ...


class Comparer(System.Object, System.Collections.IComparer, System.Runtime.Serialization.ISerializable):
    """Compares two objects for equivalence, where string comparisons are case-sensitive."""

    DEFAULT: System.Collections.Comparer = ...

    DEFAULT_INVARIANT: System.Collections.Comparer = ...

    def __init__(self, culture: System.Globalization.CultureInfo) -> None:
        ...

    def compare(self, a: typing.Any, b: typing.Any) -> int:
        ...

    def get_object_data(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """Obsoletions.LegacyFormatterImplMessage"""
        warnings.warn("Obsoletions.LegacyFormatterImplMessage", DeprecationWarning)


class BitArray(System.Object, System.Collections.ICollection, System.ICloneable):
    """This class has no documentation."""

    @property
    def length(self) -> int:
        ...

    @length.setter
    def length(self, value: int) -> None:
        ...

    @property
    def count(self) -> int:
        ...

    @property
    def sync_root(self) -> System.Object:
        ...

    @property
    def is_synchronized(self) -> bool:
        ...

    @property
    def is_read_only(self) -> bool:
        ...

    def __getitem__(self, index: int) -> bool:
        ...

    @overload
    def __init__(self, length: int) -> None:
        ...

    @overload
    def __init__(self, length: int, default_value: bool) -> None:
        ...

    @overload
    def __init__(self, bytes: typing.List[int]) -> None:
        ...

    @overload
    def __init__(self, values: typing.List[bool]) -> None:
        ...

    @overload
    def __init__(self, values: typing.List[int]) -> None:
        ...

    @overload
    def __init__(self, bits: System.Collections.BitArray) -> None:
        ...

    def __setitem__(self, index: int, value: bool) -> None:
        ...

    def And(self, value: System.Collections.BitArray) -> System.Collections.BitArray:
        ...

    def clone(self) -> System.Object:
        ...

    def copy_to(self, array: System.Array, index: int) -> None:
        ...

    def get(self, index: int) -> bool:
        ...

    def get_enumerator(self) -> System.Collections.IEnumerator:
        ...

    def has_all_set(self) -> bool:
        """
        Determines whether all bits in the BitArray are set to true.
        
        :returns: true if every bit in the BitArray is set to true, or if BitArray is empty; otherwise, false.
        """
        ...

    def has_any_set(self) -> bool:
        """
        Determines whether any bit in the BitArray is set to true.
        
        :returns: true if BitArray is not empty and at least one of its bit is set to true; otherwise, false.
        """
        ...

    def left_shift(self, count: int) -> System.Collections.BitArray:
        ...

    def Not(self) -> System.Collections.BitArray:
        ...

    def Or(self, value: System.Collections.BitArray) -> System.Collections.BitArray:
        ...

    def right_shift(self, count: int) -> System.Collections.BitArray:
        ...

    def set(self, index: int, value: bool) -> None:
        ...

    def set_all(self, value: bool) -> None:
        ...

    def xor(self, value: System.Collections.BitArray) -> System.Collections.BitArray:
        ...


class StructuralComparisons(System.Object):
    """This class has no documentation."""

    STRUCTURAL_COMPARER: System.Collections.IComparer

    STRUCTURAL_EQUALITY_COMPARER: System.Collections.IEqualityComparer


