from typing import overload
from enum import Enum
import abc
import typing

import System
import System.Collections
import System.Collections.Frozen
import System.Collections.Generic
import System.Collections.Immutable

System_Collections_Frozen_FrozenSet_T = typing.TypeVar("System_Collections_Frozen_FrozenSet_T")
System_Collections_Frozen_FrozenSet_AlternateLookup_TAlternate = typing.TypeVar("System_Collections_Frozen_FrozenSet_AlternateLookup_TAlternate")
System_Collections_Frozen_FrozenDictionary_TKey = typing.TypeVar("System_Collections_Frozen_FrozenDictionary_TKey")
System_Collections_Frozen_FrozenDictionary_TValue = typing.TypeVar("System_Collections_Frozen_FrozenDictionary_TValue")
System_Collections_Frozen_FrozenDictionary_AlternateLookup_TAlternateKey = typing.TypeVar("System_Collections_Frozen_FrozenDictionary_AlternateLookup_TAlternateKey")


class FrozenSet(typing.Generic[System_Collections_Frozen_FrozenSet_T], System.Object, System.Collections.Generic.ISet[System_Collections_Frozen_FrozenSet_T], System.Collections.Generic.IReadOnlyCollection[System_Collections_Frozen_FrozenSet_T], System.Collections.ICollection, typing.Iterable[System_Collections_Frozen_FrozenSet_T], metaclass=abc.ABCMeta):
    """Provides a set of initialization methods for instances of the FrozenSet{T} class."""

    class AlternateLookup(typing.Generic[System_Collections_Frozen_FrozenSet_AlternateLookup_TAlternate]):
        """
        Provides a type that may be used to perform operations on a FrozenSet{T}
        using a TAlternate as a key instead of a T.
        """

        @property
        def set(self) -> System.Collections.Frozen.FrozenSet[System_Collections_Frozen_FrozenSet_T]:
            """Gets the FrozenSet{T} against which this instance performs operations."""
            ...

        def contains(self, item: System_Collections_Frozen_FrozenSet_AlternateLookup_TAlternate) -> bool:
            """
            Determines whether a set contains the specified element.
            
            :param item: The element to locate in the set.
            :returns: true if the set contains the specified element; otherwise, false.
            """
            ...

        def try_get_value(self, equal_value: System_Collections_Frozen_FrozenSet_AlternateLookup_TAlternate, actual_value: typing.Optional[System_Collections_Frozen_FrozenSet_T]) -> typing.Tuple[bool, System_Collections_Frozen_FrozenSet_T]:
            """
            Searches the set for a given value and returns the equal value it finds, if any.
            
            :param equal_value: The value to search for.
            :param actual_value: The value from the set that the search found, or the default value of T when the search yielded no match.
            :returns: A value indicating whether the search was successful.
            """
            ...

    class Enumerator(System.Collections.Generic.IEnumerator[System_Collections_Frozen_FrozenSet_T]):
        """Enumerates the values of a FrozenSet{T}."""

        @property
        def current(self) -> System_Collections_Frozen_FrozenSet_T:
            ...

        def move_next(self) -> bool:
            ...

    EMPTY: System.Collections.Frozen.FrozenSet[System_Collections_Frozen_FrozenSet_T]
    """Gets an empty FrozenSet{T}."""

    @property
    def comparer(self) -> System.Collections.Generic.IEqualityComparer[System_Collections_Frozen_FrozenSet_T]:
        """Gets the comparer used by this set."""
        ...

    @property
    def items(self) -> System.Collections.Immutable.ImmutableArray[System_Collections_Frozen_FrozenSet_T]:
        """Gets a collection containing the values in the set."""
        ...

    @property
    def count(self) -> int:
        """Gets the number of values contained in the set."""
        ...

    def __iter__(self) -> typing.Iterator[System_Collections_Frozen_FrozenSet_T]:
        ...

    def contains(self, item: System_Collections_Frozen_FrozenSet_T) -> bool:
        """
        Determines whether the set contains the specified element.
        
        :param item: The element to locate.
        :returns: true if the set contains the specified element; otherwise, false.
        """
        ...

    @overload
    def copy_to(self, destination: typing.List[System_Collections_Frozen_FrozenSet_T], destination_index: int) -> None:
        """
        Copies the values in the set to an array, starting at the specified .
        
        :param destination: The array that is the destination of the values copied from the set.
        :param destination_index: The zero-based index in  at which copying begins.
        """
        ...

    @overload
    def copy_to(self, destination: System.Span[System_Collections_Frozen_FrozenSet_T]) -> None:
        """
        Copies the values in the set to a span.
        
        :param destination: The span that is the destination of the values copied from the set.
        """
        ...

    def get_enumerator(self) -> System.Collections.Frozen.FrozenSet.Enumerator:
        """
        Returns an enumerator that iterates through the set.
        
        :returns: An enumerator that iterates through the set.
        """
        ...

    def is_proper_subset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Frozen_FrozenSet_T]) -> bool:
        ...

    def is_proper_superset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Frozen_FrozenSet_T]) -> bool:
        ...

    def is_subset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Frozen_FrozenSet_T]) -> bool:
        ...

    def is_superset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Frozen_FrozenSet_T]) -> bool:
        ...

    def overlaps(self, other: System.Collections.Generic.IEnumerable[System_Collections_Frozen_FrozenSet_T]) -> bool:
        ...

    def set_equals(self, other: System.Collections.Generic.IEnumerable[System_Collections_Frozen_FrozenSet_T]) -> bool:
        ...

    def try_get_value(self, equal_value: System_Collections_Frozen_FrozenSet_T, actual_value: typing.Optional[System_Collections_Frozen_FrozenSet_T]) -> typing.Tuple[bool, System_Collections_Frozen_FrozenSet_T]:
        """
        Searches the set for a given value and returns the equal value it finds, if any.
        
        :param equal_value: The value to search for.
        :param actual_value: The value from the set that the search found, or the default value of T when the search yielded no match.
        :returns: A value indicating whether the search was successful.
        """
        ...


class FrozenDictionary(typing.Generic[System_Collections_Frozen_FrozenDictionary_TKey, System_Collections_Frozen_FrozenDictionary_TValue], System.Object, System.Collections.Generic.IDictionary[System_Collections_Frozen_FrozenDictionary_TKey, System_Collections_Frozen_FrozenDictionary_TValue], System.Collections.Generic.IReadOnlyDictionary[System_Collections_Frozen_FrozenDictionary_TKey, System_Collections_Frozen_FrozenDictionary_TValue], System.Collections.IDictionary, typing.Iterable[System.Collections.Generic.KeyValuePair[System_Collections_Frozen_FrozenDictionary_TKey, System_Collections_Frozen_FrozenDictionary_TValue]], metaclass=abc.ABCMeta):
    """Provides a set of initialization methods for instances of the FrozenDictionary{TKey, TValue} class."""

    class AlternateLookup(typing.Generic[System_Collections_Frozen_FrozenDictionary_AlternateLookup_TAlternateKey]):
        """
        Provides a type that may be used to perform operations on a FrozenDictionary{TKey, TValue}
        using a TAlternateKey as a key instead of a TKey.
        """

        @property
        def dictionary(self) -> System.Collections.Frozen.FrozenDictionary[System_Collections_Frozen_FrozenDictionary_TKey, System_Collections_Frozen_FrozenDictionary_TValue]:
            """Gets the FrozenDictionary{TKey, TValue} against which this instance performs operations."""
            ...

        def __getitem__(self, key: System_Collections_Frozen_FrozenDictionary_AlternateLookup_TAlternateKey) -> System_Collections_Frozen_FrozenDictionary_TValue:
            """
            Gets or sets the value associated with the specified alternate key.
            
            :param key: The alternate key of the value to get or set.
            """
            ...

        def contains_key(self, key: System_Collections_Frozen_FrozenDictionary_AlternateLookup_TAlternateKey) -> bool:
            """
            Determines whether the FrozenDictionary{TKey, TValue} contains the specified alternate key.
            
            :param key: The alternate key to check.
            :returns: true if the key is in the dictionary; otherwise, false.
            """
            ...

        def try_get_value(self, key: System_Collections_Frozen_FrozenDictionary_AlternateLookup_TAlternateKey, value: typing.Optional[System_Collections_Frozen_FrozenDictionary_TValue]) -> typing.Tuple[bool, System_Collections_Frozen_FrozenDictionary_TValue]:
            """
            Gets the value associated with the specified alternate key.
            
            :param key: The alternate key of the value to get.
            :param value: When this method returns, contains the value associated with the specified key, if the key is found; otherwise, the default value for the type of the value parameter.
            :returns: true if an entry was found; otherwise, false.
            """
            ...

    class Enumerator(System.Collections.Generic.IEnumerator[System.Collections.Generic.KeyValuePair[System_Collections_Frozen_FrozenDictionary_TKey, System_Collections_Frozen_FrozenDictionary_TValue]]):
        """Enumerates the elements of a FrozenDictionary{TKey, TValue}."""

        @property
        def current(self) -> System.Collections.Generic.KeyValuePair[System_Collections_Frozen_FrozenDictionary_TKey, System_Collections_Frozen_FrozenDictionary_TValue]:
            ...

        def move_next(self) -> bool:
            ...

    EMPTY: System.Collections.Frozen.FrozenDictionary[System_Collections_Frozen_FrozenDictionary_TKey, System_Collections_Frozen_FrozenDictionary_TValue]
    """Gets an empty FrozenDictionary{TKey, TValue}."""

    @property
    def comparer(self) -> System.Collections.Generic.IEqualityComparer[System_Collections_Frozen_FrozenDictionary_TKey]:
        """Gets the comparer used by this dictionary."""
        ...

    @property
    def keys(self) -> System.Collections.Immutable.ImmutableArray[System_Collections_Frozen_FrozenDictionary_TKey]:
        """Gets a collection containing the keys in the dictionary."""
        ...

    @property
    def values(self) -> System.Collections.Immutable.ImmutableArray[System_Collections_Frozen_FrozenDictionary_TValue]:
        """Gets a collection containing the values in the dictionary."""
        ...

    @property
    def count(self) -> int:
        """Gets the number of key/value pairs contained in the dictionary."""
        ...

    def __contains__(self, key: System_Collections_Frozen_FrozenDictionary_TKey) -> bool:
        """
        Determines whether the dictionary contains the specified key.
        
        :param key: The key to locate in the dictionary.
        :returns: true if the dictionary contains an element with the specified key; otherwise, false.
        """
        ...

    def __getitem__(self, key: System_Collections_Frozen_FrozenDictionary_TKey) -> typing.Any:
        """
        Gets a reference to the value associated with the specified key.
        
        :param key: The key of the value to get.
        :returns: A reference to the value associated with the specified key.
        """
        ...

    def __iter__(self) -> typing.Iterator[System.Collections.Generic.KeyValuePair[System_Collections_Frozen_FrozenDictionary_TKey, System_Collections_Frozen_FrozenDictionary_TValue]]:
        ...

    def __len__(self) -> int:
        ...

    def contains_key(self, key: System_Collections_Frozen_FrozenDictionary_TKey) -> bool:
        """
        Determines whether the dictionary contains the specified key.
        
        :param key: The key to locate in the dictionary.
        :returns: true if the dictionary contains an element with the specified key; otherwise, false.
        """
        ...

    @overload
    def copy_to(self, destination: typing.List[System.Collections.Generic.KeyValuePair[System_Collections_Frozen_FrozenDictionary_TKey, System_Collections_Frozen_FrozenDictionary_TValue]], destination_index: int) -> None:
        """
        Copies the elements of the dictionary to an array of type KeyValuePair{TKey, TValue}, starting at the specified .
        
        :param destination: The array that is the destination of the elements copied from the dictionary.
        :param destination_index: The zero-based index in  at which copying begins.
        """
        ...

    @overload
    def copy_to(self, destination: System.Span[System.Collections.Generic.KeyValuePair[System_Collections_Frozen_FrozenDictionary_TKey, System_Collections_Frozen_FrozenDictionary_TValue]]) -> None:
        """
        Copies the elements of the dictionary to a span of type KeyValuePair{TKey, TValue}.
        
        :param destination: The span that is the destination of the elements copied from the dictionary.
        """
        ...

    def get_enumerator(self) -> System.Collections.Frozen.FrozenDictionary.Enumerator:
        """
        Returns an enumerator that iterates through the dictionary.
        
        :returns: An enumerator that iterates through the dictionary.
        """
        ...

    def get_value_ref_or_null_ref(self, key: System_Collections_Frozen_FrozenDictionary_TKey) -> typing.Any:
        """
        Gets either a reference to a TValue in the dictionary or a null reference if the key does not exist in the dictionary.
        
        :param key: The key used for lookup.
        :returns: A reference to a TValue in the dictionary or a null reference if the key does not exist in the dictionary.
        """
        ...

    def try_get_value(self, key: System_Collections_Frozen_FrozenDictionary_TKey, value: typing.Optional[System_Collections_Frozen_FrozenDictionary_TValue]) -> typing.Tuple[bool, System_Collections_Frozen_FrozenDictionary_TValue]:
        """
        Gets the value associated with the specified key.
        
        :param key: The key of the value to get.
        :param value: When this method returns, contains the value associated with the specified key, if the key is found; otherwise, the default value for the type of the value parameter.
        :returns: true if the dictionary contains an element with the specified key; otherwise, false.
        """
        ...


