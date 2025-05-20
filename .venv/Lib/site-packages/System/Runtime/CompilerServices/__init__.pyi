from typing import overload
from enum import Enum
import abc
import typing
import warnings

import System
import System.Collections.Generic
import System.Diagnostics.Contracts
import System.Runtime.CompilerServices
import System.Runtime.Serialization
import System.Threading
import System.Threading.Tasks

System_Runtime_CompilerServices_ConfiguredValueTaskAwaitable_TResult = typing.TypeVar("System_Runtime_CompilerServices_ConfiguredValueTaskAwaitable_TResult")
System_Runtime_CompilerServices_PoolingAsyncValueTaskMethodBuilder_TResult = typing.TypeVar("System_Runtime_CompilerServices_PoolingAsyncValueTaskMethodBuilder_TResult")
System_Runtime_CompilerServices_AsyncTaskMethodBuilder_TResult = typing.TypeVar("System_Runtime_CompilerServices_AsyncTaskMethodBuilder_TResult")
System_Runtime_CompilerServices_ConfiguredCancelableAsyncEnumerable_T = typing.TypeVar("System_Runtime_CompilerServices_ConfiguredCancelableAsyncEnumerable_T")
System_Runtime_CompilerServices_ConditionalWeakTable_TKey = typing.TypeVar("System_Runtime_CompilerServices_ConditionalWeakTable_TKey")
System_Runtime_CompilerServices_ConditionalWeakTable_TValue = typing.TypeVar("System_Runtime_CompilerServices_ConditionalWeakTable_TValue")
System_Runtime_CompilerServices_TaskAwaiter_TResult = typing.TypeVar("System_Runtime_CompilerServices_TaskAwaiter_TResult")
System_Runtime_CompilerServices_ConfiguredTaskAwaitable_TResult = typing.TypeVar("System_Runtime_CompilerServices_ConfiguredTaskAwaitable_TResult")
System_Runtime_CompilerServices_StrongBox_T = typing.TypeVar("System_Runtime_CompilerServices_StrongBox_T")
System_Runtime_CompilerServices_ValueTaskAwaiter_TResult = typing.TypeVar("System_Runtime_CompilerServices_ValueTaskAwaiter_TResult")
System_Runtime_CompilerServices_AsyncValueTaskMethodBuilder_TResult = typing.TypeVar("System_Runtime_CompilerServices_AsyncValueTaskMethodBuilder_TResult")
System_Runtime_CompilerServices_InlineArray2_T = typing.TypeVar("System_Runtime_CompilerServices_InlineArray2_T")
System_Runtime_CompilerServices_InlineArray3_T = typing.TypeVar("System_Runtime_CompilerServices_InlineArray3_T")
System_Runtime_CompilerServices_InlineArray4_T = typing.TypeVar("System_Runtime_CompilerServices_InlineArray4_T")
System_Runtime_CompilerServices_InlineArray5_T = typing.TypeVar("System_Runtime_CompilerServices_InlineArray5_T")
System_Runtime_CompilerServices_InlineArray6_T = typing.TypeVar("System_Runtime_CompilerServices_InlineArray6_T")
System_Runtime_CompilerServices_InlineArray7_T = typing.TypeVar("System_Runtime_CompilerServices_InlineArray7_T")
System_Runtime_CompilerServices_InlineArray8_T = typing.TypeVar("System_Runtime_CompilerServices_InlineArray8_T")
System_Runtime_CompilerServices_InlineArray9_T = typing.TypeVar("System_Runtime_CompilerServices_InlineArray9_T")
System_Runtime_CompilerServices_InlineArray10_T = typing.TypeVar("System_Runtime_CompilerServices_InlineArray10_T")
System_Runtime_CompilerServices_InlineArray11_T = typing.TypeVar("System_Runtime_CompilerServices_InlineArray11_T")
System_Runtime_CompilerServices_InlineArray12_T = typing.TypeVar("System_Runtime_CompilerServices_InlineArray12_T")
System_Runtime_CompilerServices_InlineArray13_T = typing.TypeVar("System_Runtime_CompilerServices_InlineArray13_T")
System_Runtime_CompilerServices_InlineArray14_T = typing.TypeVar("System_Runtime_CompilerServices_InlineArray14_T")
System_Runtime_CompilerServices_InlineArray15_T = typing.TypeVar("System_Runtime_CompilerServices_InlineArray15_T")
System_Runtime_CompilerServices_InlineArray16_T = typing.TypeVar("System_Runtime_CompilerServices_InlineArray16_T")
System_Runtime_CompilerServices__EventContainer_Callable = typing.TypeVar("System_Runtime_CompilerServices__EventContainer_Callable")
System_Runtime_CompilerServices__EventContainer_ReturnType = typing.TypeVar("System_Runtime_CompilerServices__EventContainer_ReturnType")


class AsyncHelpers(System.Object):
    """This class has no documentation."""

    @staticmethod
    @overload
    def Await(task: System.Threading.Tasks.Task) -> None:
        ...

    @staticmethod
    @overload
    def Await(task: System.Threading.Tasks.ValueTask) -> None:
        ...

    @staticmethod
    @overload
    def Await(configuredAwaitable: System.Runtime.CompilerServices.ConfiguredTaskAwaitable) -> None:
        ...

    @staticmethod
    @overload
    def Await(configuredAwaitable: System.Runtime.CompilerServices.ConfiguredValueTaskAwaitable) -> None:
        ...


class InternalsVisibleToAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def assembly_name(self) -> str:
        ...

    @property
    def all_internals_visible(self) -> bool:
        ...

    @all_internals_visible.setter
    def all_internals_visible(self, value: bool) -> None:
        ...

    def __init__(self, assembly_name: str) -> None:
        ...


class ConfiguredValueTaskAwaitable(typing.Generic[System_Runtime_CompilerServices_ConfiguredValueTaskAwaitable_TResult]):
    """Provides an awaitable type that enables configured awaits on a ValueTask{TResult}."""

    def get_awaiter(self) -> System.Runtime.CompilerServices.ConfiguredValueTaskAwaitable.ConfiguredValueTaskAwaiter:
        """Returns an awaiter for this ConfiguredValueTaskAwaitable instance."""
        ...


class IAsyncStateMachine(metaclass=abc.ABCMeta):
    """
    Represents state machines generated for asynchronous methods.
    This type is intended for compiler use only.
    """

    def move_next(self) -> None:
        """Moves the state machine to its next state."""
        ...

    def set_state_machine(self, state_machine: System.Runtime.CompilerServices.IAsyncStateMachine) -> None:
        """
        Configures the state machine with a heap-allocated replica.
        
        :param state_machine: The heap-allocated replica.
        """
        ...


class DefaultInterpolatedStringHandler:
    """Provides a handler used by the language compiler to process interpolated strings into string instances."""

    @property
    def text(self) -> System.ReadOnlySpan[str]:
        """Gets a span of the characters appended to the handler."""
        ...

    @overload
    def __init__(self, literal_length: int, formatted_count: int) -> None:
        """
        Creates a handler used to translate an interpolated string into a string.
        
        :param literal_length: The number of constant characters outside of interpolation expressions in the interpolated string.
        :param formatted_count: The number of interpolation expressions in the interpolated string.
        """
        ...

    @overload
    def __init__(self, literal_length: int, formatted_count: int, provider: System.IFormatProvider) -> None:
        """
        Creates a handler used to translate an interpolated string into a string.
        
        :param literal_length: The number of constant characters outside of interpolation expressions in the interpolated string.
        :param formatted_count: The number of interpolation expressions in the interpolated string.
        :param provider: An object that supplies culture-specific formatting information.
        """
        ...

    @overload
    def __init__(self, literal_length: int, formatted_count: int, provider: System.IFormatProvider, initial_buffer: System.Span[str]) -> None:
        """
        Creates a handler used to translate an interpolated string into a string.
        
        :param literal_length: The number of constant characters outside of interpolation expressions in the interpolated string.
        :param formatted_count: The number of interpolation expressions in the interpolated string.
        :param provider: An object that supplies culture-specific formatting information.
        :param initial_buffer: A buffer temporarily transferred to the handler for use as part of its formatting.  Contents may be overwritten.
        """
        ...

    @overload
    def append_formatted(self, value: typing.Any, alignment: int = 0, format: str = None) -> None:
        ...

    @overload
    def append_formatted(self, value: System.ReadOnlySpan[str]) -> None:
        ...

    @overload
    def append_formatted(self, value: System.ReadOnlySpan[str], alignment: int = 0, format: str = None) -> None:
        """
        Writes the specified string of chars to the handler.
        
        :param value: The span to write.
        :param alignment: Minimum number of characters that should be written for this value.  If the value is negative, it indicates left-aligned and the required minimum is the absolute value.
        :param format: The format string.
        """
        ...

    @overload
    def append_formatted(self, value: str) -> None:
        ...

    @overload
    def append_formatted(self, value: str, alignment: int = 0, format: str = None) -> None:
        """
        Writes the specified value to the handler.
        
        :param value: The value to write.
        :param alignment: Minimum number of characters that should be written for this value.  If the value is negative, it indicates left-aligned and the required minimum is the absolute value.
        :param format: The format string.
        """
        ...

    def append_literal(self, value: str) -> None:
        """
        Writes the specified string to the handler.
        
        :param value: The string to write.
        """
        ...

    def clear(self) -> None:
        """Clears the handler."""
        ...

    def to_string(self) -> str:
        """
        Gets the built string.
        
        :returns: The built string.
        """
        ...

    def to_string_and_clear(self) -> str:
        """
        Gets the built string and clears the handler.
        
        :returns: The built string.
        """
        ...


class UnsafeAccessorKind(Enum):
    """Specifies the kind of target to which an UnsafeAccessorAttribute is providing access."""

    CONSTRUCTOR = 0
    """Provide access to a constructor."""

    METHOD = 1
    """Provide access to a method."""

    STATIC_METHOD = 2
    """Provide access to a static method."""

    FIELD = 3
    """Provide access to a field."""

    STATIC_FIELD = 4
    """Provide access to a static field."""


class UnsafeAccessorAttribute(System.Attribute):
    """Provides access to an inaccessible member of a specific type."""

    @property
    def kind(self) -> System.Runtime.CompilerServices.UnsafeAccessorKind:
        """Gets the kind of member to which access is provided."""
        ...

    @property
    def name(self) -> str:
        """Gets or sets the name of the member to which access is provided."""
        ...

    @name.setter
    def name(self, value: str) -> None:
        ...

    def __init__(self, kind: System.Runtime.CompilerServices.UnsafeAccessorKind) -> None:
        """
        Instantiates an UnsafeAccessorAttribute providing access to a member of kind UnsafeAccessorKind.
        
        :param kind: The kind of the target to which access is provided.
        """
        ...


class PoolingAsyncValueTaskMethodBuilder(typing.Generic[System_Runtime_CompilerServices_PoolingAsyncValueTaskMethodBuilder_TResult]):
    """Represents a builder for asynchronous methods that returns a ValueTask{TResult}."""

    @property
    def task(self) -> System.Threading.Tasks.ValueTask:
        """Gets the task for this builder."""
        ...

    @staticmethod
    def create() -> System.Runtime.CompilerServices.PoolingAsyncValueTaskMethodBuilder:
        """
        Creates an instance of the PoolingAsyncValueTaskMethodBuilder struct.
        
        :returns: The initialized instance.
        """
        ...

    def set_exception(self, exception: System.Exception) -> None:
        """
        Marks the task as failed and binds the specified exception to the task.
        
        :param exception: The exception to bind to the task.
        """
        ...

    @overload
    def set_result(self) -> None:
        """Marks the task as successfully completed."""
        ...

    @overload
    def set_result(self, result: System_Runtime_CompilerServices_PoolingAsyncValueTaskMethodBuilder_TResult) -> None:
        """
        Marks the value task as successfully completed.
        
        :param result: The result to use to complete the value task.
        """
        ...

    def set_state_machine(self, state_machine: System.Runtime.CompilerServices.IAsyncStateMachine) -> None:
        """
        Associates the builder with the specified state machine.
        
        :param state_machine: The state machine instance to associate with the builder.
        """
        ...


class ContractHelper(System.Object):
    """This class has no documentation."""

    @staticmethod
    def raise_contract_failed_event(failure_kind: System.Diagnostics.Contracts.ContractFailureKind, user_message: str, condition_text: str, inner_exception: System.Exception) -> str:
        """
        Rewriter will call this method on a contract failure to allow listeners to be notified.
        The method should not perform any failure (assert/throw) itself.
        This method has 3 functions:
        1. Call any contract hooks (such as listeners to Contract failed events)
        2. Determine if the listeners deem the failure as handled (then resultFailureMessage should be set to null)
        3. Produce a localized resultFailureMessage used in advertising the failure subsequently.
        On exit: null if the event was handled and should not trigger a failure.
                 Otherwise, returns the localized failure message.
        """
        ...

    @staticmethod
    def trigger_failure(kind: System.Diagnostics.Contracts.ContractFailureKind, display_message: str, user_message: str, condition_text: str, inner_exception: System.Exception) -> None:
        """Rewriter calls this method to get the default failure behavior."""
        ...


class AsyncTaskMethodBuilder(typing.Generic[System_Runtime_CompilerServices_AsyncTaskMethodBuilder_TResult]):
    """
    Provides a builder for asynchronous methods that return Task{TResult}.
    This type is intended for compiler use only.
    """

    @property
    def task(self) -> System.Threading.Tasks.Task:
        """Gets the Threading.Tasks.Task for this builder."""
        ...

    @staticmethod
    def create() -> System.Runtime.CompilerServices.AsyncTaskMethodBuilder:
        """
        Initializes a new AsyncTaskMethodBuilder.
        
        :returns: The initialized AsyncTaskMethodBuilder.
        """
        ...

    def set_exception(self, exception: System.Exception) -> None:
        """
        Completes the Threading.Tasks.Task in the
        TaskStatus state with the specified exception.
        
        :param exception: The Exception to use to fault the task.
        """
        ...

    @overload
    def set_result(self) -> None:
        """
        Completes the Threading.Tasks.Task in the
        TaskStatus state.
        """
        ...

    @overload
    def set_result(self, result: System_Runtime_CompilerServices_AsyncTaskMethodBuilder_TResult) -> None:
        """
        Completes the Task{TResult} in the
        TaskStatus state with the specified result.
        
        :param result: The result to use to complete the task.
        """
        ...

    def set_state_machine(self, state_machine: System.Runtime.CompilerServices.IAsyncStateMachine) -> None:
        """
        Associates the builder with the state machine it represents.
        
        :param state_machine: The heap-allocated state machine object.
        """
        ...


class CompilerGlobalScopeAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class CompilerGeneratedAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class CallConvCdecl(System.Object):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class CallConvFastcall(System.Object):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class CallConvStdcall(System.Object):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class CallConvSwift(System.Object):
    """Indicates that a method should using the https://github.com/apple/swift/blob/main/docs/ABIStabilityManifesto.md#calling-conventioncalling convention."""

    def __init__(self) -> None:
        """Initializes a new instance of the CallConvSwift class."""
        ...


class CallConvSuppressGCTransition(System.Object):
    """Indicates that a method should suppress the GC transition as part of the calling convention."""

    def __init__(self) -> None:
        """Initializes a new instance of the CallConvSuppressGCTransition class."""
        ...


class CallConvThiscall(System.Object):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class CallConvMemberFunction(System.Object):
    """Indicates that the calling convention used is the member function variant."""

    def __init__(self) -> None:
        """Initializes a new instance of the CallConvMemberFunction class."""
        ...


class TypeForwardedToAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def destination(self) -> typing.Type:
        ...

    def __init__(self, destination: typing.Type) -> None:
        ...


class IsConst(System.Object):
    """This class has no documentation."""


class CompilerFeatureRequiredAttribute(System.Attribute):
    """Indicates that compiler support for a particular feature is required for the location where this attribute is applied."""

    @property
    def feature_name(self) -> str:
        """The name of the compiler feature."""
        ...

    @property
    def is_optional(self) -> bool:
        """If true, the compiler can choose to allow access to the location where this attribute is applied if it does not understand FeatureName."""
        ...

    REF_STRUCTS: str = ...
    """The FeatureName used for the ref structs C# feature."""

    REQUIRED_MEMBERS: str = ...
    """The FeatureName used for the required members C# feature."""

    def __init__(self, feature_name: str) -> None:
        ...


class CallerFilePathAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class AsyncMethodBuilderAttribute(System.Attribute):
    """
    Indicates the type of the async method builder that should be used by a language compiler to
    build the attributed async method or to build the attributed type when used as the return type
    of an async method.
    """

    @property
    def builder_type(self) -> typing.Type:
        """Gets the Type of the associated builder."""
        ...

    def __init__(self, builder_type: typing.Type) -> None:
        """
        Initializes the AsyncMethodBuilderAttribute.
        
        :param builder_type: The Type of the associated builder.
        """
        ...


class ExtensionAttribute(System.Attribute):
    """Indicates that a method is an extension method, or that a class or assembly contains extension methods."""


class ConfiguredCancelableAsyncEnumerable(typing.Generic[System_Runtime_CompilerServices_ConfiguredCancelableAsyncEnumerable_T]):
    """Provides an awaitable async enumerable that enables cancelable iteration and configured awaits."""

    class Enumerator:
        """Provides an awaitable async enumerator that enables cancelable iteration and configured awaits."""

        @property
        def current(self) -> System_Runtime_CompilerServices_ConfiguredCancelableAsyncEnumerable_T:
            """Gets the element in the collection at the current position of the enumerator."""
            ...

        def dispose_async(self) -> System.Runtime.CompilerServices.ConfiguredValueTaskAwaitable:
            """
            Performs application-defined tasks associated with freeing, releasing, or
            resetting unmanaged resources asynchronously.
            """
            ...

        def move_next_async(self) -> System.Runtime.CompilerServices.ConfiguredValueTaskAwaitable[bool]:
            """
            Advances the enumerator asynchronously to the next element of the collection.
            
            :returns: A ConfiguredValueTaskAwaitable{Boolean} that will complete with a result of true if the enumerator was successfully advanced to the next element, or false if the enumerator has passed the end of the collection.
            """
            ...

    def configure_await(self, continue_on_captured_context: bool) -> System.Runtime.CompilerServices.ConfiguredCancelableAsyncEnumerable[System_Runtime_CompilerServices_ConfiguredCancelableAsyncEnumerable_T]:
        """
        Configures how awaits on the tasks returned from an async iteration will be performed.
        
        :param continue_on_captured_context: true to capture and marshal back to the current context; otherwise, false.
        :returns: The configured enumerable.
        """
        ...

    def get_async_enumerator(self) -> System.Runtime.CompilerServices.ConfiguredCancelableAsyncEnumerable.Enumerator:
        """
        Returns an enumerator that iterates asynchronously through collections that enables cancelable iteration and configured awaits.
        
        :returns: An enumerator for the System.Runtime.CompilerServices.ConfiguredCancelableAsyncEnumerable`1 class.
        """
        ...

    def with_cancellation(self, cancellation_token: System.Threading.CancellationToken) -> System.Runtime.CompilerServices.ConfiguredCancelableAsyncEnumerable[System_Runtime_CompilerServices_ConfiguredCancelableAsyncEnumerable_T]:
        """
        Sets the CancellationToken to be passed to IAsyncEnumerable{T}.GetAsyncEnumerator(CancellationToken) when iterating.
        
        :param cancellation_token: The CancellationToken to use.
        :returns: The configured enumerable.
        """
        ...


class ConditionalWeakTable(typing.Generic[System_Runtime_CompilerServices_ConditionalWeakTable_TKey, System_Runtime_CompilerServices_ConditionalWeakTable_TValue], System.Object, System.Collections.Generic.IEnumerable[System.Collections.Generic.KeyValuePair[System_Runtime_CompilerServices_ConditionalWeakTable_TKey, System_Runtime_CompilerServices_ConditionalWeakTable_TValue]], typing.Iterable[System.Collections.Generic.KeyValuePair[System_Runtime_CompilerServices_ConditionalWeakTable_TKey, System_Runtime_CompilerServices_ConditionalWeakTable_TValue]]):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...

    def __iter__(self) -> typing.Iterator[System.Collections.Generic.KeyValuePair[System_Runtime_CompilerServices_ConditionalWeakTable_TKey, System_Runtime_CompilerServices_ConditionalWeakTable_TValue]]:
        ...

    def add(self, key: System_Runtime_CompilerServices_ConditionalWeakTable_TKey, value: System_Runtime_CompilerServices_ConditionalWeakTable_TValue) -> None:
        """
        Adds a key to the table.
        
        :param key: key to add. May not be null.
        :param value: value to associate with key.
        """
        ...

    def add_or_update(self, key: System_Runtime_CompilerServices_ConditionalWeakTable_TKey, value: System_Runtime_CompilerServices_ConditionalWeakTable_TValue) -> None:
        """
        Adds the key and value if the key doesn't exist, or updates the existing key's value if it does exist.
        
        :param key: key to add or update. May not be null.
        :param value: value to associate with key.
        """
        ...

    def clear(self) -> None:
        """Clear all the key/value pairs"""
        ...

    def create_value_callback(self, key: System_Runtime_CompilerServices_ConditionalWeakTable_TKey) -> System_Runtime_CompilerServices_ConditionalWeakTable_TValue:
        ...

    @overload
    def get_or_add(self, key: System_Runtime_CompilerServices_ConditionalWeakTable_TKey, value: System_Runtime_CompilerServices_ConditionalWeakTable_TValue) -> System_Runtime_CompilerServices_ConditionalWeakTable_TValue:
        """
        Searches for a specified key in the table and returns the corresponding value. If the key does
        not exist in the table, the method adds the given value and binds it to the specified key.
        
        :param key: The key of the value to find. It cannot be null.
        :param value: The value to add and bind to TKey, if one does not exist already.
        :returns: The value bound to TKey in the current ConditionalWeakTable{TKey, TValue} instance, after the method completes.
        """
        ...

    @overload
    def get_or_add(self, key: System_Runtime_CompilerServices_ConditionalWeakTable_TKey, value_factory: typing.Callable[[System_Runtime_CompilerServices_ConditionalWeakTable_TKey], System_Runtime_CompilerServices_ConditionalWeakTable_TValue]) -> System_Runtime_CompilerServices_ConditionalWeakTable_TValue:
        """
        Searches for a specified key in the table and returns the corresponding value. If the key does not exist
        in the table, the method invokes the supplied factory to create a value that is bound to the specified key.
        
        :param key: The key of the value to find. It cannot be null.
        :param value_factory: The callback that creates a value for key, if one does not exist already. It cannot be null.
        :returns: The value bound to TKey in the current ConditionalWeakTable{TKey, TValue} instance, after the method completes.
        """
        ...

    def get_or_create_value(self, key: System_Runtime_CompilerServices_ConditionalWeakTable_TKey) -> System_Runtime_CompilerServices_ConditionalWeakTable_TValue:
        """
        Helper method to call GetValue without passing a creation delegate.  Uses Activator.CreateInstance
        to create new instances as needed.  If TValue does not have a default constructor, this will throw.
        
        :param key: key of the value to find. Cannot be null.
        """
        ...

    def get_value(self, key: System_Runtime_CompilerServices_ConditionalWeakTable_TKey, create_value_callback: typing.Callable[[System_Runtime_CompilerServices_ConditionalWeakTable_TKey], System_Runtime_CompilerServices_ConditionalWeakTable_TValue]) -> System_Runtime_CompilerServices_ConditionalWeakTable_TValue:
        """
        Searches for a specified key in the table and returns the corresponding value. If the key does not exist
        in the table, the method invokes a callback method to create a value that is bound to the specified key.
        
        :param key: key of the value to find. Cannot be null.
        :param create_value_callback: callback that creates value for key. Cannot be null.
        """
        ...

    @overload
    def remove(self, key: System_Runtime_CompilerServices_ConditionalWeakTable_TKey) -> bool:
        """
        Removes a key and its value from the table.
        
        :param key: The key to remove.
        :returns: true if the key is found and removed; otherwise, false.
        """
        ...

    @overload
    def remove(self, key: System_Runtime_CompilerServices_ConditionalWeakTable_TKey, value: typing.Optional[System_Runtime_CompilerServices_ConditionalWeakTable_TValue]) -> typing.Tuple[bool, System_Runtime_CompilerServices_ConditionalWeakTable_TValue]:
        """
        Removes a key and its value from the table, and returns the removed value if it was present.
        
        :param key: The key to remove.
        :param value: value removed from the table, if it was present.
        :returns: true if the key is found and removed; otherwise, false.
        """
        ...

    def try_add(self, key: System_Runtime_CompilerServices_ConditionalWeakTable_TKey, value: System_Runtime_CompilerServices_ConditionalWeakTable_TValue) -> bool:
        """
        Adds a key to the table if it doesn't already exist.
        
        :param key: The key to add.
        :param value: The key's property value.
        :returns: true if the key/value pair was added; false if the table already contained the key.
        """
        ...

    def try_get_value(self, key: System_Runtime_CompilerServices_ConditionalWeakTable_TKey, value: typing.Optional[System_Runtime_CompilerServices_ConditionalWeakTable_TValue]) -> typing.Tuple[bool, System_Runtime_CompilerServices_ConditionalWeakTable_TValue]:
        """
        Gets the value of the specified key.
        
        :param key: key of the value to find. Cannot be null.
        :param value: If the key is found, contains the value associated with the key upon method return. If the key is not found, contains default(TValue).
        :returns: Returns "true" if key was found, "false" otherwise.
        """
        ...


class ModuleInitializerAttribute(System.Attribute):
    """
    Used to indicate to the compiler that a method should be called
    in its containing module's initializer.
    """

    def __init__(self) -> None:
        ...


class TypeForwardedFromAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def assembly_full_name(self) -> str:
        ...

    def __init__(self, assembly_full_name: str) -> None:
        ...


class PreserveBaseOverridesAttribute(System.Attribute):
    """This class has no documentation."""


class INotifyCompletion(metaclass=abc.ABCMeta):
    """Represents an operation that will schedule continuations when the operation completes."""

    def on_completed(self, continuation: typing.Callable[[], None]) -> None:
        """
        Schedules the continuation action to be invoked when the instance completes.
        
        :param continuation: The action to invoke when the operation completes.
        """
        ...


class ICriticalNotifyCompletion(System.Runtime.CompilerServices.INotifyCompletion, metaclass=abc.ABCMeta):
    """Represents an awaiter used to schedule continuations when an await operation completes."""

    def unsafe_on_completed(self, continuation: typing.Callable[[], None]) -> None:
        """
        Schedules the continuation action to be invoked when the instance completes.
        
        :param continuation: The action to invoke when the operation completes.
        """
        ...


class YieldAwaitable:
    """Provides an awaitable context for switching into a target environment."""

    class YieldAwaiter(System.Runtime.CompilerServices.ICriticalNotifyCompletion, System.Runtime.CompilerServices.IStateMachineBoxAwareAwaiter):
        """Provides an awaiter that switches into a target environment."""

        @property
        def is_completed(self) -> bool:
            """Gets whether a yield is not required."""
            ...

        def get_result(self) -> None:
            """Ends the await operation."""
            ...

        def on_completed(self, continuation: typing.Callable[[], None]) -> None:
            """
            Posts the  back to the current context.
            
            :param continuation: The action to invoke asynchronously.
            """
            ...

        def unsafe_on_completed(self, continuation: typing.Callable[[], None]) -> None:
            """
            Posts the  back to the current context.
            
            :param continuation: The action to invoke asynchronously.
            """
            ...

    def get_awaiter(self) -> System.Runtime.CompilerServices.YieldAwaitable.YieldAwaiter:
        """
        Gets an awaiter for this YieldAwaitable.
        
        :returns: An awaiter for this awaitable.
        """
        ...


class Unsafe(System.Object):
    """Contains generic, low-level functionality for manipulating pointers."""

    @staticmethod
    @overload
    def copy_block(destination: typing.Any, source: typing.Any, byte_count: int) -> None:
        """Copies bytes from the source address to the destination address."""
        ...

    @staticmethod
    @overload
    def copy_block(destination: int, source: int, byte_count: int) -> None:
        """Copies bytes from the source address to the destination address."""
        ...

    @staticmethod
    @overload
    def copy_block_unaligned(destination: typing.Any, source: typing.Any, byte_count: int) -> None:
        """Copies bytes from the source address to the destination address without assuming architecture dependent alignment of the addresses."""
        ...

    @staticmethod
    @overload
    def copy_block_unaligned(destination: int, source: int, byte_count: int) -> None:
        """Copies bytes from the source address to the destination address without assuming architecture dependent alignment of the addresses."""
        ...

    @staticmethod
    @overload
    def init_block(start_address: typing.Any, value: int, byte_count: int) -> None:
        """Initializes a block of memory at the given location with a given initial value."""
        ...

    @staticmethod
    @overload
    def init_block(start_address: int, value: int, byte_count: int) -> None:
        """Initializes a block of memory at the given location with a given initial value."""
        ...

    @staticmethod
    @overload
    def init_block_unaligned(start_address: typing.Any, value: int, byte_count: int) -> None:
        """
        Initializes a block of memory at the given location with a given initial value
        without assuming architecture dependent alignment of the address.
        """
        ...

    @staticmethod
    @overload
    def init_block_unaligned(start_address: int, value: int, byte_count: int) -> None:
        """
        Initializes a block of memory at the given location with a given initial value
        without assuming architecture dependent alignment of the address.
        """
        ...


class CallerMemberNameAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class SuppressIldasmAttribute(System.Attribute):
    """Obsoletions.SuppressIldasmAttributeMessage"""

    def __init__(self) -> None:
        ...


class TupleElementNamesAttribute(System.Attribute):
    """Indicates that the use of ValueTuple on a member is meant to be treated as a tuple with element names."""

    @property
    def transform_names(self) -> typing.List[str]:
        """
        Specifies, in a pre-order depth-first traversal of a type's
        construction, which ValueTuple elements are
        meant to carry element names.
        """
        ...

    def __init__(self, transform_names: typing.List[str]) -> None:
        """
        Initializes a new instance of the TupleElementNamesAttribute class.
        
        :param transform_names: Specifies, in a pre-order depth-first traversal of a type's construction, which ValueType occurrences are meant to carry element names.
        """
        ...


class UnsafeValueTypeAttribute(System.Attribute):
    """This class has no documentation."""


class RuntimeWrappedException(System.Exception):
    """Exception used to wrap all non-CLS compliant exceptions."""

    @property
    def wrapped_exception(self) -> System.Object:
        ...

    def __init__(self, thrown_object: typing.Any) -> None:
        ...

    def get_object_data(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """Obsoletions.LegacyFormatterImplMessage"""
        warnings.warn("Obsoletions.LegacyFormatterImplMessage", DeprecationWarning)


class DisablePrivateReflectionAttribute(System.Attribute):
    """Obsoletions.DisablePrivateReflectionAttributeMessage"""

    def __init__(self) -> None:
        ...


class NullablePublicOnlyAttribute(System.Attribute):
    """
    Reserved for use by a compiler for tracking metadata.
    This attribute should not be used by developers in source code.
    """

    @property
    def includes_internals(self) -> bool:
        """Indicates whether metadata for internal members is included."""
        ...

    @includes_internals.setter
    def includes_internals(self, value: bool) -> None:
        ...

    def __init__(self, value: bool) -> None:
        """
        Initializes the attribute.
        
        :param value: Indicates whether metadata for internal members is included.
        """
        ...


class SpecialNameAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class AccessedThroughPropertyAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def property_name(self) -> str:
        ...

    def __init__(self, property_name: str) -> None:
        ...


class TaskAwaiter(typing.Generic[System_Runtime_CompilerServices_TaskAwaiter_TResult], System.Runtime.CompilerServices.ICriticalNotifyCompletion, System.Runtime.CompilerServices.ITaskAwaiter):
    """Provides an awaiter for awaiting a Task{TResult}."""

    @property
    def is_completed(self) -> bool:
        """Gets whether the task being awaited is completed."""
        ...

    def get_result(self) -> None:
        """Ends the await on the completed Task."""
        ...

    def on_completed(self, continuation: typing.Callable[[], None]) -> None:
        """
        Schedules the continuation onto the Task associated with this TaskAwaiter.
        
        :param continuation: The action to invoke when the await operation completes.
        """
        ...

    def unsafe_on_completed(self, continuation: typing.Callable[[], None]) -> None:
        """
        Schedules the continuation onto the Task associated with this TaskAwaiter.
        
        :param continuation: The action to invoke when the await operation completes.
        """
        ...


class ConfiguredTaskAwaitable(typing.Generic[System_Runtime_CompilerServices_ConfiguredTaskAwaitable_TResult]):
    """Provides an awaitable object that allows for configured awaits on Task{TResult}."""

    def get_awaiter(self) -> System.Runtime.CompilerServices.ConfiguredTaskAwaitable.ConfiguredTaskAwaiter:
        """
        Gets an awaiter for this awaitable.
        
        :returns: The awaiter.
        """
        ...


class IStrongBox(metaclass=abc.ABCMeta):
    """Defines a property for accessing the value that an object references."""

    @property
    @abc.abstractmethod
    def value(self) -> System.Object:
        """Gets or sets the value the object references."""
        ...

    @value.setter
    def value(self, value: System.Object) -> None:
        ...


class StrongBox(typing.Generic[System_Runtime_CompilerServices_StrongBox_T], System.Object, System.Runtime.CompilerServices.IStrongBox):
    """Holds a reference to a value."""

    @property
    def value(self) -> System_Runtime_CompilerServices_StrongBox_T:
        """Gets the strongly typed value associated with the StrongBox{T}This is explicitly exposed as a field instead of a property to enable loading the address of the field."""
        ...

    @value.setter
    def value(self, value: System_Runtime_CompilerServices_StrongBox_T) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new StrongBox which can receive a value when used in a reference call."""
        ...

    @overload
    def __init__(self, value: System_Runtime_CompilerServices_StrongBox_T) -> None:
        """
        Initializes a new StrongBox{T} with the specified value.
        
        :param value: A value that the StrongBox{T} will reference.
        """
        ...


class ValueTaskAwaiter(typing.Generic[System_Runtime_CompilerServices_ValueTaskAwaiter_TResult], System.Runtime.CompilerServices.ICriticalNotifyCompletion, System.Runtime.CompilerServices.IStateMachineBoxAwareAwaiter):
    """Provides an awaiter for a ValueTask{TResult}."""

    @property
    def is_completed(self) -> bool:
        """Gets whether the ValueTask has completed."""
        ...

    def get_result(self) -> None:
        """Gets the result of the ValueTask."""
        ...

    def on_completed(self, continuation: typing.Callable[[], None]) -> None:
        """Schedules the continuation action for this ValueTask."""
        ...

    def unsafe_on_completed(self, continuation: typing.Callable[[], None]) -> None:
        """Schedules the continuation action for this ValueTask."""
        ...


class CreateNewOnMetadataUpdateAttribute(System.Attribute):
    """Indicates a type should be replaced rather than updated when applying metadata updates."""


class MethodCodeType(Enum):
    """This class has no documentation."""

    IL = ...

    NATIVE = ...

    OPTIL = ...

    RUNTIME = ...


class AsyncValueTaskMethodBuilder(typing.Generic[System_Runtime_CompilerServices_AsyncValueTaskMethodBuilder_TResult]):
    """Represents a builder for asynchronous methods that returns a ValueTask{TResult}."""

    @property
    def task(self) -> System.Threading.Tasks.ValueTask:
        """Gets the task for this builder."""
        ...

    @staticmethod
    def create() -> System.Runtime.CompilerServices.AsyncValueTaskMethodBuilder:
        """
        Creates an instance of the AsyncValueTaskMethodBuilder struct.
        
        :returns: The initialized instance.
        """
        ...

    def set_exception(self, exception: System.Exception) -> None:
        """
        Marks the task as failed and binds the specified exception to the task.
        
        :param exception: The exception to bind to the task.
        """
        ...

    @overload
    def set_result(self) -> None:
        """Marks the task as successfully completed."""
        ...

    @overload
    def set_result(self, result: System_Runtime_CompilerServices_AsyncValueTaskMethodBuilder_TResult) -> None:
        """
        Marks the value task as successfully completed.
        
        :param result: The result to use to complete the value task.
        """
        ...

    def set_state_machine(self, state_machine: System.Runtime.CompilerServices.IAsyncStateMachine) -> None:
        """
        Associates the builder with the specified state machine.
        
        :param state_machine: The state machine instance to associate with the builder.
        """
        ...


class EnumeratorCancellationAttribute(System.Attribute):
    """Allows users of async-enumerable methods to mark the parameter that should receive the cancellation token value from System.Collections.Generic.IAsyncEnumerable`1.GetAsyncEnumerator(System.Threading.CancellationToken)."""

    def __init__(self) -> None:
        """Initializes a new instance of the System.Runtime.CompilerServices.EnumeratorCancellationAttribute class."""
        ...


class IsByRefLikeAttribute(System.Attribute):
    """
    Reserved for use by a compiler for tracking metadata.
    This attribute should not be used by developers in source code.
    """

    def __init__(self) -> None:
        """Initializes the attribute."""
        ...


class FixedAddressValueTypeAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class RuntimeCompatibilityAttribute(System.Attribute):
    """Specifies whether to enable various legacy or new opt-in behaviors."""

    @property
    def wrap_non_exception_throws(self) -> bool:
        ...

    @wrap_non_exception_throws.setter
    def wrap_non_exception_throws(self, value: bool) -> None:
        ...

    def __init__(self) -> None:
        ...


class ParamCollectionAttribute(System.Attribute):
    """Indicates that a method will allow a variable number of arguments in its invocation."""


class IndexerNameAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self, indexer_name: str) -> None:
        ...


class StringFreezingAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class StateMachineAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def state_machine_type(self) -> typing.Type:
        ...

    def __init__(self, state_machine_type: typing.Type) -> None:
        ...


class AsyncStateMachineAttribute(System.Runtime.CompilerServices.StateMachineAttribute):
    """This class has no documentation."""

    def __init__(self, state_machine_type: typing.Type) -> None:
        ...


class CompilationRelaxations(Enum):
    """This class has no documentation."""

    NO_STRING_INTERNING = ...


class CompilationRelaxationsAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def compilation_relaxations(self) -> int:
        ...

    @overload
    def __init__(self, relaxations: int) -> None:
        ...

    @overload
    def __init__(self, relaxations: System.Runtime.CompilerServices.CompilationRelaxations) -> None:
        ...


class ConfiguredAsyncDisposable:
    """Provides a type that can be used to configure how awaits on an IAsyncDisposable are performed."""

    def dispose_async(self) -> System.Runtime.CompilerServices.ConfiguredValueTaskAwaitable:
        """
        Asynchronously releases the unmanaged resources used by the System.Runtime.CompilerServices.ConfiguredAsyncDisposable.
        
        :returns: A task that represents the asynchronous dispose operation.
        """
        ...


class SkipLocalsInitAttribute(System.Attribute):
    """
    Used to indicate to the compiler that the .locals init
    flag should not be set in method headers.
    """

    def __init__(self) -> None:
        ...


class DecimalConstantAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def value(self) -> float:
        ...

    def __init__(self, scale: int, sign: int, hi: int, mid: int, low: int) -> None:
        ...


class AsyncIteratorMethodBuilder:
    """Represents a builder for asynchronous iterators."""

    def complete(self) -> None:
        """Marks iteration as being completed, whether successfully or otherwise."""
        ...

    @staticmethod
    def create() -> System.Runtime.CompilerServices.AsyncIteratorMethodBuilder:
        """
        Creates an instance of the AsyncIteratorMethodBuilder struct.
        
        :returns: The initialized instance.
        """
        ...


class CallerLineNumberAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class NullableContextAttribute(System.Attribute):
    """
    Reserved for use by a compiler for tracking metadata.
    This attribute should not be used by developers in source code.
    """

    @property
    def flag(self) -> int:
        """Flag specifying metadata related to nullable reference types."""
        ...

    @flag.setter
    def flag(self, value: int) -> None:
        ...

    def __init__(self, value: int) -> None:
        """
        Initializes the attribute.
        
        :param value: The flag value.
        """
        ...


class DisableRuntimeMarshallingAttribute(System.Attribute):
    """
    Disables the built-in runtime managed/unmanaged marshalling subsystem for
    P/Invokes, Delegate types, and unmanaged function pointer invocations.
    """


class RuntimeFeature(System.Object):
    """This class has no documentation."""

    PORTABLE_PDB: str = ...
    """Name of the Portable PDB feature."""

    DEFAULT_IMPLEMENTATIONS_OF_INTERFACES: str = ...
    """Indicates that this version of runtime supports default interface method implementations."""

    UNMANAGED_SIGNATURE_CALLING_CONVENTION: str = ...
    """Indicates that this version of runtime supports the Unmanaged calling convention value."""

    COVARIANT_RETURNS_OF_CLASSES: str = ...
    """Indicates that this version of runtime supports covariant returns in overrides of methods declared in classes."""

    BY_REF_FIELDS: str = ...
    """Represents a runtime feature where types can define ref fields."""

    BY_REF_LIKE_GENERICS: str = ...
    """Represents a runtime feature where byref-like types can be used in Generic parameters."""

    VIRTUAL_STATICS_IN_INTERFACES: str = ...
    """Indicates that this version of runtime supports virtual static members of interfaces."""

    NUMERIC_INT_PTR: str = ...
    """Indicates that this version of runtime supports System.IntPtr and System.UIntPtr as numeric types."""

    IS_DYNAMIC_CODE_SUPPORTED: bool

    IS_DYNAMIC_CODE_COMPILED: bool

    @staticmethod
    def is_supported(feature: str) -> bool:
        """Checks whether a certain feature is supported by the Runtime."""
        ...


class RefSafetyRulesAttribute(System.Attribute):
    """Indicates the language version of the ref safety rules used when the module was compiled."""

    @property
    def version(self) -> int:
        """Gets the language version of the ref safety rules used when the module was compiled."""
        ...

    def __init__(self, version: int) -> None:
        """
        Initializes a new instance of the RefSafetyRulesAttribute class.
        
        :param version: The language version of the ref safety rules used when the module was compiled.
        """
        ...


class IsReadOnlyAttribute(System.Attribute):
    """
    Reserved for use by a compiler for tracking metadata.
    This attribute should not be used by developers in source code.
    """

    def __init__(self) -> None:
        """Initializes the attribute."""
        ...


class MetadataUpdateOriginalTypeAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def original_type(self) -> typing.Type:
        ...

    def __init__(self, original_type: typing.Type) -> None:
        """
        This attribute is emitted by Roslyn when a type that is marked with (or derives
        from a type that is marked with) CreateNewOnMetadataUpdateAttribute is updated
        during a hot reload session.  The OriginalType points to the original version
        of the updated type.  The next update of the type will have the same OriginalType. Frameworks that provide support for hot reload by implementing a
        Reflection.Metadata.MetadataUpdateHandlerAttribute may use this
        attribute to relate an updated type to its original version.
        
        :param original_type: The original type that was updated
        """
        ...


class MethodImplOptions(Enum):
    """This class has no documentation."""

    UNMANAGED = ...

    NO_INLINING = ...

    FORWARD_REF = ...

    SYNCHRONIZED = ...

    NO_OPTIMIZATION = ...

    PRESERVE_SIG = ...

    AGGRESSIVE_INLINING = ...

    AGGRESSIVE_OPTIMIZATION = ...

    ASYNC = ...

    INTERNAL_CALL = ...


class MethodImplAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def method_code_type(self) -> System.Runtime.CompilerServices.MethodCodeType:
        ...

    @method_code_type.setter
    def method_code_type(self, value: System.Runtime.CompilerServices.MethodCodeType) -> None:
        ...

    @property
    def value(self) -> System.Runtime.CompilerServices.MethodImplOptions:
        ...

    @overload
    def __init__(self, method_impl_options: System.Runtime.CompilerServices.MethodImplOptions) -> None:
        ...

    @overload
    def __init__(self, value: int) -> None:
        ...

    @overload
    def __init__(self) -> None:
        ...


class AsyncVoidMethodBuilder:
    """
    Provides a builder for asynchronous methods that return void.
    This type is intended for compiler use only.
    """

    @staticmethod
    def create() -> System.Runtime.CompilerServices.AsyncVoidMethodBuilder:
        """
        Initializes a new AsyncVoidMethodBuilder.
        
        :returns: The initialized AsyncVoidMethodBuilder.
        """
        ...

    def set_exception(self, exception: System.Exception) -> None:
        """
        Faults the method builder with an exception.
        
        :param exception: The exception that is the cause of this fault.
        """
        ...

    def set_result(self) -> None:
        """Completes the method builder successfully."""
        ...

    def set_state_machine(self, state_machine: System.Runtime.CompilerServices.IAsyncStateMachine) -> None:
        """
        Associates the builder with the state machine it represents.
        
        :param state_machine: The heap-allocated state machine object.
        """
        ...


class FormattableStringFactory(System.Object):
    """Provides a static method to create a FormattableString object from a composite format string and its arguments."""

    @staticmethod
    def create(format: str, *arguments: typing.Union[System.Object, typing.Iterable[System.Object]]) -> System.FormattableString:
        """
        Create a FormattableString from a composite format string and object
        array containing zero or more objects to format.
        """
        ...


class DiscardableAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class InterpolatedStringHandlerArgumentAttribute(System.Attribute):
    """Indicates which arguments to a method involving an interpolated string handler should be passed to that handler."""

    @property
    def arguments(self) -> typing.List[str]:
        """Gets the names of the arguments that should be passed to the handler."""
        ...

    @overload
    def __init__(self, argument: str) -> None:
        """
        Initializes a new instance of the InterpolatedStringHandlerArgumentAttribute class.
        
        :param argument: The name of the argument that should be passed to the handler.
        """
        ...

    @overload
    def __init__(self, *arguments: typing.Union[str, typing.Iterable[str]]) -> None:
        """
        Initializes a new instance of the InterpolatedStringHandlerArgumentAttribute class.
        
        :param arguments: The names of the arguments that should be passed to the handler.
        """
        ...


class LoadHint(Enum):
    """This class has no documentation."""

    DEFAULT = ...

    ALWAYS = ...

    SOMETIMES = ...


class DefaultDependencyAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def load_hint(self) -> System.Runtime.CompilerServices.LoadHint:
        ...

    def __init__(self, load_hint_argument: System.Runtime.CompilerServices.LoadHint) -> None:
        ...


class CustomConstantAttribute(System.Attribute, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def value(self) -> System.Object:
        ...


class DateTimeConstantAttribute(System.Runtime.CompilerServices.CustomConstantAttribute):
    """This class has no documentation."""

    @property
    def value(self) -> System.Object:
        ...

    def __init__(self, ticks: int) -> None:
        ...


class SwitchExpressionException(System.InvalidOperationException):
    """
    Indicates that a switch expression that was non-exhaustive failed to match its input
    at runtime, e.g. in the C# 8 expression 3 switch { 4 => 5 }.
    The exception optionally contains an object representing the unmatched value.
    """

    @property
    def unmatched_value(self) -> System.Object:
        ...

    @property
    def message(self) -> str:
        ...

    @overload
    def __init__(self, unmatched_value: typing.Any) -> None:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, inner_exception: System.Exception) -> None:
        ...

    @overload
    def __init__(self, message: str) -> None:
        ...

    @overload
    def __init__(self, message: str, inner_exception: System.Exception) -> None:
        ...

    def get_object_data(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """Obsoletions.LegacyFormatterImplMessage"""
        warnings.warn("Obsoletions.LegacyFormatterImplMessage", DeprecationWarning)


class InlineArray2(typing.Generic[System_Runtime_CompilerServices_InlineArray2_T]):
    """Represents an inline array of T with a fixed length of 2."""


class InlineArray3(typing.Generic[System_Runtime_CompilerServices_InlineArray3_T]):
    """Represents an inline array of T with a fixed length of 3."""


class InlineArray4(typing.Generic[System_Runtime_CompilerServices_InlineArray4_T]):
    """Represents an inline array of T with a fixed length of 4."""


class InlineArray5(typing.Generic[System_Runtime_CompilerServices_InlineArray5_T]):
    """Represents an inline array of T with a fixed length of 5."""


class InlineArray6(typing.Generic[System_Runtime_CompilerServices_InlineArray6_T]):
    """Represents an inline array of T with a fixed length of 6."""


class InlineArray7(typing.Generic[System_Runtime_CompilerServices_InlineArray7_T]):
    """Represents an inline array of T with a fixed length of 7."""


class InlineArray8(typing.Generic[System_Runtime_CompilerServices_InlineArray8_T]):
    """Represents an inline array of T with a fixed length of 8."""


class InlineArray9(typing.Generic[System_Runtime_CompilerServices_InlineArray9_T]):
    """Represents an inline array of T with a fixed length of 9."""


class InlineArray10(typing.Generic[System_Runtime_CompilerServices_InlineArray10_T]):
    """Represents an inline array of T with a fixed length of 10."""


class InlineArray11(typing.Generic[System_Runtime_CompilerServices_InlineArray11_T]):
    """Represents an inline array of T with a fixed length of 11."""


class InlineArray12(typing.Generic[System_Runtime_CompilerServices_InlineArray12_T]):
    """Represents an inline array of T with a fixed length of 12."""


class InlineArray13(typing.Generic[System_Runtime_CompilerServices_InlineArray13_T]):
    """Represents an inline array of T with a fixed length of 13."""


class InlineArray14(typing.Generic[System_Runtime_CompilerServices_InlineArray14_T]):
    """Represents an inline array of T with a fixed length of 14."""


class InlineArray15(typing.Generic[System_Runtime_CompilerServices_InlineArray15_T]):
    """Represents an inline array of T with a fixed length of 15."""


class InlineArray16(typing.Generic[System_Runtime_CompilerServices_InlineArray16_T]):
    """Represents an inline array of T with a fixed length of 16."""


class IsUnmanagedAttribute(System.Attribute):
    """
    Reserved for use by a compiler for tracking metadata.
    This attribute should not be used by developers in source code.
    """

    def __init__(self) -> None:
        """Initializes the attribute."""
        ...


class FixedBufferAttribute(System.Attribute):
    """Indicates that a field should be treated as containing a fixed number of elements of the specified primitive type."""

    @property
    def element_type(self) -> typing.Type:
        ...

    @property
    def length(self) -> int:
        ...

    def __init__(self, element_type: typing.Type, length: int) -> None:
        ...


class IsVolatile(System.Object):
    """This class has no documentation."""


class RuntimeHelpers(System.Object):
    """This class has no documentation."""

    OFFSET_TO_STRING_DATA: int
    """OffsetToStringData has been deprecated. Use string.GetPinnableReference() instead."""

    @staticmethod
    def allocate_type_associated_memory(type: typing.Type, size: int) -> System.IntPtr:
        ...

    @staticmethod
    def box(target: int, type: System.RuntimeTypeHandle) -> System.Object:
        """
        Create a boxed object of the specified type from the data located at the target reference.
        
        :param target: The target data
        :param type: The type of box to create.
        :returns: A boxed object containing the specified data.
        """
        ...

    def cleanup_code(self, user_data: typing.Any, exception_thrown: bool) -> None:
        ...

    @staticmethod
    def ensure_sufficient_execution_stack() -> None:
        ...

    @staticmethod
    def equals(o_1: typing.Any, o_2: typing.Any) -> bool:
        ...

    @staticmethod
    def execute_code_with_guaranteed_cleanup(code: typing.Callable[[System.Object], None], backout_code: typing.Callable[[System.Object, bool], None], user_data: typing.Any) -> None:
        """Obsoletions.ConstrainedExecutionRegionMessage"""
        warnings.warn("Obsoletions.ConstrainedExecutionRegionMessage", DeprecationWarning)

    @staticmethod
    def get_hash_code(o: typing.Any) -> int:
        ...

    @staticmethod
    def get_object_value(obj: typing.Any) -> System.Object:
        ...

    @staticmethod
    def get_uninitialized_object(type: typing.Type) -> System.Object:
        ...

    @staticmethod
    def initialize_array(array: System.Array, fld_handle: System.RuntimeFieldHandle) -> None:
        ...

    @staticmethod
    def prepare_constrained_regions() -> None:
        """Obsoletions.ConstrainedExecutionRegionMessage"""
        warnings.warn("Obsoletions.ConstrainedExecutionRegionMessage", DeprecationWarning)

    @staticmethod
    def prepare_constrained_regions_no_op() -> None:
        """Obsoletions.ConstrainedExecutionRegionMessage"""
        warnings.warn("Obsoletions.ConstrainedExecutionRegionMessage", DeprecationWarning)

    @staticmethod
    def prepare_contracted_delegate(d: System.Delegate) -> None:
        """Obsoletions.ConstrainedExecutionRegionMessage"""
        warnings.warn("Obsoletions.ConstrainedExecutionRegionMessage", DeprecationWarning)

    @staticmethod
    def prepare_delegate(d: System.Delegate) -> None:
        ...

    @staticmethod
    @overload
    def prepare_method(method: System.RuntimeMethodHandle) -> None:
        ...

    @staticmethod
    @overload
    def prepare_method(method: System.RuntimeMethodHandle, instantiation: typing.List[System.RuntimeTypeHandle]) -> None:
        ...

    @staticmethod
    def probe_for_sufficient_stack() -> None:
        """Obsoletions.ConstrainedExecutionRegionMessage"""
        warnings.warn("Obsoletions.ConstrainedExecutionRegionMessage", DeprecationWarning)

    @staticmethod
    def run_class_constructor(type: System.RuntimeTypeHandle) -> None:
        ...

    @staticmethod
    def run_module_constructor(module: System.ModuleHandle) -> None:
        ...

    @staticmethod
    def size_of(type: System.RuntimeTypeHandle) -> int:
        """
        Get the size of an object of the given type.
        
        :param type: The type to get the size of.
        :returns: The size of instances of the type.
        """
        ...

    def try_code(self, user_data: typing.Any) -> None:
        ...

    @staticmethod
    def try_ensure_sufficient_execution_stack() -> bool:
        ...


class NullableAttribute(System.Attribute):
    """
    Reserved for use by a compiler for tracking metadata.
    This attribute should not be used by developers in source code.
    """

    @property
    def nullable_flags(self) -> typing.List[int]:
        """Flags specifying metadata related to nullable reference types."""
        ...

    @nullable_flags.setter
    def nullable_flags(self, value: typing.List[int]) -> None:
        ...

    @overload
    def __init__(self, value: int) -> None:
        """
        Initializes the attribute.
        
        :param value: The flags value.
        """
        ...

    @overload
    def __init__(self, value: typing.List[int]) -> None:
        """
        Initializes the attribute.
        
        :param value: The flags value.
        """
        ...


class ScopedRefAttribute(System.Attribute):
    """
    Reserved for use by a compiler for tracking metadata.
    This attribute should not be used by developers in source code.
    """

    def __init__(self) -> None:
        """Initializes the attribute."""
        ...


class InterpolatedStringHandlerAttribute(System.Attribute):
    """Indicates the attributed type is to be used as an interpolated string handler."""

    def __init__(self) -> None:
        """Initializes the InterpolatedStringHandlerAttribute."""
        ...


class RequiresLocationAttribute(System.Attribute):
    """
    Reserved for use by a compiler for tracking metadata.
    This attribute should not be used by developers in source code.
    """

    def __init__(self) -> None:
        """Initializes the attribute."""
        ...


class IteratorStateMachineAttribute(System.Runtime.CompilerServices.StateMachineAttribute):
    """This class has no documentation."""

    def __init__(self, state_machine_type: typing.Type) -> None:
        ...


class ITuple(metaclass=abc.ABCMeta):
    """This interface is required for types that want to be indexed into by dynamic patterns."""

    @property
    @abc.abstractmethod
    def length(self) -> int:
        """The number of positions in this data structure."""
        ...

    def __getitem__(self, index: int) -> typing.Any:
        """Get the element at position ."""
        ...


class InlineArrayAttribute(System.Attribute):
    """Indicates that the instance's storage is sequentially replicated "length" times."""

    @property
    def length(self) -> int:
        """Gets the number of sequential fields to replicate in the inline array type."""
        ...

    def __init__(self, length: int) -> None:
        """
        Creates a new InlineArrayAttribute instance with the specified length.
        
        :param length: The number of sequential fields to replicate in the inline array type.
        """
        ...


class AsyncIteratorStateMachineAttribute(System.Runtime.CompilerServices.StateMachineAttribute):
    """Indicates whether a method is an asynchronous iterator."""

    def __init__(self, state_machine_type: typing.Type) -> None:
        """
        Initializes a new instance of the AsyncIteratorStateMachineAttribute class.
        
        :param state_machine_type: The type object for the underlying state machine type that's used to implement a state machine method.
        """
        ...


class ReferenceAssemblyAttribute(System.Attribute):
    """Identifies an assembly as a reference assembly, which contains metadata but no executable code."""

    @property
    def description(self) -> str:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, description: str) -> None:
        ...


class DependencyAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def dependent_assembly(self) -> str:
        ...

    @property
    def load_hint(self) -> System.Runtime.CompilerServices.LoadHint:
        ...

    def __init__(self, dependent_assembly_argument: str, load_hint_argument: System.Runtime.CompilerServices.LoadHint) -> None:
        ...


class _EventContainer(typing.Generic[System_Runtime_CompilerServices__EventContainer_Callable, System_Runtime_CompilerServices__EventContainer_ReturnType]):
    """This class is used to provide accurate autocomplete on events and cannot be imported."""

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> System_Runtime_CompilerServices__EventContainer_ReturnType:
        """Fires the event."""
        ...

    def __iadd__(self, item: System_Runtime_CompilerServices__EventContainer_Callable) -> typing.Self:
        """Registers an event handler."""
        ...

    def __isub__(self, item: System_Runtime_CompilerServices__EventContainer_Callable) -> typing.Self:
        """Unregisters an event handler."""
        ...


