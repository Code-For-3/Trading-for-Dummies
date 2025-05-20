from typing import overload
from enum import Enum
import abc
import datetime
import typing

import System
import System.Collections.Generic
import System.Runtime.CompilerServices
import System.Runtime.Serialization
import System.Threading
import System.Threading.Tasks
import System.Threading.Tasks.Sources

System_Threading_Tasks_Task = typing.Any
System_Threading_Tasks_ValueTask = typing.Any

System_Threading_Tasks_TaskCompletionSource_TResult = typing.TypeVar("System_Threading_Tasks_TaskCompletionSource_TResult")
System_Threading_Tasks_Task_TResult = typing.TypeVar("System_Threading_Tasks_Task_TResult")
System_Threading_Tasks_TaskFactory_TResult = typing.TypeVar("System_Threading_Tasks_TaskFactory_TResult")
System_Threading_Tasks_ValueTask_TResult = typing.TypeVar("System_Threading_Tasks_ValueTask_TResult")
System_Threading_Tasks__EventContainer_Callable = typing.TypeVar("System_Threading_Tasks__EventContainer_Callable")
System_Threading_Tasks__EventContainer_ReturnType = typing.TypeVar("System_Threading_Tasks__EventContainer_ReturnType")


class UnobservedTaskExceptionEventArgs(System.EventArgs):
    """
    Provides data for the event that is raised when a faulted Task's
    exception goes unobserved.
    """

    @property
    def observed(self) -> bool:
        """Gets whether this exception has been marked as "observed.\""""
        ...

    @property
    def exception(self) -> System.AggregateException:
        """The Exception that went unobserved."""
        ...

    def __init__(self, exception: System.AggregateException) -> None:
        """
        Initializes a new instance of the UnobservedTaskExceptionEventArgs class
        with the unobserved exception.
        
        :param exception: The Exception that has gone unobserved.
        """
        ...

    def set_observed(self) -> None:
        """
        Marks the Exception as "observed," thus preventing it
        from triggering exception escalation policy which, by default, terminates the process.
        """
        ...


class TaskScheduler(System.Object, metaclass=abc.ABCMeta):
    """Represents an abstract scheduler for tasks."""

    @property
    def maximum_concurrency_level(self) -> int:
        """
        Indicates the maximum concurrency level this
        TaskScheduler  is able to support.
        """
        ...

    DEFAULT: System.Threading.Tasks.TaskScheduler
    """Gets the default TaskScheduler instance."""

    CURRENT: System.Threading.Tasks.TaskScheduler
    """
    Gets the TaskScheduler
    associated with the currently executing task.
    """

    @property
    def id(self) -> int:
        """Gets the unique ID for this TaskScheduler."""
        ...

    unobserved_task_exception: _EventContainer[typing.Callable[[System.Object, System.Threading.Tasks.UnobservedTaskExceptionEventArgs], None], None]
    """
    Occurs when a faulted Task's unobserved exception is about to trigger exception escalation
    policy, which, by default, would terminate the process.
    """

    def __init__(self) -> None:
        """
        Initializes the TaskScheduler.
        
        This method is protected.
        """
        ...

    @staticmethod
    def from_current_synchronization_context() -> System.Threading.Tasks.TaskScheduler:
        """
        Creates a TaskScheduler
        associated with the current SynchronizationContext.
        
        :returns: A TaskScheduler associated with the current SynchronizationContext, as determined by SynchronizationContext.Current.
        """
        ...

    def get_scheduled_tasks(self) -> System.Collections.Generic.IEnumerable[System.Threading.Tasks.Task]:
        """
        Generates an enumerable of Task instances
        currently queued to the scheduler waiting to be executed.
        
        This method is protected.
        
        :returns: An enumerable that allows traversal of tasks currently queued to this scheduler.
        """
        ...

    def try_execute_task(self, task: System.Threading.Tasks.Task) -> bool:
        """
        Attempts to execute the provided Task
        on this scheduler.
        
        This method is protected.
        
        :param task: A Task object to be executed.
        :returns: A Boolean that is true if  was successfully executed, false if it was not. A common reason for execution failure is that the task had previously been executed or is in the process of being executed by another thread.
        """
        ...

    def try_execute_task_inline(self, task: System.Threading.Tasks.Task, task_was_previously_queued: bool) -> bool:
        """
        Determines whether the provided Task
        can be executed synchronously in this call, and if it can, executes it.
        
        This method is protected.
        
        :param task: The Task to be executed.
        :param task_was_previously_queued: A Boolean denoting whether or not task has previously been queued. If this parameter is True, then the task may have been previously queued (scheduled); if False, then the task is known not to have been queued, and this call is being made in order to execute the task inline without queueing it.
        :returns: A Boolean value indicating whether the task was executed inline.
        """
        ...


class ConfigureAwaitOptions(Enum):
    """Options to control behavior when awaiting."""

    NONE = ...
    """No options specified."""

    CONTINUE_ON_CAPTURED_CONTEXT = ...
    """
    Attempt to marshal the continuation back to the original SynchronizationContext or
    TaskScheduler present on the originating thread at the time of the await.
    """

    SUPPRESS_THROWING = ...
    """
    Avoids throwing an exception at the completion of awaiting a Task that ends
    in the TaskStatus.Faulted or TaskStatus.Canceled state.
    """

    FORCE_YIELDING = ...
    """
    Forces an await on an already completed Task to behave as if the Task
    wasn't yet completed, such that the current asynchronous method will be forced to yield its execution.
    """


class TaskAsyncEnumerableExtensions(System.Object):
    """Provides a set of static methods for configuring Task-related behaviors on asynchronous enumerables and disposables."""

    @staticmethod
    def configure_await(source: System.IAsyncDisposable, continue_on_captured_context: bool) -> System.Runtime.CompilerServices.ConfiguredAsyncDisposable:
        """
        Configures how awaits on the tasks returned from an async disposable will be performed.
        
        :param source: The source async disposable.
        :param continue_on_captured_context: true to capture and marshal back to the current context; otherwise, false.
        :returns: The configured async disposable.
        """
        ...


class TaskCreationOptions(Enum):
    """Specifies flags that control optional behavior for the creation and execution of tasks."""

    NONE = ...
    """Specifies that the default behavior should be used."""

    PREFER_FAIRNESS = ...
    """
    A hint to a TaskScheduler to schedule a
    task in as fair a manner as possible, meaning that tasks scheduled sooner will be more likely to
    be run sooner, and tasks scheduled later will be more likely to be run later.
    """

    LONG_RUNNING = ...
    """
    Specifies that a task will be a long-running, course-grained operation. It provides a hint to the
    TaskScheduler that oversubscription may be
    warranted.
    """

    ATTACHED_TO_PARENT = ...
    """Specifies that a task is attached to a parent in the task hierarchy."""

    DENY_CHILD_ATTACH = ...
    """Specifies that an InvalidOperationException will be thrown if an attempt is made to attach a child task to the created task."""

    HIDE_SCHEDULER = ...
    """
    Prevents the ambient scheduler from being seen as the current scheduler in the created task.  This means that operations
    like StartNew or ContinueWith that are performed in the created task will see TaskScheduler.Default as the current scheduler.
    """

    RUN_CONTINUATIONS_ASYNCHRONOUSLY = ...
    """
    Forces continuations added to the current task to be executed asynchronously.
    This option has precedence over TaskContinuationOptions.ExecuteSynchronously
    """


class TaskCompletionSource(typing.Generic[System_Threading_Tasks_TaskCompletionSource_TResult], System.Object):
    """
    Represents the producer side of a Task{TResult} unbound to a
    delegate, providing access to the consumer side through the Task property.
    """

    @property
    def task(self) -> System.Threading.Tasks.Task:
        """
        Gets the Tasks.Task created
        by this TaskCompletionSource.
        """
        ...

    @overload
    def __init__(self, state: typing.Any) -> None:
        """
        Creates a TaskCompletionSource with the specified state.
        
        :param state: The state to use as the underlying Tasks.Task's AsyncState.
        """
        ...

    @overload
    def __init__(self, state: typing.Any, creation_options: System.Threading.Tasks.TaskCreationOptions) -> None:
        """
        Creates a TaskCompletionSource with the specified state and options.
        
        :param state: The state to use as the underlying Tasks.Task's AsyncState.
        :param creation_options: The options to use when creating the underlying Tasks.Task.
        """
        ...

    @overload
    def __init__(self) -> None:
        """Creates a TaskCompletionSource."""
        ...

    @overload
    def __init__(self, creation_options: System.Threading.Tasks.TaskCreationOptions) -> None:
        """
        Creates a TaskCompletionSource with the specified options.
        
        :param creation_options: The options to use when creating the underlying Tasks.Task.
        """
        ...

    @overload
    def set_canceled(self) -> None:
        """Transitions the underlying Tasks.Task into the TaskStatus.Canceled state."""
        ...

    @overload
    def set_canceled(self, cancellation_token: System.Threading.CancellationToken) -> None:
        """
        Transitions the underlying Tasks.Task into the TaskStatus.Canceled state
        using the specified token.
        
        :param cancellation_token: The cancellation token with which to cancel the Tasks.Task.
        """
        ...

    @overload
    def set_exception(self, exception: System.Exception) -> None:
        """
        Transitions the underlying Tasks.Task into the TaskStatus.Faulted state.
        
        :param exception: The exception to bind to this Tasks.Task.
        """
        ...

    @overload
    def set_exception(self, exceptions: System.Collections.Generic.IEnumerable[System.Exception]) -> None:
        """
        Transitions the underlying Tasks.Task into the TaskStatus.Faulted state.
        
        :param exceptions: The collection of exceptions to bind to this Tasks.Task.
        """
        ...

    @overload
    def set_from_task(self, completed_task: System.Threading.Tasks.Task) -> None:
        """
        Transition the underlying Task{TResult} into the same completion state as the specified .
        
        :param completed_task: The completed task whose completion status (including exception or cancellation information) should be copied to the underlying task.
        """
        ...

    @overload
    def set_from_task(self, completed_task: System.Threading.Tasks.Task[System_Threading_Tasks_TaskCompletionSource_TResult]) -> None:
        """
        Transition the underlying Task{TResult} into the same completion state as the specified .
        
        :param completed_task: The completed task whose completion status (including result, exception, or cancellation information) should be copied to the underlying task.
        """
        ...

    @overload
    def set_result(self) -> None:
        """Transitions the underlying Tasks.Task into the TaskStatus.RanToCompletion state."""
        ...

    @overload
    def set_result(self, result: System_Threading_Tasks_TaskCompletionSource_TResult) -> None:
        """
        Transitions the underlying Task{TResult} into the TaskStatus.RanToCompletion state.
        
        :param result: The result value to bind to this Task{TResult}.
        """
        ...

    @overload
    def try_set_canceled(self) -> bool:
        """
        Attempts to transition the underlying Tasks.Task into the TaskStatus.Canceled state.
        
        :returns: True if the operation was successful; otherwise, false.
        """
        ...

    @overload
    def try_set_canceled(self, cancellation_token: System.Threading.CancellationToken) -> bool:
        """
        Attempts to transition the underlying Tasks.Task into the TaskStatus.Canceled state.
        
        :param cancellation_token: The cancellation token with which to cancel the Tasks.Task.
        :returns: True if the operation was successful; otherwise, false.
        """
        ...

    @overload
    def try_set_exception(self, exception: System.Exception) -> bool:
        """
        Attempts to transition the underlying Tasks.Task into the TaskStatus.Faulted state.
        
        :param exception: The exception to bind to this Tasks.Task.
        :returns: True if the operation was successful; otherwise, false.
        """
        ...

    @overload
    def try_set_exception(self, exceptions: System.Collections.Generic.IEnumerable[System.Exception]) -> bool:
        """
        Attempts to transition the underlying Tasks.Task into the TaskStatus.Faulted state.
        
        :param exceptions: The collection of exceptions to bind to this Tasks.Task.
        :returns: True if the operation was successful; otherwise, false.
        """
        ...

    @overload
    def try_set_from_task(self, completed_task: System.Threading.Tasks.Task) -> bool:
        """
        Attempts to transition the underlying Task{TResult} into the same completion state as the specified .
        
        :param completed_task: The completed task whose completion status (including exception or cancellation information) should be copied to the underlying task.
        :returns: true if the operation was successful; otherwise, false.
        """
        ...

    @overload
    def try_set_from_task(self, completed_task: System.Threading.Tasks.Task[System_Threading_Tasks_TaskCompletionSource_TResult]) -> bool:
        """
        Attempts to transition the underlying Task{TResult} into the same completion state as the specified .
        
        :param completed_task: The completed task whose completion status (including result, exception, or cancellation information) should be copied to the underlying task.
        :returns: true if the operation was successful; otherwise, false.
        """
        ...

    @overload
    def try_set_result(self) -> bool:
        """
        Attempts to transition the underlying Tasks.Task into the TaskStatus.RanToCompletion state.
        
        :returns: True if the operation was successful; otherwise, false.
        """
        ...

    @overload
    def try_set_result(self, result: System_Threading_Tasks_TaskCompletionSource_TResult) -> bool:
        """
        Attempts to transition the underlying Task{TResult} into the TaskStatus.RanToCompletion state.
        
        :param result: The result value to bind to this Task{TResult}.
        :returns: True if the operation was successful; otherwise, false.
        """
        ...


class TaskSchedulerException(System.Exception):
    """
    Represents an exception used to communicate an invalid operation by a
    TaskScheduler.
    """

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the TaskSchedulerException class."""
        ...

    @overload
    def __init__(self, message: str) -> None:
        """
        Initializes a new instance of the TaskSchedulerException
        class with a specified error message.
        
        :param message: The error message that explains the reason for the exception.
        """
        ...

    @overload
    def __init__(self, inner_exception: System.Exception) -> None:
        """
        Initializes a new instance of the TaskSchedulerException
        class using the default error message and a reference to the inner exception that is the cause of
        this exception.
        
        :param inner_exception: The exception that is the cause of the current exception.
        """
        ...

    @overload
    def __init__(self, message: str, inner_exception: System.Exception) -> None:
        """
        Initializes a new instance of the TaskSchedulerException
        class with a specified error message and a reference to the inner exception that is the cause of
        this exception.
        
        :param message: The error message that explains the reason for the exception.
        :param inner_exception: The exception that is the cause of the current exception.
        """
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """
        Initializes a new instance of the TaskSchedulerException
        class with serialized data.
        
        This method is protected.
        
        Obsoletions.LegacyFormatterImplMessage
        
        :param info: The SerializationInfo that holds the serialized object data about the exception being thrown.
        :param context: The StreamingContext that contains contextual information about the source or destination.
        """
        ...


class TaskStatus(Enum):
    """Represents the current stage in the lifecycle of a Task."""

    CREATED = 0
    """The task has been initialized but has not yet been scheduled."""

    WAITING_FOR_ACTIVATION = 1
    """The task is waiting to be activated and scheduled internally by the .NET Framework infrastructure."""

    WAITING_TO_RUN = 2
    """The task has been scheduled for execution but has not yet begun executing."""

    RUNNING = 3
    """The task is running but has not yet completed."""

    WAITING_FOR_CHILDREN_TO_COMPLETE = 4
    """
    The task has finished executing and is implicitly waiting for
    attached child tasks to complete.
    """

    RAN_TO_COMPLETION = 5
    """The task completed execution successfully."""

    CANCELED = 6
    """
    The task acknowledged cancellation by throwing an OperationCanceledException with its own CancellationToken
    while the token was in signaled state, or the task's CancellationToken was already signaled before the
    task started executing.
    """

    FAULTED = 7
    """The task completed due to an unhandled exception."""


class TaskContinuationOptions(Enum):
    """Specifies flags that control optional behavior for the creation and execution of continuation tasks."""

    NONE = 0
    """
    Default = "Continue on any, no task options, run asynchronously"
    Specifies that the default behavior should be used.  Continuations, by default, will
    be scheduled when the antecedent task completes, regardless of the task's final TaskStatus.
    """

    PREFER_FAIRNESS = ...
    """
    A hint to a TaskScheduler to schedule a
    task in as fair a manner as possible, meaning that tasks scheduled sooner will be more likely to
    be run sooner, and tasks scheduled later will be more likely to be run later.
    """

    LONG_RUNNING = ...
    """
    Specifies that a task will be a long-running, coarse-grained operation.  It provides
    a hint to the TaskScheduler that
    oversubscription may be warranted.
    """

    ATTACHED_TO_PARENT = ...
    """Specifies that a task is attached to a parent in the task hierarchy."""

    DENY_CHILD_ATTACH = ...
    """Specifies that an InvalidOperationException will be thrown if an attempt is made to attach a child task to the created task."""

    HIDE_SCHEDULER = ...
    """
    Prevents the ambient scheduler from being seen as the current scheduler in the created task.  This means that operations
    like StartNew or ContinueWith that are performed in the created task will see TaskScheduler.Default as the current scheduler.
    """

    LAZY_CANCELLATION = ...
    """In the case of continuation cancellation, prevents completion of the continuation until the antecedent has completed."""

    RUN_CONTINUATIONS_ASYNCHRONOUSLY = ...

    NOT_ON_RAN_TO_COMPLETION = ...
    """
    Specifies that the continuation task should not be scheduled if its antecedent ran to completion.
    This option is not valid for multi-task continuations.
    """

    NOT_ON_FAULTED = ...
    """
    Specifies that the continuation task should not be scheduled if its antecedent threw an unhandled
    exception. This option is not valid for multi-task continuations.
    """

    NOT_ON_CANCELED = ...
    """
    Specifies that the continuation task should not be scheduled if its antecedent was canceled. This
    option is not valid for multi-task continuations.
    """

    ONLY_ON_RAN_TO_COMPLETION = ...
    """
    Specifies that the continuation task should be scheduled only if its antecedent ran to
    completion. This option is not valid for multi-task continuations.
    """

    ONLY_ON_FAULTED = ...
    """
    Specifies that the continuation task should be scheduled only if its antecedent threw an
    unhandled exception. This option is not valid for multi-task continuations.
    """

    ONLY_ON_CANCELED = ...
    """
    Specifies that the continuation task should be scheduled only if its antecedent was canceled.
    This option is not valid for multi-task continuations.
    """

    EXECUTE_SYNCHRONOUSLY = ...
    """
    Specifies that the continuation task should be executed synchronously. With this option
    specified, the continuation will be run on the same thread that causes the antecedent task to
    transition into its final state. If the antecedent is already complete when the continuation is
    created, the continuation will run on the thread creating the continuation.  Only very
    short-running continuations should be executed synchronously.
    """


class Task(typing.Generic[System_Threading_Tasks_Task_TResult], System_Threading_Tasks_Task):
    """Represents an asynchronous operation that produces a result at some time in the future."""

    @property
    def id(self) -> int:
        """Gets a unique ID for this Task instance."""
        ...

    CURRENT_ID: typing.Optional[int]
    """Returns the unique ID of the currently executing Task."""

    @property
    def exception(self) -> System.AggregateException:
        """
        Gets the AggregateException that caused the Task to end prematurely. If the Task completed successfully or has not yet thrown any
        exceptions, this will return null.
        """
        ...

    @property
    def status(self) -> System.Threading.Tasks.TaskStatus:
        """Gets the TaskStatus of this Task."""
        ...

    @property
    def is_canceled(self) -> bool:
        """
        Gets whether this Task instance has completed
        execution due to being canceled.
        """
        ...

    @property
    def is_completed(self) -> bool:
        """Gets whether this Task has completed."""
        ...

    @property
    def is_completed_successfully(self) -> bool:
        ...

    @property
    def creation_options(self) -> System.Threading.Tasks.TaskCreationOptions:
        """
        Gets the TaskCreationOptions used
        to create this task.
        """
        ...

    @property
    def async_state(self) -> System.Object:
        """
        Gets the state object supplied when the Task was created,
        or null if none was supplied.
        """
        ...

    FACTORY: System.Threading.Tasks.TaskFactory
    """Provides access to factory methods for creating Task and Task{TResult} instances."""

    COMPLETED_TASK: System.Threading.Tasks.Task
    """Gets a task that's already been completed successfully."""

    @property
    def is_faulted(self) -> bool:
        """Gets whether the Task completed due to an unhandled exception."""
        ...

    @property
    def result(self) -> System_Threading_Tasks_Task_TResult:
        """Gets the result value of this Task{TResult}."""
        ...

    @overload
    def __init__(self, action: typing.Callable[[System.Object], None], state: typing.Any) -> None:
        """
        Initializes a new Task with the specified action and state.
        
        :param action: The delegate that represents the code to execute in the task.
        :param state: An object representing data to be used by the action.
        """
        ...

    @overload
    def __init__(self, action: typing.Callable[[System.Object], None], state: typing.Any, cancellation_token: System.Threading.CancellationToken) -> None:
        """
        Initializes a new Task with the specified action, state, and options.
        
        :param action: The delegate that represents the code to execute in the task.
        :param state: An object representing data to be used by the action.
        :param cancellation_token: The CancellationToken that will be assigned to the new task.
        """
        ...

    @overload
    def __init__(self, action: typing.Callable[[System.Object], None], state: typing.Any, creation_options: System.Threading.Tasks.TaskCreationOptions) -> None:
        """
        Initializes a new Task with the specified action, state, and options.
        
        :param action: The delegate that represents the code to execute in the task.
        :param state: An object representing data to be used by the action.
        :param creation_options: The TaskCreationOptions used to customize the Task's behavior.
        """
        ...

    @overload
    def __init__(self, action: typing.Callable[[System.Object], None], state: typing.Any, cancellation_token: System.Threading.CancellationToken, creation_options: System.Threading.Tasks.TaskCreationOptions) -> None:
        """
        Initializes a new Task with the specified action, state, and options.
        
        :param action: The delegate that represents the code to execute in the task.
        :param state: An object representing data to be used by the action.
        :param cancellation_token: The CancellationToken that will be assigned to the new task.
        :param creation_options: The TaskCreationOptions used to customize the Task's behavior.
        """
        ...

    @overload
    def __init__(self, function: typing.Callable[[System.Object], System_Threading_Tasks_Task_TResult], state: typing.Any) -> None:
        """
        Initializes a new Task{TResult} with the specified function and state.
        
        :param function: The delegate that represents the code to execute in the task. When the function has completed, the task's Result property will be set to return the result value of the function.
        :param state: An object representing data to be used by the action.
        """
        ...

    @overload
    def __init__(self, function: typing.Callable[[System.Object], System_Threading_Tasks_Task_TResult], state: typing.Any, cancellation_token: System.Threading.CancellationToken) -> None:
        """
        Initializes a new Task{TResult} with the specified action, state, and options.
        
        :param function: The delegate that represents the code to execute in the task. When the function has completed, the task's Result property will be set to return the result value of the function.
        :param state: An object representing data to be used by the function.
        :param cancellation_token: The CancellationToken to be assigned to the new task.
        """
        ...

    @overload
    def __init__(self, function: typing.Callable[[System.Object], System_Threading_Tasks_Task_TResult], state: typing.Any, creation_options: System.Threading.Tasks.TaskCreationOptions) -> None:
        """
        Initializes a new Task{TResult} with the specified action, state, and options.
        
        :param function: The delegate that represents the code to execute in the task. When the function has completed, the task's Result property will be set to return the result value of the function.
        :param state: An object representing data to be used by the function.
        :param creation_options: The TaskCreationOptions used to customize the task's behavior.
        """
        ...

    @overload
    def __init__(self, function: typing.Callable[[System.Object], System_Threading_Tasks_Task_TResult], state: typing.Any, cancellation_token: System.Threading.CancellationToken, creation_options: System.Threading.Tasks.TaskCreationOptions) -> None:
        """
        Initializes a new Task{TResult} with the specified action, state, and options.
        
        :param function: The delegate that represents the code to execute in the task. When the function has completed, the task's Result property will be set to return the result value of the function.
        :param state: An object representing data to be used by the function.
        :param cancellation_token: The CancellationToken to be assigned to the new task.
        :param creation_options: The TaskCreationOptions used to customize the task's behavior.
        """
        ...

    @overload
    def __init__(self, action: typing.Callable[[], None]) -> None:
        """
        Initializes a new Task with the specified action.
        
        :param action: The delegate that represents the code to execute in the Task.
        """
        ...

    @overload
    def __init__(self, action: typing.Callable[[], None], cancellation_token: System.Threading.CancellationToken) -> None:
        """
        Initializes a new Task with the specified action and Threading.CancellationToken.
        
        :param action: The delegate that represents the code to execute in the Task.
        :param cancellation_token: The Threading.CancellationToken that will be assigned to the new Task.
        """
        ...

    @overload
    def __init__(self, action: typing.Callable[[], None], creation_options: System.Threading.Tasks.TaskCreationOptions) -> None:
        """
        Initializes a new Task with the specified action and creation options.
        
        :param action: The delegate that represents the code to execute in the task.
        :param creation_options: The TaskCreationOptions used to customize the Task's behavior.
        """
        ...

    @overload
    def __init__(self, action: typing.Callable[[], None], cancellation_token: System.Threading.CancellationToken, creation_options: System.Threading.Tasks.TaskCreationOptions) -> None:
        """
        Initializes a new Task with the specified action and creation options.
        
        :param action: The delegate that represents the code to execute in the task.
        :param cancellation_token: The CancellationToken that will be assigned to the new task.
        :param creation_options: The TaskCreationOptions used to customize the Task's behavior.
        """
        ...

    @overload
    def __init__(self, function: typing.Callable[[], System_Threading_Tasks_Task_TResult]) -> None:
        """
        Initializes a new Task{TResult} with the specified function.
        
        :param function: The delegate that represents the code to execute in the task. When the function has completed, the task's Result property will be set to return the result value of the function.
        """
        ...

    @overload
    def __init__(self, function: typing.Callable[[], System_Threading_Tasks_Task_TResult], cancellation_token: System.Threading.CancellationToken) -> None:
        """
        Initializes a new Task{TResult} with the specified function.
        
        :param function: The delegate that represents the code to execute in the task. When the function has completed, the task's Result property will be set to return the result value of the function.
        :param cancellation_token: The CancellationToken to be assigned to this task.
        """
        ...

    @overload
    def __init__(self, function: typing.Callable[[], System_Threading_Tasks_Task_TResult], creation_options: System.Threading.Tasks.TaskCreationOptions) -> None:
        """
        Initializes a new Task{TResult} with the specified function and creation options.
        
        :param function: The delegate that represents the code to execute in the task. When the function has completed, the task's Result property will be set to return the result value of the function.
        :param creation_options: The TaskCreationOptions used to customize the task's behavior.
        """
        ...

    @overload
    def __init__(self, function: typing.Callable[[], System_Threading_Tasks_Task_TResult], cancellation_token: System.Threading.CancellationToken, creation_options: System.Threading.Tasks.TaskCreationOptions) -> None:
        """
        Initializes a new Task{TResult} with the specified function and creation options.
        
        :param function: The delegate that represents the code to execute in the task. When the function has completed, the task's Result property will be set to return the result value of the function.
        :param cancellation_token: The CancellationToken that will be assigned to the new task.
        :param creation_options: The TaskCreationOptions used to customize the task's behavior.
        """
        ...

    @overload
    def configure_await(self, continue_on_captured_context: bool) -> System.Runtime.CompilerServices.ConfiguredTaskAwaitable:
        """
        Configures an awaiter used to await this Task.
        
        :param continue_on_captured_context: true to attempt to marshal the continuation back to the original context captured; otherwise, false.
        :returns: An object used to await this task.
        """
        ...

    @overload
    def configure_await(self, options: System.Threading.Tasks.ConfigureAwaitOptions) -> System.Runtime.CompilerServices.ConfiguredTaskAwaitable:
        """
        Configures an awaiter used to await this Task.
        
        :param options: Options used to configure how awaits on this task are performed.
        :returns: An object used to await this task.
        """
        ...

    @overload
    def continue_with(self, continuation_action: typing.Callable[[System.Threading.Tasks.Task, System.Object], None], state: typing.Any) -> System.Threading.Tasks.Task:
        """
        Creates a continuation that executes when the target Task completes.
        
        :param continuation_action: An action to run when the Task completes. When run, the delegate will be passed the completed task as and the caller-supplied state object as arguments.
        :param state: An object representing data to be used by the continuation action.
        :returns: A new continuation Task.
        """
        ...

    @overload
    def continue_with(self, continuation_action: typing.Callable[[System.Threading.Tasks.Task, System.Object], None], state: typing.Any, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        """
        Creates a continuation that executes when the target Task completes.
        
        :param continuation_action: An action to run when the Task completes. When run, the delegate will be passed the completed task and the caller-supplied state object as arguments.
        :param state: An object representing data to be used by the continuation action.
        :param cancellation_token: The CancellationToken that will be assigned to the new continuation task.
        :returns: A new continuation Task.
        """
        ...

    @overload
    def continue_with(self, continuation_action: typing.Callable[[System.Threading.Tasks.Task, System.Object], None], state: typing.Any, scheduler: System.Threading.Tasks.TaskScheduler) -> System.Threading.Tasks.Task:
        """
        Creates a continuation that executes when the target Task completes.
        
        :param continuation_action: An action to run when the Task completes.  When run, the delegate will be passed the completed task and the caller-supplied state object as arguments.
        :param state: An object representing data to be used by the continuation action.
        :param scheduler: The TaskScheduler to associate with the continuation task and to use for its execution.
        :returns: A new continuation Task.
        """
        ...

    @overload
    def continue_with(self, continuation_action: typing.Callable[[System.Threading.Tasks.Task, System.Object], None], state: typing.Any, continuation_options: System.Threading.Tasks.TaskContinuationOptions) -> System.Threading.Tasks.Task:
        """
        Creates a continuation that executes when the target Task completes.
        
        :param continuation_action: An action to run when the Task completes. When run, the delegate will be passed the completed task and the caller-supplied state object as arguments.
        :param state: An object representing data to be used by the continuation action.
        :param continuation_options: Options for when the continuation is scheduled and how it behaves. This includes criteria, such as TaskContinuationOptions.OnlyOnCanceled, as well as execution options, such as TaskContinuationOptions.ExecuteSynchronously.
        :returns: A new continuation Task.
        """
        ...

    @overload
    def continue_with(self, continuation_action: typing.Callable[[System.Threading.Tasks.Task, System.Object], None], state: typing.Any, cancellation_token: System.Threading.CancellationToken, continuation_options: System.Threading.Tasks.TaskContinuationOptions, scheduler: System.Threading.Tasks.TaskScheduler) -> System.Threading.Tasks.Task:
        """
        Creates a continuation that executes when the target Task completes.
        
        :param continuation_action: An action to run when the Task completes. When run, the delegate will be passed the completed task and the caller-supplied state object as arguments.
        :param state: An object representing data to be used by the continuation action.
        :param cancellation_token: The CancellationToken that will be assigned to the new continuation task.
        :param continuation_options: Options for when the continuation is scheduled and how it behaves. This includes criteria, such as TaskContinuationOptions.OnlyOnCanceled, as well as execution options, such as TaskContinuationOptions.ExecuteSynchronously.
        :param scheduler: The TaskScheduler to associate with the continuation task and to use for its execution.
        :returns: A new continuation Task.
        """
        ...

    @overload
    def continue_with(self, continuation_action: typing.Callable[[System.Threading.Tasks.Task[System_Threading_Tasks_Task_TResult], System.Object], None], state: typing.Any) -> System.Threading.Tasks.Task:
        """
        Creates a continuation that executes when the target Task{TResult} completes.
        
        :param continuation_action: An action to run when the Task{TResult} completes. When run, the delegate will be passed the completed task and the caller-supplied state object as arguments.
        :param state: An object representing data to be used by the continuation action.
        :returns: A new continuation Task.
        """
        ...

    @overload
    def continue_with(self, continuation_action: typing.Callable[[System.Threading.Tasks.Task[System_Threading_Tasks_Task_TResult], System.Object], None], state: typing.Any, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        """
        Creates a continuation that executes when the target Task{TResult} completes.
        
        :param continuation_action: An action to run when the Task{TResult} completes. When run, the delegate will be passed the completed task and the caller-supplied state object as arguments.
        :param state: An object representing data to be used by the continuation action.
        :param cancellation_token: The CancellationToken that will be assigned to the new continuation task.
        :returns: A new continuation Task.
        """
        ...

    @overload
    def continue_with(self, continuation_action: typing.Callable[[System.Threading.Tasks.Task[System_Threading_Tasks_Task_TResult], System.Object], None], state: typing.Any, scheduler: System.Threading.Tasks.TaskScheduler) -> System.Threading.Tasks.Task:
        """
        Creates a continuation that executes when the target Task{TResult} completes.
        
        :param continuation_action: An action to run when the Task{TResult} completes. When run, the delegate will be passed the completed task and the caller-supplied state object as arguments.
        :param state: An object representing data to be used by the continuation action.
        :param scheduler: The TaskScheduler to associate with the continuation task and to use for its execution.
        :returns: A new continuation Task.
        """
        ...

    @overload
    def continue_with(self, continuation_action: typing.Callable[[System.Threading.Tasks.Task[System_Threading_Tasks_Task_TResult], System.Object], None], state: typing.Any, continuation_options: System.Threading.Tasks.TaskContinuationOptions) -> System.Threading.Tasks.Task:
        """
        Creates a continuation that executes when the target Task{TResult} completes.
        
        :param continuation_action: An action to run when the Task{TResult} completes. When run, the delegate will be passed the completed task and the caller-supplied state object as arguments.
        :param state: An object representing data to be used by the continuation action.
        :param continuation_options: Options for when the continuation is scheduled and how it behaves. This includes criteria, such as TaskContinuationOptions.OnlyOnCanceled, as well as execution options, such as TaskContinuationOptions.ExecuteSynchronously.
        :returns: A new continuation Task.
        """
        ...

    @overload
    def continue_with(self, continuation_action: typing.Callable[[System.Threading.Tasks.Task[System_Threading_Tasks_Task_TResult], System.Object], None], state: typing.Any, cancellation_token: System.Threading.CancellationToken, continuation_options: System.Threading.Tasks.TaskContinuationOptions, scheduler: System.Threading.Tasks.TaskScheduler) -> System.Threading.Tasks.Task:
        """
        Creates a continuation that executes when the target Task{TResult} completes.
        
        :param continuation_action: An action to run when the Task{TResult} completes. When run, the delegate will be passed the completed task and the caller-supplied state object as arguments.
        :param state: An object representing data to be used by the continuation action.
        :param cancellation_token: The CancellationToken that will be assigned to the new continuation task.
        :param continuation_options: Options for when the continuation is scheduled and how it behaves. This includes criteria, such as TaskContinuationOptions.OnlyOnCanceled, as well as execution options, such as TaskContinuationOptions.ExecuteSynchronously.
        :param scheduler: The TaskScheduler to associate with the continuation task and to use for its execution.
        :returns: A new continuation Task.
        """
        ...

    @overload
    def continue_with(self, continuation_action: typing.Callable[[System.Threading.Tasks.Task], None]) -> System.Threading.Tasks.Task:
        ...

    @overload
    def continue_with(self, continuation_action: typing.Callable[[System.Threading.Tasks.Task], None], cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        """
        Creates a continuation that executes when the target Task completes.
        
        :param continuation_action: An action to run when the Task completes. When run, the delegate will be passed the completed task as an argument.
        :param cancellation_token: The CancellationToken that will be assigned to the new continuation task.
        :returns: A new continuation Task.
        """
        ...

    @overload
    def continue_with(self, continuation_action: typing.Callable[[System.Threading.Tasks.Task], None], scheduler: System.Threading.Tasks.TaskScheduler) -> System.Threading.Tasks.Task:
        """
        Creates a continuation that executes when the target Task completes.
        
        :param continuation_action: An action to run when the Task completes.  When run, the delegate will be passed the completed task as an argument.
        :param scheduler: The TaskScheduler to associate with the continuation task and to use for its execution.
        :returns: A new continuation Task.
        """
        ...

    @overload
    def continue_with(self, continuation_action: typing.Callable[[System.Threading.Tasks.Task], None], continuation_options: System.Threading.Tasks.TaskContinuationOptions) -> System.Threading.Tasks.Task:
        """
        Creates a continuation that executes when the target Task completes.
        
        :param continuation_action: An action to run when the Task completes. When run, the delegate will be passed the completed task as an argument.
        :param continuation_options: Options for when the continuation is scheduled and how it behaves. This includes criteria, such as TaskContinuationOptions.OnlyOnCanceled, as well as execution options, such as TaskContinuationOptions.ExecuteSynchronously.
        :returns: A new continuation Task.
        """
        ...

    @overload
    def continue_with(self, continuation_action: typing.Callable[[System.Threading.Tasks.Task], None], cancellation_token: System.Threading.CancellationToken, continuation_options: System.Threading.Tasks.TaskContinuationOptions, scheduler: System.Threading.Tasks.TaskScheduler) -> System.Threading.Tasks.Task:
        """
        Creates a continuation that executes when the target Task completes.
        
        :param continuation_action: An action to run when the Task completes. When run, the delegate will be passed the completed task as an argument.
        :param cancellation_token: The CancellationToken that will be assigned to the new continuation task.
        :param continuation_options: Options for when the continuation is scheduled and how it behaves. This includes criteria, such as TaskContinuationOptions.OnlyOnCanceled, as well as execution options, such as TaskContinuationOptions.ExecuteSynchronously.
        :param scheduler: The TaskScheduler to associate with the continuation task and to use for its execution.
        :returns: A new continuation Task.
        """
        ...

    @overload
    def continue_with(self, continuation_action: typing.Callable[[System.Threading.Tasks.Task[System_Threading_Tasks_Task_TResult]], None]) -> System.Threading.Tasks.Task:
        """
        Creates a continuation that executes when the target Task{TResult} completes.
        
        :param continuation_action: An action to run when the Task{TResult} completes. When run, the delegate will be passed the completed task as an argument.
        :returns: A new continuation Task.
        """
        ...

    @overload
    def continue_with(self, continuation_action: typing.Callable[[System.Threading.Tasks.Task[System_Threading_Tasks_Task_TResult]], None], cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        """
        Creates a continuation that executes when the target Task{TResult} completes.
        
        :param continuation_action: An action to run when the Task{TResult} completes. When run, the delegate will be passed the completed task as an argument.
        :param cancellation_token: The CancellationToken that will be assigned to the new continuation task.
        :returns: A new continuation Task.
        """
        ...

    @overload
    def continue_with(self, continuation_action: typing.Callable[[System.Threading.Tasks.Task[System_Threading_Tasks_Task_TResult]], None], scheduler: System.Threading.Tasks.TaskScheduler) -> System.Threading.Tasks.Task:
        """
        Creates a continuation that executes when the target Task{TResult} completes.
        
        :param continuation_action: An action to run when the Task{TResult} completes. When run, the delegate will be passed the completed task as an argument.
        :param scheduler: The TaskScheduler to associate with the continuation task and to use for its execution.
        :returns: A new continuation Task.
        """
        ...

    @overload
    def continue_with(self, continuation_action: typing.Callable[[System.Threading.Tasks.Task[System_Threading_Tasks_Task_TResult]], None], continuation_options: System.Threading.Tasks.TaskContinuationOptions) -> System.Threading.Tasks.Task:
        """
        Creates a continuation that executes when the target Task{TResult} completes.
        
        :param continuation_action: An action to run when the Task{TResult} completes. When run, the delegate will be passed the completed task as an argument.
        :param continuation_options: Options for when the continuation is scheduled and how it behaves. This includes criteria, such as TaskContinuationOptions.OnlyOnCanceled, as well as execution options, such as TaskContinuationOptions.ExecuteSynchronously.
        :returns: A new continuation Task.
        """
        ...

    @overload
    def continue_with(self, continuation_action: typing.Callable[[System.Threading.Tasks.Task[System_Threading_Tasks_Task_TResult]], None], cancellation_token: System.Threading.CancellationToken, continuation_options: System.Threading.Tasks.TaskContinuationOptions, scheduler: System.Threading.Tasks.TaskScheduler) -> System.Threading.Tasks.Task:
        """
        Creates a continuation that executes when the target Task{TResult} completes.
        
        :param continuation_action: An action to run when the Task{TResult} completes. When run, the delegate will be passed the completed task as an argument.
        :param cancellation_token: The CancellationToken that will be assigned to the new continuation task.
        :param continuation_options: Options for when the continuation is scheduled and how it behaves. This includes criteria, such as TaskContinuationOptions.OnlyOnCanceled, as well as execution options, such as TaskContinuationOptions.ExecuteSynchronously.
        :param scheduler: The TaskScheduler to associate with the continuation task and to use for its execution.
        :returns: A new continuation Task.
        """
        ...

    @staticmethod
    @overload
    def delay(delay: datetime.timedelta) -> System.Threading.Tasks.Task:
        """
        Creates a Task that will complete after a time delay.
        
        :param delay: The time span to wait before completing the returned Task
        :returns: A Task that represents the time delay.
        """
        ...

    @staticmethod
    @overload
    def delay(delay: datetime.timedelta, time_provider: System.TimeProvider) -> System.Threading.Tasks.Task:
        """
        Creates a task that completes after a specified time interval.
        
        :param delay: The TimeSpan to wait before completing the returned task, or Timeout.InfiniteTimeSpan to wait indefinitely.
        :param time_provider: The TimeProvider with which to interpret .
        :returns: A task that represents the time delay.
        """
        ...

    @staticmethod
    @overload
    def delay(delay: datetime.timedelta, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        """
        Creates a Task that will complete after a time delay.
        
        :param delay: The time span to wait before completing the returned Task
        :param cancellation_token: The cancellation token that will be checked prior to completing the returned Task
        :returns: A Task that represents the time delay.
        """
        ...

    @staticmethod
    @overload
    def delay(delay: datetime.timedelta, time_provider: System.TimeProvider, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        """
        Creates a cancellable task that completes after a specified time interval.
        
        :param delay: The TimeSpan to wait before completing the returned task, or Timeout.InfiniteTimeSpan to wait indefinitely.
        :param time_provider: The TimeProvider with which to interpret .
        :param cancellation_token: A cancellation token to observe while waiting for the task to complete.
        :returns: A task that represents the time delay.
        """
        ...

    @staticmethod
    @overload
    def delay(milliseconds_delay: int) -> System.Threading.Tasks.Task:
        """
        Creates a Task that will complete after a time delay.
        
        :param milliseconds_delay: The number of milliseconds to wait before completing the returned Task
        :returns: A Task that represents the time delay.
        """
        ...

    @staticmethod
    @overload
    def delay(milliseconds_delay: int, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        """
        Creates a Task that will complete after a time delay.
        
        :param milliseconds_delay: The number of milliseconds to wait before completing the returned Task
        :param cancellation_token: The cancellation token that will be checked prior to completing the returned Task
        :returns: A Task that represents the time delay.
        """
        ...

    @overload
    def dispose(self) -> None:
        """Disposes the Task, releasing all of its unmanaged resources."""
        ...

    @overload
    def dispose(self, disposing: bool) -> None:
        """
        Disposes the Task, releasing all of its unmanaged resources.
        
        This method is protected.
        
        :param disposing: A Boolean value that indicates whether this method is being called due to a call to Dispose().
        """
        ...

    @staticmethod
    def from_canceled(cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        """
        Creates a Task that's completed due to cancellation with the specified token.
        
        :param cancellation_token: The token with which to complete the task.
        :returns: The canceled task.
        """
        ...

    @staticmethod
    def from_exception(exception: System.Exception) -> System.Threading.Tasks.Task:
        """
        Creates a Task{TResult} that's completed exceptionally with the specified exception.
        
        :param exception: The exception with which to complete the task.
        :returns: The faulted task.
        """
        ...

    def get_awaiter(self) -> System.Runtime.CompilerServices.TaskAwaiter:
        ...

    @staticmethod
    @overload
    def run(action: typing.Callable[[], None]) -> System.Threading.Tasks.Task:
        """
        Queues the specified work to run on the ThreadPool and returns a Task handle for that work.
        
        :param action: The work to execute asynchronously
        :returns: A Task that represents the work queued to execute in the ThreadPool.
        """
        ...

    @staticmethod
    @overload
    def run(action: typing.Callable[[], None], cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        """
        Queues the specified work to run on the ThreadPool and returns a Task handle for that work.
        
        :param action: The work to execute asynchronously
        :param cancellation_token: A cancellation token that should be used to cancel the work
        :returns: A Task that represents the work queued to execute in the ThreadPool.
        """
        ...

    @staticmethod
    @overload
    def run(function: typing.Callable[[], System.Threading.Tasks.Task]) -> System.Threading.Tasks.Task:
        """
        Queues the specified work to run on the ThreadPool and returns a proxy for the
        Task returned by .
        
        :param function: The work to execute asynchronously
        :returns: A Task that represents a proxy for the Task returned by .
        """
        ...

    @staticmethod
    @overload
    def run(function: typing.Callable[[], System.Threading.Tasks.Task], cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        """
        Queues the specified work to run on the ThreadPool and returns a proxy for the
        Task returned by .
        
        :param function: The work to execute asynchronously
        :param cancellation_token: A cancellation token that should be used to cancel the work
        :returns: A Task that represents a proxy for the Task returned by .
        """
        ...

    @overload
    def run_synchronously(self) -> None:
        """Runs the Task synchronously on the current TaskScheduler."""
        ...

    @overload
    def run_synchronously(self, scheduler: System.Threading.Tasks.TaskScheduler) -> None:
        """
        Runs the Task synchronously on the TaskScheduler provided.
        
        :param scheduler: The scheduler on which to attempt to run this task inline.
        """
        ...

    @overload
    def start(self) -> None:
        """Starts the Task, scheduling it for execution to the current TaskScheduler."""
        ...

    @overload
    def start(self, scheduler: System.Threading.Tasks.TaskScheduler) -> None:
        """
        Starts the Task, scheduling it for execution to the specified TaskScheduler.
        
        :param scheduler: The TaskScheduler with which to associate and execute this task.
        """
        ...

    @overload
    def wait(self) -> None:
        """Waits for the Task to complete execution."""
        ...

    @overload
    def wait(self, timeout: datetime.timedelta) -> bool:
        """
        Waits for the Task to complete execution.
        
        :param timeout: A TimeSpan that represents the number of milliseconds to wait, or a TimeSpan that represents -1 milliseconds to wait indefinitely.
        :returns: true if the Task completed execution within the allotted time; otherwise, false.
        """
        ...

    @overload
    def wait(self, timeout: datetime.timedelta, cancellation_token: System.Threading.CancellationToken) -> bool:
        """
        Waits for the Task to complete execution.
        
        :param timeout: The time to wait, or Timeout.InfiniteTimeSpan to wait indefinitely
        :param cancellation_token: A CancellationToken to observe while waiting for the task to complete.
        :returns: true if the Task completed execution within the allotted time; otherwise, false.
        """
        ...

    @overload
    def wait(self, cancellation_token: System.Threading.CancellationToken) -> None:
        """
        Waits for the Task to complete execution.
        
        :param cancellation_token: A CancellationToken to observe while waiting for the task to complete.
        """
        ...

    @overload
    def wait(self, milliseconds_timeout: int) -> bool:
        """
        Waits for the Task to complete execution.
        
        :param milliseconds_timeout: The number of milliseconds to wait, or Timeout.Infinite (-1) to wait indefinitely.
        :returns: true if the Task completed execution within the allotted time; otherwise, false.
        """
        ...

    @overload
    def wait(self, milliseconds_timeout: int, cancellation_token: System.Threading.CancellationToken) -> bool:
        """
        Waits for the Task to complete execution.
        
        :param milliseconds_timeout: The number of milliseconds to wait, or Timeout.Infinite (-1) to wait indefinitely.
        :param cancellation_token: A CancellationToken to observe while waiting for the task to complete.
        :returns: true if the Task completed execution within the allotted time; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def wait_all(*tasks: typing.Union[System.Threading.Tasks.Task, typing.Iterable[System.Threading.Tasks.Task]]) -> None:
        """
        Waits for all of the provided Task objects to complete execution.
        
        :param tasks: An array of Task instances on which to wait.
        """
        ...

    @staticmethod
    @overload
    def wait_all(tasks: typing.List[System.Threading.Tasks.Task], timeout: datetime.timedelta) -> bool:
        """
        Waits for all of the provided Task objects to complete execution.
        
        :param tasks: An array of Task instances on which to wait.
        :param timeout: A TimeSpan that represents the number of milliseconds to wait, or a TimeSpan that represents -1 milliseconds to wait indefinitely.
        :returns: true if all of the Task instances completed execution within the allotted time; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def wait_all(tasks: typing.List[System.Threading.Tasks.Task], milliseconds_timeout: int) -> bool:
        """
        Waits for all of the provided Task objects to complete execution.
        
        :param tasks: An array of Task instances on which to wait.
        :param milliseconds_timeout: The number of milliseconds to wait, or Timeout.Infinite (-1) to wait indefinitely.
        :returns: true if all of the Task instances completed execution within the allotted time; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def wait_all(tasks: typing.List[System.Threading.Tasks.Task], cancellation_token: System.Threading.CancellationToken) -> None:
        """
        Waits for all of the provided Task objects to complete execution.
        
        :param tasks: An array of Task instances on which to wait.
        :param cancellation_token: A CancellationToken to observe while waiting for the tasks to complete.
        """
        ...

    @staticmethod
    @overload
    def wait_all(tasks: typing.List[System.Threading.Tasks.Task], milliseconds_timeout: int, cancellation_token: System.Threading.CancellationToken) -> bool:
        """
        Waits for all of the provided Task objects to complete execution.
        
        :param tasks: An array of Task instances on which to wait.
        :param milliseconds_timeout: The number of milliseconds to wait, or Timeout.Infinite (-1) to wait indefinitely.
        :param cancellation_token: A CancellationToken to observe while waiting for the tasks to complete.
        :returns: true if all of the Task instances completed execution within the allotted time; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def wait_all(tasks: System.Collections.Generic.IEnumerable[System.Threading.Tasks.Task], cancellation_token: System.Threading.CancellationToken = ...) -> None:
        """
        Waits for all of the provided Task objects to complete execution unless the wait is cancelled.
        
        :param tasks: An IEnumerable{T} of Task instances on which to wait.
        :param cancellation_token: A CancellationToken to observe while waiting for the tasks to complete.
        """
        ...

    @staticmethod
    @overload
    def wait_any(*tasks: typing.Union[System.Threading.Tasks.Task, typing.Iterable[System.Threading.Tasks.Task]]) -> int:
        """
        Waits for any of the provided Task objects to complete execution.
        
        :param tasks: An array of Task instances on which to wait.
        :returns: The index of the completed task in the  array argument.
        """
        ...

    @staticmethod
    @overload
    def wait_any(tasks: typing.List[System.Threading.Tasks.Task], timeout: datetime.timedelta) -> int:
        """
        Waits for any of the provided Task objects to complete execution.
        
        :param tasks: An array of Task instances on which to wait.
        :param timeout: A TimeSpan that represents the number of milliseconds to wait, or a TimeSpan that represents -1 milliseconds to wait indefinitely.
        :returns: The index of the completed task in the  array argument, or -1 if the timeout occurred.
        """
        ...

    @staticmethod
    @overload
    def wait_any(tasks: typing.List[System.Threading.Tasks.Task], cancellation_token: System.Threading.CancellationToken) -> int:
        """
        Waits for any of the provided Task objects to complete execution.
        
        :param tasks: An array of Task instances on which to wait.
        :param cancellation_token: A CancellationToken to observe while waiting for a task to complete.
        :returns: The index of the completed task in the  array argument.
        """
        ...

    @staticmethod
    @overload
    def wait_any(tasks: typing.List[System.Threading.Tasks.Task], milliseconds_timeout: int) -> int:
        """
        Waits for any of the provided Task objects to complete execution.
        
        :param tasks: An array of Task instances on which to wait.
        :param milliseconds_timeout: The number of milliseconds to wait, or Timeout.Infinite (-1) to wait indefinitely.
        :returns: The index of the completed task in the  array argument, or -1 if the timeout occurred.
        """
        ...

    @staticmethod
    @overload
    def wait_any(tasks: typing.List[System.Threading.Tasks.Task], milliseconds_timeout: int, cancellation_token: System.Threading.CancellationToken) -> int:
        """
        Waits for any of the provided Task objects to complete execution.
        
        :param tasks: An array of Task instances on which to wait.
        :param milliseconds_timeout: The number of milliseconds to wait, or Timeout.Infinite (-1) to wait indefinitely.
        :param cancellation_token: A CancellationToken to observe while waiting for a task to complete.
        :returns: The index of the completed task in the  array argument, or -1 if the timeout occurred.
        """
        ...

    @overload
    def wait_async(self, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        """
        Gets a Task that will complete when this Task completes or when the specified CancellationToken has cancellation requested.
        
        :param cancellation_token: The CancellationToken to monitor for a cancellation request.
        :returns: The Task representing the asynchronous wait.  It may or may not be the same instance as the current instance.
        """
        ...

    @overload
    def wait_async(self, timeout: datetime.timedelta) -> System.Threading.Tasks.Task:
        """
        Gets a Task that will complete when this Task completes or when the specified timeout expires.
        
        :param timeout: The timeout after which the Task should be faulted with a TimeoutException if it hasn't otherwise completed.
        :returns: The Task representing the asynchronous wait.  It may or may not be the same instance as the current instance.
        """
        ...

    @overload
    def wait_async(self, timeout: datetime.timedelta, time_provider: System.TimeProvider) -> System.Threading.Tasks.Task:
        """
        Gets a Task that will complete when this Task completes or when the specified timeout expires.
        
        :param timeout: The timeout after which the Task should be faulted with a TimeoutException if it hasn't otherwise completed.
        :param time_provider: The TimeProvider with which to interpret .
        :returns: The Task representing the asynchronous wait.  It may or may not be the same instance as the current instance.
        """
        ...

    @overload
    def wait_async(self, timeout: datetime.timedelta, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        """
        Gets a Task that will complete when this Task completes, when the specified timeout expires, or when the specified CancellationToken has cancellation requested.
        
        :param timeout: The timeout after which the Task should be faulted with a TimeoutException if it hasn't otherwise completed.
        :param cancellation_token: The CancellationToken to monitor for a cancellation request.
        :returns: The Task representing the asynchronous wait.  It may or may not be the same instance as the current instance.
        """
        ...

    @overload
    def wait_async(self, timeout: datetime.timedelta, time_provider: System.TimeProvider, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        """
        Gets a Task that will complete when this Task completes, when the specified timeout expires, or when the specified CancellationToken has cancellation requested.
        
        :param timeout: The timeout after which the Task should be faulted with a TimeoutException if it hasn't otherwise completed.
        :param time_provider: The TimeProvider with which to interpret .
        :param cancellation_token: The CancellationToken to monitor for a cancellation request.
        :returns: The Task representing the asynchronous wait.  It may or may not be the same instance as the current instance.
        """
        ...

    @staticmethod
    @overload
    def when_all(tasks: System.Collections.Generic.IEnumerable[System.Threading.Tasks.Task]) -> System.Threading.Tasks.Task:
        ...

    @staticmethod
    @overload
    def when_all(*tasks: typing.Union[System.Threading.Tasks.Task, typing.Iterable[System.Threading.Tasks.Task]]) -> System.Threading.Tasks.Task:
        """
        Creates a task that will complete when all of the supplied tasks have completed.
        
        :param tasks: The tasks to wait on for completion.
        :returns: A task that represents the completion of all of the supplied tasks.
        """
        ...

    @staticmethod
    @overload
    def when_any(*tasks: typing.Union[System.Threading.Tasks.Task, typing.Iterable[System.Threading.Tasks.Task]]) -> System.Threading.Tasks.Task[System.Threading.Tasks.Task]:
        ...

    @staticmethod
    @overload
    def when_any(task_1: System.Threading.Tasks.Task, task_2: System.Threading.Tasks.Task) -> System.Threading.Tasks.Task[System.Threading.Tasks.Task]:
        """
        Creates a task that will complete when either of the supplied tasks have completed.
        
        :param task_1: The first task to wait on for completion.
        :param task_2: The second task to wait on for completion.
        :returns: A task that represents the completion of one of the supplied tasks.  The return Task's Result is the task that completed.
        """
        ...

    @staticmethod
    @overload
    def when_any(tasks: System.Collections.Generic.IEnumerable[System.Threading.Tasks.Task]) -> System.Threading.Tasks.Task[System.Threading.Tasks.Task]:
        """
        Creates a task that will complete when any of the supplied tasks have completed.
        
        :param tasks: The tasks to wait on for completion.
        :returns: A task that represents the completion of one of the supplied tasks.  The return Task's Result is the task that completed.
        """
        ...

    @staticmethod
    @overload
    def when_each(*tasks: typing.Union[System.Threading.Tasks.Task, typing.Iterable[System.Threading.Tasks.Task]]) -> System.Collections.Generic.IAsyncEnumerable[System.Threading.Tasks.Task]:
        ...

    @staticmethod
    @overload
    def when_each(tasks: System.Collections.Generic.IEnumerable[System.Threading.Tasks.Task]) -> System.Collections.Generic.IAsyncEnumerable[System.Threading.Tasks.Task]:
        """:param tasks: The tasks to iterate through as they complete."""
        ...

    @staticmethod
    def Yield() -> System.Runtime.CompilerServices.YieldAwaitable:
        """
        Creates an awaitable that asynchronously yields back to the current context when awaited.
        
        :returns: A context that, when awaited, will asynchronously transition back into the current context at the time of the await. If the current SynchronizationContext is non-null, that is treated as the current context. Otherwise, TaskScheduler.Current is treated as the current context.
        """
        ...


class TaskExtensions(System.Object):
    """Provides a set of static methods for working with specific kinds of Task instances."""

    @staticmethod
    def unwrap(task: System.Threading.Tasks.Task[System.Threading.Tasks.Task]) -> System.Threading.Tasks.Task:
        """
        Creates a proxy Task that represents the asynchronous operation of a Task{Task}.
        
        :param task: The Task{Task} to unwrap.
        :returns: A Task that represents the asynchronous operation of the provided Task{Task}.
        """
        ...


class TaskCanceledException(System.OperationCanceledException):
    """Represents an exception used to communicate task cancellation."""

    @property
    def task(self) -> System.Threading.Tasks.Task:
        """Gets the task associated with this exception."""
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the TaskCanceledException class."""
        ...

    @overload
    def __init__(self, message: str) -> None:
        """
        Initializes a new instance of the TaskCanceledException
        class with a specified error message.
        
        :param message: The error message that explains the reason for the exception.
        """
        ...

    @overload
    def __init__(self, message: str, inner_exception: System.Exception) -> None:
        """
        Initializes a new instance of the TaskCanceledException
        class with a specified error message and a reference to the inner exception that is the cause of
        this exception.
        
        :param message: The error message that explains the reason for the exception.
        :param inner_exception: The exception that is the cause of the current exception.
        """
        ...

    @overload
    def __init__(self, message: str, inner_exception: System.Exception, token: System.Threading.CancellationToken) -> None:
        """
        Initializes a new instance of the TaskCanceledException
        class with a specified error message, a reference to the inner exception that is the cause of
        this exception, and the CancellationToken that triggered the cancellation.
        
        :param message: The error message that explains the reason for the exception.
        :param inner_exception: The exception that is the cause of the current exception.
        :param token: The CancellationToken that triggered the cancellation.
        """
        ...

    @overload
    def __init__(self, task: System.Threading.Tasks.Task) -> None:
        """
        Initializes a new instance of the TaskCanceledException class
        with a reference to the Tasks.Task that has been canceled.
        
        :param task: A task that has been canceled.
        """
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """
        Initializes a new instance of the TaskCanceledException
        class with serialized data.
        
        This method is protected.
        
        Obsoletions.LegacyFormatterImplMessage
        
        :param info: The SerializationInfo that holds the serialized object data about the exception being thrown.
        :param context: The StreamingContext that contains contextual information about the source or destination.
        """
        ...


class ConcurrentExclusiveSchedulerPair(System.Object):
    """
    Provides concurrent and exclusive task schedulers that coordinate to execute
    tasks while ensuring that concurrent tasks may run concurrently and exclusive tasks never do.
    """

    @property
    def completion(self) -> System.Threading.Tasks.Task:
        """Gets a Task that will complete when the scheduler has completed processing."""
        ...

    @property
    def concurrent_scheduler(self) -> System.Threading.Tasks.TaskScheduler:
        """
        Gets a TaskScheduler that can be used to schedule tasks to this pair
        that may run concurrently with other tasks on this pair.
        """
        ...

    @property
    def exclusive_scheduler(self) -> System.Threading.Tasks.TaskScheduler:
        """
        Gets a TaskScheduler that can be used to schedule tasks to this pair
        that must run exclusively with regards to other tasks on this pair.
        """
        ...

    @overload
    def __init__(self) -> None:
        """Initializes the ConcurrentExclusiveSchedulerPair."""
        ...

    @overload
    def __init__(self, task_scheduler: System.Threading.Tasks.TaskScheduler) -> None:
        """
        Initializes the ConcurrentExclusiveSchedulerPair to target the specified scheduler.
        
        :param task_scheduler: The target scheduler on which this pair should execute.
        """
        ...

    @overload
    def __init__(self, task_scheduler: System.Threading.Tasks.TaskScheduler, max_concurrency_level: int) -> None:
        """
        Initializes the ConcurrentExclusiveSchedulerPair to target the specified scheduler with a maximum concurrency level.
        
        :param task_scheduler: The target scheduler on which this pair should execute.
        :param max_concurrency_level: The maximum number of tasks to run concurrently.
        """
        ...

    @overload
    def __init__(self, task_scheduler: System.Threading.Tasks.TaskScheduler, max_concurrency_level: int, max_items_per_task: int) -> None:
        """
        Initializes the ConcurrentExclusiveSchedulerPair to target the specified scheduler with a maximum
        concurrency level and a maximum number of scheduled tasks that may be processed as a unit.
        
        :param task_scheduler: The target scheduler on which this pair should execute.
        :param max_concurrency_level: The maximum number of tasks to run concurrently.
        :param max_items_per_task: The maximum number of tasks to process for each underlying scheduled task used by the pair.
        """
        ...

    def complete(self) -> None:
        """Informs the scheduler pair that it should not accept any more tasks."""
        ...


class TaskFactory(typing.Generic[System_Threading_Tasks_TaskFactory_TResult], System.Object):
    """
    Provides support for creating and scheduling
    Task{TResult} objects.
    """

    @property
    def cancellation_token(self) -> System.Threading.CancellationToken:
        """
        Gets the default Threading.CancellationToken of this
        TaskFactory.
        """
        ...

    @property
    def scheduler(self) -> System.Threading.Tasks.TaskScheduler:
        """
        Gets the TaskScheduler of this
        TaskFactory{TResult}.
        """
        ...

    @property
    def creation_options(self) -> System.Threading.Tasks.TaskCreationOptions:
        """Gets the TaskCreationOptions value of this TaskFactory{TResult}."""
        ...

    @property
    def continuation_options(self) -> System.Threading.Tasks.TaskContinuationOptions:
        """Gets the TaskCreationOptions value of this TaskFactory{TResult}."""
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a TaskFactory{TResult} instance with the default configuration."""
        ...

    @overload
    def __init__(self, cancellation_token: System.Threading.CancellationToken) -> None:
        """
        Initializes a TaskFactory{TResult} instance with the default configuration.
        
        :param cancellation_token: The default CancellationToken that will be assigned to tasks created by this TaskFactory unless another CancellationToken is explicitly specified while calling the factory methods.
        """
        ...

    @overload
    def __init__(self, scheduler: System.Threading.Tasks.TaskScheduler) -> None:
        """
        Initializes a TaskFactory{TResult} instance with the specified configuration.
        
        :param scheduler: The TaskScheduler to use to schedule any tasks created with this TaskFactory{TResult}. A null value indicates that the current TaskScheduler should be used.
        """
        ...

    @overload
    def __init__(self, creation_options: System.Threading.Tasks.TaskCreationOptions, continuation_options: System.Threading.Tasks.TaskContinuationOptions) -> None:
        """
        Initializes a TaskFactory{TResult} instance with the specified configuration.
        
        :param creation_options: The default TaskCreationOptions to use when creating tasks with this TaskFactory{TResult}.
        :param continuation_options: The default TaskContinuationOptions to use when creating continuation tasks with this TaskFactory{TResult}.
        """
        ...

    @overload
    def __init__(self, cancellation_token: System.Threading.CancellationToken, creation_options: System.Threading.Tasks.TaskCreationOptions, continuation_options: System.Threading.Tasks.TaskContinuationOptions, scheduler: System.Threading.Tasks.TaskScheduler) -> None:
        """
        Initializes a TaskFactory{TResult} instance with the specified configuration.
        
        :param cancellation_token: The default CancellationToken that will be assigned to tasks created by this TaskFactory unless another CancellationToken is explicitly specified while calling the factory methods.
        :param creation_options: The default TaskCreationOptions to use when creating tasks with this TaskFactory{TResult}.
        :param continuation_options: The default TaskContinuationOptions to use when creating continuation tasks with this TaskFactory{TResult}.
        :param scheduler: The default TaskScheduler to use to schedule any Tasks created with this TaskFactory{TResult}. A null value indicates that TaskScheduler.Current should be used.
        """
        ...

    @overload
    def continue_when_all(self, tasks: typing.List[System.Threading.Tasks.Task], continuation_function: typing.Callable[[typing.List[System.Threading.Tasks.Task]], System_Threading_Tasks_TaskFactory_TResult]) -> System.Threading.Tasks.Task[System_Threading_Tasks_TaskFactory_TResult]:
        """
        Creates a continuation Task{TResult}
        that will be started upon the completion of a set of provided Tasks.
        
        :param tasks: The array of tasks from which to continue.
        :param continuation_function: The function delegate to execute when all tasks in the  array have completed.
        :returns: The new continuation Task{TResult}.
        """
        ...

    @overload
    def continue_when_all(self, tasks: typing.List[System.Threading.Tasks.Task], continuation_function: typing.Callable[[typing.List[System.Threading.Tasks.Task]], System_Threading_Tasks_TaskFactory_TResult], cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task[System_Threading_Tasks_TaskFactory_TResult]:
        """
        Creates a continuation Task{TResult}
        that will be started upon the completion of a set of provided Tasks.
        
        :param tasks: The array of tasks from which to continue.
        :param continuation_function: The function delegate to execute when all tasks in the  array have completed.
        :param cancellation_token: The Threading.CancellationToken that will be assigned to the new continuation task.
        :returns: The new continuation Task{TResult}.
        """
        ...

    @overload
    def continue_when_all(self, tasks: typing.List[System.Threading.Tasks.Task], continuation_function: typing.Callable[[typing.List[System.Threading.Tasks.Task]], System_Threading_Tasks_TaskFactory_TResult], continuation_options: System.Threading.Tasks.TaskContinuationOptions) -> System.Threading.Tasks.Task[System_Threading_Tasks_TaskFactory_TResult]:
        """
        Creates a continuation Task{TResult}
        that will be started upon the completion of a set of provided Tasks.
        
        :param tasks: The array of tasks from which to continue.
        :param continuation_function: The function delegate to execute when all tasks in the  array have completed.
        :param continuation_options: The TaskContinuationOptions value that controls the behavior of the created continuation Task{TResult}.
        :returns: The new continuation Task{TResult}.
        """
        ...

    @overload
    def continue_when_all(self, tasks: typing.List[System.Threading.Tasks.Task], continuation_function: typing.Callable[[typing.List[System.Threading.Tasks.Task]], System_Threading_Tasks_TaskFactory_TResult], cancellation_token: System.Threading.CancellationToken, continuation_options: System.Threading.Tasks.TaskContinuationOptions, scheduler: System.Threading.Tasks.TaskScheduler) -> System.Threading.Tasks.Task[System_Threading_Tasks_TaskFactory_TResult]:
        """
        Creates a continuation Task{TResult}
        that will be started upon the completion of a set of provided Tasks.
        
        :param tasks: The array of tasks from which to continue.
        :param continuation_function: The function delegate to execute when all tasks in the  array have completed.
        :param cancellation_token: The Threading.CancellationToken that will be assigned to the new continuation task.
        :param continuation_options: The TaskContinuationOptions value that controls the behavior of the created continuation Task{TResult}.
        :param scheduler: The TaskScheduler that is used to schedule the created continuation Task.
        :returns: The new continuation Task{TResult}.
        """
        ...

    @overload
    def continue_when_all(self, tasks: typing.List[System.Threading.Tasks.Task], continuation_action: typing.Callable[[typing.List[System.Threading.Tasks.Task]], None]) -> System.Threading.Tasks.Task:
        """
        Creates a continuation Task
        that will be started upon the completion of a set of provided Tasks.
        
        :param tasks: The array of tasks from which to continue.
        :param continuation_action: The action delegate to execute when all tasks in the  array have completed.
        :returns: The new continuation Task.
        """
        ...

    @overload
    def continue_when_all(self, tasks: typing.List[System.Threading.Tasks.Task], continuation_action: typing.Callable[[typing.List[System.Threading.Tasks.Task]], None], cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        """
        Creates a continuation Task
        that will be started upon the completion of a set of provided Tasks.
        
        :param tasks: The array of tasks from which to continue.
        :param continuation_action: The action delegate to execute when all tasks in the  array have completed.
        :param cancellation_token: The Threading.CancellationToken that will be assigned to the new continuation task.
        :returns: The new continuation Task.
        """
        ...

    @overload
    def continue_when_all(self, tasks: typing.List[System.Threading.Tasks.Task], continuation_action: typing.Callable[[typing.List[System.Threading.Tasks.Task]], None], continuation_options: System.Threading.Tasks.TaskContinuationOptions) -> System.Threading.Tasks.Task:
        """
        Creates a continuation Task
        that will be started upon the completion of a set of provided Tasks.
        
        :param tasks: The array of tasks from which to continue.
        :param continuation_action: The action delegate to execute when all tasks in the  array have completed.
        :param continuation_options: The TaskContinuationOptions value that controls the behavior of the created continuation Task.
        :returns: The new continuation Task.
        """
        ...

    @overload
    def continue_when_all(self, tasks: typing.List[System.Threading.Tasks.Task], continuation_action: typing.Callable[[typing.List[System.Threading.Tasks.Task]], None], cancellation_token: System.Threading.CancellationToken, continuation_options: System.Threading.Tasks.TaskContinuationOptions, scheduler: System.Threading.Tasks.TaskScheduler) -> System.Threading.Tasks.Task:
        """
        Creates a continuation Task
        that will be started upon the completion of a set of provided Tasks.
        
        :param tasks: The array of tasks from which to continue.
        :param continuation_action: The action delegate to execute when all tasks in the  array have completed.
        :param cancellation_token: The Threading.CancellationToken that will be assigned to the new continuation task.
        :param continuation_options: The TaskContinuationOptions value that controls the behavior of the created continuation Task.
        :param scheduler: The TaskScheduler that is used to schedule the created continuation Task.
        :returns: The new continuation Task.
        """
        ...

    @overload
    def continue_when_any(self, tasks: typing.List[System.Threading.Tasks.Task], continuation_function: typing.Callable[[System.Threading.Tasks.Task], System_Threading_Tasks_TaskFactory_TResult]) -> System.Threading.Tasks.Task[System_Threading_Tasks_TaskFactory_TResult]:
        """
        Creates a continuation Task{TResult}
        that will be started upon the completion of any Task in the provided set.
        
        :param tasks: The array of tasks from which to continue when one task completes.
        :param continuation_function: The function delegate to execute when one task in the  array completes.
        :returns: The new continuation Task{TResult}.
        """
        ...

    @overload
    def continue_when_any(self, tasks: typing.List[System.Threading.Tasks.Task], continuation_function: typing.Callable[[System.Threading.Tasks.Task], System_Threading_Tasks_TaskFactory_TResult], cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task[System_Threading_Tasks_TaskFactory_TResult]:
        """
        Creates a continuation Task{TResult}
        that will be started upon the completion of any Task in the provided set.
        
        :param tasks: The array of tasks from which to continue when one task completes.
        :param continuation_function: The function delegate to execute when one task in the  array completes.
        :param cancellation_token: The Threading.CancellationToken that will be assigned to the new continuation task.
        :returns: The new continuation Task{TResult}.
        """
        ...

    @overload
    def continue_when_any(self, tasks: typing.List[System.Threading.Tasks.Task], continuation_function: typing.Callable[[System.Threading.Tasks.Task], System_Threading_Tasks_TaskFactory_TResult], continuation_options: System.Threading.Tasks.TaskContinuationOptions) -> System.Threading.Tasks.Task[System_Threading_Tasks_TaskFactory_TResult]:
        """
        Creates a continuation Task{TResult}
        that will be started upon the completion of any Task in the provided set.
        
        :param tasks: The array of tasks from which to continue when one task completes.
        :param continuation_function: The function delegate to execute when one task in the  array completes.
        :param continuation_options: The TaskContinuationOptions value that controls the behavior of the created continuation Task{TResult}.
        :returns: The new continuation Task{TResult}.
        """
        ...

    @overload
    def continue_when_any(self, tasks: typing.List[System.Threading.Tasks.Task], continuation_function: typing.Callable[[System.Threading.Tasks.Task], System_Threading_Tasks_TaskFactory_TResult], cancellation_token: System.Threading.CancellationToken, continuation_options: System.Threading.Tasks.TaskContinuationOptions, scheduler: System.Threading.Tasks.TaskScheduler) -> System.Threading.Tasks.Task[System_Threading_Tasks_TaskFactory_TResult]:
        """
        Creates a continuation Task{TResult}
        that will be started upon the completion of any Task in the provided set.
        
        :param tasks: The array of tasks from which to continue when one task completes.
        :param continuation_function: The function delegate to execute when one task in the  array completes.
        :param cancellation_token: The Threading.CancellationToken that will be assigned to the new continuation task.
        :param continuation_options: The TaskContinuationOptions value that controls the behavior of the created continuation Task{TResult}.
        :param scheduler: The TaskScheduler that is used to schedule the created continuation Task.
        :returns: The new continuation Task{TResult}.
        """
        ...

    @overload
    def continue_when_any(self, tasks: typing.List[System.Threading.Tasks.Task], continuation_action: typing.Callable[[System.Threading.Tasks.Task], None]) -> System.Threading.Tasks.Task:
        """
        Creates a continuation Task
        that will be started upon the completion of any Task in the provided set.
        
        :param tasks: The array of tasks from which to continue when one task completes.
        :param continuation_action: The action delegate to execute when one task in the  array completes.
        :returns: The new continuation Task.
        """
        ...

    @overload
    def continue_when_any(self, tasks: typing.List[System.Threading.Tasks.Task], continuation_action: typing.Callable[[System.Threading.Tasks.Task], None], cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        """
        Creates a continuation Task
        that will be started upon the completion of any Task in the provided set.
        
        :param tasks: The array of tasks from which to continue when one task completes.
        :param continuation_action: The action delegate to execute when one task in the  array completes.
        :param cancellation_token: The Threading.CancellationToken that will be assigned to the new continuation task.
        :returns: The new continuation Task.
        """
        ...

    @overload
    def continue_when_any(self, tasks: typing.List[System.Threading.Tasks.Task], continuation_action: typing.Callable[[System.Threading.Tasks.Task], None], continuation_options: System.Threading.Tasks.TaskContinuationOptions) -> System.Threading.Tasks.Task:
        """
        Creates a continuation Task
        that will be started upon the completion of any Task in the provided set.
        
        :param tasks: The array of tasks from which to continue when one task completes.
        :param continuation_action: The action delegate to execute when one task in the  array completes.
        :param continuation_options: The TaskContinuationOptions value that controls the behavior of the created continuation Task.
        :returns: The new continuation Task.
        """
        ...

    @overload
    def continue_when_any(self, tasks: typing.List[System.Threading.Tasks.Task], continuation_action: typing.Callable[[System.Threading.Tasks.Task], None], cancellation_token: System.Threading.CancellationToken, continuation_options: System.Threading.Tasks.TaskContinuationOptions, scheduler: System.Threading.Tasks.TaskScheduler) -> System.Threading.Tasks.Task:
        """
        Creates a continuation Task
        that will be started upon the completion of any Task in the provided set.
        
        :param tasks: The array of tasks from which to continue when one task completes.
        :param continuation_action: The action delegate to execute when one task in the  array completes.
        :param cancellation_token: The Threading.CancellationToken that will be assigned to the new continuation task.
        :param continuation_options: The TaskContinuationOptions value that controls the behavior of the created continuation Task.
        :param scheduler: The TaskScheduler that is used to schedule the created continuation Task.
        :returns: The new continuation Task.
        """
        ...

    @overload
    def from_async(self, begin_method: typing.Callable[[typing.Callable[[System.IAsyncResult], None], System.Object], System.IAsyncResult], end_method: typing.Callable[[System.IAsyncResult], System_Threading_Tasks_TaskFactory_TResult], state: typing.Any) -> System.Threading.Tasks.Task[System_Threading_Tasks_TaskFactory_TResult]:
        """
        Creates a Task{TResult} that represents a pair of
        begin and end methods that conform to the Asynchronous Programming Model pattern.
        
        :param begin_method: The delegate that begins the asynchronous operation.
        :param end_method: The delegate that ends the asynchronous operation.
        :param state: An object containing data to be used by the  delegate.
        :returns: The created Task{TResult} that represents the asynchronous operation.
        """
        ...

    @overload
    def from_async(self, begin_method: typing.Callable[[typing.Callable[[System.IAsyncResult], None], System.Object], System.IAsyncResult], end_method: typing.Callable[[System.IAsyncResult], System_Threading_Tasks_TaskFactory_TResult], state: typing.Any, creation_options: System.Threading.Tasks.TaskCreationOptions) -> System.Threading.Tasks.Task[System_Threading_Tasks_TaskFactory_TResult]:
        """
        Creates a Task{TResult} that represents a pair of
        begin and end methods that conform to the Asynchronous Programming Model pattern.
        
        :param begin_method: The delegate that begins the asynchronous operation.
        :param end_method: The delegate that ends the asynchronous operation.
        :param state: An object containing data to be used by the  delegate.
        :param creation_options: The TaskCreationOptions value that controls the behavior of the created Task{TResult}.
        :returns: The created Task{TResult} that represents the asynchronous operation.
        """
        ...

    @overload
    def from_async(self, begin_method: typing.Callable[[typing.Callable[[System.IAsyncResult], None], System.Object], System.IAsyncResult], end_method: typing.Callable[[System.IAsyncResult], None], state: typing.Any) -> System.Threading.Tasks.Task:
        """
        Creates a Task that represents a pair of begin
        and end methods that conform to the Asynchronous Programming Model pattern.
        
        :param begin_method: The delegate that begins the asynchronous operation.
        :param end_method: The delegate that ends the asynchronous operation.
        :param state: An object containing data to be used by the  delegate.
        :returns: The created Task that represents the asynchronous operation.
        """
        ...

    @overload
    def from_async(self, begin_method: typing.Callable[[typing.Callable[[System.IAsyncResult], None], System.Object], System.IAsyncResult], end_method: typing.Callable[[System.IAsyncResult], None], state: typing.Any, creation_options: System.Threading.Tasks.TaskCreationOptions) -> System.Threading.Tasks.Task:
        """
        Creates a Task that represents a pair of begin
        and end methods that conform to the Asynchronous Programming Model pattern.
        
        :param begin_method: The delegate that begins the asynchronous operation.
        :param end_method: The delegate that ends the asynchronous operation.
        :param state: An object containing data to be used by the  delegate.
        :param creation_options: The TaskCreationOptions value that controls the behavior of the created Task.
        :returns: The created Task that represents the asynchronous operation.
        """
        ...

    @overload
    def from_async(self, async_result: System.IAsyncResult, end_method: typing.Callable[[System.IAsyncResult], System_Threading_Tasks_TaskFactory_TResult]) -> System.Threading.Tasks.Task[System_Threading_Tasks_TaskFactory_TResult]:
        """
        Creates a Task{TResult} that executes an end
        method function when a specified IAsyncResult completes.
        
        :param async_result: The IAsyncResult whose completion should trigger the processing of the .
        :param end_method: The function delegate that processes the completed .
        :returns: A Task{TResult} that represents the asynchronous operation.
        """
        ...

    @overload
    def from_async(self, async_result: System.IAsyncResult, end_method: typing.Callable[[System.IAsyncResult], System_Threading_Tasks_TaskFactory_TResult], creation_options: System.Threading.Tasks.TaskCreationOptions) -> System.Threading.Tasks.Task[System_Threading_Tasks_TaskFactory_TResult]:
        """
        Creates a Task{TResult} that executes an end
        method function when a specified IAsyncResult completes.
        
        :param async_result: The IAsyncResult whose completion should trigger the processing of the .
        :param end_method: The function delegate that processes the completed .
        :param creation_options: The TaskCreationOptions value that controls the behavior of the created Task{TResult}.
        :returns: A Task{TResult} that represents the asynchronous operation.
        """
        ...

    @overload
    def from_async(self, async_result: System.IAsyncResult, end_method: typing.Callable[[System.IAsyncResult], System_Threading_Tasks_TaskFactory_TResult], creation_options: System.Threading.Tasks.TaskCreationOptions, scheduler: System.Threading.Tasks.TaskScheduler) -> System.Threading.Tasks.Task[System_Threading_Tasks_TaskFactory_TResult]:
        """
        Creates a Task{TResult} that executes an end
        method function when a specified IAsyncResult completes.
        
        :param async_result: The IAsyncResult whose completion should trigger the processing of the .
        :param end_method: The function delegate that processes the completed .
        :param creation_options: The TaskCreationOptions value that controls the behavior of the created Task{TResult}.
        :param scheduler: The TaskScheduler that is used to schedule the task that executes the end method.
        :returns: A Task{TResult} that represents the asynchronous operation.
        """
        ...

    @overload
    def from_async(self, async_result: System.IAsyncResult, end_method: typing.Callable[[System.IAsyncResult], None]) -> System.Threading.Tasks.Task:
        """
        Creates a Task that executes an end method action
        when a specified IAsyncResult completes.
        
        :param async_result: The IAsyncResult whose completion should trigger the processing of the .
        :param end_method: The action delegate that processes the completed .
        :returns: A Task that represents the asynchronous operation.
        """
        ...

    @overload
    def from_async(self, async_result: System.IAsyncResult, end_method: typing.Callable[[System.IAsyncResult], None], creation_options: System.Threading.Tasks.TaskCreationOptions) -> System.Threading.Tasks.Task:
        """
        Creates a Task that executes an end method action
        when a specified IAsyncResult completes.
        
        :param async_result: The IAsyncResult whose completion should trigger the processing of the .
        :param end_method: The action delegate that processes the completed .
        :param creation_options: The TaskCreationOptions value that controls the behavior of the created Task.
        :returns: A Task that represents the asynchronous operation.
        """
        ...

    @overload
    def from_async(self, async_result: System.IAsyncResult, end_method: typing.Callable[[System.IAsyncResult], None], creation_options: System.Threading.Tasks.TaskCreationOptions, scheduler: System.Threading.Tasks.TaskScheduler) -> System.Threading.Tasks.Task:
        """
        Creates a Task that executes an end method action
        when a specified IAsyncResult completes.
        
        :param async_result: The IAsyncResult whose completion should trigger the processing of the .
        :param end_method: The action delegate that processes the completed .
        :param creation_options: The TaskCreationOptions value that controls the behavior of the created Task.
        :param scheduler: The TaskScheduler that is used to schedule the task that executes the end method.
        :returns: A Task that represents the asynchronous operation.
        """
        ...

    @overload
    def start_new(self, function: typing.Callable[[System.Object], System_Threading_Tasks_TaskFactory_TResult], state: typing.Any) -> System.Threading.Tasks.Task[System_Threading_Tasks_TaskFactory_TResult]:
        """
        Creates and starts a Task{TResult}.
        
        :param function: A function delegate that returns the future result to be available through the Task{TResult}.
        :param state: An object containing data to be used by the  delegate.
        :returns: The started Task{TResult}.
        """
        ...

    @overload
    def start_new(self, function: typing.Callable[[System.Object], System_Threading_Tasks_TaskFactory_TResult], state: typing.Any, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task[System_Threading_Tasks_TaskFactory_TResult]:
        """
        Creates and starts a Task{TResult}.
        
        :param function: A function delegate that returns the future result to be available through the Task{TResult}.
        :param state: An object containing data to be used by the  delegate.
        :param cancellation_token: The CancellationToken that will be assigned to the new task.
        :returns: The started Task{TResult}.
        """
        ...

    @overload
    def start_new(self, function: typing.Callable[[System.Object], System_Threading_Tasks_TaskFactory_TResult], state: typing.Any, creation_options: System.Threading.Tasks.TaskCreationOptions) -> System.Threading.Tasks.Task[System_Threading_Tasks_TaskFactory_TResult]:
        """
        Creates and starts a Task{TResult}.
        
        :param function: A function delegate that returns the future result to be available through the Task{TResult}.
        :param state: An object containing data to be used by the  delegate.
        :param creation_options: A TaskCreationOptions value that controls the behavior of the created Task{TResult}.
        :returns: The started Task{TResult}.
        """
        ...

    @overload
    def start_new(self, function: typing.Callable[[System.Object], System_Threading_Tasks_TaskFactory_TResult], state: typing.Any, cancellation_token: System.Threading.CancellationToken, creation_options: System.Threading.Tasks.TaskCreationOptions, scheduler: System.Threading.Tasks.TaskScheduler) -> System.Threading.Tasks.Task[System_Threading_Tasks_TaskFactory_TResult]:
        """
        Creates and starts a Task{TResult}.
        
        :param function: A function delegate that returns the future result to be available through the Task{TResult}.
        :param state: An object containing data to be used by the  delegate.
        :param cancellation_token: The CancellationToken that will be assigned to the new task.
        :param creation_options: A TaskCreationOptions value that controls the behavior of the created Task{TResult}.
        :param scheduler: The TaskScheduler that is used to schedule the created Task{TResult}.
        :returns: The started Task{TResult}.
        """
        ...

    @overload
    def start_new(self, action: typing.Callable[[System.Object], None], state: typing.Any) -> System.Threading.Tasks.Task:
        """
        Creates and starts a Task.
        
        :param action: The action delegate to execute asynchronously.
        :param state: An object containing data to be used by the  delegate.
        :returns: The started Task.
        """
        ...

    @overload
    def start_new(self, action: typing.Callable[[System.Object], None], state: typing.Any, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        """
        Creates and starts a Task.
        
        :param action: The action delegate to execute asynchronously.
        :param state: An object containing data to be used by the  delegate.
        :param cancellation_token: The CancellationToken that will be assigned to the new Task
        :returns: The started Task.
        """
        ...

    @overload
    def start_new(self, action: typing.Callable[[System.Object], None], state: typing.Any, creation_options: System.Threading.Tasks.TaskCreationOptions) -> System.Threading.Tasks.Task:
        """
        Creates and starts a Task.
        
        :param action: The action delegate to execute asynchronously.
        :param state: An object containing data to be used by the  delegate.
        :param creation_options: A TaskCreationOptions value that controls the behavior of the created Task
        :returns: The started Task.
        """
        ...

    @overload
    def start_new(self, action: typing.Callable[[System.Object], None], state: typing.Any, cancellation_token: System.Threading.CancellationToken, creation_options: System.Threading.Tasks.TaskCreationOptions, scheduler: System.Threading.Tasks.TaskScheduler) -> System.Threading.Tasks.Task:
        """
        Creates and starts a Task.
        
        :param action: The action delegate to execute asynchronously.
        :param state: An object containing data to be used by the  delegate.
        :param cancellation_token: The CancellationToken that will be assigned to the new task.
        :param creation_options: A TaskCreationOptions value that controls the behavior of the created Task
        :param scheduler: The TaskScheduler that is used to schedule the created Task.
        :returns: The started Task.
        """
        ...

    @overload
    def start_new(self, function: typing.Callable[[], System_Threading_Tasks_TaskFactory_TResult]) -> System.Threading.Tasks.Task[System_Threading_Tasks_TaskFactory_TResult]:
        """
        Creates and starts a Task{TResult}.
        
        :param function: A function delegate that returns the future result to be available through the Task{TResult}.
        :returns: The started Task{TResult}.
        """
        ...

    @overload
    def start_new(self, function: typing.Callable[[], System_Threading_Tasks_TaskFactory_TResult], cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task[System_Threading_Tasks_TaskFactory_TResult]:
        """
        Creates and starts a Task{TResult}.
        
        :param function: A function delegate that returns the future result to be available through the Task{TResult}.
        :param cancellation_token: The CancellationToken that will be assigned to the new task.
        :returns: The started Task{TResult}.
        """
        ...

    @overload
    def start_new(self, function: typing.Callable[[], System_Threading_Tasks_TaskFactory_TResult], creation_options: System.Threading.Tasks.TaskCreationOptions) -> System.Threading.Tasks.Task[System_Threading_Tasks_TaskFactory_TResult]:
        """
        Creates and starts a Task{TResult}.
        
        :param function: A function delegate that returns the future result to be available through the Task{TResult}.
        :param creation_options: A TaskCreationOptions value that controls the behavior of the created Task{TResult}.
        :returns: The started Task{TResult}.
        """
        ...

    @overload
    def start_new(self, function: typing.Callable[[], System_Threading_Tasks_TaskFactory_TResult], cancellation_token: System.Threading.CancellationToken, creation_options: System.Threading.Tasks.TaskCreationOptions, scheduler: System.Threading.Tasks.TaskScheduler) -> System.Threading.Tasks.Task[System_Threading_Tasks_TaskFactory_TResult]:
        """
        Creates and starts a Task{TResult}.
        
        :param function: A function delegate that returns the future result to be available through the Task{TResult}.
        :param cancellation_token: The CancellationToken that will be assigned to the new task.
        :param creation_options: A TaskCreationOptions value that controls the behavior of the created Task{TResult}.
        :param scheduler: The TaskScheduler that is used to schedule the created Task{TResult}.
        :returns: The started Task{TResult}.
        """
        ...

    @overload
    def start_new(self, action: typing.Callable[[], None]) -> System.Threading.Tasks.Task:
        """
        Creates and starts a Task.
        
        :param action: The action delegate to execute asynchronously.
        :returns: The started Task.
        """
        ...

    @overload
    def start_new(self, action: typing.Callable[[], None], cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        """
        Creates and starts a Task.
        
        :param action: The action delegate to execute asynchronously.
        :param cancellation_token: The CancellationToken that will be assigned to the new task.
        :returns: The started Task.
        """
        ...

    @overload
    def start_new(self, action: typing.Callable[[], None], creation_options: System.Threading.Tasks.TaskCreationOptions) -> System.Threading.Tasks.Task:
        """
        Creates and starts a Task.
        
        :param action: The action delegate to execute asynchronously.
        :param creation_options: A TaskCreationOptions value that controls the behavior of the created Task
        :returns: The started Task.
        """
        ...

    @overload
    def start_new(self, action: typing.Callable[[], None], cancellation_token: System.Threading.CancellationToken, creation_options: System.Threading.Tasks.TaskCreationOptions, scheduler: System.Threading.Tasks.TaskScheduler) -> System.Threading.Tasks.Task:
        """
        Creates and starts a Task.
        
        :param action: The action delegate to execute asynchronously.
        :param cancellation_token: The CancellationToken that will be assigned to the new Task
        :param creation_options: A TaskCreationOptions value that controls the behavior of the created Task
        :param scheduler: The TaskScheduler that is used to schedule the created Task.
        :returns: The started Task.
        """
        ...


class ValueTask(typing.Generic[System_Threading_Tasks_ValueTask_TResult], System.IEquatable[System_Threading_Tasks_ValueTask]):
    """Provides a value type that can represent a synchronously available value or a task object."""

    COMPLETED_TASK: System.Threading.Tasks.ValueTask
    """Gets a task that has already completed successfully."""

    @property
    def is_completed(self) -> bool:
        """Gets whether the ValueTask represents a completed operation."""
        ...

    @property
    def is_completed_successfully(self) -> bool:
        """Gets whether the ValueTask represents a successfully completed operation."""
        ...

    @property
    def is_faulted(self) -> bool:
        """Gets whether the ValueTask represents a failed operation."""
        ...

    @property
    def is_canceled(self) -> bool:
        """Gets whether the ValueTask represents a canceled operation."""
        ...

    @property
    def result(self) -> System_Threading_Tasks_ValueTask_TResult:
        """Gets the result."""
        ...

    @overload
    def __eq__(self, right: System.Threading.Tasks.ValueTask) -> bool:
        """Returns a value indicating whether two ValueTask values are equal."""
        ...

    @overload
    def __eq__(self, right: System.Threading.Tasks.ValueTask[System_Threading_Tasks_ValueTask_TResult]) -> bool:
        """Returns a value indicating whether two ValueTask{TResult} values are equal."""
        ...

    @overload
    def __init__(self, task: System.Threading.Tasks.Task) -> None:
        """
        Initialize the ValueTask with a Task that represents the operation.
        
        :param task: The task.
        """
        ...

    @overload
    def __init__(self, source: System.Threading.Tasks.Sources.IValueTaskSource, token: int) -> None:
        """
        Initialize the ValueTask with a IValueTaskSource object that represents the operation.
        
        :param source: The source.
        :param token: Opaque value passed through to the IValueTaskSource.
        """
        ...

    @overload
    def __init__(self, result: System_Threading_Tasks_ValueTask_TResult) -> None:
        """
        Initialize the ValueTask{TResult} with a TResult result value.
        
        :param result: The result.
        """
        ...

    @overload
    def __init__(self, task: System.Threading.Tasks.Task[System_Threading_Tasks_ValueTask_TResult]) -> None:
        """
        Initialize the ValueTask{TResult} with a Task{TResult} that represents the operation.
        
        :param task: The task.
        """
        ...

    @overload
    def __init__(self, source: System.Threading.Tasks.Sources.IValueTaskSource[System_Threading_Tasks_ValueTask_TResult], token: int) -> None:
        """
        Initialize the ValueTask{TResult} with a IValueTaskSource{TResult} object that represents the operation.
        
        :param source: The source.
        :param token: Opaque value passed through to the IValueTaskSource.
        """
        ...

    @overload
    def __ne__(self, right: System.Threading.Tasks.ValueTask) -> bool:
        """Returns a value indicating whether two ValueTask values are not equal."""
        ...

    @overload
    def __ne__(self, right: System.Threading.Tasks.ValueTask[System_Threading_Tasks_ValueTask_TResult]) -> bool:
        """Returns a value indicating whether two ValueTask{TResult} values are not equal."""
        ...

    def as_task(self) -> System.Threading.Tasks.Task:
        """Gets a Task object to represent this ValueTask."""
        ...

    def configure_await(self, continue_on_captured_context: bool) -> System.Runtime.CompilerServices.ConfiguredValueTaskAwaitable:
        """
        Configures an awaiter for this ValueTask.
        
        :param continue_on_captured_context: true to attempt to marshal the continuation back to the captured context; otherwise, false.
        """
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        """Returns a value indicating whether this value is equal to a specified object."""
        ...

    @overload
    def equals(self, other: System.Threading.Tasks.ValueTask) -> bool:
        """Returns a value indicating whether this value is equal to a specified ValueTask value."""
        ...

    @overload
    def equals(self, other: System.Threading.Tasks.ValueTask[System_Threading_Tasks_ValueTask_TResult]) -> bool:
        """Returns a value indicating whether this value is equal to a specified ValueTask{TResult} value."""
        ...

    @staticmethod
    def from_canceled(cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.ValueTask:
        """
        Creates a ValueTask that has completed due to cancellation with the specified cancellation token.
        
        :param cancellation_token: The cancellation token with which to complete the task.
        :returns: The canceled task.
        """
        ...

    @staticmethod
    def from_exception(exception: System.Exception) -> System.Threading.Tasks.ValueTask:
        """
        Creates a ValueTask that has completed with the specified exception.
        
        :param exception: The exception with which to complete the task.
        :returns: The faulted task.
        """
        ...

    def get_awaiter(self) -> System.Runtime.CompilerServices.ValueTaskAwaiter:
        """Gets an awaiter for this ValueTask."""
        ...

    def get_hash_code(self) -> int:
        """Returns the hash code for this instance."""
        ...

    def preserve(self) -> System.Threading.Tasks.ValueTask:
        """Gets a ValueTask that may be used at any point in the future."""
        ...

    def to_string(self) -> str:
        """Gets a string-representation of this ValueTask{TResult}."""
        ...


class _EventContainer(typing.Generic[System_Threading_Tasks__EventContainer_Callable, System_Threading_Tasks__EventContainer_ReturnType]):
    """This class is used to provide accurate autocomplete on events and cannot be imported."""

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> System_Threading_Tasks__EventContainer_ReturnType:
        """Fires the event."""
        ...

    def __iadd__(self, item: System_Threading_Tasks__EventContainer_Callable) -> typing.Self:
        """Registers an event handler."""
        ...

    def __isub__(self, item: System_Threading_Tasks__EventContainer_Callable) -> typing.Self:
        """Unregisters an event handler."""
        ...


