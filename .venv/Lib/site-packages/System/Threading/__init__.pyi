from typing import overload
from enum import Enum
import abc
import datetime
import typing
import warnings

import Microsoft.Win32.SafeHandles
import System
import System.Globalization
import System.Runtime.ConstrainedExecution
import System.Runtime.InteropServices
import System.Runtime.Serialization
import System.Security.Principal
import System.Threading
import System.Threading.Tasks

System_Threading_CancellationTokenRegistration = typing.Any
System_Threading_CancellationToken = typing.Any
System_Threading_AsyncFlowControl = typing.Any

System_Threading_ThreadLocal_T = typing.TypeVar("System_Threading_ThreadLocal_T")
System_Threading_AsyncLocal_T = typing.TypeVar("System_Threading_AsyncLocal_T")
System_Threading_AsyncLocalValueChangedArgs_T = typing.TypeVar("System_Threading_AsyncLocalValueChangedArgs_T")


class WaitHandle(System.MarshalByRefObject, System.IDisposable, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    INVALID_HANDLE: System.IntPtr = ...
    """This field is protected."""

    WAIT_TIMEOUT: int = ...

    @property
    def handle(self) -> System.IntPtr:
        """WaitHandle.Handle has been deprecated. Use the SafeWaitHandle property instead."""
        warnings.warn("WaitHandle.Handle has been deprecated. Use the SafeWaitHandle property instead.", DeprecationWarning)

    @handle.setter
    def handle(self, value: System.IntPtr) -> None:
        warnings.warn("WaitHandle.Handle has been deprecated. Use the SafeWaitHandle property instead.", DeprecationWarning)

    @property
    def safe_wait_handle(self) -> Microsoft.Win32.SafeHandles.SafeWaitHandle:
        ...

    @safe_wait_handle.setter
    def safe_wait_handle(self, value: Microsoft.Win32.SafeHandles.SafeWaitHandle) -> None:
        ...

    def __init__(self) -> None:
        """This method is protected."""
        ...

    def close(self) -> None:
        ...

    @overload
    def dispose(self, explicit_disposing: bool) -> None:
        """This method is protected."""
        ...

    @overload
    def dispose(self) -> None:
        ...

    @staticmethod
    @overload
    def signal_and_wait(to_signal: System.Threading.WaitHandle, to_wait_on: System.Threading.WaitHandle) -> bool:
        ...

    @staticmethod
    @overload
    def signal_and_wait(to_signal: System.Threading.WaitHandle, to_wait_on: System.Threading.WaitHandle, timeout: datetime.timedelta, exit_context: bool) -> bool:
        ...

    @staticmethod
    @overload
    def signal_and_wait(to_signal: System.Threading.WaitHandle, to_wait_on: System.Threading.WaitHandle, milliseconds_timeout: int, exit_context: bool) -> bool:
        ...

    @staticmethod
    @overload
    def wait_all(wait_handles: typing.List[System.Threading.WaitHandle], milliseconds_timeout: int) -> bool:
        ...

    @staticmethod
    @overload
    def wait_all(wait_handles: typing.List[System.Threading.WaitHandle], timeout: datetime.timedelta) -> bool:
        ...

    @staticmethod
    @overload
    def wait_all(wait_handles: typing.List[System.Threading.WaitHandle]) -> bool:
        ...

    @staticmethod
    @overload
    def wait_all(wait_handles: typing.List[System.Threading.WaitHandle], milliseconds_timeout: int, exit_context: bool) -> bool:
        ...

    @staticmethod
    @overload
    def wait_all(wait_handles: typing.List[System.Threading.WaitHandle], timeout: datetime.timedelta, exit_context: bool) -> bool:
        ...

    @staticmethod
    @overload
    def wait_any(wait_handles: typing.List[System.Threading.WaitHandle], milliseconds_timeout: int) -> int:
        ...

    @staticmethod
    @overload
    def wait_any(wait_handles: typing.List[System.Threading.WaitHandle], timeout: datetime.timedelta) -> int:
        ...

    @staticmethod
    @overload
    def wait_any(wait_handles: typing.List[System.Threading.WaitHandle]) -> int:
        ...

    @staticmethod
    @overload
    def wait_any(wait_handles: typing.List[System.Threading.WaitHandle], milliseconds_timeout: int, exit_context: bool) -> int:
        ...

    @staticmethod
    @overload
    def wait_any(wait_handles: typing.List[System.Threading.WaitHandle], timeout: datetime.timedelta, exit_context: bool) -> int:
        ...

    @overload
    def wait_one(self, milliseconds_timeout: int) -> bool:
        ...

    @overload
    def wait_one(self, timeout: datetime.timedelta) -> bool:
        ...

    @overload
    def wait_one(self) -> bool:
        ...

    @overload
    def wait_one(self, milliseconds_timeout: int, exit_context: bool) -> bool:
        ...

    @overload
    def wait_one(self, timeout: datetime.timedelta, exit_context: bool) -> bool:
        ...


class EventResetMode(Enum):
    """Indicates whether an EventWaitHandle is reset automatically or manually after receiving a signal."""

    AUTO_RESET = 0

    MANUAL_RESET = 1


class NamedWaitHandleOptions:
    """
    Represents a set of options for named synchronization objects that are wait handles and can be shared between processes,
    such as 'Mutex', 'Semaphore', and 'EventWaitHandle'.
    """

    @property
    def current_user_only(self) -> bool:
        """Indicates whether the named synchronization object should be limited in access to the current user."""
        ...

    @current_user_only.setter
    def current_user_only(self, value: bool) -> None:
        ...

    @property
    def current_session_only(self) -> bool:
        """Indicates whether the named synchronization object is intended to be used only within the current session."""
        ...

    @current_session_only.setter
    def current_session_only(self, value: bool) -> None:
        ...


class EventWaitHandle(System.Threading.WaitHandle):
    """This class has no documentation."""

    @overload
    def __init__(self, initial_state: bool, mode: System.Threading.EventResetMode) -> None:
        ...

    @overload
    def __init__(self, initial_state: bool, mode: System.Threading.EventResetMode, name: str, options: System.Threading.NamedWaitHandleOptions) -> None:
        """
        Creates a named or unnamed event, or opens a named event if a event with the name already exists.
        
        :param initial_state: True to initially set the event to a signaled state; false otherwise.
        :param mode: Indicates whether the event resets automatically or manually.
        :param name: The name, if the event is to be shared with other processes; otherwise, null or an empty string.
        :param options: Options for the named event. Defaulted options, such as when passing 'options: default' in C#, are 'CurrentUserOnly = true' and 'CurrentSessionOnly = true'. For more information, see 'NamedWaitHandleOptions'. The specified options may affect the namespace for the name, and access to the underlying event object.
        """
        ...

    @overload
    def __init__(self, initial_state: bool, mode: System.Threading.EventResetMode, name: str) -> None:
        ...

    @overload
    def __init__(self, initial_state: bool, mode: System.Threading.EventResetMode, name: str, options: System.Threading.NamedWaitHandleOptions, created_new: typing.Optional[bool]) -> typing.Tuple[None, bool]:
        """
        Creates a named or unnamed event, or opens a named event if a event with the name already exists.
        
        :param initial_state: True to initially set the event to a signaled state; false otherwise.
        :param mode: Indicates whether the event resets automatically or manually.
        :param name: The name, if the event is to be shared with other processes; otherwise, null or an empty string.
        :param options: Options for the named event. Defaulted options, such as when passing 'options: default' in C#, are 'CurrentUserOnly = true' and 'CurrentSessionOnly = true'. For more information, see 'NamedWaitHandleOptions'. The specified options may affect the namespace for the name, and access to the underlying event object.
        :param created_new: True if the event was created; false if an existing named event was opened.
        """
        ...

    @overload
    def __init__(self, initial_state: bool, mode: System.Threading.EventResetMode, name: str, created_new: typing.Optional[bool]) -> typing.Tuple[None, bool]:
        ...

    @staticmethod
    @overload
    def open_existing(name: str, options: System.Threading.NamedWaitHandleOptions) -> System.Threading.EventWaitHandle:
        """
        Opens an existing named event.
        
        :param name: The name of the event to be shared with other processes.
        :param options: Options for the named event. Defaulted options, such as when passing 'options: default' in C#, are 'CurrentUserOnly = true' and 'CurrentSessionOnly = true'. For more information, see 'NamedWaitHandleOptions'. The specified options may affect the namespace for the name, and access to the underlying event object.
        :returns: An object that represents the named event.
        """
        ...

    @staticmethod
    @overload
    def open_existing(name: str) -> System.Threading.EventWaitHandle:
        ...

    def reset(self) -> bool:
        ...

    def set(self) -> bool:
        ...

    @staticmethod
    @overload
    def try_open_existing(name: str, options: System.Threading.NamedWaitHandleOptions, result: typing.Optional[System.Threading.EventWaitHandle]) -> typing.Tuple[bool, System.Threading.EventWaitHandle]:
        """
        Tries to open an existing named event and returns a value indicating whether it was successful.
        
        :param name: The name of the event to be shared with other processes.
        :param options: Options for the named event. Defaulted options, such as when passing 'options: default' in C#, are 'CurrentUserOnly = true' and 'CurrentSessionOnly = true'. For more information, see 'NamedWaitHandleOptions'. The specified options may affect the namespace for the name, and access to the underlying event object.
        :param result: An object that represents the named event if the method returns true; otherwise, null.
        :returns: True if the named event was opened successfully; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def try_open_existing(name: str, result: typing.Optional[System.Threading.EventWaitHandle]) -> typing.Tuple[bool, System.Threading.EventWaitHandle]:
        ...


class AsyncFlowControl(System.IEquatable[System_Threading_AsyncFlowControl], System.IDisposable):
    """This class has no documentation."""

    def __eq__(self, b: System.Threading.AsyncFlowControl) -> bool:
        ...

    def __ne__(self, b: System.Threading.AsyncFlowControl) -> bool:
        ...

    def dispose(self) -> None:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, obj: System.Threading.AsyncFlowControl) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def undo(self) -> None:
        ...


class ExecutionContext(System.Object, System.IDisposable, System.Runtime.Serialization.ISerializable):
    """Manages the execution context for the current thread."""

    @staticmethod
    def capture() -> System.Threading.ExecutionContext:
        ...

    def create_copy(self) -> System.Threading.ExecutionContext:
        ...

    def dispose(self) -> None:
        ...

    def get_object_data(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """Obsoletions.LegacyFormatterImplMessage"""
        warnings.warn("Obsoletions.LegacyFormatterImplMessage", DeprecationWarning)

    @staticmethod
    def is_flow_suppressed() -> bool:
        ...

    @staticmethod
    def restore(execution_context: System.Threading.ExecutionContext) -> None:
        """
        Restores a captured execution context to on the current thread.
        
        :param execution_context: The ExecutionContext to set.
        """
        ...

    @staticmethod
    def restore_flow() -> None:
        ...

    @staticmethod
    def run(execution_context: System.Threading.ExecutionContext, callback: typing.Callable[[System.Object], None], state: typing.Any) -> None:
        ...

    @staticmethod
    def suppress_flow() -> System.Threading.AsyncFlowControl:
        ...


class ApartmentState(Enum):
    """This class has no documentation."""

    STA = 0

    MTA = 1

    UNKNOWN = 2


class ThreadPriority(Enum):
    """This class has no documentation."""

    LOWEST = 0

    BELOW_NORMAL = 1

    NORMAL = 2

    ABOVE_NORMAL = 3

    HIGHEST = 4


class ThreadState(Enum):
    """This class has no documentation."""

    RUNNING = 0

    STOP_REQUESTED = 1

    SUSPEND_REQUESTED = 2

    BACKGROUND = 4

    UNSTARTED = 8

    STOPPED = 16

    WAIT_SLEEP_JOIN = 32

    SUSPENDED = 64

    ABORT_REQUESTED = 128

    ABORTED = 256


class CompressedStack(System.Object, System.Runtime.Serialization.ISerializable):
    """This class has no documentation."""

    @staticmethod
    def capture() -> System.Threading.CompressedStack:
        ...

    def create_copy(self) -> System.Threading.CompressedStack:
        ...

    @staticmethod
    def get_compressed_stack() -> System.Threading.CompressedStack:
        ...

    def get_object_data(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """Obsoletions.LegacyFormatterImplMessage"""
        warnings.warn("Obsoletions.LegacyFormatterImplMessage", DeprecationWarning)

    @staticmethod
    def run(compressed_stack: System.Threading.CompressedStack, callback: typing.Callable[[System.Object], None], state: typing.Any) -> None:
        ...


class Thread(System.Runtime.ConstrainedExecution.CriticalFinalizerObject):
    """This class has no documentation."""

    @property
    def current_culture(self) -> System.Globalization.CultureInfo:
        ...

    @current_culture.setter
    def current_culture(self, value: System.Globalization.CultureInfo) -> None:
        ...

    @property
    def current_ui_culture(self) -> System.Globalization.CultureInfo:
        ...

    @current_ui_culture.setter
    def current_ui_culture(self, value: System.Globalization.CultureInfo) -> None:
        ...

    current_principal: System.Security.Principal.IPrincipal

    CURRENT_THREAD: System.Threading.Thread

    @property
    def execution_context(self) -> System.Threading.ExecutionContext:
        ...

    @property
    def name(self) -> str:
        ...

    @name.setter
    def name(self, value: str) -> None:
        ...

    @property
    def apartment_state(self) -> System.Threading.ApartmentState:
        """The ApartmentState property has been deprecated. Use GetApartmentState, SetApartmentState or TrySetApartmentState instead."""
        warnings.warn("The ApartmentState property has been deprecated. Use GetApartmentState, SetApartmentState or TrySetApartmentState instead.", DeprecationWarning)

    @apartment_state.setter
    def apartment_state(self, value: System.Threading.ApartmentState) -> None:
        warnings.warn("The ApartmentState property has been deprecated. Use GetApartmentState, SetApartmentState or TrySetApartmentState instead.", DeprecationWarning)

    @property
    def is_alive(self) -> bool:
        ...

    @property
    def is_background(self) -> bool:
        ...

    @is_background.setter
    def is_background(self, value: bool) -> None:
        ...

    @property
    def is_thread_pool_thread(self) -> bool:
        ...

    @property
    def managed_thread_id(self) -> int:
        ...

    @property
    def priority(self) -> System.Threading.ThreadPriority:
        ...

    @priority.setter
    def priority(self, value: System.Threading.ThreadPriority) -> None:
        ...

    @property
    def thread_state(self) -> System.Threading.ThreadState:
        ...

    @overload
    def __init__(self, start: typing.Callable[[], None]) -> None:
        ...

    @overload
    def __init__(self, start: typing.Callable[[], None], max_stack_size: int) -> None:
        ...

    @overload
    def __init__(self, start: typing.Callable[[System.Object], None]) -> None:
        ...

    @overload
    def __init__(self, start: typing.Callable[[System.Object], None], max_stack_size: int) -> None:
        ...

    @overload
    def abort(self, state_info: typing.Any) -> None:
        """Obsoletions.ThreadAbortMessage"""
        ...

    @overload
    def abort(self) -> None:
        """Obsoletions.ThreadAbortMessage"""
        ...

    @staticmethod
    def allocate_data_slot() -> System.LocalDataStoreSlot:
        ...

    @staticmethod
    def allocate_named_data_slot(name: str) -> System.LocalDataStoreSlot:
        ...

    @staticmethod
    def begin_critical_region() -> None:
        ...

    @staticmethod
    def begin_thread_affinity() -> None:
        ...

    def disable_com_object_eager_cleanup(self) -> None:
        ...

    @staticmethod
    def end_critical_region() -> None:
        ...

    @staticmethod
    def end_thread_affinity() -> None:
        ...

    @staticmethod
    def free_named_data_slot(name: str) -> None:
        ...

    def get_apartment_state(self) -> System.Threading.ApartmentState:
        ...

    def get_compressed_stack(self) -> System.Threading.CompressedStack:
        """Obsoletions.CodeAccessSecurityMessage"""
        warnings.warn("Obsoletions.CodeAccessSecurityMessage", DeprecationWarning)

    @staticmethod
    def get_current_processor_id() -> int:
        ...

    @staticmethod
    def get_data(slot: System.LocalDataStoreSlot) -> System.Object:
        ...

    @staticmethod
    def get_domain() -> System.AppDomain:
        ...

    @staticmethod
    def get_domain_id() -> int:
        ...

    def get_hash_code(self) -> int:
        ...

    @staticmethod
    def get_named_data_slot(name: str) -> System.LocalDataStoreSlot:
        ...

    def interrupt(self) -> None:
        ...

    @overload
    def join(self) -> None:
        ...

    @overload
    def join(self, timeout: datetime.timedelta) -> bool:
        ...

    @overload
    def join(self, milliseconds_timeout: int) -> bool:
        ...

    @staticmethod
    def memory_barrier() -> None:
        ...

    @staticmethod
    def reset_abort() -> None:
        """Obsoletions.ThreadResetAbortMessage"""
        warnings.warn("Obsoletions.ThreadResetAbortMessage", DeprecationWarning)

    def resume(self) -> None:
        """Thread.Resume has been deprecated. Use other classes in System.Threading, such as Monitor, Mutex, Event, and Semaphore, to synchronize Threads or protect resources."""
        warnings.warn("Thread.Resume has been deprecated. Use other classes in System.Threading, such as Monitor, Mutex, Event, and Semaphore, to synchronize Threads or protect resources.", DeprecationWarning)

    def set_apartment_state(self, state: System.Threading.ApartmentState) -> None:
        ...

    def set_compressed_stack(self, stack: System.Threading.CompressedStack) -> None:
        """Obsoletions.CodeAccessSecurityMessage"""
        warnings.warn("Obsoletions.CodeAccessSecurityMessage", DeprecationWarning)

    @staticmethod
    def set_data(slot: System.LocalDataStoreSlot, data: typing.Any) -> None:
        ...

    @staticmethod
    @overload
    def sleep(milliseconds_timeout: int) -> None:
        ...

    @staticmethod
    @overload
    def sleep(timeout: datetime.timedelta) -> None:
        ...

    @staticmethod
    def spin_wait(iterations: int) -> None:
        ...

    @overload
    def start(self, parameter: typing.Any) -> None:
        """
        Causes the operating system to change the state of the current instance to ThreadState.Running, and optionally supplies an object containing data to be used by the method the thread executes.
        
        :param parameter: An object that contains data to be used by the method the thread executes.
        """
        ...

    @overload
    def start(self) -> None:
        """Causes the operating system to change the state of the current instance to ThreadState.Running."""
        ...

    def suspend(self) -> None:
        """Thread.Suspend has been deprecated. Use other classes in System.Threading, such as Monitor, Mutex, Event, and Semaphore, to synchronize Threads or protect resources."""
        warnings.warn("Thread.Suspend has been deprecated. Use other classes in System.Threading, such as Monitor, Mutex, Event, and Semaphore, to synchronize Threads or protect resources.", DeprecationWarning)

    def try_set_apartment_state(self, state: System.Threading.ApartmentState) -> bool:
        ...

    @overload
    def unsafe_start(self, parameter: typing.Any) -> None:
        """
        Causes the operating system to change the state of the current instance to ThreadState.Running, and optionally supplies an object containing data to be used by the method the thread executes.
        
        :param parameter: An object that contains data to be used by the method the thread executes.
        """
        ...

    @overload
    def unsafe_start(self) -> None:
        """Causes the operating system to change the state of the current instance to ThreadState.Running."""
        ...

    @staticmethod
    @overload
    def volatile_read(address: typing.Any) -> System.Object:
        """Obsoletions.ThreadVolatileReadWriteMessage"""
        ...

    @staticmethod
    @overload
    def volatile_read(address: int) -> int:
        """Obsoletions.ThreadVolatileReadWriteMessage"""
        ...

    @staticmethod
    @overload
    def volatile_read(address: float) -> float:
        """Obsoletions.ThreadVolatileReadWriteMessage"""
        ...

    @staticmethod
    @overload
    def volatile_read(address: System.IntPtr) -> System.IntPtr:
        """Obsoletions.ThreadVolatileReadWriteMessage"""
        ...

    @staticmethod
    @overload
    def volatile_read(address: System.UIntPtr) -> System.UIntPtr:
        """Obsoletions.ThreadVolatileReadWriteMessage"""
        ...

    @staticmethod
    @overload
    def volatile_write(address: typing.Any, value: typing.Any) -> None:
        """Obsoletions.ThreadVolatileReadWriteMessage"""
        ...

    @staticmethod
    @overload
    def volatile_write(address: int, value: int) -> None:
        """Obsoletions.ThreadVolatileReadWriteMessage"""
        ...

    @staticmethod
    @overload
    def volatile_write(address: float, value: float) -> None:
        """Obsoletions.ThreadVolatileReadWriteMessage"""
        ...

    @staticmethod
    @overload
    def volatile_write(address: System.IntPtr, value: System.IntPtr) -> None:
        """Obsoletions.ThreadVolatileReadWriteMessage"""
        ...

    @staticmethod
    @overload
    def volatile_write(address: System.UIntPtr, value: System.UIntPtr) -> None:
        """Obsoletions.ThreadVolatileReadWriteMessage"""
        ...

    @staticmethod
    def Yield() -> bool:
        ...


class PreAllocatedOverlapped(System.Object, System.IDisposable, System.Threading.IDeferredDisposable):
    """Represents pre-allocated state for native overlapped I/O operations."""

    def __init__(self, callback: typing.Callable[[int, int, typing.Any], None], state: typing.Any, pin_data: typing.Any) -> None:
        """
        Initializes a new instance of the PreAllocatedOverlapped class, specifying
            a delegate that is invoked when each asynchronous I/O operation is complete, a user-provided
            object providing context, and managed objects that serve as buffers.
        
        :param callback: An IOCompletionCallback delegate that represents the callback method     invoked when each asynchronous I/O operation completes.
        :param state: A user-provided object that distinguishes NativeOverlapped instance produced from this     object from other NativeOverlapped instances. Can be null.
        :param pin_data: An object or array of objects representing the input or output buffer for the operations. Each     object represents a buffer, for example an array of bytes.  Can be null.
        """
        ...

    def dispose(self) -> None:
        """Frees the resources associated with this PreAllocatedOverlapped instance."""
        ...

    @staticmethod
    def unsafe_create(callback: typing.Callable[[int, int, typing.Any], None], state: typing.Any, pin_data: typing.Any) -> System.Threading.PreAllocatedOverlapped:
        """
        Initializes a new instance of the PreAllocatedOverlapped class, specifying
            a delegate that is invoked when each asynchronous I/O operation is complete, a user-provided
            object providing context, and managed objects that serve as buffers.
        
        :param callback: An IOCompletionCallback delegate that represents the callback method     invoked when each asynchronous I/O operation completes.
        :param state: A user-provided object that distinguishes NativeOverlapped instance produced from this     object from other NativeOverlapped instances. Can be null.
        :param pin_data: An object or array of objects representing the input or output buffer for the operations. Each     object represents a buffer, for example an array of bytes.  Can be null.
        """
        ...


class ThreadPoolBoundHandle(System.Object, System.IDisposable, System.Threading.IDeferredDisposable):
    """
    Represents an I/O handle that is bound to the system thread pool and enables low-level
        components to receive notifications for asynchronous I/O operations.
    """

    @property
    def handle(self) -> System.Runtime.InteropServices.SafeHandle:
        """Gets the bound operating system handle."""
        ...

    @overload
    def allocate_native_overlapped(self, callback: typing.Callable[[int, int, typing.Any], None], state: typing.Any, pin_data: typing.Any) -> typing.Any:
        """
        Returns an unmanaged pointer to a NativeOverlapped structure, specifying
            a delegate that is invoked when the asynchronous I/O operation is complete, a user-provided
            object providing context, and managed objects that serve as buffers.
        
        :param callback: An IOCompletionCallback delegate that represents the callback method     invoked when the asynchronous I/O operation completes.
        :param state: A user-provided object that distinguishes this NativeOverlapped from other     NativeOverlapped instances. Can be null.
        :param pin_data: An object or array of objects representing the input or output buffer for the operation. Each     object represents a buffer, for example an array of bytes.  Can be null.
        :returns: An unmanaged pointer to a NativeOverlapped structure.
        """
        ...

    @overload
    def allocate_native_overlapped(self, pre_allocated: System.Threading.PreAllocatedOverlapped) -> typing.Any:
        """
        Returns an unmanaged pointer to a NativeOverlapped structure, using the callback,
            state, and buffers associated with the specified PreAllocatedOverlapped object.
        
        :param pre_allocated: A PreAllocatedOverlapped object from which to create the NativeOverlapped pointer.
        :returns: An unmanaged pointer to a NativeOverlapped structure.
        """
        ...

    @staticmethod
    def bind_handle(handle: System.Runtime.InteropServices.SafeHandle) -> System.Threading.ThreadPoolBoundHandle:
        """
        Returns a ThreadPoolBoundHandle for the specific handle,
            which is bound to the system thread pool.
        
        :param handle: A SafeHandle object that holds the operating system handle. The     handle must have been opened for overlapped I/O on the unmanaged side.
        :returns: ThreadPoolBoundHandle for , which     is bound to the system thread pool.
        """
        ...

    def dispose(self) -> None:
        ...

    def free_native_overlapped(self, overlapped: typing.Any) -> None:
        """
        Frees the unmanaged memory associated with a NativeOverlapped structure
            allocated by the AllocateNativeOverlapped method.
        
        :param overlapped: An unmanaged pointer to the NativeOverlapped structure to be freed.
        """
        ...

    @staticmethod
    def get_native_overlapped_state(overlapped: typing.Any) -> System.Object:
        """
        Returns the user-provided object specified when the NativeOverlapped instance was
            allocated using the AllocateNativeOverlapped(IOCompletionCallback, object, object).
        
        :param overlapped: An unmanaged pointer to the NativeOverlapped structure from which to return the     associated user-provided object.
        :returns: A user-provided object that distinguishes this NativeOverlapped     from other NativeOverlapped instances, otherwise, null if one was     not specified when the instance was allocated using AllocateNativeOverlapped.
        """
        ...

    def unsafe_allocate_native_overlapped(self, callback: typing.Callable[[int, int, typing.Any], None], state: typing.Any, pin_data: typing.Any) -> typing.Any:
        """
        Returns an unmanaged pointer to a NativeOverlapped structure, specifying
            a delegate that is invoked when the asynchronous I/O operation is complete, a user-provided
            object providing context, and managed objects that serve as buffers.
        
        :param callback: An IOCompletionCallback delegate that represents the callback method     invoked when the asynchronous I/O operation completes.
        :param state: A user-provided object that distinguishes this NativeOverlapped from other     NativeOverlapped instances. Can be null.
        :param pin_data: An object or array of objects representing the input or output buffer for the operation. Each     object represents a buffer, for example an array of bytes.  Can be null.
        :returns: An unmanaged pointer to a NativeOverlapped structure.
        """
        ...


class CancellationToken(System.IEquatable[System_Threading_CancellationToken]):
    """Propagates notification that operations should be canceled."""

    NONE: System.Threading.CancellationToken
    """Returns an empty CancellationToken value."""

    @property
    def is_cancellation_requested(self) -> bool:
        """Gets whether cancellation has been requested for this token."""
        ...

    @property
    def can_be_canceled(self) -> bool:
        """Gets whether this token is capable of being in the canceled state."""
        ...

    @property
    def wait_handle(self) -> System.Threading.WaitHandle:
        """Gets a Threading.WaitHandle that is signaled when the token is canceled."""
        ...

    def __eq__(self, right: System.Threading.CancellationToken) -> bool:
        """
        Determines whether two CancellationToken instances are equal.
        
        :param left: The first instance.
        :param right: The second instance.
        :returns: True if the instances are equal; otherwise, false.
        """
        ...

    def __init__(self, canceled: bool) -> None:
        """
        Initializes the CancellationToken.
        
        :param canceled: The canceled state for the token.
        """
        ...

    def __ne__(self, right: System.Threading.CancellationToken) -> bool:
        """
        Determines whether two CancellationToken instances are not equal.
        
        :param left: The first instance.
        :param right: The second instance.
        :returns: True if the instances are not equal; otherwise, false.
        """
        ...

    @overload
    def equals(self, other: typing.Any) -> bool:
        """
        Determines whether the current CancellationToken instance is equal to the
        specified object.
        
        :param other: The other object to which to compare this instance.
        :returns: True if  is a CancellationToken and if the two instances are equal; otherwise, false. Two tokens are equal if they are associated with the same CancellationTokenSource or if they were both constructed from public CancellationToken constructors and their IsCancellationRequested values are equal.
        """
        ...

    @overload
    def equals(self, other: System.Threading.CancellationToken) -> bool:
        """
        Determines whether the current CancellationToken instance is equal to the
        specified token.
        
        :param other: The other CancellationToken to which to compare this instance.
        :returns: True if the instances are equal; otherwise, false. Two tokens are equal if they are associated with the same CancellationTokenSource or if they were both constructed from public CancellationToken constructors and their IsCancellationRequested values are equal.
        """
        ...

    def get_hash_code(self) -> int:
        """
        Serves as a hash function for a CancellationToken.
        
        :returns: A hash code for the current CancellationToken instance.
        """
        ...

    @overload
    def register(self, callback: typing.Callable[[System.Object], None], state: typing.Any) -> System.Threading.CancellationTokenRegistration:
        """
        Registers a delegate that will be called when this
        CancellationToken is canceled.
        
        :param callback: The delegate to be executed when the CancellationToken is canceled.
        :param state: The state to pass to the  when the delegate is invoked.  This may be null.
        :returns: The CancellationTokenRegistration instance that can be used to unregister the callback.
        """
        ...

    @overload
    def register(self, callback: typing.Callable[[System.Object, System.Threading.CancellationToken], None], state: typing.Any) -> System.Threading.CancellationTokenRegistration:
        """
        Registers a delegate that will be called when this CancellationToken is canceled.
        
        :param callback: The delegate to be executed when the CancellationToken is canceled.
        :param state: The state to pass to the  when the delegate is invoked.  This may be null.
        :returns: The CancellationTokenRegistration instance that can be used to unregister the callback.
        """
        ...

    @overload
    def register(self, callback: typing.Callable[[System.Object], None], state: typing.Any, use_synchronization_context: bool) -> System.Threading.CancellationTokenRegistration:
        """
        Registers a delegate that will be called when this
        CancellationToken is canceled.
        
        :param callback: The delegate to be executed when the CancellationToken is canceled.
        :param state: The state to pass to the  when the delegate is invoked.  This may be null.
        :param use_synchronization_context: A Boolean value that indicates whether to capture the current SynchronizationContext and use it when invoking the .
        :returns: The CancellationTokenRegistration instance that can be used to unregister the callback.
        """
        ...

    @overload
    def register(self, callback: typing.Callable[[], None]) -> System.Threading.CancellationTokenRegistration:
        """
        Registers a delegate that will be called when this CancellationToken is canceled.
        
        :param callback: The delegate to be executed when the CancellationToken is canceled.
        :returns: The CancellationTokenRegistration instance that can be used to unregister the callback.
        """
        ...

    @overload
    def register(self, callback: typing.Callable[[], None], use_synchronization_context: bool) -> System.Threading.CancellationTokenRegistration:
        """
        Registers a delegate that will be called when this
        CancellationToken is canceled.
        
        :param callback: The delegate to be executed when the CancellationToken is canceled.
        :param use_synchronization_context: A Boolean value that indicates whether to capture the current SynchronizationContext and use it when invoking the .
        :returns: The CancellationTokenRegistration instance that can be used to unregister the callback.
        """
        ...

    def throw_if_cancellation_requested(self) -> None:
        """
        Throws a OperationCanceledException if
        this token has had cancellation requested.
        """
        ...

    @overload
    def unsafe_register(self, callback: typing.Callable[[System.Object], None], state: typing.Any) -> System.Threading.CancellationTokenRegistration:
        """
        Registers a delegate that will be called when this
        CancellationToken is canceled.
        
        :param callback: The delegate to be executed when the CancellationToken is canceled.
        :param state: The state to pass to the  when the delegate is invoked.  This may be null.
        :returns: The CancellationTokenRegistration instance that can be used to unregister the callback.
        """
        ...

    @overload
    def unsafe_register(self, callback: typing.Callable[[System.Object, System.Threading.CancellationToken], None], state: typing.Any) -> System.Threading.CancellationTokenRegistration:
        """
        Registers a delegate that will be called when this CancellationToken is canceled.
        
        :param callback: The delegate to be executed when the CancellationToken is canceled.
        :param state: The state to pass to the  when the delegate is invoked.  This may be null.
        :returns: The CancellationTokenRegistration instance that can be used to unregister the callback.
        """
        ...


class CancellationTokenRegistration(System.IEquatable[System_Threading_CancellationTokenRegistration], System.IDisposable, System.IAsyncDisposable):
    """Represents a callback delegate that has been registered with a CancellationToken."""

    @property
    def token(self) -> System.Threading.CancellationToken:
        """Gets the CancellationToken with which this registration is associated."""
        ...

    def __eq__(self, right: System.Threading.CancellationTokenRegistration) -> bool:
        """
        Determines whether two CancellationTokenRegistration
        instances are equal.
        
        :param left: The first instance.
        :param right: The second instance.
        :returns: True if the instances are equal; otherwise, false.
        """
        ...

    def __ne__(self, right: System.Threading.CancellationTokenRegistration) -> bool:
        """
        Determines whether two CancellationTokenRegistration instances are not equal.
        
        :param left: The first instance.
        :param right: The second instance.
        :returns: True if the instances are not equal; otherwise, false.
        """
        ...

    def dispose(self) -> None:
        """
        Disposes of the registration and unregisters the target callback from the associated
        CancellationToken.
        If the target callback is currently executing, this method will wait until it completes, except
        in the degenerate cases where a callback method unregisters itself.
        """
        ...

    def dispose_async(self) -> System.Threading.Tasks.ValueTask:
        """
        Disposes of the registration and unregisters the target callback from the associated
        CancellationToken.
        The returned ValueTask will complete once the associated callback
        is unregistered without having executed or once it's finished executing, except
        in the degenerate case where the callback itself is unregistering itself.
        """
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        """
        Determines whether the current CancellationTokenRegistration instance is equal to the
        specified object.
        
        :param obj: The other object to which to compare this instance.
        :returns: True, if both this and  are equal. False, otherwise. Two CancellationTokenRegistration instances are equal if they both refer to the output of a single call to the same Register method of a CancellationToken.
        """
        ...

    @overload
    def equals(self, other: System.Threading.CancellationTokenRegistration) -> bool:
        """
        Determines whether the current CancellationToken instance is equal to the
        specified object.
        
        :param other: The other CancellationTokenRegistration to which to compare this instance.
        :returns: True, if both this and  are equal. False, otherwise. Two CancellationTokenRegistration instances are equal if they both refer to the output of a single call to the same Register method of a CancellationToken.
        """
        ...

    def get_hash_code(self) -> int:
        """
        Serves as a hash function for a CancellationTokenRegistration.
        
        :returns: A hash code for the current CancellationTokenRegistration instance.
        """
        ...

    def unregister(self) -> bool:
        """
        Disposes of the registration and unregisters the target callback from the associated
        CancellationToken.
        """
        ...


class RegisteredWaitHandle(System.MarshalByRefObject):
    """An object representing the registration of a WaitHandle via ThreadPool.RegisterWaitForSingleObject."""

    def unregister(self, wait_object: System.Threading.WaitHandle) -> bool:
        ...


class IThreadPoolWorkItem(metaclass=abc.ABCMeta):
    """Represents a work item that can be executed by the ThreadPool."""

    def execute(self) -> None:
        ...


class ThreadPool(System.Object):
    """This class has no documentation."""

    THREAD_COUNT: int
    """Gets the number of thread pool threads that currently exist."""

    COMPLETED_WORK_ITEM_COUNT: int
    """Gets the number of work items that have been processed so far."""

    PENDING_WORK_ITEM_COUNT: int
    """Gets the number of work items that are currently queued to be processed."""

    @staticmethod
    @overload
    def bind_handle(os_handle: System.Runtime.InteropServices.SafeHandle) -> bool:
        ...

    @staticmethod
    @overload
    def bind_handle(os_handle: System.IntPtr) -> bool:
        """ThreadPool.BindHandle(IntPtr) has been deprecated. Use ThreadPool.BindHandle(SafeHandle) instead."""
        ...

    @staticmethod
    def get_available_threads(worker_threads: typing.Optional[int], completion_port_threads: typing.Optional[int]) -> typing.Tuple[None, int, int]:
        ...

    @staticmethod
    def get_max_threads(worker_threads: typing.Optional[int], completion_port_threads: typing.Optional[int]) -> typing.Tuple[None, int, int]:
        ...

    @staticmethod
    def get_min_threads(worker_threads: typing.Optional[int], completion_port_threads: typing.Optional[int]) -> typing.Tuple[None, int, int]:
        ...

    @staticmethod
    @overload
    def queue_user_work_item(call_back: typing.Callable[[System.Object], None], state: typing.Any) -> bool:
        ...

    @staticmethod
    @overload
    def queue_user_work_item(call_back: typing.Callable[[System.Object], None]) -> bool:
        ...

    @staticmethod
    @overload
    def register_wait_for_single_object(wait_object: System.Threading.WaitHandle, call_back: typing.Callable[[System.Object, bool], None], state: typing.Any, milliseconds_time_out_interval: int, execute_only_once: bool) -> System.Threading.RegisteredWaitHandle:
        ...

    @staticmethod
    @overload
    def register_wait_for_single_object(wait_object: System.Threading.WaitHandle, call_back: typing.Callable[[System.Object, bool], None], state: typing.Any, timeout: datetime.timedelta, execute_only_once: bool) -> System.Threading.RegisteredWaitHandle:
        ...

    @staticmethod
    def set_max_threads(worker_threads: int, completion_port_threads: int) -> bool:
        ...

    @staticmethod
    def set_min_threads(worker_threads: int, completion_port_threads: int) -> bool:
        ...

    @staticmethod
    def unsafe_queue_native_overlapped(overlapped: typing.Any) -> bool:
        ...

    @staticmethod
    @overload
    def unsafe_queue_user_work_item(call_back: typing.Callable[[System.Object], None], state: typing.Any) -> bool:
        ...

    @staticmethod
    @overload
    def unsafe_queue_user_work_item(call_back: System.Threading.IThreadPoolWorkItem, prefer_local: bool) -> bool:
        ...

    @staticmethod
    @overload
    def unsafe_register_wait_for_single_object(wait_object: System.Threading.WaitHandle, call_back: typing.Callable[[System.Object, bool], None], state: typing.Any, milliseconds_time_out_interval: int, execute_only_once: bool) -> System.Threading.RegisteredWaitHandle:
        ...

    @staticmethod
    @overload
    def unsafe_register_wait_for_single_object(wait_object: System.Threading.WaitHandle, call_back: typing.Callable[[System.Object, bool], None], state: typing.Any, timeout: datetime.timedelta, execute_only_once: bool) -> System.Threading.RegisteredWaitHandle:
        ...


class SemaphoreSlim(System.Object, System.IDisposable):
    """Limits the number of threads that can access a resource or pool of resources concurrently."""

    @property
    def current_count(self) -> int:
        """Gets the current count of the SemaphoreSlim."""
        ...

    @property
    def available_wait_handle(self) -> System.Threading.WaitHandle:
        """Returns a WaitHandle that can be used to wait on the semaphore."""
        ...

    @overload
    def __init__(self, initial_count: int) -> None:
        ...

    @overload
    def __init__(self, initial_count: int, max_count: int) -> None:
        """
        Initializes a new instance of the SemaphoreSlim class, specifying
        the initial and maximum number of requests that can be granted concurrently.
        
        :param initial_count: The initial number of requests for the semaphore that can be granted concurrently.
        :param max_count: The maximum number of requests for the semaphore that can be granted concurrently.
        """
        ...

    @overload
    def dispose(self) -> None:
        """Releases all resources used by the current instance of SemaphoreSlim."""
        ...

    @overload
    def dispose(self, disposing: bool) -> None:
        """
        When overridden in a derived class, releases the unmanaged resources used by the
        ManualResetEventSlim, and optionally releases the managed resources.
        
        This method is protected.
        
        :param disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
        """
        ...

    @overload
    def release(self) -> int:
        """
        Exits the SemaphoreSlim once.
        
        :returns: The previous count of the SemaphoreSlim.
        """
        ...

    @overload
    def release(self, release_count: int) -> int:
        """
        Exits the SemaphoreSlim a specified number of times.
        
        :param release_count: The number of times to exit the semaphore.
        :returns: The previous count of the SemaphoreSlim.
        """
        ...

    @overload
    def wait(self) -> None:
        ...

    @overload
    def wait(self, cancellation_token: System.Threading.CancellationToken) -> None:
        """
        Blocks the current thread until it can enter the SemaphoreSlim, while observing a
        CancellationToken.
        
        :param cancellation_token: The CancellationToken token to observe.
        """
        ...

    @overload
    def wait(self, timeout: datetime.timedelta) -> bool:
        """
        Blocks the current thread until it can enter the SemaphoreSlim, using a TimeSpan to measure the time interval.
        
        :param timeout: A TimeSpan that represents the number of milliseconds to wait, or a TimeSpan that represents -1 milliseconds to wait indefinitely.
        :returns: true if the current thread successfully entered the SemaphoreSlim; otherwise, false.
        """
        ...

    @overload
    def wait(self, timeout: datetime.timedelta, cancellation_token: System.Threading.CancellationToken) -> bool:
        """
        Blocks the current thread until it can enter the SemaphoreSlim, using a TimeSpan to measure the time interval, while observing a CancellationToken.
        
        :param timeout: A TimeSpan that represents the number of milliseconds to wait, or a TimeSpan that represents -1 milliseconds to wait indefinitely.
        :param cancellation_token: The CancellationToken to observe.
        :returns: true if the current thread successfully entered the SemaphoreSlim; otherwise, false.
        """
        ...

    @overload
    def wait(self, milliseconds_timeout: int) -> bool:
        """
        Blocks the current thread until it can enter the SemaphoreSlim, using a 32-bit
        signed integer to measure the time interval.
        
        :param milliseconds_timeout: The number of milliseconds to wait, or Timeout.Infinite(-1) to wait indefinitely.
        :returns: true if the current thread successfully entered the SemaphoreSlim; otherwise, false.
        """
        ...

    @overload
    def wait(self, milliseconds_timeout: int, cancellation_token: System.Threading.CancellationToken) -> bool:
        """
        Blocks the current thread until it can enter the SemaphoreSlim,
        using a 32-bit signed integer to measure the time interval,
        while observing a CancellationToken.
        
        :param milliseconds_timeout: The number of milliseconds to wait, or Timeout.Infinite(-1) to wait indefinitely.
        :param cancellation_token: The CancellationToken to observe.
        :returns: true if the current thread successfully entered the SemaphoreSlim; otherwise, false.
        """
        ...

    @overload
    def wait_async(self) -> System.Threading.Tasks.Task:
        """
        Asynchronously waits to enter the SemaphoreSlim.
        
        :returns: A task that will complete when the semaphore has been entered.
        """
        ...

    @overload
    def wait_async(self, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        """
        Asynchronously waits to enter the SemaphoreSlim, while observing a
        CancellationToken.
        
        :param cancellation_token: The CancellationToken token to observe.
        :returns: A task that will complete when the semaphore has been entered.
        """
        ...

    @overload
    def wait_async(self, milliseconds_timeout: int) -> System.Threading.Tasks.Task[bool]:
        """
        Asynchronously waits to enter the SemaphoreSlim,
        using a 32-bit signed integer to measure the time interval.
        
        :param milliseconds_timeout: The number of milliseconds to wait, or Timeout.Infinite(-1) to wait indefinitely.
        :returns: A task that will complete with a result of true if the current thread successfully entered the SemaphoreSlim, otherwise with a result of false.
        """
        ...

    @overload
    def wait_async(self, timeout: datetime.timedelta) -> System.Threading.Tasks.Task[bool]:
        """
        Asynchronously waits to enter the SemaphoreSlim, using a TimeSpan to measure the time interval, while observing a
        CancellationToken.
        
        :param timeout: A TimeSpan that represents the number of milliseconds to wait, or a TimeSpan that represents -1 milliseconds to wait indefinitely.
        :returns: A task that will complete with a result of true if the current thread successfully entered the SemaphoreSlim, otherwise with a result of false.
        """
        ...

    @overload
    def wait_async(self, timeout: datetime.timedelta, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task[bool]:
        """
        Asynchronously waits to enter the SemaphoreSlim, using a TimeSpan to measure the time interval.
        
        :param timeout: A TimeSpan that represents the number of milliseconds to wait, or a TimeSpan that represents -1 milliseconds to wait indefinitely.
        :param cancellation_token: The CancellationToken token to observe.
        :returns: A task that will complete with a result of true if the current thread successfully entered the SemaphoreSlim, otherwise with a result of false.
        """
        ...

    @overload
    def wait_async(self, milliseconds_timeout: int, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task[bool]:
        """
        Asynchronously waits to enter the SemaphoreSlim,
        using a 32-bit signed integer to measure the time interval,
        while observing a CancellationToken.
        
        :param milliseconds_timeout: The number of milliseconds to wait, or Timeout.Infinite(-1) to wait indefinitely.
        :param cancellation_token: The CancellationToken to observe.
        :returns: A task that will complete with a result of true if the current thread successfully entered the SemaphoreSlim, otherwise with a result of false.
        """
        ...


class ThreadInterruptedException(System.SystemException):
    """An exception class to indicate that the thread was interrupted from a waiting state."""

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


class Semaphore(System.Threading.WaitHandle):
    """This class has no documentation."""

    @overload
    def __init__(self, initial_count: int, maximum_count: int) -> None:
        ...

    @overload
    def __init__(self, initial_count: int, maximum_count: int, name: str, options: System.Threading.NamedWaitHandleOptions) -> None:
        """
        Creates a named or unnamed semaphore, or opens a named semaphore if a semaphore with the name already exists.
        
        :param initial_count: The initial number of requests for the semaphore that can be satisfied concurrently.
        :param maximum_count: The maximum number of requests for the semaphore that can be satisfied concurrently.
        :param name: The name, if the semaphore is to be shared with other processes; otherwise, null or an empty string.
        :param options: Options for the named semaphore. Defaulted options, such as when passing 'options: default' in C#, are 'CurrentUserOnly = true' and 'CurrentSessionOnly = true'. For more information, see 'NamedWaitHandleOptions'. The specified options may affect the namespace for the name, and access to the underlying semaphore object.
        """
        ...

    @overload
    def __init__(self, initial_count: int, maximum_count: int, name: str) -> None:
        ...

    @overload
    def __init__(self, initial_count: int, maximum_count: int, name: str, options: System.Threading.NamedWaitHandleOptions, created_new: typing.Optional[bool]) -> typing.Tuple[None, bool]:
        """
        Creates a named or unnamed semaphore, or opens a named semaphore if a semaphore with the name already exists.
        
        :param initial_count: The initial number of requests for the semaphore that can be satisfied concurrently.
        :param maximum_count: The maximum number of requests for the semaphore that can be satisfied concurrently.
        :param name: The name, if the semaphore is to be shared with other processes; otherwise, null or an empty string.
        :param options: Options for the named semaphore. Defaulted options, such as when passing 'options: default' in C#, are 'CurrentUserOnly = true' and 'CurrentSessionOnly = true'. For more information, see 'NamedWaitHandleOptions'. The specified options may affect the namespace for the name, and access to the underlying semaphore object.
        :param created_new: True if the semaphore was created; false if an existing named semaphore was opened.
        """
        ...

    @overload
    def __init__(self, initial_count: int, maximum_count: int, name: str, created_new: typing.Optional[bool]) -> typing.Tuple[None, bool]:
        ...

    @staticmethod
    @overload
    def open_existing(name: str, options: System.Threading.NamedWaitHandleOptions) -> System.Threading.Semaphore:
        """
        Opens an existing named semaphore.
        
        :param name: The name of the semaphore to be shared with other processes.
        :param options: Options for the named semaphore. Defaulted options, such as when passing 'options: default' in C#, are 'CurrentUserOnly = true' and 'CurrentSessionOnly = true'. For more information, see 'NamedWaitHandleOptions'. The specified options may affect the namespace for the name, and access to the underlying semaphore object.
        :returns: An object that represents the named semaphore.
        """
        ...

    @staticmethod
    @overload
    def open_existing(name: str) -> System.Threading.Semaphore:
        ...

    @overload
    def release(self) -> int:
        ...

    @overload
    def release(self, release_count: int) -> int:
        ...

    @staticmethod
    @overload
    def try_open_existing(name: str, options: System.Threading.NamedWaitHandleOptions, result: typing.Optional[System.Threading.Semaphore]) -> typing.Tuple[bool, System.Threading.Semaphore]:
        """
        Tries to open an existing named semaphore and returns a value indicating whether it was successful.
        
        :param name: The name of the semaphore to be shared with other processes.
        :param options: Options for the named semaphore. Defaulted options, such as when passing 'options: default' in C#, are 'CurrentUserOnly = true' and 'CurrentSessionOnly = true'. For more information, see 'NamedWaitHandleOptions'. The specified options may affect the namespace for the name, and access to the underlying semaphore object.
        :param result: An object that represents the named semaphore if the method returns true; otherwise, null.
        :returns: True if the named semaphore was opened successfully; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def try_open_existing(name: str, result: typing.Optional[System.Threading.Semaphore]) -> typing.Tuple[bool, System.Threading.Semaphore]:
        ...


class Lock(System.Object):
    """
    Provides a way to get mutual exclusion in regions of code between different threads. A lock may be held by one thread at
    a time.
    """

    class Scope:
        """A disposable structure that is returned by EnterScope(), which when disposed, exits the lock."""

        def dispose(self) -> None:
            """Exits the lock."""
            ...

    @property
    def is_held_by_current_thread(self) -> bool:
        """true if the lock is held by the calling thread, false otherwise."""
        ...

    def __init__(self) -> None:
        """Initializes a new instance of the Lock class."""
        ...

    def enter(self) -> None:
        """Enters the lock. Once the method returns, the calling thread would be the only thread that holds the lock."""
        ...

    def enter_scope(self) -> System.Threading.Lock.Scope:
        """
        Enters the lock and returns a Scope that may be disposed to exit the lock. Once the method returns,
        the calling thread would be the only thread that holds the lock. This method is intended to be used along with a
        language construct that would automatically dispose the Scope, such as with the C# using
        statement.
        
        :returns: A Scope that may be disposed to exit the lock.
        """
        ...

    def exit(self) -> None:
        """Exits the lock."""
        ...

    @overload
    def try_enter(self) -> bool:
        """
        Tries to enter the lock without waiting. If the lock is entered, the calling thread would be the only thread that
        holds the lock.
        
        :returns: true if the lock was entered, false otherwise.
        """
        ...

    @overload
    def try_enter(self, milliseconds_timeout: int) -> bool:
        """
        Tries to enter the lock, waiting for roughly the specified duration. If the lock is entered, the calling thread
        would be the only thread that holds the lock.
        
        :param milliseconds_timeout: The rough duration in milliseconds for which the method will wait if the lock is not available. A value of 0 specifies that the method should not wait, and a value of Timeout.Infinite or -1 specifies that the method should wait indefinitely until the lock is entered.
        :returns: true if the lock was entered, false otherwise.
        """
        ...

    @overload
    def try_enter(self, timeout: datetime.timedelta) -> bool:
        """
        Tries to enter the lock, waiting for roughly the specified duration. If the lock is entered, the calling thread
        would be the only thread that holds the lock.
        
        :param timeout: The rough duration for which the method will wait if the lock is not available. The timeout is converted to a number of milliseconds by casting TimeSpan.TotalMilliseconds of the timeout to an integer value. A value representing 0 milliseconds specifies that the method should not wait, and a value representing Timeout.Infinite or -1 milliseconds specifies that the method should wait indefinitely until the lock is entered.
        :returns: true if the lock was entered, false otherwise.
        """
        ...


class ThreadLocal(typing.Generic[System_Threading_ThreadLocal_T], System.Object, System.IDisposable):
    """Provides thread-local storage of data."""

    @property
    def value(self) -> System_Threading_ThreadLocal_T:
        """Gets or sets the value of this instance for the current thread."""
        ...

    @value.setter
    def value(self, value: System_Threading_ThreadLocal_T) -> None:
        ...

    @property
    def values(self) -> typing.List[System_Threading_ThreadLocal_T]:
        """Gets a list for all of the values currently stored by all of the threads that have accessed this instance."""
        ...

    @property
    def is_value_created(self) -> bool:
        """Gets whether Value is initialized on the current thread."""
        ...

    @overload
    def __init__(self) -> None:
        """Initializes the ThreadLocal{T} instance."""
        ...

    @overload
    def __init__(self, track_all_values: bool) -> None:
        """
        Initializes the ThreadLocal{T} instance.
        
        :param track_all_values: Whether to track all values set on the instance and expose them through the Values property.
        """
        ...

    @overload
    def __init__(self, value_factory: typing.Callable[[], System_Threading_ThreadLocal_T]) -> None:
        """
        Initializes the ThreadLocal{T} instance with the
        specified  function.
        
        :param value_factory: The Func{T} invoked to produce a lazily-initialized value when an attempt is made to retrieve Value without it having been previously initialized.
        """
        ...

    @overload
    def __init__(self, value_factory: typing.Callable[[], System_Threading_ThreadLocal_T], track_all_values: bool) -> None:
        """
        Initializes the ThreadLocal{T} instance with the
        specified  function.
        
        :param value_factory: The Func{T} invoked to produce a lazily-initialized value when an attempt is made to retrieve Value without it having been previously initialized.
        :param track_all_values: Whether to track all values set on the instance and expose them via the Values property.
        """
        ...

    @overload
    def dispose(self) -> None:
        """Releases the resources used by this ThreadLocal{T} instance."""
        ...

    @overload
    def dispose(self, disposing: bool) -> None:
        """
        Releases the resources used by this ThreadLocal{T} instance.
        
        This method is protected.
        
        :param disposing: A Boolean value that indicates whether this method is being called due to a call to Dispose().
        """
        ...

    def to_string(self) -> str:
        """
        Creates and returns a string representation of this instance for the current thread.
        
        :returns: The result of calling object.ToString on the Value.
        """
        ...


class Mutex(System.Threading.WaitHandle):
    """Synchronization primitive that can also be used for interprocess synchronization"""

    @overload
    def __init__(self, initially_owned: bool, name: str, options: System.Threading.NamedWaitHandleOptions, created_new: typing.Optional[bool]) -> typing.Tuple[None, bool]:
        """
        Creates a named or unnamed mutex, or opens a named mutex if a mutex with the name already exists.
        
        :param initially_owned: True to acquire the mutex on the calling thread if it's created; otherwise, false.
        :param name: The name, if the mutex is to be shared with other processes; otherwise, null or an empty string.
        :param options: Options for the named mutex. Defaulted options, such as when passing 'options: default' in C#, are 'CurrentUserOnly = true' and 'CurrentSessionOnly = true'. For more information, see 'NamedWaitHandleOptions'. The specified options may affect the namespace for the name, and access to the underlying mutex object.
        :param created_new: True if the mutex was created; false if an existing named mutex was opened.
        """
        ...

    @overload
    def __init__(self, initially_owned: bool, name: str, created_new: typing.Optional[bool]) -> typing.Tuple[None, bool]:
        ...

    @overload
    def __init__(self, initially_owned: bool, name: str, options: System.Threading.NamedWaitHandleOptions) -> None:
        """
        Creates a named or unnamed mutex, or opens a named mutex if a mutex with the name already exists.
        
        :param initially_owned: True to acquire the mutex on the calling thread if it's created; otherwise, false.
        :param name: The name, if the mutex is to be shared with other processes; otherwise, null or an empty string.
        :param options: Options for the named mutex. Defaulted options, such as when passing 'options: default' in C#, are 'CurrentUserOnly = true' and 'CurrentSessionOnly = true'. For more information, see 'NamedWaitHandleOptions'. The specified options may affect the namespace for the name, and access to the underlying mutex object.
        """
        ...

    @overload
    def __init__(self, initially_owned: bool, name: str) -> None:
        ...

    @overload
    def __init__(self, name: str, options: System.Threading.NamedWaitHandleOptions) -> None:
        """
        Creates a named or unnamed mutex, or opens a named mutex if a mutex with the name already exists.
        
        :param name: The name, if the mutex is to be shared with other processes; otherwise, null or an empty string.
        :param options: Options for the named mutex. Defaulted options, such as when passing 'options: default' in C#, are 'CurrentUserOnly = true' and 'CurrentSessionOnly = true'. For more information, see 'NamedWaitHandleOptions'. The specified options may affect the namespace for the name, and access to the underlying mutex object.
        """
        ...

    @overload
    def __init__(self, initially_owned: bool) -> None:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @staticmethod
    @overload
    def open_existing(name: str, options: System.Threading.NamedWaitHandleOptions) -> System.Threading.Mutex:
        """
        Opens an existing named mutex.
        
        :param name: The name of the mutex to be shared with other processes.
        :param options: Options for the named mutex. Defaulted options, such as when passing 'options: default' in C#, are 'CurrentUserOnly = true' and 'CurrentSessionOnly = true'. For more information, see 'NamedWaitHandleOptions'. The specified options may affect the namespace for the name, and access to the underlying mutex object.
        :returns: An object that represents the named mutex.
        """
        ...

    @staticmethod
    @overload
    def open_existing(name: str) -> System.Threading.Mutex:
        ...

    def release_mutex(self) -> None:
        ...

    @staticmethod
    @overload
    def try_open_existing(name: str, options: System.Threading.NamedWaitHandleOptions, result: typing.Optional[System.Threading.Mutex]) -> typing.Tuple[bool, System.Threading.Mutex]:
        """
        Tries to open an existing named mutex and returns a value indicating whether it was successful.
        
        :param name: The name of the mutex to be shared with other processes.
        :param options: Options for the named mutex. Defaulted options, such as when passing 'options: default' in C#, are 'CurrentUserOnly = true' and 'CurrentSessionOnly = true'. For more information, see 'NamedWaitHandleOptions'. The specified options may affect the namespace for the name, and access to the underlying mutex object.
        :param result: An object that represents the named mutex if the method returns true; otherwise, null.
        :returns: True if the named mutex was opened successfully; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def try_open_existing(name: str, result: typing.Optional[System.Threading.Mutex]) -> typing.Tuple[bool, System.Threading.Mutex]:
        ...


class AbandonedMutexException(System.SystemException):
    """This class has no documentation."""

    @property
    def mutex(self) -> System.Threading.Mutex:
        ...

    @property
    def mutex_index(self) -> int:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, message: str) -> None:
        ...

    @overload
    def __init__(self, message: str, inner: System.Exception) -> None:
        ...

    @overload
    def __init__(self, location: int, handle: System.Threading.WaitHandle) -> None:
        ...

    @overload
    def __init__(self, message: str, location: int, handle: System.Threading.WaitHandle) -> None:
        ...

    @overload
    def __init__(self, message: str, inner: System.Exception, location: int, handle: System.Threading.WaitHandle) -> None:
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """
        This method is protected.
        
        Obsoletions.LegacyFormatterImplMessage
        """
        ...


class SpinWait:
    """Provides support for spin-based waiting."""

    @property
    def count(self) -> int:
        """Gets the number of times SpinOnce() has been called on this instance."""
        ...

    @property
    def next_spin_will_yield(self) -> bool:
        """
        Gets whether the next call to SpinOnce() will yield the processor, triggering a
        forced context switch.
        """
        ...

    def reset(self) -> None:
        """Resets the spin counter."""
        ...

    @overload
    def spin_once(self) -> None:
        """Performs a single spin."""
        ...

    @overload
    def spin_once(self, sleep_1_threshold: int) -> None:
        """
        Performs a single spin.
        
        :param sleep_1_threshold: A minimum spin count after which Thread.Sleep(1) may be used. A value of -1 may be used to disable the use of Thread.Sleep(1).
        """
        ...

    @staticmethod
    @overload
    def spin_until(condition: typing.Callable[[], bool]) -> None:
        ...

    @staticmethod
    @overload
    def spin_until(condition: typing.Callable[[], bool], timeout: datetime.timedelta) -> bool:
        """
        Spins until the specified condition is satisfied or until the specified timeout is expired.
        
        :param condition: A delegate to be executed over and over until it returns true.
        :param timeout: A TimeSpan that represents the number of milliseconds to wait, or a TimeSpan that represents -1 milliseconds to wait indefinitely.
        :returns: True if the condition is satisfied within the timeout; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def spin_until(condition: typing.Callable[[], bool], milliseconds_timeout: int) -> bool:
        """
        Spins until the specified condition is satisfied or until the specified timeout is expired.
        
        :param condition: A delegate to be executed over and over until it returns true.
        :param milliseconds_timeout: The number of milliseconds to wait, or Timeout.Infinite (-1) to wait indefinitely.
        :returns: True if the condition is satisfied within the timeout; otherwise, false.
        """
        ...


class Timeout(System.Object):
    """This class has no documentation."""

    INFINITE_TIME_SPAN: datetime.timedelta = ...

    INFINITE: int = -1


class LazyThreadSafetyMode(Enum):
    """Specifies how a Lazy{T} instance should synchronize access among multiple threads."""

    NONE = 0
    """
    This mode makes no guarantees around the thread-safety of the Lazy{T} instance.  If used from multiple threads, the behavior of the Lazy{T} is undefined.
    This mode should be used when a Lazy{T} is guaranteed to never be initialized from more than one thread simultaneously and high performance is crucial.
    If valueFactory throws an exception when the Lazy{T} is initialized, the exception will be cached and returned on subsequent accesses to Value. Also, if valueFactory recursively
    accesses Value on this Lazy{T} instance, a InvalidOperationException will be thrown.
    """

    PUBLICATION_ONLY = 1
    """
    When multiple threads attempt to simultaneously initialize a Lazy{T} instance, this mode allows each thread to execute the
    valueFactory but only the first thread to complete initialization will be allowed to set the final value of the  Lazy{T}.
    Once initialized successfully, any future calls to Value will return the cached result.  If valueFactory throws an exception on any thread, that exception will be
    propagated out of Value. If any thread executes valueFactory without throwing an exception and, therefore, successfully sets the value, that value will be returned on
    subsequent accesses to Value from any thread.  If no thread succeeds in setting the value, IsValueCreated will remain false and subsequent accesses to Value will result in
    the valueFactory delegate re-executing.  Also, if valueFactory recursively accesses Value on this  Lazy{T} instance, an exception will NOT be thrown.
    """

    EXECUTION_AND_PUBLICATION = 2
    """
    This mode uses locks to ensure that only a single thread can initialize a Lazy{T} instance in a thread-safe manner.  In general,
    taken if this mode is used in conjunction with a Lazy{T} valueFactory delegate that uses locks internally, a deadlock can occur if not
    handled carefully.  If valueFactory throws an exception when theLazy{T} is initialized, the exception will be cached and returned on
    subsequent accesses to Value. Also, if valueFactory recursively accesses Value on this Lazy{T} instance, a  InvalidOperationException will be thrown.
    """


class LazyInitializer(System.Object):
    """Provides lazy initialization routines."""


class AutoResetEvent(System.Threading.EventWaitHandle):
    """This class has no documentation."""

    def __init__(self, initial_state: bool) -> None:
        ...


class NativeOverlapped:
    """This class has no documentation."""

    @property
    def internal_low(self) -> System.IntPtr:
        ...

    @internal_low.setter
    def internal_low(self, value: System.IntPtr) -> None:
        ...

    @property
    def internal_high(self) -> System.IntPtr:
        ...

    @internal_high.setter
    def internal_high(self, value: System.IntPtr) -> None:
        ...

    @property
    def offset_low(self) -> int:
        ...

    @offset_low.setter
    def offset_low(self, value: int) -> None:
        ...

    @property
    def offset_high(self) -> int:
        ...

    @offset_high.setter
    def offset_high(self, value: int) -> None:
        ...

    @property
    def event_handle(self) -> System.IntPtr:
        ...

    @event_handle.setter
    def event_handle(self, value: System.IntPtr) -> None:
        ...


class SynchronizationContext(System.Object):
    """This class has no documentation."""

    CURRENT: System.Threading.SynchronizationContext

    def __init__(self) -> None:
        ...

    def create_copy(self) -> System.Threading.SynchronizationContext:
        ...

    def is_wait_notification_required(self) -> bool:
        ...

    def operation_completed(self) -> None:
        """Optional override for subclasses, for responding to notification that operation has completed."""
        ...

    def operation_started(self) -> None:
        """Optional override for subclasses, for responding to notification that operation is starting."""
        ...

    def post(self, d: typing.Callable[[System.Object], None], state: typing.Any) -> None:
        ...

    def send(self, d: typing.Callable[[System.Object], None], state: typing.Any) -> None:
        ...

    @staticmethod
    def set_synchronization_context(sync_context: System.Threading.SynchronizationContext) -> None:
        ...

    def set_wait_notification_required(self) -> None:
        """This method is protected."""
        ...

    def wait(self, wait_handles: typing.List[System.IntPtr], wait_all: bool, milliseconds_timeout: int) -> int:
        ...

    @staticmethod
    def wait_helper(wait_handles: typing.List[System.IntPtr], wait_all: bool, milliseconds_timeout: int) -> int:
        """This method is protected."""
        ...


class ThreadStateException(System.SystemException):
    """The exception that is thrown when a Thread is in an invalid Thread.ThreadState for the method call."""

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


class ThreadExceptionEventArgs(System.EventArgs):
    """This class has no documentation."""

    @property
    def exception(self) -> System.Exception:
        ...

    def __init__(self, t: System.Exception) -> None:
        ...


class PeriodicTimer(System.Object, System.IDisposable):
    """Provides a periodic timer that enables waiting asynchronously for timer ticks."""

    @property
    def period(self) -> datetime.timedelta:
        """Gets or sets the period between ticks."""
        ...

    @period.setter
    def period(self, value: datetime.timedelta) -> None:
        ...

    @overload
    def __init__(self, period: datetime.timedelta) -> None:
        """
        Initializes the timer.
        
        :param period: The period between ticks
        """
        ...

    @overload
    def __init__(self, period: datetime.timedelta, time_provider: System.TimeProvider) -> None:
        """
        Initializes the timer.
        
        :param period: The period between ticks
        :param time_provider: The TimeProvider used to interpret .
        """
        ...

    def dispose(self) -> None:
        """Stops the timer and releases associated managed resources."""
        ...

    def wait_for_next_tick_async(self, cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.ValueTask[bool]:
        """
        Wait for the next tick of the timer, or for the timer to be stopped.
        
        :param cancellation_token: A CancellationToken to use to cancel the asynchronous wait. If cancellation is requested, it affects only the single wait operation; the underlying timer continues firing.
        :returns: A task that will be completed due to the timer firing, Dispose being called to stop the timer, or cancellation being requested.
        """
        ...


class AsyncLocal(typing.Generic[System_Threading_AsyncLocal_T], System.Object, System.Threading.IAsyncLocal):
    """Represents ambient data that is local to a given asynchronous control flow, such as an asynchronous method."""

    @property
    def value(self) -> System_Threading_AsyncLocal_T:
        """Gets or sets the value of the ambient data."""
        ...

    @value.setter
    def value(self, value: System_Threading_AsyncLocal_T) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """Instantiates an AsyncLocal{T} instance that does not receive change notifications."""
        ...

    @overload
    def __init__(self, value_changed_handler: typing.Callable[[System.Threading.AsyncLocalValueChangedArgs[System_Threading_AsyncLocal_T]], None]) -> None:
        """
        Instantiates an AsyncLocal{T} instance that receives change notifications.
        
        :param value_changed_handler: The delegate that is called whenever the current value changes on any thread.
        """
        ...


class AsyncLocalValueChangedArgs(typing.Generic[System_Threading_AsyncLocalValueChangedArgs_T]):
    """The class that provides data change information to AsyncLocal{T} instances that register for change notifications."""

    @property
    def previous_value(self) -> System_Threading_AsyncLocalValueChangedArgs_T:
        """Gets the data's previous value."""
        ...

    @property
    def current_value(self) -> System_Threading_AsyncLocalValueChangedArgs_T:
        """Gets the data's current value."""
        ...

    @property
    def thread_context_changed(self) -> bool:
        """Returns a value that indicates whether the value changes because of a change of execution context."""
        ...


class ThreadStartException(System.SystemException):
    """This class has no documentation."""


class Monitor(System.Object):
    """This class has no documentation."""

    LOCK_CONTENTION_COUNT: int

    @staticmethod
    @overload
    def enter(obj: typing.Any) -> None:
        ...

    @staticmethod
    @overload
    def enter(obj: typing.Any, lock_taken: bool) -> None:
        ...

    @staticmethod
    def exit(obj: typing.Any) -> None:
        ...

    @staticmethod
    def is_entered(obj: typing.Any) -> bool:
        ...

    @staticmethod
    def pulse(obj: typing.Any) -> None:
        ...

    @staticmethod
    def pulse_all(obj: typing.Any) -> None:
        ...

    @staticmethod
    @overload
    def try_enter(obj: typing.Any, timeout: datetime.timedelta) -> bool:
        ...

    @staticmethod
    @overload
    def try_enter(obj: typing.Any, timeout: datetime.timedelta, lock_taken: bool) -> None:
        ...

    @staticmethod
    @overload
    def try_enter(obj: typing.Any) -> bool:
        ...

    @staticmethod
    @overload
    def try_enter(obj: typing.Any, lock_taken: bool) -> None:
        ...

    @staticmethod
    @overload
    def try_enter(obj: typing.Any, milliseconds_timeout: int) -> bool:
        ...

    @staticmethod
    @overload
    def try_enter(obj: typing.Any, milliseconds_timeout: int, lock_taken: bool) -> None:
        ...

    @staticmethod
    @overload
    def wait(obj: typing.Any, timeout: datetime.timedelta) -> bool:
        ...

    @staticmethod
    @overload
    def wait(obj: typing.Any) -> bool:
        ...

    @staticmethod
    @overload
    def wait(obj: typing.Any, milliseconds_timeout: int, exit_context: bool) -> bool:
        ...

    @staticmethod
    @overload
    def wait(obj: typing.Any, timeout: datetime.timedelta, exit_context: bool) -> bool:
        ...

    @staticmethod
    @overload
    def wait(obj: typing.Any, milliseconds_timeout: int) -> bool:
        ...


class ManualResetEventSlim(System.Object, System.IDisposable):
    """Provides a slimmed down version of ManualResetEvent."""

    @property
    def wait_handle(self) -> System.Threading.WaitHandle:
        """Gets the underlying Threading.WaitHandle object for this ManualResetEventSlim."""
        ...

    @property
    def is_set(self) -> bool:
        """Gets whether the event is set."""
        ...

    @property
    def spin_count(self) -> int:
        """Gets the number of spin waits that will be occur before falling back to a true wait."""
        ...

    @overload
    def __init__(self) -> None:
        """
        Initializes a new instance of the ManualResetEventSlim
        class with an initial state of nonsignaled.
        """
        ...

    @overload
    def __init__(self, initial_state: bool) -> None:
        """
        Initializes a new instance of the ManualResetEventSlim
        class with a boolean value indicating whether to set the initial state to signaled.
        
        :param initial_state: true to set the initial state signaled; false to set the initial state to nonsignaled.
        """
        ...

    @overload
    def __init__(self, initial_state: bool, spin_count: int) -> None:
        """
        Initializes a new instance of the ManualResetEventSlim
        class with a Boolean value indicating whether to set the initial state to signaled and a specified
        spin count.
        
        :param initial_state: true to set the initial state to signaled; false to set the initial state to nonsignaled.
        :param spin_count: The number of spin waits that will occur before falling back to a true wait.
        """
        ...

    @overload
    def dispose(self) -> None:
        """Releases all resources used by the current instance of ManualResetEventSlim."""
        ...

    @overload
    def dispose(self, disposing: bool) -> None:
        """
        When overridden in a derived class, releases the unmanaged resources used by the
        ManualResetEventSlim, and optionally releases the managed resources.
        
        This method is protected.
        
        :param disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
        """
        ...

    def reset(self) -> None:
        """Sets the state of the event to nonsignaled, which causes threads to block."""
        ...

    def set(self) -> None:
        """
        Sets the state of the event to signaled, which allows one or more threads waiting on the event to
        proceed.
        """
        ...

    @overload
    def wait(self) -> None:
        """Blocks the current thread until the current ManualResetEventSlim is set."""
        ...

    @overload
    def wait(self, cancellation_token: System.Threading.CancellationToken) -> None:
        """
        Blocks the current thread until the current ManualResetEventSlim receives a signal,
        while observing a CancellationToken.
        
        :param cancellation_token: The CancellationToken to observe.
        """
        ...

    @overload
    def wait(self, timeout: datetime.timedelta) -> bool:
        """
        Blocks the current thread until the current ManualResetEventSlim is set, using a
        TimeSpan to measure the time interval.
        
        :param timeout: A TimeSpan that represents the number of milliseconds to wait, or a TimeSpan that represents -1 milliseconds to wait indefinitely.
        :returns: true if the ManualResetEventSlim was set; otherwise, false.
        """
        ...

    @overload
    def wait(self, timeout: datetime.timedelta, cancellation_token: System.Threading.CancellationToken) -> bool:
        """
        Blocks the current thread until the current ManualResetEventSlim is set, using a
        TimeSpan to measure the time interval, while observing a CancellationToken.
        
        :param timeout: A TimeSpan that represents the number of milliseconds to wait, or a TimeSpan that represents -1 milliseconds to wait indefinitely.
        :param cancellation_token: The CancellationToken to observe.
        :returns: true if the ManualResetEventSlim was set; otherwise, false.
        """
        ...

    @overload
    def wait(self, milliseconds_timeout: int) -> bool:
        """
        Blocks the current thread until the current ManualResetEventSlim is set, using a
        32-bit signed integer to measure the time interval.
        
        :param milliseconds_timeout: The number of milliseconds to wait, or Timeout.Infinite(-1) to wait indefinitely.
        :returns: true if the ManualResetEventSlim was set; otherwise, false.
        """
        ...

    @overload
    def wait(self, milliseconds_timeout: int, cancellation_token: System.Threading.CancellationToken) -> bool:
        """
        Blocks the current thread until the current ManualResetEventSlim is set, using a
        32-bit signed integer to measure the time interval, while observing a CancellationToken.
        
        :param milliseconds_timeout: The number of milliseconds to wait, or Timeout.Infinite(-1) to wait indefinitely.
        :param cancellation_token: The CancellationToken to observe.
        :returns: true if the ManualResetEventSlim was set; otherwise, false.
        """
        ...


class Volatile(System.Object):
    """Methods for accessing memory with volatile semantics."""

    @staticmethod
    @overload
    def read(location: bool) -> bool:
        ...

    @staticmethod
    @overload
    def read(location: int) -> int:
        ...

    @staticmethod
    @overload
    def read(location: float) -> float:
        ...

    @staticmethod
    @overload
    def read(location: System.IntPtr) -> System.IntPtr:
        ...

    @staticmethod
    @overload
    def read(location: System.UIntPtr) -> System.UIntPtr:
        ...

    @staticmethod
    def read_barrier() -> None:
        ...

    @staticmethod
    @overload
    def write(location: bool, value: bool) -> None:
        ...

    @staticmethod
    @overload
    def write(location: int, value: int) -> None:
        ...

    @staticmethod
    @overload
    def write(location: float, value: float) -> None:
        ...

    @staticmethod
    @overload
    def write(location: System.IntPtr, value: System.IntPtr) -> None:
        ...

    @staticmethod
    @overload
    def write(location: System.UIntPtr, value: System.UIntPtr) -> None:
        ...

    @staticmethod
    def write_barrier() -> None:
        """
        Synchronizes memory access as follows:
        The processor that executes the current thread cannot reorder instructions in such a way that memory writes after
        the call to WriteBarrier execute before memory accesses that follow the call to WriteBarrier.
        """
        ...


class WaitHandleCannotBeOpenedException(System.ApplicationException):
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


class SemaphoreFullException(System.SystemException):
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


class Overlapped(System.Object):
    """This class has no documentation."""

    @property
    def async_result(self) -> System.IAsyncResult:
        ...

    @async_result.setter
    def async_result(self, value: System.IAsyncResult) -> None:
        ...

    @property
    def offset_low(self) -> int:
        ...

    @offset_low.setter
    def offset_low(self, value: int) -> None:
        ...

    @property
    def offset_high(self) -> int:
        ...

    @offset_high.setter
    def offset_high(self, value: int) -> None:
        ...

    @property
    def event_handle(self) -> int:
        """Overlapped.EventHandle is not 64-bit compatible and has been deprecated. Use EventHandleIntPtr instead."""
        warnings.warn("Overlapped.EventHandle is not 64-bit compatible and has been deprecated. Use EventHandleIntPtr instead.", DeprecationWarning)

    @event_handle.setter
    def event_handle(self, value: int) -> None:
        warnings.warn("Overlapped.EventHandle is not 64-bit compatible and has been deprecated. Use EventHandleIntPtr instead.", DeprecationWarning)

    @property
    def event_handle_int_ptr(self) -> System.IntPtr:
        ...

    @event_handle_int_ptr.setter
    def event_handle_int_ptr(self, value: System.IntPtr) -> None:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, offset_lo: int, offset_hi: int, h_event: System.IntPtr, ar: System.IAsyncResult) -> None:
        ...

    @overload
    def __init__(self, offset_lo: int, offset_hi: int, h_event: int, ar: System.IAsyncResult) -> None:
        """This constructor is not 64-bit compatible and has been deprecated. Use the constructor that accepts an IntPtr for the event handle instead."""
        ...

    @staticmethod
    def free(native_overlapped_ptr: typing.Any) -> None:
        ...

    @overload
    def pack(self, iocb: typing.Callable[[int, int, typing.Any], None], user_data: typing.Any) -> typing.Any:
        ...

    @overload
    def pack(self, iocb: typing.Callable[[int, int, typing.Any], None]) -> typing.Any:
        """This overload is not safe and has been deprecated. Use Pack(IOCompletionCallback?, object?) instead."""
        ...

    @staticmethod
    def unpack(native_overlapped_ptr: typing.Any) -> System.Threading.Overlapped:
        ...

    @overload
    def unsafe_pack(self, iocb: typing.Callable[[int, int, typing.Any], None], user_data: typing.Any) -> typing.Any:
        ...

    @overload
    def unsafe_pack(self, iocb: typing.Callable[[int, int, typing.Any], None]) -> typing.Any:
        """This overload is not safe and has been deprecated. Use UnsafePack(IOCompletionCallback?, object?) instead."""
        ...


class ManualResetEvent(System.Threading.EventWaitHandle):
    """This class has no documentation."""

    def __init__(self, initial_state: bool) -> None:
        ...


class SpinLock:
    """
    Provides a mutual exclusion lock primitive where a thread trying to acquire the lock waits in a loop
    repeatedly checking until the lock becomes available.
    """

    @property
    def is_held(self) -> bool:
        """Gets whether the lock is currently held by any thread."""
        ...

    @property
    def is_held_by_current_thread(self) -> bool:
        """Gets whether the lock is currently held by any thread."""
        ...

    @property
    def is_thread_owner_tracking_enabled(self) -> bool:
        """Gets whether thread ownership tracking is enabled for this instance."""
        ...

    def __init__(self, enable_thread_owner_tracking: bool) -> None:
        """
        Initializes a new instance of the SpinLock
        structure with the option to track thread IDs to improve debugging.
        
        :param enable_thread_owner_tracking: Whether to capture and use thread IDs for debugging purposes.
        """
        ...

    def enter(self, lock_taken: bool) -> None:
        """
        Initializes a new instance of the SpinLock
        structure with the option to track thread IDs to improve debugging.
        
        :param lock_taken: True if the lock is acquired; otherwise, false.  must be initialized to false prior to calling this method.
        """
        ...

    @overload
    def exit(self) -> None:
        """Releases the lock."""
        ...

    @overload
    def exit(self, use_memory_barrier: bool) -> None:
        """
        Releases the lock.
        
        :param use_memory_barrier: A Boolean value that indicates whether a memory fence should be issued in order to immediately publish the exit operation to other threads.
        """
        ...

    @overload
    def try_enter(self, lock_taken: bool) -> None:
        """
        Attempts to acquire the lock in a reliable manner, such that even if an exception occurs within
        the method call,  can be examined reliably to determine whether the
        lock was acquired.
        
        :param lock_taken: True if the lock is acquired; otherwise, false.  must be initialized to false prior to calling this method.
        """
        ...

    @overload
    def try_enter(self, timeout: datetime.timedelta, lock_taken: bool) -> None:
        """
        Attempts to acquire the lock in a reliable manner, such that even if an exception occurs within
        the method call,  can be examined reliably to determine whether the
        lock was acquired.
        
        :param timeout: A TimeSpan that represents the number of milliseconds to wait, or a TimeSpan that represents -1 milliseconds to wait indefinitely.
        :param lock_taken: True if the lock is acquired; otherwise, false.  must be initialized to false prior to calling this method.
        """
        ...

    @overload
    def try_enter(self, milliseconds_timeout: int, lock_taken: bool) -> None:
        """
        Attempts to acquire the lock in a reliable manner, such that even if an exception occurs within
        the method call,  can be examined reliably to determine whether the
        lock was acquired.
        
        :param milliseconds_timeout: The number of milliseconds to wait, or Timeout.Infinite (-1) to wait indefinitely.
        :param lock_taken: True if the lock is acquired; otherwise, false.  must be initialized to false prior to calling this method.
        """
        ...


class SynchronizationLockException(System.SystemException):
    """The exception that is thrown when a method requires the caller to own the lock on a given Monitor, and the method is invoked by a caller that does not own that lock."""

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


class Timer(System.MarshalByRefObject, System.Threading.ITimer):
    """This class has no documentation."""

    ACTIVE_COUNT: int
    """
    Gets the number of timers that are currently active. An active timer is registered to tick at some point in the
    future, and has not yet been canceled.
    """

    @overload
    def __init__(self, callback: typing.Callable[[System.Object], None], state: typing.Any, due_time: int, period: int) -> None:
        ...

    @overload
    def __init__(self, callback: typing.Callable[[System.Object], None], state: typing.Any, due_time: datetime.timedelta, period: datetime.timedelta) -> None:
        ...

    @overload
    def __init__(self, callback: typing.Callable[[System.Object], None]) -> None:
        ...

    @overload
    def change(self, due_time: int, period: int) -> bool:
        ...

    @overload
    def change(self, due_time: datetime.timedelta, period: datetime.timedelta) -> bool:
        ...

    @overload
    def dispose(self, notify_object: System.Threading.WaitHandle) -> bool:
        ...

    @overload
    def dispose(self) -> None:
        ...

    def dispose_async(self) -> System.Threading.Tasks.ValueTask:
        ...


class WaitHandleExtensions(System.Object):
    """This class has no documentation."""

    @staticmethod
    def get_safe_wait_handle(wait_handle: System.Threading.WaitHandle) -> Microsoft.Win32.SafeHandles.SafeWaitHandle:
        """
        Gets the native operating system handle.
        
        :param wait_handle: The WaitHandle to operate on.
        :returns: A Runtime.InteropServices.SafeHandle representing the native operating system handle.
        """
        ...

    @staticmethod
    def set_safe_wait_handle(wait_handle: System.Threading.WaitHandle, value: Microsoft.Win32.SafeHandles.SafeWaitHandle) -> None:
        """
        Sets the native operating system handle
        
        :param wait_handle: The WaitHandle to operate on.
        :param value: A Runtime.InteropServices.SafeHandle representing the native operating system handle.
        """
        ...


class CancellationTokenSource(System.Object, System.IDisposable):
    """Signals to a CancellationToken that it should be canceled."""

    @property
    def is_cancellation_requested(self) -> bool:
        """Gets whether cancellation has been requested for this CancellationTokenSource."""
        ...

    @property
    def token(self) -> System.Threading.CancellationToken:
        """Gets the CancellationToken associated with this CancellationTokenSource."""
        ...

    @overload
    def __init__(self) -> None:
        """Initializes the CancellationTokenSource."""
        ...

    @overload
    def __init__(self, delay: datetime.timedelta) -> None:
        """
        Constructs a CancellationTokenSource that will be canceled after a specified time span.
        
        :param delay: The time span to wait before canceling this CancellationTokenSource
        """
        ...

    @overload
    def __init__(self, delay: datetime.timedelta, time_provider: System.TimeProvider) -> None:
        """
        Initializes a new instance of the CancellationTokenSource class that will be canceled after the specified TimeSpan.
        
        :param delay: The time interval to wait before canceling this CancellationTokenSource.
        :param time_provider: The TimeProvider with which to interpret the .
        """
        ...

    @overload
    def __init__(self, milliseconds_delay: int) -> None:
        """
        Constructs a CancellationTokenSource that will be canceled after a specified time span.
        
        :param milliseconds_delay: The time span to wait before canceling this CancellationTokenSource
        """
        ...

    @overload
    def cancel(self) -> None:
        """Communicates a request for cancellation."""
        ...

    @overload
    def cancel(self, throw_on_first_exception: bool) -> None:
        """
        Communicates a request for cancellation.
        
        :param throw_on_first_exception: Specifies whether exceptions should immediately propagate.
        """
        ...

    @overload
    def cancel_after(self, delay: datetime.timedelta) -> None:
        """
        Schedules a Cancel operation on this CancellationTokenSource.
        
        :param delay: The time span to wait before canceling this CancellationTokenSource.
        """
        ...

    @overload
    def cancel_after(self, milliseconds_delay: int) -> None:
        """
        Schedules a Cancel operation on this CancellationTokenSource.
        
        :param milliseconds_delay: The time span to wait before canceling this CancellationTokenSource.
        """
        ...

    def cancel_async(self) -> System.Threading.Tasks.Task:
        """
        Communicates a request for cancellation asynchronously.
        
        :returns: A task that will complete after cancelable operations and callbacks registered with the associated CancellationToken have completed.
        """
        ...

    @staticmethod
    @overload
    def create_linked_token_source(token_1: System.Threading.CancellationToken, token_2: System.Threading.CancellationToken) -> System.Threading.CancellationTokenSource:
        """
        Creates a CancellationTokenSource that will be in the canceled state
        when any of the source tokens are in the canceled state.
        
        :param token_1: The first CancellationToken to observe.
        :param token_2: The second CancellationToken to observe.
        :returns: A CancellationTokenSource that is linked to the source tokens.
        """
        ...

    @staticmethod
    @overload
    def create_linked_token_source(token: System.Threading.CancellationToken) -> System.Threading.CancellationTokenSource:
        """
        Creates a CancellationTokenSource that will be in the canceled state
        when the supplied token is in the canceled state.
        
        :param token: The CancellationToken to observe.
        :returns: A CancellationTokenSource that is linked to the source token.
        """
        ...

    @staticmethod
    @overload
    def create_linked_token_source(*tokens: typing.Union[System.Threading.CancellationToken, typing.Iterable[System.Threading.CancellationToken]]) -> System.Threading.CancellationTokenSource:
        """
        Creates a CancellationTokenSource that will be in the canceled state
        when any of the source tokens are in the canceled state.
        
        :param tokens: The CancellationToken instances to observe.
        :returns: A CancellationTokenSource that is linked to the source tokens.
        """
        ...

    @overload
    def dispose(self) -> None:
        """Releases the resources used by this CancellationTokenSource."""
        ...

    @overload
    def dispose(self, disposing: bool) -> None:
        """
        Releases the unmanaged resources used by the CancellationTokenSource class and optionally releases the managed resources.
        
        This method is protected.
        
        :param disposing: true to release both managed and unmanaged resources; false to release only unmanaged resources.
        """
        ...

    def try_reset(self) -> bool:
        """
        Attempts to reset the CancellationTokenSource to be used for an unrelated operation.
        
        :returns: true if the CancellationTokenSource has not had cancellation requested and could have its state reset to be reused for a subsequent operation; otherwise, false.
        """
        ...


class Interlocked(System.Object):
    """Provides atomic operations for variables that are shared by multiple threads."""

    @staticmethod
    def add(location_1: int, value: int) -> int:
        ...

    @staticmethod
    def And(location1: int, value: int) -> int:
        ...

    @staticmethod
    @overload
    def compare_exchange(location_1: typing.Any, value: typing.Any, comparand: typing.Any) -> System.Object:
        ...

    @staticmethod
    @overload
    def compare_exchange(location_1: int, value: int, comparand: int) -> int:
        ...

    @staticmethod
    @overload
    def compare_exchange(location_1: float, value: float, comparand: float) -> float:
        """
        Compares two single-precision floating point numbers for equality and, if they are equal, replaces the first value.
        
        :param location_1: The destination, whose value is compared with  and possibly replaced.
        :param value: The value that replaces the destination value if the comparison results in equality.
        :param comparand: The value that is compared to the value at .
        :returns: The original value in .
        """
        ...

    @staticmethod
    @overload
    def compare_exchange(location_1: System.IntPtr, value: System.IntPtr, comparand: System.IntPtr) -> System.IntPtr:
        """
        Compares two platform-specific handles or pointers for equality and, if they are equal, replaces the first one.
        
        :param location_1: The destination IntPtr, whose value is compared with the value of  and possibly replaced by .
        :param value: The IntPtr that replaces the destination value if the comparison results in equality.
        :param comparand: The IntPtr that is compared to the value at .
        :returns: The original value in .
        """
        ...

    @staticmethod
    @overload
    def compare_exchange(location_1: System.UIntPtr, value: System.UIntPtr, comparand: System.UIntPtr) -> System.UIntPtr:
        """
        Compares two platform-specific handles or pointers for equality and, if they are equal, replaces the first one.
        
        :param location_1: The destination UIntPtr, whose value is compared with the value of  and possibly replaced by .
        :param value: The UIntPtr that replaces the destination value if the comparison results in equality.
        :param comparand: The UIntPtr that is compared to the value at .
        :returns: The original value in .
        """
        ...

    @staticmethod
    def decrement(location: int) -> int:
        ...

    @staticmethod
    @overload
    def exchange(location_1: typing.Any, value: typing.Any) -> System.Object:
        ...

    @staticmethod
    @overload
    def exchange(location_1: int, value: int) -> int:
        ...

    @staticmethod
    @overload
    def exchange(location_1: float, value: float) -> float:
        """
        Sets a single-precision floating point number to a specified value and returns the original value, as an atomic operation.
        
        :param location_1: The variable to set to the specified value.
        :param value: The value to which the  parameter is set.
        :returns: The original value of .
        """
        ...

    @staticmethod
    @overload
    def exchange(location_1: System.IntPtr, value: System.IntPtr) -> System.IntPtr:
        """
        Sets a platform-specific handle or pointer to a specified value and returns the original value, as an atomic operation.
        
        :param location_1: The variable to set to the specified value.
        :param value: The value to which the  parameter is set.
        :returns: The original value of .
        """
        ...

    @staticmethod
    @overload
    def exchange(location_1: System.UIntPtr, value: System.UIntPtr) -> System.UIntPtr:
        """
        Sets a platform-specific handle or pointer to a specified value and returns the original value, as an atomic operation.
        
        :param location_1: The variable to set to the specified value.
        :param value: The value to which the  parameter is set.
        :returns: The original value of .
        """
        ...

    @staticmethod
    def increment(location: int) -> int:
        ...

    @staticmethod
    def memory_barrier() -> None:
        ...

    @staticmethod
    def memory_barrier_process_wide() -> None:
        ...

    @staticmethod
    def Or(location1: int, value: int) -> int:
        ...

    @staticmethod
    def read(location: int) -> int:
        ...


class ThreadAbortException(System.SystemException):
    """The exception that is thrown when a call is made to the Thread.Abort method."""

    @property
    def exception_state(self) -> System.Object:
        ...


class LockRecursionException(System.Exception):
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


class LockRecursionPolicy(Enum):
    """This class has no documentation."""

    NO_RECURSION = 0

    SUPPORTS_RECURSION = 1


class ReaderWriterLockSlim(System.Object, System.IDisposable):
    """
    A reader-writer lock implementation that is intended to be simple, yet very
    efficient.  In particular only 1 interlocked operation is taken for any lock
    operation (we use spin locks to achieve this).  The spin lock is never held
    for more than a few instructions (in particular, we never call event APIs
    or in fact any non-trivial API while holding the spin lock).
    """

    @property
    def is_read_lock_held(self) -> bool:
        ...

    @property
    def is_upgradeable_read_lock_held(self) -> bool:
        ...

    @property
    def is_write_lock_held(self) -> bool:
        ...

    @property
    def recursion_policy(self) -> System.Threading.LockRecursionPolicy:
        ...

    @property
    def current_read_count(self) -> int:
        ...

    @property
    def recursive_read_count(self) -> int:
        ...

    @property
    def recursive_upgrade_count(self) -> int:
        ...

    @property
    def recursive_write_count(self) -> int:
        ...

    @property
    def waiting_read_count(self) -> int:
        ...

    @property
    def waiting_upgrade_count(self) -> int:
        ...

    @property
    def waiting_write_count(self) -> int:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, recursion_policy: System.Threading.LockRecursionPolicy) -> None:
        ...

    def dispose(self) -> None:
        ...

    def enter_read_lock(self) -> None:
        ...

    def enter_upgradeable_read_lock(self) -> None:
        ...

    def enter_write_lock(self) -> None:
        ...

    def exit_read_lock(self) -> None:
        ...

    def exit_upgradeable_read_lock(self) -> None:
        ...

    def exit_write_lock(self) -> None:
        ...

    @overload
    def try_enter_read_lock(self, timeout: datetime.timedelta) -> bool:
        ...

    @overload
    def try_enter_read_lock(self, milliseconds_timeout: int) -> bool:
        ...

    @overload
    def try_enter_upgradeable_read_lock(self, timeout: datetime.timedelta) -> bool:
        ...

    @overload
    def try_enter_upgradeable_read_lock(self, milliseconds_timeout: int) -> bool:
        ...

    @overload
    def try_enter_write_lock(self, timeout: datetime.timedelta) -> bool:
        ...

    @overload
    def try_enter_write_lock(self, milliseconds_timeout: int) -> bool:
        ...


