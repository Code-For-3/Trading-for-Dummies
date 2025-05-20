from typing import overload
from enum import Enum
import typing

import System
import System.Runtime.InteropServices
import System.Runtime.InteropServices.Marshalling

System_Runtime_InteropServices_Marshalling_ArrayMarshaller_T = typing.TypeVar("System_Runtime_InteropServices_Marshalling_ArrayMarshaller_T")
System_Runtime_InteropServices_Marshalling_ArrayMarshaller_TUnmanagedElement = typing.TypeVar("System_Runtime_InteropServices_Marshalling_ArrayMarshaller_TUnmanagedElement")
System_Runtime_InteropServices_Marshalling_PointerArrayMarshaller_T = typing.TypeVar("System_Runtime_InteropServices_Marshalling_PointerArrayMarshaller_T")
System_Runtime_InteropServices_Marshalling_PointerArrayMarshaller_TUnmanagedElement = typing.TypeVar("System_Runtime_InteropServices_Marshalling_PointerArrayMarshaller_TUnmanagedElement")
System_Runtime_InteropServices_Marshalling_ReadOnlySpanMarshaller_T = typing.TypeVar("System_Runtime_InteropServices_Marshalling_ReadOnlySpanMarshaller_T")
System_Runtime_InteropServices_Marshalling_ReadOnlySpanMarshaller_TUnmanagedElement = typing.TypeVar("System_Runtime_InteropServices_Marshalling_ReadOnlySpanMarshaller_TUnmanagedElement")
System_Runtime_InteropServices_Marshalling_SafeHandleMarshaller_T = typing.TypeVar("System_Runtime_InteropServices_Marshalling_SafeHandleMarshaller_T")
System_Runtime_InteropServices_Marshalling_SpanMarshaller_T = typing.TypeVar("System_Runtime_InteropServices_Marshalling_SpanMarshaller_T")
System_Runtime_InteropServices_Marshalling_SpanMarshaller_TUnmanagedElement = typing.TypeVar("System_Runtime_InteropServices_Marshalling_SpanMarshaller_TUnmanagedElement")


class Utf8StringMarshaller(System.Object):
    """Marshaller for UTF-8 strings."""

    class ManagedToUnmanagedIn:
        """Custom marshaller to marshal a managed string as a UTF-8 unmanaged string."""

        BUFFER_SIZE: int
        """Gets the requested buffer size for optimized marshalling."""

        def free(self) -> None:
            """Frees any allocated unmanaged memory."""
            ...

        def from_managed(self, managed: str, buffer: System.Span[int]) -> None:
            """
            Initializes the marshaller with a managed string and requested buffer.
            
            :param managed: The managed string with which to initialize the marshaller.
            :param buffer: The request buffer whose size is at least BufferSize.
            """
            ...

        def to_unmanaged(self) -> typing.Any:
            """
            Converts the current managed string to an unmanaged string.
            
            :returns: An unmanaged string.
            """
            ...

    @staticmethod
    def convert_to_managed(unmanaged: typing.Any) -> str:
        """
        Converts an unmanaged string to a managed version.
        
        :param unmanaged: The unmanaged string to convert.
        :returns: A managed string.
        """
        ...

    @staticmethod
    def convert_to_unmanaged(managed: str) -> typing.Any:
        """
        Converts a string to an unmanaged version.
        
        :param managed: The managed string to convert.
        :returns: An unmanaged string.
        """
        ...

    @staticmethod
    def free(unmanaged: typing.Any) -> None:
        """
        Free the memory for a specified unmanaged string.
        
        :param unmanaged: The memory allocated for the unmanaged string.
        """
        ...


class ComVariant(System.IDisposable):
    """A type that represents an OLE VARIANT in managed code."""

    NULL: System.Runtime.InteropServices.Marshalling.ComVariant
    """A ComVariant instance that represents a null value with VarEnum.VT_NULL type."""

    @property
    def var_type(self) -> System.Runtime.InteropServices.VarEnum:
        """The type of the data stored in this ComVariant."""
        ...

    def dispose(self) -> None:
        """Release resources owned by this ComVariant instance."""
        ...


class AnsiStringMarshaller(System.Object):
    """Represents a marshaller for ANSI strings."""

    class ManagedToUnmanagedIn:
        """Custom marshaller to marshal a managed string as a ANSI unmanaged string."""

        BUFFER_SIZE: int
        """Gets the requested buffer size for optimized marshalling."""

        def free(self) -> None:
            """Frees any allocated unmanaged string memory."""
            ...

        def from_managed(self, managed: str, buffer: System.Span[int]) -> None:
            """
            Initializes the marshaller with a managed string and requested buffer.
            
            :param managed: The managed string to initialize the marshaller with.
            :param buffer: A request buffer of at least size BufferSize.
            """
            ...

        def to_unmanaged(self) -> typing.Any:
            """
            Converts the current managed string to an unmanaged string.
            
            :returns: The converted unmanaged string.
            """
            ...

    @staticmethod
    def convert_to_managed(unmanaged: typing.Any) -> str:
        """
        Converts an unmanaged string to a managed version.
        
        :param unmanaged: The unmanaged string to convert.
        :returns: A managed string.
        """
        ...

    @staticmethod
    def convert_to_unmanaged(managed: str) -> typing.Any:
        """
        Converts a string to an unmanaged version.
        
        :param managed: The managed string to convert.
        :returns: An unmanaged string.
        """
        ...

    @staticmethod
    def free(unmanaged: typing.Any) -> None:
        """
        Frees the memory for the unmanaged string.
        
        :param unmanaged: The memory allocated for the unmanaged string.
        """
        ...


class ArrayMarshaller(typing.Generic[System_Runtime_InteropServices_Marshalling_ArrayMarshaller_T, System_Runtime_InteropServices_Marshalling_ArrayMarshaller_TUnmanagedElement], System.Object):
    """Represents a marshaller for arrays."""

    class ManagedToUnmanagedIn:
        """Marshaller for marshalling a array from managed to unmanaged."""

        BUFFER_SIZE: int
        """Gets the requested caller-allocated buffer size."""

        def free(self) -> None:
            """Frees resources."""
            ...

        def from_managed(self, array: typing.List[System_Runtime_InteropServices_Marshalling_ArrayMarshaller_T], buffer: System.Span[System_Runtime_InteropServices_Marshalling_ArrayMarshaller_TUnmanagedElement]) -> None:
            """
            Initializes the ArrayMarshaller{T, TUnmanagedElement}.ManagedToUnmanagedIn marshaller.
            
            :param array: The array to be marshalled.
            :param buffer: The buffer that may be used for marshalling.
            """
            ...

        def get_managed_values_source(self) -> System.ReadOnlySpan[System_Runtime_InteropServices_Marshalling_ArrayMarshaller_T]:
            """
            Returns a span that points to the memory where the managed values of the array are stored.
            
            :returns: A span over managed values of the array.
            """
            ...

        @overload
        def get_pinnable_reference(self) -> typing.Any:
            """
            Returns a reference to the marshalled array.
            
            :returns: A pinnable reference to the unmanaged marshalled array.
            """
            ...

        @staticmethod
        @overload
        def get_pinnable_reference(array: typing.List[System_Runtime_InteropServices_Marshalling_ArrayMarshaller_T]) -> typing.Any:
            """
            Gets a pinnable reference to the managed array.
            
            :param array: The managed array.
            :returns: The reference that can be pinned and directly passed to unmanaged code.
            """
            ...

        def get_unmanaged_values_destination(self) -> System.Span[System_Runtime_InteropServices_Marshalling_ArrayMarshaller_TUnmanagedElement]:
            """
            Returns a span that points to the memory where the unmanaged values of the array should be stored.
            
            :returns: A span where unmanaged values of the array should be stored.
            """
            ...

        def to_unmanaged(self) -> typing.Any:
            """
            Returns the unmanaged value representing the array.
            
            :returns: A pointer to the beginning of the unmanaged value.
            """
            ...

    @staticmethod
    def allocate_container_for_managed_elements(unmanaged: typing.Any, num_elements: int) -> typing.List[System_Runtime_InteropServices_Marshalling_ArrayMarshaller_T]:
        """
        Allocates memory for the managed representation of the array.
        
        :param unmanaged: The unmanaged array.
        :param num_elements: The unmanaged element count.
        :returns: The managed array.
        """
        ...

    @staticmethod
    def allocate_container_for_unmanaged_elements(managed: typing.List[System_Runtime_InteropServices_Marshalling_ArrayMarshaller_T], num_elements: typing.Optional[int]) -> typing.Tuple[typing.Any, int]:
        """
        Allocates memory for the unmanaged representation of the array.
        
        :param managed: The managed array.
        :param num_elements: The unmanaged element count.
        :returns: The unmanaged pointer to the allocated memory.
        """
        ...

    @staticmethod
    def free(unmanaged: typing.Any) -> None:
        """
        Frees memory for the unmanaged array.
        
        :param unmanaged: The unmanaged array.
        """
        ...

    @staticmethod
    def get_managed_values_destination(managed: typing.List[System_Runtime_InteropServices_Marshalling_ArrayMarshaller_T]) -> System.Span[System_Runtime_InteropServices_Marshalling_ArrayMarshaller_T]:
        """
        Gets a destination for the managed elements in the array.
        
        :param managed: The managed array.
        :returns: The Span{T} of managed elements.
        """
        ...

    @staticmethod
    def get_managed_values_source(managed: typing.List[System_Runtime_InteropServices_Marshalling_ArrayMarshaller_T]) -> System.ReadOnlySpan[System_Runtime_InteropServices_Marshalling_ArrayMarshaller_T]:
        """
        Gets a source for the managed elements in the array.
        
        :param managed: The managed array.
        :returns: The ReadOnlySpan{T} containing the managed elements to marshal.
        """
        ...

    @staticmethod
    def get_unmanaged_values_destination(unmanaged: typing.Any, num_elements: int) -> System.Span[System_Runtime_InteropServices_Marshalling_ArrayMarshaller_TUnmanagedElement]:
        """
        Gets a destination for the unmanaged elements in the array.
        
        :param unmanaged: The unmanaged allocation.
        :param num_elements: The unmanaged element count.
        :returns: The Span{TUnmanagedElement} of unmanaged elements.
        """
        ...

    @staticmethod
    def get_unmanaged_values_source(unmanaged_value: typing.Any, num_elements: int) -> System.ReadOnlySpan[System_Runtime_InteropServices_Marshalling_ArrayMarshaller_TUnmanagedElement]:
        """
        Gets a source for the unmanaged elements in the array.
        
        :param unmanaged_value: The unmanaged array.
        :param num_elements: The unmanaged element count.
        :returns: The ReadOnlySpan{TUnmanagedElement} containing the unmanaged elements to marshal.
        """
        ...


class MarshalMode(Enum):
    """Represents the different marshalling modes."""

    DEFAULT = 0
    """
    All modes. A marshaller specified with this mode will be used if there's no specific
    marshaller for a given usage mode.
    """

    MANAGED_TO_UNMANAGED_IN = 1
    """By-value and in parameters in managed-to-unmanaged scenarios, like P/Invoke."""

    MANAGED_TO_UNMANAGED_REF = 2
    """ref parameters in managed-to-unmanaged scenarios, like P/Invoke."""

    MANAGED_TO_UNMANAGED_OUT = 3
    """out parameters in managed-to-unmanaged scenarios, like P/Invoke."""

    UNMANAGED_TO_MANAGED_IN = 4
    """By-value and in parameters in unmanaged-to-managed scenarios, like Reverse P/Invoke."""

    UNMANAGED_TO_MANAGED_REF = 5
    """ref parameters in unmanaged-to-managed scenarios, like Reverse P/Invoke."""

    UNMANAGED_TO_MANAGED_OUT = 6
    """out parameters in unmanaged-to-managed scenarios, like Reverse P/Invoke."""

    ELEMENT_IN = 7
    """Elements of arrays passed with in or by-value in interop scenarios."""

    ELEMENT_REF = 8
    """Elements of arrays passed with ref or passed by-value with both InAttribute and OutAttribute in interop scenarios."""

    ELEMENT_OUT = 9
    """Elements of arrays passed with out or passed by-value with only OutAttribute in interop scenarios."""


class CustomMarshallerAttribute(System.Attribute):
    """Indicates an entry point type for defining a marshaller."""

    class GenericPlaceholder:
        """Placeholder type for a generic parameter."""

    @property
    def managed_type(self) -> typing.Type:
        """Gets the managed type to marshal."""
        ...

    @property
    def marshal_mode(self) -> System.Runtime.InteropServices.Marshalling.MarshalMode:
        """Gets the marshalling mode this attribute applies to."""
        ...

    @property
    def marshaller_type(self) -> typing.Type:
        """Gets the type used for marshalling."""
        ...

    def __init__(self, managed_type: typing.Type, marshal_mode: System.Runtime.InteropServices.Marshalling.MarshalMode, marshaller_type: typing.Type) -> None:
        """
        Initializes a new instance of the CustomMarshallerAttribute class.
        
        :param managed_type: The managed type to marshal.
        :param marshal_mode: The marshalling mode this attribute applies to.
        :param marshaller_type: The type used for marshalling.
        """
        ...


class ContiguousCollectionMarshallerAttribute(System.Attribute):
    """Specifies that this marshaller entry-point type is a contiguous collection marshaller."""


class Utf16StringMarshaller(System.Object):
    """Marshaller for UTF-16 strings."""

    @staticmethod
    def convert_to_managed(unmanaged: typing.Any) -> str:
        """
        Converts an unmanaged string to a managed version.
        
        :param unmanaged: The unmanaged string to convert.
        :returns: A managed string.
        """
        ...

    @staticmethod
    def convert_to_unmanaged(managed: str) -> typing.Any:
        """
        Converts a string to an unmanaged version.
        
        :param managed: The managed string to convert.
        :returns: An unmanaged string.
        """
        ...

    @staticmethod
    def free(unmanaged: typing.Any) -> None:
        """
        Frees the memory for the unmanaged string.
        
        :param unmanaged: The memory allocated for the unmanaged string.
        """
        ...

    @staticmethod
    def get_pinnable_reference(str: str) -> typing.Any:
        """
        Gets a pinnable reference for the specified string.
        
        :param str: The string to get a reference for.
        :returns: A pinnable reference.
        """
        ...


class PointerArrayMarshaller(typing.Generic[System_Runtime_InteropServices_Marshalling_PointerArrayMarshaller_T, System_Runtime_InteropServices_Marshalling_PointerArrayMarshaller_TUnmanagedElement], System.Object):
    """Represents a marshaller for an array of pointers."""

    class ManagedToUnmanagedIn:
        """Represents a marshaller for marshalling an array from managed to unmanaged."""

        BUFFER_SIZE: int
        """Gets the requested caller-allocated buffer size."""

        def free(self) -> None:
            """Frees resources."""
            ...

        def from_managed(self, array: typing.List[typing.Any], buffer: System.Span[System_Runtime_InteropServices_Marshalling_PointerArrayMarshaller_TUnmanagedElement]) -> None:
            """
            Initializes the PointerArrayMarshaller{T, TUnmanagedElement}.ManagedToUnmanagedIn marshaller.
            
            :param array: The array to be marshalled.
            :param buffer: The buffer that may be used for marshalling.
            """
            ...

        def get_managed_values_source(self) -> System.ReadOnlySpan[System.IntPtr]:
            """
            Returns a span that points to the memory where the managed values of the array are stored.
            
            :returns: A span over managed values of the array.
            """
            ...

        @overload
        def get_pinnable_reference(self) -> typing.Any:
            """
            Returns a reference to the marshalled array.
            
            :returns: A pinnable reference to the unmanaged marshalled array.
            """
            ...

        @staticmethod
        @overload
        def get_pinnable_reference(array: typing.List[typing.Any]) -> typing.Any:
            """
            Gets a pinnable reference to the managed array.
            
            :param array: The managed array.
            :returns: The reference that can be pinned and directly passed to unmanaged code.
            """
            ...

        def get_unmanaged_values_destination(self) -> System.Span[System_Runtime_InteropServices_Marshalling_PointerArrayMarshaller_TUnmanagedElement]:
            """
            Returns a span that points to the memory where the unmanaged values of the array should be stored.
            
            :returns: A span where unmanaged values of the array should be stored.
            """
            ...

        def to_unmanaged(self) -> typing.Any:
            """
            Returns the unmanaged value representing the array.
            
            :returns: A pointer to the beginning of the unmanaged value.
            """
            ...

    @staticmethod
    def allocate_container_for_managed_elements(unmanaged: typing.Any, num_elements: int) -> typing.List[typing.Any]:
        """
        Allocates memory for the managed representation of the array.
        
        :param unmanaged: The unmanaged array.
        :param num_elements: The unmanaged element count.
        :returns: The managed array.
        """
        ...

    @staticmethod
    def allocate_container_for_unmanaged_elements(managed: typing.List[typing.Any], num_elements: typing.Optional[int]) -> typing.Tuple[typing.Any, int]:
        """
        Allocates memory for the unmanaged representation of the array.
        
        :param managed: The managed array to marshal.
        :param num_elements: The unmanaged element count.
        :returns: The unmanaged pointer to the allocated memory.
        """
        ...

    @staticmethod
    def free(unmanaged: typing.Any) -> None:
        """
        Frees memory for the unmanaged array.
        
        :param unmanaged: The unmanaged array.
        """
        ...

    @staticmethod
    def get_managed_values_destination(managed: typing.List[typing.Any]) -> System.Span[System.IntPtr]:
        """
        Gets a destination for the managed elements in the array.
        
        :param managed: The managed array to get a destination for.
        :returns: The Span{T} of managed elements.
        """
        ...

    @staticmethod
    def get_managed_values_source(managed: typing.List[typing.Any]) -> System.ReadOnlySpan[System.IntPtr]:
        """
        Gets a source for the managed elements in the array.
        
        :param managed: The managed array to get a source for.
        :returns: The ReadOnlySpan{IntPtr} containing the managed elements to marshal.
        """
        ...

    @staticmethod
    def get_unmanaged_values_destination(unmanaged: typing.Any, num_elements: int) -> System.Span[System_Runtime_InteropServices_Marshalling_PointerArrayMarshaller_TUnmanagedElement]:
        """
        Gets a destination for the unmanaged elements in the array.
        
        :param unmanaged: The unmanaged allocation to get a destination for.
        :param num_elements: The unmanaged element count.
        :returns: The Span{TUnmanagedElement} of unmanaged elements.
        """
        ...

    @staticmethod
    def get_unmanaged_values_source(unmanaged_value: typing.Any, num_elements: int) -> System.ReadOnlySpan[System_Runtime_InteropServices_Marshalling_PointerArrayMarshaller_TUnmanagedElement]:
        """
        Gets a source for the unmanaged elements in the array.
        
        :param unmanaged_value: The unmanaged array to get a source for.
        :param num_elements: The unmanaged element count.
        :returns: The ReadOnlySpan{TUnmanagedElement} containing the unmanaged elements to marshal.
        """
        ...


class MarshalUsingAttribute(System.Attribute):
    """Provides type or size information to a custom marshaller."""

    @property
    def native_type(self) -> typing.Type:
        """Gets the marshaller type used to convert the attributed type from managed to native code. This type must be attributed with CustomMarshallerAttribute."""
        ...

    @property
    def count_element_name(self) -> str:
        """Gets or sets the name of the parameter that will provide the size of the collection when marshalling from unmanaged to managed, or ReturnsCountValue if the return value provides the size."""
        ...

    @count_element_name.setter
    def count_element_name(self, value: str) -> None:
        ...

    @property
    def constant_element_count(self) -> int:
        """Gets or sets the size of the collection when marshalling from unmanaged to managed, if the collection is constant size."""
        ...

    @constant_element_count.setter
    def constant_element_count(self, value: int) -> None:
        ...

    @property
    def element_indirection_depth(self) -> int:
        """Gets or sets the indirection depth this marshalling info is provided for."""
        ...

    @element_indirection_depth.setter
    def element_indirection_depth(self, value: int) -> None:
        ...

    RETURNS_COUNT_VALUE: str = "return-value"
    """Represents the name of the return value for CountElementName."""

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the MarshalUsingAttribute class that provides only size information."""
        ...

    @overload
    def __init__(self, native_type: typing.Type) -> None:
        """
        Initializes a new instance of the MarshalUsingAttribute class that provides a native marshalling type and optionally size information.
        
        :param native_type: The marshaller type used to convert the attributed type from managed to native code. This type must be attributed with CustomMarshallerAttribute.
        """
        ...


class ReadOnlySpanMarshaller(typing.Generic[System_Runtime_InteropServices_Marshalling_ReadOnlySpanMarshaller_T, System_Runtime_InteropServices_Marshalling_ReadOnlySpanMarshaller_TUnmanagedElement], System.Object):
    """
    Supports marshalling a ReadOnlySpan{T} from managed value
    to a contiguous native array of the unmanaged values of the elements.
    """

    class UnmanagedToManagedOut(System.Object):
        """Supports marshalling from managed into unmanaged in a call from unmanaged code to managed code."""

        @staticmethod
        def allocate_container_for_unmanaged_elements(managed: System.ReadOnlySpan[System_Runtime_InteropServices_Marshalling_ReadOnlySpanMarshaller_T], num_elements: typing.Optional[int]) -> typing.Tuple[typing.Any, int]:
            """
            Allocates the space to store the unmanaged elements.
            
            :param managed: The managed span.
            :param num_elements: The number of elements in the span.
            :returns: A pointer to the block of memory for the unmanaged elements.
            """
            ...

        @staticmethod
        def get_managed_values_source(managed: System.ReadOnlySpan[System_Runtime_InteropServices_Marshalling_ReadOnlySpanMarshaller_T]) -> System.ReadOnlySpan[System_Runtime_InteropServices_Marshalling_ReadOnlySpanMarshaller_T]:
            """
            Gets a span of the managed collection elements.
            
            :param managed: The managed collection.
            :returns: A span of the managed collection elements.
            """
            ...

        @staticmethod
        def get_unmanaged_values_destination(unmanaged: typing.Any, num_elements: int) -> System.Span[System_Runtime_InteropServices_Marshalling_ReadOnlySpanMarshaller_TUnmanagedElement]:
            """
            Gets a span of the space where the unmanaged collection elements should be stored.
            
            :param unmanaged: The pointer to the block of memory for the unmanaged elements.
            :param num_elements: The number of elements that will be copied into the memory block.
            :returns: A span over the unmanaged memory that can contain the specified number of elements.
            """
            ...

    class ManagedToUnmanagedIn:
        """Supports marshalling from managed into unmanaged in a call from managed code to unmanaged code."""

        BUFFER_SIZE: int
        """Gets the size of the caller-allocated buffer to allocate."""

        def free(self) -> None:
            """Frees resources."""
            ...

        def from_managed(self, managed: System.ReadOnlySpan[System_Runtime_InteropServices_Marshalling_ReadOnlySpanMarshaller_T], buffer: System.Span[System_Runtime_InteropServices_Marshalling_ReadOnlySpanMarshaller_TUnmanagedElement]) -> None:
            """
            Initializes the ReadOnlySpanMarshaller{T, TUnmanagedElement}.ManagedToUnmanagedIn marshaller.
            
            :param managed: The span to be marshalled.
            :param buffer: The buffer that may be used for marshalling.
            """
            ...

        def get_managed_values_source(self) -> System.ReadOnlySpan[System_Runtime_InteropServices_Marshalling_ReadOnlySpanMarshaller_T]:
            """
            Returns a span that points to the memory where the managed values of the array are stored.
            
            :returns: A span over managed values of the array.
            """
            ...

        @overload
        def get_pinnable_reference(self) -> typing.Any:
            """Returns a reference to the marshalled array."""
            ...

        @staticmethod
        @overload
        def get_pinnable_reference(managed: System.ReadOnlySpan[System_Runtime_InteropServices_Marshalling_ReadOnlySpanMarshaller_T]) -> typing.Any:
            """
            Pins the managed span to a pointer to pass directly to unmanaged code.
            
            :param managed: The managed span.
            :returns: A reference that can be pinned and directly passed to unmanaged code.
            """
            ...

        def get_unmanaged_values_destination(self) -> System.Span[System_Runtime_InteropServices_Marshalling_ReadOnlySpanMarshaller_TUnmanagedElement]:
            """
            Returns a span that points to the memory where the unmanaged values of the array should be stored.
            
            :returns: A span where unmanaged values of the array should be stored.
            """
            ...

        def to_unmanaged(self) -> typing.Any:
            """Returns the unmanaged value representing the array."""
            ...

    class ManagedToUnmanagedOut:
        """Supports marshalling from unmanaged to managed in a call from managed code to unmanaged code. For example, return values and `out` parameters in P/Invoke methods."""

        def free(self) -> None:
            """Frees resources."""
            ...

        def from_unmanaged(self, unmanaged: typing.Any) -> None:
            """
            Initializes the ReadOnlySpanMarshaller{T, TUnmanagedElement}.ManagedToUnmanagedOut marshaller.
            
            :param unmanaged: A pointer to the array to be unmarshalled from native to managed.
            """
            ...

        def get_managed_values_destination(self, num_elements: int) -> System.Span[System_Runtime_InteropServices_Marshalling_ReadOnlySpanMarshaller_T]:
            """
            Returns a span that points to the memory where the managed elements of the array should be stored.
            
            :param num_elements: The number of elements in the array.
            :returns: A span where managed values of the array should be stored.
            """
            ...

        def get_unmanaged_values_source(self, num_elements: int) -> System.ReadOnlySpan[System_Runtime_InteropServices_Marshalling_ReadOnlySpanMarshaller_TUnmanagedElement]:
            """
            Returns a span that points to the memory where the unmanaged elements of the array are stored.
            
            :param num_elements: The number of elements in the array.
            :returns: A span over unmanaged values of the array.
            """
            ...

        def to_managed(self) -> System.ReadOnlySpan[System_Runtime_InteropServices_Marshalling_ReadOnlySpanMarshaller_T]:
            """
            Returns the managed value representing the native array.
            
            :returns: A span over managed values of the array.
            """
            ...


class SafeHandleMarshaller(typing.Generic[System_Runtime_InteropServices_Marshalling_SafeHandleMarshaller_T], System.Object):
    """A marshaller for SafeHandle-derived types that marshals the handle following the lifetime rules for SafeHandles."""

    class ManagedToUnmanagedIn:
        """Custom marshaller to marshal a SafeHandle as its underlying handle value."""

        def free(self) -> None:
            """Release any references keeping the managed handle alive."""
            ...

        def from_managed(self, handle: System_Runtime_InteropServices_Marshalling_SafeHandleMarshaller_T) -> None:
            """
            Initializes the marshaller from a managed handle.
            
            :param handle: The managed handle.
            """
            ...

        def to_unmanaged(self) -> System.IntPtr:
            """
            Get the unmanaged handle.
            
            :returns: The unmanaged handle.
            """
            ...

    class ManagedToUnmanagedRef:
        """Custom marshaller to marshal a SafeHandle as its underlying handle value."""

        def __init__(self) -> None:
            """Create the marshaller in a default state."""
            ...

        def free(self) -> None:
            """Free any resources and reference counts owned by the marshaller."""
            ...

        def from_managed(self, handle: System_Runtime_InteropServices_Marshalling_SafeHandleMarshaller_T) -> None:
            """
            Initialize the marshaller from a managed handle.
            
            :param handle: The managed handle
            """
            ...

        def from_unmanaged(self, value: System.IntPtr) -> None:
            """
            Initialize the marshaller from an unmanaged handle.
            
            :param value: The unmanaged handle.
            """
            ...

        def on_invoked(self) -> None:
            """Notify the marshaller that the native call has been invoked."""
            ...

        def to_managed_finally(self) -> System_Runtime_InteropServices_Marshalling_SafeHandleMarshaller_T:
            """
            Retrieve the managed handle from the marshaller.
            
            :returns: The managed handle.
            """
            ...

        def to_unmanaged(self) -> System.IntPtr:
            """
            Retrieve the unmanaged handle.
            
            :returns: The unmanaged handle.
            """
            ...

    class ManagedToUnmanagedOut:
        """Custom marshaller to marshal a SafeHandle as its underlying handle value."""

        def __init__(self) -> None:
            """Create the marshaller in a default state."""
            ...

        def free(self) -> None:
            """Free any resources and reference counts owned by the marshaller."""
            ...

        def from_unmanaged(self, value: System.IntPtr) -> None:
            """
            Initialize the marshaller from an unmanaged handle.
            
            :param value: The unmanaged handle.
            """
            ...

        def to_managed(self) -> System_Runtime_InteropServices_Marshalling_SafeHandleMarshaller_T:
            """
            Retrieve the managed handle from the marshaller.
            
            :returns: The managed handle.
            """
            ...


class SpanMarshaller(typing.Generic[System_Runtime_InteropServices_Marshalling_SpanMarshaller_T, System_Runtime_InteropServices_Marshalling_SpanMarshaller_TUnmanagedElement], System.Object):
    """
    Supports marshalling a Span{T} from managed value
    to a contiguous native array of the unmanaged values of the elements.
    """

    class ManagedToUnmanagedIn:
        """Supports marshalling from managed into unmanaged in a call from managed code to unmanaged code."""

        BUFFER_SIZE: int

        def free(self) -> None:
            """Frees resources."""
            ...

        def from_managed(self, managed: System.Span[System_Runtime_InteropServices_Marshalling_SpanMarshaller_T], buffer: System.Span[System_Runtime_InteropServices_Marshalling_SpanMarshaller_TUnmanagedElement]) -> None:
            """
            Initializes the SpanMarshaller{T, TUnmanagedElement}.ManagedToUnmanagedIn marshaller.
            
            :param managed: The span to be marshalled.
            :param buffer: The buffer that may be used for marshalling.
            """
            ...

        def get_managed_values_source(self) -> System.ReadOnlySpan[System_Runtime_InteropServices_Marshalling_SpanMarshaller_T]:
            """
            Gets a span that points to the memory where the managed values of the array are stored.
            
            :returns: A span over the managed values of the array.
            """
            ...

        @overload
        def get_pinnable_reference(self) -> typing.Any:
            """Returns a reference to the marshalled array."""
            ...

        @staticmethod
        @overload
        def get_pinnable_reference(managed: System.Span[System_Runtime_InteropServices_Marshalling_SpanMarshaller_T]) -> typing.Any:
            """
            Gets a pinnable reference to the managed span.
            
            :param managed: The managed span.
            :returns: A reference that can be pinned and directly passed to unmanaged code.
            """
            ...

        def get_unmanaged_values_destination(self) -> System.Span[System_Runtime_InteropServices_Marshalling_SpanMarshaller_TUnmanagedElement]:
            """
            Returns a span that points to the memory where the unmanaged values of the array should be stored.
            
            :returns: A span where unmanaged values of the array should be stored.
            """
            ...

        def to_unmanaged(self) -> typing.Any:
            """Returns the unmanaged value representing the array."""
            ...

    @staticmethod
    def allocate_container_for_managed_elements(unmanaged: typing.Any, num_elements: int) -> System.Span[System_Runtime_InteropServices_Marshalling_SpanMarshaller_T]:
        """
        Allocates space to store the managed elements.
        
        :param unmanaged: The unmanaged value.
        :param num_elements: The number of elements in the unmanaged collection.
        :returns: A span over enough memory to contain  elements.
        """
        ...

    @staticmethod
    def allocate_container_for_unmanaged_elements(managed: System.Span[System_Runtime_InteropServices_Marshalling_SpanMarshaller_T], num_elements: typing.Optional[int]) -> typing.Tuple[typing.Any, int]:
        """
        Allocates the space to store the unmanaged elements.
        
        :param managed: The managed span.
        :param num_elements: The number of elements in the span.
        :returns: A pointer to the block of memory for the unmanaged elements.
        """
        ...

    @staticmethod
    def free(unmanaged: typing.Any) -> None:
        """
        Frees the allocated unmanaged memory.
        
        :param unmanaged: A pointer to the allocated unmanaged memory.
        """
        ...

    @staticmethod
    def get_managed_values_destination(managed: System.Span[System_Runtime_InteropServices_Marshalling_SpanMarshaller_T]) -> System.Span[System_Runtime_InteropServices_Marshalling_SpanMarshaller_T]:
        """
        Gets a span of the space where the managed collection elements should be stored.
        
        :param managed: A span over the space to store the managed elements.
        :returns: A span over the managed memory that can contain the specified number of elements.
        """
        ...

    @staticmethod
    def get_managed_values_source(managed: System.Span[System_Runtime_InteropServices_Marshalling_SpanMarshaller_T]) -> System.ReadOnlySpan[System_Runtime_InteropServices_Marshalling_SpanMarshaller_T]:
        """
        Gets a span of the managed collection elements.
        
        :param managed: The managed collection.
        :returns: A span of the managed collection elements.
        """
        ...

    @staticmethod
    def get_unmanaged_values_destination(unmanaged: typing.Any, num_elements: int) -> System.Span[System_Runtime_InteropServices_Marshalling_SpanMarshaller_TUnmanagedElement]:
        """
        Gets a span of the space where the unmanaged collection elements should be stored.
        
        :param unmanaged: The pointer to the block of memory for the unmanaged elements.
        :param num_elements: The number of elements that will be copied into the memory block.
        :returns: A span over the unmanaged memory that can contain the specified number of elements.
        """
        ...

    @staticmethod
    def get_unmanaged_values_source(unmanaged: typing.Any, num_elements: int) -> System.ReadOnlySpan[System_Runtime_InteropServices_Marshalling_SpanMarshaller_TUnmanagedElement]:
        """
        Gets a span of the native collection elements.
        
        :param unmanaged: The unmanaged value.
        :param num_elements: The number of elements in the unmanaged collection.
        :returns: A span over the native collection elements.
        """
        ...


class NativeMarshallingAttribute(System.Attribute):
    """Provides a default custom marshaller type for a given managed type."""

    @property
    def native_type(self) -> typing.Type:
        """Gets the marshaller type used to convert the attributed type from managed to native code. This type must be attributed with CustomMarshallerAttribute."""
        ...

    def __init__(self, native_type: typing.Type) -> None:
        """
        Initializes a new instance of the  NativeMarshallingAttribute class that provides a native marshalling type.
        
        :param native_type: The marshaller type used to convert the attributed type from managed to native code. This type must be attributed with CustomMarshallerAttribute.
        """
        ...


class BStrStringMarshaller(System.Object):
    """Represents a marshaller for BSTR strings."""

    class ManagedToUnmanagedIn:
        """Custom marshaller to marshal a managed string as a ANSI unmanaged string."""

        BUFFER_SIZE: int
        """Gets the requested buffer size for optimized marshalling."""

        def free(self) -> None:
            """Frees any allocated unmanaged string memory."""
            ...

        def from_managed(self, managed: str, buffer: System.Span[int]) -> None:
            """
            Initializes the marshaller with a managed string and requested buffer.
            
            :param managed: The managed string to initialize the marshaller with.
            :param buffer: A request buffer of at least size BufferSize.
            """
            ...

        def to_unmanaged(self) -> typing.Any:
            """
            Converts the current managed string to an unmanaged string.
            
            :returns: The converted unmanaged string.
            """
            ...

    @staticmethod
    def convert_to_managed(unmanaged: typing.Any) -> str:
        """
        Converts an unmanaged string to a managed version.
        
        :param unmanaged: An unmanaged string to convert.
        :returns: The converted managed string.
        """
        ...

    @staticmethod
    def convert_to_unmanaged(managed: str) -> typing.Any:
        """
        Converts a string to an unmanaged version.
        
        :param managed: A managed string to convert.
        :returns: The converted unmanaged string.
        """
        ...

    @staticmethod
    def free(unmanaged: typing.Any) -> None:
        """
        Frees the memory for the unmanaged string.
        
        :param unmanaged: The memory allocated for the unmanaged string.
        """
        ...


