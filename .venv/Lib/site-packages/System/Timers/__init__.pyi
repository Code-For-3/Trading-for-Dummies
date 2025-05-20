from typing import overload
from enum import Enum
import datetime
import typing

import System
import System.ComponentModel
import System.Timers

System_Timers__EventContainer_Callable = typing.TypeVar("System_Timers__EventContainer_Callable")
System_Timers__EventContainer_ReturnType = typing.TypeVar("System_Timers__EventContainer_ReturnType")


class ElapsedEventArgs(System.EventArgs):
    """Provides data for the System.Timers.Timer.Elapsed event."""

    @property
    def signal_time(self) -> datetime.datetime:
        """Gets the time when the timer elapsed."""
        ...

    def __init__(self, signal_time: typing.Union[datetime.datetime, datetime.date]) -> None:
        """
        Initializes a new instance of the System.Timers.ElapsedEventArgs class.
        
        :param signal_time: Time when the timer elapsed
        """
        ...


class TimersDescriptionAttribute(System.ComponentModel.DescriptionAttribute):
    """
    DescriptionAttribute marks a property, event, or extender with a
    description. Visual designers can display this description when referencing
    the member.
    """

    @property
    def description(self) -> str:
        """Retrieves the description text."""
        ...

    def __init__(self, description: str) -> None:
        """Constructs a new sys description."""
        ...


class Timer(System.ComponentModel.Component, System.ComponentModel.ISupportInitialize):
    """Handles recurring events in an application."""

    @property
    def auto_reset(self) -> bool:
        """
        Gets or sets a value indicating whether the Timer raises the Tick event each time the specified
        Interval has elapsed, when Enabled is set to true.
        """
        ...

    @auto_reset.setter
    def auto_reset(self, value: bool) -> None:
        ...

    @property
    def enabled(self) -> bool:
        """
        Gets or sets a value indicating whether the System.Timers.Timer
        is able to raise events at a defined interval.
        The default value by design is false, don't change it.
        """
        ...

    @enabled.setter
    def enabled(self, value: bool) -> None:
        ...

    @property
    def interval(self) -> float:
        """Gets or sets the interval on which to raise events."""
        ...

    @interval.setter
    def interval(self, value: float) -> None:
        ...

    @property
    def elapsed(self) -> _EventContainer[typing.Callable[[System.Object, System.Timers.ElapsedEventArgs], None], None]:
        """
        Occurs when the System.Timers.Timer.Interval has
        elapsed.
        """
        ...

    @elapsed.setter
    def elapsed(self, value: _EventContainer[typing.Callable[[System.Object, System.Timers.ElapsedEventArgs], None], None]) -> None:
        ...

    @property
    def site(self) -> System.ComponentModel.ISite:
        """Sets the enable property in design mode to true by default."""
        ...

    @site.setter
    def site(self, value: System.ComponentModel.ISite) -> None:
        ...

    @property
    def synchronizing_object(self) -> System.ComponentModel.ISynchronizeInvoke:
        """
        Gets or sets the object used to marshal event-handler calls that are issued when
        an interval has elapsed.
        """
        ...

    @synchronizing_object.setter
    def synchronizing_object(self, value: System.ComponentModel.ISynchronizeInvoke) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """
        Initializes a new instance of the System.Timers.Timer class, with the properties
        set to initial values.
        """
        ...

    @overload
    def __init__(self, interval: float) -> None:
        """
        Initializes a new instance of the System.Timers.Timer class, setting the System.Timers.Timer.Interval property to the specified period.
        
        :param interval: The time, in milliseconds, between events. The value must be greater than zero and less than or equal to int.MaxValue.
        """
        ...

    @overload
    def __init__(self, interval: datetime.timedelta) -> None:
        """
        Initializes a new instance of the Timer class, setting the Interval property to the specified period.
        
        :param interval: The time between events. The value in milliseconds must be greater than zero and less than or equal to int.MaxValue.
        """
        ...

    def begin_init(self) -> None:
        """Notifies the object that initialization is beginning and tells it to stand by."""
        ...

    def close(self) -> None:
        """
        Disposes of the resources (other than memory) used by
        the System.Timers.Timer.
        """
        ...

    def dispose(self, disposing: bool) -> None:
        """This method is protected."""
        ...

    def end_init(self) -> None:
        """Notifies the object that initialization is complete."""
        ...

    def start(self) -> None:
        """Starts the timing by setting System.Timers.Timer.Enabled to true."""
        ...

    def stop(self) -> None:
        """Stops the timing by setting System.Timers.Timer.Enabled to false."""
        ...


class _EventContainer(typing.Generic[System_Timers__EventContainer_Callable, System_Timers__EventContainer_ReturnType]):
    """This class is used to provide accurate autocomplete on events and cannot be imported."""

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> System_Timers__EventContainer_ReturnType:
        """Fires the event."""
        ...

    def __iadd__(self, item: System_Timers__EventContainer_Callable) -> typing.Self:
        """Registers an event handler."""
        ...

    def __isub__(self, item: System_Timers__EventContainer_Callable) -> typing.Self:
        """Unregisters an event handler."""
        ...


