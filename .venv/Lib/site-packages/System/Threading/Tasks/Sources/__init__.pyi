from typing import overload
from enum import Enum
import abc
import typing

import System
import System.Threading.Tasks.Sources

System_Threading_Tasks_Sources_ManualResetValueTaskSourceCore_TResult = typing.TypeVar("System_Threading_Tasks_Sources_ManualResetValueTaskSourceCore_TResult")
System_Threading_Tasks_Sources_IValueTaskSource_TResult = typing.TypeVar("System_Threading_Tasks_Sources_IValueTaskSource_TResult")


class ValueTaskSourceStatus(Enum):
    """Indicates the status of an IValueTaskSource or IValueTaskSource{TResult}."""

    PENDING = 0
    """The operation has not yet completed."""

    SUCCEEDED = 1
    """The operation completed successfully."""

    FAULTED = 2
    """The operation completed with an error."""

    CANCELED = 3
    """The operation completed due to cancellation."""


class ValueTaskSourceOnCompletedFlags(Enum):
    """
    Flags passed from ValueTask and ValueTask{TResult} to
    IValueTaskSource.OnCompleted and IValueTaskSource{TResult}.OnCompleted
    to control behavior.
    """

    NONE = 0
    """No requirements are placed on how the continuation is invoked."""

    USE_SCHEDULING_CONTEXT = ...
    """
    Set if OnCompleted should capture the current scheduling context (e.g. SynchronizationContext)
    and use it when queueing the continuation for execution.  If this is not set, the implementation
    may choose to execute the continuation in an arbitrary location.
    """

    FLOW_EXECUTION_CONTEXT = ...
    """Set if OnCompleted should capture the current ExecutionContext and use it to run the continuation."""


class ManualResetValueTaskSourceCore(typing.Generic[System_Threading_Tasks_Sources_ManualResetValueTaskSourceCore_TResult]):
    """Provides the core logic for implementing a manual-reset IValueTaskSource or IValueTaskSource{TResult}."""

    @property
    def run_continuations_asynchronously(self) -> bool:
        """Gets or sets whether to force continuations to run asynchronously."""
        ...

    @run_continuations_asynchronously.setter
    def run_continuations_asynchronously(self, value: bool) -> None:
        ...

    @property
    def version(self) -> int:
        """Gets the operation version."""
        ...

    def get_result(self, token: int) -> System_Threading_Tasks_Sources_ManualResetValueTaskSourceCore_TResult:
        """
        Gets the result of the operation.
        
        :param token: Opaque value that was provided to the ValueTask's constructor.
        """
        ...

    def get_status(self, token: int) -> System.Threading.Tasks.Sources.ValueTaskSourceStatus:
        """
        Gets the status of the operation.
        
        :param token: Opaque value that was provided to the ValueTask's constructor.
        """
        ...

    def on_completed(self, continuation: typing.Callable[[System.Object], None], state: typing.Any, token: int, flags: System.Threading.Tasks.Sources.ValueTaskSourceOnCompletedFlags) -> None:
        """
        Schedules the continuation action for this operation.
        
        :param continuation: The continuation to invoke when the operation has completed.
        :param state: The state object to pass to  when it's invoked.
        :param token: Opaque value that was provided to the ValueTask's constructor.
        :param flags: The flags describing the behavior of the continuation.
        """
        ...

    def reset(self) -> None:
        """Resets to prepare for the next operation."""
        ...

    def set_exception(self, error: System.Exception) -> None:
        """
        Completes with an error.
        
        :param error: The exception.
        """
        ...

    def set_result(self, result: System_Threading_Tasks_Sources_ManualResetValueTaskSourceCore_TResult) -> None:
        """
        Completes with a successful result.
        
        :param result: The result.
        """
        ...


class IValueTaskSource(typing.Generic[System_Threading_Tasks_Sources_IValueTaskSource_TResult], metaclass=abc.ABCMeta):
    """Represents an object that can be wrapped by a ValueTask{TResult}."""

    def get_result(self, token: int) -> None:
        """
        Gets the result of the IValueTaskSource.
        
        :param token: Opaque value that was provided to the ValueTask's constructor.
        """
        ...

    def get_status(self, token: int) -> System.Threading.Tasks.Sources.ValueTaskSourceStatus:
        """
        Gets the status of the current operation.
        
        :param token: Opaque value that was provided to the ValueTask's constructor.
        """
        ...

    def on_completed(self, continuation: typing.Callable[[System.Object], None], state: typing.Any, token: int, flags: System.Threading.Tasks.Sources.ValueTaskSourceOnCompletedFlags) -> None:
        """
        Schedules the continuation action for this IValueTaskSource.
        
        :param continuation: The continuation to invoke when the operation has completed.
        :param state: The state object to pass to  when it's invoked.
        :param token: Opaque value that was provided to the ValueTask's constructor.
        :param flags: The flags describing the behavior of the continuation.
        """
        ...


