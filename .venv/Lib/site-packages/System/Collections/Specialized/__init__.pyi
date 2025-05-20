from typing import overload
from enum import Enum
import abc
import typing

import System
import System.Collections
import System.Collections.Specialized

System_Collections_Specialized__EventContainer_Callable = typing.TypeVar("System_Collections_Specialized__EventContainer_Callable")
System_Collections_Specialized__EventContainer_ReturnType = typing.TypeVar("System_Collections_Specialized__EventContainer_ReturnType")


class NotifyCollectionChangedAction(Enum):
    """This enum describes the action that caused a CollectionChanged event."""

    ADD = 0
    """One or more items were added to the collection."""

    REMOVE = 1
    """One or more items were removed from the collection."""

    REPLACE = 2
    """One or more items were replaced in the collection."""

    MOVE = 3
    """One or more items were moved within the collection."""

    RESET = 4
    """The contents of the collection changed dramatically."""


class NotifyCollectionChangedEventArgs(System.EventArgs):
    """
    Arguments for the CollectionChanged event.
    A collection that supports INotifyCollectionChangedThis raises this event
    whenever an item is added or removed, or when the contents of the collection
    changes dramatically.
    """

    @property
    def action(self) -> System.Collections.Specialized.NotifyCollectionChangedAction:
        """The action that caused the event."""
        ...

    @property
    def new_items(self) -> typing.List[typing.Any]:
        """The items affected by the change."""
        ...

    @property
    def old_items(self) -> typing.List[typing.Any]:
        """The old items affected by the change (for Replace events)."""
        ...

    @property
    def new_starting_index(self) -> int:
        """The index where the change occurred."""
        ...

    @property
    def old_starting_index(self) -> int:
        """The old index where the change occurred (for Move events)."""
        ...

    @overload
    def __init__(self, action: System.Collections.Specialized.NotifyCollectionChangedAction, changed_item: typing.Any) -> None:
        """
        Construct a NotifyCollectionChangedEventArgs that describes a one-item change.
        
        :param action: The action that caused the event; can only be Reset, Add or Remove action.
        :param changed_item: The item affected by the change.
        """
        ...

    @overload
    def __init__(self, action: System.Collections.Specialized.NotifyCollectionChangedAction, changed_item: typing.Any, index: int) -> None:
        """
        Construct a NotifyCollectionChangedEventArgs that describes a one-item change.
        
        :param action: The action that caused the event.
        :param changed_item: The item affected by the change.
        :param index: The index where the change occurred.
        """
        ...

    @overload
    def __init__(self, action: System.Collections.Specialized.NotifyCollectionChangedAction, new_item: typing.Any, old_item: typing.Any) -> None:
        """
        Construct a NotifyCollectionChangedEventArgs that describes a one-item Replace event.
        
        :param action: Can only be a Replace action.
        :param new_item: The new item replacing the original item.
        :param old_item: The original item that is replaced.
        """
        ...

    @overload
    def __init__(self, action: System.Collections.Specialized.NotifyCollectionChangedAction, new_item: typing.Any, old_item: typing.Any, index: int) -> None:
        """
        Construct a NotifyCollectionChangedEventArgs that describes a one-item Replace event.
        
        :param action: Can only be a Replace action.
        :param new_item: The new item replacing the original item.
        :param old_item: The original item that is replaced.
        :param index: The index of the item being replaced.
        """
        ...

    @overload
    def __init__(self, action: System.Collections.Specialized.NotifyCollectionChangedAction, changed_item: typing.Any, index: int, old_index: int) -> None:
        """
        Construct a NotifyCollectionChangedEventArgs that describes a one-item Move event.
        
        :param action: Can only be a Move action.
        :param changed_item: The item affected by the change.
        :param index: The new index for the changed item.
        :param old_index: The old index for the changed item.
        """
        ...

    @overload
    def __init__(self, action: System.Collections.Specialized.NotifyCollectionChangedAction) -> None:
        """
        Construct a NotifyCollectionChangedEventArgs that describes a reset change.
        
        :param action: The action that caused the event (must be Reset).
        """
        ...

    @overload
    def __init__(self, action: System.Collections.Specialized.NotifyCollectionChangedAction, changed_items: System.Collections.IList) -> None:
        """
        Construct a NotifyCollectionChangedEventArgs that describes a multi-item change.
        
        :param action: The action that caused the event.
        :param changed_items: The items affected by the change.
        """
        ...

    @overload
    def __init__(self, action: System.Collections.Specialized.NotifyCollectionChangedAction, changed_items: System.Collections.IList, starting_index: int) -> None:
        """
        Construct a NotifyCollectionChangedEventArgs that describes a multi-item change (or a reset).
        
        :param action: The action that caused the event.
        :param changed_items: The items affected by the change.
        :param starting_index: The index where the change occurred.
        """
        ...

    @overload
    def __init__(self, action: System.Collections.Specialized.NotifyCollectionChangedAction, new_items: System.Collections.IList, old_items: System.Collections.IList) -> None:
        """
        Construct a NotifyCollectionChangedEventArgs that describes a multi-item Replace event.
        
        :param action: Can only be a Replace action.
        :param new_items: The new items replacing the original items.
        :param old_items: The original items that are replaced.
        """
        ...

    @overload
    def __init__(self, action: System.Collections.Specialized.NotifyCollectionChangedAction, new_items: System.Collections.IList, old_items: System.Collections.IList, starting_index: int) -> None:
        """
        Construct a NotifyCollectionChangedEventArgs that describes a multi-item Replace event.
        
        :param action: Can only be a Replace action.
        :param new_items: The new items replacing the original items.
        :param old_items: The original items that are replaced.
        :param starting_index: The starting index of the items being replaced.
        """
        ...

    @overload
    def __init__(self, action: System.Collections.Specialized.NotifyCollectionChangedAction, changed_items: System.Collections.IList, index: int, old_index: int) -> None:
        """
        Construct a NotifyCollectionChangedEventArgs that describes a multi-item Move event.
        
        :param action: The action that caused the event.
        :param changed_items: The items affected by the change.
        :param index: The new index for the changed items.
        :param old_index: The old index for the changed items.
        """
        ...


class INotifyCollectionChanged(metaclass=abc.ABCMeta):
    """
    A collection implementing this interface will notify listeners of dynamic changes,
    e.g. when items get added and removed or the whole list is refreshed.
    """

    @property
    @abc.abstractmethod
    def collection_changed(self) -> _EventContainer[typing.Callable[[System.Object, System.Collections.Specialized.NotifyCollectionChangedEventArgs], None], None]:
        """Occurs when the collection changes, either by adding or removing an item."""
        ...

    @collection_changed.setter
    def collection_changed(self, value: _EventContainer[typing.Callable[[System.Object, System.Collections.Specialized.NotifyCollectionChangedEventArgs], None], None]) -> None:
        ...


class _EventContainer(typing.Generic[System_Collections_Specialized__EventContainer_Callable, System_Collections_Specialized__EventContainer_ReturnType]):
    """This class is used to provide accurate autocomplete on events and cannot be imported."""

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> System_Collections_Specialized__EventContainer_ReturnType:
        """Fires the event."""
        ...

    def __iadd__(self, item: System_Collections_Specialized__EventContainer_Callable) -> typing.Self:
        """Registers an event handler."""
        ...

    def __isub__(self, item: System_Collections_Specialized__EventContainer_Callable) -> typing.Self:
        """Unregisters an event handler."""
        ...


