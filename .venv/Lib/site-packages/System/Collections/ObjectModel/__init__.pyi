from typing import overload
from enum import Enum
import abc
import typing

import System
import System.Collections
import System.Collections.Generic
import System.Collections.ObjectModel
import System.Collections.Specialized
import System.ComponentModel

System_Collections_ObjectModel_ReadOnlySet_T = typing.TypeVar("System_Collections_ObjectModel_ReadOnlySet_T")
System_Collections_ObjectModel_ReadOnlyCollection_T = typing.TypeVar("System_Collections_ObjectModel_ReadOnlyCollection_T")
System_Collections_ObjectModel_Collection_T = typing.TypeVar("System_Collections_ObjectModel_Collection_T")
System_Collections_ObjectModel_ReadOnlyDictionary_TKey = typing.TypeVar("System_Collections_ObjectModel_ReadOnlyDictionary_TKey")
System_Collections_ObjectModel_ReadOnlyDictionary_TValue = typing.TypeVar("System_Collections_ObjectModel_ReadOnlyDictionary_TValue")
System_Collections_ObjectModel_KeyedCollection_TItem = typing.TypeVar("System_Collections_ObjectModel_KeyedCollection_TItem")
System_Collections_ObjectModel_KeyedCollection_TKey = typing.TypeVar("System_Collections_ObjectModel_KeyedCollection_TKey")
System_Collections_ObjectModel_ObservableCollection_T = typing.TypeVar("System_Collections_ObjectModel_ObservableCollection_T")
System_Collections_ObjectModel_ReadOnlyObservableCollection_T = typing.TypeVar("System_Collections_ObjectModel_ReadOnlyObservableCollection_T")
System_Collections_ObjectModel__EventContainer_Callable = typing.TypeVar("System_Collections_ObjectModel__EventContainer_Callable")
System_Collections_ObjectModel__EventContainer_ReturnType = typing.TypeVar("System_Collections_ObjectModel__EventContainer_ReturnType")


class ReadOnlySet(typing.Generic[System_Collections_ObjectModel_ReadOnlySet_T], System.Object, System.Collections.Generic.IReadOnlySet[System_Collections_ObjectModel_ReadOnlySet_T], System.Collections.Generic.ISet[System_Collections_ObjectModel_ReadOnlySet_T], System.Collections.ICollection, typing.Iterable[System_Collections_ObjectModel_ReadOnlySet_T]):
    """Represents a read-only, generic set of values."""

    EMPTY: System.Collections.ObjectModel.ReadOnlySet[System_Collections_ObjectModel_ReadOnlySet_T]
    """Gets an empty ReadOnlySet{T}."""

    @property
    def set(self) -> System.Collections.Generic.ISet[System_Collections_ObjectModel_ReadOnlySet_T]:
        """
        Gets the set that is wrapped by this ReadOnlySet{T} object.
        
        This property is protected.
        """
        ...

    @property
    def count(self) -> int:
        ...

    def __init__(self, set: System.Collections.Generic.ISet[System_Collections_ObjectModel_ReadOnlySet_T]) -> None:
        """
        Initializes a new instance of the ReadOnlySet{T} class that is a wrapper around the specified set.
        
        :param set: The set to wrap.
        """
        ...

    def __iter__(self) -> typing.Iterator[System_Collections_ObjectModel_ReadOnlySet_T]:
        ...

    def contains(self, item: System_Collections_ObjectModel_ReadOnlySet_T) -> bool:
        ...

    def get_enumerator(self) -> System.Collections.Generic.IEnumerator[System_Collections_ObjectModel_ReadOnlySet_T]:
        ...

    def is_proper_subset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_ObjectModel_ReadOnlySet_T]) -> bool:
        ...

    def is_proper_superset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_ObjectModel_ReadOnlySet_T]) -> bool:
        ...

    def is_subset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_ObjectModel_ReadOnlySet_T]) -> bool:
        ...

    def is_superset_of(self, other: System.Collections.Generic.IEnumerable[System_Collections_ObjectModel_ReadOnlySet_T]) -> bool:
        ...

    def overlaps(self, other: System.Collections.Generic.IEnumerable[System_Collections_ObjectModel_ReadOnlySet_T]) -> bool:
        ...

    def set_equals(self, other: System.Collections.Generic.IEnumerable[System_Collections_ObjectModel_ReadOnlySet_T]) -> bool:
        ...


class ReadOnlyCollection(typing.Generic[System_Collections_ObjectModel_ReadOnlyCollection_T], System.Object, System.Collections.Generic.IList[System_Collections_ObjectModel_ReadOnlyCollection_T], System.Collections.IList, System.Collections.Generic.IReadOnlyList[System_Collections_ObjectModel_ReadOnlyCollection_T], typing.Iterable[System_Collections_ObjectModel_ReadOnlyCollection_T]):
    """Provides static methods for read-only collections."""

    EMPTY: System.Collections.ObjectModel.ReadOnlyCollection[System_Collections_ObjectModel_ReadOnlyCollection_T]
    """Gets an empty ReadOnlyCollection{T}."""

    @property
    def count(self) -> int:
        ...

    @property
    def items(self) -> typing.List[System_Collections_ObjectModel_ReadOnlyCollection_T]:
        """This property is protected."""
        ...

    def __getitem__(self, index: int) -> System_Collections_ObjectModel_ReadOnlyCollection_T:
        ...

    def __init__(self, list: System.Collections.Generic.IList[System_Collections_ObjectModel_ReadOnlyCollection_T]) -> None:
        ...

    def __iter__(self) -> typing.Iterator[System_Collections_ObjectModel_ReadOnlyCollection_T]:
        ...

    def contains(self, value: System_Collections_ObjectModel_ReadOnlyCollection_T) -> bool:
        ...

    def copy_to(self, array: typing.List[System_Collections_ObjectModel_ReadOnlyCollection_T], index: int) -> None:
        ...

    def get_enumerator(self) -> System.Collections.Generic.IEnumerator[System_Collections_ObjectModel_ReadOnlyCollection_T]:
        ...

    def index_of(self, value: System_Collections_ObjectModel_ReadOnlyCollection_T) -> int:
        ...


class Collection(typing.Generic[System_Collections_ObjectModel_Collection_T], System.Object, System.Collections.Generic.IList[System_Collections_ObjectModel_Collection_T], System.Collections.IList, System.Collections.Generic.IReadOnlyList[System_Collections_ObjectModel_Collection_T], typing.Iterable[System_Collections_ObjectModel_Collection_T]):
    """This class has no documentation."""

    @property
    def count(self) -> int:
        ...

    @property
    def items(self) -> typing.List[System_Collections_ObjectModel_Collection_T]:
        """This property is protected."""
        ...

    def __getitem__(self, index: int) -> System_Collections_ObjectModel_Collection_T:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, list: System.Collections.Generic.IList[System_Collections_ObjectModel_Collection_T]) -> None:
        ...

    def __iter__(self) -> typing.Iterator[System_Collections_ObjectModel_Collection_T]:
        ...

    def __setitem__(self, index: int, value: System_Collections_ObjectModel_Collection_T) -> None:
        ...

    def add(self, item: System_Collections_ObjectModel_Collection_T) -> None:
        ...

    def clear(self) -> None:
        ...

    def clear_items(self) -> None:
        """This method is protected."""
        ...

    def contains(self, item: System_Collections_ObjectModel_Collection_T) -> bool:
        ...

    def copy_to(self, array: typing.List[System_Collections_ObjectModel_Collection_T], index: int) -> None:
        ...

    def get_enumerator(self) -> System.Collections.Generic.IEnumerator[System_Collections_ObjectModel_Collection_T]:
        ...

    def index_of(self, item: System_Collections_ObjectModel_Collection_T) -> int:
        ...

    def insert(self, index: int, item: System_Collections_ObjectModel_Collection_T) -> None:
        ...

    def insert_item(self, index: int, item: System_Collections_ObjectModel_Collection_T) -> None:
        """This method is protected."""
        ...

    def remove(self, item: System_Collections_ObjectModel_Collection_T) -> bool:
        ...

    def remove_at(self, index: int) -> None:
        ...

    def remove_item(self, index: int) -> None:
        """This method is protected."""
        ...

    def set_item(self, index: int, item: System_Collections_ObjectModel_Collection_T) -> None:
        """This method is protected."""
        ...


class ReadOnlyDictionary(typing.Generic[System_Collections_ObjectModel_ReadOnlyDictionary_TKey, System_Collections_ObjectModel_ReadOnlyDictionary_TValue], System.Object, System.Collections.Generic.IDictionary[System_Collections_ObjectModel_ReadOnlyDictionary_TKey, System_Collections_ObjectModel_ReadOnlyDictionary_TValue], System.Collections.IDictionary, System.Collections.Generic.IReadOnlyDictionary[System_Collections_ObjectModel_ReadOnlyDictionary_TKey, System_Collections_ObjectModel_ReadOnlyDictionary_TValue], typing.Iterable[System.Collections.Generic.KeyValuePair[System_Collections_ObjectModel_ReadOnlyDictionary_TKey, System_Collections_ObjectModel_ReadOnlyDictionary_TValue]]):
    """This class has no documentation."""

    class KeyCollection(System.Object, System.Collections.Generic.ICollection[System_Collections_ObjectModel_ReadOnlyDictionary_TKey], System.Collections.ICollection, System.Collections.Generic.IReadOnlyCollection[System_Collections_ObjectModel_ReadOnlyDictionary_TKey], typing.Iterable[System_Collections_ObjectModel_ReadOnlyDictionary_TKey]):
        """This class has no documentation."""

        @property
        def count(self) -> int:
            ...

        def __iter__(self) -> typing.Iterator[System_Collections_ObjectModel_ReadOnlyDictionary_TKey]:
            ...

        def contains(self, item: System_Collections_ObjectModel_ReadOnlyDictionary_TKey) -> bool:
            ...

        def copy_to(self, array: typing.List[System_Collections_ObjectModel_ReadOnlyDictionary_TKey], array_index: int) -> None:
            ...

        def get_enumerator(self) -> System.Collections.Generic.IEnumerator[System_Collections_ObjectModel_ReadOnlyDictionary_TKey]:
            ...

    class ValueCollection(System.Object, System.Collections.Generic.ICollection[System_Collections_ObjectModel_ReadOnlyDictionary_TValue], System.Collections.ICollection, System.Collections.Generic.IReadOnlyCollection[System_Collections_ObjectModel_ReadOnlyDictionary_TValue], typing.Iterable[System_Collections_ObjectModel_ReadOnlyDictionary_TValue]):
        """This class has no documentation."""

        @property
        def count(self) -> int:
            ...

        def __iter__(self) -> typing.Iterator[System_Collections_ObjectModel_ReadOnlyDictionary_TValue]:
            ...

        def copy_to(self, array: typing.List[System_Collections_ObjectModel_ReadOnlyDictionary_TValue], array_index: int) -> None:
            ...

        def get_enumerator(self) -> System.Collections.Generic.IEnumerator[System_Collections_ObjectModel_ReadOnlyDictionary_TValue]:
            ...

    EMPTY: System.Collections.ObjectModel.ReadOnlyDictionary[System_Collections_ObjectModel_ReadOnlyDictionary_TKey, System_Collections_ObjectModel_ReadOnlyDictionary_TValue]
    """Gets an empty ReadOnlyDictionary{TKey, TValue}."""

    @property
    def dictionary(self) -> System.Collections.Generic.IDictionary[System_Collections_ObjectModel_ReadOnlyDictionary_TKey, System_Collections_ObjectModel_ReadOnlyDictionary_TValue]:
        """This property is protected."""
        ...

    @property
    def keys(self) -> System.Collections.ObjectModel.ReadOnlyDictionary.KeyCollection:
        ...

    @property
    def values(self) -> System.Collections.ObjectModel.ReadOnlyDictionary.ValueCollection:
        ...

    @property
    def count(self) -> int:
        ...

    def __contains__(self, key: System_Collections_ObjectModel_ReadOnlyDictionary_TKey) -> bool:
        ...

    def __getitem__(self, key: System_Collections_ObjectModel_ReadOnlyDictionary_TKey) -> System_Collections_ObjectModel_ReadOnlyDictionary_TValue:
        ...

    def __init__(self, dictionary: System.Collections.Generic.IDictionary[System_Collections_ObjectModel_ReadOnlyDictionary_TKey, System_Collections_ObjectModel_ReadOnlyDictionary_TValue]) -> None:
        ...

    def __iter__(self) -> typing.Iterator[System.Collections.Generic.KeyValuePair[System_Collections_ObjectModel_ReadOnlyDictionary_TKey, System_Collections_ObjectModel_ReadOnlyDictionary_TValue]]:
        ...

    def __len__(self) -> int:
        ...

    def contains_key(self, key: System_Collections_ObjectModel_ReadOnlyDictionary_TKey) -> bool:
        ...

    def get_enumerator(self) -> System.Collections.Generic.IEnumerator[System.Collections.Generic.KeyValuePair[System_Collections_ObjectModel_ReadOnlyDictionary_TKey, System_Collections_ObjectModel_ReadOnlyDictionary_TValue]]:
        ...

    def try_get_value(self, key: System_Collections_ObjectModel_ReadOnlyDictionary_TKey, value: typing.Optional[System_Collections_ObjectModel_ReadOnlyDictionary_TValue]) -> typing.Tuple[bool, System_Collections_ObjectModel_ReadOnlyDictionary_TValue]:
        ...


class KeyedCollection(typing.Generic[System_Collections_ObjectModel_KeyedCollection_TKey, System_Collections_ObjectModel_KeyedCollection_TItem], System.Collections.ObjectModel.Collection[System_Collections_ObjectModel_KeyedCollection_TItem], metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    def comparer(self) -> System.Collections.Generic.IEqualityComparer[System_Collections_ObjectModel_KeyedCollection_TKey]:
        ...

    @property
    def dictionary(self) -> System.Collections.Generic.IDictionary[System_Collections_ObjectModel_KeyedCollection_TKey, System_Collections_ObjectModel_KeyedCollection_TItem]:
        """This property is protected."""
        ...

    def __getitem__(self, key: System_Collections_ObjectModel_KeyedCollection_TKey) -> System_Collections_ObjectModel_KeyedCollection_TItem:
        ...

    @overload
    def __init__(self) -> None:
        """This method is protected."""
        ...

    @overload
    def __init__(self, comparer: System.Collections.Generic.IEqualityComparer[System_Collections_ObjectModel_KeyedCollection_TKey]) -> None:
        """This method is protected."""
        ...

    @overload
    def __init__(self, comparer: System.Collections.Generic.IEqualityComparer[System_Collections_ObjectModel_KeyedCollection_TKey], dictionary_creation_threshold: int) -> None:
        """This method is protected."""
        ...

    def change_item_key(self, item: System_Collections_ObjectModel_KeyedCollection_TItem, new_key: System_Collections_ObjectModel_KeyedCollection_TKey) -> None:
        """This method is protected."""
        ...

    def clear_items(self) -> None:
        """This method is protected."""
        ...

    def contains(self, key: System_Collections_ObjectModel_KeyedCollection_TKey) -> bool:
        ...

    def get_key_for_item(self, item: System_Collections_ObjectModel_KeyedCollection_TItem) -> System_Collections_ObjectModel_KeyedCollection_TKey:
        """This method is protected."""
        ...

    def insert_item(self, index: int, item: System_Collections_ObjectModel_KeyedCollection_TItem) -> None:
        """This method is protected."""
        ...

    def remove(self, key: System_Collections_ObjectModel_KeyedCollection_TKey) -> bool:
        ...

    def remove_item(self, index: int) -> None:
        """This method is protected."""
        ...

    def set_item(self, index: int, item: System_Collections_ObjectModel_KeyedCollection_TItem) -> None:
        """This method is protected."""
        ...

    def try_get_value(self, key: System_Collections_ObjectModel_KeyedCollection_TKey, item: typing.Optional[System_Collections_ObjectModel_KeyedCollection_TItem]) -> typing.Tuple[bool, System_Collections_ObjectModel_KeyedCollection_TItem]:
        ...


class ObservableCollection(typing.Generic[System_Collections_ObjectModel_ObservableCollection_T], System.Collections.ObjectModel.Collection[System_Collections_ObjectModel_ObservableCollection_T], System.Collections.Specialized.INotifyCollectionChanged, System.ComponentModel.INotifyPropertyChanged):
    """
    Implementation of a dynamic data collection based on generic Collection<T>,
    implementing INotifyCollectionChanged to notify listeners
    when items get added, removed or the whole list is refreshed.
    """

    @property
    def collection_changed(self) -> _EventContainer[typing.Callable[[System.Object, System.Collections.Specialized.NotifyCollectionChangedEventArgs], None], None]:
        """Occurs when the collection changes, either by adding or removing an item."""
        ...

    @collection_changed.setter
    def collection_changed(self, value: _EventContainer[typing.Callable[[System.Object, System.Collections.Specialized.NotifyCollectionChangedEventArgs], None], None]) -> None:
        ...

    @property
    def property_changed(self) -> _EventContainer[typing.Callable[[System.Object, System.ComponentModel.PropertyChangedEventArgs], None], None]:
        """
        PropertyChanged event (per INotifyPropertyChanged).
        
        This field is protected.
        """
        ...

    @property_changed.setter
    def property_changed(self, value: _EventContainer[typing.Callable[[System.Object, System.ComponentModel.PropertyChangedEventArgs], None], None]) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of ObservableCollection that is empty and has default initial capacity."""
        ...

    @overload
    def __init__(self, collection: System.Collections.Generic.IEnumerable[System_Collections_ObjectModel_ObservableCollection_T]) -> None:
        """
        Initializes a new instance of the ObservableCollection class that contains
        elements copied from the specified collection and has sufficient capacity
        to accommodate the number of elements copied.
        
        :param collection: The collection whose elements are copied to the new list.
        """
        ...

    @overload
    def __init__(self, list: System.Collections.Generic.List[System_Collections_ObjectModel_ObservableCollection_T]) -> None:
        """
        Initializes a new instance of the ObservableCollection class
        that contains elements copied from the specified list
        
        :param list: The list whose elements are copied to the new list.
        """
        ...

    def block_reentrancy(self) -> System.IDisposable:
        """
        Disallow reentrant attempts to change this collection. E.g. an event handler
        of the CollectionChanged event is not allowed to make changes to this collection.
        
        This method is protected.
        """
        ...

    def check_reentrancy(self) -> None:
        """
        Check and assert for reentrant attempts to change this collection.
        
        This method is protected.
        """
        ...

    def clear_items(self) -> None:
        """
        Called by base class Collection<T> when the list is being cleared;
        raises a CollectionChanged event to any listeners.
        
        This method is protected.
        """
        ...

    def insert_item(self, index: int, item: System_Collections_ObjectModel_ObservableCollection_T) -> None:
        """
        Called by base class Collection<T> when an item is added to list;
        raises a CollectionChanged event to any listeners.
        
        This method is protected.
        """
        ...

    def move(self, old_index: int, new_index: int) -> None:
        """Move item at old_index to new_index."""
        ...

    def move_item(self, old_index: int, new_index: int) -> None:
        """
        Called by base class ObservableCollection<T> when an item is to be moved within the list;
        raises a CollectionChanged event to any listeners.
        
        This method is protected.
        """
        ...

    def on_collection_changed(self, e: System.Collections.Specialized.NotifyCollectionChangedEventArgs) -> None:
        """
        Raise CollectionChanged event to any listeners.
        Properties/methods modifying this ObservableCollection will raise
        a collection changed event through this virtual method.
        
        This method is protected.
        """
        ...

    def on_property_changed(self, e: System.ComponentModel.PropertyChangedEventArgs) -> None:
        """
        Raises a PropertyChanged event (per INotifyPropertyChanged).
        
        This method is protected.
        """
        ...

    def remove_item(self, index: int) -> None:
        """
        Called by base class Collection<T> when an item is removed from list;
        raises a CollectionChanged event to any listeners.
        
        This method is protected.
        """
        ...

    def set_item(self, index: int, item: System_Collections_ObjectModel_ObservableCollection_T) -> None:
        """
        Called by base class Collection<T> when an item is set in list;
        raises a CollectionChanged event to any listeners.
        
        This method is protected.
        """
        ...


class ReadOnlyObservableCollection(typing.Generic[System_Collections_ObjectModel_ReadOnlyObservableCollection_T], System.Collections.ObjectModel.ReadOnlyCollection[System_Collections_ObjectModel_ReadOnlyObservableCollection_T], System.Collections.Specialized.INotifyCollectionChanged, System.ComponentModel.INotifyPropertyChanged):
    """Read-only wrapper around an ObservableCollection."""

    EMPTY: System.Collections.ObjectModel.ReadOnlyObservableCollection[System_Collections_ObjectModel_ReadOnlyObservableCollection_T]
    """Gets an empty ReadOnlyObservableCollection{T}."""

    @property
    def collection_changed(self) -> _EventContainer[typing.Callable[[System.Object, System.Collections.Specialized.NotifyCollectionChangedEventArgs], None], None]:
        """
        Occurs when the collection changes, either by adding or removing an item.
        
        This field is protected.
        """
        ...

    @collection_changed.setter
    def collection_changed(self, value: _EventContainer[typing.Callable[[System.Object, System.Collections.Specialized.NotifyCollectionChangedEventArgs], None], None]) -> None:
        ...

    @property
    def property_changed(self) -> _EventContainer[typing.Callable[[System.Object, System.ComponentModel.PropertyChangedEventArgs], None], None]:
        """
        Occurs when a property changes.
        
        This field is protected.
        """
        ...

    @property_changed.setter
    def property_changed(self, value: _EventContainer[typing.Callable[[System.Object, System.ComponentModel.PropertyChangedEventArgs], None], None]) -> None:
        ...

    def __init__(self, list: System.Collections.ObjectModel.ObservableCollection[System_Collections_ObjectModel_ReadOnlyObservableCollection_T]) -> None:
        """
        Initializes a new instance of ReadOnlyObservableCollection that
        wraps the given ObservableCollection.
        """
        ...

    def on_collection_changed(self, args: System.Collections.Specialized.NotifyCollectionChangedEventArgs) -> None:
        """
        raise CollectionChanged event to any listeners
        
        This method is protected.
        """
        ...

    def on_property_changed(self, args: System.ComponentModel.PropertyChangedEventArgs) -> None:
        """
        raise PropertyChanged event to any listeners
        
        This method is protected.
        """
        ...


class _EventContainer(typing.Generic[System_Collections_ObjectModel__EventContainer_Callable, System_Collections_ObjectModel__EventContainer_ReturnType]):
    """This class is used to provide accurate autocomplete on events and cannot be imported."""

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> System_Collections_ObjectModel__EventContainer_ReturnType:
        """Fires the event."""
        ...

    def __iadd__(self, item: System_Collections_ObjectModel__EventContainer_Callable) -> typing.Self:
        """Registers an event handler."""
        ...

    def __isub__(self, item: System_Collections_ObjectModel__EventContainer_Callable) -> typing.Self:
        """Unregisters an event handler."""
        ...


