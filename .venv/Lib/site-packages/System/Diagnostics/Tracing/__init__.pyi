from typing import overload
from enum import Enum
import abc
import datetime
import typing

import System
import System.Collections.Generic
import System.Collections.ObjectModel
import System.Diagnostics.Tracing
import System.Runtime.Serialization

System_Diagnostics_Tracing__EventContainer_Callable = typing.TypeVar("System_Diagnostics_Tracing__EventContainer_Callable")
System_Diagnostics_Tracing__EventContainer_ReturnType = typing.TypeVar("System_Diagnostics_Tracing__EventContainer_ReturnType")


class EventActivityOptions(Enum):
    """EventActivityOptions flags allow to specify different activity related characteristics."""

    NONE = 0
    """No special options are added to the event."""

    DISABLE = ...
    """Disable Implicit Activity Tracking"""

    RECURSIVE = ...
    """Allow activity event to call itself (directly or indirectly)"""

    DETACHABLE = ...
    """Allows event activity to live beyond its parent."""


class EventSourceException(System.Exception):
    """Exception that is thrown when an error occurs during EventSource operation."""

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the EventSourceException class."""
        ...

    @overload
    def __init__(self, message: str) -> None:
        """Initializes a new instance of the EventSourceException class with a specified error message."""
        ...

    @overload
    def __init__(self, message: str, inner_exception: System.Exception) -> None:
        """
        Initializes a new instance of the EventSourceException class with a specified error message
        and a reference to the inner exception that is the cause of this exception.
        """
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """
        Initializes a new instance of the EventSourceException class with serialized data.
        
        This method is protected.
        
        Obsoletions.LegacyFormatterImplMessage
        """
        ...


class EventSourceSettings(Enum):
    """Enables specifying event source configuration options to be used in the EventSource constructor."""

    DEFAULT = 0
    """This specifies none of the special configuration options should be enabled."""

    THROW_ON_EVENT_WRITE_ERRORS = 1
    """Normally an EventSource NEVER throws; setting this option will tell it to throw when it encounters errors."""

    ETW_MANIFEST_EVENT_FORMAT = 4
    """
    Setting this option is a directive to the ETW listener should use manifest-based format when
    firing events. This is the default option when defining a type derived from EventSource
    (using the protected EventSource constructors).
    Only one of EtwManifestEventFormat or EtwSelfDescribingEventFormat should be specified
    """

    ETW_SELF_DESCRIBING_EVENT_FORMAT = 8
    """
    Setting this option is a directive to the ETW listener should use self-describing event format
    when firing events. This is the default option when creating a new instance of the EventSource
    type (using the public EventSource constructors).
    Only one of EtwManifestEventFormat or EtwSelfDescribingEventFormat should be specified
    """


class EventLevel(Enum):
    """
    Contains an event level that is defined in an event provider. The level signifies the severity of the event.
    Custom values must be in the range from 16 through 255.
    """

    LOG_ALWAYS = 0
    """Log always"""

    CRITICAL = 1
    """Only critical errors"""

    ERROR = 2
    """All errors, including previous levels"""

    WARNING = 3
    """All warnings, including previous levels"""

    INFORMATIONAL = 4
    """All informational events, including previous levels"""

    VERBOSE = 5
    """All events, including previous levels"""


class EventKeywords(Enum):
    """Defines the standard keywords that apply to events."""

    NONE = ...
    """No events."""

    ALL = ...
    """All Events"""

    MICROSOFT_TELEMETRY = ...
    """Telemetry events"""

    WDI_CONTEXT = ...
    """WDI context events"""

    WDI_DIAGNOSTIC = ...
    """WDI diagnostic events"""

    SQM = ...
    """SQM events"""

    AUDIT_FAILURE = ...
    """Failed security audits"""

    AUDIT_SUCCESS = ...
    """Successful security audits"""

    CORRELATION_HINT = ...
    """
    Transfer events where the related Activity ID is a computed value and not a GUID
    N.B. The correct value for this field is 0x40000000000000.
    """

    EVENT_LOG_CLASSIC = ...
    """Events raised using classic eventlog API"""


class EventChannel(Enum):
    """Specifies the event log channel for the event."""

    NONE = 0
    """No channel"""

    ADMIN = 16

    OPERATIONAL = 17
    """The operational channel"""

    ANALYTIC = 18
    """The analytic channel"""

    DEBUG = 19
    """The debug channel"""


class EventManifestOptions(Enum):
    """
    Flags that can be used with EventSource.GenerateManifest to control how the ETW manifest for the EventSource is
    generated.
    """

    NONE = ...
    """Only the resources associated with current UI culture are included in the  manifest"""

    STRICT = ...
    """Throw exceptions for any inconsistency encountered"""

    ALL_CULTURES = ...
    """Generate a "resources" node under "localization" for every satellite assembly provided"""

    ONLY_IF_NEEDED_FOR_REGISTRATION = ...
    """
    Generate the manifest only if the event source needs to be registered on the machine,
    otherwise return null (but still perform validation if Strict is specified)
    """

    ALLOW_EVENT_SOURCE_OVERRIDE = ...
    """
    When generating the manifest do *not* enforce the rule that the current EventSource class
    must be the base class for the user-defined type passed in. This allows validation of .net
    event sources using the new validation code
    """


class EventCommand(Enum):
    """Describes the pre-defined command (EventCommandEventArgs.Command property) that is passed to the OnEventCommand callback."""

    UPDATE = 0
    """Update EventSource state"""

    SEND_MANIFEST = -1
    """Request EventSource to generate and send its manifest"""

    ENABLE = -2
    """Enable event"""

    DISABLE = -3
    """Disable event"""


class EventCommandEventArgs(System.EventArgs):
    """Passed to the code:EventSource.OnEventCommand callback"""

    @property
    def command(self) -> System.Diagnostics.Tracing.EventCommand:
        """Gets the command for the callback."""
        ...

    @property
    def arguments(self) -> System.Collections.Generic.IDictionary[str, str]:
        """Gets the arguments for the callback."""
        ...

    def disable_event(self, event_id: int) -> bool:
        """
        Disables the event that have the specified identifier.
        
        :param event_id: Event ID of event to be disabled
        :returns: true if event_id is in range.
        """
        ...

    def enable_event(self, event_id: int) -> bool:
        """
        Enables the event that has the specified identifier.
        
        :param event_id: Event ID of event to be enabled
        :returns: true if event_id is in range.
        """
        ...


class EventOpcode(Enum):
    """
    Contains an event opcode that is defined in an event provider. An opcode defines a numeric value that identifies the activity or a point within an activity that the application was performing when it raised the event.
    Custom values must be in the range from 11 through 239.
    """

    INFO = 0
    """An informational event"""

    START = 1
    """An activity start event"""

    STOP = 2
    """An activity end event"""

    DATA_COLLECTION_START = 3
    """A trace collection start event"""

    DATA_COLLECTION_STOP = 4
    """A trace collection end event"""

    EXTENSION = 5
    """An extensional event"""

    REPLY = 6
    """A reply event"""

    RESUME = 7
    """An event representing the activity resuming from the suspension"""

    SUSPEND = 8
    """An event representing the activity is suspended, pending another activity's completion"""

    SEND = 9
    """An event representing the activity is transferred to another component, and can continue to work"""

    RECEIVE = 240
    """An event representing receiving an activity transfer from another component"""


class EventTags(Enum):
    """
    Tags are flags that are not interpreted by EventSource but are passed along
    to the EventListener. The EventListener determines the semantics of the flags.
    """

    NONE = 0
    """No special traits are added to the event."""


class EventSourceOptions:
    """
    Used when calling EventSource.Write.
    Optional overrides for event settings such as Level, Keywords, or Opcode.
    If overrides are not provided for a setting, default values will be used.
    """

    @property
    def level(self) -> System.Diagnostics.Tracing.EventLevel:
        """
        Gets or sets the level to use for the specified event. If this property
        is unset, the event's level will be 5 (Verbose).
        """
        ...

    @level.setter
    def level(self, value: System.Diagnostics.Tracing.EventLevel) -> None:
        ...

    @property
    def opcode(self) -> System.Diagnostics.Tracing.EventOpcode:
        """
        Gets or sets the opcode to use for the specified event. If this property
        is unset, the event's opcode will 0 (Info).
        """
        ...

    @opcode.setter
    def opcode(self, value: System.Diagnostics.Tracing.EventOpcode) -> None:
        ...

    @property
    def keywords(self) -> System.Diagnostics.Tracing.EventKeywords:
        """
        Gets or sets the keywords to use for the specified event. If this
        property is unset, the event's keywords will be 0.
        """
        ...

    @keywords.setter
    def keywords(self, value: System.Diagnostics.Tracing.EventKeywords) -> None:
        ...

    @property
    def tags(self) -> System.Diagnostics.Tracing.EventTags:
        """
        Gets or sets the tags to use for the specified event. If this property is
        unset, the event's tags will be 0.
        """
        ...

    @tags.setter
    def tags(self, value: System.Diagnostics.Tracing.EventTags) -> None:
        ...

    @property
    def activity_options(self) -> System.Diagnostics.Tracing.EventActivityOptions:
        """
        Gets or sets the activity options for this specified events. If this property is
        unset, the event's activity options will be 0.
        """
        ...

    @activity_options.setter
    def activity_options(self, value: System.Diagnostics.Tracing.EventActivityOptions) -> None:
        ...


class EventSource(System.Object, System.IDisposable):
    """
    This class is meant to be inherited by a user-defined event source in order to define a managed
    ETW provider.   Please See DESIGN NOTES above for the internal architecture.
    The minimal definition of an EventSource simply specifies a number of ETW event methods that
    call one of the EventSource.WriteEvent overloads, WriteEventCore,
    or WriteEventWithRelatedActivityIdCore to log them. This functionality
    is sufficient for many users.
    
    To achieve more control over the ETW provider manifest exposed by the event source type, the
    [] attributes can be specified for the ETW event methods.
    
    For very advanced EventSources, it is possible to intercept the commands being given to the
    eventSource and change what filtering is done (see EventListener.EnableEvents and
    ) or cause actions to be performed by the eventSource,
    e.g. dumping a data structure (see EventSource.SendCommand and
    ).
    
    The eventSources can be turned on with Windows ETW controllers (e.g. logman), immediately.
    It is also possible to control and intercept the data dispatcher programmatically.  See
     for more.
    """

    class EventSourcePrimitive:
        """
        A wrapper type for separating primitive types (int, long, string, etc) from other types
        in the EventSource API. This type shouldn't be used directly, but just as implicit conversions
        when using the WriteEvent API.
        """

    @property
    def name(self) -> str:
        """The human-friendly name of the eventSource.  It defaults to the simple name of the class"""
        ...

    @property
    def guid(self) -> System.Guid:
        """Every eventSource is assigned a GUID to uniquely identify it to the system."""
        ...

    @property
    def settings(self) -> System.Diagnostics.Tracing.EventSourceSettings:
        """Returns the settings for the event source instance"""
        ...

    @property
    def construction_exception(self) -> System.Exception:
        ...

    @property
    def event_command_executed(self) -> _EventContainer[typing.Callable[[System.Object, System.Diagnostics.Tracing.EventCommandEventArgs], None], None]:
        """Fires when a Command (e.g. Enable) comes from a an EventListener."""
        ...

    @event_command_executed.setter
    def event_command_executed(self, value: _EventContainer[typing.Callable[[System.Object, System.Diagnostics.Tracing.EventCommandEventArgs], None], None]) -> None:
        ...

    CURRENT_THREAD_ACTIVITY_ID: System.Guid
    """Retrieves the ETW activity ID associated with the current thread."""

    @overload
    def __init__(self) -> None:
        """This method is protected."""
        ...

    @overload
    def __init__(self, throw_on_event_write_errors: bool) -> None:
        """
        By default calling the 'WriteEvent' methods do NOT throw on errors (they silently discard the event).
        This is because in most cases users assume logging is not 'precious' and do NOT wish to have logging failures
        crash the program. However for those applications where logging is 'precious' and if it fails the caller
        wishes to react, setting 'throw_on_event_write_errors' will cause an exception to be thrown if WriteEvent
        fails. Note the fact that EventWrite succeeds does not necessarily mean that the event reached its destination
        only that operation of writing it did not fail. These EventSources will not generate self-describing ETW events.
        
        For compatibility only use the EventSourceSettings.ThrowOnEventWriteErrors flag instead.
        
        This method is protected.
        """
        ...

    @overload
    def __init__(self, settings: System.Diagnostics.Tracing.EventSourceSettings) -> None:
        """
        Construct an EventSource with additional non-default settings (see EventSourceSettings for more)
        
        This method is protected.
        """
        ...

    @overload
    def __init__(self, settings: System.Diagnostics.Tracing.EventSourceSettings, *traits: typing.Union[str, typing.Iterable[str]]) -> None:
        """
        Construct an EventSource with additional non-default settings.
        
        Also specify a list of key-value pairs called traits (you must pass an even number of strings).
        The first string is the key and the second is the value.   These are not interpreted by EventSource
        itself but may be interpreted the listeners.  Can be fetched with GetTrait(string).
        
        This method is protected.
        
        :param settings: See EventSourceSettings for more.
        :param traits: A collection of key-value strings (must be an even number).
        """
        ...

    @overload
    def __init__(self, event_source_name: str) -> None:
        """
        Construct an EventSource with a given name for non-contract based events (e.g. those using the Write() API).
        
        :param event_source_name: The name of the event source. Must not be null.
        """
        ...

    @overload
    def __init__(self, event_source_name: str, config: System.Diagnostics.Tracing.EventSourceSettings) -> None:
        """
        Construct an EventSource with a given name for non-contract based events (e.g. those using the Write() API).
        
        :param event_source_name: The name of the event source. Must not be null.
        :param config: Configuration options for the EventSource as a whole.
        """
        ...

    @overload
    def __init__(self, event_source_name: str, config: System.Diagnostics.Tracing.EventSourceSettings, *traits: typing.Union[str, typing.Iterable[str]]) -> None:
        """
        Construct an EventSource with a given name for non-contract based events (e.g. those using the Write() API).
        
        Also specify a list of key-value pairs called traits (you must pass an even number of strings).
        The first string is the key and the second is the value.   These are not interpreted by EventSource
        itself but may be interpreted the listeners.  Can be fetched with GetTrait(string).
        
        :param event_source_name: The name of the event source. Must not be null.
        :param config: Configuration options for the EventSource as a whole.
        :param traits: A collection of key-value strings (must be an even number).
        """
        ...

    @overload
    def dispose(self) -> None:
        ...

    @overload
    def dispose(self, disposing: bool) -> None:
        """
        Disposes of an EventSource.
        
        This method is protected.
        
        :param disposing: True if called from Dispose(), false if called from the finalizer.
        """
        ...

    @staticmethod
    @overload
    def generate_manifest(event_source_type: typing.Type, assembly_path_to_include_in_manifest: str) -> str:
        """
        Returns a string of the XML manifest associated with the event_source_type. The scheme for this XML is
        documented at in EventManifest Schema https://learn.microsoft.com/windows/desktop/WES/eventmanifestschema-schema.
        This is the preferred way of generating a manifest to be embedded in the ETW stream as it is fast and
        the fact that it only includes localized entries for the current UI culture is an acceptable tradeoff.
        
        :param event_source_type: The type of the event source class for which the manifest is generated
        :param assembly_path_to_include_in_manifest: The manifest XML fragment contains the string name of the DLL name in which it is embedded.  This parameter specifies what name will be used
        :returns: The XML data string.
        """
        ...

    @staticmethod
    @overload
    def generate_manifest(event_source_type: typing.Type, assembly_path_to_include_in_manifest: str, flags: System.Diagnostics.Tracing.EventManifestOptions) -> str:
        """
        Returns a string of the XML manifest associated with the event_source_type. The scheme for this XML is
        documented at in EventManifest Schema https://learn.microsoft.com/windows/desktop/WES/eventmanifestschema-schema.
        Pass EventManifestOptions.AllCultures when generating a manifest to be registered on the machine. This
        ensures that the entries in the event log will be "optimally" localized.
        
        :param event_source_type: The type of the event source class for which the manifest is generated
        :param assembly_path_to_include_in_manifest: The manifest XML fragment contains the string name of the DLL name in which it is embedded.  This parameter specifies what name will be used
        :param flags: The flags to customize manifest generation. If flags has bit OnlyIfNeededForRegistration specified this returns null when the event_source_type does not require explicit registration
        :returns: The XML data string or null.
        """
        ...

    @staticmethod
    def get_guid(event_source_type: typing.Type) -> System.Guid:
        ...

    @staticmethod
    def get_name(event_source_type: typing.Type) -> str:
        """
        Returns the official ETW Provider name for the eventSource defined by 'event_source_type'.
        This API allows you to compute this without actually creating an instance of the EventSource.
        It only needs to reflect over the type.
        """
        ...

    @staticmethod
    def get_sources() -> System.Collections.Generic.IEnumerable[System.Diagnostics.Tracing.EventSource]:
        ...

    def get_trait(self, key: str) -> str:
        """
        EventSources can have arbitrary string key-value pairs associated with them called Traits.
        These traits are not interpreted by the EventSource but may be interpreted by EventListeners
        (e.g. like the built in ETW listener).   These traits are specified at EventSource
        construction time and can be retrieved by using this GetTrait API.
        
        :param key: The key to look up in the set of key-value pairs passed to the EventSource constructor
        :returns: The value string associated with key.  Will return null if there is no such key.
        """
        ...

    @overload
    def is_enabled(self) -> bool:
        """
        Returns true if the eventSource has been enabled at all. This is the preferred test
        to be performed before a relatively expensive EventSource operation.
        """
        ...

    @overload
    def is_enabled(self, level: System.Diagnostics.Tracing.EventLevel, keywords: System.Diagnostics.Tracing.EventKeywords) -> bool:
        """
        Returns true if events with greater than or equal 'level' and have one of 'keywords' set are enabled.
        
        Note that the result of this function is only an approximation on whether a particular
        event is active or not. It is only meant to be used as way of avoiding expensive
        computation for logging when logging is not on, therefore it sometimes returns false
        positives (but is always accurate when returning false).  EventSources are free to
        have additional filtering.
        """
        ...

    @overload
    def is_enabled(self, level: System.Diagnostics.Tracing.EventLevel, keywords: System.Diagnostics.Tracing.EventKeywords, channel: System.Diagnostics.Tracing.EventChannel) -> bool:
        """
        Returns true if events with greater than or equal 'level' and have one of 'keywords' set are enabled, or
        if 'keywords' specifies a channel bit for a channel that is enabled.
        
        Note that the result of this function only an approximation on whether a particular
        event is active or not. It is only meant to be used as way of avoiding expensive
        computation for logging when logging is not on, therefore it sometimes returns false
        positives (but is always accurate when returning false).  EventSources are free to
        have additional filtering.
        """
        ...

    def on_event_command(self, command: System.Diagnostics.Tracing.EventCommandEventArgs) -> None:
        """
        This method is called when the eventSource is updated by the controller.
        
        This method is protected.
        """
        ...

    @staticmethod
    def send_command(event_source: System.Diagnostics.Tracing.EventSource, command: System.Diagnostics.Tracing.EventCommand, command_arguments: System.Collections.Generic.IDictionary[str, str]) -> None:
        """
        Send a command to a particular EventSource identified by 'event_source'.
        Calling this routine simply forwards the command to the EventSource.OnEventCommand
        callback.  What the EventSource does with the command and its arguments are from
        that point EventSource-specific.
        
        :param event_source: The instance of EventSource to send the command to
        :param command: A positive user-defined EventCommand, or EventCommand.SendManifest
        :param command_arguments: A set of (name-argument, value-argument) pairs associated with the command
        """
        ...

    @staticmethod
    @overload
    def set_current_thread_activity_id(activity_id: System.Guid) -> None:
        """
        When a thread starts work that is on behalf of 'something else' (typically another
        thread or network request) it should mark the thread as working on that other work.
        This API marks the current thread as working on activity 'activityID'. This API
        should be used when the caller knows the thread's current activity (the one being
        overwritten) has completed. Otherwise, callers should prefer the overload that
        return the oldActivityThatWillContinue (below).
        
        All events created with the EventSource on this thread are also tagged with the
        activity ID of the thread.
        
        It is common, and good practice after setting the thread to an activity to log an event
        with a 'start' opcode to indicate that precise time/thread where the new activity
        started.
        
        :param activity_id: A Guid that represents the new activity with which to mark the current thread
        """
        ...

    @staticmethod
    @overload
    def set_current_thread_activity_id(activity_id: System.Guid, old_activity_that_will_continue: typing.Optional[System.Guid]) -> typing.Tuple[None, System.Guid]:
        """
        When a thread starts work that is on behalf of 'something else' (typically another
        thread or network request) it should mark the thread as working on that other work.
        This API marks the current thread as working on activity 'activityID'. It returns
        whatever activity the thread was previously marked with. There is a convention that
        callers can assume that callees restore this activity mark before the callee returns.
        To encourage this, this API returns the old activity, so that it can be restored later.
        
        All events created with the EventSource on this thread are also tagged with the
        activity ID of the thread.
        
        It is common, and good practice after setting the thread to an activity to log an event
        with a 'start' opcode to indicate that precise time/thread where the new activity
        started.
        
        :param activity_id: A Guid that represents the new activity with which to mark the current thread
        :param old_activity_that_will_continue: The Guid that represents the current activity which will continue at some point in the future, on the current thread
        """
        ...

    def to_string(self) -> str:
        """Displays the name and GUID for the eventSource for debugging purposes."""
        ...

    @overload
    def write(self, event_name: str) -> None:
        """
        Writes an event with no fields and default options.
        (Native API: EventWriteTransfer)
        
        :param event_name: The name of the event.
        """
        ...

    @overload
    def write(self, event_name: str, options: System.Diagnostics.Tracing.EventSourceOptions) -> None:
        """
        Writes an event with no fields.
        (Native API: EventWriteTransfer)
        
        :param event_name: The name of the event.
        :param options: Options for the event, such as the level, keywords, and opcode. Unset options will be set to default values.
        """
        ...

    @overload
    def write_event(self, event_id: int) -> None:
        """This method is protected."""
        ...

    @overload
    def write_event(self, event_id: int, arg_1: int) -> None:
        """This method is protected."""
        ...

    @overload
    def write_event(self, event_id: int, arg_1: int, arg_2: int) -> None:
        """This method is protected."""
        ...

    @overload
    def write_event(self, event_id: int, arg_1: int, arg_2: int, arg_3: int) -> None:
        """This method is protected."""
        ...

    @overload
    def write_event(self, event_id: int, arg_1: str) -> None:
        """This method is protected."""
        ...

    @overload
    def write_event(self, event_id: int, arg_1: str, arg_2: str) -> None:
        """This method is protected."""
        ...

    @overload
    def write_event(self, event_id: int, arg_1: str, arg_2: str, arg_3: str) -> None:
        """This method is protected."""
        ...

    @overload
    def write_event(self, event_id: int, arg_1: str, arg_2: int) -> None:
        """This method is protected."""
        ...

    @overload
    def write_event(self, event_id: int, arg_1: str, arg_2: int, arg_3: int) -> None:
        """This method is protected."""
        ...

    @overload
    def write_event(self, event_id: int, arg_1: int, arg_2: str) -> None:
        """This method is protected."""
        ...

    @overload
    def write_event(self, event_id: int, arg_1: typing.List[int]) -> None:
        """This method is protected."""
        ...

    @overload
    def write_event(self, event_id: int, arg_1: int, arg_2: typing.List[int]) -> None:
        """This method is protected."""
        ...

    @overload
    def write_event(self, event_id: int, *args: typing.Union[System.Diagnostics.Tracing.EventSource.EventSourcePrimitive, typing.Iterable[System.Diagnostics.Tracing.EventSource.EventSourcePrimitive]]) -> None:
        """
        This is a varargs helper for writing an event. It does create an array and box all the arguments so it is
        relatively inefficient and should only be used for relatively rare events (e.g. less than 100 / sec). If your
        rates are faster than that you should use WriteEventCore to create fast helpers for your particular
        method signature. Even if you use this for rare events, this call should be guarded by an IsEnabled()
        check so that the varargs call is not made when the EventSource is not active.
        
        This method is protected.
        """
        ...

    @overload
    def write_event(self, event_id: int, *args: typing.Union[System.Object, typing.Iterable[System.Object]]) -> None:
        """This method is protected."""
        ...

    def write_event_core(self, event_id: int, event_data_count: int, data: typing.Any) -> None:
        """
        This routine allows you to create efficient WriteEvent helpers, however the code that you use to
        do this, while straightforward, is unsafe.
        
        This method is protected.
        """
        ...

    def write_event_with_related_activity_id(self, event_id: int, related_activity_id: System.Guid, *args: typing.Union[System.Object, typing.Iterable[System.Object]]) -> None:
        """
        This is the varargs helper for writing an event which also specifies a related activity. It is completely analogous
        to corresponding WriteEvent (they share implementation). It does create an array and box all the arguments so it is
        relatively inefficient and should only be used for relatively rare events (e.g. less than 100 / sec).  If your
        rates are faster than that you should use WriteEventWithRelatedActivityIdCore to create fast helpers for your
        particular method signature. Even if you use this for rare events, this call should be guarded by an IsEnabled()
        check so that the varargs call is not made when the EventSource is not active.
        
        This method is protected.
        """
        ...

    def write_event_with_related_activity_id_core(self, event_id: int, related_activity_id: typing.Any, event_data_count: int, data: typing.Any) -> None:
        """
        This routine allows you to create efficient WriteEventWithRelatedActivityId helpers, however the code
        that you use to do this, while straightforward, is unsafe. The only difference from
        WriteEventCore is that you pass the related_activity_id from caller through to this API
        
        This method is protected.
        """
        ...


class DiagnosticCounter(System.Object, System.IDisposable, metaclass=abc.ABCMeta):
    """
    DiagnosticCounter is an abstract class that serves as the parent class for various Counter* classes,
    namely EventCounter, PollingCounter, IncrementingEventCounter, and IncrementingPollingCounter.
    """

    @property
    def display_name(self) -> str:
        ...

    @display_name.setter
    def display_name(self, value: str) -> None:
        ...

    @property
    def display_units(self) -> str:
        ...

    @display_units.setter
    def display_units(self, value: str) -> None:
        ...

    @property
    def name(self) -> str:
        ...

    @property
    def event_source(self) -> System.Diagnostics.Tracing.EventSource:
        ...

    def add_metadata(self, key: str, value: str) -> None:
        """Adds a key-value metadata to the EventCounter that will be included as a part of the payload"""
        ...

    def dispose(self) -> None:
        """
        Removes the counter from set that the EventSource will report on.  After being disposed, this
        counter will do nothing and its resource will be reclaimed if all references to it are removed.
        If an EventCounter is not explicitly disposed it will be cleaned up automatically when the
        EventSource it is attached to dies.
        """
        ...


class EventCounter(System.Diagnostics.Tracing.DiagnosticCounter):
    """
    Provides the ability to collect statistics through EventSource
    
    See https://github.com/dotnet/runtime/blob/main/src/libraries/System.Diagnostics.Tracing/documentation/EventCounterTutorial.md
    for a tutorial guide.
    
    See https://github.com/dotnet/runtime/blob/main/src/libraries/System.Diagnostics.Tracing/tests/BasicEventSourceTest/TestEventCounter.cs
    which shows tests, which are also useful in seeing actual use.
    """

    def __init__(self, name: str, event_source: System.Diagnostics.Tracing.EventSource) -> None:
        """
        Initializes a new instance of the EventCounter class.
        EVentCounters live as long as the EventSource that they are attached to unless they are
        explicitly Disposed.
        
        :param name: The name.
        :param event_source: The event source.
        """
        ...

    def to_string(self) -> str:
        ...

    def write_metric(self, value: float) -> None:
        """
        Writes 'value' to the stream of values tracked by the counter.  This updates the sum and other statistics that will
        be logged on the next timer interval.
        
        :param value: The value.
        """
        ...


class EventSourceCreatedEventArgs(System.EventArgs):
    """EventSourceCreatedEventArgs is passed to EventListener.EventSourceCreated"""

    @property
    def event_source(self) -> System.Diagnostics.Tracing.EventSource:
        """The EventSource that is attaching to the listener."""
        ...


class EventTask(Enum):
    """
    Contains an event task that is defined in an event provider. The task identifies a portion of an application or a component that publishes an event. A task is a 16-bit value with 16 top values reserved.
    Custom values must be in the range from 1 through 65534.
    """

    NONE = 0
    """Undefined task"""


class EventWrittenEventArgs(System.EventArgs):
    """
    EventWrittenEventArgs is passed to the user-provided override for
    EventListener.OnEventWritten when an event is fired.
    """

    @property
    def event_name(self) -> str:
        """The name of the event."""
        ...

    @property
    def event_id(self) -> int:
        """Gets the event ID for the event that was written."""
        ...

    @property
    def activity_id(self) -> System.Guid:
        """Gets the activity ID for the thread on which the event was written."""
        ...

    @property
    def related_activity_id(self) -> System.Guid:
        """Gets the related activity ID if one was specified when the event was written."""
        ...

    @property
    def payload(self) -> System.Collections.ObjectModel.ReadOnlyCollection[System.Object]:
        """Gets the payload for the event."""
        ...

    @property
    def payload_names(self) -> System.Collections.ObjectModel.ReadOnlyCollection[str]:
        """Gets the payload argument names."""
        ...

    @property
    def event_source(self) -> System.Diagnostics.Tracing.EventSource:
        """Gets the event source object."""
        ...

    @property
    def keywords(self) -> System.Diagnostics.Tracing.EventKeywords:
        """Gets the keywords for the event."""
        ...

    @property
    def opcode(self) -> System.Diagnostics.Tracing.EventOpcode:
        """Gets the operation code for the event."""
        ...

    @property
    def task(self) -> System.Diagnostics.Tracing.EventTask:
        """Gets the task for the event."""
        ...

    @property
    def tags(self) -> System.Diagnostics.Tracing.EventTags:
        """Any provider/user defined options associated with the event."""
        ...

    @property
    def message(self) -> str:
        """Gets the message for the event.  If the message has {N} parameters they are NOT substituted."""
        ...

    @property
    def channel(self) -> System.Diagnostics.Tracing.EventChannel:
        """Gets the channel for the event."""
        ...

    @property
    def version(self) -> int:
        """Gets the version of the event."""
        ...

    @property
    def level(self) -> System.Diagnostics.Tracing.EventLevel:
        """Gets the level for the event."""
        ...

    @property
    def os_thread_id(self) -> int:
        """Gets the identifier for the OS thread that wrote the event."""
        ...

    @property
    def time_stamp(self) -> datetime.datetime:
        """Gets a UTC DateTime that specifies when the event was written."""
        ...


class EventListener(System.Object, System.IDisposable, metaclass=abc.ABCMeta):
    """
    An EventListener represents a target for the events generated by EventSources (that is subclasses
    of EventSource), in the current appdomain. When a new EventListener is created
    it is logically attached to all eventSources in that appdomain. When the EventListener is Disposed, then
    it is disconnected from the event eventSources. Note that there is a internal list of STRONG references
    to EventListeners, which means that relying on the lack of references to EventListeners to clean up
    EventListeners will NOT work. You must call EventListener.Dispose explicitly when a dispatcher is no
    longer needed.
    
    Once created, EventListeners can enable or disable on a per-eventSource basis using verbosity levels
    () and bitfields () to further restrict the set of
    events to be sent to the dispatcher. The dispatcher can also send arbitrary commands to a particular
    eventSource using the 'SendCommand' method. The meaning of the commands are eventSource specific.
    
    The Null Guid (that is (new Guid()) has special meaning as a wildcard for 'all current eventSources in
    the appdomain'. Thus it is relatively easy to turn on all events in the appdomain if desired.
    
    It is possible for there to be many EventListener's defined in a single appdomain. Each dispatcher is
    logically independent of the other listeners. Thus when one dispatcher enables or disables events, it
    affects only that dispatcher (other listeners get the events they asked for). It is possible that
    commands sent with 'SendCommand' would do a semantic operation that would affect the other listeners
    (like doing a GC, or flushing data ...), but this is the exception rather than the rule.
    
    Thus the model is that each EventSource keeps a list of EventListeners that it is sending events
    to. Associated with each EventSource-dispatcher pair is a set of filtering criteria that determine for
    that eventSource what events that dispatcher will receive.
    
    Listeners receive the events on their 'OnEventWritten' method. Thus subclasses of EventListener must
    override this method to do something useful with the data.
    
    In addition, when new eventSources are created, the 'OnEventSourceCreate' method is called. The
    invariant associated with this callback is that every eventSource gets exactly one
    'OnEventSourceCreate' call for ever eventSource that can potentially send it log messages. In
    particular when a EventListener is created, typically a series of OnEventSourceCreate' calls are
    made to notify the new dispatcher of all the eventSources that existed before the EventListener was
    created.
    """

    @property
    def event_source_created(self) -> _EventContainer[typing.Callable[[System.Object, System.Diagnostics.Tracing.EventSourceCreatedEventArgs], None], None]:
        """
        This event is raised whenever a new eventSource is 'attached' to the dispatcher.
        This can happen for all existing EventSources when the EventListener is created
        as well as for any EventSources that come into existence after the EventListener
        has been created.
        
        These 'catch up' events are called during the construction of the EventListener.
        Subclasses need to be prepared for that.
        
        In a multi-threaded environment, it is possible that 'EventSourceEventWrittenCallback'
        events for a particular eventSource to occur BEFORE the EventSourceCreatedCallback is issued.
        """
        ...

    @event_source_created.setter
    def event_source_created(self, value: _EventContainer[typing.Callable[[System.Object, System.Diagnostics.Tracing.EventSourceCreatedEventArgs], None], None]) -> None:
        ...

    @property
    def event_written(self) -> _EventContainer[typing.Callable[[System.Object, System.Diagnostics.Tracing.EventWrittenEventArgs], None], None]:
        """
        This event is raised whenever an event has been written by a EventSource for which
        the EventListener has enabled events.
        """
        ...

    @event_written.setter
    def event_written(self, value: _EventContainer[typing.Callable[[System.Object, System.Diagnostics.Tracing.EventWrittenEventArgs], None], None]) -> None:
        ...

    def __init__(self) -> None:
        """
        Create a new EventListener in which all events start off turned off (use EnableEvents to turn
        them on).
        
        This method is protected.
        """
        ...

    def disable_events(self, event_source: System.Diagnostics.Tracing.EventSource) -> None:
        """
        Disables all events coming from event_source identified by 'event_source'.
        
        This call never has an effect on other EventListeners.
        """
        ...

    def dispose(self) -> None:
        """
        Dispose should be called when the EventListener no longer desires 'OnEvent*' callbacks. Because
        there is an internal list of strong references to all EventListeners, calling 'Dispose' directly
        is the only way to actually make the listen die. Thus it is important that users of EventListener
        call Dispose when they are done with their logging.
        """
        ...

    @overload
    def enable_events(self, event_source: System.Diagnostics.Tracing.EventSource, level: System.Diagnostics.Tracing.EventLevel) -> None:
        """
        Enable all events from the event_source identified by 'event_source' to the current
        dispatcher that have a verbosity level of 'level' or lower.
        
        This call can have the effect of REDUCING the number of events sent to the
        dispatcher if 'level' indicates a less verbose level than was previously enabled.
        
        This call never has an effect on other EventListeners.
        """
        ...

    @overload
    def enable_events(self, event_source: System.Diagnostics.Tracing.EventSource, level: System.Diagnostics.Tracing.EventLevel, match_any_keyword: System.Diagnostics.Tracing.EventKeywords) -> None:
        """
        Enable all events from the event_source identified by 'event_source' to the current
        dispatcher that have a verbosity level of 'level' or lower and have a event keyword
        matching any of the bits in 'match_any_keyword'.
        
        This call can have the effect of REDUCING the number of events sent to the
        dispatcher if 'level' indicates a less verbose level than was previously enabled or
        if 'match_any_keyword' has fewer keywords set than where previously set.
        
        This call never has an effect on other EventListeners.
        """
        ...

    @overload
    def enable_events(self, event_source: System.Diagnostics.Tracing.EventSource, level: System.Diagnostics.Tracing.EventLevel, match_any_keyword: System.Diagnostics.Tracing.EventKeywords, arguments: System.Collections.Generic.IDictionary[str, str]) -> None:
        """
        Enable all events from the event_source identified by 'event_source' to the current
        dispatcher that have a verbosity level of 'level' or lower and have a event keyword
        matching any of the bits in 'match_any_keyword' as well as any (event_source specific)
        effect passing additional 'key-value' arguments 'arguments' might have.
        
        This call can have the effect of REDUCING the number of events sent to the
        dispatcher if 'level' indicates a less verbose level than was previously enabled or
        if 'match_any_keyword' has fewer keywords set than where previously set.
        
        This call never has an effect on other EventListeners.
        """
        ...


class EventSourceAttribute(System.Attribute):
    """Allows customizing defaults and specifying localization support for the event source class to which it is applied."""

    @property
    def name(self) -> str:
        """Overrides the ETW name of the event source (which defaults to the class name)"""
        ...

    @name.setter
    def name(self, value: str) -> None:
        ...

    @property
    def guid(self) -> str:
        """
        Overrides the default (calculated) Guid of an EventSource type. Explicitly defining a GUID is discouraged,
        except when upgrading existing ETW providers to using event sources.
        """
        ...

    @guid.setter
    def guid(self, value: str) -> None:
        ...

    @property
    def localization_resources(self) -> str:
        """
        EventSources support localization of events. The names used for events, opcodes, tasks, keywords and maps
        can be localized to several languages if desired. This works by creating a ResX style string table
        (by simply adding a 'Resource File' to your project). This resource file is given a name e.g.
        'DefaultNameSpace.ResourceFileName' which can be passed to the ResourceManager constructor to read the
        resources. This name is the value of the LocalizationResources property.
        
        If LocalizationResources property is non-null, then EventSource will look up the localized strings for events by
        using the following resource naming scheme
        * event_EVENTNAME* task_TASKNAME* keyword_KEYWORDNAME* map_MAPNAME
        where the capitalized name is the name of the event, task, keyword, or map value that should be localized.
        Note that the localized string for an event corresponds to the Message string, and can have {0} values
        which represent the payload values.
        """
        ...

    @localization_resources.setter
    def localization_resources(self, value: str) -> None:
        ...


class EventAttribute(System.Attribute):
    """
    Any instance methods in a class that subclasses EventSource and that return void are
    assumed by default to be methods that generate an ETW event. Enough information can be deduced from the
    name of the method and its signature to generate basic schema information for the event. The
    EventAttribute class allows you to specify additional event schema information for an event if
    desired.
    """

    @property
    def event_id(self) -> int:
        """Event's ID"""
        ...

    @property
    def level(self) -> System.Diagnostics.Tracing.EventLevel:
        """Event's severity level: indicates the severity or verbosity of the event"""
        ...

    @level.setter
    def level(self, value: System.Diagnostics.Tracing.EventLevel) -> None:
        ...

    @property
    def keywords(self) -> System.Diagnostics.Tracing.EventKeywords:
        """Event's keywords: allows classification of events by "categories\""""
        ...

    @keywords.setter
    def keywords(self, value: System.Diagnostics.Tracing.EventKeywords) -> None:
        ...

    @property
    def opcode(self) -> System.Diagnostics.Tracing.EventOpcode:
        """Event's operation code: allows defining operations, generally used with Tasks"""
        ...

    @opcode.setter
    def opcode(self, value: System.Diagnostics.Tracing.EventOpcode) -> None:
        ...

    @property
    def task(self) -> System.Diagnostics.Tracing.EventTask:
        """Event's task: allows logical grouping of events"""
        ...

    @task.setter
    def task(self, value: System.Diagnostics.Tracing.EventTask) -> None:
        ...

    @property
    def channel(self) -> System.Diagnostics.Tracing.EventChannel:
        """Event's channel: defines an event log as an additional destination for the event"""
        ...

    @channel.setter
    def channel(self, value: System.Diagnostics.Tracing.EventChannel) -> None:
        ...

    @property
    def version(self) -> int:
        """Event's version"""
        ...

    @version.setter
    def version(self, value: int) -> None:
        ...

    @property
    def message(self) -> str:
        """
        This can be specified to enable formatting and localization of the event's payload. You can
        use standard .NET substitution operators (eg {1}) in the string and they will be replaced
        with the 'ToString()' of the corresponding part of the  event payload.
        """
        ...

    @message.setter
    def message(self, value: str) -> None:
        ...

    @property
    def tags(self) -> System.Diagnostics.Tracing.EventTags:
        """
        User defined options associated with the event.  These do not have meaning to the EventSource but
        are passed through to listeners which given them semantics.
        """
        ...

    @tags.setter
    def tags(self, value: System.Diagnostics.Tracing.EventTags) -> None:
        ...

    @property
    def activity_options(self) -> System.Diagnostics.Tracing.EventActivityOptions:
        """Allows fine control over the Activity IDs generated by start and stop events"""
        ...

    @activity_options.setter
    def activity_options(self, value: System.Diagnostics.Tracing.EventActivityOptions) -> None:
        ...

    def __init__(self, event_id: int) -> None:
        """
        Construct an EventAttribute with specified event_id
        
        :param event_id: ID of the ETW event (an integer between 1 and 65535)
        """
        ...


class NonEventAttribute(System.Attribute):
    """
    By default all instance methods in a class that subclasses code:EventSource that and return
    void are assumed to be methods that generate an event. This default can be overridden by specifying
    the code:NonEventAttribute
    """

    def __init__(self) -> None:
        """Constructs a default NonEventAttribute"""
        ...


class IncrementingEventCounter(System.Diagnostics.Tracing.DiagnosticCounter):
    """
    IncrementingEventCounter is a variant of EventCounter for variables that are ever-increasing.
    Ex) # of exceptions in the runtime.
    It does not calculate statistics like mean, standard deviation, etc. because it only accumulates
    the counter value.
    """

    @property
    def display_rate_time_scale(self) -> datetime.timedelta:
        ...

    @display_rate_time_scale.setter
    def display_rate_time_scale(self, value: datetime.timedelta) -> None:
        ...

    def __init__(self, name: str, event_source: System.Diagnostics.Tracing.EventSource) -> None:
        """
        Initializes a new instance of the IncrementingEventCounter class.
        IncrementingEventCounter live as long as the EventSource that they are attached to unless they are
        explicitly Disposed.
        
        :param name: The name.
        :param event_source: The event source.
        """
        ...

    def increment(self, increment: float = 1) -> None:
        """
        Writes 'value' to the stream of values tracked by the counter.  This updates the sum and other statistics that will
        be logged on the next timer interval.
        
        :param increment: The value to increment by.
        """
        ...

    def to_string(self) -> str:
        ...


class PollingCounter(System.Diagnostics.Tracing.DiagnosticCounter):
    """
    PollingCounter is a variant of EventCounter - it collects and calculates similar statistics
    as EventCounter. PollingCounter differs from EventCounter in that it takes in a callback
    function to collect metrics on its own rather than the user having to call WriteMetric()
    every time.
    """

    def __init__(self, name: str, event_source: System.Diagnostics.Tracing.EventSource, metric_provider: typing.Callable[[], float]) -> None:
        """
        Initializes a new instance of the PollingCounter class.
        PollingCounter live as long as the EventSource that they are attached to unless they are
        explicitly Disposed.
        
        :param name: The name.
        :param event_source: The event source.
        :param metric_provider: The delegate to invoke to get the current metric value.
        """
        ...

    def to_string(self) -> str:
        ...


class IncrementingPollingCounter(System.Diagnostics.Tracing.DiagnosticCounter):
    """
    IncrementingPollingCounter is a variant of EventCounter for variables that are ever-increasing.
    Ex) # of exceptions in the runtime.
    It does not calculate statistics like mean, standard deviation, etc. because it only accumulates
    the counter value.
    Unlike IncrementingEventCounter, this takes in a polling callback that it can call to update
    its own metric periodically.
    """

    @property
    def display_rate_time_scale(self) -> datetime.timedelta:
        ...

    @display_rate_time_scale.setter
    def display_rate_time_scale(self, value: datetime.timedelta) -> None:
        ...

    def __init__(self, name: str, event_source: System.Diagnostics.Tracing.EventSource, total_value_provider: typing.Callable[[], float]) -> None:
        """
        Initializes a new instance of the IncrementingPollingCounter class.
        IncrementingPollingCounter live as long as the EventSource that they are attached to unless they are
        explicitly Disposed.
        
        :param name: The name.
        :param event_source: The event source.
        :param total_value_provider: The delegate to invoke to get the total value for this counter.
        """
        ...

    def to_string(self) -> str:
        ...


class EventIgnoreAttribute(System.Attribute):
    """
    Used when authoring types that will be passed to EventSource.Write.
    By default, EventSource.Write will write all of an object's public
    properties to the event payload. Apply [EventIgnore] to a public
    property to prevent EventSource.Write from including the property in
    the event.
    """


class EventFieldTags(Enum):
    """
    Tags are flags that are not interpreted by EventSource but are passed along
    to the EventListener. The EventListener determines the semantics of the flags.
    """

    NONE = 0
    """No special traits are added to the field."""


class EventFieldFormat(Enum):
    """
    Provides a hint that may be used by an event listener when formatting
    an event field for display. Note that the event listener may ignore the
    hint if it does not recognize a particular combination of type and format.
    Similar to TDH_OUTTYPE.
    """

    DEFAULT = 0
    """Field receives default formatting based on the field's underlying type."""

    STRING = 2

    BOOLEAN = 3
    """
    Field should be formatted as boolean data. Typically applied to 8-bit
    or 32-bit integers. This is the default format for the Boolean type.
    """

    HEXADECIMAL = 4
    """
    Field should be formatted as hexadecimal data. Typically applied to
    integer types.
    """

    XML = 11
    """
    Field should be formatted as an Internet Protocol v6 address. Typically applied to
    byte[] types.
    """

    JSON = 12
    """
    Field should be formatted as JSON string data. Typically applied to
    strings or arrays of 8-bit or 16-bit integers.
    """

    H_RESULT = 15
    """
    Field should be formatted as an NTSTATUS code. Typically applied to
    32-bit integer types.
    """


class EventFieldAttribute(System.Attribute):
    """
    TraceLogging: used when authoring types that will be passed to EventSource.Write.
    Controls how a field or property is handled when it is written as a
    field in a TraceLogging event. Apply this attribute to a field or
    property if the default handling is not correct. (Apply the
    TraceLoggingIgnore attribute if the property should not be
    included as a field in the event.)
    The default for Name is null, which means that the name of the
    underlying field or property will be used as the event field's name.
    The default for PiiTag is 0, which means that the event field does not
    contain personally-identifiable information.
    """

    @property
    def tags(self) -> System.Diagnostics.Tracing.EventFieldTags:
        """
        User defined options for the field. These are not interpreted by the EventSource
        but are available to the Listener. See EventFieldSettings for details
        """
        ...

    @tags.setter
    def tags(self, value: System.Diagnostics.Tracing.EventFieldTags) -> None:
        ...

    @property
    def format(self) -> System.Diagnostics.Tracing.EventFieldFormat:
        """Gets or sets a field formatting hint."""
        ...

    @format.setter
    def format(self, value: System.Diagnostics.Tracing.EventFieldFormat) -> None:
        ...


class EventDataAttribute(System.Attribute):
    """
    Used when authoring types that will be passed to EventSource.Write.
    EventSource.Write<T> only works when T is either an anonymous type
    or a type with an [EventData] attribute. In addition, the properties
    of T must be supported property types. Supported property types include
    simple built-in types (int, string, Guid, DateTime, DateTimeOffset,
    KeyValuePair, etc.), anonymous types that only contain supported types,
    types with an [EventData] attribute, arrays of the above, and IEnumerable
    of the above.
    """

    @property
    def name(self) -> str:
        """
        Gets or sets the name to use if this type is used for an
        implicitly-named event or an implicitly-named property.
        
        Example 1:
        
            EventSource.Write(null, new T()); // implicitly-named event
        
        The name of the event will be determined as follows:
        
        if (T has an EventData attribute and attribute.Name != null)
            eventName = attribute.Name;
        else
            eventName = typeof(T).Name;
        
        Example 2:
        
            EventSource.Write(name, new { _1 = new T() }); // implicitly-named field
        
        The name of the field will be determined as follows:
        
        if (T has an EventData attribute and attribute.Name != null)
            fieldName = attribute.Name;
        else
            fieldName = typeof(T).Name;
        """
        ...

    @name.setter
    def name(self, value: str) -> None:
        ...


class _EventContainer(typing.Generic[System_Diagnostics_Tracing__EventContainer_Callable, System_Diagnostics_Tracing__EventContainer_ReturnType]):
    """This class is used to provide accurate autocomplete on events and cannot be imported."""

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> System_Diagnostics_Tracing__EventContainer_ReturnType:
        """Fires the event."""
        ...

    def __iadd__(self, item: System_Diagnostics_Tracing__EventContainer_Callable) -> typing.Self:
        """Registers an event handler."""
        ...

    def __isub__(self, item: System_Diagnostics_Tracing__EventContainer_Callable) -> typing.Self:
        """Unregisters an event handler."""
        ...


