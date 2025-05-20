from typing import overload
from enum import Enum
import abc
import typing

import System
import System.Collections
import System.Collections.Generic
import System.Collections.Immutable

System_Collections_Immutable_ImmutableHashSet_Enumerator = typing.Any
System_Collections_Immutable_ImmutableList_Enumerator = typing.Any
System_Collections_Immutable_ImmutableArray = typing.Any
System_Collections_Immutable_ImmutableSortedSet_Enumerator = typing.Any

System_Collections_Immutable_ImmutableDictionary_TValue = typing.TypeVar("System_Collections_Immutable_ImmutableDictionary_TValue")
System_Collections_Immutable_ImmutableDictionary_TKey = typing.TypeVar("System_Collections_Immutable_ImmutableDictionary_TKey")
System_Collections_Immutable_ImmutableHashSet_T = typing.TypeVar("System_Collections_Immutable_ImmutableHashSet_T")
System_Collections_Immutable_IImmutableSet_T = typing.TypeVar("System_Collections_Immutable_IImmutableSet_T")
System_Collections_Immutable_ImmutableList_T = typing.TypeVar("System_Collections_Immutable_ImmutableList_T")
System_Collections_Immutable_ImmutableArray_T = typing.TypeVar("System_Collections_Immutable_ImmutableArray_T")
System_Collections_Immutable_ImmutableSortedSet_T = typing.TypeVar("System_Collections_Immutable_ImmutableSortedSet_T")
System_Collections_Immutable_ImmutableQueue_T = typing.TypeVar("System_Collections_Immutable_ImmutableQueue_T")
System_Collections_Immutable_ImmutableSortedDictionary_TValue = typing.TypeVar("System_Collections_Immutable_ImmutableSortedDictionary_TValue")
System_Collections_Immutable_ImmutableSortedDictionary_TKey = typing.TypeVar("System_Collections_Immutable_ImmutableSortedDictionary_TKey")
System_Collections_Immutable_ImmutableStack_T = typing.TypeVar("System_Collections_Immutable_ImmutableStack_T")
System_Collections_Immutable_IImmutableList_T = typing.TypeVar("System_Collections_Immutable_IImmutableList_T")
System_Collections_Immutable_IImmutableDictionary_TKey = typing.TypeVar("System_Collections_Immutable_IImmutableDictionary_TKey")
System_Collections_Immutable_IImmutableDictionary_TValue = typing.TypeVar("System_Collections_Immutable_IImmutableDictionary_TValue")
System_Collections_Immutable_IImmutableStack_T = typing.TypeVar("System_Collections_Immutable_IImmutableStack_T")
System_Collections_Immutable_IImmutableQueue_T = typing.TypeVar("System_Collections_Immutable_IImmutableQueue_T")


class ImmutableDictionary(typing.Generic[System_Collections_Immutable_ImmutableDictionary_TKey, System_Collections_Immutable_ImmutableDictionary_TValue], System.Object, System.Collections.Immutable.IImmutableDictionary[System_Collections_Immutable_ImmutableDictionary_TKey, System_Collections_Immutable_ImmutableDictionary_TValue], System.Collections.Immutable.IImmutableDictionaryInternal[System_Collections_Immutable_ImmutableDictionary_TKey, System_Collections_Immutable_ImmutableDictionary_TValue], System.Collections.Generic.IDictionary[System_Collections_Immutable_ImmutableDictionary_TKey, System_Collections_Immutable_ImmutableDictionary_TValue], System.Collections.IDictionary, typing.Iterable[System.Collections.Generic.KeyValuePair[System_Collections_Immutable_ImmutableDictionary_TKey, System_Collections_Immutable_ImmutableDictionary_TValue]]):
    """An immutable unordered dictionary implementation."""

    class Builder(System.Object, System.Collections.Generic.IDictionary[System_Collections_Immutable_ImmutableDictionary_TKey, System_Collections_Immutable_ImmutableDictionary_TValue], System.Collections.Generic.IReadOnlyDictionary[System_Collections_Immutable_ImmutableDictionary_TKey, System_Collections_Immutable_ImmutableDictionary_TValue], System.Collections.IDictionary, typing.Iterable[System.Collections.Generic.KeyValuePair[System_Collections_Immutable_ImmutableDictionary_TKey, System_Collections_Immutable_ImmutableDictionary_TValue]]):
        """
        A dictionary that mutates with little or no memory allocations,
        can produce and/or build on immutable dictionary instances very efficiently.
        """

        @property
        def key_comparer(self) -> System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableDictionary_TKey]:
            """Gets or sets the key comparer."""
            ...

        @key_comparer.setter
        def key_comparer(self, value: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableDictionary_TKey]) -> None:
            ...

        @property
        def value_comparer(self) -> System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableDictionary_TValue]:
            """Gets or sets the value comparer."""
            ...

        @value_comparer.setter
        def value_comparer(self, value: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableDictionary_TValue]) -> None:
            ...

        @property
        def count(self) -> int:
            """Gets the number of elements contained in the ICollection{T}."""
            ...

        @property
        def keys(self) -> typing.Iterable[System_Collections_Immutable_ImmutableDictionary_TKey]:
            """See IReadOnlyDictionary{TKey, TValue}"""
            ...

        @property
        def values(self) -> typing.Iterable[System_Collections_Immutable_ImmutableDictionary_TValue]:
            """See IReadOnlyDictionary{TKey, TValue}"""
            ...

        def __contains__(self, key: System_Collections_Immutable_ImmutableDictionary_TKey) -> bool:
            """
            Determines whether the IDictionary{TKey, TValue} contains an element with the specified key.
            
            :param key: The key to locate in the IDictionary{TKey, TValue}.
            :returns: true if the IDictionary{TKey, TValue} contains an element with the key; otherwise, false.
            """
            ...

        def __getitem__(self, key: System_Collections_Immutable_ImmutableDictionary_TKey) -> System_Collections_Immutable_ImmutableDictionary_TValue:
            """
            Gets or sets the element with the specified key.
            
            :returns: The element with the specified key.
            """
            ...

        def __iter__(self) -> typing.Iterator[System.Collections.Generic.KeyValuePair[System_Collections_Immutable_ImmutableDictionary_TKey, System_Collections_Immutable_ImmutableDictionary_TValue]]:
            ...

        def __len__(self) -> int:
            ...

        def __setitem__(self, key: System_Collections_Immutable_ImmutableDictionary_TKey, value: System_Collections_Immutable_ImmutableDictionary_TValue) -> None:
            """
            Gets or sets the element with the specified key.
            
            :returns: The element with the specified key.
            """
            ...

        @overload
        def add(self, key: System_Collections_Immutable_ImmutableDictionary_TKey, value: System_Collections_Immutable_ImmutableDictionary_TValue) -> None:
            """
            Adds an element with the provided key and value to the IDictionary{TKey, TValue}.
            
            :param key: The object to use as the key of the element to add.
            :param value: The object to use as the value of the element to add.
            """
            ...

        @overload
        def add(self, item: System.Collections.Generic.KeyValuePair[System_Collections_Immutable_ImmutableDictionary_TKey, System_Collections_Immutable_ImmutableDictionary_TValue]) -> None:
            """
            Adds an item to the ICollection{T}.
            
            :param item: The object to add to the ICollection{T}.
            """
            ...

        def add_range(self, items: System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[System_Collections_Immutable_ImmutableDictionary_TKey, System_Collections_Immutable_ImmutableDictionary_TValue]]) -> None:
            """
            Adds a sequence of values to this collection.
            
            :param items: The items.
            """
            ...

        def clear(self) -> None:
            """Removes all items from the ICollection{T}."""
            ...

        def contains(self, item: System.Collections.Generic.KeyValuePair[System_Collections_Immutable_ImmutableDictionary_TKey, System_Collections_Immutable_ImmutableDictionary_TValue]) -> bool:
            """
            Determines whether the ICollection{T} contains a specific value.
            
            :param item: The object to locate in the ICollection{T}.
            :returns: true if  is found in the ICollection{T}; otherwise, false.
            """
            ...

        def contains_key(self, key: System_Collections_Immutable_ImmutableDictionary_TKey) -> bool:
            """
            Determines whether the IDictionary{TKey, TValue} contains an element with the specified key.
            
            :param key: The key to locate in the IDictionary{TKey, TValue}.
            :returns: true if the IDictionary{TKey, TValue} contains an element with the key; otherwise, false.
            """
            ...

        def contains_value(self, value: System_Collections_Immutable_ImmutableDictionary_TValue) -> bool:
            """
            Determines whether the ImmutableDictionary{TKey, TValue}
            contains an element with the specified value.
            
            :param value: The value to locate in the ImmutableDictionary{TKey, TValue}. The value can be null for reference types.
            :returns: true if the ImmutableDictionary{TKey, TValue} contains an element with the specified value; otherwise, false.
            """
            ...

        def get_enumerator(self) -> System.Collections.Immutable.ImmutableDictionary.Enumerator:
            """
            Returns an enumerator that iterates through the collection.
            
            :returns: A IEnumerator{T} that can be used to iterate through the collection.
            """
            ...

        @overload
        def get_value_or_default(self, key: System_Collections_Immutable_ImmutableDictionary_TKey) -> System_Collections_Immutable_ImmutableDictionary_TValue:
            """
            Gets the value for a given key if a matching key exists in the dictionary.
            
            :param key: The key to search for.
            :returns: The value for the key, or the default value of type TValue if no matching key was found.
            """
            ...

        @overload
        def get_value_or_default(self, key: System_Collections_Immutable_ImmutableDictionary_TKey, default_value: System_Collections_Immutable_ImmutableDictionary_TValue) -> System_Collections_Immutable_ImmutableDictionary_TValue:
            """
            Gets the value for a given key if a matching key exists in the dictionary.
            
            :param key: The key to search for.
            :param default_value: The default value to return if no matching key is found in the dictionary.
            :returns: The value for the key, or  if no matching key was found.
            """
            ...

        @overload
        def remove(self, key: System_Collections_Immutable_ImmutableDictionary_TKey) -> bool:
            """
            Removes the element with the specified key from the IDictionary{TKey, TValue}.
            
            :param key: The key of the element to remove.
            :returns: true if the element is successfully removed; otherwise, false.  This method also returns false if  was not found in the original IDictionary{TKey, TValue}.
            """
            ...

        @overload
        def remove(self, item: System.Collections.Generic.KeyValuePair[System_Collections_Immutable_ImmutableDictionary_TKey, System_Collections_Immutable_ImmutableDictionary_TValue]) -> bool:
            """
            Removes the first occurrence of a specific object from the ICollection{T}.
            
            :param item: The object to remove from the ICollection{T}.
            :returns: true if  was successfully removed from the ICollection{T}; otherwise, false. This method also returns false if  is not found in the original ICollection{T}.
            """
            ...

        def remove_range(self, keys: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableDictionary_TKey]) -> None:
            """
            Removes any entries from the dictionaries with keys that match those found in the specified sequence.
            
            :param keys: The keys for entries to remove from the dictionary.
            """
            ...

        def to_immutable(self) -> System.Collections.Immutable.ImmutableDictionary[System_Collections_Immutable_ImmutableDictionary_TKey, System_Collections_Immutable_ImmutableDictionary_TValue]:
            """
            Creates an immutable dictionary based on the contents of this instance.
            
            :returns: An immutable map.
            """
            ...

        def try_get_key(self, equal_key: System_Collections_Immutable_ImmutableDictionary_TKey, actual_key: typing.Optional[System_Collections_Immutable_ImmutableDictionary_TKey]) -> typing.Tuple[bool, System_Collections_Immutable_ImmutableDictionary_TKey]:
            """See the IImmutableDictionary{TKey, TValue} interface."""
            ...

        def try_get_value(self, key: System_Collections_Immutable_ImmutableDictionary_TKey, value: typing.Optional[System_Collections_Immutable_ImmutableDictionary_TValue]) -> typing.Tuple[bool, System_Collections_Immutable_ImmutableDictionary_TValue]:
            """
            Gets the value associated with the specified key.
            
            :param key: The key whose value to get.
            :param value: When this method returns, the value associated with the specified key, if the key is found; otherwise, the default value of the type TValue. This parameter is passed uninitialized.
            :returns: true if the object that implements IDictionary{TKey, TValue} contains an element with the specified key; otherwise, false.
            """
            ...

    class Enumerator(System.Collections.Generic.IEnumerator[System.Collections.Generic.KeyValuePair[System_Collections_Immutable_ImmutableDictionary_TKey, System_Collections_Immutable_ImmutableDictionary_TValue]]):
        """Enumerates the contents of the collection in an allocation-free manner."""

        @property
        def current(self) -> System.Collections.Generic.KeyValuePair[System_Collections_Immutable_ImmutableDictionary_TKey, System_Collections_Immutable_ImmutableDictionary_TValue]:
            """Gets the current element."""
            ...

        def dispose(self) -> None:
            """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
            ...

        def move_next(self) -> bool:
            """
            Advances the enumerator to the next element of the collection.
            
            :returns: true if the enumerator was successfully advanced to the next element; false if the enumerator has passed the end of the collection.
            """
            ...

        def reset(self) -> None:
            """Sets the enumerator to its initial position, which is before the first element in the collection."""
            ...

    EMPTY: System.Collections.Immutable.ImmutableDictionary[System_Collections_Immutable_ImmutableDictionary_TKey, System_Collections_Immutable_ImmutableDictionary_TValue] = ...
    """An empty immutable dictionary with default equality comparers."""

    @property
    def count(self) -> int:
        """Gets the number of elements in this collection."""
        ...

    @property
    def is_empty(self) -> bool:
        """Gets a value indicating whether this instance is empty."""
        ...

    @property
    def key_comparer(self) -> System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableDictionary_TKey]:
        """Gets the key comparer."""
        ...

    @property
    def value_comparer(self) -> System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableDictionary_TValue]:
        """Gets the value comparer used to determine whether values are equal."""
        ...

    @property
    def keys(self) -> typing.Iterable[System_Collections_Immutable_ImmutableDictionary_TKey]:
        """Gets the keys in the map."""
        ...

    @property
    def values(self) -> typing.Iterable[System_Collections_Immutable_ImmutableDictionary_TValue]:
        """Gets the values in the map."""
        ...

    def __contains__(self, key: System_Collections_Immutable_ImmutableDictionary_TKey) -> bool:
        """
        Determines whether the specified key contains key.
        
        :param key: The key.
        :returns: true if the specified key contains key; otherwise, false.
        """
        ...

    def __getitem__(self, key: System_Collections_Immutable_ImmutableDictionary_TKey) -> System_Collections_Immutable_ImmutableDictionary_TValue:
        """Gets the TValue with the specified key."""
        ...

    def __iter__(self) -> typing.Iterator[System.Collections.Generic.KeyValuePair[System_Collections_Immutable_ImmutableDictionary_TKey, System_Collections_Immutable_ImmutableDictionary_TValue]]:
        ...

    def __len__(self) -> int:
        ...

    def add(self, key: System_Collections_Immutable_ImmutableDictionary_TKey, value: System_Collections_Immutable_ImmutableDictionary_TValue) -> System.Collections.Immutable.ImmutableDictionary[System_Collections_Immutable_ImmutableDictionary_TKey, System_Collections_Immutable_ImmutableDictionary_TValue]:
        """See the IImmutableDictionary{TKey, TValue} interface."""
        ...

    def add_range(self, pairs: System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[System_Collections_Immutable_ImmutableDictionary_TKey, System_Collections_Immutable_ImmutableDictionary_TValue]]) -> System.Collections.Immutable.ImmutableDictionary[System_Collections_Immutable_ImmutableDictionary_TKey, System_Collections_Immutable_ImmutableDictionary_TValue]:
        """See the IImmutableDictionary{TKey, TValue} interface."""
        ...

    def clear(self) -> System.Collections.Immutable.ImmutableDictionary[System_Collections_Immutable_ImmutableDictionary_TKey, System_Collections_Immutable_ImmutableDictionary_TValue]:
        """See the IImmutableDictionary{TKey, TValue} interface."""
        ...

    def contains(self, pair: System.Collections.Generic.KeyValuePair[System_Collections_Immutable_ImmutableDictionary_TKey, System_Collections_Immutable_ImmutableDictionary_TValue]) -> bool:
        """
        Determines whether [contains] [the specified key value pair].
        
        :param pair: The key value pair.
        :returns: true if [contains] [the specified key value pair]; otherwise, false.
        """
        ...

    def contains_key(self, key: System_Collections_Immutable_ImmutableDictionary_TKey) -> bool:
        """
        Determines whether the specified key contains key.
        
        :param key: The key.
        :returns: true if the specified key contains key; otherwise, false.
        """
        ...

    def contains_value(self, value: System_Collections_Immutable_ImmutableDictionary_TValue) -> bool:
        """
        Determines whether the ImmutableDictionary{TKey, TValue}
        contains an element with the specified value.
        
        :param value: The value to locate in the ImmutableDictionary{TKey, TValue}. The value can be null for reference types.
        :returns: true if the ImmutableDictionary{TKey, TValue} contains an element with the specified value; otherwise, false.
        """
        ...

    def get_enumerator(self) -> System.Collections.Immutable.ImmutableDictionary.Enumerator:
        """
        Returns an enumerator that iterates through the collection.
        
        :returns: A IEnumerator{T} that can be used to iterate through the collection.
        """
        ...

    def remove(self, key: System_Collections_Immutable_ImmutableDictionary_TKey) -> System.Collections.Immutable.ImmutableDictionary[System_Collections_Immutable_ImmutableDictionary_TKey, System_Collections_Immutable_ImmutableDictionary_TValue]:
        """See the IImmutableDictionary{TKey, TValue} interface."""
        ...

    def remove_range(self, keys: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableDictionary_TKey]) -> System.Collections.Immutable.ImmutableDictionary[System_Collections_Immutable_ImmutableDictionary_TKey, System_Collections_Immutable_ImmutableDictionary_TValue]:
        """See the IImmutableDictionary{TKey, TValue} interface."""
        ...

    def set_item(self, key: System_Collections_Immutable_ImmutableDictionary_TKey, value: System_Collections_Immutable_ImmutableDictionary_TValue) -> System.Collections.Immutable.ImmutableDictionary[System_Collections_Immutable_ImmutableDictionary_TKey, System_Collections_Immutable_ImmutableDictionary_TValue]:
        """See the IImmutableDictionary{TKey, TValue} interface."""
        ...

    def set_items(self, items: System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[System_Collections_Immutable_ImmutableDictionary_TKey, System_Collections_Immutable_ImmutableDictionary_TValue]]) -> System.Collections.Immutable.ImmutableDictionary[System_Collections_Immutable_ImmutableDictionary_TKey, System_Collections_Immutable_ImmutableDictionary_TValue]:
        """
        Applies a given set of key=value pairs to an immutable dictionary, replacing any conflicting keys in the resulting dictionary.
        
        :param items: The key=value pairs to set on the map.  Any keys that conflict with existing keys will overwrite the previous values.
        :returns: An immutable dictionary.
        """
        ...

    def to_builder(self) -> System.Collections.Immutable.ImmutableDictionary.Builder:
        """
        Creates a collection with the same contents as this collection that
        can be efficiently mutated across multiple operations using standard
        mutable interfaces.
        """
        ...

    def try_get_key(self, equal_key: System_Collections_Immutable_ImmutableDictionary_TKey, actual_key: typing.Optional[System_Collections_Immutable_ImmutableDictionary_TKey]) -> typing.Tuple[bool, System_Collections_Immutable_ImmutableDictionary_TKey]:
        """See the IImmutableDictionary{TKey, TValue} interface."""
        ...

    def try_get_value(self, key: System_Collections_Immutable_ImmutableDictionary_TKey, value: typing.Optional[System_Collections_Immutable_ImmutableDictionary_TValue]) -> typing.Tuple[bool, System_Collections_Immutable_ImmutableDictionary_TValue]:
        """See the IImmutableDictionary{TKey, TValue} interface."""
        ...

    @overload
    def with_comparers(self, key_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableDictionary_TKey], value_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableDictionary_TValue]) -> System.Collections.Immutable.ImmutableDictionary[System_Collections_Immutable_ImmutableDictionary_TKey, System_Collections_Immutable_ImmutableDictionary_TValue]:
        """See the IImmutableDictionary{TKey, TValue} interface."""
        ...

    @overload
    def with_comparers(self, key_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableDictionary_TKey]) -> System.Collections.Immutable.ImmutableDictionary[System_Collections_Immutable_ImmutableDictionary_TKey, System_Collections_Immutable_ImmutableDictionary_TValue]:
        """See the IImmutableDictionary{TKey, TValue} interface."""
        ...


class ImmutableHashSet(typing.Generic[System_Collections_Immutable_ImmutableHashSet_T], System.Object, System.Collections.Immutable.IImmutableSet[System_Collections_Immutable_ImmutableHashSet_T], System.Collections.Generic.ISet[System_Collections_Immutable_ImmutableHashSet_T], System.Collections.ICollection, System.Collections.Immutable.IStrongEnumerable[System_Collections_Immutable_ImmutableHashSet_T, System_Collections_Immutable_ImmutableHashSet_Enumerator], typing.Iterable[System_Collections_Immutable_ImmutableHashSet_T]):
    """An immutable unordered hash set implementation."""

    class Builder(System.Object, System.Collections.Generic.IReadOnlyCollection[System_Collections_Immutable_ImmutableHashSet_T], System.Collections.Generic.ISet[System_Collections_Immutable_ImmutableHashSet_T], typing.Iterable[System_Collections_Immutable_ImmutableHashSet_T]):
        """
        A hash set that mutates with little or no memory allocations,
        can produce and/or build on immutable hash set instances very efficiently.
        """

        @property
        def count(self) -> int:
            """Gets the number of elements contained in the ICollection{T}."""
            ...

        @property
        def key_comparer(self) -> System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableHashSet_T]:
            """Gets or sets the key comparer."""
            ...

        @key_comparer.setter
        def key_comparer(self, value: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableHashSet_T]) -> None:
            ...

        def __iter__(self) -> typing.Iterator[System_Collections_Immutable_ImmutableHashSet_T]:
            ...

        def add(self, item: System_Collections_Immutable_ImmutableHashSet_T) -> bool:
            """
            Adds the specified item.
            
            :param item: The item.
            :returns: True if the item did not already belong to the collection.
            """
            ...

        def clear(self) -> None:
            """Removes all items from the ICollection{T}."""
            ...

        def contains(self, item: System_Collections_Immutable_ImmutableHashSet_T) -> bool:
            """
            Determines whether the ICollection{T} contains a specific value.
            
            :param item: The object to locate in the ICollection{T}.
            :returns: true if  is found in the ICollection{T}; otherwise, false.
            """
            ...

        def except_with(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableHashSet_T]) -> None:
            """
            Removes all elements in the specified collection from the current set.
            
            :param other: The collection of items to remove from the set.
            """
            ...

        def get_enumerator(self) -> System.Collections.Immutable.ImmutableHashSet.Enumerator:
            """
            Returns an enumerator that iterates through the collection.
            
            :returns: A IEnumerator{T} that can be used to iterate through the collection.
            """
            ...

        def intersect_with(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableHashSet_T]) -> None:
            """
            Modifies the current set so that it contains only elements that are also in a specified collection.
            
            :param other: The collection to compare to the current set.
            """
            ...

        def is_proper_subset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableHashSet_T]) -> bool:
            """
            Determines whether the current set is a proper (strict) subset of a specified collection.
            
            :param other: The collection to compare to the current set.
            :returns: true if the current set is a correct subset of other; otherwise, false.
            """
            ...

        def is_proper_superset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableHashSet_T]) -> bool:
            """
            Determines whether the current set is a proper (strict) superset of a specified collection.
            
            :param other: The collection to compare to the current set.
            :returns: true if the current set is a superset of other; otherwise, false.
            """
            ...

        def is_subset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableHashSet_T]) -> bool:
            """
            Determines whether the current set is a subset of a specified collection.
            
            :param other: The collection to compare to the current set.
            :returns: true if the current set is a subset of other; otherwise, false.
            """
            ...

        def is_superset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableHashSet_T]) -> bool:
            """
            Determines whether the current set is a superset of a specified collection.
            
            :param other: The collection to compare to the current set.
            :returns: true if the current set is a superset of other; otherwise, false.
            """
            ...

        def overlaps(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableHashSet_T]) -> bool:
            """
            Determines whether the current set overlaps with the specified collection.
            
            :param other: The collection to compare to the current set.
            :returns: true if the current set and other share at least one common element; otherwise, false.
            """
            ...

        def remove(self, item: System_Collections_Immutable_ImmutableHashSet_T) -> bool:
            """
            Removes the first occurrence of a specific object from the ICollection{T}.
            
            :param item: The object to remove from the ICollection{T}.
            :returns: true if  was successfully removed from the ICollection{T}; otherwise, false. This method also returns false if  is not found in the original ICollection{T}.
            """
            ...

        def set_equals(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableHashSet_T]) -> bool:
            """
            Determines whether the current set and the specified collection contain the same elements.
            
            :param other: The collection to compare to the current set.
            :returns: true if the current set is equal to other; otherwise, false.
            """
            ...

        def symmetric_except_with(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableHashSet_T]) -> None:
            """
            Modifies the current set so that it contains only elements that are present either in the current set or in the specified collection, but not both.
            
            :param other: The collection to compare to the current set.
            """
            ...

        def to_immutable(self) -> System.Collections.Immutable.ImmutableHashSet[System_Collections_Immutable_ImmutableHashSet_T]:
            """
            Creates an immutable hash set based on the contents of this instance.
            
            :returns: An immutable set.
            """
            ...

        def try_get_value(self, equal_value: System_Collections_Immutable_ImmutableHashSet_T, actual_value: typing.Optional[System_Collections_Immutable_ImmutableHashSet_T]) -> typing.Tuple[bool, System_Collections_Immutable_ImmutableHashSet_T]:
            """
            Searches the set for a given value and returns the equal value it finds, if any.
            
            :param equal_value: The value for which to search.
            :param actual_value: The value from the set that the search found, or the original value if the search yielded no match.
            :returns: A value indicating whether the search was successful.
            """
            ...

        def union_with(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableHashSet_T]) -> None:
            """
            Modifies the current set so that it contains all elements that are present in both the current set and in the specified collection.
            
            :param other: The collection to compare to the current set.
            """
            ...

    class Enumerator(System.Collections.Generic.IEnumerator[System_Collections_Immutable_ImmutableHashSet_T], System.Collections.Immutable.IStrongEnumerator[System_Collections_Immutable_ImmutableHashSet_T]):
        """Enumerates the contents of the collection in an allocation-free manner."""

        @property
        def current(self) -> System_Collections_Immutable_ImmutableHashSet_T:
            """Gets the current element."""
            ...

        def dispose(self) -> None:
            """Performs application-defined tasks associated with freeing, releasing, or resetting unmanaged resources."""
            ...

        def move_next(self) -> bool:
            """
            Advances the enumerator to the next element of the collection.
            
            :returns: true if the enumerator was successfully advanced to the next element; false if the enumerator has passed the end of the collection.
            """
            ...

        def reset(self) -> None:
            """Sets the enumerator to its initial position, which is before the first element in the collection."""
            ...

    EMPTY: System.Collections.Immutable.ImmutableHashSet[System_Collections_Immutable_ImmutableHashSet_T] = ...
    """An empty immutable hash set with the default comparer for T."""

    @property
    def count(self) -> int:
        """See the IImmutableSet{T} interface."""
        ...

    @property
    def is_empty(self) -> bool:
        """See the IImmutableSet{T} interface."""
        ...

    @property
    def key_comparer(self) -> System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableHashSet_T]:
        """See the IImmutableSet{T} interface."""
        ...

    def __iter__(self) -> typing.Iterator[System_Collections_Immutable_ImmutableHashSet_T]:
        ...

    def add(self, item: System_Collections_Immutable_ImmutableHashSet_T) -> System.Collections.Immutable.ImmutableHashSet[System_Collections_Immutable_ImmutableHashSet_T]:
        """See the IImmutableSet{T} interface."""
        ...

    def clear(self) -> System.Collections.Immutable.ImmutableHashSet[System_Collections_Immutable_ImmutableHashSet_T]:
        """See the IImmutableSet{T} interface."""
        ...

    def contains(self, item: System_Collections_Immutable_ImmutableHashSet_T) -> bool:
        """See the IImmutableSet{T} interface."""
        ...

    def Except(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableHashSet_T]) -> System.Collections.Immutable.ImmutableHashSet[System_Collections_Immutable_ImmutableHashSet_T]:
        """See the IImmutableSet{T} interface."""
        ...

    def get_enumerator(self) -> System.Collections.Immutable.ImmutableHashSet.Enumerator:
        """
        Returns an enumerator that iterates through the collection.
        
        :returns: A IEnumerator{T} that can be used to iterate through the collection.
        """
        ...

    def intersect(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableHashSet_T]) -> System.Collections.Immutable.ImmutableHashSet[System_Collections_Immutable_ImmutableHashSet_T]:
        """See the IImmutableSet{T} interface."""
        ...

    def is_proper_subset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableHashSet_T]) -> bool:
        """
        Determines whether the current set is a property (strict) subset of a specified collection.
        
        :param other: The collection to compare to the current set.
        :returns: true if the current set is a correct subset of ; otherwise, false.
        """
        ...

    def is_proper_superset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableHashSet_T]) -> bool:
        """
        Determines whether the current set is a correct superset of a specified collection.
        
        :param other: The collection to compare to the current set.
        :returns: true if the current set is a correct superset of ; otherwise, false.
        """
        ...

    def is_subset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableHashSet_T]) -> bool:
        """
        Determines whether a set is a subset of a specified collection.
        
        :param other: The collection to compare to the current set.
        :returns: true if the current set is a subset of ; otherwise, false.
        """
        ...

    def is_superset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableHashSet_T]) -> bool:
        """
        Determines whether the current set is a superset of a specified collection.
        
        :param other: The collection to compare to the current set.
        :returns: true if the current set is a superset of ; otherwise, false.
        """
        ...

    def overlaps(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableHashSet_T]) -> bool:
        """
        Determines whether the current set overlaps with the specified collection.
        
        :param other: The collection to compare to the current set.
        :returns: true if the current set and  share at least one common element; otherwise, false.
        """
        ...

    def remove(self, item: System_Collections_Immutable_ImmutableHashSet_T) -> System.Collections.Immutable.ImmutableHashSet[System_Collections_Immutable_ImmutableHashSet_T]:
        """See the IImmutableSet{T} interface."""
        ...

    def set_equals(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableHashSet_T]) -> bool:
        """
        Checks whether a given sequence of items entirely describe the contents of this set.
        
        :param other: The sequence of items to check against this set.
        :returns: A value indicating whether the sets are equal.
        """
        ...

    def symmetric_except(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableHashSet_T]) -> System.Collections.Immutable.ImmutableHashSet[System_Collections_Immutable_ImmutableHashSet_T]:
        """
        Produces a set that contains elements either in this set or a given sequence, but not both.
        
        :param other: The other sequence of items.
        :returns: The new set.
        """
        ...

    def to_builder(self) -> System.Collections.Immutable.ImmutableHashSet.Builder:
        """
        Creates a collection with the same contents as this collection that
        can be efficiently mutated across multiple operations using standard
        mutable interfaces.
        """
        ...

    def try_get_value(self, equal_value: System_Collections_Immutable_ImmutableHashSet_T, actual_value: typing.Optional[System_Collections_Immutable_ImmutableHashSet_T]) -> typing.Tuple[bool, System_Collections_Immutable_ImmutableHashSet_T]:
        """
        Searches the set for a given value and returns the equal value it finds, if any.
        
        :param equal_value: The value to search for.
        :param actual_value: The value from the set that the search found, or the original value if the search yielded no match.
        :returns: A value indicating whether the search was successful.
        """
        ...

    def union(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableHashSet_T]) -> System.Collections.Immutable.ImmutableHashSet[System_Collections_Immutable_ImmutableHashSet_T]:
        """See the IImmutableSet{T} interface."""
        ...

    def with_comparer(self, equality_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableHashSet_T]) -> System.Collections.Immutable.ImmutableHashSet[System_Collections_Immutable_ImmutableHashSet_T]:
        """See the IImmutableSet{T} interface."""
        ...


class IImmutableSet(typing.Generic[System_Collections_Immutable_IImmutableSet_T], System.Collections.Generic.IReadOnlyCollection[System_Collections_Immutable_IImmutableSet_T], metaclass=abc.ABCMeta):
    """A set of elements that can only be modified by creating a new instance of the set."""

    def add(self, value: System_Collections_Immutable_IImmutableSet_T) -> System.Collections.Immutable.IImmutableSet[System_Collections_Immutable_IImmutableSet_T]:
        """
        Adds the specified value to this set.
        
        :param value: The value to add.
        :returns: A new set with the element added, or this set if the element is already in this set.
        """
        ...

    def clear(self) -> System.Collections.Immutable.IImmutableSet[System_Collections_Immutable_IImmutableSet_T]:
        """Gets an empty set that retains the same sort or unordered semantics that this instance has."""
        ...

    def contains(self, value: System_Collections_Immutable_IImmutableSet_T) -> bool:
        """
        Determines whether this set contains the specified value.
        
        :param value: The value.
        :returns: true if the set contains the specified value; otherwise, false.
        """
        ...

    def Except(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_IImmutableSet_T]) -> System.Collections.Immutable.IImmutableSet[System_Collections_Immutable_IImmutableSet_T]:
        """
        Removes a given set of items from this set.
        
        :param other: The items to remove from this set.
        :returns: The new set with the items removed; or the original set if none of the items were in the set.
        """
        ...

    def intersect(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_IImmutableSet_T]) -> System.Collections.Immutable.IImmutableSet[System_Collections_Immutable_IImmutableSet_T]:
        """
        Produces a set that contains elements that exist in both this set and the specified set.
        
        :param other: The set to intersect with this one.
        :returns: A new set that contains any elements that exist in both sets.
        """
        ...

    def is_proper_subset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_IImmutableSet_T]) -> bool:
        """
        Determines whether the current set is a proper (strict) subset of a specified collection.
        
        :param other: The collection to compare to the current set.
        :returns: true if the current set is a correct subset of other; otherwise, false.
        """
        ...

    def is_proper_superset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_IImmutableSet_T]) -> bool:
        """
        Determines whether the current set is a proper superset of a specified collection.
        
        :param other: The collection to compare to the current set.
        :returns: true if the current set is a correct superset of other; otherwise, false.
        """
        ...

    def is_subset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_IImmutableSet_T]) -> bool:
        """
        Determines whether a set is a subset of a specified collection.
        
        :param other: The collection to compare to the current set.
        :returns: true if the current set is a subset of other; otherwise, false.
        """
        ...

    def is_superset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_IImmutableSet_T]) -> bool:
        """
        Determines whether the current set is a superset of a specified collection.
        
        :param other: The collection to compare to the current set.
        :returns: true if the current set is a superset of other; otherwise, false.
        """
        ...

    def overlaps(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_IImmutableSet_T]) -> bool:
        """
        Determines whether the current set overlaps with the specified collection.
        
        :param other: The collection to compare to the current set.
        :returns: true if the current set and other share at least one common element; otherwise, false.
        """
        ...

    def remove(self, value: System_Collections_Immutable_IImmutableSet_T) -> System.Collections.Immutable.IImmutableSet[System_Collections_Immutable_IImmutableSet_T]:
        """
        Removes the specified value from this set.
        
        :param value: The value to remove.
        :returns: A new set with the element removed, or this set if the element is not in this set.
        """
        ...

    def set_equals(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_IImmutableSet_T]) -> bool:
        """
        Checks whether a given sequence of items entirely describe the contents of this set.
        
        :param other: The sequence of items to check against this set.
        :returns: A value indicating whether the sets are equal.
        """
        ...

    def symmetric_except(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_IImmutableSet_T]) -> System.Collections.Immutable.IImmutableSet[System_Collections_Immutable_IImmutableSet_T]:
        """
        Produces a set that contains elements either in this set or a given sequence, but not both.
        
        :param other: The other sequence of items.
        :returns: The new set.
        """
        ...

    def try_get_value(self, equal_value: System_Collections_Immutable_IImmutableSet_T, actual_value: typing.Optional[System_Collections_Immutable_IImmutableSet_T]) -> typing.Tuple[bool, System_Collections_Immutable_IImmutableSet_T]:
        """
        Searches the set for a given value and returns the equal value it finds, if any.
        
        :param equal_value: The value to search for.
        :param actual_value: The value from the set that the search found, or  if the search yielded no match.
        :returns: A value indicating whether the search was successful.
        """
        ...

    def union(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_IImmutableSet_T]) -> System.Collections.Immutable.IImmutableSet[System_Collections_Immutable_IImmutableSet_T]:
        """
        Adds a given set of items to this set.
        
        :param other: The items to add.
        :returns: The new set with the items added; or the original set if all the items were already in the set.
        """
        ...


class ImmutableList(typing.Generic[System_Collections_Immutable_ImmutableList_T], System.Object, System.Collections.Immutable.IImmutableList[System_Collections_Immutable_ImmutableList_T], System.Collections.Generic.IList[System_Collections_Immutable_ImmutableList_T], System.Collections.IList, System.Collections.Immutable.IStrongEnumerable[System_Collections_Immutable_ImmutableList_T, System_Collections_Immutable_ImmutableList_Enumerator], typing.Iterable[System_Collections_Immutable_ImmutableList_T]):
    """An immutable list implementation."""

    class Enumerator(System.Collections.Generic.IEnumerator[System_Collections_Immutable_ImmutableList_T], System.Collections.Immutable.ISecurePooledObjectUser, System.Collections.Immutable.IStrongEnumerator[System_Collections_Immutable_ImmutableList_T]):
        """Enumerates the contents of a binary tree."""

        @property
        def current(self) -> System_Collections_Immutable_ImmutableList_T:
            """The current element."""
            ...

        def dispose(self) -> None:
            """Disposes of this enumerator and returns the stack reference to the resource pool."""
            ...

        def move_next(self) -> bool:
            """
            Advances enumeration to the next element.
            
            :returns: A value indicating whether there is another element in the enumeration.
            """
            ...

        def reset(self) -> None:
            """Restarts enumeration."""
            ...

    class Builder(System.Object, System.Collections.Generic.IList[System_Collections_Immutable_ImmutableList_T], System.Collections.IList, System.Collections.Generic.IReadOnlyList[System_Collections_Immutable_ImmutableList_T], typing.Iterable[System_Collections_Immutable_ImmutableList_T]):
        """
        A list that mutates with little or no memory allocations,
        can produce and/or build on immutable list instances very efficiently.
        """

        @property
        def count(self) -> int:
            """Gets the number of elements in this list."""
            ...

        def __getitem__(self, index: int) -> System_Collections_Immutable_ImmutableList_T:
            """
            Gets or sets the value for a given index into the list.
            
            :param index: The index of the desired element.
            :returns: The value at the specified index.
            """
            ...

        def __iter__(self) -> typing.Iterator[System_Collections_Immutable_ImmutableList_T]:
            ...

        def __setitem__(self, index: int, value: System_Collections_Immutable_ImmutableList_T) -> None:
            """
            Gets or sets the value for a given index into the list.
            
            :param index: The index of the desired element.
            :returns: The value at the specified index.
            """
            ...

        def add(self, item: System_Collections_Immutable_ImmutableList_T) -> None:
            """See IList{T}"""
            ...

        def add_range(self, items: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableList_T]) -> None:
            """
            Adds the elements of a sequence to the end of this collection.
            
            :param items: The sequence whose elements should be appended to this collection. The sequence itself cannot be null, but it can contain elements that are null, if type T is a reference type.
            """
            ...

        @overload
        def binary_search(self, item: System_Collections_Immutable_ImmutableList_T) -> int:
            """
            Searches the entire sorted System.Collections.Generic.List<T> for an element
            using the default comparer and returns the zero-based index of the element.
            
            :param item: The object to locate. The value can be null for reference types.
            :returns: The zero-based index of item in the sorted System.Collections.Generic.List<T>, if item is found; otherwise, a negative number that is the bitwise complement of the index of the next element that is larger than item or, if there is no larger element, the bitwise complement of System.Collections.Generic.List<T>.Count.
            """
            ...

        @overload
        def binary_search(self, item: System_Collections_Immutable_ImmutableList_T, comparer: System.Collections.Generic.IComparer[System_Collections_Immutable_ImmutableList_T]) -> int:
            """
            Searches the entire sorted System.Collections.Generic.List<T> for an element
             using the specified comparer and returns the zero-based index of the element.
            
            :param item: The object to locate. The value can be null for reference types.
            :param comparer: The System.Collections.Generic.IComparer<T> implementation to use when comparing elements.-or-null to use the default comparer System.Collections.Generic.Comparer<T>.Default.
            :returns: The zero-based index of item in the sorted System.Collections.Generic.List<T>, if item is found; otherwise, a negative number that is the bitwise complement of the index of the next element that is larger than item or, if there is no larger element, the bitwise complement of System.Collections.Generic.List<T>.Count.
            """
            ...

        @overload
        def binary_search(self, index: int, count: int, item: System_Collections_Immutable_ImmutableList_T, comparer: System.Collections.Generic.IComparer[System_Collections_Immutable_ImmutableList_T]) -> int:
            """
            Searches a range of elements in the sorted System.Collections.Generic.List<T>
            for an element using the specified comparer and returns the zero-based index
            of the element.
            
            :param index: The zero-based starting index of the range to search.
            :param count: The length of the range to search.
            :param item: The object to locate. The value can be null for reference types.
            :param comparer: The System.Collections.Generic.IComparer<T> implementation to use when comparing elements, or null to use the default comparer System.Collections.Generic.Comparer<T>.Default.
            :returns: The zero-based index of item in the sorted System.Collections.Generic.List<T>, if item is found; otherwise, a negative number that is the bitwise complement of the index of the next element that is larger than item or, if there is no larger element, the bitwise complement of System.Collections.Generic.List<T>.Count.
            """
            ...

        def clear(self) -> None:
            """See IList{T}"""
            ...

        def contains(self, item: System_Collections_Immutable_ImmutableList_T) -> bool:
            """See IList{T}"""
            ...

        @overload
        def copy_to(self, array: typing.List[System_Collections_Immutable_ImmutableList_T]) -> None:
            """
            Copies the entire ImmutableList<T> to a compatible one-dimensional
            array, starting at the beginning of the target array.
            
            :param array: The one-dimensional System.Array that is the destination of the elements copied from ImmutableList<T>. The System.Array must have zero-based indexing.
            """
            ...

        @overload
        def copy_to(self, array: typing.List[System_Collections_Immutable_ImmutableList_T], array_index: int) -> None:
            """
            Copies the entire ImmutableList<T> to a compatible one-dimensional
            array, starting at the specified index of the target array.
            
            :param array: The one-dimensional System.Array that is the destination of the elements copied from ImmutableList<T>. The System.Array must have zero-based indexing.
            :param array_index: The zero-based index in array at which copying begins.
            """
            ...

        @overload
        def copy_to(self, index: int, array: typing.List[System_Collections_Immutable_ImmutableList_T], array_index: int, count: int) -> None:
            """
            Copies a range of elements from the ImmutableList<T> to
            a compatible one-dimensional array, starting at the specified index of the
            target array.
            
            :param index: The zero-based index in the source ImmutableList<T> at which copying begins.
            :param array: The one-dimensional System.Array that is the destination of the elements copied from ImmutableList<T>. The System.Array must have zero-based indexing.
            :param array_index: The zero-based index in array at which copying begins.
            :param count: The number of elements to copy.
            """
            ...

        def exists(self, match: typing.Callable[[System_Collections_Immutable_ImmutableList_T], bool]) -> bool:
            """
            Determines whether the ImmutableList<T> contains elements
            that match the conditions defined by the specified predicate.
            
            :param match: The System.Predicate<T> delegate that defines the conditions of the elements to search for.
            :returns: true if the ImmutableList<T> contains one or more elements that match the conditions defined by the specified predicate; otherwise, false.
            """
            ...

        def find(self, match: typing.Callable[[System_Collections_Immutable_ImmutableList_T], bool]) -> System_Collections_Immutable_ImmutableList_T:
            """
            Searches for an element that matches the conditions defined by the specified
            predicate, and returns the first occurrence within the entire ImmutableList<T>.
            
            :param match: The System.Predicate<T> delegate that defines the conditions of the element to search for.
            :returns: The first element that matches the conditions defined by the specified predicate, if found; otherwise, the default value for type T.
            """
            ...

        def find_all(self, match: typing.Callable[[System_Collections_Immutable_ImmutableList_T], bool]) -> System.Collections.Immutable.ImmutableList[System_Collections_Immutable_ImmutableList_T]:
            """
            Retrieves all the elements that match the conditions defined by the specified
            predicate.
            
            :param match: The System.Predicate<T> delegate that defines the conditions of the elements to search for.
            :returns: A ImmutableList<T> containing all the elements that match the conditions defined by the specified predicate, if found; otherwise, an empty ImmutableList<T>.
            """
            ...

        @overload
        def find_index(self, match: typing.Callable[[System_Collections_Immutable_ImmutableList_T], bool]) -> int:
            """
            Searches for an element that matches the conditions defined by the specified
            predicate, and returns the zero-based index of the first occurrence within
            the entire ImmutableList<T>.
            
            :param match: The System.Predicate<T> delegate that defines the conditions of the element to search for.
            :returns: The zero-based index of the first occurrence of an element that matches the conditions defined by match, if found; otherwise, -1.
            """
            ...

        @overload
        def find_index(self, start_index: int, match: typing.Callable[[System_Collections_Immutable_ImmutableList_T], bool]) -> int:
            """
            Searches for an element that matches the conditions defined by the specified
            predicate, and returns the zero-based index of the first occurrence within
            the range of elements in the ImmutableList<T> that extends
            from the specified index to the last element.
            
            :param start_index: The zero-based starting index of the search.
            :param match: The System.Predicate<T> delegate that defines the conditions of the element to search for.
            :returns: The zero-based index of the first occurrence of an element that matches the conditions defined by match, if found; otherwise, -1.
            """
            ...

        @overload
        def find_index(self, start_index: int, count: int, match: typing.Callable[[System_Collections_Immutable_ImmutableList_T], bool]) -> int:
            """
            Searches for an element that matches the conditions defined by the specified
            predicate, and returns the zero-based index of the first occurrence within
            the range of elements in the ImmutableList<T> that starts
            at the specified index and contains the specified number of elements.
            
            :param start_index: The zero-based starting index of the search.
            :param count: The number of elements in the section to search.
            :param match: The System.Predicate<T> delegate that defines the conditions of the element to search for.
            :returns: The zero-based index of the first occurrence of an element that matches the conditions defined by match, if found; otherwise, -1.
            """
            ...

        def find_last(self, match: typing.Callable[[System_Collections_Immutable_ImmutableList_T], bool]) -> System_Collections_Immutable_ImmutableList_T:
            """
            Searches for an element that matches the conditions defined by the specified
            predicate, and returns the last occurrence within the entire ImmutableList<T>.
            
            :param match: The System.Predicate<T> delegate that defines the conditions of the element to search for.
            :returns: The last element that matches the conditions defined by the specified predicate, if found; otherwise, the default value for type T.
            """
            ...

        @overload
        def find_last_index(self, match: typing.Callable[[System_Collections_Immutable_ImmutableList_T], bool]) -> int:
            """
            Searches for an element that matches the conditions defined by the specified
            predicate, and returns the zero-based index of the last occurrence within
            the entire ImmutableList<T>.
            
            :param match: The System.Predicate<T> delegate that defines the conditions of the element to search for.
            :returns: The zero-based index of the last occurrence of an element that matches the conditions defined by match, if found; otherwise, -1.
            """
            ...

        @overload
        def find_last_index(self, start_index: int, match: typing.Callable[[System_Collections_Immutable_ImmutableList_T], bool]) -> int:
            """
            Searches for an element that matches the conditions defined by the specified
            predicate, and returns the zero-based index of the last occurrence within
            the range of elements in the ImmutableList<T> that extends
            from the first element to the specified index.
            
            :param start_index: The zero-based starting index of the backward search.
            :param match: The System.Predicate<T> delegate that defines the conditions of the element to search for.
            :returns: The zero-based index of the last occurrence of an element that matches the conditions defined by match, if found; otherwise, -1.
            """
            ...

        @overload
        def find_last_index(self, start_index: int, count: int, match: typing.Callable[[System_Collections_Immutable_ImmutableList_T], bool]) -> int:
            """
            Searches for an element that matches the conditions defined by the specified
            predicate, and returns the zero-based index of the last occurrence within
            the range of elements in the ImmutableList<T> that contains
            the specified number of elements and ends at the specified index.
            
            :param start_index: The zero-based starting index of the backward search.
            :param count: The number of elements in the section to search.
            :param match: The System.Predicate<T> delegate that defines the conditions of the element to search for.
            :returns: The zero-based index of the last occurrence of an element that matches the conditions defined by match, if found; otherwise, -1.
            """
            ...

        def for_each(self, action: typing.Callable[[System_Collections_Immutable_ImmutableList_T], None]) -> None:
            """
            Performs the specified action on each element of the list.
            
            :param action: The System.Action<T> delegate to perform on each element of the list.
            """
            ...

        def get_enumerator(self) -> System.Collections.Immutable.ImmutableList.Enumerator:
            """
            Returns an enumerator that iterates through the collection.
            
            :returns: A IEnumerator{T} that can be used to iterate through the collection.
            """
            ...

        def get_range(self, index: int, count: int) -> System.Collections.Immutable.ImmutableList[System_Collections_Immutable_ImmutableList_T]:
            """
            Creates a shallow copy of a range of elements in the source ImmutableList<T>.
            
            :param index: The zero-based ImmutableList<T> index at which the range starts.
            :param count: The number of elements in the range.
            :returns: A shallow copy of a range of elements in the source ImmutableList<T>.
            """
            ...

        @overload
        def index_of(self, item: System_Collections_Immutable_ImmutableList_T) -> int:
            """See IList{T}"""
            ...

        @overload
        def index_of(self, item: System_Collections_Immutable_ImmutableList_T, index: int) -> int:
            """
            Searches for the specified object and returns the zero-based index of the
            first occurrence within the range of elements in the ImmutableList<T>
            that extends from the specified index to the last element.
            
            :param item: The object to locate in the ImmutableList<T>. The value can be null for reference types.
            :param index: The zero-based starting index of the search. 0 (zero) is valid in an empty list.
            :returns: The zero-based index of the first occurrence of item within the range of elements in the ImmutableList<T> that extends from index to the last element, if found; otherwise, -1.
            """
            ...

        @overload
        def index_of(self, item: System_Collections_Immutable_ImmutableList_T, index: int, count: int) -> int:
            """
            Searches for the specified object and returns the zero-based index of the
            first occurrence within the range of elements in the ImmutableList<T>
            that starts at the specified index and contains the specified number of elements.
            
            :param item: The object to locate in the ImmutableList<T>. The value can be null for reference types.
            :param index: The zero-based starting index of the search. 0 (zero) is valid in an empty list.
            :param count: The number of elements in the section to search.
            :returns: The zero-based index of the first occurrence of item within the range of elements in the ImmutableList<T> that starts at index and contains count number of elements, if found; otherwise, -1.
            """
            ...

        @overload
        def index_of(self, item: System_Collections_Immutable_ImmutableList_T, index: int, count: int, equality_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableList_T]) -> int:
            """
            Searches for the specified object and returns the zero-based index of the
            first occurrence within the range of elements in the ImmutableList<T>
            that starts at the specified index and contains the specified number of elements.
            
            :param item: The object to locate in the ImmutableList<T>. The value can be null for reference types.
            :param index: The zero-based starting index of the search. 0 (zero) is valid in an empty list.
            :param count: The number of elements in the section to search.
            :param equality_comparer: The equality comparer to use in the search. If null, EqualityComparer{T}.Default is used.
            :returns: The zero-based index of the first occurrence of item within the range of elements in the ImmutableList<T> that starts at index and contains count number of elements, if found; otherwise, -1.
            """
            ...

        def insert(self, index: int, item: System_Collections_Immutable_ImmutableList_T) -> None:
            """See IList{T}"""
            ...

        def insert_range(self, index: int, items: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableList_T]) -> None:
            """
            Inserts the elements of a collection into the ImmutableList<T>
            at the specified index.
            
            :param index: The zero-based index at which the new elements should be inserted.
            :param items: The collection whose elements should be inserted into the ImmutableList<T>. The collection itself cannot be null, but it can contain elements that are null, if type T is a reference type.
            """
            ...

        def item_ref(self, index: int) -> typing.Any:
            """
            Gets a read-only reference to the value for a given index into the list.
            
            :param index: The index of the desired element.
            :returns: A read-only reference to the value at the specified index.
            """
            ...

        @overload
        def last_index_of(self, item: System_Collections_Immutable_ImmutableList_T) -> int:
            """
            Searches for the specified object and returns the zero-based index of the
            last occurrence within the range of elements in the ImmutableList<T>
            that contains the specified number of elements and ends at the specified
            index.
            
            :param item: The object to locate in the ImmutableList<T>. The value can be null for reference types.
            :returns: The zero-based index of the last occurrence of item within the range of elements in the ImmutableList<T> that contains count number of elements and ends at index, if found; otherwise, -1.
            """
            ...

        @overload
        def last_index_of(self, item: System_Collections_Immutable_ImmutableList_T, start_index: int) -> int:
            """
            Searches for the specified object and returns the zero-based index of the
            last occurrence within the range of elements in the ImmutableList<T>
            that contains the specified number of elements and ends at the specified
            index.
            
            :param item: The object to locate in the ImmutableList<T>. The value can be null for reference types.
            :param start_index: The zero-based starting index of the backward search.
            :returns: The zero-based index of the last occurrence of item within the range of elements in the ImmutableList<T> that contains count number of elements and ends at index, if found; otherwise, -1.
            """
            ...

        @overload
        def last_index_of(self, item: System_Collections_Immutable_ImmutableList_T, start_index: int, count: int) -> int:
            """
            Searches for the specified object and returns the zero-based index of the
            last occurrence within the range of elements in the ImmutableList<T>
            that contains the specified number of elements and ends at the specified
            index.
            
            :param item: The object to locate in the ImmutableList<T>. The value can be null for reference types.
            :param start_index: The zero-based starting index of the backward search.
            :param count: The number of elements in the section to search.
            :returns: The zero-based index of the last occurrence of item within the range of elements in the ImmutableList<T> that contains count number of elements and ends at index, if found; otherwise, -1.
            """
            ...

        @overload
        def last_index_of(self, item: System_Collections_Immutable_ImmutableList_T, start_index: int, count: int, equality_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableList_T]) -> int:
            """
            Searches for the specified object and returns the zero-based index of the
            last occurrence within the range of elements in the ImmutableList<T>
            that contains the specified number of elements and ends at the specified
            index.
            
            :param item: The object to locate in the ImmutableList<T>. The value can be null for reference types.
            :param start_index: The zero-based starting index of the backward search.
            :param count: The number of elements in the section to search.
            :param equality_comparer: The equality comparer to use in the search.
            :returns: The zero-based index of the last occurrence of item within the range of elements in the ImmutableList<T> that contains count number of elements and ends at index, if found; otherwise, -1.
            """
            ...

        @overload
        def remove(self, item: System_Collections_Immutable_ImmutableList_T) -> bool:
            """See IList{T}"""
            ...

        @overload
        def remove(self, item: System_Collections_Immutable_ImmutableList_T, equality_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableList_T]) -> bool:
            """
            Removes the first occurrence matching the specified value from this list.
            
            :param item: The item to remove.
            :param equality_comparer: The equality comparer to use in the search. If null, EqualityComparer{T}.Default is used.
            :returns: A value indicating whether the specified element was found and removed from the collection.
            """
            ...

        def remove_all(self, match: typing.Callable[[System_Collections_Immutable_ImmutableList_T], bool]) -> int:
            """
            Removes all the elements that match the conditions defined by the specified
            predicate.
            
            :param match: The System.Predicate<T> delegate that defines the conditions of the elements to remove.
            :returns: The number of elements removed from the ImmutableList<T>.
            """
            ...

        def remove_at(self, index: int) -> None:
            """See IList{T}"""
            ...

        @overload
        def remove_range(self, index: int, count: int) -> None:
            """
            Removes the specified range of values from this list.
            
            :param index: The starting index to begin removal.
            :param count: The number of elements to remove.
            """
            ...

        @overload
        def remove_range(self, items: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableList_T], equality_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableList_T]) -> None:
            """
            Removes any first occurrences of the specified values from this list.
            
            :param items: The items to remove if matches are found in this list.
            :param equality_comparer: The equality comparer to use in the search. If null, EqualityComparer{T}.Default is used.
            """
            ...

        @overload
        def remove_range(self, items: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableList_T]) -> None:
            """
            Removes any first occurrences of the specified values from this list.
            
            :param items: The items to remove if matches are found in this list.
            """
            ...

        @overload
        def replace(self, old_value: System_Collections_Immutable_ImmutableList_T, new_value: System_Collections_Immutable_ImmutableList_T) -> None:
            """
            Replaces the first equal element in the list with the specified element.
            
            :param old_value: The element to replace.
            :param new_value: The element to replace the old element with.
            """
            ...

        @overload
        def replace(self, old_value: System_Collections_Immutable_ImmutableList_T, new_value: System_Collections_Immutable_ImmutableList_T, equality_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableList_T]) -> None:
            """
            Replaces the first equal element in the list with the specified element.
            
            :param old_value: The element to replace.
            :param new_value: The element to replace the old element with.
            :param equality_comparer: The equality comparer to use in the search. If null, EqualityComparer{T}.Default is used.
            """
            ...

        @overload
        def reverse(self) -> None:
            """Reverses the order of the elements in the entire ImmutableList<T>."""
            ...

        @overload
        def reverse(self, index: int, count: int) -> None:
            """
            Reverses the order of the elements in the specified range.
            
            :param index: The zero-based starting index of the range to reverse.
            :param count: The number of elements in the range to reverse.
            """
            ...

        @overload
        def sort(self) -> None:
            """
            Sorts the elements in the entire ImmutableList<T> using
            the default comparer.
            """
            ...

        @overload
        def sort(self, comparison: typing.Callable[[System_Collections_Immutable_ImmutableList_T, System_Collections_Immutable_ImmutableList_T], int]) -> None:
            """
            Sorts the elements in the entire ImmutableList<T> using
            the specified System.Comparison<T>.
            
            :param comparison: The Comparison{T} to use when comparing elements.
            """
            ...

        @overload
        def sort(self, comparer: System.Collections.Generic.IComparer[System_Collections_Immutable_ImmutableList_T]) -> None:
            """
            Sorts the elements in the entire ImmutableList<T> using
            the specified comparer.
            
            :param comparer: The IComparer{T} implementation to use when comparing elements, or null to use Comparer{T}.Default.
            """
            ...

        @overload
        def sort(self, index: int, count: int, comparer: System.Collections.Generic.IComparer[System_Collections_Immutable_ImmutableList_T]) -> None:
            """
            Sorts the elements in a range of elements in ImmutableList<T>
            using the specified comparer.
            
            :param index: The zero-based starting index of the range to sort.
            :param count: The length of the range to sort.
            :param comparer: The IComparer{T} implementation to use when comparing elements, or null to use Comparer{T}.Default.
            """
            ...

        def to_immutable(self) -> System.Collections.Immutable.ImmutableList[System_Collections_Immutable_ImmutableList_T]:
            """
            Creates an immutable list based on the contents of this instance.
            
            :returns: An immutable list.
            """
            ...

        def true_for_all(self, match: typing.Callable[[System_Collections_Immutable_ImmutableList_T], bool]) -> bool:
            """
            Determines whether every element in the ImmutableList<T>
            matches the conditions defined by the specified predicate.
            
            :param match: The System.Predicate<T> delegate that defines the conditions to check against the elements.
            :returns: true if every element in the ImmutableList<T> matches the conditions defined by the specified predicate; otherwise, false. If the list has no elements, the return value is true.
            """
            ...

    EMPTY: System.Collections.Immutable.ImmutableList[System_Collections_Immutable_ImmutableList_T] = ...
    """An empty immutable list."""

    @property
    def is_empty(self) -> bool:
        """See the IImmutableList{T} interface."""
        ...

    @property
    def count(self) -> int:
        """See the IImmutableList{T} interface."""
        ...

    def __getitem__(self, index: int) -> System_Collections_Immutable_ImmutableList_T:
        """
        Gets the element of the set at the given index.
        
        :param index: The 0-based index of the element in the set to return.
        :returns: The element at the given position.
        """
        ...

    def __iter__(self) -> typing.Iterator[System_Collections_Immutable_ImmutableList_T]:
        ...

    def add(self, value: System_Collections_Immutable_ImmutableList_T) -> System.Collections.Immutable.ImmutableList[System_Collections_Immutable_ImmutableList_T]:
        """See the IImmutableList{T} interface."""
        ...

    def add_range(self, items: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableList_T]) -> System.Collections.Immutable.ImmutableList[System_Collections_Immutable_ImmutableList_T]:
        """See the IImmutableList{T} interface."""
        ...

    @overload
    def binary_search(self, item: System_Collections_Immutable_ImmutableList_T) -> int:
        """
        Searches the entire sorted ImmutableList{T} for an element
        using the default comparer and returns the zero-based index of the element.
        
        :param item: The object to locate. The value can be null for reference types.
        :returns: The zero-based index of item in the sorted ImmutableList{T}, if item is found; otherwise, a negative number that is the bitwise complement of the index of the next element that is larger than item or, if there is no larger element, the bitwise complement of ImmutableList{T}.Count.
        """
        ...

    @overload
    def binary_search(self, item: System_Collections_Immutable_ImmutableList_T, comparer: System.Collections.Generic.IComparer[System_Collections_Immutable_ImmutableList_T]) -> int:
        """
        Searches the entire sorted ImmutableList{T} for an element
         using the specified comparer and returns the zero-based index of the element.
        
        :param item: The object to locate. The value can be null for reference types.
        :param comparer: The IComparer{T} implementation to use when comparing elements.-or-null to use the default comparer Comparer{T}.Default.
        :returns: The zero-based index of item in the sorted ImmutableList{T}, if item is found; otherwise, a negative number that is the bitwise complement of the index of the next element that is larger than item or, if there is no larger element, the bitwise complement of ImmutableList{T}.Count.
        """
        ...

    @overload
    def binary_search(self, index: int, count: int, item: System_Collections_Immutable_ImmutableList_T, comparer: System.Collections.Generic.IComparer[System_Collections_Immutable_ImmutableList_T]) -> int:
        """
        Searches a range of elements in the sorted ImmutableList{T}
        for an element using the specified comparer and returns the zero-based index
        of the element.
        
        :param index: The zero-based starting index of the range to search.
        :param count: The length of the range to search.
        :param item: The object to locate. The value can be null for reference types.
        :param comparer: The IComparer{T} implementation to use when comparing elements, or null to use the default comparer Comparer{T}.Default.
        :returns: The zero-based index of item in the sorted ImmutableList{T}, if item is found; otherwise, a negative number that is the bitwise complement of the index of the next element that is larger than item or, if there is no larger element, the bitwise complement of ImmutableList{T}.Count.
        """
        ...

    def clear(self) -> System.Collections.Immutable.ImmutableList[System_Collections_Immutable_ImmutableList_T]:
        """See the IImmutableList{T} interface."""
        ...

    def contains(self, value: System_Collections_Immutable_ImmutableList_T) -> bool:
        """See the IImmutableList{T} interface."""
        ...

    @overload
    def copy_to(self, array: typing.List[System_Collections_Immutable_ImmutableList_T]) -> None:
        """
        Copies the entire ImmutableList{T} to a compatible one-dimensional
        array, starting at the beginning of the target array.
        
        :param array: The one-dimensional Array that is the destination of the elements copied from ImmutableList{T}. The Array must have zero-based indexing.
        """
        ...

    @overload
    def copy_to(self, array: typing.List[System_Collections_Immutable_ImmutableList_T], array_index: int) -> None:
        """
        Copies the entire ImmutableList{T} to a compatible one-dimensional
        array, starting at the specified index of the target array.
        
        :param array: The one-dimensional Array that is the destination of the elements copied from ImmutableList{T}. The Array must have zero-based indexing.
        :param array_index: The zero-based index in array at which copying begins.
        """
        ...

    @overload
    def copy_to(self, index: int, array: typing.List[System_Collections_Immutable_ImmutableList_T], array_index: int, count: int) -> None:
        """
        Copies a range of elements from the ImmutableList{T} to
        a compatible one-dimensional array, starting at the specified index of the
        target array.
        
        :param index: The zero-based index in the source ImmutableList{T} at which copying begins.
        :param array: The one-dimensional Array that is the destination of the elements copied from ImmutableList{T}. The Array must have zero-based indexing.
        :param array_index: The zero-based index in array at which copying begins.
        :param count: The number of elements to copy.
        """
        ...

    def exists(self, match: typing.Callable[[System_Collections_Immutable_ImmutableList_T], bool]) -> bool:
        """
        Determines whether the ImmutableList{T} contains elements
        that match the conditions defined by the specified predicate.
        
        :param match: The Predicate{T} delegate that defines the conditions of the elements to search for.
        :returns: true if the ImmutableList{T} contains one or more elements that match the conditions defined by the specified predicate; otherwise, false.
        """
        ...

    def find(self, match: typing.Callable[[System_Collections_Immutable_ImmutableList_T], bool]) -> System_Collections_Immutable_ImmutableList_T:
        """
        Searches for an element that matches the conditions defined by the specified
        predicate, and returns the first occurrence within the entire ImmutableList{T}.
        
        :param match: The Predicate{T} delegate that defines the conditions of the element to search for.
        :returns: The first element that matches the conditions defined by the specified predicate, if found; otherwise, the default value for type T.
        """
        ...

    def find_all(self, match: typing.Callable[[System_Collections_Immutable_ImmutableList_T], bool]) -> System.Collections.Immutable.ImmutableList[System_Collections_Immutable_ImmutableList_T]:
        """
        Retrieves all the elements that match the conditions defined by the specified
        predicate.
        
        :param match: The Predicate{T} delegate that defines the conditions of the elements to search for.
        :returns: A ImmutableList{T} containing all the elements that match the conditions defined by the specified predicate, if found; otherwise, an empty ImmutableList{T}.
        """
        ...

    @overload
    def find_index(self, match: typing.Callable[[System_Collections_Immutable_ImmutableList_T], bool]) -> int:
        """
        Searches for an element that matches the conditions defined by the specified
        predicate, and returns the zero-based index of the first occurrence within
        the entire ImmutableList{T}.
        
        :param match: The Predicate{T} delegate that defines the conditions of the element to search for.
        :returns: The zero-based index of the first occurrence of an element that matches the conditions defined by , if found; otherwise, -1.
        """
        ...

    @overload
    def find_index(self, start_index: int, match: typing.Callable[[System_Collections_Immutable_ImmutableList_T], bool]) -> int:
        """
        Searches for an element that matches the conditions defined by the specified
        predicate, and returns the zero-based index of the first occurrence within
        the range of elements in the ImmutableList{T} that extends
        from the specified index to the last element.
        
        :param start_index: The zero-based starting index of the search.
        :param match: The Predicate{T} delegate that defines the conditions of the element to search for.
        :returns: The zero-based index of the first occurrence of an element that matches the conditions defined by , if found; otherwise, -1.
        """
        ...

    @overload
    def find_index(self, start_index: int, count: int, match: typing.Callable[[System_Collections_Immutable_ImmutableList_T], bool]) -> int:
        """
        Searches for an element that matches the conditions defined by the specified
        predicate, and returns the zero-based index of the first occurrence within
        the range of elements in the ImmutableList{T} that starts
        at the specified index and contains the specified number of elements.
        
        :param start_index: The zero-based starting index of the search.
        :param count: The number of elements in the section to search.
        :param match: The Predicate{T} delegate that defines the conditions of the element to search for.
        :returns: The zero-based index of the first occurrence of an element that matches the conditions defined by , if found; otherwise, -1.
        """
        ...

    def find_last(self, match: typing.Callable[[System_Collections_Immutable_ImmutableList_T], bool]) -> System_Collections_Immutable_ImmutableList_T:
        """
        Searches for an element that matches the conditions defined by the specified
        predicate, and returns the last occurrence within the entire ImmutableList{T}.
        
        :param match: The Predicate{T} delegate that defines the conditions of the element to search for.
        :returns: The last element that matches the conditions defined by the specified predicate, if found; otherwise, the default value for type T.
        """
        ...

    @overload
    def find_last_index(self, match: typing.Callable[[System_Collections_Immutable_ImmutableList_T], bool]) -> int:
        """
        Searches for an element that matches the conditions defined by the specified
        predicate, and returns the zero-based index of the last occurrence within
        the entire ImmutableList{T}.
        
        :param match: The Predicate{T} delegate that defines the conditions of the element to search for.
        :returns: The zero-based index of the last occurrence of an element that matches the conditions defined by , if found; otherwise, -1.
        """
        ...

    @overload
    def find_last_index(self, start_index: int, match: typing.Callable[[System_Collections_Immutable_ImmutableList_T], bool]) -> int:
        """
        Searches for an element that matches the conditions defined by the specified
        predicate, and returns the zero-based index of the last occurrence within
        the range of elements in the ImmutableList{T} that extends
        from the first element to the specified index.
        
        :param start_index: The zero-based starting index of the backward search.
        :param match: The Predicate{T} delegate that defines the conditions of the element to search for.
        :returns: The zero-based index of the last occurrence of an element that matches the conditions defined by , if found; otherwise, -1.
        """
        ...

    @overload
    def find_last_index(self, start_index: int, count: int, match: typing.Callable[[System_Collections_Immutable_ImmutableList_T], bool]) -> int:
        """
        Searches for an element that matches the conditions defined by the specified
        predicate, and returns the zero-based index of the last occurrence within
        the range of elements in the ImmutableList{T} that contains
        the specified number of elements and ends at the specified index.
        
        :param start_index: The zero-based starting index of the backward search.
        :param count: The number of elements in the section to search.
        :param match: The Predicate{T} delegate that defines the conditions of the element to search for.
        :returns: The zero-based index of the last occurrence of an element that matches the conditions defined by , if found; otherwise, -1.
        """
        ...

    def for_each(self, action: typing.Callable[[System_Collections_Immutable_ImmutableList_T], None]) -> None:
        """
        Performs the specified action on each element of the list.
        
        :param action: The System.Action<T> delegate to perform on each element of the list.
        """
        ...

    def get_enumerator(self) -> System.Collections.Immutable.ImmutableList.Enumerator:
        """
        Returns an enumerator that iterates through the collection.
        
        :returns: A IEnumerator{T} that can be used to iterate through the collection.
        """
        ...

    def get_range(self, index: int, count: int) -> System.Collections.Immutable.ImmutableList[System_Collections_Immutable_ImmutableList_T]:
        """
        Creates a shallow copy of a range of elements in the source ImmutableList{T}.
        
        :param index: The zero-based ImmutableList{T} index at which the range starts.
        :param count: The number of elements in the range.
        :returns: A shallow copy of a range of elements in the source ImmutableList{T}.
        """
        ...

    @overload
    def index_of(self, item: System_Collections_Immutable_ImmutableList_T, index: int, count: int, equality_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableList_T]) -> int:
        """
        Searches for the specified object and returns the zero-based index of the
        first occurrence within the range of elements in the ImmutableList{T}
        that starts at the specified index and contains the specified number of elements.
        
        :param item: The object to locate in the ImmutableList{T}. The value can be null for reference types.
        :param index: The zero-based starting index of the search. 0 (zero) is valid in an empty list.
        :param count: The number of elements in the section to search.
        :param equality_comparer: The equality comparer to use in the search.
        :returns: The zero-based index of the first occurrence of  within the range of elements in the ImmutableList{T} that starts at  and contains  number of elements, if found; otherwise, -1.
        """
        ...

    @overload
    def index_of(self, value: System_Collections_Immutable_ImmutableList_T) -> int:
        """See the IImmutableList{T} interface."""
        ...

    def insert(self, index: int, item: System_Collections_Immutable_ImmutableList_T) -> System.Collections.Immutable.ImmutableList[System_Collections_Immutable_ImmutableList_T]:
        """See the IImmutableList{T} interface."""
        ...

    def insert_range(self, index: int, items: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableList_T]) -> System.Collections.Immutable.ImmutableList[System_Collections_Immutable_ImmutableList_T]:
        """See the IImmutableList{T} interface."""
        ...

    def item_ref(self, index: int) -> typing.Any:
        """
        Gets a read-only reference to the element of the set at the given index.
        
        :param index: The 0-based index of the element in the set to return.
        :returns: A read-only reference to the element at the given position.
        """
        ...

    def last_index_of(self, item: System_Collections_Immutable_ImmutableList_T, index: int, count: int, equality_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableList_T]) -> int:
        """
        Searches for the specified object and returns the zero-based index of the
        last occurrence within the range of elements in the ImmutableList{T}
        that contains the specified number of elements and ends at the specified
        index.
        
        :param item: The object to locate in the ImmutableList{T}. The value can be null for reference types.
        :param index: The zero-based starting index of the backward search.
        :param count: The number of elements in the section to search.
        :param equality_comparer: The equality comparer to use in the search.
        :returns: The zero-based index of the last occurrence of  within the range of elements in the ImmutableList{T} that contains  number of elements and ends at , if found; otherwise, -1.
        """
        ...

    @overload
    def remove(self, value: System_Collections_Immutable_ImmutableList_T) -> System.Collections.Immutable.ImmutableList[System_Collections_Immutable_ImmutableList_T]:
        """See the IImmutableList{T} interface."""
        ...

    @overload
    def remove(self, value: System_Collections_Immutable_ImmutableList_T, equality_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableList_T]) -> System.Collections.Immutable.ImmutableList[System_Collections_Immutable_ImmutableList_T]:
        """See the IImmutableList{T} interface."""
        ...

    def remove_all(self, match: typing.Callable[[System_Collections_Immutable_ImmutableList_T], bool]) -> System.Collections.Immutable.ImmutableList[System_Collections_Immutable_ImmutableList_T]:
        """
        Removes all the elements that match the conditions defined by the specified
        predicate.
        
        :param match: The Predicate{T} delegate that defines the conditions of the elements to remove.
        :returns: The new list.
        """
        ...

    def remove_at(self, index: int) -> System.Collections.Immutable.ImmutableList[System_Collections_Immutable_ImmutableList_T]:
        """See the IImmutableList{T} interface."""
        ...

    @overload
    def remove_range(self, index: int, count: int) -> System.Collections.Immutable.ImmutableList[System_Collections_Immutable_ImmutableList_T]:
        """
        Removes the specified values from this list.
        
        :param index: The starting index to begin removal.
        :param count: The number of elements to remove.
        :returns: A new list with the elements removed.
        """
        ...

    @overload
    def remove_range(self, items: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableList_T]) -> System.Collections.Immutable.ImmutableList[System_Collections_Immutable_ImmutableList_T]:
        """
        Removes the specified values from this list.
        
        :param items: The items to remove if matches are found in this list.
        :returns: A new list with the elements removed.
        """
        ...

    @overload
    def remove_range(self, items: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableList_T], equality_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableList_T]) -> System.Collections.Immutable.ImmutableList[System_Collections_Immutable_ImmutableList_T]:
        """
        Removes the specified values from this list.
        
        :param items: The items to remove if matches are found in this list.
        :param equality_comparer: The equality comparer to use in the search. If null, EqualityComparer{T}.Default is used.
        :returns: A new list with the elements removed.
        """
        ...

    @overload
    def replace(self, old_value: System_Collections_Immutable_ImmutableList_T, new_value: System_Collections_Immutable_ImmutableList_T) -> System.Collections.Immutable.ImmutableList[System_Collections_Immutable_ImmutableList_T]:
        """See the IImmutableList{T} interface."""
        ...

    @overload
    def replace(self, old_value: System_Collections_Immutable_ImmutableList_T, new_value: System_Collections_Immutable_ImmutableList_T, equality_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableList_T]) -> System.Collections.Immutable.ImmutableList[System_Collections_Immutable_ImmutableList_T]:
        """See the IImmutableList{T} interface."""
        ...

    @overload
    def reverse(self) -> System.Collections.Immutable.ImmutableList[System_Collections_Immutable_ImmutableList_T]:
        """
        Reverses the order of the elements in the entire ImmutableList{T}.
        
        :returns: The reversed list.
        """
        ...

    @overload
    def reverse(self, index: int, count: int) -> System.Collections.Immutable.ImmutableList[System_Collections_Immutable_ImmutableList_T]:
        """
        Reverses the order of the elements in the specified range.
        
        :param index: The zero-based starting index of the range to reverse.
        :param count: The number of elements in the range to reverse.
        :returns: The reversed list.
        """
        ...

    def set_item(self, index: int, value: System_Collections_Immutable_ImmutableList_T) -> System.Collections.Immutable.ImmutableList[System_Collections_Immutable_ImmutableList_T]:
        """See the IImmutableList{T} interface."""
        ...

    @overload
    def sort(self) -> System.Collections.Immutable.ImmutableList[System_Collections_Immutable_ImmutableList_T]:
        """
        Sorts the elements in the entire ImmutableList{T} using
        the default comparer.
        """
        ...

    @overload
    def sort(self, comparison: typing.Callable[[System_Collections_Immutable_ImmutableList_T, System_Collections_Immutable_ImmutableList_T], int]) -> System.Collections.Immutable.ImmutableList[System_Collections_Immutable_ImmutableList_T]:
        """
        Sorts the elements in the entire ImmutableList{T} using
        the specified Comparison{T}.
        
        :param comparison: The Comparison{T} to use when comparing elements.
        :returns: The sorted list.
        """
        ...

    @overload
    def sort(self, comparer: System.Collections.Generic.IComparer[System_Collections_Immutable_ImmutableList_T]) -> System.Collections.Immutable.ImmutableList[System_Collections_Immutable_ImmutableList_T]:
        """
        Sorts the elements in the entire ImmutableList{T} using
        the specified comparer.
        
        :param comparer: The IComparer{T} implementation to use when comparing elements, or null to use the default comparer Comparer{T}.Default.
        :returns: The sorted list.
        """
        ...

    @overload
    def sort(self, index: int, count: int, comparer: System.Collections.Generic.IComparer[System_Collections_Immutable_ImmutableList_T]) -> System.Collections.Immutable.ImmutableList[System_Collections_Immutable_ImmutableList_T]:
        """
        Sorts the elements in a range of elements in ImmutableList{T}
        using the specified comparer.
        
        :param index: The zero-based starting index of the range to sort.
        :param count: The length of the range to sort.
        :param comparer: The IComparer{T} implementation to use when comparing elements, or null to use the default comparer Comparer{T}.Default.
        :returns: The sorted list.
        """
        ...

    def to_builder(self) -> System.Collections.Immutable.ImmutableList.Builder:
        """
        Creates a collection with the same contents as this collection that
        can be efficiently mutated across multiple operations using standard
        mutable interfaces.
        """
        ...

    def true_for_all(self, match: typing.Callable[[System_Collections_Immutable_ImmutableList_T], bool]) -> bool:
        """
        Determines whether every element in the ImmutableList{T}
        matches the conditions defined by the specified predicate.
        
        :param match: The Predicate{T} delegate that defines the conditions to check against the elements.
        :returns: true if every element in the ImmutableList{T} matches the conditions defined by the specified predicate; otherwise, false. If the list has no elements, the return value is true.
        """
        ...


class ImmutableArray(typing.Generic[System_Collections_Immutable_ImmutableArray_T], System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableArray_T], System.IEquatable[System_Collections_Immutable_ImmutableArray], System.Collections.Immutable.IImmutableArray, System.Collections.Generic.IList[System_Collections_Immutable_ImmutableArray_T], System.Collections.IList, System.Collections.IStructuralComparable, System.Collections.IStructuralEquatable, System.Collections.Immutable.IImmutableList[System_Collections_Immutable_ImmutableArray_T], typing.Iterable[System_Collections_Immutable_ImmutableArray_T]):
    """A readonly array with O(1) indexable lookup time."""

    class Enumerator:
        """An array enumerator."""

        @property
        def current(self) -> System_Collections_Immutable_ImmutableArray_T:
            """Gets the currently enumerated value."""
            ...

        def move_next(self) -> bool:
            """
            Advances to the next value to be enumerated.
            
            :returns: true if another item exists in the array; false otherwise.
            """
            ...

    class Builder(System.Object, System.Collections.Generic.IList[System_Collections_Immutable_ImmutableArray_T], System.Collections.Generic.IReadOnlyList[System_Collections_Immutable_ImmutableArray_T], typing.Iterable[System_Collections_Immutable_ImmutableArray_T]):
        """
        A writable array accessor that can be converted into an ImmutableArray{T}
        instance without allocating memory.
        """

        @property
        def capacity(self) -> int:
            """
            Get and sets the length of the internal array.  When set the internal array is
            reallocated to the given capacity if it is not already the specified length.
            """
            ...

        @capacity.setter
        def capacity(self, value: int) -> None:
            ...

        @property
        def count(self) -> int:
            """Gets or sets the length of the builder."""
            ...

        @count.setter
        def count(self, value: int) -> None:
            ...

        def __getitem__(self, index: int) -> System_Collections_Immutable_ImmutableArray_T:
            """
            Gets or sets the element at the specified index.
            
            :param index: The index.
            """
            ...

        def __iter__(self) -> typing.Iterator[System_Collections_Immutable_ImmutableArray_T]:
            ...

        def __setitem__(self, index: int, value: System_Collections_Immutable_ImmutableArray_T) -> None:
            """
            Gets or sets the element at the specified index.
            
            :param index: The index.
            """
            ...

        def add(self, item: System_Collections_Immutable_ImmutableArray_T) -> None:
            """
            Adds an item to the ICollection{T}.
            
            :param item: The object to add to the ICollection{T}.
            """
            ...

        @overload
        def add_range(self, items: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableArray_T]) -> None:
            """
            Adds the specified items to the end of the array.
            
            :param items: The items.
            """
            ...

        @overload
        def add_range(self, *items: typing.Union[System_Collections_Immutable_ImmutableArray_T, typing.Iterable[System_Collections_Immutable_ImmutableArray_T]]) -> None:
            """
            Adds the specified items to the end of the array.
            
            :param items: The items.
            """
            ...

        @overload
        def add_range(self, items: typing.List[System_Collections_Immutable_ImmutableArray_T], length: int) -> None:
            """
            Adds the specified items to the end of the array.
            
            :param items: The items.
            :param length: The number of elements from the source array to add.
            """
            ...

        @overload
        def add_range(self, items: System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]) -> None:
            """
            Adds the specified items to the end of the array.
            
            :param items: The items.
            """
            ...

        @overload
        def add_range(self, items: System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T], length: int) -> None:
            """
            Adds the specified items to the end of the array.
            
            :param items: The items.
            :param length: The number of elements from the source array to add.
            """
            ...

        @overload
        def add_range(self, items: System.Collections.Immutable.ImmutableArray.Builder) -> None:
            """
            Adds the specified items to the end of the array.
            
            :param items: The items to add at the end of the array.
            """
            ...

        def clear(self) -> None:
            """Removes all items from the ICollection{T}."""
            ...

        def contains(self, item: System_Collections_Immutable_ImmutableArray_T) -> bool:
            """
            Determines whether the ICollection{T} contains a specific value.
            
            :param item: The object to locate in the ICollection{T}.
            :returns: true if  is found in the ICollection{T}; otherwise, false.
            """
            ...

        @overload
        def copy_to(self, array: typing.List[System_Collections_Immutable_ImmutableArray_T], index: int) -> None:
            """
            Copies the current contents to the specified array.
            
            :param array: The array to copy to.
            :param index: The starting index of the target array.
            """
            ...

        @overload
        def copy_to(self, destination: typing.List[System_Collections_Immutable_ImmutableArray_T]) -> None:
            """
            Copies the contents of this array to the specified array.
            
            :param destination: The array to copy to.
            """
            ...

        @overload
        def copy_to(self, source_index: int, destination: typing.List[System_Collections_Immutable_ImmutableArray_T], destination_index: int, length: int) -> None:
            """
            Copies the contents of this array to the specified array.
            
            :param source_index: The index into this collection of the first element to copy.
            :param destination: The array to copy to.
            :param destination_index: The index into the destination array to which the first copied element is written.
            :param length: The number of elements to copy.
            """
            ...

        @overload
        def copy_to(self, destination: System.Span[System_Collections_Immutable_ImmutableArray_T]) -> None:
            """
            Copies the current contents to the specified Span{T}.
            
            :param destination: The Span{T} to copy to.
            """
            ...

        def drain_to_immutable(self) -> System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]:
            """
            Returns the current contents as an ImmutableArray{T} and sets the collection to a zero length array.
            
            :returns: An immutable array.
            """
            ...

        def get_enumerator(self) -> System.Collections.Generic.IEnumerator[System_Collections_Immutable_ImmutableArray_T]:
            """
            Returns an enumerator for the contents of the array.
            
            :returns: An enumerator.
            """
            ...

        @overload
        def index_of(self, item: System_Collections_Immutable_ImmutableArray_T) -> int:
            """
            Determines the index of a specific item in the IList{T}.
            
            :param item: The object to locate in the IList{T}.
            :returns: The index of  if found in the list; otherwise, -1.
            """
            ...

        @overload
        def index_of(self, item: System_Collections_Immutable_ImmutableArray_T, start_index: int) -> int:
            """
            Searches the array for the specified item.
            
            :param item: The item to search for.
            :param start_index: The index at which to begin the search.
            :returns: The 0-based index into the array where the item was found; or -1 if it could not be found.
            """
            ...

        @overload
        def index_of(self, item: System_Collections_Immutable_ImmutableArray_T, start_index: int, count: int) -> int:
            """
            Searches the array for the specified item.
            
            :param item: The item to search for.
            :param start_index: The index at which to begin the search.
            :param count: The number of elements to search.
            :returns: The 0-based index into the array where the item was found; or -1 if it could not be found.
            """
            ...

        @overload
        def index_of(self, item: System_Collections_Immutable_ImmutableArray_T, start_index: int, count: int, equality_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableArray_T]) -> int:
            """
            Searches the array for the specified item.
            
            :param item: The item to search for.
            :param start_index: The index at which to begin the search.
            :param count: The number of elements to search.
            :param equality_comparer: The equality comparer to use in the search. If null, EqualityComparer{T}.Default is used.
            :returns: The 0-based index into the array where the item was found; or -1 if it could not be found.
            """
            ...

        @overload
        def index_of(self, item: System_Collections_Immutable_ImmutableArray_T, start_index: int, equality_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableArray_T]) -> int:
            """
            Searches the array for the specified item.
            
            :param item: The item to search for.
            :param start_index: The index at which to begin the search.
            :param equality_comparer: The equality comparer to use in the search. If null, EqualityComparer{T}.Default is used.
            :returns: The 0-based index into the array where the item was found; or -1 if it could not be found.
            """
            ...

        def insert(self, index: int, item: System_Collections_Immutable_ImmutableArray_T) -> None:
            """
            Inserts an item to the IList{T} at the specified index.
            
            :param index: The zero-based index at which  should be inserted.
            :param item: The object to insert into the IList{T}.
            """
            ...

        @overload
        def insert_range(self, index: int, items: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableArray_T]) -> None:
            """
            Inserts the specified values at the specified index.
            
            :param index: The index at which to insert the value.
            :param items: The elements to insert.
            """
            ...

        @overload
        def insert_range(self, index: int, items: System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]) -> None:
            """
            Inserts the specified values at the specified index.
            
            :param index: The index at which to insert the value.
            :param items: The elements to insert.
            """
            ...

        def item_ref(self, index: int) -> typing.Any:
            """
            Gets a read-only reference to the element at the specified index.
            
            :param index: The index.
            """
            ...

        @overload
        def last_index_of(self, item: System_Collections_Immutable_ImmutableArray_T) -> int:
            """
            Searches the array for the specified item in reverse.
            
            :param item: The item to search for.
            :returns: The 0-based index into the array where the item was found; or -1 if it could not be found.
            """
            ...

        @overload
        def last_index_of(self, item: System_Collections_Immutable_ImmutableArray_T, start_index: int) -> int:
            """
            Searches the array for the specified item in reverse.
            
            :param item: The item to search for.
            :param start_index: The index at which to begin the search.
            :returns: The 0-based index into the array where the item was found; or -1 if it could not be found.
            """
            ...

        @overload
        def last_index_of(self, item: System_Collections_Immutable_ImmutableArray_T, start_index: int, count: int) -> int:
            """
            Searches the array for the specified item in reverse.
            
            :param item: The item to search for.
            :param start_index: The index at which to begin the search.
            :param count: The number of elements to search.
            :returns: The 0-based index into the array where the item was found; or -1 if it could not be found.
            """
            ...

        @overload
        def last_index_of(self, item: System_Collections_Immutable_ImmutableArray_T, start_index: int, count: int, equality_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableArray_T]) -> int:
            """
            Searches the array for the specified item in reverse.
            
            :param item: The item to search for.
            :param start_index: The index at which to begin the search.
            :param count: The number of elements to search.
            :param equality_comparer: The equality comparer to use in the search.
            :returns: The 0-based index into the array where the item was found; or -1 if it could not be found.
            """
            ...

        def move_to_immutable(self) -> System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]:
            """
            Extracts the internal array as an ImmutableArray{T} and replaces it
            with a zero length array.
            """
            ...

        @overload
        def remove(self, element: System_Collections_Immutable_ImmutableArray_T) -> bool:
            """
            Removes the first occurrence of the specified element from the builder.
            If no match is found, the builder remains unchanged.
            
            :param element: The element.
            :returns: A value indicating whether the specified element was found and removed from the collection.
            """
            ...

        @overload
        def remove(self, element: System_Collections_Immutable_ImmutableArray_T, equality_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableArray_T]) -> bool:
            """
            Removes the first occurrence of the specified element from the builder.
            If no match is found, the builder remains unchanged.
            
            :param element: The element to remove.
            :param equality_comparer: The equality comparer to use in the search. If null, EqualityComparer{T}.Default is used.
            :returns: A value indicating whether the specified element was found and removed from the collection.
            """
            ...

        def remove_all(self, match: typing.Callable[[System_Collections_Immutable_ImmutableArray_T], bool]) -> None:
            """
            Removes all the elements that match the conditions defined by the specified
            predicate.
            
            :param match: The Predicate{T} delegate that defines the conditions of the elements to remove.
            """
            ...

        def remove_at(self, index: int) -> None:
            """
            Removes the IList{T} item at the specified index.
            
            :param index: The zero-based index of the item to remove.
            """
            ...

        @overload
        def remove_range(self, index: int, length: int) -> None:
            """
            Removes the specified values from this list.
            
            :param index: The 0-based index into the array for the element to omit from the returned array.
            :param length: The number of elements to remove.
            """
            ...

        @overload
        def remove_range(self, items: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableArray_T]) -> None:
            """
            Removes the specified values from this list.
            
            :param items: The items to remove if matches are found in this list.
            """
            ...

        @overload
        def remove_range(self, items: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableArray_T], equality_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableArray_T]) -> None:
            """
            Removes the specified values from this list.
            
            :param items: The items to remove if matches are found in this list.
            :param equality_comparer: The equality comparer to use in the search. If null, EqualityComparer{T}.Default is used.
            """
            ...

        @overload
        def replace(self, old_value: System_Collections_Immutable_ImmutableArray_T, new_value: System_Collections_Immutable_ImmutableArray_T) -> None:
            """
            Replaces the first equal element in the list with the specified element.
            
            :param old_value: The element to replace.
            :param new_value: The element to replace the old element with.
            """
            ...

        @overload
        def replace(self, old_value: System_Collections_Immutable_ImmutableArray_T, new_value: System_Collections_Immutable_ImmutableArray_T, equality_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableArray_T]) -> None:
            """
            Replaces the first equal element in the list with the specified element.
            
            :param old_value: The element to replace.
            :param new_value: The element to replace the old element with.
            :param equality_comparer: The equality comparer to use in the search. If null, EqualityComparer{T}.Default is used.
            """
            ...

        def reverse(self) -> None:
            """Reverses the order of elements in the collection."""
            ...

        @overload
        def sort(self) -> None:
            """Sorts the array."""
            ...

        @overload
        def sort(self, comparison: typing.Callable[[System_Collections_Immutable_ImmutableArray_T, System_Collections_Immutable_ImmutableArray_T], int]) -> None:
            """
            Sorts the elements in the entire array using
            the specified Comparison{T}.
            
            :param comparison: The Comparison{T} to use when comparing elements.
            """
            ...

        @overload
        def sort(self, comparer: System.Collections.Generic.IComparer[System_Collections_Immutable_ImmutableArray_T]) -> None:
            """
            Sorts the array.
            
            :param comparer: The comparer to use in sorting. If null, the default comparer is used.
            """
            ...

        @overload
        def sort(self, index: int, count: int, comparer: System.Collections.Generic.IComparer[System_Collections_Immutable_ImmutableArray_T]) -> None:
            """
            Sorts the array.
            
            :param index: The index of the first element to consider in the sort.
            :param count: The number of elements to include in the sort.
            :param comparer: The comparer to use in sorting. If null, the default comparer is used.
            """
            ...

        def to_array(self) -> typing.List[System_Collections_Immutable_ImmutableArray_T]:
            """Creates a new array with the current contents of this Builder."""
            ...

        def to_immutable(self) -> System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]:
            """
            Returns an immutable copy of the current contents of this collection.
            
            :returns: An immutable array.
            """
            ...

    EMPTY: System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T] = ...

    @property
    def is_empty(self) -> bool:
        """Gets a value indicating whether this collection is empty."""
        ...

    @property
    def length(self) -> int:
        """Gets the number of elements in the array."""
        ...

    @property
    def is_default(self) -> bool:
        """Gets a value indicating whether this struct was initialized without an actual array instance."""
        ...

    @property
    def is_default_or_empty(self) -> bool:
        """Gets a value indicating whether this struct is empty or uninitialized."""
        ...

    @overload
    def __eq__(self, right: System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]) -> bool:
        """
        Checks equality between two instances.
        
        :param left: The instance to the left of the operator.
        :param right: The instance to the right of the operator.
        :returns: true if the values' underlying arrays are reference equal; false otherwise.
        """
        ...

    @overload
    def __eq__(self, right: typing.Optional[System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]]) -> bool:
        """
        Checks equality between two instances.
        
        :param left: The instance to the left of the operator.
        :param right: The instance to the right of the operator.
        :returns: true if the values' underlying arrays are reference equal; false otherwise.
        """
        ...

    def __getitem__(self, index: int) -> System_Collections_Immutable_ImmutableArray_T:
        """
        Gets the element at the specified index in the read-only list.
        
        :param index: The zero-based index of the element to get.
        :returns: The element at the specified index in the read-only list.
        """
        ...

    def __iter__(self) -> typing.Iterator[System_Collections_Immutable_ImmutableArray_T]:
        ...

    @overload
    def __ne__(self, right: System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]) -> bool:
        """
        Checks inequality between two instances.
        
        :param left: The instance to the left of the operator.
        :param right: The instance to the right of the operator.
        :returns: true if the values' underlying arrays are reference not equal; false otherwise.
        """
        ...

    @overload
    def __ne__(self, right: typing.Optional[System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]]) -> bool:
        """
        Checks inequality between two instances.
        
        :param left: The instance to the left of the operator.
        :param right: The instance to the right of the operator.
        :returns: true if the values' underlying arrays are reference not equal; false otherwise.
        """
        ...

    def add(self, item: System_Collections_Immutable_ImmutableArray_T) -> System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]:
        """
        Returns a new array with the specified value inserted at the end.
        
        :param item: The item to insert at the end of the array.
        :returns: A new array.
        """
        ...

    @overload
    def add_range(self, items: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableArray_T]) -> System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]:
        """
        Adds the specified values to this list.
        
        :param items: The values to add.
        :returns: A new list with the elements added.
        """
        ...

    @overload
    def add_range(self, items: typing.List[System_Collections_Immutable_ImmutableArray_T], length: int) -> System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]:
        """
        Adds the specified items to the end of the array.
        
        :param items: The values to add.
        :param length: The number of elements from the source array to add.
        :returns: A new list with the elements added.
        """
        ...

    @overload
    def add_range(self, items: System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T], length: int) -> System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]:
        """
        Adds the specified items to the end of the array.
        
        :param items: The values to add.
        :param length: The number of elements from the source array to add.
        :returns: A new list with the elements added.
        """
        ...

    @overload
    def add_range(self, items: System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]) -> System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]:
        """
        Adds the specified values to this list.
        
        :param items: The values to add.
        :returns: A new list with the elements added.
        """
        ...

    @overload
    def add_range(self, *items: typing.Union[System_Collections_Immutable_ImmutableArray_T, typing.Iterable[System_Collections_Immutable_ImmutableArray_T]]) -> System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]:
        """
        Adds the specified values to this list.
        
        :param items: The values to add.
        :returns: A new list with the elements added.
        """
        ...

    def as_memory(self) -> System.ReadOnlyMemory[System_Collections_Immutable_ImmutableArray_T]:
        """
        Creates a new read-only memory region over this immutable array.
        
        :returns: The read-only memory representation of this immutable array.
        """
        ...

    @overload
    def as_span(self, range: System.Range) -> System.ReadOnlySpan[System_Collections_Immutable_ImmutableArray_T]:
        """
        Creates a ReadOnlySpan{T} over the portion of current ImmutableArray{T} based on specified
        
        :param range: Range in current ImmutableArray{T}.
        :returns: The ReadOnlySpan{T} representation of the ImmutableArray{T}.
        """
        ...

    @overload
    def as_span(self) -> System.ReadOnlySpan[System_Collections_Immutable_ImmutableArray_T]:
        """
        Creates a new read-only span over this immutable array.
        
        :returns: The read-only span representation of this immutable array.
        """
        ...

    @overload
    def as_span(self, start: int, length: int) -> System.ReadOnlySpan[System_Collections_Immutable_ImmutableArray_T]:
        """
        Creates a ReadOnlySpan{T} over the portion of current ImmutableArray{T} beginning at a specified position for a specified length.
        
        :param start: The index at which to begin the span.
        :param length: The number of items in the span.
        :returns: The ReadOnlySpan{T} representation of the ImmutableArray{T}.
        """
        ...

    def clear(self) -> System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]:
        """Returns an empty array."""
        ...

    @overload
    def contains(self, item: System_Collections_Immutable_ImmutableArray_T) -> bool:
        """
        Determines whether the specified item exists in the array.
        
        :param item: The item to search for.
        :returns: true if an equal value was found in the array; false otherwise.
        """
        ...

    @overload
    def contains(self, item: System_Collections_Immutable_ImmutableArray_T, equality_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableArray_T]) -> bool:
        """
        Determines whether the specified item exists in the array.
        
        :param item: The item to search for.
        :param equality_comparer: The equality comparer to use in the search. If null, EqualityComparer{T}.Default is used.
        :returns: true if an equal value was found in the array; false otherwise.
        """
        ...

    @overload
    def copy_to(self, destination: typing.List[System_Collections_Immutable_ImmutableArray_T]) -> None:
        """
        Copies the contents of this array to the specified array.
        
        :param destination: The array to copy to.
        """
        ...

    @overload
    def copy_to(self, destination: typing.List[System_Collections_Immutable_ImmutableArray_T], destination_index: int) -> None:
        """
        Copies the contents of this array to the specified array.
        
        :param destination: The array to copy to.
        :param destination_index: The index into the destination array to which the first copied element is written.
        """
        ...

    @overload
    def copy_to(self, source_index: int, destination: typing.List[System_Collections_Immutable_ImmutableArray_T], destination_index: int, length: int) -> None:
        """
        Copies the contents of this array to the specified array.
        
        :param source_index: The index into this collection of the first element to copy.
        :param destination: The array to copy to.
        :param destination_index: The index into the destination array to which the first copied element is written.
        :param length: The number of elements to copy.
        """
        ...

    @overload
    def copy_to(self, destination: System.Span[System_Collections_Immutable_ImmutableArray_T]) -> None:
        """
        Copies the elements of current ImmutableArray{T} to an Span{T}.
        
        :param destination: The Span{T} that is the destination of the elements copied from current ImmutableArray{T}.
        """
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        """
        Determines whether the specified object is equal to this instance.
        
        :param obj: The object to compare with this instance.
        :returns: true if the specified object is equal to this instance; otherwise, false.
        """
        ...

    @overload
    def equals(self, other: System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]) -> bool:
        """
        Indicates whether the current object is equal to another object of the same type.
        
        :param other: An object to compare with this object.
        :returns: true if the current object is equal to the  parameter; otherwise, false.
        """
        ...

    def get_enumerator(self) -> System.Collections.Immutable.ImmutableArray.Enumerator:
        """
        Returns an enumerator for the contents of the array.
        
        :returns: An enumerator.
        """
        ...

    def get_hash_code(self) -> int:
        """
        Returns a hash code for this instance.
        
        :returns: A hash code for this instance, suitable for use in hashing algorithms and data structures like a hash table.
        """
        ...

    @overload
    def index_of(self, item: System_Collections_Immutable_ImmutableArray_T) -> int:
        """
        Searches the array for the specified item.
        
        :param item: The item to search for.
        :returns: The 0-based index into the array where the item was found; or -1 if it could not be found.
        """
        ...

    @overload
    def index_of(self, item: System_Collections_Immutable_ImmutableArray_T, start_index: int, equality_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableArray_T]) -> int:
        """
        Searches the array for the specified item.
        
        :param item: The item to search for.
        :param start_index: The index at which to begin the search.
        :param equality_comparer: The equality comparer to use in the search.
        :returns: The 0-based index into the array where the item was found; or -1 if it could not be found.
        """
        ...

    @overload
    def index_of(self, item: System_Collections_Immutable_ImmutableArray_T, start_index: int) -> int:
        """
        Searches the array for the specified item.
        
        :param item: The item to search for.
        :param start_index: The index at which to begin the search.
        :returns: The 0-based index into the array where the item was found; or -1 if it could not be found.
        """
        ...

    @overload
    def index_of(self, item: System_Collections_Immutable_ImmutableArray_T, start_index: int, count: int) -> int:
        """
        Searches the array for the specified item.
        
        :param item: The item to search for.
        :param start_index: The index at which to begin the search.
        :param count: The number of elements to search.
        :returns: The 0-based index into the array where the item was found; or -1 if it could not be found.
        """
        ...

    @overload
    def index_of(self, item: System_Collections_Immutable_ImmutableArray_T, start_index: int, count: int, equality_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableArray_T]) -> int:
        """
        Searches the array for the specified item.
        
        :param item: The item to search for.
        :param start_index: The index at which to begin the search.
        :param count: The number of elements to search.
        :param equality_comparer: The equality comparer to use in the search. If null, EqualityComparer{T}.Default is used.
        :returns: The 0-based index into the array where the item was found; or -1 if it could not be found.
        """
        ...

    def insert(self, index: int, item: System_Collections_Immutable_ImmutableArray_T) -> System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]:
        """
        Returns a new array with the specified value inserted at the specified position.
        
        :param index: The 0-based index into the array at which the new item should be added.
        :param item: The item to insert at the start of the array.
        :returns: A new array.
        """
        ...

    @overload
    def insert_range(self, index: int, items: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableArray_T]) -> System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]:
        """
        Inserts the specified values at the specified index.
        
        :param index: The index at which to insert the value.
        :param items: The elements to insert.
        :returns: The new immutable collection.
        """
        ...

    @overload
    def insert_range(self, index: int, items: System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]) -> System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]:
        """
        Inserts the specified values at the specified index.
        
        :param index: The index at which to insert the value.
        :param items: The elements to insert.
        :returns: The new immutable collection.
        """
        ...

    @overload
    def insert_range(self, index: int, items: typing.List[System_Collections_Immutable_ImmutableArray_T]) -> System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]:
        """
        Inserts the specified values at the specified index.
        
        :param index: The index at which to insert the value.
        :param items: The elements to insert.
        :returns: The new immutable collection.
        """
        ...

    @overload
    def insert_range(self, index: int, *items: typing.Union[System_Collections_Immutable_ImmutableArray_T, typing.Iterable[System_Collections_Immutable_ImmutableArray_T]]) -> System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]:
        """
        Inserts the specified values at the specified index.
        
        :param index: The index at which to insert the value.
        :param items: The elements to insert.
        :returns: The new immutable collection.
        """
        ...

    def item_ref(self, index: int) -> typing.Any:
        """
        Gets a read-only reference to the element at the specified index in the read-only list.
        
        :param index: The zero-based index of the element to get a reference to.
        :returns: A read-only reference to the element at the specified index in the read-only list.
        """
        ...

    @overload
    def last_index_of(self, item: System_Collections_Immutable_ImmutableArray_T) -> int:
        """
        Searches the array for the specified item in reverse.
        
        :param item: The item to search for.
        :returns: The 0-based index into the array where the item was found; or -1 if it could not be found.
        """
        ...

    @overload
    def last_index_of(self, item: System_Collections_Immutable_ImmutableArray_T, start_index: int) -> int:
        """
        Searches the array for the specified item in reverse.
        
        :param item: The item to search for.
        :param start_index: The index at which to begin the search.
        :returns: The 0-based index into the array where the item was found; or -1 if it could not be found.
        """
        ...

    @overload
    def last_index_of(self, item: System_Collections_Immutable_ImmutableArray_T, start_index: int, count: int) -> int:
        """
        Searches the array for the specified item in reverse.
        
        :param item: The item to search for.
        :param start_index: The index at which to begin the search.
        :param count: The number of elements to search.
        :returns: The 0-based index into the array where the item was found; or -1 if it could not be found.
        """
        ...

    @overload
    def last_index_of(self, item: System_Collections_Immutable_ImmutableArray_T, start_index: int, count: int, equality_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableArray_T]) -> int:
        """
        Searches the array for the specified item in reverse.
        
        :param item: The item to search for.
        :param start_index: The index at which to begin the search.
        :param count: The number of elements to search.
        :param equality_comparer: The equality comparer to use in the search.
        :returns: The 0-based index into the array where the item was found; or -1 if it could not be found.
        """
        ...

    @overload
    def remove(self, item: System_Collections_Immutable_ImmutableArray_T) -> System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]:
        """
        Returns an array with the first occurrence of the specified element removed from the array.
        If no match is found, the current array is returned.
        
        :param item: The item to remove.
        :returns: The new array.
        """
        ...

    @overload
    def remove(self, item: System_Collections_Immutable_ImmutableArray_T, equality_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableArray_T]) -> System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]:
        """
        Returns an array with the first occurrence of the specified element removed from the array.
        If no match is found, the current array is returned.
        
        :param item: The item to remove.
        :param equality_comparer: The equality comparer to use in the search. If null, EqualityComparer{T}.Default is used.
        :returns: The new array.
        """
        ...

    def remove_all(self, match: typing.Callable[[System_Collections_Immutable_ImmutableArray_T], bool]) -> System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]:
        """
        Removes all the elements that match the conditions defined by the specified
        predicate.
        
        :param match: The Predicate{T} delegate that defines the conditions of the elements to remove.
        :returns: The new list.
        """
        ...

    def remove_at(self, index: int) -> System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]:
        """
        Returns an array with the element at the specified position removed.
        
        :param index: The 0-based index into the array for the element to omit from the returned array.
        :returns: The new array.
        """
        ...

    @overload
    def remove_range(self, index: int, length: int) -> System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]:
        """
        Returns an array with the elements at the specified position removed.
        
        :param index: The 0-based index into the array for the element to omit from the returned array.
        :param length: The number of elements to remove.
        :returns: The new array.
        """
        ...

    @overload
    def remove_range(self, items: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableArray_T]) -> System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]:
        """
        Removes the specified values from this list.
        
        :param items: The items to remove if matches are found in this list.
        :returns: A new list with the elements removed.
        """
        ...

    @overload
    def remove_range(self, items: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableArray_T], equality_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableArray_T]) -> System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]:
        """
        Removes the specified values from this list.
        
        :param items: The items to remove if matches are found in this list.
        :param equality_comparer: The equality comparer to use in the search. If null, EqualityComparer{T}.Default is used.
        :returns: A new list with the elements removed.
        """
        ...

    @overload
    def remove_range(self, items: System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]) -> System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]:
        """
        Removes the specified values from this list.
        
        :param items: The items to remove if matches are found in this list.
        :returns: A new list with the elements removed.
        """
        ...

    @overload
    def remove_range(self, items: System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T], equality_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableArray_T]) -> System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]:
        """
        Removes the specified values from this list.
        
        :param items: The items to remove if matches are found in this list.
        :param equality_comparer: The equality comparer to use in the search.
        :returns: A new list with the elements removed.
        """
        ...

    @overload
    def remove_range(self, items: System.ReadOnlySpan[System_Collections_Immutable_ImmutableArray_T], equality_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableArray_T] = None) -> System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]:
        """
        Removes the specified values from this list.
        
        :param items: The items to remove if matches are found in this list.
        :param equality_comparer: The equality comparer to use in the search.
        :returns: A new list with the elements removed.
        """
        ...

    @overload
    def remove_range(self, items: typing.List[System_Collections_Immutable_ImmutableArray_T], equality_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableArray_T] = None) -> System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]:
        """
        Removes the specified values from this list.
        
        :param items: The items to remove if matches are found in this list.
        :param equality_comparer: The equality comparer to use in the search.
        :returns: A new list with the elements removed.
        """
        ...

    @overload
    def replace(self, old_value: System_Collections_Immutable_ImmutableArray_T, new_value: System_Collections_Immutable_ImmutableArray_T) -> System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]:
        """
        Replaces the first equal element in the list with the specified element.
        
        :param old_value: The element to replace.
        :param new_value: The element to replace the old element with.
        :returns: The new list -- even if the value being replaced is equal to the new value for that position.
        """
        ...

    @overload
    def replace(self, old_value: System_Collections_Immutable_ImmutableArray_T, new_value: System_Collections_Immutable_ImmutableArray_T, equality_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableArray_T]) -> System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]:
        """
        Replaces the first equal element in the list with the specified element.
        
        :param old_value: The element to replace.
        :param new_value: The element to replace the old element with.
        :param equality_comparer: The equality comparer to use in the search. If null, EqualityComparer{T}.Default is used.
        :returns: The new list -- even if the value being replaced is equal to the new value for that position.
        """
        ...

    def set_item(self, index: int, item: System_Collections_Immutable_ImmutableArray_T) -> System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]:
        """
        Returns an array with the item at the specified position replaced.
        
        :param index: The index of the item to replace.
        :param item: The new item.
        :returns: The new array.
        """
        ...

    def slice(self, start: int, length: int) -> System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]:
        """
        Forms a slice out of the current ImmutableArray{T} starting at a specified index for a specified length.
        
        :param start: The index at which to begin this slice.
        :param length: The desired length for the slice.
        :returns: A ImmutableArray{T} that consists of length elements from the current ImmutableArray{T} starting at start.
        """
        ...

    @overload
    def sort(self) -> System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]:
        """Returns a sorted instance of this array."""
        ...

    @overload
    def sort(self, comparison: typing.Callable[[System_Collections_Immutable_ImmutableArray_T, System_Collections_Immutable_ImmutableArray_T], int]) -> System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]:
        """
        Sorts the elements in the entire ImmutableArray{T} using
        the specified Comparison{T}.
        
        :param comparison: The Comparison{T} to use when comparing elements.
        :returns: The sorted list.
        """
        ...

    @overload
    def sort(self, comparer: System.Collections.Generic.IComparer[System_Collections_Immutable_ImmutableArray_T]) -> System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]:
        """
        Returns a sorted instance of this array.
        
        :param comparer: The comparer to use in sorting. If null, the default comparer is used.
        """
        ...

    @overload
    def sort(self, index: int, count: int, comparer: System.Collections.Generic.IComparer[System_Collections_Immutable_ImmutableArray_T]) -> System.Collections.Immutable.ImmutableArray[System_Collections_Immutable_ImmutableArray_T]:
        """
        Returns a sorted instance of this array.
        
        :param index: The index of the first element to consider in the sort.
        :param count: The number of elements to include in the sort.
        :param comparer: The comparer to use in sorting. If null, the default comparer is used.
        """
        ...

    def to_builder(self) -> System.Collections.Immutable.ImmutableArray.Builder:
        """
        Returns a builder that is populated with the same contents as this array.
        
        :returns: The new builder.
        """
        ...


class ImmutableSortedSet(typing.Generic[System_Collections_Immutable_ImmutableSortedSet_T], System.Object, System.Collections.Immutable.IImmutableSet[System_Collections_Immutable_ImmutableSortedSet_T], System.Collections.Generic.IReadOnlyList[System_Collections_Immutable_ImmutableSortedSet_T], System.Collections.Generic.IList[System_Collections_Immutable_ImmutableSortedSet_T], System.Collections.Generic.ISet[System_Collections_Immutable_ImmutableSortedSet_T], System.Collections.IList, System.Collections.Immutable.IStrongEnumerable[System_Collections_Immutable_ImmutableSortedSet_T, System_Collections_Immutable_ImmutableSortedSet_Enumerator], typing.Iterable[System_Collections_Immutable_ImmutableSortedSet_T]):
    """An immutable sorted set implementation."""

    class Builder(System.Object, System.Collections.Generic.IReadOnlyCollection[System_Collections_Immutable_ImmutableSortedSet_T], System.Collections.Generic.ISet[System_Collections_Immutable_ImmutableSortedSet_T], System.Collections.ICollection, typing.Iterable[System_Collections_Immutable_ImmutableSortedSet_T]):
        """
        A sorted set that mutates with little or no memory allocations,
        can produce and/or build on immutable sorted set instances very efficiently.
        """

        @property
        def count(self) -> int:
            """Gets the number of elements in this set."""
            ...

        @property
        def max(self) -> System_Collections_Immutable_ImmutableSortedSet_T:
            """Gets the maximum value in the collection, as defined by the comparer."""
            ...

        @property
        def min(self) -> System_Collections_Immutable_ImmutableSortedSet_T:
            """Gets the minimum value in the collection, as defined by the comparer."""
            ...

        @property
        def key_comparer(self) -> System.Collections.Generic.IComparer[System_Collections_Immutable_ImmutableSortedSet_T]:
            """Gets or sets the IComparer{T} object that is used to determine equality for the values in the ImmutableSortedSet{T}."""
            ...

        @key_comparer.setter
        def key_comparer(self, value: System.Collections.Generic.IComparer[System_Collections_Immutable_ImmutableSortedSet_T]) -> None:
            ...

        def __getitem__(self, index: int) -> System_Collections_Immutable_ImmutableSortedSet_T:
            """
            Gets the element of the set at the given index.
            
            :param index: The 0-based index of the element in the set to return.
            :returns: The element at the given position.
            """
            ...

        def __iter__(self) -> typing.Iterator[System_Collections_Immutable_ImmutableSortedSet_T]:
            ...

        def add(self, item: System_Collections_Immutable_ImmutableSortedSet_T) -> bool:
            """
            Adds an element to the current set and returns a value to indicate if the
            element was successfully added.
            
            :param item: The element to add to the set.
            :returns: true if the element is added to the set; false if the element is already in the set.
            """
            ...

        def clear(self) -> None:
            """Removes all elements from this set."""
            ...

        def contains(self, item: System_Collections_Immutable_ImmutableSortedSet_T) -> bool:
            """
            Determines whether the set contains a specific value.
            
            :param item: The object to locate in the set.
            :returns: true if item is found in the set; false otherwise.
            """
            ...

        def except_with(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableSortedSet_T]) -> None:
            """
            Removes all elements in the specified collection from the current set.
            
            :param other: The collection of items to remove from the set.
            """
            ...

        def get_enumerator(self) -> System.Collections.Immutable.ImmutableSortedSet.Enumerator:
            """
            Returns an enumerator that iterates through the collection.
            
            :returns: A enumerator that can be used to iterate through the collection.
            """
            ...

        def index_of(self, item: System_Collections_Immutable_ImmutableSortedSet_T) -> int:
            """
            Searches for the first index within this set that the specified value is contained.
            
            :param item: The value to locate within the set.
            :returns: The index of the specified  in the sorted set, if  is found.  If  is not found and  is less than one or more elements in this set, a negative number which is the bitwise complement of the index of the first element that is larger than value. If  is not found and  is greater than any of the elements in the set, a negative number which is the bitwise complement of (the index of the last element plus 1).
            """
            ...

        def intersect_with(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableSortedSet_T]) -> None:
            """
            Modifies the current set so that it contains only elements that are also in a specified collection.
            
            :param other: The collection to compare to the current set.
            """
            ...

        def is_proper_subset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableSortedSet_T]) -> bool:
            """
            Determines whether the current set is a proper (strict) subset of a specified collection.
            
            :param other: The collection to compare to the current set.
            :returns: true if the current set is a correct subset of other; otherwise, false.
            """
            ...

        def is_proper_superset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableSortedSet_T]) -> bool:
            """
            Determines whether the current set is a proper (strict) superset of a specified collection.
            
            :param other: The collection to compare to the current set.
            :returns: true if the current set is a superset of other; otherwise, false.
            """
            ...

        def is_subset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableSortedSet_T]) -> bool:
            """
            Determines whether the current set is a subset of a specified collection.
            
            :param other: The collection to compare to the current set.
            :returns: true if the current set is a subset of other; otherwise, false.
            """
            ...

        def is_superset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableSortedSet_T]) -> bool:
            """
            Determines whether the current set is a superset of a specified collection.
            
            :param other: The collection to compare to the current set.
            :returns: true if the current set is a superset of other; otherwise, false.
            """
            ...

        def item_ref(self, index: int) -> typing.Any:
            """
            Gets a read-only reference to the element of the set at the given index.
            
            :param index: The 0-based index of the element in the set to return.
            :returns: A read-only reference to the element at the given position.
            """
            ...

        def overlaps(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableSortedSet_T]) -> bool:
            """
            Determines whether the current set overlaps with the specified collection.
            
            :param other: The collection to compare to the current set.
            :returns: true if the current set and other share at least one common element; otherwise, false.
            """
            ...

        def remove(self, item: System_Collections_Immutable_ImmutableSortedSet_T) -> bool:
            """
            Removes the first occurrence of a specific object from the set.
            
            :param item: The object to remove from the set.
            :returns: true if the item was removed from the set; false if the item was not found in the set.
            """
            ...

        def reverse(self) -> System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableSortedSet_T]:
            """
            Returns an IEnumerable{T} that iterates over this
            collection in reverse order.
            
            :returns: An enumerator that iterates over the ImmutableSortedSet{T}.Builder in reverse order.
            """
            ...

        def set_equals(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableSortedSet_T]) -> bool:
            """
            Determines whether the current set and the specified collection contain the same elements.
            
            :param other: The collection to compare to the current set.
            :returns: true if the current set is equal to other; otherwise, false.
            """
            ...

        def symmetric_except_with(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableSortedSet_T]) -> None:
            """
            Modifies the current set so that it contains only elements that are present either in the current set or in the specified collection, but not both.
            
            :param other: The collection to compare to the current set.
            """
            ...

        def to_immutable(self) -> System.Collections.Immutable.ImmutableSortedSet[System_Collections_Immutable_ImmutableSortedSet_T]:
            """
            Creates an immutable sorted set based on the contents of this instance.
            
            :returns: An immutable set.
            """
            ...

        def try_get_value(self, equal_value: System_Collections_Immutable_ImmutableSortedSet_T, actual_value: typing.Optional[System_Collections_Immutable_ImmutableSortedSet_T]) -> typing.Tuple[bool, System_Collections_Immutable_ImmutableSortedSet_T]:
            """
            Searches the set for a given value and returns the equal value it finds, if any.
            
            :param equal_value: The value for which to search.
            :param actual_value: The value from the set that the search found, or the original value if the search yielded no match.
            :returns: A value indicating whether the search was successful.
            """
            ...

        def union_with(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableSortedSet_T]) -> None:
            """
            Modifies the current set so that it contains all elements that are present in both the current set and in the specified collection.
            
            :param other: The collection to compare to the current set.
            """
            ...

    class Enumerator(System.Collections.Generic.IEnumerator[System_Collections_Immutable_ImmutableSortedSet_T], System.Collections.Immutable.ISecurePooledObjectUser, System.Collections.Immutable.IStrongEnumerator[System_Collections_Immutable_ImmutableSortedSet_T]):
        """Enumerates the contents of a binary tree."""

        @property
        def current(self) -> System_Collections_Immutable_ImmutableSortedSet_T:
            """The current element."""
            ...

        def dispose(self) -> None:
            """Disposes of this enumerator and returns the stack reference to the resource pool."""
            ...

        def move_next(self) -> bool:
            """
            Advances enumeration to the next element.
            
            :returns: A value indicating whether there is another element in the enumeration.
            """
            ...

        def reset(self) -> None:
            """Restarts enumeration."""
            ...

    EMPTY: System.Collections.Immutable.ImmutableSortedSet[System_Collections_Immutable_ImmutableSortedSet_T] = ...
    """An empty sorted set with the default sort comparer."""

    @property
    def max(self) -> System_Collections_Immutable_ImmutableSortedSet_T:
        """Gets the maximum value in the collection, as defined by the comparer."""
        ...

    @property
    def min(self) -> System_Collections_Immutable_ImmutableSortedSet_T:
        """Gets the minimum value in the collection, as defined by the comparer."""
        ...

    @property
    def is_empty(self) -> bool:
        """See the IImmutableSet{T} interface."""
        ...

    @property
    def count(self) -> int:
        """See the IImmutableSet{T} interface."""
        ...

    @property
    def key_comparer(self) -> System.Collections.Generic.IComparer[System_Collections_Immutable_ImmutableSortedSet_T]:
        """See the IImmutableSet{T} interface."""
        ...

    def __getitem__(self, index: int) -> System_Collections_Immutable_ImmutableSortedSet_T:
        """
        Gets the element of the set at the given index.
        
        :param index: The 0-based index of the element in the set to return.
        :returns: The element at the given position.
        """
        ...

    def __iter__(self) -> typing.Iterator[System_Collections_Immutable_ImmutableSortedSet_T]:
        ...

    def add(self, value: System_Collections_Immutable_ImmutableSortedSet_T) -> System.Collections.Immutable.ImmutableSortedSet[System_Collections_Immutable_ImmutableSortedSet_T]:
        """See the IImmutableSet{T} interface."""
        ...

    def clear(self) -> System.Collections.Immutable.ImmutableSortedSet[System_Collections_Immutable_ImmutableSortedSet_T]:
        """See the IImmutableSet{T} interface."""
        ...

    def contains(self, value: System_Collections_Immutable_ImmutableSortedSet_T) -> bool:
        """See the IImmutableSet{T} interface."""
        ...

    def Except(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableSortedSet_T]) -> System.Collections.Immutable.ImmutableSortedSet[System_Collections_Immutable_ImmutableSortedSet_T]:
        """See the IImmutableSet{T} interface."""
        ...

    def get_enumerator(self) -> System.Collections.Immutable.ImmutableSortedSet.Enumerator:
        """
        Returns an enumerator that iterates through the collection.
        
        :returns: A IEnumerator{T} that can be used to iterate through the collection.
        """
        ...

    def index_of(self, item: System_Collections_Immutable_ImmutableSortedSet_T) -> int:
        """
        Gets the position within this set that the specified value does or would appear.
        
        :param item: The value whose position is being sought.
        :returns: The index of the specified  in the sorted set, if  is found.  If  is not found and  is less than one or more elements in this set, a negative number which is the bitwise complement of the index of the first element that is larger than value. If  is not found and  is greater than any of the elements in the set, a negative number which is the bitwise complement of (the index of the last element plus 1).
        """
        ...

    def intersect(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableSortedSet_T]) -> System.Collections.Immutable.ImmutableSortedSet[System_Collections_Immutable_ImmutableSortedSet_T]:
        """See the IImmutableSet{T} interface."""
        ...

    def is_proper_subset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableSortedSet_T]) -> bool:
        """
        Determines whether the current set is a property (strict) subset of a specified collection.
        
        :param other: The collection to compare to the current set.
        :returns: true if the current set is a correct subset of other; otherwise, false.
        """
        ...

    def is_proper_superset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableSortedSet_T]) -> bool:
        """
        Determines whether the current set is a correct superset of a specified collection.
        
        :param other: The collection to compare to the current set.
        :returns: true if the current set is a correct superset of other; otherwise, false.
        """
        ...

    def is_subset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableSortedSet_T]) -> bool:
        """
        Determines whether a set is a subset of a specified collection.
        
        :param other: The collection to compare to the current set.
        :returns: true if the current set is a subset of other; otherwise, false.
        """
        ...

    def is_superset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableSortedSet_T]) -> bool:
        """
        Determines whether the current set is a superset of a specified collection.
        
        :param other: The collection to compare to the current set.
        :returns: true if the current set is a superset of other; otherwise, false.
        """
        ...

    def item_ref(self, index: int) -> typing.Any:
        """
        Gets a read-only reference of the element of the set at the given index.
        
        :param index: The 0-based index of the element in the set to return.
        :returns: A read-only reference of the element at the given position.
        """
        ...

    def overlaps(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableSortedSet_T]) -> bool:
        """
        Determines whether the current set overlaps with the specified collection.
        
        :param other: The collection to compare to the current set.
        :returns: true if the current set and other share at least one common element; otherwise, false.
        """
        ...

    def remove(self, value: System_Collections_Immutable_ImmutableSortedSet_T) -> System.Collections.Immutable.ImmutableSortedSet[System_Collections_Immutable_ImmutableSortedSet_T]:
        """See the IImmutableSet{T} interface."""
        ...

    def reverse(self) -> System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableSortedSet_T]:
        """
        Returns an IEnumerable{T} that iterates over this
        collection in reverse order.
        
        :returns: An enumerator that iterates over the ImmutableSortedSet{T} in reverse order.
        """
        ...

    def set_equals(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableSortedSet_T]) -> bool:
        """
        Checks whether a given sequence of items entirely describe the contents of this set.
        
        :param other: The sequence of items to check against this set.
        :returns: A value indicating whether the sets are equal.
        """
        ...

    def symmetric_except(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableSortedSet_T]) -> System.Collections.Immutable.ImmutableSortedSet[System_Collections_Immutable_ImmutableSortedSet_T]:
        """
        Produces a set that contains elements either in this set or a given sequence, but not both.
        
        :param other: The other sequence of items.
        :returns: The new set.
        """
        ...

    def to_builder(self) -> System.Collections.Immutable.ImmutableSortedSet.Builder:
        """
        Creates a collection with the same contents as this collection that
        can be efficiently mutated across multiple operations using standard
        mutable interfaces.
        """
        ...

    def try_get_value(self, equal_value: System_Collections_Immutable_ImmutableSortedSet_T, actual_value: typing.Optional[System_Collections_Immutable_ImmutableSortedSet_T]) -> typing.Tuple[bool, System_Collections_Immutable_ImmutableSortedSet_T]:
        """
        Searches the set for a given value and returns the equal value it finds, if any.
        
        :param equal_value: The value to search for.
        :param actual_value: The value from the set that the search found, or the original value if the search yielded no match.
        :returns: A value indicating whether the search was successful.
        """
        ...

    def union(self, other: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableSortedSet_T]) -> System.Collections.Immutable.ImmutableSortedSet[System_Collections_Immutable_ImmutableSortedSet_T]:
        """See the IImmutableSet{T} interface."""
        ...

    def with_comparer(self, comparer: System.Collections.Generic.IComparer[System_Collections_Immutable_ImmutableSortedSet_T]) -> System.Collections.Immutable.ImmutableSortedSet[System_Collections_Immutable_ImmutableSortedSet_T]:
        """See the IImmutableSet{T} interface."""
        ...


class ImmutableQueue(typing.Generic[System_Collections_Immutable_ImmutableQueue_T], System.Object, System.Collections.Immutable.IImmutableQueue[System_Collections_Immutable_ImmutableQueue_T], typing.Iterable[System_Collections_Immutable_ImmutableQueue_T]):
    """An immutable queue."""

    class Enumerator:
        """A memory allocation-free enumerator of ImmutableQueue{T}."""

        @property
        def current(self) -> System_Collections_Immutable_ImmutableQueue_T:
            """The current element."""
            ...

        def move_next(self) -> bool:
            """
            Advances enumeration to the next element.
            
            :returns: A value indicating whether there is another element in the enumeration.
            """
            ...

    @property
    def is_empty(self) -> bool:
        """Gets a value indicating whether this instance is empty."""
        ...

    EMPTY: System.Collections.Immutable.ImmutableQueue[System_Collections_Immutable_ImmutableQueue_T]
    """Gets the empty queue."""

    def __iter__(self) -> typing.Iterator[System_Collections_Immutable_ImmutableQueue_T]:
        ...

    def clear(self) -> System.Collections.Immutable.ImmutableQueue[System_Collections_Immutable_ImmutableQueue_T]:
        """Gets the empty queue."""
        ...

    @overload
    def dequeue(self) -> System.Collections.Immutable.ImmutableQueue[System_Collections_Immutable_ImmutableQueue_T]:
        """
        Returns a queue that is missing the front element.
        
        :returns: A queue; never null.
        """
        ...

    @overload
    def dequeue(self, value: typing.Optional[System_Collections_Immutable_ImmutableQueue_T]) -> typing.Tuple[System.Collections.Immutable.ImmutableQueue[System_Collections_Immutable_ImmutableQueue_T], System_Collections_Immutable_ImmutableQueue_T]:
        """
        Retrieves the item at the head of the queue, and returns a queue with the head element removed.
        
        :param value: Receives the value from the head of the queue.
        :returns: The new queue with the head element removed.
        """
        ...

    def enqueue(self, value: System_Collections_Immutable_ImmutableQueue_T) -> System.Collections.Immutable.ImmutableQueue[System_Collections_Immutable_ImmutableQueue_T]:
        """
        Adds an element to the back of the queue.
        
        :param value: The value.
        :returns: The new queue.
        """
        ...

    def get_enumerator(self) -> System.Collections.Immutable.ImmutableQueue.Enumerator:
        """
        Returns an enumerator that iterates through the collection.
        
        :returns: An Enumerator that can be used to iterate through the collection.
        """
        ...

    def peek(self) -> System_Collections_Immutable_ImmutableQueue_T:
        """Gets the element at the front of the queue."""
        ...

    def peek_ref(self) -> typing.Any:
        """Gets a read-only reference to the element at the front of the queue."""
        ...


class ImmutableSortedDictionary(typing.Generic[System_Collections_Immutable_ImmutableSortedDictionary_TKey, System_Collections_Immutable_ImmutableSortedDictionary_TValue], System.Object, System.Collections.Immutable.IImmutableDictionary[System_Collections_Immutable_ImmutableSortedDictionary_TKey, System_Collections_Immutable_ImmutableSortedDictionary_TValue], System.Collections.Generic.IDictionary[System_Collections_Immutable_ImmutableSortedDictionary_TKey, System_Collections_Immutable_ImmutableSortedDictionary_TValue], System.Collections.IDictionary, typing.Iterable[System.Collections.Generic.KeyValuePair[System_Collections_Immutable_ImmutableSortedDictionary_TKey, System_Collections_Immutable_ImmutableSortedDictionary_TValue]]):
    """A set of initialization methods for instances of ImmutableSortedDictionary{TKey, TValue}."""

    class Enumerator(System.Collections.Generic.IEnumerator[System.Collections.Generic.KeyValuePair[System_Collections_Immutable_ImmutableSortedDictionary_TKey, System_Collections_Immutable_ImmutableSortedDictionary_TValue]], System.Collections.Immutable.ISecurePooledObjectUser):
        """Enumerates the contents of a binary tree."""

        @property
        def current(self) -> System.Collections.Generic.KeyValuePair[System_Collections_Immutable_ImmutableSortedDictionary_TKey, System_Collections_Immutable_ImmutableSortedDictionary_TValue]:
            """The current element."""
            ...

        def dispose(self) -> None:
            """Disposes of this enumerator and returns the stack reference to the resource pool."""
            ...

        def move_next(self) -> bool:
            """
            Advances enumeration to the next element.
            
            :returns: A value indicating whether there is another element in the enumeration.
            """
            ...

        def reset(self) -> None:
            """Restarts enumeration."""
            ...

    class Builder(System.Object, System.Collections.Generic.IDictionary[System_Collections_Immutable_ImmutableSortedDictionary_TKey, System_Collections_Immutable_ImmutableSortedDictionary_TValue], System.Collections.Generic.IReadOnlyDictionary[System_Collections_Immutable_ImmutableSortedDictionary_TKey, System_Collections_Immutable_ImmutableSortedDictionary_TValue], System.Collections.IDictionary, typing.Iterable[System.Collections.Generic.KeyValuePair[System_Collections_Immutable_ImmutableSortedDictionary_TKey, System_Collections_Immutable_ImmutableSortedDictionary_TValue]]):
        """
        A sorted dictionary that mutates with little or no memory allocations,
        can produce and/or build on immutable sorted dictionary instances very efficiently.
        """

        @property
        def keys(self) -> typing.Iterable[System_Collections_Immutable_ImmutableSortedDictionary_TKey]:
            """See IReadOnlyDictionary{TKey, TValue}"""
            ...

        @property
        def values(self) -> typing.Iterable[System_Collections_Immutable_ImmutableSortedDictionary_TValue]:
            """See IReadOnlyDictionary{TKey, TValue}"""
            ...

        @property
        def count(self) -> int:
            """Gets the number of elements in this map."""
            ...

        @property
        def key_comparer(self) -> System.Collections.Generic.IComparer[System_Collections_Immutable_ImmutableSortedDictionary_TKey]:
            """Gets or sets the key comparer."""
            ...

        @key_comparer.setter
        def key_comparer(self, value: System.Collections.Generic.IComparer[System_Collections_Immutable_ImmutableSortedDictionary_TKey]) -> None:
            ...

        @property
        def value_comparer(self) -> System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableSortedDictionary_TValue]:
            """Gets or sets the value comparer."""
            ...

        @value_comparer.setter
        def value_comparer(self, value: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableSortedDictionary_TValue]) -> None:
            ...

        def __contains__(self, key: System_Collections_Immutable_ImmutableSortedDictionary_TKey) -> bool:
            """See IDictionary{TKey, TValue}"""
            ...

        def __getitem__(self, key: System_Collections_Immutable_ImmutableSortedDictionary_TKey) -> System_Collections_Immutable_ImmutableSortedDictionary_TValue:
            """
            Gets or sets the value for a given key.
            
            :param key: The key.
            :returns: The value associated with the given key.
            """
            ...

        def __iter__(self) -> typing.Iterator[System.Collections.Generic.KeyValuePair[System_Collections_Immutable_ImmutableSortedDictionary_TKey, System_Collections_Immutable_ImmutableSortedDictionary_TValue]]:
            ...

        def __len__(self) -> int:
            ...

        def __setitem__(self, key: System_Collections_Immutable_ImmutableSortedDictionary_TKey, value: System_Collections_Immutable_ImmutableSortedDictionary_TValue) -> None:
            """
            Gets or sets the value for a given key.
            
            :param key: The key.
            :returns: The value associated with the given key.
            """
            ...

        @overload
        def add(self, key: System_Collections_Immutable_ImmutableSortedDictionary_TKey, value: System_Collections_Immutable_ImmutableSortedDictionary_TValue) -> None:
            """See IDictionary{TKey, TValue}"""
            ...

        @overload
        def add(self, item: System.Collections.Generic.KeyValuePair[System_Collections_Immutable_ImmutableSortedDictionary_TKey, System_Collections_Immutable_ImmutableSortedDictionary_TValue]) -> None:
            """See IDictionary{TKey, TValue}"""
            ...

        def add_range(self, items: System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[System_Collections_Immutable_ImmutableSortedDictionary_TKey, System_Collections_Immutable_ImmutableSortedDictionary_TValue]]) -> None:
            """
            Removes any entries from the dictionaries with keys that match those found in the specified sequence.
            
            :param items: The keys for entries to remove from the dictionary.
            """
            ...

        def clear(self) -> None:
            """See IDictionary{TKey, TValue}"""
            ...

        def contains(self, item: System.Collections.Generic.KeyValuePair[System_Collections_Immutable_ImmutableSortedDictionary_TKey, System_Collections_Immutable_ImmutableSortedDictionary_TValue]) -> bool:
            """See IDictionary{TKey, TValue}"""
            ...

        def contains_key(self, key: System_Collections_Immutable_ImmutableSortedDictionary_TKey) -> bool:
            """See IDictionary{TKey, TValue}"""
            ...

        def contains_value(self, value: System_Collections_Immutable_ImmutableSortedDictionary_TValue) -> bool:
            """
            Determines whether the ImmutableSortedDictionary{TKey, TValue}
            contains an element with the specified value.
            
            :param value: The value to locate in the ImmutableSortedDictionary{TKey, TValue}. The value can be null for reference types.
            :returns: true if the ImmutableSortedDictionary{TKey, TValue} contains an element with the specified value; otherwise, false.
            """
            ...

        def get_enumerator(self) -> System.Collections.Immutable.ImmutableSortedDictionary.Enumerator:
            """See IDictionary{TKey, TValue}"""
            ...

        @overload
        def get_value_or_default(self, key: System_Collections_Immutable_ImmutableSortedDictionary_TKey) -> System_Collections_Immutable_ImmutableSortedDictionary_TValue:
            """
            Gets the value for a given key if a matching key exists in the dictionary.
            
            :param key: The key to search for.
            :returns: The value for the key, or the default value for type TValue if no matching key was found.
            """
            ...

        @overload
        def get_value_or_default(self, key: System_Collections_Immutable_ImmutableSortedDictionary_TKey, default_value: System_Collections_Immutable_ImmutableSortedDictionary_TValue) -> System_Collections_Immutable_ImmutableSortedDictionary_TValue:
            """
            Gets the value for a given key if a matching key exists in the dictionary.
            
            :param key: The key to search for.
            :param default_value: The default value to return if no matching key is found in the dictionary.
            :returns: The value for the key, or  if no matching key was found.
            """
            ...

        @overload
        def remove(self, key: System_Collections_Immutable_ImmutableSortedDictionary_TKey) -> bool:
            """See IDictionary{TKey, TValue}"""
            ...

        @overload
        def remove(self, item: System.Collections.Generic.KeyValuePair[System_Collections_Immutable_ImmutableSortedDictionary_TKey, System_Collections_Immutable_ImmutableSortedDictionary_TValue]) -> bool:
            """See IDictionary{TKey, TValue}"""
            ...

        def remove_range(self, keys: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableSortedDictionary_TKey]) -> None:
            """
            Removes any entries from the dictionaries with keys that match those found in the specified sequence.
            
            :param keys: The keys for entries to remove from the dictionary.
            """
            ...

        def to_immutable(self) -> System.Collections.Immutable.ImmutableSortedDictionary[System_Collections_Immutable_ImmutableSortedDictionary_TKey, System_Collections_Immutable_ImmutableSortedDictionary_TValue]:
            """
            Creates an immutable sorted dictionary based on the contents of this instance.
            
            :returns: An immutable map.
            """
            ...

        def try_get_key(self, equal_key: System_Collections_Immutable_ImmutableSortedDictionary_TKey, actual_key: typing.Optional[System_Collections_Immutable_ImmutableSortedDictionary_TKey]) -> typing.Tuple[bool, System_Collections_Immutable_ImmutableSortedDictionary_TKey]:
            """See the IImmutableDictionary{TKey, TValue} interface."""
            ...

        def try_get_value(self, key: System_Collections_Immutable_ImmutableSortedDictionary_TKey, value: typing.Optional[System_Collections_Immutable_ImmutableSortedDictionary_TValue]) -> typing.Tuple[bool, System_Collections_Immutable_ImmutableSortedDictionary_TValue]:
            """See IDictionary{TKey, TValue}"""
            ...

        def value_ref(self, key: System_Collections_Immutable_ImmutableSortedDictionary_TKey) -> typing.Any:
            """Returns a read-only reference to the value associated with the provided key."""
            ...

    EMPTY: System.Collections.Immutable.ImmutableSortedDictionary[System_Collections_Immutable_ImmutableSortedDictionary_TKey, System_Collections_Immutable_ImmutableSortedDictionary_TValue] = ...
    """An empty sorted dictionary with default sort and equality comparers."""

    @property
    def value_comparer(self) -> System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableSortedDictionary_TValue]:
        """Gets the value comparer used to determine whether values are equal."""
        ...

    @property
    def is_empty(self) -> bool:
        """See the IImmutableDictionary{TKey, TValue} interface."""
        ...

    @property
    def count(self) -> int:
        """See the IImmutableDictionary{TKey, TValue} interface."""
        ...

    @property
    def keys(self) -> typing.Iterable[System_Collections_Immutable_ImmutableSortedDictionary_TKey]:
        """See the IImmutableDictionary{TKey, TValue} interface."""
        ...

    @property
    def values(self) -> typing.Iterable[System_Collections_Immutable_ImmutableSortedDictionary_TValue]:
        """See the IImmutableDictionary{TKey, TValue} interface."""
        ...

    @property
    def key_comparer(self) -> System.Collections.Generic.IComparer[System_Collections_Immutable_ImmutableSortedDictionary_TKey]:
        """See the IImmutableDictionary{TKey, TValue} interface."""
        ...

    def __contains__(self, key: System_Collections_Immutable_ImmutableSortedDictionary_TKey) -> bool:
        """See the IImmutableDictionary{TKey, TValue} interface."""
        ...

    def __getitem__(self, key: System_Collections_Immutable_ImmutableSortedDictionary_TKey) -> System_Collections_Immutable_ImmutableSortedDictionary_TValue:
        """Gets the TValue with the specified key."""
        ...

    def __iter__(self) -> typing.Iterator[System.Collections.Generic.KeyValuePair[System_Collections_Immutable_ImmutableSortedDictionary_TKey, System_Collections_Immutable_ImmutableSortedDictionary_TValue]]:
        ...

    def __len__(self) -> int:
        ...

    def add(self, key: System_Collections_Immutable_ImmutableSortedDictionary_TKey, value: System_Collections_Immutable_ImmutableSortedDictionary_TValue) -> System.Collections.Immutable.ImmutableSortedDictionary[System_Collections_Immutable_ImmutableSortedDictionary_TKey, System_Collections_Immutable_ImmutableSortedDictionary_TValue]:
        """See the IImmutableDictionary{TKey, TValue} interface."""
        ...

    def add_range(self, items: System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[System_Collections_Immutable_ImmutableSortedDictionary_TKey, System_Collections_Immutable_ImmutableSortedDictionary_TValue]]) -> System.Collections.Immutable.ImmutableSortedDictionary[System_Collections_Immutable_ImmutableSortedDictionary_TKey, System_Collections_Immutable_ImmutableSortedDictionary_TValue]:
        """See the IImmutableDictionary{TKey, TValue} interface."""
        ...

    def clear(self) -> System.Collections.Immutable.ImmutableSortedDictionary[System_Collections_Immutable_ImmutableSortedDictionary_TKey, System_Collections_Immutable_ImmutableSortedDictionary_TValue]:
        """See the IImmutableDictionary{TKey, TValue} interface."""
        ...

    def contains(self, pair: System.Collections.Generic.KeyValuePair[System_Collections_Immutable_ImmutableSortedDictionary_TKey, System_Collections_Immutable_ImmutableSortedDictionary_TValue]) -> bool:
        """See the IImmutableDictionary{TKey, TValue} interface."""
        ...

    def contains_key(self, key: System_Collections_Immutable_ImmutableSortedDictionary_TKey) -> bool:
        """See the IImmutableDictionary{TKey, TValue} interface."""
        ...

    def contains_value(self, value: System_Collections_Immutable_ImmutableSortedDictionary_TValue) -> bool:
        """
        Determines whether the ImmutableSortedDictionary{TKey, TValue}
        contains an element with the specified value.
        
        :param value: The value to locate in the ImmutableSortedDictionary{TKey, TValue}. The value can be null for reference types.
        :returns: true if the ImmutableSortedDictionary{TKey, TValue} contains an element with the specified value; otherwise, false.
        """
        ...

    def get_enumerator(self) -> System.Collections.Immutable.ImmutableSortedDictionary.Enumerator:
        """
        Returns an enumerator that iterates through the collection.
        
        :returns: A IEnumerator{T} that can be used to iterate through the collection.
        """
        ...

    def remove(self, value: System_Collections_Immutable_ImmutableSortedDictionary_TKey) -> System.Collections.Immutable.ImmutableSortedDictionary[System_Collections_Immutable_ImmutableSortedDictionary_TKey, System_Collections_Immutable_ImmutableSortedDictionary_TValue]:
        """See the IImmutableDictionary{TKey, TValue} interface."""
        ...

    def remove_range(self, keys: System.Collections.Generic.IEnumerable[System_Collections_Immutable_ImmutableSortedDictionary_TKey]) -> System.Collections.Immutable.ImmutableSortedDictionary[System_Collections_Immutable_ImmutableSortedDictionary_TKey, System_Collections_Immutable_ImmutableSortedDictionary_TValue]:
        """See the IImmutableDictionary{TKey, TValue} interface."""
        ...

    def set_item(self, key: System_Collections_Immutable_ImmutableSortedDictionary_TKey, value: System_Collections_Immutable_ImmutableSortedDictionary_TValue) -> System.Collections.Immutable.ImmutableSortedDictionary[System_Collections_Immutable_ImmutableSortedDictionary_TKey, System_Collections_Immutable_ImmutableSortedDictionary_TValue]:
        """See the IImmutableDictionary{TKey, TValue} interface."""
        ...

    def set_items(self, items: System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[System_Collections_Immutable_ImmutableSortedDictionary_TKey, System_Collections_Immutable_ImmutableSortedDictionary_TValue]]) -> System.Collections.Immutable.ImmutableSortedDictionary[System_Collections_Immutable_ImmutableSortedDictionary_TKey, System_Collections_Immutable_ImmutableSortedDictionary_TValue]:
        """
        Applies a given set of key=value pairs to an immutable dictionary, replacing any conflicting keys in the resulting dictionary.
        
        :param items: The key=value pairs to set on the map.  Any keys that conflict with existing keys will overwrite the previous values.
        :returns: An immutable dictionary.
        """
        ...

    def to_builder(self) -> System.Collections.Immutable.ImmutableSortedDictionary.Builder:
        """
        Creates a collection with the same contents as this collection that
        can be efficiently mutated across multiple operations using standard
        mutable interfaces.
        """
        ...

    def try_get_key(self, equal_key: System_Collections_Immutable_ImmutableSortedDictionary_TKey, actual_key: typing.Optional[System_Collections_Immutable_ImmutableSortedDictionary_TKey]) -> typing.Tuple[bool, System_Collections_Immutable_ImmutableSortedDictionary_TKey]:
        """See the IImmutableDictionary{TKey, TValue} interface."""
        ...

    def try_get_value(self, key: System_Collections_Immutable_ImmutableSortedDictionary_TKey, value: typing.Optional[System_Collections_Immutable_ImmutableSortedDictionary_TValue]) -> typing.Tuple[bool, System_Collections_Immutable_ImmutableSortedDictionary_TValue]:
        """See the IImmutableDictionary{TKey, TValue} interface."""
        ...

    def value_ref(self, key: System_Collections_Immutable_ImmutableSortedDictionary_TKey) -> typing.Any:
        """Returns a read-only reference to the value associated with the provided key."""
        ...

    @overload
    def with_comparers(self, key_comparer: System.Collections.Generic.IComparer[System_Collections_Immutable_ImmutableSortedDictionary_TKey], value_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_ImmutableSortedDictionary_TValue]) -> System.Collections.Immutable.ImmutableSortedDictionary[System_Collections_Immutable_ImmutableSortedDictionary_TKey, System_Collections_Immutable_ImmutableSortedDictionary_TValue]:
        """See the IImmutableDictionary{TKey, TValue} interface."""
        ...

    @overload
    def with_comparers(self, key_comparer: System.Collections.Generic.IComparer[System_Collections_Immutable_ImmutableSortedDictionary_TKey]) -> System.Collections.Immutable.ImmutableSortedDictionary[System_Collections_Immutable_ImmutableSortedDictionary_TKey, System_Collections_Immutable_ImmutableSortedDictionary_TValue]:
        """See the IImmutableDictionary{TKey, TValue} interface."""
        ...


class ImmutableStack(typing.Generic[System_Collections_Immutable_ImmutableStack_T], System.Object, System.Collections.Immutable.IImmutableStack[System_Collections_Immutable_ImmutableStack_T], typing.Iterable[System_Collections_Immutable_ImmutableStack_T]):
    """An immutable stack."""

    class Enumerator:
        """Enumerates a stack with no memory allocations."""

        @property
        def current(self) -> System_Collections_Immutable_ImmutableStack_T:
            """Gets the current element."""
            ...

        def move_next(self) -> bool:
            """
            Moves to the first or next element.
            
            :returns: A value indicating whether there are any more elements.
            """
            ...

    EMPTY: System.Collections.Immutable.ImmutableStack[System_Collections_Immutable_ImmutableStack_T]
    """Gets the empty stack, upon which all stacks are built."""

    @property
    def is_empty(self) -> bool:
        """Gets a value indicating whether this instance is empty."""
        ...

    def __iter__(self) -> typing.Iterator[System_Collections_Immutable_ImmutableStack_T]:
        ...

    def clear(self) -> System.Collections.Immutable.ImmutableStack[System_Collections_Immutable_ImmutableStack_T]:
        """Gets the empty stack, upon which all stacks are built."""
        ...

    def get_enumerator(self) -> System.Collections.Immutable.ImmutableStack.Enumerator:
        """
        Returns an enumerator that iterates through the collection.
        
        :returns: An Enumerator that can be used to iterate through the collection.
        """
        ...

    def peek(self) -> System_Collections_Immutable_ImmutableStack_T:
        """
        Gets the element on the top of the stack.
        
        :returns: The element on the top of the stack.
        """
        ...

    def peek_ref(self) -> typing.Any:
        """
        Gets a read-only reference to the element on the top of the stack.
        
        :returns: A read-only reference to the element on the top of the stack.
        """
        ...

    @overload
    def pop(self) -> System.Collections.Immutable.ImmutableStack[System_Collections_Immutable_ImmutableStack_T]:
        """
        Returns a stack that lacks the top element on this stack.
        
        :returns: A stack; never null.
        """
        ...

    @overload
    def pop(self, value: typing.Optional[System_Collections_Immutable_ImmutableStack_T]) -> typing.Tuple[System.Collections.Immutable.ImmutableStack[System_Collections_Immutable_ImmutableStack_T], System_Collections_Immutable_ImmutableStack_T]:
        """
        Pops the top element off the stack.
        
        :param value: The value that was removed from the stack.
        :returns: A stack; never null.
        """
        ...

    def push(self, value: System_Collections_Immutable_ImmutableStack_T) -> System.Collections.Immutable.ImmutableStack[System_Collections_Immutable_ImmutableStack_T]:
        """
        Pushes an element onto a stack and returns the new stack.
        
        :param value: The element to push onto the stack.
        :returns: The new stack.
        """
        ...


class ImmutableInterlocked(System.Object):
    """Contains interlocked exchange mechanisms for immutable collections."""


class IImmutableList(typing.Generic[System_Collections_Immutable_IImmutableList_T], System.Collections.Generic.IReadOnlyList[System_Collections_Immutable_IImmutableList_T], metaclass=abc.ABCMeta):
    """A list of elements that can only be modified by creating a new instance of the list."""

    def add(self, value: System_Collections_Immutable_IImmutableList_T) -> System.Collections.Immutable.IImmutableList[System_Collections_Immutable_IImmutableList_T]:
        """
        Adds the specified value to this list.
        
        :param value: The value to add.
        :returns: A new list with the element added.
        """
        ...

    def add_range(self, items: System.Collections.Generic.IEnumerable[System_Collections_Immutable_IImmutableList_T]) -> System.Collections.Immutable.IImmutableList[System_Collections_Immutable_IImmutableList_T]:
        """
        Adds the specified values to this list.
        
        :param items: The values to add.
        :returns: A new list with the elements added.
        """
        ...

    def clear(self) -> System.Collections.Immutable.IImmutableList[System_Collections_Immutable_IImmutableList_T]:
        """Gets an empty list that retains the same sort semantics that this instance has."""
        ...

    def index_of(self, item: System_Collections_Immutable_IImmutableList_T, index: int, count: int, equality_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_IImmutableList_T]) -> int:
        """
        Searches for the specified object and returns the zero-based index of the
        first occurrence within the range of elements in the ImmutableList{T}
        that starts at the specified index and contains the specified number of elements.
        
        :param item: The object to locate in the ImmutableList{T}. The value can be null for reference types.
        :param index: The zero-based starting index of the search. 0 (zero) is valid in an empty list.
        :param count: The number of elements in the section to search.
        :param equality_comparer: The equality comparer to use in the search. If null, EqualityComparer{T}.Default is used.
        :returns: The zero-based index of the first occurrence of item within the range of elements in the ImmutableList{T} that starts at index and contains count number of elements, if found; otherwise, -1.
        """
        ...

    def insert(self, index: int, element: System_Collections_Immutable_IImmutableList_T) -> System.Collections.Immutable.IImmutableList[System_Collections_Immutable_IImmutableList_T]:
        """
        Inserts the specified value at the specified index.
        
        :param index: The index at which to insert the value.
        :param element: The element to insert.
        :returns: The new immutable list.
        """
        ...

    def insert_range(self, index: int, items: System.Collections.Generic.IEnumerable[System_Collections_Immutable_IImmutableList_T]) -> System.Collections.Immutable.IImmutableList[System_Collections_Immutable_IImmutableList_T]:
        """
        Inserts the specified values at the specified index.
        
        :param index: The index at which to insert the value.
        :param items: The elements to insert.
        :returns: The new immutable list.
        """
        ...

    def last_index_of(self, item: System_Collections_Immutable_IImmutableList_T, index: int, count: int, equality_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_IImmutableList_T]) -> int:
        """
        Searches for the specified object and returns the zero-based index of the
        last occurrence within the range of elements in the ImmutableList{T}
        that contains the specified number of elements and ends at the specified
        index.
        
        :param item: The object to locate in the ImmutableList{T}. The value can be null for reference types.
        :param index: The starting position of the search. The search proceeds from  toward the beginning of this instance.
        :param count: The number of elements in the section to search.
        :param equality_comparer: The equality comparer to use in the search. If null, EqualityComparer{T}.Default is used.
        :returns: The zero-based index of the last occurrence of  within the range of elements in the ImmutableList{T} that contains  number of elements and ends at , if found; otherwise, -1.
        """
        ...

    def remove(self, value: System_Collections_Immutable_IImmutableList_T, equality_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_IImmutableList_T]) -> System.Collections.Immutable.IImmutableList[System_Collections_Immutable_IImmutableList_T]:
        """
        Removes the specified value from this list.
        
        :param value: The value to remove.
        :param equality_comparer: The equality comparer to use in the search. If null, EqualityComparer{T}.Default is used.
        :returns: A new list with the element removed, or this list if the element is not in this list.
        """
        ...

    def remove_all(self, match: typing.Callable[[System_Collections_Immutable_IImmutableList_T], bool]) -> System.Collections.Immutable.IImmutableList[System_Collections_Immutable_IImmutableList_T]:
        """
        Removes all the elements that match the conditions defined by the specified
        predicate.
        
        :param match: The Predicate{T} delegate that defines the conditions of the elements to remove.
        :returns: The new list.
        """
        ...

    def remove_at(self, index: int) -> System.Collections.Immutable.IImmutableList[System_Collections_Immutable_IImmutableList_T]:
        """
        Removes the element at the specified index.
        
        :param index: The index.
        :returns: A new list with the elements removed.
        """
        ...

    @overload
    def remove_range(self, items: System.Collections.Generic.IEnumerable[System_Collections_Immutable_IImmutableList_T], equality_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_IImmutableList_T]) -> System.Collections.Immutable.IImmutableList[System_Collections_Immutable_IImmutableList_T]:
        """
        Removes the specified values from this list.
        
        :param items: The items to remove if matches are found in this list.
        :param equality_comparer: The equality comparer to use in the search. If null, EqualityComparer{T}.Default is used.
        :returns: A new list with the elements removed.
        """
        ...

    @overload
    def remove_range(self, index: int, count: int) -> System.Collections.Immutable.IImmutableList[System_Collections_Immutable_IImmutableList_T]:
        """
        Removes the specified values from this list.
        
        :param index: The starting index to begin removal.
        :param count: The number of elements to remove.
        :returns: A new list with the elements removed.
        """
        ...

    def replace(self, old_value: System_Collections_Immutable_IImmutableList_T, new_value: System_Collections_Immutable_IImmutableList_T, equality_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Immutable_IImmutableList_T]) -> System.Collections.Immutable.IImmutableList[System_Collections_Immutable_IImmutableList_T]:
        """
        Replaces the first equal element in the list with the specified element.
        
        :param old_value: The element to replace.
        :param new_value: The element to replace the old element with.
        :param equality_comparer: The equality comparer to use in the search. If null, EqualityComparer{T}.Default is used.
        :returns: The new list -- even if the value being replaced is equal to the new value for that position.
        """
        ...

    def set_item(self, index: int, value: System_Collections_Immutable_IImmutableList_T) -> System.Collections.Immutable.IImmutableList[System_Collections_Immutable_IImmutableList_T]:
        """
        Replaces an element in the list at a given position with the specified element.
        
        :param index: The position in the list of the element to replace.
        :param value: The element to replace the old element with.
        :returns: The new list -- even if the value being replaced is equal to the new value for that position.
        """
        ...


class IImmutableDictionary(typing.Generic[System_Collections_Immutable_IImmutableDictionary_TKey, System_Collections_Immutable_IImmutableDictionary_TValue], System.Collections.Generic.IReadOnlyDictionary[System_Collections_Immutable_IImmutableDictionary_TKey, System_Collections_Immutable_IImmutableDictionary_TValue], metaclass=abc.ABCMeta):
    """An immutable key-value dictionary."""

    def add(self, key: System_Collections_Immutable_IImmutableDictionary_TKey, value: System_Collections_Immutable_IImmutableDictionary_TValue) -> System.Collections.Immutable.IImmutableDictionary[System_Collections_Immutable_IImmutableDictionary_TKey, System_Collections_Immutable_IImmutableDictionary_TValue]:
        """
        Adds the specified key and value to the dictionary.
        
        :param key: The key of the entry to add.
        :param value: The value of the entry to add.
        :returns: The new dictionary containing the additional key-value pair.
        """
        ...

    def add_range(self, pairs: System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[System_Collections_Immutable_IImmutableDictionary_TKey, System_Collections_Immutable_IImmutableDictionary_TValue]]) -> System.Collections.Immutable.IImmutableDictionary[System_Collections_Immutable_IImmutableDictionary_TKey, System_Collections_Immutable_IImmutableDictionary_TValue]:
        """
        Adds the specified key-value pairs to the dictionary.
        
        :param pairs: The pairs.
        :returns: The new dictionary containing the additional key-value pairs.
        """
        ...

    def clear(self) -> System.Collections.Immutable.IImmutableDictionary[System_Collections_Immutable_IImmutableDictionary_TKey, System_Collections_Immutable_IImmutableDictionary_TValue]:
        """Gets an empty dictionary with equivalent ordering and key/value comparison rules."""
        ...

    def contains(self, pair: System.Collections.Generic.KeyValuePair[System_Collections_Immutable_IImmutableDictionary_TKey, System_Collections_Immutable_IImmutableDictionary_TValue]) -> bool:
        """
        Determines whether this dictionary contains the specified key-value pair.
        
        :param pair: The key value pair.
        :returns: true if this dictionary contains the key-value pair; otherwise, false.
        """
        ...

    def remove(self, key: System_Collections_Immutable_IImmutableDictionary_TKey) -> System.Collections.Immutable.IImmutableDictionary[System_Collections_Immutable_IImmutableDictionary_TKey, System_Collections_Immutable_IImmutableDictionary_TValue]:
        """
        Removes the specified key from the dictionary with its associated value.
        
        :param key: The key to remove.
        :returns: A new dictionary with the matching entry removed; or this instance if the key is not in the dictionary.
        """
        ...

    def remove_range(self, keys: System.Collections.Generic.IEnumerable[System_Collections_Immutable_IImmutableDictionary_TKey]) -> System.Collections.Immutable.IImmutableDictionary[System_Collections_Immutable_IImmutableDictionary_TKey, System_Collections_Immutable_IImmutableDictionary_TValue]:
        """
        Removes the specified keys from the dictionary with their associated values.
        
        :param keys: The keys to remove.
        :returns: A new dictionary with those keys removed; or this instance if those keys are not in the dictionary.
        """
        ...

    def set_item(self, key: System_Collections_Immutable_IImmutableDictionary_TKey, value: System_Collections_Immutable_IImmutableDictionary_TValue) -> System.Collections.Immutable.IImmutableDictionary[System_Collections_Immutable_IImmutableDictionary_TKey, System_Collections_Immutable_IImmutableDictionary_TValue]:
        """
        Sets the specified key and value to the dictionary, possibly overwriting an existing value for the given key.
        
        :param key: The key of the entry to add.
        :param value: The value of the entry to add.
        :returns: The new dictionary containing the additional key-value pair.
        """
        ...

    def set_items(self, items: System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[System_Collections_Immutable_IImmutableDictionary_TKey, System_Collections_Immutable_IImmutableDictionary_TValue]]) -> System.Collections.Immutable.IImmutableDictionary[System_Collections_Immutable_IImmutableDictionary_TKey, System_Collections_Immutable_IImmutableDictionary_TValue]:
        """
        Applies a given set of key=value pairs to an immutable dictionary, replacing any conflicting keys in the resulting dictionary.
        
        :param items: The key=value pairs to set on the dictionary.  Any keys that conflict with existing keys will overwrite the previous values.
        :returns: An immutable dictionary.
        """
        ...

    def try_get_key(self, equal_key: System_Collections_Immutable_IImmutableDictionary_TKey, actual_key: typing.Optional[System_Collections_Immutable_IImmutableDictionary_TKey]) -> typing.Tuple[bool, System_Collections_Immutable_IImmutableDictionary_TKey]:
        """
        Searches the dictionary for a given key and returns the equal key it finds, if any.
        
        :param equal_key: The key to search for.
        :param actual_key: The key from the dictionary that the search found, or  if the search yielded no match.
        :returns: A value indicating whether the search was successful.
        """
        ...


class IImmutableStack(typing.Generic[System_Collections_Immutable_IImmutableStack_T], System.Collections.Generic.IEnumerable[System_Collections_Immutable_IImmutableStack_T], metaclass=abc.ABCMeta):
    """An immutable stack."""

    @property
    @abc.abstractmethod
    def is_empty(self) -> bool:
        """Gets a value indicating whether this is the empty stack."""
        ...

    def clear(self) -> System.Collections.Immutable.IImmutableStack[System_Collections_Immutable_IImmutableStack_T]:
        """Gets an empty stack."""
        ...

    def peek(self) -> System_Collections_Immutable_IImmutableStack_T:
        """Gets the element on the top of the stack."""
        ...

    def pop(self) -> System.Collections.Immutable.IImmutableStack[System_Collections_Immutable_IImmutableStack_T]:
        """
        Pops the top element off the stack.
        
        :returns: The new stack; never null.
        """
        ...

    def push(self, value: System_Collections_Immutable_IImmutableStack_T) -> System.Collections.Immutable.IImmutableStack[System_Collections_Immutable_IImmutableStack_T]:
        """
        Pushes an element onto a stack and returns the new stack.
        
        :param value: The element to push onto the stack.
        :returns: The new stack.
        """
        ...


class IImmutableQueue(typing.Generic[System_Collections_Immutable_IImmutableQueue_T], System.Collections.Generic.IEnumerable[System_Collections_Immutable_IImmutableQueue_T], metaclass=abc.ABCMeta):
    """An immutable queue."""

    @property
    @abc.abstractmethod
    def is_empty(self) -> bool:
        """Gets a value indicating whether this is the empty queue."""
        ...

    def clear(self) -> System.Collections.Immutable.IImmutableQueue[System_Collections_Immutable_IImmutableQueue_T]:
        """Gets an empty queue."""
        ...

    def dequeue(self) -> System.Collections.Immutable.IImmutableQueue[System_Collections_Immutable_IImmutableQueue_T]:
        """
        Returns a queue that is missing the front element.
        
        :returns: A queue; never null.
        """
        ...

    def enqueue(self, value: System_Collections_Immutable_IImmutableQueue_T) -> System.Collections.Immutable.IImmutableQueue[System_Collections_Immutable_IImmutableQueue_T]:
        """
        Adds an element to the back of the queue.
        
        :param value: The value.
        :returns: The new queue.
        """
        ...

    def peek(self) -> System_Collections_Immutable_IImmutableQueue_T:
        """
        Gets the element at the front of the queue.
        
        :returns: The element at the front of the queue.
        """
        ...


