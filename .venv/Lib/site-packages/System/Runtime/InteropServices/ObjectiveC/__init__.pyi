from typing import overload
from enum import Enum
import typing

import System
import System.Runtime.InteropServices
import System.Runtime.InteropServices.ObjectiveC


class ObjectiveCMarshal(System.Object):
    """API to enable Objective-C marshalling."""

    class MessageSendFunction(Enum):
        """Objective-C msgSend function override options."""

        MSG_SEND = 0
        """Overrides the Objective-C runtime's https://developer.apple.com/documentation/objectivec/1456712-objc_msgsend."""

        MSG_SEND_FPRET = 1
        """Overrides the Objective-C runtime's https://developer.apple.com/documentation/objectivec/1456697-objc_msgsend_fpret."""

        MSG_SEND_STRET = 2
        """Overrides the Objective-C runtime's https://developer.apple.com/documentation/objectivec/1456730-objc_msgsend_stret."""

        MSG_SEND_SUPER = 3
        """Overrides the Objective-C runtime's https://developer.apple.com/documentation/objectivec/1456716-objc_msgsendsuper."""

        MSG_SEND_SUPER_STRET = 4
        """Overrides the Objective-C runtime's https://developer.apple.com/documentation/objectivec/1456722-objc_msgsendsuper_stret."""

        MSG_SEND = 5
        """Overrides the Objective-C runtime's https://developer.apple.com/documentation/objectivec/1456712-objc_msgsend."""

        MSG_SEND_FPRET = 6
        """Overrides the Objective-C runtime's https://developer.apple.com/documentation/objectivec/1456697-objc_msgsend_fpret."""

        MSG_SEND_STRET = 7
        """Overrides the Objective-C runtime's https://developer.apple.com/documentation/objectivec/1456730-objc_msgsend_stret."""

        MSG_SEND_SUPER = 8
        """Overrides the Objective-C runtime's https://developer.apple.com/documentation/objectivec/1456716-objc_msgsendsuper."""

        MSG_SEND_SUPER_STRET = 9
        """Overrides the Objective-C runtime's https://developer.apple.com/documentation/objectivec/1456722-objc_msgsendsuper_stret."""

    @staticmethod
    def create_reference_tracking_handle(obj: typing.Any, tagged_memory: typing.Optional[System.Span[System.IntPtr]]) -> typing.Tuple[System.Runtime.InteropServices.GCHandle, System.Span[System.IntPtr]]:
        """
        Request native reference tracking for the supplied object.
        
        :param obj: The object to track.
        :param tagged_memory: A pointer to memory tagged to the object.
        :returns: Reference tracking GC handle.
        """
        ...

    @staticmethod
    def initialize(begin_end_callback: typing.Any, is_referenced_callback: typing.Any, tracked_object_entered_finalization: typing.Any, unhandled_exception_propagation_handler: typing.Any) -> None:
        """
        Initialize the Objective-C marshalling API.
        
        :param begin_end_callback: Called when tracking begins and ends.
        :param is_referenced_callback: Called to determine if a managed object instance is referenced elsewhere, and must not be collected by the GC.
        :param tracked_object_entered_finalization: Called when a tracked object enters the finalization queue.
        :param unhandled_exception_propagation_handler: Handler for the propagation of unhandled Exceptions across a managed -> native boundary (that is, Reverse P/Invoke).
        """
        ...

    @staticmethod
    def set_message_send_callback(msg_send_function: typing.Any, func: System.IntPtr) -> None:
        """
        Set a function pointer override for an Objective-C runtime message passing export.
        
        :param msg_send_function: The export to override.
        :param func: The function override.
        """
        ...

    @staticmethod
    def set_message_send_pending_exception(exception: System.Exception) -> None:
        """
        Sets a pending exception to be thrown the next time the runtime is entered from an Objective-C msgSend P/Invoke.
        
        :param exception: The exception.
        """
        ...

    def unhandled_exception_propagation_handler(self, exception: System.Exception, last_method: System.RuntimeMethodHandle, context: typing.Optional[System.IntPtr]) -> typing.Tuple[typing.Any, System.IntPtr]:
        """
        Handler for unhandled Exceptions crossing the managed -> native boundary (that is, Reverse P/Invoke).
        
        :param exception: Unhandled exception.
        :param last_method: Last managed method.
        :param context: Context provided to the returned function pointer.
        :returns: Exception propagation callback.
        """
        ...


class ObjectiveCTrackedTypeAttribute(System.Attribute):
    """Attribute used to indicate a class represents a tracked Objective-C type."""

    def __init__(self) -> None:
        """Instantiate a ObjectiveCTrackedTypeAttribute instance."""
        ...


