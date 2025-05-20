from typing import overload
from enum import Enum
import abc
import typing
import warnings

import System
import System.Collections
import System.Collections.Generic
import System.Collections.ObjectModel
import System.Runtime.Serialization
import System.Threading
import System.Threading.Tasks

System_Collections_Generic_ICollection_T = typing.TypeVar("System_Collections_Generic_ICollection_T")
System_Collections_Generic_List_T = typing.TypeVar("System_Collections_Generic_List_T")
System_Collections_Generic_Queue_T = typing.TypeVar("System_Collections_Generic_Queue_T")
System_Collections_Generic_EqualityComparer_T = typing.TypeVar("System_Collections_Generic_EqualityComparer_T")
System_Collections_Generic_GenericEqualityComparer_T = typing.TypeVar("System_Collections_Generic_GenericEqualityComparer_T")
System_Collections_Generic_NullableEqualityComparer_T = typing.TypeVar("System_Collections_Generic_NullableEqualityComparer_T")
System_Collections_Generic_ObjectEqualityComparer_T = typing.TypeVar("System_Collections_Generic_ObjectEqualityComparer_T")
System_Collections_Generic_EnumEqualityComparer_T = typing.TypeVar("System_Collections_Generic_EnumEqualityComparer_T")
System_Collections_Generic_IAsyncEnumerator_T = typing.TypeVar("System_Collections_Generic_IAsyncEnumerator_T")
System_Collections_Generic_IAlternateEqualityComparer_TAlternate = typing.TypeVar("System_Collections_Generic_IAlternateEqualityComparer_TAlternate")
System_Collections_Generic_IAlternateEqualityComparer_T = typing.TypeVar("System_Collections_Generic_IAlternateEqualityComparer_T")
System_Collections_Generic_IList_T = typing.TypeVar("System_Collections_Generic_IList_T")
System_Collections_Generic_IAsyncEnumerable_T = typing.TypeVar("System_Collections_Generic_IAsyncEnumerable_T")
System_Collections_Generic_IReadOnlySet_T = typing.TypeVar("System_Collections_Generic_IReadOnlySet_T")
System_Collections_Generic_IReadOnlyCollection_T = typing.TypeVar("System_Collections_Generic_IReadOnlyCollection_T")
System_Collections_Generic_IReadOnlyList_T = typing.TypeVar("System_Collections_Generic_IReadOnlyList_T")
System_Collections_Generic_IEnumerable_T = typing.TypeVar("System_Collections_Generic_IEnumerable_T")
System_Collections_Generic_IReadOnlyDictionary_TKey = typing.TypeVar("System_Collections_Generic_IReadOnlyDictionary_TKey")
System_Collections_Generic_IReadOnlyDictionary_TValue = typing.TypeVar("System_Collections_Generic_IReadOnlyDictionary_TValue")
System_Collections_Generic_IComparer_T = typing.TypeVar("System_Collections_Generic_IComparer_T")
System_Collections_Generic_HashSet_T = typing.TypeVar("System_Collections_Generic_HashSet_T")
System_Collections_Generic_HashSet_AlternateLookup_TAlternate = typing.TypeVar("System_Collections_Generic_HashSet_AlternateLookup_TAlternate")
System_Collections_Generic_ISet_T = typing.TypeVar("System_Collections_Generic_ISet_T")
System_Collections_Generic_IDictionary_TValue = typing.TypeVar("System_Collections_Generic_IDictionary_TValue")
System_Collections_Generic_IDictionary_TKey = typing.TypeVar("System_Collections_Generic_IDictionary_TKey")
System_Collections_Generic_IEnumerator_T = typing.TypeVar("System_Collections_Generic_IEnumerator_T")
System_Collections_Generic_Dictionary_TValue = typing.TypeVar("System_Collections_Generic_Dictionary_TValue")
System_Collections_Generic_Dictionary_TKey = typing.TypeVar("System_Collections_Generic_Dictionary_TKey")
System_Collections_Generic_Dictionary_AlternateLookup_TAlternateKey = typing.TypeVar("System_Collections_Generic_Dictionary_AlternateLookup_TAlternateKey")
System_Collections_Generic_IEqualityComparer_T = typing.TypeVar("System_Collections_Generic_IEqualityComparer_T")
System_Collections_Generic_KeyValuePair_TKey = typing.TypeVar("System_Collections_Generic_KeyValuePair_TKey")
System_Collections_Generic_KeyValuePair_TValue = typing.TypeVar("System_Collections_Generic_KeyValuePair_TValue")
System_Collections_Generic_Comparer_T = typing.TypeVar("System_Collections_Generic_Comparer_T")
System_Collections_Generic_GenericComparer_T = typing.TypeVar("System_Collections_Generic_GenericComparer_T")
System_Collections_Generic_NullableComparer_T = typing.TypeVar("System_Collections_Generic_NullableComparer_T")
System_Collections_Generic_ObjectComparer_T = typing.TypeVar("System_Collections_Generic_ObjectComparer_T")
System_Collections_Generic_SortedSet_T = typing.TypeVar("System_Collections_Generic_SortedSet_T")
System_Collections_Generic_SortedList_TKey = typing.TypeVar("System_Collections_Generic_SortedList_TKey")
System_Collections_Generic_SortedList_TValue = typing.TypeVar("System_Collections_Generic_SortedList_TValue")
System_Collections_Generic_PriorityQueue_TElement = typing.TypeVar("System_Collections_Generic_PriorityQueue_TElement")
System_Collections_Generic_PriorityQueue_TPriority = typing.TypeVar("System_Collections_Generic_PriorityQueue_TPriority")
System_Collections_Generic_SortedDictionary_TValue = typing.TypeVar("System_Collections_Generic_SortedDictionary_TValue")
System_Collections_Generic_SortedDictionary_TKey = typing.TypeVar("System_Collections_Generic_SortedDictionary_TKey")
System_Collections_Generic_TreeSet_T = typing.TypeVar("System_Collections_Generic_TreeSet_T")
System_Collections_Generic_LinkedList_T = typing.TypeVar("System_Collections_Generic_LinkedList_T")
System_Collections_Generic_LinkedListNode_T = typing.TypeVar("System_Collections_Generic_LinkedListNode_T")
System_Collections_Generic_Stack_T = typing.TypeVar("System_Collections_Generic_Stack_T")


class ICollection(typing.Generic[System_Collections_Generic_ICollection_T], System.Collections.Generic.IEnumerable[System_Collections_Generic_ICollection_T], metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def count(self) -> int:
        ...

    @property
    @abc.abstractmethod
    def is_read_only(self) -> bool:
        ...

    def __contains__(self, item: System_Collections_Generic_ICollection_T) -> bool:
        ...

    def __len__(self) -> int:
        ...

    def add(self, item: System_Collections_Generic_ICollection_T) -> None:
        ...

    def clear(self) -> None:
        ...

    def contains(self, item: System_Collections_Generic_ICollection_T) -> bool:
        ...

    def copy_to(self, array: typing.List[System_Collections_Generic_ICollection_T], array_index: int) -> None:
        ...

    def remove(self, item: System_Collections_Generic_ICollection_T) -> bool:
        ...


class List(typing.Generic[System_Collections_Generic_List_T], System.Object, System.Collections.Generic.IList[System_Collections_Generic_List_T], System.Collections.IList, System.Collections.Generic.IReadOnlyList[System_Collections_Generic_List_T], typing.Iterable[System_Collections_Generic_List_T]):
    """This class has no documentation."""

    class Enumerator(System.Collections.Generic.IEnumerator[System_Collections_Generic_List_T]):
        """This class has no documentation."""

        @property
        def current(self) -> System_Collections_Generic_List_T:
            ...

        def dispose(self) -> None:
            ...

        def move_next(self) -> bool:
            ...

    @property
    def capacity(self) -> int:
        ...

    @capacity.setter
    def capacity(self, value: int) -> None:
        ...

    @property
    def count(self) -> int:
        ...

    def __contains__(self, item: System_Collections_Generic_List_T) -> bool:
        ...

    def __getitem__(self, index: int) -> System_Collections_Generic_List_T:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, capacity: int) -> None:
        ...

    @overload
    def __init__(self, collection: System.Collections.Generic.IEnumerable[System_Collections_Generic_List_T]) -> None:
        ...

    def __iter__(self) -> typing.Iterator[System_Collections_Generic_List_T]:
        ...

    def __len__(self) -> int:
        ...

    def __setitem__(self, index: int, value: System_Collections_Generic_List_T) -> None:
        ...

    def add(self, item: System_Collections_Generic_List_T) -> None:
        ...

    def add_range(self, collection: System.Collections.Generic.IEnumerable[System_Collections_Generic_List_T]) -> None:
        ...

    def as_read_only(self) -> System.Collections.ObjectModel.ReadOnlyCollection[System_Collections_Generic_List_T]:
        ...

    @overload
    def binary_search(self, index: int, count: int, item: System_Collections_Generic_List_T, comparer: System.Collections.Generic.IComparer[System_Collections_Generic_List_T]) -> int:
        ...

    @overload
    def binary_search(self, item: System_Collections_Generic_List_T) -> int:
        ...

    @overload
    def binary_search(self, item: System_Collections_Generic_List_T, comparer: System.Collections.Generic.IComparer[System_Collections_Generic_List_T]) -> int:
        ...

    def clear(self) -> None:
        ...

    def contains(self, item: System_Collections_Generic_List_T) -> bool:
        ...

    @overload
    def copy_to(self, array: typing.List[System_Collections_Generic_List_T]) -> None:
        ...

    @overload
    def copy_to(self, index: int, array: typing.List[System_Collections_Generic_List_T], array_index: int, count: int) -> None:
        ...

    @overload
    def copy_to(self, array: typing.List[System_Collections_Generic_List_T], array_index: int) -> None:
        ...

    def ensure_capacity(self, capacity: int) -> int:
        """
        Ensures that the capacity of this list is at least the specified .
        If the current capacity of the list is less than specified ,
        the capacity is increased to at least .
        
        :param capacity: The minimum capacity to ensure.
        :returns: The new capacity of this list.
        """
        ...

    def exists(self, match: typing.Callable[[System_Collections_Generic_List_T], bool]) -> bool:
        ...

    def find(self, match: typing.Callable[[System_Collections_Generic_List_T], bool]) -> System_Collections_Generic_List_T:
        ...

    def find_all(self, match: typing.Callable[[System_Collections_Generic_List_T], bool]) -> System.Collections.Generic.List[System_Collections_Generic_List_T]:
        ...

    @overload
    def find_index(self, match: typing.Callable[[System_Collections_Generic_List_T], bool]) -> int:
        ...

    @overload
    def find_index(self, start_index: int, match: typing.Callable[[System_Collections_Generic_List_T], bool]) -> int:
        ...

    @overload
    def find_index(self, start_index: int, count: int, match: typing.Callable[[System_Collections_Generic_List_T], bool]) -> int:
        ...

    def find_last(self, match: typing.Callable[[System_Collections_Generic_List_T], bool]) -> System_Collections_Generic_List_T:
        ...

    @overload
    def find_last_index(self, match: typing.Callable[[System_Collections_Generic_List_T], bool]) -> int:
        ...

    @overload
    def find_last_index(self, start_index: int, match: typing.Callable[[System_Collections_Generic_List_T], bool]) -> int:
        ...

    @overload
    def find_last_index(self, start_index: int, count: int, match: typing.Callable[[System_Collections_Generic_List_T], bool]) -> int:
        ...

    def for_each(self, action: typing.Callable[[System_Collections_Generic_List_T], None]) -> None:
        ...

    def get_enumerator(self) -> System.Collections.Generic.List.Enumerator:
        ...

    def get_range(self, index: int, count: int) -> System.Collections.Generic.List[System_Collections_Generic_List_T]:
        ...

    @overload
    def index_of(self, item: System_Collections_Generic_List_T) -> int:
        ...

    @overload
    def index_of(self, item: System_Collections_Generic_List_T, index: int) -> int:
        ...

    @overload
    def index_of(self, item: System_Collections_Generic_List_T, index: int, count: int) -> int:
        ...

    def insert(self, index: int, item: System_Collections_Generic_List_T) -> None:
        ...

    def insert_range(self, index: int, collection: System.Collections.Generic.IEnumerable[System_Collections_Generic_List_T]) -> None:
        ...

    @overload
    def last_index_of(self, item: System_Collections_Generic_List_T) -> int:
        ...

    @overload
    def last_index_of(self, item: System_Collections_Generic_List_T, index: int) -> int:
        ...

    @overload
    def last_index_of(self, item: System_Collections_Generic_List_T, index: int, count: int) -> int:
        ...

    def remove(self, item: System_Collections_Generic_List_T) -> bool:
        ...

    def remove_all(self, match: typing.Callable[[System_Collections_Generic_List_T], bool]) -> int:
        ...

    def remove_at(self, index: int) -> None:
        ...

    def remove_range(self, index: int, count: int) -> None:
        ...

    @overload
    def reverse(self) -> None:
        ...

    @overload
    def reverse(self, index: int, count: int) -> None:
        ...

    def slice(self, start: int, length: int) -> System.Collections.Generic.List[System_Collections_Generic_List_T]:
        """
        Creates a shallow copy of a range of elements in the source List{T}.
        
        :param start: The zero-based List{T} index at which the range starts.
        :param length: The length of the range.
        :returns: A shallow copy of a range of elements in the source List{T}.
        """
        ...

    @overload
    def sort(self) -> None:
        ...

    @overload
    def sort(self, comparer: System.Collections.Generic.IComparer[System_Collections_Generic_List_T]) -> None:
        ...

    @overload
    def sort(self, index: int, count: int, comparer: System.Collections.Generic.IComparer[System_Collections_Generic_List_T]) -> None:
        ...

    @overload
    def sort(self, comparison: typing.Callable[[System_Collections_Generic_List_T, System_Collections_Generic_List_T], int]) -> None:
        ...

    def to_array(self) -> typing.List[System_Collections_Generic_List_T]:
        ...

    def trim_excess(self) -> None:
        ...

    def true_for_all(self, match: typing.Callable[[System_Collections_Generic_List_T], bool]) -> bool:
        ...


class Queue(typing.Generic[System_Collections_Generic_Queue_T], System.Object, System.Collections.ICollection, System.Collections.Generic.IReadOnlyCollection[System_Collections_Generic_Queue_T], typing.Iterable[System_Collections_Generic_Queue_T]):
    """Represents a first-in, first-out collection of objects."""

    class Enumerator(System.Collections.Generic.IEnumerator[System_Collections_Generic_Queue_T]):
        """This class has no documentation."""

        @property
        def current(self) -> System_Collections_Generic_Queue_T:
            ...

        def dispose(self) -> None:
            ...

        def move_next(self) -> bool:
            ...

    @property
    def count(self) -> int:
        ...

    @property
    def capacity(self) -> int:
        """Gets the total numbers of elements the internal data structure can hold without resizing."""
        ...

    def __contains__(self, item: System_Collections_Generic_Queue_T) -> bool:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, capacity: int) -> None:
        ...

    @overload
    def __init__(self, collection: System.Collections.Generic.IEnumerable[System_Collections_Generic_Queue_T]) -> None:
        ...

    def __iter__(self) -> typing.Iterator[System_Collections_Generic_Queue_T]:
        ...

    def __len__(self) -> int:
        ...

    def clear(self) -> None:
        ...

    def contains(self, item: System_Collections_Generic_Queue_T) -> bool:
        ...

    def copy_to(self, array: typing.List[System_Collections_Generic_Queue_T], array_index: int) -> None:
        ...

    def dequeue(self) -> System_Collections_Generic_Queue_T:
        ...

    def enqueue(self, item: System_Collections_Generic_Queue_T) -> None:
        ...

    def ensure_capacity(self, capacity: int) -> int:
        """
        Ensures that the capacity of this Queue is at least the specified .
        
        :param capacity: The minimum capacity to ensure.
        :returns: The new capacity of this queue.
        """
        ...

    def get_enumerator(self) -> System.Collections.Generic.Queue.Enumerator:
        ...

    def peek(self) -> System_Collections_Generic_Queue_T:
        ...

    def to_array(self) -> typing.List[System_Collections_Generic_Queue_T]:
        ...

    @overload
    def trim_excess(self) -> None:
        ...

    @overload
    def trim_excess(self, capacity: int) -> None:
        """
        Sets the capacity of a Queue{T} object to the specified number of entries.
        
        :param capacity: The new capacity.
        """
        ...

    def try_dequeue(self, result: typing.Optional[System_Collections_Generic_Queue_T]) -> typing.Tuple[bool, System_Collections_Generic_Queue_T]:
        ...

    def try_peek(self, result: typing.Optional[System_Collections_Generic_Queue_T]) -> typing.Tuple[bool, System_Collections_Generic_Queue_T]:
        ...


class EqualityComparer(typing.Generic[System_Collections_Generic_EqualityComparer_T], System.Object, System.Collections.IEqualityComparer, System.Collections.Generic.IEqualityComparer[System_Collections_Generic_EqualityComparer_T], metaclass=abc.ABCMeta):
    """This class has no documentation."""

    DEFAULT: System.Collections.Generic.EqualityComparer[System_Collections_Generic_EqualityComparer_T]

    @staticmethod
    def create(equals: typing.Callable[[System_Collections_Generic_EqualityComparer_T, System_Collections_Generic_EqualityComparer_T], bool], get_hash_code: typing.Callable[[System_Collections_Generic_EqualityComparer_T], int] = None) -> System.Collections.Generic.EqualityComparer[System_Collections_Generic_EqualityComparer_T]:
        """
        Creates an EqualityComparer{T} by using the specified delegates as the implementation of the comparer's
        EqualityComparer{T}.Equals and EqualityComparer{T}.GetHashCode methods.
        
        :param equals: The delegate to use to implement the EqualityComparer{T}.Equals method.
        :param get_hash_code: The delegate to use to implement the EqualityComparer{T}.GetHashCode method. If no delegate is supplied, calls to the resulting comparer's EqualityComparer{T}.GetHashCode will throw NotSupportedException.
        :returns: The new comparer.
        """
        ...

    def equals(self, x: System_Collections_Generic_EqualityComparer_T, y: System_Collections_Generic_EqualityComparer_T) -> bool:
        ...

    def get_hash_code(self, obj: System_Collections_Generic_EqualityComparer_T) -> int:
        ...


class GenericEqualityComparer(typing.Generic[System_Collections_Generic_GenericEqualityComparer_T], System.Collections.Generic.EqualityComparer[System_Collections_Generic_GenericEqualityComparer_T]):
    """This class has no documentation."""

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, x: System_Collections_Generic_GenericEqualityComparer_T, y: System_Collections_Generic_GenericEqualityComparer_T) -> bool:
        ...

    @overload
    def get_hash_code(self, obj: System_Collections_Generic_GenericEqualityComparer_T) -> int:
        ...

    @overload
    def get_hash_code(self) -> int:
        ...


class NullableEqualityComparer(typing.Generic[System_Collections_Generic_NullableEqualityComparer_T], System.Collections.Generic.EqualityComparer[typing.Optional[System_Collections_Generic_NullableEqualityComparer_T]], System.Runtime.Serialization.ISerializable):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, x: typing.Optional[System_Collections_Generic_NullableEqualityComparer_T], y: typing.Optional[System_Collections_Generic_NullableEqualityComparer_T]) -> bool:
        ...

    @overload
    def get_hash_code(self, obj: typing.Optional[System_Collections_Generic_NullableEqualityComparer_T]) -> int:
        ...

    @overload
    def get_hash_code(self) -> int:
        ...

    def get_object_data(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...


class ObjectEqualityComparer(typing.Generic[System_Collections_Generic_ObjectEqualityComparer_T], System.Collections.Generic.EqualityComparer[System_Collections_Generic_ObjectEqualityComparer_T]):
    """This class has no documentation."""

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, x: System_Collections_Generic_ObjectEqualityComparer_T, y: System_Collections_Generic_ObjectEqualityComparer_T) -> bool:
        ...

    @overload
    def get_hash_code(self, obj: System_Collections_Generic_ObjectEqualityComparer_T) -> int:
        ...

    @overload
    def get_hash_code(self) -> int:
        ...


class ByteEqualityComparer(System.Collections.Generic.EqualityComparer[int]):
    """This class has no documentation."""

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, x: int, y: int) -> bool:
        ...

    @overload
    def get_hash_code(self, b: int) -> int:
        ...

    @overload
    def get_hash_code(self) -> int:
        ...


class EnumEqualityComparer(typing.Generic[System_Collections_Generic_EnumEqualityComparer_T], System.Collections.Generic.EqualityComparer[System_Collections_Generic_EnumEqualityComparer_T], System.Runtime.Serialization.ISerializable):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, x: System_Collections_Generic_EnumEqualityComparer_T, y: System_Collections_Generic_EnumEqualityComparer_T) -> bool:
        ...

    @overload
    def get_hash_code(self, obj: System_Collections_Generic_EnumEqualityComparer_T) -> int:
        ...

    @overload
    def get_hash_code(self) -> int:
        ...

    def get_object_data(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...


class IAsyncEnumerator(typing.Generic[System_Collections_Generic_IAsyncEnumerator_T], System.IAsyncDisposable, metaclass=abc.ABCMeta):
    """Supports a simple asynchronous iteration over a generic collection."""

    @property
    @abc.abstractmethod
    def current(self) -> System_Collections_Generic_IAsyncEnumerator_T:
        """Gets the element in the collection at the current position of the enumerator."""
        ...

    def move_next_async(self) -> System.Threading.Tasks.ValueTask[bool]:
        """
        Advances the enumerator asynchronously to the next element of the collection.
        
        :returns: A ValueTask{Boolean} that will complete with a result of true if the enumerator was successfully advanced to the next element, or false if the enumerator has passed the end of the collection.
        """
        ...


class IAlternateEqualityComparer(typing.Generic[System_Collections_Generic_IAlternateEqualityComparer_TAlternate, System_Collections_Generic_IAlternateEqualityComparer_T], metaclass=abc.ABCMeta):
    """
    Implemented by an IEqualityComparer{T} to support comparing
    a TAlternate instance with a T instance.
    """

    def create(self, alternate: System_Collections_Generic_IAlternateEqualityComparer_TAlternate) -> System_Collections_Generic_IAlternateEqualityComparer_T:
        """
        Creates a T that is considered by Equals(TAlternate, T) to be equal
        to the specified .
        
        :param alternate: The instance of type TAlternate for which an equal T is required.
        :returns: A T considered equal to the specified .
        """
        ...

    def equals(self, alternate: System_Collections_Generic_IAlternateEqualityComparer_TAlternate, other: System_Collections_Generic_IAlternateEqualityComparer_T) -> bool:
        """
        Determines whether the specified  equals the specified .
        
        :param alternate: The instance of type TAlternate to compare.
        :param other: The instance of type T to compare.
        :returns: true if the specified instances are equal; otherwise, false.
        """
        ...

    def get_hash_code(self, alternate: System_Collections_Generic_IAlternateEqualityComparer_TAlternate) -> int:
        """
        Returns a hash code for the specified alternate instance.
        
        :param alternate: The instance of type TAlternate for which to get a hash code.
        :returns: A hash code for the specified instance.
        """
        ...


class IList(typing.Generic[System_Collections_Generic_IList_T], System.Collections.Generic.ICollection[System_Collections_Generic_IList_T], metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def __getitem__(self, index: int) -> System_Collections_Generic_IList_T:
        ...

    def __setitem__(self, index: int, value: System_Collections_Generic_IList_T) -> None:
        ...

    def index_of(self, item: System_Collections_Generic_IList_T) -> int:
        ...

    def insert(self, index: int, item: System_Collections_Generic_IList_T) -> None:
        ...

    def remove_at(self, index: int) -> None:
        ...


class IAsyncEnumerable(typing.Generic[System_Collections_Generic_IAsyncEnumerable_T], metaclass=abc.ABCMeta):
    """Exposes an enumerator that provides asynchronous iteration over values of a specified type."""

    def get_async_enumerator(self, cancellation_token: System.Threading.CancellationToken = ...) -> System.Collections.Generic.IAsyncEnumerator[System_Collections_Generic_IAsyncEnumerable_T]:
        """
        Returns an enumerator that iterates asynchronously through the collection.
        
        :param cancellation_token: A CancellationToken that may be used to cancel the asynchronous iteration.
        :returns: An enumerator that can be used to iterate asynchronously through the collection.
        """
        ...


class IReadOnlySet(typing.Generic[System_Collections_Generic_IReadOnlySet_T], System.Collections.Generic.IReadOnlyCollection[System_Collections_Generic_IReadOnlySet_T], metaclass=abc.ABCMeta):
    """Provides a readonly abstraction of a set."""

    def __contains__(self, item: System_Collections_Generic_IReadOnlySet_T) -> bool:
        """
        Determines if the set contains a specific item
        
        :param item: The item to check if the set contains.
        :returns: true if found; otherwise false.
        """
        ...

    def __len__(self) -> int:
        ...

    def contains(self, item: System_Collections_Generic_IReadOnlySet_T) -> bool:
        """
        Determines if the set contains a specific item
        
        :param item: The item to check if the set contains.
        :returns: true if found; otherwise false.
        """
        ...

    def is_proper_subset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_IReadOnlySet_T]) -> bool:
        """
        Determines whether the current set is a proper (strict) subset of a specified collection.
        
        :param other: The collection to compare to the current set.
        :returns: true if the current set is a proper subset of other; otherwise false.
        """
        ...

    def is_proper_superset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_IReadOnlySet_T]) -> bool:
        """
        Determines whether the current set is a proper (strict) superset of a specified collection.
        
        :param other: The collection to compare to the current set.
        :returns: true if the collection is a proper superset of other; otherwise false.
        """
        ...

    def is_subset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_IReadOnlySet_T]) -> bool:
        """
        Determine whether the current set is a subset of a specified collection.
        
        :param other: The collection to compare to the current set.
        :returns: true if the current set is a subset of other; otherwise false.
        """
        ...

    def is_superset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_IReadOnlySet_T]) -> bool:
        """
        Determine whether the current set is a super set of a specified collection.
        
        :param other: The collection to compare to the current set
        :returns: true if the current set is a subset of other; otherwise false.
        """
        ...

    def overlaps(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_IReadOnlySet_T]) -> bool:
        """
        Determines whether the current set overlaps with the specified collection.
        
        :param other: The collection to compare to the current set.
        :returns: true if the current set and other share at least one common element; otherwise, false.
        """
        ...

    def set_equals(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_IReadOnlySet_T]) -> bool:
        """
        Determines whether the current set and the specified collection contain the same elements.
        
        :param other: The collection to compare to the current set.
        :returns: true if the current set is equal to other; otherwise, false.
        """
        ...


class IReadOnlyCollection(typing.Generic[System_Collections_Generic_IReadOnlyCollection_T], System.Collections.Generic.IEnumerable[System_Collections_Generic_IReadOnlyCollection_T], metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def count(self) -> int:
        ...


class IReadOnlyList(typing.Generic[System_Collections_Generic_IReadOnlyList_T], System.Collections.Generic.IReadOnlyCollection[System_Collections_Generic_IReadOnlyList_T], metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def __getitem__(self, index: int) -> System_Collections_Generic_IReadOnlyList_T:
        ...


class IEnumerable(typing.Generic[System_Collections_Generic_IEnumerable_T], System.Collections.IEnumerable, typing.Iterable[System_Collections_Generic_IEnumerable_T], metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def __iter__(self) -> typing.Iterator[System_Collections_Generic_IEnumerable_T]:
        ...


class IReadOnlyDictionary(typing.Generic[System_Collections_Generic_IReadOnlyDictionary_TKey, System_Collections_Generic_IReadOnlyDictionary_TValue], System.Collections.Generic.IReadOnlyCollection[System.Collections.Generic.KeyValuePair[System_Collections_Generic_IReadOnlyDictionary_TKey, System_Collections_Generic_IReadOnlyDictionary_TValue]], metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def keys(self) -> typing.Iterable[System_Collections_Generic_IReadOnlyDictionary_TKey]:
        ...

    @property
    @abc.abstractmethod
    def values(self) -> typing.Iterable[System_Collections_Generic_IReadOnlyDictionary_TValue]:
        ...

    def __contains__(self, key: System_Collections_Generic_IReadOnlyDictionary_TKey) -> bool:
        ...

    def __getitem__(self, key: System_Collections_Generic_IReadOnlyDictionary_TKey) -> System_Collections_Generic_IReadOnlyDictionary_TValue:
        ...

    def __len__(self) -> int:
        ...

    def contains_key(self, key: System_Collections_Generic_IReadOnlyDictionary_TKey) -> bool:
        ...

    def try_get_value(self, key: System_Collections_Generic_IReadOnlyDictionary_TKey, value: typing.Optional[System_Collections_Generic_IReadOnlyDictionary_TValue]) -> typing.Tuple[bool, System_Collections_Generic_IReadOnlyDictionary_TValue]:
        ...


class CollectionExtensions(System.Object):
    """This class has no documentation."""


class IComparer(typing.Generic[System_Collections_Generic_IComparer_T], metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def compare(self, x: System_Collections_Generic_IComparer_T, y: System_Collections_Generic_IComparer_T) -> int:
        ...


class HashSet(typing.Generic[System_Collections_Generic_HashSet_T], System.Object, System.Collections.Generic.ISet[System_Collections_Generic_HashSet_T], System.Collections.Generic.IReadOnlySet[System_Collections_Generic_HashSet_T], System.Runtime.Serialization.ISerializable, System.Runtime.Serialization.IDeserializationCallback, typing.Iterable[System_Collections_Generic_HashSet_T]):
    """This class has no documentation."""

    class AlternateLookup(typing.Generic[System_Collections_Generic_HashSet_AlternateLookup_TAlternate]):
        """
        Provides a type that may be used to perform operations on a HashSet{T}
        using a TAlternate instead of a T.
        """

        @property
        def set(self) -> System.Collections.Generic.HashSet[System_Collections_Generic_HashSet_T]:
            """Gets the HashSet{T} against which this instance performs operations."""
            ...

        def __contains__(self, item: System_Collections_Generic_HashSet_AlternateLookup_TAlternate) -> bool:
            """
            Determines whether a set contains the specified element.
            
            :param item: The element to locate in the set.
            :returns: true if the set contains the specified element; otherwise, false.
            """
            ...

        def __len__(self) -> int:
            ...

        def add(self, item: System_Collections_Generic_HashSet_AlternateLookup_TAlternate) -> bool:
            """
            Adds the specified element to a set.
            
            :param item: The element to add to the set.
            :returns: true if the element is added to the set; false if the element is already present.
            """
            ...

        def contains(self, item: System_Collections_Generic_HashSet_AlternateLookup_TAlternate) -> bool:
            """
            Determines whether a set contains the specified element.
            
            :param item: The element to locate in the set.
            :returns: true if the set contains the specified element; otherwise, false.
            """
            ...

        def remove(self, item: System_Collections_Generic_HashSet_AlternateLookup_TAlternate) -> bool:
            """
            Removes the specified element from a set.
            
            :param item: The element to remove.
            :returns: true if the element is successfully found and removed; otherwise, false.
            """
            ...

        def try_get_value(self, equal_value: System_Collections_Generic_HashSet_AlternateLookup_TAlternate, actual_value: typing.Optional[System_Collections_Generic_HashSet_T]) -> typing.Tuple[bool, System_Collections_Generic_HashSet_T]:
            """
            Searches the set for a given value and returns the equal value it finds, if any.
            
            :param equal_value: The value to search for.
            :param actual_value: The value from the set that the search found, or the default value of T when the search yielded no match.
            :returns: A value indicating whether the search was successful.
            """
            ...

    class Enumerator(System.Collections.Generic.IEnumerator[System_Collections_Generic_HashSet_T]):
        """This class has no documentation."""

        @property
        def current(self) -> System_Collections_Generic_HashSet_T:
            ...

        def dispose(self) -> None:
            ...

        def move_next(self) -> bool:
            ...

    @property
    def count(self) -> int:
        """Gets the number of elements that are contained in the set."""
        ...

    @property
    def capacity(self) -> int:
        """Gets the total numbers of elements the internal data structure can hold without resizing."""
        ...

    @property
    def comparer(self) -> System.Collections.Generic.IEqualityComparer[System_Collections_Generic_HashSet_T]:
        """Gets the IEqualityComparer object that is used to determine equality for the values in the set."""
        ...

    def __contains__(self, item: System_Collections_Generic_HashSet_T) -> bool:
        """
        Determines whether the HashSet{T} contains the specified element.
        
        :param item: The element to locate in the HashSet{T} object.
        :returns: true if the HashSet{T} object contains the specified element; otherwise, false.
        """
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Generic_HashSet_T]) -> None:
        ...

    @overload
    def __init__(self, capacity: int) -> None:
        ...

    @overload
    def __init__(self, collection: System.Collections.Generic.IEnumerable[System_Collections_Generic_HashSet_T]) -> None:
        ...

    @overload
    def __init__(self, collection: System.Collections.Generic.IEnumerable[System_Collections_Generic_HashSet_T], comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Generic_HashSet_T]) -> None:
        ...

    @overload
    def __init__(self, capacity: int, comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Generic_HashSet_T]) -> None:
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """
        This method is protected.
        
        Obsoletions.LegacyFormatterImplMessage
        """
        ...

    def __iter__(self) -> typing.Iterator[System_Collections_Generic_HashSet_T]:
        ...

    def __len__(self) -> int:
        ...

    def add(self, item: System_Collections_Generic_HashSet_T) -> bool:
        """
        Adds the specified element to the HashSet{T}.
        
        :param item: The element to add to the set.
        :returns: true if the element is added to the HashSet{T} object; false if the element is already present.
        """
        ...

    def clear(self) -> None:
        """Removes all elements from the HashSet{T} object."""
        ...

    def contains(self, item: System_Collections_Generic_HashSet_T) -> bool:
        """
        Determines whether the HashSet{T} contains the specified element.
        
        :param item: The element to locate in the HashSet{T} object.
        :returns: true if the HashSet{T} object contains the specified element; otherwise, false.
        """
        ...

    @overload
    def copy_to(self, array: typing.List[System_Collections_Generic_HashSet_T]) -> None:
        ...

    @overload
    def copy_to(self, array: typing.List[System_Collections_Generic_HashSet_T], array_index: int) -> None:
        """
        Copies the elements of a HashSet{T} object to an array, starting at the specified array index.
        
        :param array: The destination array.
        :param array_index: The zero-based index in array at which copying begins.
        """
        ...

    @overload
    def copy_to(self, array: typing.List[System_Collections_Generic_HashSet_T], array_index: int, count: int) -> None:
        ...

    @staticmethod
    def create_set_comparer() -> System.Collections.Generic.IEqualityComparer[System.Collections.Generic.HashSet[System_Collections_Generic_HashSet_T]]:
        """Returns an IEqualityComparer object that can be used for equality testing of a HashSet{T} object."""
        ...

    def ensure_capacity(self, capacity: int) -> int:
        """Ensures that this hash set can hold the specified number of elements without growing."""
        ...

    def except_with(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_HashSet_T]) -> None:
        """
        Removes all elements in the specified collection from the current HashSet{T} object.
        
        :param other: The collection to compare to the current HashSet{T} object.
        """
        ...

    def get_enumerator(self) -> System.Collections.Generic.HashSet.Enumerator:
        ...

    def get_object_data(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """Obsoletions.LegacyFormatterImplMessage"""
        warnings.warn("Obsoletions.LegacyFormatterImplMessage", DeprecationWarning)

    def intersect_with(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_HashSet_T]) -> None:
        """
        Modifies the current HashSet{T} object to contain only elements that are present in that object and in the specified collection.
        
        :param other: The collection to compare to the current HashSet{T} object.
        """
        ...

    def is_proper_subset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_HashSet_T]) -> bool:
        """
        Determines whether a HashSet{T} object is a proper subset of the specified collection.
        
        :param other: The collection to compare to the current HashSet{T} object.
        :returns: true if the HashSet{T} object is a proper subset of ; otherwise, false.
        """
        ...

    def is_proper_superset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_HashSet_T]) -> bool:
        """
        Determines whether a HashSet{T} object is a proper superset of the specified collection.
        
        :param other: The collection to compare to the current HashSet{T} object.
        :returns: true if the HashSet{T} object is a proper superset of ; otherwise, false.
        """
        ...

    def is_subset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_HashSet_T]) -> bool:
        """
        Determines whether a HashSet{T} object is a subset of the specified collection.
        
        :param other: The collection to compare to the current HashSet{T} object.
        :returns: true if the HashSet{T} object is a subset of ; otherwise, false.
        """
        ...

    def is_superset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_HashSet_T]) -> bool:
        """
        Determines whether a HashSet{T} object is a proper superset of the specified collection.
        
        :param other: The collection to compare to the current HashSet{T} object.
        :returns: true if the HashSet{T} object is a superset of ; otherwise, false.
        """
        ...

    def on_deserialization(self, sender: typing.Any) -> None:
        ...

    def overlaps(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_HashSet_T]) -> bool:
        """
        Determines whether the current HashSet{T} object and a specified collection share common elements.
        
        :param other: The collection to compare to the current HashSet{T} object.
        :returns: true if the HashSet{T} object and  share at least one common element; otherwise, false.
        """
        ...

    def remove(self, item: System_Collections_Generic_HashSet_T) -> bool:
        ...

    def remove_where(self, match: typing.Callable[[System_Collections_Generic_HashSet_T], bool]) -> int:
        """Removes all elements that match the conditions defined by the specified predicate from a HashSet{T} collection."""
        ...

    def set_equals(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_HashSet_T]) -> bool:
        """
        Determines whether a HashSet{T} object and the specified collection contain the same elements.
        
        :param other: The collection to compare to the current HashSet{T} object.
        :returns: true if the HashSet{T} object is equal to ; otherwise, false.
        """
        ...

    def symmetric_except_with(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_HashSet_T]) -> None:
        """
        Modifies the current HashSet{T} object to contain only elements that are present either in that object or in the specified collection, but not both.
        
        :param other: The collection to compare to the current HashSet{T} object.
        """
        ...

    @overload
    def trim_excess(self) -> None:
        """
        Sets the capacity of a HashSet{T} object to the actual number of elements it contains,
        rounded up to a nearby, implementation-specific value.
        """
        ...

    @overload
    def trim_excess(self, capacity: int) -> None:
        """
        Sets the capacity of a HashSet{T} object to the specified number of entries,
        rounded up to a nearby, implementation-specific value.
        
        :param capacity: The new capacity.
        """
        ...

    def try_get_value(self, equal_value: System_Collections_Generic_HashSet_T, actual_value: typing.Optional[System_Collections_Generic_HashSet_T]) -> typing.Tuple[bool, System_Collections_Generic_HashSet_T]:
        """
        Searches the set for a given value and returns the equal value it finds, if any.
        
        :param equal_value: The value to search for.
        :param actual_value: The value from the set that the search found, or the default value of T when the search yielded no match.
        :returns: A value indicating whether the search was successful.
        """
        ...

    def union_with(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_HashSet_T]) -> None:
        """
        Modifies the current HashSet{T} object to contain all elements that are present in itself, the specified collection, or both.
        
        :param other: The collection to compare to the current HashSet{T} object.
        """
        ...


class NonRandomizedStringEqualityComparer(System.Object, System.Collections.Generic.IInternalStringEqualityComparer, System.Runtime.Serialization.ISerializable):
    """This class has no documentation."""

    def __init__(self, information: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """
        This method is protected.
        
        Obsoletions.LegacyFormatterImplMessage
        """
        warnings.warn("Obsoletions.LegacyFormatterImplMessage", DeprecationWarning)

    def equals(self, x: str, y: str) -> bool:
        ...

    def get_hash_code(self, obj: str) -> int:
        ...

    @staticmethod
    def get_string_comparer(comparer: typing.Any) -> System.Collections.Generic.IEqualityComparer[str]:
        ...

    def get_underlying_equality_comparer(self) -> System.Collections.Generic.IEqualityComparer[str]:
        ...


class ISet(typing.Generic[System_Collections_Generic_ISet_T], System.Collections.Generic.ICollection[System_Collections_Generic_ISet_T], metaclass=abc.ABCMeta):
    """
    Generic collection that guarantees the uniqueness of its elements, as defined
    by some comparer. It also supports basic set operations such as Union, Intersection,
    Complement and Exclusive Complement.
    """

    def except_with(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_ISet_T]) -> None:
        ...

    def intersect_with(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_ISet_T]) -> None:
        ...

    def is_proper_subset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_ISet_T]) -> bool:
        ...

    def is_proper_superset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_ISet_T]) -> bool:
        ...

    def is_subset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_ISet_T]) -> bool:
        ...

    def is_superset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_ISet_T]) -> bool:
        ...

    def overlaps(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_ISet_T]) -> bool:
        ...

    def set_equals(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_ISet_T]) -> bool:
        ...

    def symmetric_except_with(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_ISet_T]) -> None:
        ...

    def union_with(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_ISet_T]) -> None:
        ...


class IDictionary(typing.Generic[System_Collections_Generic_IDictionary_TKey, System_Collections_Generic_IDictionary_TValue], System.Collections.Generic.ICollection[System.Collections.Generic.KeyValuePair[System_Collections_Generic_IDictionary_TKey, System_Collections_Generic_IDictionary_TValue]], metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def keys(self) -> System.Collections.Generic.ICollection[System_Collections_Generic_IDictionary_TKey]:
        ...

    @property
    @abc.abstractmethod
    def values(self) -> System.Collections.Generic.ICollection[System_Collections_Generic_IDictionary_TValue]:
        ...

    def __contains__(self, key: System_Collections_Generic_IDictionary_TKey) -> bool:
        ...

    def __getitem__(self, key: System_Collections_Generic_IDictionary_TKey) -> System_Collections_Generic_IDictionary_TValue:
        ...

    def __len__(self) -> int:
        ...

    def __setitem__(self, key: System_Collections_Generic_IDictionary_TKey, value: System_Collections_Generic_IDictionary_TValue) -> None:
        ...

    def add(self, key: System_Collections_Generic_IDictionary_TKey, value: System_Collections_Generic_IDictionary_TValue) -> None:
        ...

    def contains_key(self, key: System_Collections_Generic_IDictionary_TKey) -> bool:
        ...

    def remove(self, key: System_Collections_Generic_IDictionary_TKey) -> bool:
        ...

    def try_get_value(self, key: System_Collections_Generic_IDictionary_TKey, value: typing.Optional[System_Collections_Generic_IDictionary_TValue]) -> typing.Tuple[bool, System_Collections_Generic_IDictionary_TValue]:
        ...


class IEnumerator(typing.Generic[System_Collections_Generic_IEnumerator_T], System.IDisposable, System.Collections.IEnumerator, metaclass=abc.ABCMeta):
    """This class has no documentation."""


class Dictionary(typing.Generic[System_Collections_Generic_Dictionary_TKey, System_Collections_Generic_Dictionary_TValue], System.Object, System.Collections.Generic.IDictionary[System_Collections_Generic_Dictionary_TKey, System_Collections_Generic_Dictionary_TValue], System.Collections.IDictionary, System.Collections.Generic.IReadOnlyDictionary[System_Collections_Generic_Dictionary_TKey, System_Collections_Generic_Dictionary_TValue], System.Runtime.Serialization.ISerializable, System.Runtime.Serialization.IDeserializationCallback, typing.Iterable[System.Collections.Generic.KeyValuePair[System_Collections_Generic_Dictionary_TKey, System_Collections_Generic_Dictionary_TValue]]):
    """This class has no documentation."""

    class AlternateLookup(typing.Generic[System_Collections_Generic_Dictionary_AlternateLookup_TAlternateKey]):
        """
        Provides a type that may be used to perform operations on a Dictionary{TKey, TValue}
        using a TAlternateKey as a key instead of a TKey.
        """

        @property
        def dictionary(self) -> System.Collections.Generic.Dictionary[System_Collections_Generic_Dictionary_TKey, System_Collections_Generic_Dictionary_TValue]:
            """Gets the Dictionary{TKey, TValue} against which this instance performs operations."""
            ...

        def __contains__(self, key: System_Collections_Generic_Dictionary_AlternateLookup_TAlternateKey) -> bool:
            """
            Determines whether the Dictionary{TKey, TValue} contains the specified alternate key.
            
            :param key: The alternate key to check.
            :returns: true if the key is in the dictionary; otherwise, false.
            """
            ...

        def __getitem__(self, key: System_Collections_Generic_Dictionary_AlternateLookup_TAlternateKey) -> System_Collections_Generic_Dictionary_TValue:
            """
            Gets or sets the value associated with the specified alternate key.
            
            :param key: The alternate key of the value to get or set.
            """
            ...

        def __len__(self) -> int:
            ...

        def __setitem__(self, key: System_Collections_Generic_Dictionary_AlternateLookup_TAlternateKey, value: System_Collections_Generic_Dictionary_TValue) -> None:
            """
            Gets or sets the value associated with the specified alternate key.
            
            :param key: The alternate key of the value to get or set.
            """
            ...

        def contains_key(self, key: System_Collections_Generic_Dictionary_AlternateLookup_TAlternateKey) -> bool:
            """
            Determines whether the Dictionary{TKey, TValue} contains the specified alternate key.
            
            :param key: The alternate key to check.
            :returns: true if the key is in the dictionary; otherwise, false.
            """
            ...

        @overload
        def remove(self, key: System_Collections_Generic_Dictionary_AlternateLookup_TAlternateKey) -> bool:
            """
            Removes the value with the specified alternate key from the Dictionary{TKey, TValue}.
            
            :param key: The alternate key of the element to remove.
            :returns: true if the element is successfully found and removed; otherwise, false.
            """
            ...

        @overload
        def remove(self, key: System_Collections_Generic_Dictionary_AlternateLookup_TAlternateKey, actual_key: typing.Optional[System_Collections_Generic_Dictionary_TKey], value: typing.Optional[System_Collections_Generic_Dictionary_TValue]) -> typing.Tuple[bool, System_Collections_Generic_Dictionary_TKey, System_Collections_Generic_Dictionary_TValue]:
            """
            Removes the value with the specified alternate key from the Dictionary{TKey, TValue},
            and copies the element to the value parameter.
            
            :param key: The alternate key of the element to remove.
            :param actual_key: The removed key.
            :param value: The removed element.
            :returns: true if the element is successfully found and removed; otherwise, false.
            """
            ...

        def try_add(self, key: System_Collections_Generic_Dictionary_AlternateLookup_TAlternateKey, value: System_Collections_Generic_Dictionary_TValue) -> bool:
            """
            Attempts to add the specified key and value to the dictionary.
            
            :param key: The alternate key of the element to add.
            :param value: The value of the element to add.
            :returns: true if the key/value pair was added to the dictionary successfully; otherwise, false.
            """
            ...

        @overload
        def try_get_value(self, key: System_Collections_Generic_Dictionary_AlternateLookup_TAlternateKey, value: typing.Optional[System_Collections_Generic_Dictionary_TValue]) -> typing.Tuple[bool, System_Collections_Generic_Dictionary_TValue]:
            """
            Gets the value associated with the specified alternate key.
            
            :param key: The alternate key of the value to get.
            :param value: When this method returns, contains the value associated with the specified key, if the key is found; otherwise, the default value for the type of the value parameter.
            :returns: true if an entry was found; otherwise, false.
            """
            ...

        @overload
        def try_get_value(self, key: System_Collections_Generic_Dictionary_AlternateLookup_TAlternateKey, actual_key: typing.Optional[System_Collections_Generic_Dictionary_TKey], value: typing.Optional[System_Collections_Generic_Dictionary_TValue]) -> typing.Tuple[bool, System_Collections_Generic_Dictionary_TKey, System_Collections_Generic_Dictionary_TValue]:
            """
            Gets the value associated with the specified alternate key.
            
            :param key: The alternate key of the value to get.
            :param actual_key: When this method returns, contains the actual key associated with the alternate key, if the key is found; otherwise, the default value for the type of the key parameter.
            :param value: When this method returns, contains the value associated with the specified key, if the key is found; otherwise, the default value for the type of the value parameter.
            :returns: true if an entry was found; otherwise, false.
            """
            ...

    class Enumerator(System.Collections.Generic.IEnumerator[System.Collections.Generic.KeyValuePair[System_Collections_Generic_Dictionary_TKey, System_Collections_Generic_Dictionary_TValue]], System.Collections.IDictionaryEnumerator):
        """This class has no documentation."""

        @property
        def current(self) -> System.Collections.Generic.KeyValuePair[System_Collections_Generic_Dictionary_TKey, System_Collections_Generic_Dictionary_TValue]:
            ...

        def dispose(self) -> None:
            ...

        def move_next(self) -> bool:
            ...

    class KeyCollection(System.Object, System.Collections.Generic.ICollection[System_Collections_Generic_Dictionary_TKey], System.Collections.ICollection, System.Collections.Generic.IReadOnlyCollection[System_Collections_Generic_Dictionary_TKey], typing.Iterable[System_Collections_Generic_Dictionary_TKey]):
        """This class has no documentation."""

        class Enumerator(System.Collections.Generic.IEnumerator[System_Collections_Generic_Dictionary_TKey]):
            """This class has no documentation."""

            @property
            def current(self) -> System_Collections_Generic_Dictionary_TKey:
                ...

            def dispose(self) -> None:
                ...

            def move_next(self) -> bool:
                ...

        @property
        def count(self) -> int:
            ...

        def __contains__(self, item: System_Collections_Generic_Dictionary_TKey) -> bool:
            ...

        def __init__(self, dictionary: System.Collections.Generic.Dictionary[System_Collections_Generic_Dictionary_TKey, System_Collections_Generic_Dictionary_TValue]) -> None:
            ...

        def __iter__(self) -> typing.Iterator[System_Collections_Generic_Dictionary_TKey]:
            ...

        def __len__(self) -> int:
            ...

        def contains(self, item: System_Collections_Generic_Dictionary_TKey) -> bool:
            ...

        def copy_to(self, array: typing.List[System_Collections_Generic_Dictionary_TKey], index: int) -> None:
            ...

        def get_enumerator(self) -> System.Collections.Generic.Dictionary.KeyCollection.Enumerator:
            ...

    class ValueCollection(System.Object, System.Collections.Generic.ICollection[System_Collections_Generic_Dictionary_TValue], System.Collections.ICollection, System.Collections.Generic.IReadOnlyCollection[System_Collections_Generic_Dictionary_TValue], typing.Iterable[System_Collections_Generic_Dictionary_TValue]):
        """This class has no documentation."""

        class Enumerator(System.Collections.Generic.IEnumerator[System_Collections_Generic_Dictionary_TValue]):
            """This class has no documentation."""

            @property
            def current(self) -> System_Collections_Generic_Dictionary_TValue:
                ...

            def dispose(self) -> None:
                ...

            def move_next(self) -> bool:
                ...

        @property
        def count(self) -> int:
            ...

        def __init__(self, dictionary: System.Collections.Generic.Dictionary[System_Collections_Generic_Dictionary_TKey, System_Collections_Generic_Dictionary_TValue]) -> None:
            ...

        def __iter__(self) -> typing.Iterator[System_Collections_Generic_Dictionary_TValue]:
            ...

        def __len__(self) -> int:
            ...

        def copy_to(self, array: typing.List[System_Collections_Generic_Dictionary_TValue], index: int) -> None:
            ...

        def get_enumerator(self) -> System.Collections.Generic.Dictionary.ValueCollection.Enumerator:
            ...

    @property
    def comparer(self) -> System.Collections.Generic.IEqualityComparer[System_Collections_Generic_Dictionary_TKey]:
        ...

    @property
    def count(self) -> int:
        ...

    @property
    def capacity(self) -> int:
        """Gets the total numbers of elements the internal data structure can hold without resizing."""
        ...

    @property
    def keys(self) -> System.Collections.Generic.Dictionary.KeyCollection:
        ...

    @property
    def values(self) -> System.Collections.Generic.Dictionary.ValueCollection:
        ...

    def __contains__(self, key: System_Collections_Generic_Dictionary_TKey) -> bool:
        ...

    def __getitem__(self, key: System_Collections_Generic_Dictionary_TKey) -> System_Collections_Generic_Dictionary_TValue:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, capacity: int) -> None:
        ...

    @overload
    def __init__(self, comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Generic_Dictionary_TKey]) -> None:
        ...

    @overload
    def __init__(self, capacity: int, comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Generic_Dictionary_TKey]) -> None:
        ...

    @overload
    def __init__(self, dictionary: System.Collections.Generic.IDictionary[System_Collections_Generic_Dictionary_TKey, System_Collections_Generic_Dictionary_TValue]) -> None:
        ...

    @overload
    def __init__(self, dictionary: System.Collections.Generic.IDictionary[System_Collections_Generic_Dictionary_TKey, System_Collections_Generic_Dictionary_TValue], comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Generic_Dictionary_TKey]) -> None:
        ...

    @overload
    def __init__(self, collection: System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[System_Collections_Generic_Dictionary_TKey, System_Collections_Generic_Dictionary_TValue]]) -> None:
        ...

    @overload
    def __init__(self, collection: System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[System_Collections_Generic_Dictionary_TKey, System_Collections_Generic_Dictionary_TValue]], comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Generic_Dictionary_TKey]) -> None:
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """
        This method is protected.
        
        Obsoletions.LegacyFormatterImplMessage
        """
        ...

    def __iter__(self) -> typing.Iterator[System.Collections.Generic.KeyValuePair[System_Collections_Generic_Dictionary_TKey, System_Collections_Generic_Dictionary_TValue]]:
        ...

    def __len__(self) -> int:
        ...

    def __setitem__(self, key: System_Collections_Generic_Dictionary_TKey, value: System_Collections_Generic_Dictionary_TValue) -> None:
        ...

    def add(self, key: System_Collections_Generic_Dictionary_TKey, value: System_Collections_Generic_Dictionary_TValue) -> None:
        ...

    def clear(self) -> None:
        ...

    def contains_key(self, key: System_Collections_Generic_Dictionary_TKey) -> bool:
        ...

    def contains_value(self, value: System_Collections_Generic_Dictionary_TValue) -> bool:
        ...

    def ensure_capacity(self, capacity: int) -> int:
        """Ensures that the dictionary can hold up to 'capacity' entries without any further expansion of its backing storage"""
        ...

    def get_enumerator(self) -> System.Collections.Generic.Dictionary.Enumerator:
        ...

    def get_object_data(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """Obsoletions.LegacyFormatterImplMessage"""
        warnings.warn("Obsoletions.LegacyFormatterImplMessage", DeprecationWarning)

    def on_deserialization(self, sender: typing.Any) -> None:
        ...

    @overload
    def remove(self, key: System_Collections_Generic_Dictionary_TKey) -> bool:
        ...

    @overload
    def remove(self, key: System_Collections_Generic_Dictionary_TKey, value: typing.Optional[System_Collections_Generic_Dictionary_TValue]) -> typing.Tuple[bool, System_Collections_Generic_Dictionary_TValue]:
        ...

    @overload
    def trim_excess(self) -> None:
        """Sets the capacity of this dictionary to what it would be if it had been originally initialized with all its entries"""
        ...

    @overload
    def trim_excess(self, capacity: int) -> None:
        """Sets the capacity of this dictionary to hold up 'capacity' entries without any further expansion of its backing storage"""
        ...

    def try_add(self, key: System_Collections_Generic_Dictionary_TKey, value: System_Collections_Generic_Dictionary_TValue) -> bool:
        ...

    def try_get_value(self, key: System_Collections_Generic_Dictionary_TKey, value: typing.Optional[System_Collections_Generic_Dictionary_TValue]) -> typing.Tuple[bool, System_Collections_Generic_Dictionary_TValue]:
        ...


class IEqualityComparer(typing.Generic[System_Collections_Generic_IEqualityComparer_T], metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def equals(self, x: System_Collections_Generic_IEqualityComparer_T, y: System_Collections_Generic_IEqualityComparer_T) -> bool:
        ...

    def get_hash_code(self, obj: System_Collections_Generic_IEqualityComparer_T) -> int:
        ...


class KeyValuePair(typing.Generic[System_Collections_Generic_KeyValuePair_TKey, System_Collections_Generic_KeyValuePair_TValue]):
    """This class has no documentation."""

    @property
    def key(self) -> System_Collections_Generic_KeyValuePair_TKey:
        ...

    @property
    def value(self) -> System_Collections_Generic_KeyValuePair_TValue:
        ...

    def __init__(self, key: System_Collections_Generic_KeyValuePair_TKey, value: System_Collections_Generic_KeyValuePair_TValue) -> None:
        ...

    def deconstruct(self, key: typing.Optional[System_Collections_Generic_KeyValuePair_TKey], value: typing.Optional[System_Collections_Generic_KeyValuePair_TValue]) -> typing.Tuple[None, System_Collections_Generic_KeyValuePair_TKey, System_Collections_Generic_KeyValuePair_TValue]:
        ...

    def to_string(self) -> str:
        ...


class KeyNotFoundException(System.SystemException):
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


class Comparer(typing.Generic[System_Collections_Generic_Comparer_T], System.Object, System.Collections.IComparer, System.Collections.Generic.IComparer[System_Collections_Generic_Comparer_T], metaclass=abc.ABCMeta):
    """This class has no documentation."""

    DEFAULT: System.Collections.Generic.Comparer[System_Collections_Generic_Comparer_T]

    def compare(self, x: System_Collections_Generic_Comparer_T, y: System_Collections_Generic_Comparer_T) -> int:
        ...

    @staticmethod
    def create(comparison: typing.Callable[[System_Collections_Generic_Comparer_T, System_Collections_Generic_Comparer_T], int]) -> System.Collections.Generic.Comparer[System_Collections_Generic_Comparer_T]:
        ...


class GenericComparer(typing.Generic[System_Collections_Generic_GenericComparer_T], System.Collections.Generic.Comparer[System_Collections_Generic_GenericComparer_T]):
    """This class has no documentation."""

    def compare(self, x: System_Collections_Generic_GenericComparer_T, y: System_Collections_Generic_GenericComparer_T) -> int:
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...


class NullableComparer(typing.Generic[System_Collections_Generic_NullableComparer_T], System.Collections.Generic.Comparer[typing.Optional[System_Collections_Generic_NullableComparer_T]], System.Runtime.Serialization.ISerializable):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...

    def compare(self, x: typing.Optional[System_Collections_Generic_NullableComparer_T], y: typing.Optional[System_Collections_Generic_NullableComparer_T]) -> int:
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def get_object_data(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        ...


class ObjectComparer(typing.Generic[System_Collections_Generic_ObjectComparer_T], System.Collections.Generic.Comparer[System_Collections_Generic_ObjectComparer_T]):
    """This class has no documentation."""

    def compare(self, x: System_Collections_Generic_ObjectComparer_T, y: System_Collections_Generic_ObjectComparer_T) -> int:
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...


class SortedSet(typing.Generic[System_Collections_Generic_SortedSet_T], System.Object, System.Collections.Generic.ISet[System_Collections_Generic_SortedSet_T], System.Collections.ICollection, System.Collections.Generic.IReadOnlySet[System_Collections_Generic_SortedSet_T], System.Runtime.Serialization.ISerializable, System.Runtime.Serialization.IDeserializationCallback, typing.Iterable[System_Collections_Generic_SortedSet_T]):
    """This class has no documentation."""

    class Enumerator(System.Collections.Generic.IEnumerator[System_Collections_Generic_SortedSet_T], System.Runtime.Serialization.ISerializable, System.Runtime.Serialization.IDeserializationCallback):
        """This class has no documentation."""

        @property
        def current(self) -> System_Collections_Generic_SortedSet_T:
            ...

        def dispose(self) -> None:
            ...

        def move_next(self) -> bool:
            ...

    @property
    def count(self) -> int:
        ...

    @property
    def comparer(self) -> System.Collections.Generic.IComparer[System_Collections_Generic_SortedSet_T]:
        ...

    @property
    def min(self) -> System_Collections_Generic_SortedSet_T:
        ...

    @property
    def max(self) -> System_Collections_Generic_SortedSet_T:
        ...

    def __contains__(self, item: System_Collections_Generic_SortedSet_T) -> bool:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, comparer: System.Collections.Generic.IComparer[System_Collections_Generic_SortedSet_T]) -> None:
        ...

    @overload
    def __init__(self, collection: System.Collections.Generic.IEnumerable[System_Collections_Generic_SortedSet_T]) -> None:
        ...

    @overload
    def __init__(self, collection: System.Collections.Generic.IEnumerable[System_Collections_Generic_SortedSet_T], comparer: System.Collections.Generic.IComparer[System_Collections_Generic_SortedSet_T]) -> None:
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """
        This method is protected.
        
        Obsoletions.LegacyFormatterImplMessage
        """
        ...

    def __iter__(self) -> typing.Iterator[System_Collections_Generic_SortedSet_T]:
        ...

    def __len__(self) -> int:
        ...

    def add(self, item: System_Collections_Generic_SortedSet_T) -> bool:
        ...

    def clear(self) -> None:
        ...

    def contains(self, item: System_Collections_Generic_SortedSet_T) -> bool:
        ...

    @overload
    def copy_to(self, array: typing.List[System_Collections_Generic_SortedSet_T]) -> None:
        ...

    @overload
    def copy_to(self, array: typing.List[System_Collections_Generic_SortedSet_T], index: int) -> None:
        ...

    @overload
    def copy_to(self, array: typing.List[System_Collections_Generic_SortedSet_T], index: int, count: int) -> None:
        ...

    @staticmethod
    @overload
    def create_set_comparer() -> System.Collections.Generic.IEqualityComparer[System.Collections.Generic.SortedSet[System_Collections_Generic_SortedSet_T]]:
        """Returns an IEqualityComparer{T} object that can be used to create a collection that contains individual sets."""
        ...

    @staticmethod
    @overload
    def create_set_comparer(member_equality_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Generic_SortedSet_T]) -> System.Collections.Generic.IEqualityComparer[System.Collections.Generic.SortedSet[System_Collections_Generic_SortedSet_T]]:
        """Returns an IEqualityComparer{T} object, according to a specified comparer, that can be used to create a collection that contains individual sets."""
        ...

    def except_with(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_SortedSet_T]) -> None:
        ...

    def get_enumerator(self) -> System.Collections.Generic.SortedSet.Enumerator:
        ...

    def get_object_data(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """This method is protected."""
        ...

    def get_view_between(self, lower_value: System_Collections_Generic_SortedSet_T, upper_value: System_Collections_Generic_SortedSet_T) -> System.Collections.Generic.SortedSet[System_Collections_Generic_SortedSet_T]:
        ...

    def intersect_with(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_SortedSet_T]) -> None:
        ...

    def is_proper_subset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_SortedSet_T]) -> bool:
        ...

    def is_proper_superset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_SortedSet_T]) -> bool:
        ...

    def is_subset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_SortedSet_T]) -> bool:
        ...

    def is_superset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_SortedSet_T]) -> bool:
        ...

    def on_deserialization(self, sender: typing.Any) -> None:
        """This method is protected."""
        ...

    def overlaps(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_SortedSet_T]) -> bool:
        ...

    def remove(self, item: System_Collections_Generic_SortedSet_T) -> bool:
        ...

    def remove_where(self, match: typing.Callable[[System_Collections_Generic_SortedSet_T], bool]) -> int:
        ...

    def reverse(self) -> System.Collections.Generic.IEnumerable[System_Collections_Generic_SortedSet_T]:
        ...

    def set_equals(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_SortedSet_T]) -> bool:
        ...

    def symmetric_except_with(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_SortedSet_T]) -> None:
        ...

    def try_get_value(self, equal_value: System_Collections_Generic_SortedSet_T, actual_value: typing.Optional[System_Collections_Generic_SortedSet_T]) -> typing.Tuple[bool, System_Collections_Generic_SortedSet_T]:
        """
        Searches the set for a given value and returns the equal value it finds, if any.
        
        :param equal_value: The value to search for.
        :param actual_value: The value from the set that the search found, or the default value of T when the search yielded no match.
        :returns: A value indicating whether the search was successful.
        """
        ...

    def union_with(self, other: System.Collections.Generic.IEnumerable[System_Collections_Generic_SortedSet_T]) -> None:
        ...


class SortedList(typing.Generic[System_Collections_Generic_SortedList_TKey, System_Collections_Generic_SortedList_TValue], System.Object, System.Collections.Generic.IDictionary[System_Collections_Generic_SortedList_TKey, System_Collections_Generic_SortedList_TValue], System.Collections.IDictionary, System.Collections.Generic.IReadOnlyDictionary[System_Collections_Generic_SortedList_TKey, System_Collections_Generic_SortedList_TValue], typing.Iterable[System.Collections.Generic.KeyValuePair[System_Collections_Generic_SortedList_TKey, System_Collections_Generic_SortedList_TValue]]):
    """This class has no documentation."""

    class KeyList(System.Object, System.Collections.Generic.IList[System_Collections_Generic_SortedList_TKey], System.Collections.ICollection, typing.Iterable[System_Collections_Generic_SortedList_TKey]):
        """This class has no documentation."""

        @property
        def count(self) -> int:
            ...

        @property
        def is_read_only(self) -> bool:
            ...

        def __contains__(self, key: System_Collections_Generic_SortedList_TKey) -> bool:
            ...

        def __getitem__(self, index: int) -> System_Collections_Generic_SortedList_TKey:
            ...

        def __iter__(self) -> typing.Iterator[System_Collections_Generic_SortedList_TKey]:
            ...

        def __len__(self) -> int:
            ...

        def __setitem__(self, index: int, value: System_Collections_Generic_SortedList_TKey) -> None:
            ...

        def add(self, key: System_Collections_Generic_SortedList_TKey) -> None:
            ...

        def clear(self) -> None:
            ...

        def contains(self, key: System_Collections_Generic_SortedList_TKey) -> bool:
            ...

        def copy_to(self, array: typing.List[System_Collections_Generic_SortedList_TKey], array_index: int) -> None:
            ...

        def get_enumerator(self) -> System.Collections.Generic.IEnumerator[System_Collections_Generic_SortedList_TKey]:
            ...

        def index_of(self, key: System_Collections_Generic_SortedList_TKey) -> int:
            ...

        def insert(self, index: int, value: System_Collections_Generic_SortedList_TKey) -> None:
            ...

        def remove(self, key: System_Collections_Generic_SortedList_TKey) -> bool:
            ...

        def remove_at(self, index: int) -> None:
            ...

    class ValueList(System.Object, System.Collections.Generic.IList[System_Collections_Generic_SortedList_TValue], System.Collections.ICollection, typing.Iterable[System_Collections_Generic_SortedList_TValue]):
        """This class has no documentation."""

        @property
        def count(self) -> int:
            ...

        @property
        def is_read_only(self) -> bool:
            ...

        def __contains__(self, value: System_Collections_Generic_SortedList_TValue) -> bool:
            ...

        def __getitem__(self, index: int) -> System_Collections_Generic_SortedList_TValue:
            ...

        def __iter__(self) -> typing.Iterator[System_Collections_Generic_SortedList_TValue]:
            ...

        def __len__(self) -> int:
            ...

        def __setitem__(self, index: int, value: System_Collections_Generic_SortedList_TValue) -> None:
            ...

        def add(self, key: System_Collections_Generic_SortedList_TValue) -> None:
            ...

        def clear(self) -> None:
            ...

        def contains(self, value: System_Collections_Generic_SortedList_TValue) -> bool:
            ...

        def copy_to(self, array: typing.List[System_Collections_Generic_SortedList_TValue], array_index: int) -> None:
            ...

        def get_enumerator(self) -> System.Collections.Generic.IEnumerator[System_Collections_Generic_SortedList_TValue]:
            ...

        def index_of(self, value: System_Collections_Generic_SortedList_TValue) -> int:
            ...

        def insert(self, index: int, value: System_Collections_Generic_SortedList_TValue) -> None:
            ...

        def remove(self, value: System_Collections_Generic_SortedList_TValue) -> bool:
            ...

        def remove_at(self, index: int) -> None:
            ...

    @property
    def capacity(self) -> int:
        ...

    @capacity.setter
    def capacity(self, value: int) -> None:
        ...

    @property
    def comparer(self) -> System.Collections.Generic.IComparer[System_Collections_Generic_SortedList_TKey]:
        ...

    @property
    def count(self) -> int:
        ...

    @property
    def keys(self) -> typing.List[System_Collections_Generic_SortedList_TKey]:
        ...

    @property
    def values(self) -> typing.List[System_Collections_Generic_SortedList_TValue]:
        ...

    def __contains__(self, key: System_Collections_Generic_SortedList_TKey) -> bool:
        ...

    def __getitem__(self, key: System_Collections_Generic_SortedList_TKey) -> System_Collections_Generic_SortedList_TValue:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, capacity: int) -> None:
        ...

    @overload
    def __init__(self, comparer: System.Collections.Generic.IComparer[System_Collections_Generic_SortedList_TKey]) -> None:
        ...

    @overload
    def __init__(self, capacity: int, comparer: System.Collections.Generic.IComparer[System_Collections_Generic_SortedList_TKey]) -> None:
        ...

    @overload
    def __init__(self, dictionary: System.Collections.Generic.IDictionary[System_Collections_Generic_SortedList_TKey, System_Collections_Generic_SortedList_TValue]) -> None:
        ...

    @overload
    def __init__(self, dictionary: System.Collections.Generic.IDictionary[System_Collections_Generic_SortedList_TKey, System_Collections_Generic_SortedList_TValue], comparer: System.Collections.Generic.IComparer[System_Collections_Generic_SortedList_TKey]) -> None:
        ...

    def __iter__(self) -> typing.Iterator[System.Collections.Generic.KeyValuePair[System_Collections_Generic_SortedList_TKey, System_Collections_Generic_SortedList_TValue]]:
        ...

    def __len__(self) -> int:
        ...

    def __setitem__(self, key: System_Collections_Generic_SortedList_TKey, value: System_Collections_Generic_SortedList_TValue) -> None:
        ...

    def add(self, key: System_Collections_Generic_SortedList_TKey, value: System_Collections_Generic_SortedList_TValue) -> None:
        ...

    def clear(self) -> None:
        ...

    def contains_key(self, key: System_Collections_Generic_SortedList_TKey) -> bool:
        ...

    def contains_value(self, value: System_Collections_Generic_SortedList_TValue) -> bool:
        ...

    def get_enumerator(self) -> System.Collections.Generic.IEnumerator[System.Collections.Generic.KeyValuePair[System_Collections_Generic_SortedList_TKey, System_Collections_Generic_SortedList_TValue]]:
        ...

    def get_key_at_index(self, index: int) -> System_Collections_Generic_SortedList_TKey:
        """
        Gets the key corresponding to the specified index.
        
        :param index: The zero-based index of the key within the entire SortedList{TKey, TValue}.
        :returns: The key corresponding to the specified index.
        """
        ...

    def get_value_at_index(self, index: int) -> System_Collections_Generic_SortedList_TValue:
        """
        Gets the value corresponding to the specified index.
        
        :param index: The zero-based index of the value within the entire SortedList{TKey, TValue}.
        :returns: The value corresponding to the specified index.
        """
        ...

    def index_of_key(self, key: System_Collections_Generic_SortedList_TKey) -> int:
        ...

    def index_of_value(self, value: System_Collections_Generic_SortedList_TValue) -> int:
        ...

    def remove(self, key: System_Collections_Generic_SortedList_TKey) -> bool:
        ...

    def remove_at(self, index: int) -> None:
        ...

    def set_value_at_index(self, index: int, value: System_Collections_Generic_SortedList_TValue) -> None:
        """
        Updates the value corresponding to the specified index.
        
        :param index: The zero-based index of the value within the entire SortedList{TKey, TValue}.
        :param value: The value with which to replace the entry at the specified index.
        """
        ...

    def trim_excess(self) -> None:
        ...

    def try_get_value(self, key: System_Collections_Generic_SortedList_TKey, value: typing.Optional[System_Collections_Generic_SortedList_TValue]) -> typing.Tuple[bool, System_Collections_Generic_SortedList_TValue]:
        ...


class PriorityQueue(typing.Generic[System_Collections_Generic_PriorityQueue_TElement, System_Collections_Generic_PriorityQueue_TPriority], System.Object):
    """Represents a min priority queue."""

    class UnorderedItemsCollection(System.Object, System.Collections.Generic.IReadOnlyCollection[System.ValueTuple[System_Collections_Generic_PriorityQueue_TElement, System_Collections_Generic_PriorityQueue_TPriority]], System.Collections.ICollection, typing.Iterable[System.ValueTuple[System_Collections_Generic_PriorityQueue_TElement, System_Collections_Generic_PriorityQueue_TPriority]]):
        """Enumerates the contents of a PriorityQueue{TElement, TPriority}, without any ordering guarantees."""

        class Enumerator(System.Collections.Generic.IEnumerator[System.ValueTuple[System_Collections_Generic_PriorityQueue_TElement, System_Collections_Generic_PriorityQueue_TPriority]]):
            """
            Enumerates the element and priority pairs of a PriorityQueue{TElement, TPriority},
             without any ordering guarantees.
            """

            @property
            def current(self) -> System.ValueTuple[System_Collections_Generic_PriorityQueue_TElement, System_Collections_Generic_PriorityQueue_TPriority]:
                """Gets the element at the current position of the enumerator."""
                ...

            def dispose(self) -> None:
                """Releases all resources used by the Enumerator."""
                ...

            def move_next(self) -> bool:
                """
                Advances the enumerator to the next element of the UnorderedItems.
                
                :returns: true if the enumerator was successfully advanced to the next element; false if the enumerator has passed the end of the collection.
                """
                ...

        @property
        def count(self) -> int:
            ...

        def __iter__(self) -> typing.Iterator[System.ValueTuple[System_Collections_Generic_PriorityQueue_TElement, System_Collections_Generic_PriorityQueue_TPriority]]:
            ...

        def get_enumerator(self) -> System.Collections.Generic.PriorityQueue.UnorderedItemsCollection.Enumerator:
            """
            Returns an enumerator that iterates through the UnorderedItems.
            
            :returns: An Enumerator for the UnorderedItems.
            """
            ...

    @property
    def count(self) -> int:
        """Gets the number of elements contained in the PriorityQueue{TElement, TPriority}."""
        ...

    @property
    def capacity(self) -> int:
        """Gets the total numbers of elements the queue's backing storage can hold without resizing."""
        ...

    @property
    def comparer(self) -> System.Collections.Generic.IComparer[System_Collections_Generic_PriorityQueue_TPriority]:
        """Gets the priority comparer used by the PriorityQueue{TElement, TPriority}."""
        ...

    @property
    def unordered_items(self) -> System.Collections.Generic.PriorityQueue.UnorderedItemsCollection:
        """Gets a collection that enumerates the elements of the queue in an unordered manner."""
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the PriorityQueue{TElement, TPriority} class."""
        ...

    @overload
    def __init__(self, initial_capacity: int) -> None:
        """
        Initializes a new instance of the PriorityQueue{TElement, TPriority} class
         with the specified initial capacity.
        
        :param initial_capacity: Initial capacity to allocate in the underlying heap array.
        """
        ...

    @overload
    def __init__(self, comparer: System.Collections.Generic.IComparer[System_Collections_Generic_PriorityQueue_TPriority]) -> None:
        """
        Initializes a new instance of the PriorityQueue{TElement, TPriority} class
         with the specified custom priority comparer.
        
        :param comparer: Custom comparer dictating the ordering of elements.  Uses Comparer{T}.Default if the argument is null.
        """
        ...

    @overload
    def __init__(self, initial_capacity: int, comparer: System.Collections.Generic.IComparer[System_Collections_Generic_PriorityQueue_TPriority]) -> None:
        """
        Initializes a new instance of the PriorityQueue{TElement, TPriority} class
         with the specified initial capacity and custom priority comparer.
        
        :param initial_capacity: Initial capacity to allocate in the underlying heap array.
        :param comparer: Custom comparer dictating the ordering of elements.  Uses Comparer{T}.Default if the argument is null.
        """
        ...

    @overload
    def __init__(self, items: System.Collections.Generic.IEnumerable[System.ValueTuple[System_Collections_Generic_PriorityQueue_TElement, System_Collections_Generic_PriorityQueue_TPriority]]) -> None:
        """
        Initializes a new instance of the PriorityQueue{TElement, TPriority} class
         that is populated with the specified elements and priorities.
        
        :param items: The pairs of elements and priorities with which to populate the queue.
        """
        ...

    @overload
    def __init__(self, items: System.Collections.Generic.IEnumerable[System.ValueTuple[System_Collections_Generic_PriorityQueue_TElement, System_Collections_Generic_PriorityQueue_TPriority]], comparer: System.Collections.Generic.IComparer[System_Collections_Generic_PriorityQueue_TPriority]) -> None:
        """
        Initializes a new instance of the PriorityQueue{TElement, TPriority} class
         that is populated with the specified elements and priorities,
         and with the specified custom priority comparer.
        
        :param items: The pairs of elements and priorities with which to populate the queue.
        :param comparer: Custom comparer dictating the ordering of elements.  Uses Comparer{T}.Default if the argument is null.
        """
        ...

    def clear(self) -> None:
        """Removes all items from the PriorityQueue{TElement, TPriority}."""
        ...

    def dequeue(self) -> System_Collections_Generic_PriorityQueue_TElement:
        """
        Removes and returns the minimal element from the PriorityQueue{TElement, TPriority}.
        
        :returns: The minimal element of the PriorityQueue{TElement, TPriority}.
        """
        ...

    def dequeue_enqueue(self, element: System_Collections_Generic_PriorityQueue_TElement, priority: System_Collections_Generic_PriorityQueue_TPriority) -> System_Collections_Generic_PriorityQueue_TElement:
        """
        Removes the minimal element and then immediately adds the specified element with associated priority to the PriorityQueue{TElement, TPriority},
        
        :param element: The element to add to the PriorityQueue{TElement, TPriority}.
        :param priority: The priority with which to associate the new element.
        :returns: The minimal element removed before performing the enqueue operation.
        """
        ...

    def enqueue(self, element: System_Collections_Generic_PriorityQueue_TElement, priority: System_Collections_Generic_PriorityQueue_TPriority) -> None:
        """
        Adds the specified element with associated priority to the PriorityQueue{TElement, TPriority}.
        
        :param element: The element to add to the PriorityQueue{TElement, TPriority}.
        :param priority: The priority with which to associate the new element.
        """
        ...

    def enqueue_dequeue(self, element: System_Collections_Generic_PriorityQueue_TElement, priority: System_Collections_Generic_PriorityQueue_TPriority) -> System_Collections_Generic_PriorityQueue_TElement:
        """
        Adds the specified element with associated priority to the PriorityQueue{TElement, TPriority},
         and immediately removes the minimal element, returning the result.
        
        :param element: The element to add to the PriorityQueue{TElement, TPriority}.
        :param priority: The priority with which to associate the new element.
        :returns: The minimal element removed after the enqueue operation.
        """
        ...

    @overload
    def enqueue_range(self, items: System.Collections.Generic.IEnumerable[System.ValueTuple[System_Collections_Generic_PriorityQueue_TElement, System_Collections_Generic_PriorityQueue_TPriority]]) -> None:
        """
        Enqueues a sequence of element/priority pairs to the PriorityQueue{TElement, TPriority}.
        
        :param items: The pairs of elements and priorities to add to the queue.
        """
        ...

    @overload
    def enqueue_range(self, elements: System.Collections.Generic.IEnumerable[System_Collections_Generic_PriorityQueue_TElement], priority: System_Collections_Generic_PriorityQueue_TPriority) -> None:
        """
        Enqueues a sequence of elements pairs to the PriorityQueue{TElement, TPriority},
         all associated with the specified priority.
        
        :param elements: The elements to add to the queue.
        :param priority: The priority to associate with the new elements.
        """
        ...

    def ensure_capacity(self, capacity: int) -> int:
        """
        Ensures that the PriorityQueue{TElement, TPriority} can hold up to
          items without further expansion of its backing storage.
        
        :param capacity: The minimum capacity to be used.
        :returns: The current capacity of the PriorityQueue{TElement, TPriority}.
        """
        ...

    def peek(self) -> System_Collections_Generic_PriorityQueue_TElement:
        """
        Returns the minimal element from the PriorityQueue{TElement, TPriority} without removing it.
        
        :returns: The minimal element of the PriorityQueue{TElement, TPriority}.
        """
        ...

    def remove(self, element: System_Collections_Generic_PriorityQueue_TElement, removed_element: typing.Optional[System_Collections_Generic_PriorityQueue_TElement], priority: typing.Optional[System_Collections_Generic_PriorityQueue_TPriority], equality_comparer: System.Collections.Generic.IEqualityComparer[System_Collections_Generic_PriorityQueue_TElement] = None) -> typing.Tuple[bool, System_Collections_Generic_PriorityQueue_TElement, System_Collections_Generic_PriorityQueue_TPriority]:
        """
        Removes the first occurrence that equals the specified parameter.
        
        :param element: The element to try to remove.
        :param removed_element: The actual element that got removed from the queue.
        :param priority: The priority value associated with the removed element.
        :param equality_comparer: The equality comparer governing element equality.
        :returns: true if matching entry was found and removed, false otherwise.
        """
        ...

    def trim_excess(self) -> None:
        """
        Sets the capacity to the actual number of items in the PriorityQueue{TElement, TPriority},
         if that is less than 90 percent of current capacity.
        """
        ...

    def try_dequeue(self, element: typing.Optional[System_Collections_Generic_PriorityQueue_TElement], priority: typing.Optional[System_Collections_Generic_PriorityQueue_TPriority]) -> typing.Tuple[bool, System_Collections_Generic_PriorityQueue_TElement, System_Collections_Generic_PriorityQueue_TPriority]:
        """
        Removes the minimal element from the PriorityQueue{TElement, TPriority},
         and copies it to the  parameter,
         and its associated priority to the  parameter.
        
        :param element: The removed element.
        :param priority: The priority associated with the removed element.
        :returns: true if the element is successfully removed;  false if the PriorityQueue{TElement, TPriority} is empty.
        """
        ...

    def try_peek(self, element: typing.Optional[System_Collections_Generic_PriorityQueue_TElement], priority: typing.Optional[System_Collections_Generic_PriorityQueue_TPriority]) -> typing.Tuple[bool, System_Collections_Generic_PriorityQueue_TElement, System_Collections_Generic_PriorityQueue_TPriority]:
        """
        Returns a value that indicates whether there is a minimal element in the PriorityQueue{TElement, TPriority},
         and if one is present, copies it to the  parameter,
         and its associated priority to the  parameter.
         The element is not removed from the PriorityQueue{TElement, TPriority}.
        
        :param element: The minimal element in the queue.
        :param priority: The priority associated with the minimal element.
        :returns: true if there is a minimal element;  false if the PriorityQueue{TElement, TPriority} is empty.
        """
        ...


class SortedDictionary(typing.Generic[System_Collections_Generic_SortedDictionary_TKey, System_Collections_Generic_SortedDictionary_TValue], System.Object, System.Collections.Generic.IDictionary[System_Collections_Generic_SortedDictionary_TKey, System_Collections_Generic_SortedDictionary_TValue], System.Collections.IDictionary, System.Collections.Generic.IReadOnlyDictionary[System_Collections_Generic_SortedDictionary_TKey, System_Collections_Generic_SortedDictionary_TValue], typing.Iterable[System.Collections.Generic.KeyValuePair[System_Collections_Generic_SortedDictionary_TKey, System_Collections_Generic_SortedDictionary_TValue]]):
    """This class has no documentation."""

    class Enumerator(System.Collections.Generic.IEnumerator[System.Collections.Generic.KeyValuePair[System_Collections_Generic_SortedDictionary_TKey, System_Collections_Generic_SortedDictionary_TValue]], System.Collections.IDictionaryEnumerator):
        """This class has no documentation."""

        @property
        def current(self) -> System.Collections.Generic.KeyValuePair[System_Collections_Generic_SortedDictionary_TKey, System_Collections_Generic_SortedDictionary_TValue]:
            ...

        def dispose(self) -> None:
            ...

        def move_next(self) -> bool:
            ...

    class KeyCollection(System.Object, System.Collections.Generic.ICollection[System_Collections_Generic_SortedDictionary_TKey], System.Collections.ICollection, System.Collections.Generic.IReadOnlyCollection[System_Collections_Generic_SortedDictionary_TKey], typing.Iterable[System_Collections_Generic_SortedDictionary_TKey]):
        """This class has no documentation."""

        class Enumerator(System.Collections.Generic.IEnumerator[System_Collections_Generic_SortedDictionary_TKey]):
            """This class has no documentation."""

            @property
            def current(self) -> System_Collections_Generic_SortedDictionary_TKey:
                ...

            def dispose(self) -> None:
                ...

            def move_next(self) -> bool:
                ...

        @property
        def count(self) -> int:
            ...

        def __contains__(self, item: System_Collections_Generic_SortedDictionary_TKey) -> bool:
            ...

        def __init__(self, dictionary: System.Collections.Generic.SortedDictionary[System_Collections_Generic_SortedDictionary_TKey, System_Collections_Generic_SortedDictionary_TValue]) -> None:
            ...

        def __iter__(self) -> typing.Iterator[System_Collections_Generic_SortedDictionary_TKey]:
            ...

        def __len__(self) -> int:
            ...

        def contains(self, item: System_Collections_Generic_SortedDictionary_TKey) -> bool:
            ...

        def copy_to(self, array: typing.List[System_Collections_Generic_SortedDictionary_TKey], index: int) -> None:
            ...

        def get_enumerator(self) -> System.Collections.Generic.SortedDictionary.KeyCollection.Enumerator:
            ...

    class ValueCollection(System.Object, System.Collections.Generic.ICollection[System_Collections_Generic_SortedDictionary_TValue], System.Collections.ICollection, System.Collections.Generic.IReadOnlyCollection[System_Collections_Generic_SortedDictionary_TValue], typing.Iterable[System_Collections_Generic_SortedDictionary_TValue]):
        """This class has no documentation."""

        class Enumerator(System.Collections.Generic.IEnumerator[System_Collections_Generic_SortedDictionary_TValue]):
            """This class has no documentation."""

            @property
            def current(self) -> System_Collections_Generic_SortedDictionary_TValue:
                ...

            def dispose(self) -> None:
                ...

            def move_next(self) -> bool:
                ...

        @property
        def count(self) -> int:
            ...

        def __init__(self, dictionary: System.Collections.Generic.SortedDictionary[System_Collections_Generic_SortedDictionary_TKey, System_Collections_Generic_SortedDictionary_TValue]) -> None:
            ...

        def __iter__(self) -> typing.Iterator[System_Collections_Generic_SortedDictionary_TValue]:
            ...

        def __len__(self) -> int:
            ...

        def copy_to(self, array: typing.List[System_Collections_Generic_SortedDictionary_TValue], index: int) -> None:
            ...

        def get_enumerator(self) -> System.Collections.Generic.SortedDictionary.ValueCollection.Enumerator:
            ...

    class KeyValuePairComparer(System.Collections.Generic.Comparer[System.Collections.Generic.KeyValuePair[System_Collections_Generic_SortedDictionary_TKey, System_Collections_Generic_SortedDictionary_TValue]]):
        """This class has no documentation."""

        def __init__(self, key_comparer: System.Collections.Generic.IComparer[System_Collections_Generic_SortedDictionary_TKey]) -> None:
            ...

        def compare(self, x: System.Collections.Generic.KeyValuePair[System_Collections_Generic_SortedDictionary_TKey, System_Collections_Generic_SortedDictionary_TValue], y: System.Collections.Generic.KeyValuePair[System_Collections_Generic_SortedDictionary_TKey, System_Collections_Generic_SortedDictionary_TValue]) -> int:
            ...

        def equals(self, obj: typing.Any) -> bool:
            ...

        def get_hash_code(self) -> int:
            ...

    @property
    def count(self) -> int:
        ...

    @property
    def comparer(self) -> System.Collections.Generic.IComparer[System_Collections_Generic_SortedDictionary_TKey]:
        ...

    @property
    def keys(self) -> System.Collections.Generic.SortedDictionary.KeyCollection:
        ...

    @property
    def values(self) -> System.Collections.Generic.SortedDictionary.ValueCollection:
        ...

    def __contains__(self, key: System_Collections_Generic_SortedDictionary_TKey) -> bool:
        ...

    def __getitem__(self, key: System_Collections_Generic_SortedDictionary_TKey) -> System_Collections_Generic_SortedDictionary_TValue:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, dictionary: System.Collections.Generic.IDictionary[System_Collections_Generic_SortedDictionary_TKey, System_Collections_Generic_SortedDictionary_TValue]) -> None:
        ...

    @overload
    def __init__(self, dictionary: System.Collections.Generic.IDictionary[System_Collections_Generic_SortedDictionary_TKey, System_Collections_Generic_SortedDictionary_TValue], comparer: System.Collections.Generic.IComparer[System_Collections_Generic_SortedDictionary_TKey]) -> None:
        ...

    @overload
    def __init__(self, comparer: System.Collections.Generic.IComparer[System_Collections_Generic_SortedDictionary_TKey]) -> None:
        ...

    def __iter__(self) -> typing.Iterator[System.Collections.Generic.KeyValuePair[System_Collections_Generic_SortedDictionary_TKey, System_Collections_Generic_SortedDictionary_TValue]]:
        ...

    def __len__(self) -> int:
        ...

    def __setitem__(self, key: System_Collections_Generic_SortedDictionary_TKey, value: System_Collections_Generic_SortedDictionary_TValue) -> None:
        ...

    def add(self, key: System_Collections_Generic_SortedDictionary_TKey, value: System_Collections_Generic_SortedDictionary_TValue) -> None:
        ...

    def clear(self) -> None:
        ...

    def contains_key(self, key: System_Collections_Generic_SortedDictionary_TKey) -> bool:
        ...

    def contains_value(self, value: System_Collections_Generic_SortedDictionary_TValue) -> bool:
        ...

    def copy_to(self, array: typing.List[System.Collections.Generic.KeyValuePair[System_Collections_Generic_SortedDictionary_TKey, System_Collections_Generic_SortedDictionary_TValue]], index: int) -> None:
        ...

    def get_enumerator(self) -> System.Collections.Generic.SortedDictionary.Enumerator:
        ...

    def remove(self, key: System_Collections_Generic_SortedDictionary_TKey) -> bool:
        ...

    def try_get_value(self, key: System_Collections_Generic_SortedDictionary_TKey, value: typing.Optional[System_Collections_Generic_SortedDictionary_TValue]) -> typing.Tuple[bool, System_Collections_Generic_SortedDictionary_TValue]:
        ...


class TreeSet(typing.Generic[System_Collections_Generic_TreeSet_T], System.Collections.Generic.SortedSet[System_Collections_Generic_TreeSet_T]):
    """
    This class is intended as a helper for backwards compatibility with existing SortedDictionaries.
    TreeSet has been converted into SortedSet{T}, which will be exposed publicly. SortedDictionaries
    have the problem where they have already been serialized to disk as having a backing class named
    TreeSet. To ensure that we can read back anything that has already been written to disk, we need to
    make sure that we have a class named TreeSet that does everything the way it used to.
    
    The only thing that makes it different from SortedSet is that it throws on duplicates
    """

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, comparer: System.Collections.Generic.IComparer[System_Collections_Generic_TreeSet_T]) -> None:
        ...


class LinkedList(typing.Generic[System_Collections_Generic_LinkedList_T], System.Object, System.Collections.Generic.ICollection[System_Collections_Generic_LinkedList_T], System.Collections.ICollection, System.Collections.Generic.IReadOnlyCollection[System_Collections_Generic_LinkedList_T], System.Runtime.Serialization.ISerializable, System.Runtime.Serialization.IDeserializationCallback, typing.Iterable[System_Collections_Generic_LinkedList_T]):
    """This class has no documentation."""

    class Enumerator(System.Collections.Generic.IEnumerator[System_Collections_Generic_LinkedList_T], System.Runtime.Serialization.ISerializable, System.Runtime.Serialization.IDeserializationCallback):
        """This class has no documentation."""

        @property
        def current(self) -> System_Collections_Generic_LinkedList_T:
            ...

        def dispose(self) -> None:
            ...

        def move_next(self) -> bool:
            ...

    @property
    def count(self) -> int:
        ...

    @property
    def first(self) -> System.Collections.Generic.LinkedListNode[System_Collections_Generic_LinkedList_T]:
        ...

    @property
    def last(self) -> System.Collections.Generic.LinkedListNode[System_Collections_Generic_LinkedList_T]:
        ...

    def __contains__(self, value: System_Collections_Generic_LinkedList_T) -> bool:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, collection: System.Collections.Generic.IEnumerable[System_Collections_Generic_LinkedList_T]) -> None:
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """
        This method is protected.
        
        Obsoletions.LegacyFormatterImplMessage
        """
        ...

    def __iter__(self) -> typing.Iterator[System_Collections_Generic_LinkedList_T]:
        ...

    def __len__(self) -> int:
        ...

    @overload
    def add_after(self, node: System.Collections.Generic.LinkedListNode[System_Collections_Generic_LinkedList_T], value: System_Collections_Generic_LinkedList_T) -> System.Collections.Generic.LinkedListNode[System_Collections_Generic_LinkedList_T]:
        ...

    @overload
    def add_after(self, node: System.Collections.Generic.LinkedListNode[System_Collections_Generic_LinkedList_T], new_node: System.Collections.Generic.LinkedListNode[System_Collections_Generic_LinkedList_T]) -> None:
        ...

    @overload
    def add_before(self, node: System.Collections.Generic.LinkedListNode[System_Collections_Generic_LinkedList_T], value: System_Collections_Generic_LinkedList_T) -> System.Collections.Generic.LinkedListNode[System_Collections_Generic_LinkedList_T]:
        ...

    @overload
    def add_before(self, node: System.Collections.Generic.LinkedListNode[System_Collections_Generic_LinkedList_T], new_node: System.Collections.Generic.LinkedListNode[System_Collections_Generic_LinkedList_T]) -> None:
        ...

    @overload
    def add_first(self, value: System_Collections_Generic_LinkedList_T) -> System.Collections.Generic.LinkedListNode[System_Collections_Generic_LinkedList_T]:
        ...

    @overload
    def add_first(self, node: System.Collections.Generic.LinkedListNode[System_Collections_Generic_LinkedList_T]) -> None:
        ...

    @overload
    def add_last(self, value: System_Collections_Generic_LinkedList_T) -> System.Collections.Generic.LinkedListNode[System_Collections_Generic_LinkedList_T]:
        ...

    @overload
    def add_last(self, node: System.Collections.Generic.LinkedListNode[System_Collections_Generic_LinkedList_T]) -> None:
        ...

    def clear(self) -> None:
        ...

    def contains(self, value: System_Collections_Generic_LinkedList_T) -> bool:
        ...

    def copy_to(self, array: typing.List[System_Collections_Generic_LinkedList_T], index: int) -> None:
        ...

    def find(self, value: System_Collections_Generic_LinkedList_T) -> System.Collections.Generic.LinkedListNode[System_Collections_Generic_LinkedList_T]:
        ...

    def find_last(self, value: System_Collections_Generic_LinkedList_T) -> System.Collections.Generic.LinkedListNode[System_Collections_Generic_LinkedList_T]:
        ...

    def get_enumerator(self) -> System.Collections.Generic.LinkedList.Enumerator:
        ...

    def get_object_data(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """Obsoletions.LegacyFormatterImplMessage"""
        warnings.warn("Obsoletions.LegacyFormatterImplMessage", DeprecationWarning)

    def on_deserialization(self, sender: typing.Any) -> None:
        ...

    @overload
    def remove(self, value: System_Collections_Generic_LinkedList_T) -> bool:
        ...

    @overload
    def remove(self, node: System.Collections.Generic.LinkedListNode[System_Collections_Generic_LinkedList_T]) -> None:
        ...

    def remove_first(self) -> None:
        ...

    def remove_last(self) -> None:
        ...


class LinkedListNode(typing.Generic[System_Collections_Generic_LinkedListNode_T], System.Object):
    """This class has no documentation."""

    @property
    def list(self) -> System.Collections.Generic.LinkedList[System_Collections_Generic_LinkedListNode_T]:
        ...

    @property
    def next(self) -> System.Collections.Generic.LinkedListNode[System_Collections_Generic_LinkedListNode_T]:
        ...

    @property
    def previous(self) -> System.Collections.Generic.LinkedListNode[System_Collections_Generic_LinkedListNode_T]:
        ...

    @property
    def value(self) -> System_Collections_Generic_LinkedListNode_T:
        ...

    @value.setter
    def value(self, value: System_Collections_Generic_LinkedListNode_T) -> None:
        ...

    @property
    def value_ref(self) -> typing.Any:
        """Gets a reference to the value held by the node."""
        ...

    def __init__(self, value: System_Collections_Generic_LinkedListNode_T) -> None:
        ...


class Stack(typing.Generic[System_Collections_Generic_Stack_T], System.Object, System.Collections.ICollection, System.Collections.Generic.IReadOnlyCollection[System_Collections_Generic_Stack_T], typing.Iterable[System_Collections_Generic_Stack_T]):
    """This class has no documentation."""

    class Enumerator(System.Collections.Generic.IEnumerator[System_Collections_Generic_Stack_T]):
        """This class has no documentation."""

        @property
        def current(self) -> System_Collections_Generic_Stack_T:
            ...

        def dispose(self) -> None:
            ...

        def move_next(self) -> bool:
            ...

    @property
    def count(self) -> int:
        ...

    @property
    def capacity(self) -> int:
        """Gets the total numbers of elements the internal data structure can hold without resizing."""
        ...

    def __contains__(self, item: System_Collections_Generic_Stack_T) -> bool:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, capacity: int) -> None:
        ...

    @overload
    def __init__(self, collection: System.Collections.Generic.IEnumerable[System_Collections_Generic_Stack_T]) -> None:
        ...

    def __iter__(self) -> typing.Iterator[System_Collections_Generic_Stack_T]:
        ...

    def __len__(self) -> int:
        ...

    def clear(self) -> None:
        ...

    def contains(self, item: System_Collections_Generic_Stack_T) -> bool:
        ...

    def copy_to(self, array: typing.List[System_Collections_Generic_Stack_T], array_index: int) -> None:
        ...

    def ensure_capacity(self, capacity: int) -> int:
        """
        Ensures that the capacity of this Stack is at least the specified .
        If the current capacity of the Stack is less than specified ,
        the capacity is increased by continuously twice current capacity until it is at least the specified .
        
        :param capacity: The minimum capacity to ensure.
        :returns: The new capacity of this stack.
        """
        ...

    def get_enumerator(self) -> System.Collections.Generic.Stack.Enumerator:
        ...

    def peek(self) -> System_Collections_Generic_Stack_T:
        ...

    def pop(self) -> System_Collections_Generic_Stack_T:
        ...

    def push(self, item: System_Collections_Generic_Stack_T) -> None:
        ...

    def to_array(self) -> typing.List[System_Collections_Generic_Stack_T]:
        ...

    @overload
    def trim_excess(self) -> None:
        ...

    @overload
    def trim_excess(self, capacity: int) -> None:
        """
        Sets the capacity of a Stack{T} object to a specified number of entries.
        
        :param capacity: The new capacity.
        """
        ...

    def try_peek(self, result: typing.Optional[System_Collections_Generic_Stack_T]) -> typing.Tuple[bool, System_Collections_Generic_Stack_T]:
        ...

    def try_pop(self, result: typing.Optional[System_Collections_Generic_Stack_T]) -> typing.Tuple[bool, System_Collections_Generic_Stack_T]:
        ...


