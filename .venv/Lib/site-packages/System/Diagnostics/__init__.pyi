from typing import overload
from enum import Enum
import datetime
import typing

import System
import System.Collections.Generic
import System.Diagnostics
import System.Reflection


class Stopwatch(System.Object):
    """This class has no documentation."""

    FREQUENCY: int = ...

    IS_HIGH_RESOLUTION: bool = True

    @property
    def is_running(self) -> bool:
        ...

    @property
    def elapsed(self) -> datetime.timedelta:
        ...

    @property
    def elapsed_milliseconds(self) -> int:
        ...

    @property
    def elapsed_ticks(self) -> int:
        ...

    def __init__(self) -> None:
        ...

    @staticmethod
    @overload
    def get_elapsed_time(starting_timestamp: int) -> datetime.timedelta:
        """
        Gets the elapsed time since the  value retrieved using GetTimestamp.
        
        :param starting_timestamp: The timestamp marking the beginning of the time period.
        :returns: A TimeSpan for the elapsed time between the starting timestamp and the time of this call.
        """
        ...

    @staticmethod
    @overload
    def get_elapsed_time(starting_timestamp: int, ending_timestamp: int) -> datetime.timedelta:
        """
        Gets the elapsed time between two timestamps retrieved using GetTimestamp.
        
        :param starting_timestamp: The timestamp marking the beginning of the time period.
        :param ending_timestamp: The timestamp marking the end of the time period.
        :returns: A TimeSpan for the elapsed time between the starting and ending timestamps.
        """
        ...

    @staticmethod
    def get_timestamp() -> int:
        ...

    def reset(self) -> None:
        ...

    def restart(self) -> None:
        ...

    def start(self) -> None:
        ...

    @staticmethod
    def start_new() -> System.Diagnostics.Stopwatch:
        ...

    def stop(self) -> None:
        ...

    def to_string(self) -> str:
        """
        Returns the Elapsed time as a string.
        
        :returns: Elapsed time string in the same format used by TimeSpan.ToString().
        """
        ...


class StackTraceHiddenAttribute(System.Attribute):
    """
    Types and Methods attributed with StackTraceHidden will be omitted from the stack trace text shown in StackTrace.ToString()
    and Exception.StackTrace
    """

    def __init__(self) -> None:
        """Initializes a new instance of the StackTraceHiddenAttribute class."""
        ...


class DebugProvider(System.Object):
    """Provides default implementation for Write and Fail methods in Debug class."""

    def fail(self, message: str, detail_message: str) -> None:
        ...

    @staticmethod
    def fail_core(stack_trace: str, message: str, detail_message: str, error_source: str) -> None:
        ...

    def on_indent_level_changed(self, indent_level: int) -> None:
        ...

    def on_indent_size_changed(self, indent_size: int) -> None:
        ...

    def write(self, message: str) -> None:
        ...

    @staticmethod
    def write_core(message: str) -> None:
        ...

    def write_line(self, message: str) -> None:
        ...


class DebuggerTypeProxyAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def proxy_type_name(self) -> str:
        ...

    @property
    def target(self) -> typing.Type:
        ...

    @target.setter
    def target(self, value: typing.Type) -> None:
        ...

    @property
    def target_type_name(self) -> str:
        ...

    @target_type_name.setter
    def target_type_name(self, value: str) -> None:
        ...

    @overload
    def __init__(self, type: typing.Type) -> None:
        ...

    @overload
    def __init__(self, type_name: str) -> None:
        ...


class UnreachableException(System.Exception):
    """Exception thrown when the program executes an instruction that was thought to be unreachable."""

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the UnreachableException class with the default error message."""
        ...

    @overload
    def __init__(self, message: str) -> None:
        """
        Initializes a new instance of the UnreachableException
        class with a specified error message.
        
        :param message: The error message that explains the reason for the exception.
        """
        ...

    @overload
    def __init__(self, message: str, inner_exception: System.Exception) -> None:
        """
        Initializes a new instance of the UnreachableException
        class with a specified error message and a reference to the inner exception that is the cause of
        this exception.
        
        :param message: The error message that explains the reason for the exception.
        :param inner_exception: The exception that is the cause of the current exception.
        """
        ...


class DebuggableAttribute(System.Attribute):
    """This class has no documentation."""

    class DebuggingModes(Enum):
        """This class has no documentation."""

        NONE = ...

        DEFAULT = ...

        DISABLE_OPTIMIZATIONS = ...

        IGNORE_SYMBOL_STORE_SEQUENCE_POINTS = ...

        ENABLE_EDIT_AND_CONTINUE = ...

    @property
    def is_jit_tracking_enabled(self) -> bool:
        ...

    @property
    def is_jit_optimizer_disabled(self) -> bool:
        ...

    @property
    def debugging_flags(self) -> System.Diagnostics.DebuggableAttribute.DebuggingModes:
        ...

    @overload
    def __init__(self, is_jit_tracking_enabled: bool, is_jit_optimizer_disabled: bool) -> None:
        ...

    @overload
    def __init__(self, modes: System.Diagnostics.DebuggableAttribute.DebuggingModes) -> None:
        ...


class DebuggerStepperBoundaryAttribute(System.Attribute):
    """Indicates the code following the attribute is to be executed in run, not step, mode."""

    def __init__(self) -> None:
        ...


class DebuggerDisableUserUnhandledExceptionsAttribute(System.Attribute):
    """
    If a .NET Debugger is attached which supports the Debugger.BreakForUserUnhandledException(Exception) API,
    this attribute will prevent the debugger from breaking on user-unhandled exceptions when the
    exception is caught by a method with this attribute, unless BreakForUserUnhandledException is called.
    """


class DebuggerNonUserCodeAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class Debug(System.Object):
    """Provides a set of properties and methods for debugging code."""

    class AssertInterpolatedStringHandler:
        """Provides an interpolated string handler for Debug.Assert that only performs formatting if the assert fails."""

        def __init__(self, literal_length: int, formatted_count: int, condition: bool, should_append: typing.Optional[bool]) -> typing.Tuple[None, bool]:
            """
            Creates an instance of the handler..
            
            :param literal_length: The number of constant characters outside of interpolation expressions in the interpolated string.
            :param formatted_count: The number of interpolation expressions in the interpolated string.
            :param condition: The condition Boolean passed to the Debug method.
            :param should_append: A value indicating whether formatting should proceed.
            """
            ...

        @overload
        def append_formatted(self, value: typing.Any, alignment: int = 0, format: str = None) -> None:
            """
            Writes the specified value to the handler.
            
            :param value: The value to write.
            :param alignment: Minimum number of characters that should be written for this value.  If the value is negative, it indicates left-aligned and the required minimum is the absolute value.
            :param format: The format string.
            """
            ...

        @overload
        def append_formatted(self, value: System.ReadOnlySpan[str]) -> None:
            """
            Writes the specified character span to the handler.
            
            :param value: The span to write.
            """
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
            """
            Writes the specified value to the handler.
            
            :param value: The value to write.
            """
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

    class WriteIfInterpolatedStringHandler:
        """Provides an interpolated string handler for Debug.WriteIf and Debug.WriteLineIf that only performs formatting if the condition applies."""

        def __init__(self, literal_length: int, formatted_count: int, condition: bool, should_append: typing.Optional[bool]) -> typing.Tuple[None, bool]:
            """
            Creates an instance of the handler..
            
            :param literal_length: The number of constant characters outside of interpolation expressions in the interpolated string.
            :param formatted_count: The number of interpolation expressions in the interpolated string.
            :param condition: The condition Boolean passed to the Debug method.
            :param should_append: A value indicating whether formatting should proceed.
            """
            ...

        @overload
        def append_formatted(self, value: typing.Any, alignment: int = 0, format: str = None) -> None:
            """
            Writes the specified value to the handler.
            
            :param value: The value to write.
            :param alignment: Minimum number of characters that should be written for this value.  If the value is negative, it indicates left-aligned and the required minimum is the absolute value.
            :param format: The format string.
            """
            ...

        @overload
        def append_formatted(self, value: System.ReadOnlySpan[str]) -> None:
            """
            Writes the specified character span to the handler.
            
            :param value: The span to write.
            """
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
            """
            Writes the specified value to the handler.
            
            :param value: The value to write.
            """
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

    auto_flush: bool

    indent_level: int

    indent_size: int

    @staticmethod
    @overload
    def Assert(condition: bool) -> None:
        ...

    @staticmethod
    @overload
    def Assert(condition: bool, message: str = None) -> None:
        ...

    @staticmethod
    @overload
    def Assert(condition: bool, message: System.Diagnostics.Debug.AssertInterpolatedStringHandler) -> None:
        ...

    @staticmethod
    @overload
    def Assert(condition: bool, message: str, detailMessage: str) -> None:
        ...

    @staticmethod
    @overload
    def Assert(condition: bool, message: System.Diagnostics.Debug.AssertInterpolatedStringHandler, detailMessage: System.Diagnostics.Debug.AssertInterpolatedStringHandler) -> None:
        ...

    @staticmethod
    @overload
    def Assert(condition: bool, message: str, detailMessageFormat: str, *args: typing.Union[System.Object, typing.Iterable[System.Object]]) -> None:
        ...

    @staticmethod
    def close() -> None:
        ...

    @staticmethod
    @overload
    def fail(message: str) -> None:
        ...

    @staticmethod
    @overload
    def fail(message: str, detail_message: str) -> None:
        ...

    @staticmethod
    def flush() -> None:
        ...

    @staticmethod
    def indent() -> None:
        ...

    @staticmethod
    @overload
    def print(message: str) -> None:
        ...

    @staticmethod
    @overload
    def print(format: str, *args: typing.Union[System.Object, typing.Iterable[System.Object]]) -> None:
        ...

    @staticmethod
    def set_provider(provider: System.Diagnostics.DebugProvider) -> System.Diagnostics.DebugProvider:
        ...

    @staticmethod
    def unindent() -> None:
        ...

    @staticmethod
    @overload
    def write(value: typing.Any) -> None:
        ...

    @staticmethod
    @overload
    def write(value: typing.Any, category: str) -> None:
        ...

    @staticmethod
    @overload
    def write(message: str) -> None:
        ...

    @staticmethod
    @overload
    def write(message: str, category: str) -> None:
        ...

    @staticmethod
    @overload
    def write_if(condition: bool, value: typing.Any) -> None:
        ...

    @staticmethod
    @overload
    def write_if(condition: bool, value: typing.Any, category: str) -> None:
        ...

    @staticmethod
    @overload
    def write_if(condition: bool, message: str) -> None:
        ...

    @staticmethod
    @overload
    def write_if(condition: bool, message: System.Diagnostics.Debug.WriteIfInterpolatedStringHandler) -> None:
        ...

    @staticmethod
    @overload
    def write_if(condition: bool, message: str, category: str) -> None:
        ...

    @staticmethod
    @overload
    def write_if(condition: bool, message: System.Diagnostics.Debug.WriteIfInterpolatedStringHandler, category: str) -> None:
        ...

    @staticmethod
    @overload
    def write_line(value: typing.Any) -> None:
        ...

    @staticmethod
    @overload
    def write_line(value: typing.Any, category: str) -> None:
        ...

    @staticmethod
    @overload
    def write_line(message: str) -> None:
        ...

    @staticmethod
    @overload
    def write_line(format: str, *args: typing.Union[System.Object, typing.Iterable[System.Object]]) -> None:
        ...

    @staticmethod
    @overload
    def write_line(message: str, category: str) -> None:
        ...

    @staticmethod
    @overload
    def write_line_if(condition: bool, value: typing.Any) -> None:
        ...

    @staticmethod
    @overload
    def write_line_if(condition: bool, value: typing.Any, category: str) -> None:
        ...

    @staticmethod
    @overload
    def write_line_if(condition: bool, message: str) -> None:
        ...

    @staticmethod
    @overload
    def write_line_if(condition: bool, message: System.Diagnostics.Debug.WriteIfInterpolatedStringHandler) -> None:
        ...

    @staticmethod
    @overload
    def write_line_if(condition: bool, message: str, category: str) -> None:
        ...

    @staticmethod
    @overload
    def write_line_if(condition: bool, message: System.Diagnostics.Debug.WriteIfInterpolatedStringHandler, category: str) -> None:
        ...


class StackFrame(System.Object):
    """There is no good reason for the methods of this class to be virtual."""

    OFFSET_UNKNOWN: int = -1
    """Constant returned when the native or IL offset is unknown"""

    @overload
    def __init__(self) -> None:
        """Constructs a StackFrame corresponding to the active stack frame."""
        ...

    @overload
    def __init__(self, need_file_info: bool) -> None:
        """Constructs a StackFrame corresponding to the active stack frame."""
        ...

    @overload
    def __init__(self, skip_frames: int) -> None:
        """Constructs a StackFrame corresponding to a calling stack frame."""
        ...

    @overload
    def __init__(self, skip_frames: int, need_file_info: bool) -> None:
        """Constructs a StackFrame corresponding to a calling stack frame."""
        ...

    @overload
    def __init__(self, file_name: str, line_number: int) -> None:
        """
        Constructs a "fake" stack frame, just containing the given file
        name and line number.  Use when you don't want to use the
        debugger's line mapping logic.
        """
        ...

    @overload
    def __init__(self, file_name: str, line_number: int, col_number: int) -> None:
        """
        Constructs a "fake" stack frame, just containing the given file
        name, line number and column number.  Use when you don't want to
        use the debugger's line mapping logic.
        """
        ...

    def get_file_column_number(self) -> int:
        """
        Returns the column number in the line containing the code being executed.
        This information is normally extracted from the debugging symbols
        for the executable.
        """
        ...

    def get_file_line_number(self) -> int:
        """
        Returns the line number in the file containing the code being executed.
        This information is normally extracted from the debugging symbols
        for the executable.
        """
        ...

    def get_file_name(self) -> str:
        """
        Returns the file name containing the code being executed.  This
        information is normally extracted from the debugging symbols
        for the executable.
        """
        ...

    def get_il_offset(self) -> int:
        """
        Returns the offset from the start of the IL code for the
        method being executed.  This offset may be approximate depending
        on whether the jitter is generating debuggable code or not.
        """
        ...

    def get_method(self) -> System.Reflection.MethodBase:
        ...

    def get_native_offset(self) -> int:
        """
        Returns the offset from the start of the native (jitted) code for the
        method being executed
        """
        ...

    def to_string(self) -> str:
        """Builds a readable representation of the stack frame"""
        ...


class DiagnosticMethodInfo(System.Object):
    """
    Represents diagnostic information about a method. Information provided by this class is similar to information
    provided by MethodBase but it's meant for logging and tracing purposes.
    """

    @property
    def name(self) -> str:
        """Gets the name of the method."""
        ...

    @property
    def declaring_type_name(self) -> str:
        """Gets the fully qualified name of the type that owns this method, including its namespace but not its assembly."""
        ...

    @property
    def declaring_assembly_name(self) -> str:
        """Gets the display name of the assembly that owns this method."""
        ...

    @staticmethod
    @overload
    def create(delegate: System.Delegate) -> System.Diagnostics.DiagnosticMethodInfo:
        """Creates a DiagnosticMethodInfo that represents the target of the delegate."""
        ...

    @staticmethod
    @overload
    def create(frame: System.Diagnostics.StackFrame) -> System.Diagnostics.DiagnosticMethodInfo:
        """Creates a DiagnosticMethodInfo that represents the method this stack frame is associtated with."""
        ...


class DebuggerVisualizerAttribute(System.Attribute):
    """
    Signifies that the attributed type has a visualizer which is pointed
    to by the parameter type name strings.
    """

    @property
    def visualizer_object_source_type_name(self) -> str:
        ...

    @property
    def visualizer_type_name(self) -> str:
        ...

    @property
    def description(self) -> str:
        ...

    @description.setter
    def description(self, value: str) -> None:
        ...

    @property
    def target(self) -> typing.Type:
        ...

    @target.setter
    def target(self, value: typing.Type) -> None:
        ...

    @property
    def target_type_name(self) -> str:
        ...

    @target_type_name.setter
    def target_type_name(self, value: str) -> None:
        ...

    @overload
    def __init__(self, visualizer_type_name: str) -> None:
        ...

    @overload
    def __init__(self, visualizer_type_name: str, visualizer_object_source_type_name: str) -> None:
        ...

    @overload
    def __init__(self, visualizer_type_name: str, visualizer_object_source: typing.Type) -> None:
        ...

    @overload
    def __init__(self, visualizer: typing.Type) -> None:
        ...

    @overload
    def __init__(self, visualizer: typing.Type, visualizer_object_source: typing.Type) -> None:
        ...

    @overload
    def __init__(self, visualizer: typing.Type, visualizer_object_source_type_name: str) -> None:
        ...


class ConditionalAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def condition_string(self) -> str:
        ...

    def __init__(self, condition_string: str) -> None:
        ...


class DebuggerHiddenAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class StackTrace(System.Object):
    """
    Class which represents a description of a stack trace
    There is no good reason for the methods of this class to be virtual.
    """

    METHODS_TO_SKIP: int = 0

    @property
    def frame_count(self) -> int:
        """Property to get the number of frames in the stack trace"""
        ...

    @overload
    def __init__(self) -> None:
        """Constructs a stack trace from the current location."""
        ...

    @overload
    def __init__(self, f_need_file_info: bool) -> None:
        """Constructs a stack trace from the current location."""
        ...

    @overload
    def __init__(self, skip_frames: int) -> None:
        """
        Constructs a stack trace from the current location, in a caller's
        frame
        """
        ...

    @overload
    def __init__(self, skip_frames: int, f_need_file_info: bool) -> None:
        """
        Constructs a stack trace from the current location, in a caller's
        frame
        """
        ...

    @overload
    def __init__(self, e: System.Exception) -> None:
        """Constructs a stack trace from the current location."""
        ...

    @overload
    def __init__(self, e: System.Exception, f_need_file_info: bool) -> None:
        """Constructs a stack trace from the current location."""
        ...

    @overload
    def __init__(self, e: System.Exception, skip_frames: int) -> None:
        """
        Constructs a stack trace from the current location, in a caller's
        frame
        """
        ...

    @overload
    def __init__(self, e: System.Exception, skip_frames: int, f_need_file_info: bool) -> None:
        """
        Constructs a stack trace from the current location, in a caller's
        frame
        """
        ...

    @overload
    def __init__(self, frame: System.Diagnostics.StackFrame) -> None:
        """
        Constructs a "fake" stack trace, just containing a single frame.
        Does not have the overhead of a full stack trace.
        """
        ...

    @overload
    def __init__(self, frames: System.Collections.Generic.IEnumerable[System.Diagnostics.StackFrame]) -> None:
        """
        Constructs a stack trace from a set of StackFrame objects
        
        :param frames: The set of stack frames that should be present in the stack trace
        """
        ...

    def get_frame(self, index: int) -> System.Diagnostics.StackFrame:
        """
        Returns a given stack frame.  Stack frames are numbered starting at
        zero, which is the last stack frame pushed.
        """
        ...

    def get_frames(self) -> typing.List[System.Diagnostics.StackFrame]:
        """
        Returns an array of all stack frames for this stacktrace.
        The array is ordered and sized such that GetFrames()[i] == GetFrame(i)
        The nth element of this array is the same as GetFrame(n).
        The length of the array is the same as FrameCount.
        """
        ...

    def to_string(self) -> str:
        """Builds a readable representation of the stack trace"""
        ...


class DebuggerDisplayAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def value(self) -> str:
        ...

    @property
    def name(self) -> str:
        ...

    @name.setter
    def name(self, value: str) -> None:
        ...

    @property
    def type(self) -> str:
        ...

    @type.setter
    def type(self, value: str) -> None:
        ...

    @property
    def target(self) -> typing.Type:
        ...

    @target.setter
    def target(self, value: typing.Type) -> None:
        ...

    @property
    def target_type_name(self) -> str:
        ...

    @target_type_name.setter
    def target_type_name(self, value: str) -> None:
        ...

    def __init__(self, value: str) -> None:
        ...


class Debugger(System.Object):
    """This class has no documentation."""

    @staticmethod
    def break_for_user_unhandled_exception(exception: System.Exception) -> None:
        """
        Signals a breakpoint to an attached debugger with the  details
        if a .NET debugger is attached with break on user-unhandled exception enabled and a method
        attributed with DebuggerDisableUserUnhandledExceptionsAttribute calls this method.
        
        :param exception: The user-unhandled exception.
        """
        ...


class DebuggerStepThroughAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class DebuggerBrowsableState(Enum):
    """This class has no documentation."""

    NEVER = 0

    COLLAPSED = 2

    ROOT_HIDDEN = 3


class DebuggerBrowsableAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def state(self) -> System.Diagnostics.DebuggerBrowsableState:
        ...

    def __init__(self, state: System.Diagnostics.DebuggerBrowsableState) -> None:
        ...


class StackFrameExtensions(System.Object):
    """This class has no documentation."""

    @staticmethod
    def get_native_image_base(stack_frame: System.Diagnostics.StackFrame) -> System.IntPtr:
        ...

    @staticmethod
    def get_native_ip(stack_frame: System.Diagnostics.StackFrame) -> System.IntPtr:
        ...

    @staticmethod
    def has_il_offset(stack_frame: System.Diagnostics.StackFrame) -> bool:
        ...

    @staticmethod
    def has_method(stack_frame: System.Diagnostics.StackFrame) -> bool:
        ...

    @staticmethod
    def has_native_image(stack_frame: System.Diagnostics.StackFrame) -> bool:
        ...

    @staticmethod
    def has_source(stack_frame: System.Diagnostics.StackFrame) -> bool:
        ...


