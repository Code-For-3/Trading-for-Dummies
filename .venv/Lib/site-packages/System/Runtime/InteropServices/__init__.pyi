from typing import overload
from enum import Enum
import abc
import typing
import warnings

import Microsoft.Win32.SafeHandles
import System
import System.Collections
import System.Globalization
import System.Numerics
import System.Reflection
import System.Runtime.ConstrainedExecution
import System.Runtime.InteropServices
import System.Runtime.InteropServices.ComTypes
import System.Runtime.Serialization
import System.Security

System_Runtime_InteropServices_GCHandle = typing.Any
System_Runtime_InteropServices_OSPlatform = typing.Any
System_Runtime_InteropServices_CLong = typing.Any
System_Runtime_InteropServices_PinnedGCHandle = typing.Any
System_Runtime_InteropServices_ArrayWithOffset = typing.Any
System_Runtime_InteropServices_CULong = typing.Any
System_Runtime_InteropServices_NFloat = typing.Any
System_Runtime_InteropServices_WeakGCHandle = typing.Any

System_Runtime_InteropServices_GCHandle_T = typing.TypeVar("System_Runtime_InteropServices_GCHandle_T")
System_Runtime_InteropServices_PinnedGCHandle_T = typing.TypeVar("System_Runtime_InteropServices_PinnedGCHandle_T")
System_Runtime_InteropServices_TypeMapAssociationAttribute_TTypeMapGroup = typing.TypeVar("System_Runtime_InteropServices_TypeMapAssociationAttribute_TTypeMapGroup")
System_Runtime_InteropServices_TypeMapAttribute_TTypeMapGroup = typing.TypeVar("System_Runtime_InteropServices_TypeMapAttribute_TTypeMapGroup")
System_Runtime_InteropServices_TypeMapAssemblyTargetAttribute_TTypeMapGroup = typing.TypeVar("System_Runtime_InteropServices_TypeMapAssemblyTargetAttribute_TTypeMapGroup")
System_Runtime_InteropServices_WeakGCHandle_T = typing.TypeVar("System_Runtime_InteropServices_WeakGCHandle_T")


class LayoutKind(Enum):
    """This class has no documentation."""

    SEQUENTIAL = 0

    EXPLICIT = 2

    AUTO = 3


class SafeArrayTypeMismatchException(System.SystemException):
    """
    The exception is thrown when the runtime type of an array is different
    than the safe array sub type specified in the metadata.
    """

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
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """
        This method is protected.
        
        Obsoletions.LegacyFormatterImplMessage
        """
        ...


class PosixSignal(Enum):
    """Specifies a POSIX signal number."""

    SIGHUP = -1
    """Hangup"""

    SIGINT = -2
    """Interrupt"""

    SIGQUIT = -3
    """Quit"""

    SIGTERM = -4
    """Termination"""

    SIGCHLD = -5
    """Child stopped"""

    SIGCONT = -6
    """Continue if stopped"""

    SIGWINCH = -7
    """Window resized"""

    SIGTTIN = -8
    """Terminal input for background process"""

    SIGTTOU = -9
    """Terminal output for background process"""

    SIGTSTP = -10
    """Stop typed at terminal"""


class PosixSignalContext(System.Object):
    """Provides data for a PosixSignalRegistration event."""

    @property
    def signal(self) -> System.Runtime.InteropServices.PosixSignal:
        """Gets the signal that occurred."""
        ...

    @property
    def cancel(self) -> bool:
        """Gets or sets a value that indicates whether to cancel the default handling of the signal. The default is false."""
        ...

    @cancel.setter
    def cancel(self, value: bool) -> None:
        ...

    def __init__(self, signal: System.Runtime.InteropServices.PosixSignal) -> None:
        """Initializes a new instance of the PosixSignalContext class."""
        ...


class PosixSignalRegistration(System.Object, System.IDisposable):
    """Handles a PosixSignal."""

    @staticmethod
    def create(signal: System.Runtime.InteropServices.PosixSignal, handler: typing.Callable[[System.Runtime.InteropServices.PosixSignalContext], None]) -> System.Runtime.InteropServices.PosixSignalRegistration:
        """
        Registers a  that is invoked when the  occurs.
        
        :param signal: The signal to register for.
        :param handler: The handler that gets invoked.
        :returns: A PosixSignalRegistration instance that can be disposed to unregister the handler.
        """
        ...

    def dispose(self) -> None:
        """Unregister the handler."""
        ...


class ICustomFactory(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def create_instance(self, server_type: typing.Type) -> System.MarshalByRefObject:
        ...


class SafeHandle(System.Runtime.ConstrainedExecution.CriticalFinalizerObject, System.IDisposable, metaclass=abc.ABCMeta):
    """Represents a wrapper class for operating system handles."""

    @property
    def handle(self) -> System.IntPtr:
        """This field is protected."""
        ...

    @handle.setter
    def handle(self, value: System.IntPtr) -> None:
        ...

    @property
    def is_closed(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def is_invalid(self) -> bool:
        ...

    def __init__(self, invalid_handle_value: System.IntPtr, owns_handle: bool) -> None:
        """
        Creates a SafeHandle class.
        
        This method is protected.
        """
        ...

    def close(self) -> None:
        ...

    def dangerous_add_ref(self, success: bool) -> None:
        ...

    def dangerous_get_handle(self) -> System.IntPtr:
        ...

    def dangerous_release(self) -> None:
        ...

    @overload
    def dispose(self) -> None:
        ...

    @overload
    def dispose(self, disposing: bool) -> None:
        """This method is protected."""
        ...

    def release_handle(self) -> bool:
        """This method is protected."""
        ...

    def set_handle_as_invalid(self) -> None:
        ...


class CustomQueryInterfaceMode(Enum):
    """This class has no documentation."""

    IGNORE = 0

    ALLOW = 1


class Marshal(System.Object):
    """
    This class contains methods that are mainly used to marshal between unmanaged
    and managed types.
    """

    SYSTEM_DEFAULT_CHAR_SIZE: int = 2
    """
    The default character size for the system. This is always 2 because
    the framework only runs on UTF-16 systems.
    """

    SYSTEM_MAX_DBCS_CHAR_SIZE: int = ...
    """The max DBCS character size for the system."""

    @staticmethod
    def add_ref(p_unk: System.IntPtr) -> int:
        ...

    @staticmethod
    def alloc_co_task_mem(cb: int) -> System.IntPtr:
        ...

    @staticmethod
    @overload
    def alloc_h_global(cb: int) -> System.IntPtr:
        ...

    @staticmethod
    @overload
    def alloc_h_global(cb: System.IntPtr) -> System.IntPtr:
        ...

    @staticmethod
    def are_com_objects_available_for_cleanup() -> bool:
        ...

    @staticmethod
    def bind_to_moniker(moniker_name: str) -> System.Object:
        ...

    @staticmethod
    def change_wrapper_handle_strength(otp: typing.Any, f_is_weak: bool) -> None:
        ...

    @staticmethod
    def cleanup_unused_objects_in_current_context() -> None:
        ...

    @staticmethod
    @overload
    def copy(source: typing.List[int], start_index: int, destination: System.IntPtr, length: int) -> None:
        ...

    @staticmethod
    @overload
    def copy(source: typing.List[str], start_index: int, destination: System.IntPtr, length: int) -> None:
        ...

    @staticmethod
    @overload
    def copy(source: typing.List[float], start_index: int, destination: System.IntPtr, length: int) -> None:
        ...

    @staticmethod
    @overload
    def copy(source: typing.List[System.IntPtr], start_index: int, destination: System.IntPtr, length: int) -> None:
        ...

    @staticmethod
    @overload
    def copy(source: System.IntPtr, destination: typing.List[int], start_index: int, length: int) -> None:
        ...

    @staticmethod
    @overload
    def copy(source: System.IntPtr, destination: typing.List[str], start_index: int, length: int) -> None:
        ...

    @staticmethod
    @overload
    def copy(source: System.IntPtr, destination: typing.List[float], start_index: int, length: int) -> None:
        ...

    @staticmethod
    @overload
    def copy(source: System.IntPtr, destination: typing.List[System.IntPtr], start_index: int, length: int) -> None:
        ...

    @staticmethod
    def create_aggregated_object(p_outer: System.IntPtr, o: typing.Any) -> System.IntPtr:
        ...

    @staticmethod
    def create_wrapper_of_type(o: typing.Any, t: typing.Type) -> System.Object:
        ...

    @staticmethod
    def destroy_structure(ptr: System.IntPtr, structuretype: typing.Type) -> None:
        ...

    @staticmethod
    def final_release_com_object(o: typing.Any) -> int:
        ...

    @staticmethod
    def free_bstr(ptr: System.IntPtr) -> None:
        ...

    @staticmethod
    def free_co_task_mem(ptr: System.IntPtr) -> None:
        ...

    @staticmethod
    def free_h_global(hglobal: System.IntPtr) -> None:
        ...

    @staticmethod
    def generate_guid_for_type(type: typing.Type) -> System.Guid:
        """
        Generates a GUID for the specified type. If the type has a GUID in the
        metadata then it is returned otherwise a stable guid is generated based
        on the fully qualified name of the type.
        """
        ...

    @staticmethod
    def generate_prog_id_for_type(type: typing.Type) -> str:
        """
        This method generates a PROGID for the specified type. If the type has
        a PROGID in the metadata then it is returned otherwise a stable PROGID
        is generated based on the fully qualified name of the type.
        """
        ...

    @staticmethod
    @overload
    def get_com_interface_for_object(o: typing.Any, t: typing.Type) -> System.IntPtr:
        ...

    @staticmethod
    @overload
    def get_com_interface_for_object(o: typing.Any, t: typing.Type, mode: System.Runtime.InteropServices.CustomQueryInterfaceMode) -> System.IntPtr:
        ...

    @staticmethod
    def get_com_object_data(obj: typing.Any, key: typing.Any) -> System.Object:
        ...

    @staticmethod
    def get_delegate_for_function_pointer(ptr: System.IntPtr, t: typing.Type) -> System.Delegate:
        ...

    @staticmethod
    def get_end_com_slot(t: typing.Type) -> int:
        ...

    @staticmethod
    def get_exception_code() -> int:
        """GetExceptionCode() may be unavailable in future releases."""
        warnings.warn("GetExceptionCode() may be unavailable in future releases.", DeprecationWarning)

    @staticmethod
    @overload
    def get_exception_for_hr(error_code: int) -> System.Exception:
        """Converts the HRESULT to a CLR exception."""
        ...

    @staticmethod
    @overload
    def get_exception_for_hr(error_code: int, error_info: System.IntPtr) -> System.Exception:
        ...

    @staticmethod
    def get_exception_pointers() -> System.IntPtr:
        ...

    @staticmethod
    def get_function_pointer_for_delegate(d: System.Delegate) -> System.IntPtr:
        ...

    @staticmethod
    def get_hinstance(m: System.Reflection.Module) -> System.IntPtr:
        ...

    @staticmethod
    def get_hr_for_exception(e: System.Exception) -> int:
        ...

    @staticmethod
    def get_hr_for_last_win_32_error() -> int:
        ...

    @staticmethod
    def get_i_dispatch_for_object(o: typing.Any) -> System.IntPtr:
        ...

    @staticmethod
    def get_i_unknown_for_object(o: typing.Any) -> System.IntPtr:
        ...

    @staticmethod
    def get_last_p_invoke_error() -> int:
        """
        Get the last platform invoke error on the current thread
        
        :returns: The last platform invoke error.
        """
        ...

    @staticmethod
    def get_last_p_invoke_error_message() -> str:
        """
        Gets the system error message for the last PInvoke error code.
        
        :returns: The error message associated with the last PInvoke error code.
        """
        ...

    @staticmethod
    def get_last_system_error() -> int:
        """
        Gets the last system error on the current thread.
        
        :returns: The last system error.
        """
        ...

    @staticmethod
    def get_last_win_32_error() -> int:
        ...

    @staticmethod
    def get_native_variant_for_object(obj: typing.Any, p_dst_native_variant: System.IntPtr) -> None:
        ...

    @staticmethod
    def get_object_for_i_unknown(p_unk: System.IntPtr) -> System.Object:
        ...

    @staticmethod
    def get_object_for_native_variant(p_src_native_variant: System.IntPtr) -> System.Object:
        ...

    @staticmethod
    def get_objects_for_native_variants(a_src_native_variant: System.IntPtr, c_vars: int) -> typing.List[System.Object]:
        ...

    @staticmethod
    def get_p_invoke_error_message(error: int) -> str:
        """
        Gets the system error message for the supplied error code.
        
        :param error: The error code.
        :returns: The error message associated with .
        """
        ...

    @staticmethod
    def get_start_com_slot(t: typing.Type) -> int:
        ...

    @staticmethod
    def get_typed_object_for_i_unknown(p_unk: System.IntPtr, t: typing.Type) -> System.Object:
        ...

    @staticmethod
    def get_type_from_clsid(clsid: System.Guid) -> typing.Type:
        ...

    @staticmethod
    def get_type_info_name(type_info: System.Runtime.InteropServices.ComTypes.ITypeInfo) -> str:
        ...

    @staticmethod
    def get_unique_object_for_i_unknown(unknown: System.IntPtr) -> System.Object:
        ...

    @staticmethod
    def init_handle(safe_handle: System.Runtime.InteropServices.SafeHandle, handle: System.IntPtr) -> None:
        """
        Initializes the underlying handle of a newly created SafeHandle to the provided value.
        
        :param safe_handle: The SafeHandle instance to update.
        :param handle: The pre-existing handle.
        """
        ...

    @staticmethod
    def is_com_object(o: typing.Any) -> bool:
        ...

    @staticmethod
    def is_type_visible_from_com(t: typing.Type) -> bool:
        ...

    @staticmethod
    def offset_of(t: typing.Type, field_name: str) -> System.IntPtr:
        ...

    @staticmethod
    def prelink(m: System.Reflection.MethodInfo) -> None:
        ...

    @staticmethod
    def prelink_all(c: typing.Type) -> None:
        ...

    @staticmethod
    @overload
    def ptr_to_string_ansi(ptr: System.IntPtr) -> str:
        ...

    @staticmethod
    @overload
    def ptr_to_string_ansi(ptr: System.IntPtr, len: int) -> str:
        ...

    @staticmethod
    @overload
    def ptr_to_string_auto(ptr: System.IntPtr, len: int) -> str:
        ...

    @staticmethod
    @overload
    def ptr_to_string_auto(ptr: System.IntPtr) -> str:
        ...

    @staticmethod
    def ptr_to_string_bstr(ptr: System.IntPtr) -> str:
        ...

    @staticmethod
    @overload
    def ptr_to_string_uni(ptr: System.IntPtr) -> str:
        ...

    @staticmethod
    @overload
    def ptr_to_string_uni(ptr: System.IntPtr, len: int) -> str:
        ...

    @staticmethod
    @overload
    def ptr_to_string_utf_8(ptr: System.IntPtr) -> str:
        ...

    @staticmethod
    @overload
    def ptr_to_string_utf_8(ptr: System.IntPtr, byte_len: int) -> str:
        ...

    @staticmethod
    @overload
    def ptr_to_structure(ptr: System.IntPtr, structure: typing.Any) -> None:
        """Marshals data from a native memory block to a preallocated structure class."""
        ...

    @staticmethod
    @overload
    def ptr_to_structure(ptr: System.IntPtr, structure_type: typing.Type) -> System.Object:
        """
        Creates a new instance of  and marshals data from a
        native memory block to it.
        """
        ...

    @staticmethod
    def query_interface(p_unk: System.IntPtr, iid: System.Guid, ppv: typing.Optional[System.IntPtr]) -> typing.Tuple[int, System.IntPtr]:
        ...

    @staticmethod
    @overload
    def read_byte(ptr: System.IntPtr, ofs: int) -> int:
        ...

    @staticmethod
    @overload
    def read_byte(ptr: System.IntPtr) -> int:
        ...

    @staticmethod
    @overload
    def read_byte(ptr: typing.Any, ofs: int) -> int:
        """ReadByte(Object, Int32) may be unavailable in future releases."""
        ...

    @staticmethod
    @overload
    def read_int_16(ptr: System.IntPtr, ofs: int) -> int:
        ...

    @staticmethod
    @overload
    def read_int_16(ptr: System.IntPtr) -> int:
        ...

    @staticmethod
    @overload
    def read_int_16(ptr: typing.Any, ofs: int) -> int:
        """ReadInt16(Object, Int32) may be unavailable in future releases."""
        ...

    @staticmethod
    @overload
    def read_int_32(ptr: System.IntPtr, ofs: int) -> int:
        ...

    @staticmethod
    @overload
    def read_int_32(ptr: System.IntPtr) -> int:
        ...

    @staticmethod
    @overload
    def read_int_32(ptr: typing.Any, ofs: int) -> int:
        """ReadInt32(Object, Int32) may be unavailable in future releases."""
        ...

    @staticmethod
    @overload
    def read_int_64(ptr: System.IntPtr, ofs: int) -> int:
        ...

    @staticmethod
    @overload
    def read_int_64(ptr: System.IntPtr) -> int:
        ...

    @staticmethod
    @overload
    def read_int_64(ptr: typing.Any, ofs: int) -> int:
        """ReadInt64(Object, Int32) may be unavailable in future releases."""
        ...

    @staticmethod
    @overload
    def read_int_ptr(ptr: System.IntPtr, ofs: int) -> System.IntPtr:
        ...

    @staticmethod
    @overload
    def read_int_ptr(ptr: System.IntPtr) -> System.IntPtr:
        ...

    @staticmethod
    @overload
    def read_int_ptr(ptr: typing.Any, ofs: int) -> System.IntPtr:
        """ReadIntPtr(Object, Int32) may be unavailable in future releases."""
        ...

    @staticmethod
    def re_alloc_co_task_mem(pv: System.IntPtr, cb: int) -> System.IntPtr:
        ...

    @staticmethod
    def re_alloc_h_global(pv: System.IntPtr, cb: System.IntPtr) -> System.IntPtr:
        ...

    @staticmethod
    def release(p_unk: System.IntPtr) -> int:
        ...

    @staticmethod
    def release_com_object(o: typing.Any) -> int:
        ...

    @staticmethod
    def secure_string_to_bstr(s: System.Security.SecureString) -> System.IntPtr:
        ...

    @staticmethod
    def secure_string_to_co_task_mem_ansi(s: System.Security.SecureString) -> System.IntPtr:
        ...

    @staticmethod
    def secure_string_to_co_task_mem_unicode(s: System.Security.SecureString) -> System.IntPtr:
        ...

    @staticmethod
    def secure_string_to_global_alloc_ansi(s: System.Security.SecureString) -> System.IntPtr:
        ...

    @staticmethod
    def secure_string_to_global_alloc_unicode(s: System.Security.SecureString) -> System.IntPtr:
        ...

    @staticmethod
    def set_com_object_data(obj: typing.Any, key: typing.Any, data: typing.Any) -> bool:
        ...

    @staticmethod
    def set_last_p_invoke_error(error: int) -> None:
        """
        Set the last platform invoke error on the current thread
        
        :param error: Error to set
        """
        ...

    @staticmethod
    def set_last_system_error(error: int) -> None:
        """
        Sets the last system error on the current thread.
        
        :param error: The error to set.
        """
        ...

    @staticmethod
    @overload
    def size_of(structure: typing.Any) -> int:
        ...

    @staticmethod
    @overload
    def size_of(t: typing.Type) -> int:
        ...

    @staticmethod
    def string_to_bstr(s: str) -> System.IntPtr:
        ...

    @staticmethod
    def string_to_co_task_mem_ansi(s: str) -> System.IntPtr:
        ...

    @staticmethod
    def string_to_co_task_mem_auto(s: str) -> System.IntPtr:
        ...

    @staticmethod
    def string_to_co_task_mem_uni(s: str) -> System.IntPtr:
        ...

    @staticmethod
    def string_to_co_task_mem_utf_8(s: str) -> System.IntPtr:
        ...

    @staticmethod
    def string_to_h_global_ansi(s: str) -> System.IntPtr:
        ...

    @staticmethod
    def string_to_h_global_auto(s: str) -> System.IntPtr:
        ...

    @staticmethod
    def string_to_h_global_uni(s: str) -> System.IntPtr:
        ...

    @staticmethod
    def structure_to_ptr(structure: typing.Any, ptr: System.IntPtr, f_delete_old: bool) -> None:
        ...

    @staticmethod
    @overload
    def throw_exception_for_hr(error_code: int) -> None:
        """Throws a CLR exception based on the HRESULT."""
        ...

    @staticmethod
    @overload
    def throw_exception_for_hr(error_code: int, error_info: System.IntPtr) -> None:
        ...

    @staticmethod
    def unsafe_addr_of_pinned_array_element(arr: System.Array, index: int) -> System.IntPtr:
        """
        IMPORTANT NOTICE: This method does not do any verification on the array.
        It must be used with EXTREME CAUTION since passing in invalid index or
        an array that is not pinned can cause unexpected results.
        """
        ...

    @staticmethod
    @overload
    def write_byte(ptr: System.IntPtr, ofs: int, val: int) -> None:
        ...

    @staticmethod
    @overload
    def write_byte(ptr: System.IntPtr, val: int) -> None:
        ...

    @staticmethod
    @overload
    def write_byte(ptr: typing.Any, ofs: int, val: int) -> None:
        """WriteByte(Object, Int32, Byte) may be unavailable in future releases."""
        ...

    @staticmethod
    @overload
    def write_int_16(ptr: System.IntPtr, ofs: int, val: int) -> None:
        ...

    @staticmethod
    @overload
    def write_int_16(ptr: System.IntPtr, val: int) -> None:
        ...

    @staticmethod
    @overload
    def write_int_16(ptr: System.IntPtr, ofs: int, val: str) -> None:
        ...

    @staticmethod
    @overload
    def write_int_16(ptr: System.IntPtr, val: str) -> None:
        ...

    @staticmethod
    @overload
    def write_int_16(ptr: typing.Any, ofs: int, val: str) -> None:
        """WriteInt16(Object, Int32, Char) may be unavailable in future releases."""
        ...

    @staticmethod
    @overload
    def write_int_16(ptr: typing.Any, ofs: int, val: int) -> None:
        """WriteInt16(Object, Int32, Int16) may be unavailable in future releases."""
        ...

    @staticmethod
    @overload
    def write_int_32(ptr: System.IntPtr, ofs: int, val: int) -> None:
        ...

    @staticmethod
    @overload
    def write_int_32(ptr: System.IntPtr, val: int) -> None:
        ...

    @staticmethod
    @overload
    def write_int_32(ptr: typing.Any, ofs: int, val: int) -> None:
        """WriteInt32(Object, Int32, Int32) may be unavailable in future releases."""
        ...

    @staticmethod
    @overload
    def write_int_64(ptr: System.IntPtr, ofs: int, val: int) -> None:
        ...

    @staticmethod
    @overload
    def write_int_64(ptr: System.IntPtr, val: int) -> None:
        ...

    @staticmethod
    @overload
    def write_int_64(ptr: typing.Any, ofs: int, val: int) -> None:
        """WriteInt64(Object, Int32, Int64) may be unavailable in future releases."""
        ...

    @staticmethod
    @overload
    def write_int_ptr(ptr: System.IntPtr, ofs: int, val: System.IntPtr) -> None:
        ...

    @staticmethod
    @overload
    def write_int_ptr(ptr: System.IntPtr, val: System.IntPtr) -> None:
        ...

    @staticmethod
    @overload
    def write_int_ptr(ptr: typing.Any, ofs: int, val: System.IntPtr) -> None:
        """WriteIntPtr(Object, Int32, IntPtr) may be unavailable in future releases."""
        ...

    @staticmethod
    def zero_free_bstr(s: System.IntPtr) -> None:
        ...

    @staticmethod
    def zero_free_co_task_mem_ansi(s: System.IntPtr) -> None:
        ...

    @staticmethod
    def zero_free_co_task_mem_unicode(s: System.IntPtr) -> None:
        ...

    @staticmethod
    def zero_free_co_task_mem_utf_8(s: System.IntPtr) -> None:
        ...

    @staticmethod
    def zero_free_global_alloc_ansi(s: System.IntPtr) -> None:
        ...

    @staticmethod
    def zero_free_global_alloc_unicode(s: System.IntPtr) -> None:
        ...


class InAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class NativeMemory(System.Object):
    """This class contains methods that are mainly used to manage native memory."""

    @staticmethod
    def aligned_alloc(byte_count: System.UIntPtr, alignment: System.UIntPtr) -> typing.Any:
        """
        Allocates an aligned block of memory of the specified size and alignment, in bytes.
        
        :param byte_count: The size, in bytes, of the block to allocate.
        :param alignment: The alignment, in bytes, of the block to allocate. This must be a power of 2.
        :returns: A pointer to the allocated aligned block of memory.
        """
        ...

    @staticmethod
    def aligned_free(ptr: typing.Any) -> None:
        """
        Frees an aligned block of memory.
        
        :param ptr: A pointer to the aligned block of memory that should be freed.
        """
        ...

    @staticmethod
    def aligned_realloc(ptr: typing.Any, byte_count: System.UIntPtr, alignment: System.UIntPtr) -> typing.Any:
        """
        Reallocates an aligned block of memory of the specified size and alignment, in bytes.
        
        :param ptr: The previously allocated block of memory.
        :param byte_count: The size, in bytes, of the block to allocate.
        :param alignment: The alignment, in bytes, of the block to allocate. This must be a power of 2.
        :returns: A pointer to the reallocated aligned block of memory.
        """
        ...

    @staticmethod
    @overload
    def alloc(byte_count: System.UIntPtr) -> typing.Any:
        """
        Allocates a block of memory of the specified size, in bytes.
        
        :param byte_count: The size, in bytes, of the block to allocate.
        :returns: A pointer to the allocated block of memory.
        """
        ...

    @staticmethod
    @overload
    def alloc(element_count: System.UIntPtr, element_size: System.UIntPtr) -> typing.Any:
        """
        Allocates a block of memory of the specified size, in elements.
        
        :param element_count: The count, in elements, of the block to allocate.
        :param element_size: The size, in bytes, of each element in the allocation.
        :returns: A pointer to the allocated block of memory.
        """
        ...

    @staticmethod
    @overload
    def alloc_zeroed(element_count: System.UIntPtr, element_size: System.UIntPtr) -> typing.Any:
        """
        Allocates and zeroes a block of memory of the specified size, in elements.
        
        :param element_count: The count, in elements, of the block to allocate.
        :param element_size: The size, in bytes, of each element in the allocation.
        :returns: A pointer to the allocated and zeroed block of memory.
        """
        ...

    @staticmethod
    @overload
    def alloc_zeroed(byte_count: System.UIntPtr) -> typing.Any:
        """
        Allocates and zeroes a block of memory of the specified size, in bytes.
        
        :param byte_count: The size, in bytes, of the block to allocate.
        :returns: A pointer to the allocated and zeroed block of memory.
        """
        ...

    @staticmethod
    def clear(ptr: typing.Any, byte_count: System.UIntPtr) -> None:
        """
        Clears a block of memory.
        
        :param ptr: A pointer to the block of memory that should be cleared.
        :param byte_count: The size, in bytes, of the block to clear.
        """
        ...

    @staticmethod
    def copy(source: typing.Any, destination: typing.Any, byte_count: System.UIntPtr) -> None:
        """
        Copies a block of memory from memory location 
        to memory location .
        
        :param source: A pointer to the source of data to be copied.
        :param destination: A pointer to the destination memory block where the data is to be copied.
        :param byte_count: The size, in bytes, to be copied from the source location to the destination.
        """
        ...

    @staticmethod
    def fill(ptr: typing.Any, byte_count: System.UIntPtr, value: int) -> None:
        """
        Copies the byte  to the first  bytes
        of the memory located at .
        
        :param ptr: A pointer to the block of memory to fill.
        :param byte_count: The number of bytes to be set to .
        :param value: The value to be set.
        """
        ...

    @staticmethod
    def free(ptr: typing.Any) -> None:
        """
        Frees a block of memory.
        
        :param ptr: A pointer to the block of memory that should be freed.
        """
        ...

    @staticmethod
    def realloc(ptr: typing.Any, byte_count: System.UIntPtr) -> typing.Any:
        """
        Reallocates a block of memory to be the specified size, in bytes.
        
        :param ptr: The previously allocated block of memory.
        :param byte_count: The size, in bytes, of the reallocated block.
        :returns: A pointer to the reallocated block of memory.
        """
        ...


class ComInterfaceType(Enum):
    """This class has no documentation."""

    INTERFACE_IS_DUAL = 0

    INTERFACE_IS_I_UNKNOWN = 1

    INTERFACE_IS_I_DISPATCH = 2

    INTERFACE_IS_I_INSPECTABLE = 3


class GCHandleType(Enum):
    """This class has no documentation."""

    WEAK = 0

    WEAK_TRACK_RESURRECTION = 1

    NORMAL = 2

    PINNED = 3


class GCHandle(typing.Generic[System_Runtime_InteropServices_GCHandle_T], System.IEquatable[System_Runtime_InteropServices_GCHandle], System.IDisposable):
    """
    Represents a strongly-typed GC handle to a managed object.
    A GC handle is used to work with object references in unmanaged code.
    """

    @property
    def is_allocated(self) -> bool:
        """Determine whether this handle has been allocated or not."""
        ...

    @property
    def target(self) -> System_Runtime_InteropServices_GCHandle_T:
        """Gets or sets the object this handle represents."""
        ...

    @target.setter
    def target(self, value: System_Runtime_InteropServices_GCHandle_T) -> None:
        ...

    def __eq__(self, b: System.Runtime.InteropServices.GCHandle) -> bool:
        ...

    def __init__(self, target: System_Runtime_InteropServices_GCHandle_T) -> None:
        """
        Allocates a handle for the specified object.
        
        :param target: The object that uses the GCHandle{T}.
        """
        ...

    def __ne__(self, b: System.Runtime.InteropServices.GCHandle) -> bool:
        ...

    def addr_of_pinned_object(self) -> System.IntPtr:
        """
        Retrieve the address of an object in a Pinned handle.  This throws
        an exception if the handle is any type other than Pinned.
        """
        ...

    @staticmethod
    @overload
    def alloc(value: typing.Any) -> System.Runtime.InteropServices.GCHandle:
        """
        Creates a new GC handle for an object.
        
        :param value: The object that the GC handle is created for.
        :returns: A new GC handle that protects the object.
        """
        ...

    @staticmethod
    @overload
    def alloc(value: typing.Any, type: System.Runtime.InteropServices.GCHandleType) -> System.Runtime.InteropServices.GCHandle:
        """
        Creates a new GC handle for an object.
        
        :param value: The object that the GC handle is created for.
        :param type: The type of GC handle to create.
        :returns: A new GC handle that protects the object.
        """
        ...

    def dispose(self) -> None:
        """Releases this GCHandle{T}."""
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, o: typing.Any) -> bool:
        ...

    @overload
    def equals(self, other: System.Runtime.InteropServices.GCHandle[System_Runtime_InteropServices_GCHandle_T]) -> bool:
        ...

    @overload
    def equals(self, other: System.Runtime.InteropServices.GCHandle) -> bool:
        """
        Indicates whether the current instance is equal to another instance of the same type.
        
        :param other: An instance to compare with this instance.
        :returns: true if the current instance is equal to the other instance; otherwise, false.
        """
        ...

    def free(self) -> None:
        """Frees a GC handle."""
        ...

    @staticmethod
    def from_int_ptr(value: System.IntPtr) -> System.Runtime.InteropServices.GCHandle[System_Runtime_InteropServices_GCHandle_T]:
        """
        Returns a new GCHandle{T} object created from a handle to a managed object.
        
        :param value: An IntPtr handle to a managed object to create a GCHandle{T} object from.
        :returns: A new GCHandle{T} object that corresponds to the value parameter.
        """
        ...

    def get_hash_code(self) -> int:
        """
        Returns the hash code for the current instance.
        
        :returns: A hash code for the current instance.
        """
        ...

    @staticmethod
    @overload
    def to_int_ptr(value: System.Runtime.InteropServices.GCHandle[System_Runtime_InteropServices_GCHandle_T]) -> System.IntPtr:
        """
        Returns the internal integer representation of a GCHandle{T} object.
        
        :param value: A GCHandle{T} object to retrieve an internal integer representation from.
        :returns: An IntPtr object that represents a GCHandle{T} object.
        """
        ...

    @staticmethod
    @overload
    def to_int_ptr(value: System.Runtime.InteropServices.GCHandle) -> System.IntPtr:
        ...


class WasmImportLinkageAttribute(System.Attribute):
    """Specifies that the P/Invoke marked with this attribute should be linked in as a WASM import."""

    def __init__(self) -> None:
        """Instance constructor."""
        ...


class ComMemberType(Enum):
    """This class has no documentation."""

    METHOD = 0

    PROP_GET = 1

    PROP_SET = 2


class DefaultParameterValueAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def value(self) -> System.Object:
        ...

    def __init__(self, value: typing.Any) -> None:
        ...


class IDynamicInterfaceCastable(metaclass=abc.ABCMeta):
    """Interface used to participate in a type cast failure."""

    def get_interface_implementation(self, interface_type: System.RuntimeTypeHandle) -> System.RuntimeTypeHandle:
        """
        Called during interface dispatch when the given interface type cannot be found
        in the class's metadata.
        
        :param interface_type: The interface type.
        :returns: The type that should be used to dispatch for  on the current object.
        """
        ...

    def is_interface_implemented(self, interface_type: System.RuntimeTypeHandle, throw_if_not_implemented: bool) -> bool:
        """
        Called when an implementing class instance is cast to an interface type that
        is not contained in the class's metadata.
        
        :param interface_type: The interface type.
        :param throw_if_not_implemented: Indicates if the function should throw an exception instead of returning false.
        :returns: Whether or not this object can be cast to the given interface.
        """
        ...


class DynamicInterfaceCastableImplementationAttribute(System.Attribute):
    """Attribute required by any type that is returned by IDynamicInterfaceCastable.GetInterfaceImplementation(RuntimeTypeHandle)."""

    def __init__(self) -> None:
        ...


class Architecture(Enum):
    """Indicates the processor architecture."""

    X_86 = 0
    """An Intel-based 32-bit processor architecture."""

    X_64 = 1
    """An Intel-based 64-bit processor architecture."""

    ARM = 2
    """A 32-bit ARM processor architecture."""

    ARM_64 = 3
    """A 64-bit ARM processor architecture."""

    WASM = 4
    """The WebAssembly platform."""

    S_390X = 5
    """A S390x platform architecture."""

    LOONG_ARCH_64 = 6
    """A LoongArch64 processor architecture."""

    ARMV_6 = 7
    """A 32-bit ARMv6 processor architecture."""

    PPC_64_LE = 8
    """A PowerPC 64-bit (little-endian) processor architecture."""

    RISC_V_64 = 9
    """A RiscV 64-bit processor architecture."""


class OSPlatform(System.IEquatable[System_Runtime_InteropServices_OSPlatform]):
    """This class has no documentation."""

    FREE_BSD: System.Runtime.InteropServices.OSPlatform

    LINUX: System.Runtime.InteropServices.OSPlatform

    OSX: System.Runtime.InteropServices.OSPlatform

    WINDOWS: System.Runtime.InteropServices.OSPlatform

    def __eq__(self, right: System.Runtime.InteropServices.OSPlatform) -> bool:
        ...

    def __ne__(self, right: System.Runtime.InteropServices.OSPlatform) -> bool:
        ...

    @staticmethod
    def create(os_platform: str) -> System.Runtime.InteropServices.OSPlatform:
        """Creates a new OSPlatform instance."""
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, other: System.Runtime.InteropServices.OSPlatform) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def to_string(self) -> str:
        ...


class RuntimeInformation(System.Object):
    """This class has no documentation."""

    OS_DESCRIPTION: str

    OS_ARCHITECTURE: System.Runtime.InteropServices.Architecture

    RUNTIME_IDENTIFIER: str
    """Returns an opaque string that identifies the platform on which an app is running."""

    process_architecture: System.Runtime.InteropServices.Architecture

    @staticmethod
    def is_os_platform(os_platform: System.Runtime.InteropServices.OSPlatform) -> bool:
        """Indicates whether the current application is running on the specified platform."""
        ...


class InvalidOleVariantTypeException(System.SystemException):
    """
    Exception thrown when the type of an OLE variant that was passed into the
    runtime is invalid.
    """

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
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """
        This method is protected.
        
        Obsoletions.LegacyFormatterImplMessage
        """
        ...


class ICustomMarshaler(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def clean_up_managed_data(self, managed_obj: typing.Any) -> None:
        ...

    def clean_up_native_data(self, p_native_data: System.IntPtr) -> None:
        ...

    def get_native_data_size(self) -> int:
        ...

    def marshal_managed_to_native(self, managed_obj: typing.Any) -> System.IntPtr:
        ...

    def marshal_native_to_managed(self, p_native_data: System.IntPtr) -> System.Object:
        ...


class UnknownWrapper(System.Object):
    """This class has no documentation."""

    @property
    def wrapped_object(self) -> System.Object:
        ...

    def __init__(self, obj: typing.Any) -> None:
        ...


class CurrencyWrapper(System.Object):
    """CurrencyWrapper and support for marshalling to the VARIANT type may be unavailable in future releases."""

    @property
    def wrapped_object(self) -> float:
        ...

    @overload
    def __init__(self, obj: typing.Any) -> None:
        ...

    @overload
    def __init__(self, obj: float) -> None:
        ...


class CollectionsMarshal(System.Object):
    """An unsafe class that provides a set of methods to access the underlying data representations of collections."""


class ComSourceInterfacesAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def value(self) -> str:
        ...

    @overload
    def __init__(self, source_interfaces: str) -> None:
        ...

    @overload
    def __init__(self, source_interface: typing.Type) -> None:
        ...

    @overload
    def __init__(self, source_interface_1: typing.Type, source_interface_2: typing.Type) -> None:
        ...

    @overload
    def __init__(self, source_interface_1: typing.Type, source_interface_2: typing.Type, source_interface_3: typing.Type) -> None:
        ...

    @overload
    def __init__(self, source_interface_1: typing.Type, source_interface_2: typing.Type, source_interface_3: typing.Type, source_interface_4: typing.Type) -> None:
        ...


class HandleRef:
    """This class has no documentation."""

    @property
    def wrapper(self) -> System.Object:
        ...

    @property
    def handle(self) -> System.IntPtr:
        ...

    def __init__(self, wrapper: typing.Any, handle: System.IntPtr) -> None:
        ...

    @staticmethod
    def to_int_ptr(value: System.Runtime.InteropServices.HandleRef) -> System.IntPtr:
        ...


class CustomQueryInterfaceResult(Enum):
    """This class has no documentation."""

    HANDLED = 0

    NOT_HANDLED = 1

    FAILED = 2


class DllImportSearchPath(Enum):
    """This class has no documentation."""

    USE_DLL_DIRECTORY_FOR_DEPENDENCIES = ...

    APPLICATION_DIRECTORY = ...

    USER_DIRECTORIES = ...

    SYSTEM_32 = ...

    SAFE_DIRECTORIES = ...

    ASSEMBLY_DIRECTORY = ...

    LEGACY_BEHAVIOR = ...


class CLong(System.IEquatable[System_Runtime_InteropServices_CLong]):
    """
    CLong is an immutable value type that represents the long type in C and C++.
    It is meant to be used as an exchange type at the managed/unmanaged boundary to accurately represent
    in managed code unmanaged APIs that use the long type.
    This type has 32-bits of storage on all Windows platforms and 32-bit Unix-based platforms.
    It has 64-bits of storage on 64-bit Unix platforms.
    """

    @property
    def value(self) -> System.IntPtr:
        """The underlying integer value of this instance."""
        ...

    @overload
    def __init__(self, value: int) -> None:
        """
        Constructs an instance from a 32-bit integer.
        
        :param value: The integer value.
        """
        ...

    @overload
    def __init__(self, value: System.IntPtr) -> None:
        """
        Constructs an instance from a native sized integer.
        
        :param value: The integer value.
        """
        ...

    @overload
    def equals(self, o: typing.Any) -> bool:
        """
        Returns a value indicating whether this instance is equal to a specified object.
        
        :param o: An object to compare with this instance.
        :returns: true if  is an instance of CLong and equals the value of this instance; otherwise, false.
        """
        ...

    @overload
    def equals(self, other: System.Runtime.InteropServices.CLong) -> bool:
        """
        Returns a value indicating whether this instance is equal to a specified CLong value.
        
        :param other: A CLong value to compare to this instance.
        :returns: true if  has the same value as this instance; otherwise, false.
        """
        ...

    def get_hash_code(self) -> int:
        """
        Returns the hash code for this instance.
        
        :returns: A 32-bit signed integer hash code.
        """
        ...

    def to_string(self) -> str:
        """
        Converts the numeric value of this instance to its equivalent string representation.
        
        :returns: The string representation of the value of this instance, consisting of a negative sign if the value is negative, and a sequence of digits ranging from 0 to 9 with no leading zeroes.
        """
        ...


class DispatchWrapper(System.Object):
    """This class has no documentation."""

    @property
    def wrapped_object(self) -> System.Object:
        ...

    def __init__(self, obj: typing.Any) -> None:
        ...


class ComDefaultInterfaceAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def value(self) -> typing.Type:
        ...

    def __init__(self, default_interface: typing.Type) -> None:
        ...


class PinnedGCHandle(typing.Generic[System_Runtime_InteropServices_PinnedGCHandle_T], System.IEquatable[System_Runtime_InteropServices_PinnedGCHandle], System.IDisposable):
    """
    Represents a strongly-typed GC handle to a managed object.
    The object is pinned at fixed location in GC heap and allows its
    address to be taken.
    """

    @property
    def is_allocated(self) -> bool:
        """Determine whether this handle has been allocated or not."""
        ...

    @property
    def target(self) -> System_Runtime_InteropServices_PinnedGCHandle_T:
        """Gets or sets the object this handle represents."""
        ...

    @target.setter
    def target(self, value: System_Runtime_InteropServices_PinnedGCHandle_T) -> None:
        ...

    def __init__(self, target: System_Runtime_InteropServices_PinnedGCHandle_T) -> None:
        """
        Allocates a handle for the specified object.
        
        :param target: The object that uses the PinnedGCHandle{T}.
        """
        ...

    def dispose(self) -> None:
        """Releases this PinnedGCHandle{T}."""
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, other: System.Runtime.InteropServices.PinnedGCHandle[System_Runtime_InteropServices_PinnedGCHandle_T]) -> bool:
        ...

    @staticmethod
    def from_int_ptr(value: System.IntPtr) -> System.Runtime.InteropServices.PinnedGCHandle[System_Runtime_InteropServices_PinnedGCHandle_T]:
        """
        Returns a new PinnedGCHandle{T} object created from a handle to a managed object.
        
        :param value: An IntPtr handle to a managed object to create a PinnedGCHandle{T} object from.
        :returns: A new PinnedGCHandle{T} object that corresponds to the value parameter.
        """
        ...

    def get_address_of_object_data(self) -> typing.Any:
        """
        Retrieves the address of object data in a PinnedGCHandle{T}.
        
        :returns: The address of first instance field of the pinned object, or null if the handle doesn't point to any object.
        """
        ...

    def get_hash_code(self) -> int:
        """
        Returns the hash code for the current instance.
        
        :returns: A hash code for the current instance.
        """
        ...

    @staticmethod
    def to_int_ptr(value: System.Runtime.InteropServices.PinnedGCHandle[System_Runtime_InteropServices_PinnedGCHandle_T]) -> System.IntPtr:
        """
        Returns the internal integer representation of a PinnedGCHandle{T} object.
        
        :param value: A PinnedGCHandle{T} object to retrieve an internal integer representation from.
        :returns: An IntPtr object that represents a PinnedGCHandle{T} object.
        """
        ...


class CharSet(Enum):
    """This class has no documentation."""

    NONE = 1

    ANSI = 2

    UNICODE = 3

    AUTO = 4


class CallingConvention(Enum):
    """This class has no documentation."""

    WINAPI = 1

    CDECL = 2

    STD_CALL = 3

    THIS_CALL = 4

    FAST_CALL = 5


class DllImportAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def value(self) -> str:
        ...

    @property
    def entry_point(self) -> str:
        ...

    @entry_point.setter
    def entry_point(self, value: str) -> None:
        ...

    @property
    def char_set(self) -> System.Runtime.InteropServices.CharSet:
        ...

    @char_set.setter
    def char_set(self, value: System.Runtime.InteropServices.CharSet) -> None:
        ...

    @property
    def set_last_error(self) -> bool:
        ...

    @set_last_error.setter
    def set_last_error(self, value: bool) -> None:
        ...

    @property
    def exact_spelling(self) -> bool:
        ...

    @exact_spelling.setter
    def exact_spelling(self, value: bool) -> None:
        ...

    @property
    def calling_convention(self) -> System.Runtime.InteropServices.CallingConvention:
        ...

    @calling_convention.setter
    def calling_convention(self, value: System.Runtime.InteropServices.CallingConvention) -> None:
        ...

    @property
    def best_fit_mapping(self) -> bool:
        ...

    @best_fit_mapping.setter
    def best_fit_mapping(self, value: bool) -> None:
        ...

    @property
    def preserve_sig(self) -> bool:
        ...

    @preserve_sig.setter
    def preserve_sig(self, value: bool) -> None:
        ...

    @property
    def throw_on_unmappable_char(self) -> bool:
        ...

    @throw_on_unmappable_char.setter
    def throw_on_unmappable_char(self, value: bool) -> None:
        ...

    def __init__(self, dll_name: str) -> None:
        ...


class ExternalException(System.SystemException):
    """The base exception type for all COM interop exceptions and structured exception handling (SEH) exceptions."""

    @property
    def error_code(self) -> int:
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
    def __init__(self, message: str, error_code: int) -> None:
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """
        This method is protected.
        
        Obsoletions.LegacyFormatterImplMessage
        """
        ...

    def to_string(self) -> str:
        ...


class SEHException(System.Runtime.InteropServices.ExternalException):
    """Exception for Structured Exception Handler exceptions."""

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
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """
        This method is protected.
        
        Obsoletions.LegacyFormatterImplMessage
        """
        ...

    def can_resume(self) -> bool:
        ...


class StandardOleMarshalObject(System.MarshalByRefObject, System.Runtime.InteropServices.IMarshal):
    """This class has no documentation."""

    def __init__(self) -> None:
        """This method is protected."""
        ...


class ICustomQueryInterface(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def get_interface(self, iid: System.Guid, ppv: typing.Optional[System.IntPtr]) -> typing.Tuple[System.Runtime.InteropServices.CustomQueryInterfaceResult, System.IntPtr]:
        ...


class COMException(System.Runtime.InteropServices.ExternalException):
    """This class has no documentation."""

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
    def __init__(self, message: str, error_code: int) -> None:
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """
        This method is protected.
        
        Obsoletions.LegacyFormatterImplMessage
        """
        ...

    def to_string(self) -> str:
        ...


class CreateComInterfaceFlags(Enum):
    """Enumeration of flags for ComWrappers.GetOrCreateComInterfaceForObject(object, CreateComInterfaceFlags)."""

    NONE = 0

    CALLER_DEFINED_I_UNKNOWN = 1
    """The caller will provide an IUnknown Vtable."""

    TRACKER_SUPPORT = 2
    """
    Flag used to indicate the COM interface should implement https://learn.microsoft.com/windows/win32/api/windows.ui.xaml.hosting.referencetracker/nn-windows-ui-xaml-hosting-referencetracker-ireferencetrackertarget.
    When this flag is passed, the resulting COM interface will have an internal implementation of IUnknown
    and as such none should be supplied by the caller.
    """


class CreateObjectFlags(Enum):
    """Enumeration of flags for ComWrappers.GetOrCreateObjectForComInstance(IntPtr, CreateObjectFlags)."""

    NONE = 0

    TRACKER_OBJECT = 1
    """Indicate if the supplied external COM object implements the https://learn.microsoft.com/windows/win32/api/windows.ui.xaml.hosting.referencetracker/nn-windows-ui-xaml-hosting-referencetracker-ireferencetracker."""

    UNIQUE_INSTANCE = 2
    """Ignore any internal caching and always create a unique instance."""

    AGGREGATION = 4
    """Defined when COM aggregation is involved (that is an inner instance supplied)."""

    UNWRAP = 8
    """
    Check if the supplied instance is actually a wrapper and if so return the underlying
    managed object rather than creating a new wrapper.
    """


class ComWrappers(System.Object, metaclass=abc.ABCMeta):
    """Class for managing wrappers of COM IUnknown types."""

    class ComInterfaceEntry:
        """Interface type and pointer to targeted VTable."""

        @property
        def iid(self) -> System.Guid:
            """Interface IID."""
            ...

        @iid.setter
        def iid(self, value: System.Guid) -> None:
            ...

        @property
        def vtable(self) -> System.IntPtr:
            """Memory must have the same lifetime as the memory returned from the call to ComputeVtables(object, CreateComInterfaceFlags, out int)."""
            ...

        @vtable.setter
        def vtable(self, value: System.IntPtr) -> None:
            ...

    class ComInterfaceDispatch:
        """ABI for function dispatch of a COM interface."""

        @property
        def vtable(self) -> System.IntPtr:
            ...

        @vtable.setter
        def vtable(self, value: System.IntPtr) -> None:
            ...

    def compute_vtables(self, obj: typing.Any, flags: System.Runtime.InteropServices.CreateComInterfaceFlags, count: typing.Optional[int]) -> typing.Tuple[typing.Any, int]:
        """
        Compute the desired Vtable for  respecting the values of .
        
        This method is protected.
        
        :param obj: Target of the returned Vtables.
        :param flags: Flags used to compute Vtables.
        :param count: The number of elements contained in the returned memory.
        :returns: ComInterfaceEntry pointer containing memory for all COM interface entries.
        """
        ...

    def create_object(self, external_com_object: System.IntPtr, flags: System.Runtime.InteropServices.CreateObjectFlags) -> System.Object:
        """
        Create a managed object for the object pointed at by  respecting the values of .
        
        This method is protected.
        
        :param external_com_object: Object to import for usage into the .NET runtime.
        :param flags: Flags used to describe the external object.
        :returns: Returns a managed object associated with the supplied external COM object.
        """
        ...

    @staticmethod
    def get_i_unknown_impl(fp_query_interface: typing.Optional[System.IntPtr], fp_add_ref: typing.Optional[System.IntPtr], fp_release: typing.Optional[System.IntPtr]) -> typing.Tuple[None, System.IntPtr, System.IntPtr, System.IntPtr]:
        ...

    def get_or_create_com_interface_for_object(self, instance: typing.Any, flags: System.Runtime.InteropServices.CreateComInterfaceFlags) -> System.IntPtr:
        ...

    def get_or_create_object_for_com_instance(self, external_com_object: System.IntPtr, flags: System.Runtime.InteropServices.CreateObjectFlags) -> System.Object:
        ...

    @overload
    def get_or_register_object_for_com_instance(self, external_com_object: System.IntPtr, flags: System.Runtime.InteropServices.CreateObjectFlags, wrapper: typing.Any) -> System.Object:
        ...

    @overload
    def get_or_register_object_for_com_instance(self, external_com_object: System.IntPtr, flags: System.Runtime.InteropServices.CreateObjectFlags, wrapper: typing.Any, inner: System.IntPtr) -> System.Object:
        ...

    @staticmethod
    def register_for_marshalling(instance: System.Runtime.InteropServices.ComWrappers) -> None:
        ...

    @staticmethod
    def register_for_tracker_support(instance: System.Runtime.InteropServices.ComWrappers) -> None:
        ...

    def release_objects(self, objects: System.Collections.IEnumerable) -> None:
        """
        Called when a request is made for a collection of objects to be released outside of normal object or COM interface lifetime.
        
        This method is protected.
        
        :param objects: Collection of objects to release.
        """
        ...

    @staticmethod
    def try_get_com_instance(obj: typing.Any, unknown: typing.Optional[System.IntPtr]) -> typing.Tuple[bool, System.IntPtr]:
        ...

    @staticmethod
    def try_get_object(unknown: System.IntPtr, obj: typing.Optional[typing.Any]) -> typing.Tuple[bool, typing.Any]:
        ...


class ErrorWrapper(System.Object):
    """This class has no documentation."""

    @property
    def error_code(self) -> int:
        ...

    @overload
    def __init__(self, error_code: typing.Any) -> None:
        ...

    @overload
    def __init__(self, error_code: int) -> None:
        ...

    @overload
    def __init__(self, e: System.Exception) -> None:
        ...


class ArrayWithOffset(System.IEquatable[System_Runtime_InteropServices_ArrayWithOffset]):
    """This class has no documentation."""

    def __eq__(self, b: System.Runtime.InteropServices.ArrayWithOffset) -> bool:
        ...

    def __init__(self, array: typing.Any, offset: int) -> None:
        ...

    def __ne__(self, b: System.Runtime.InteropServices.ArrayWithOffset) -> bool:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, obj: System.Runtime.InteropServices.ArrayWithOffset) -> bool:
        ...

    def get_array(self) -> System.Object:
        ...

    def get_hash_code(self) -> int:
        ...

    def get_offset(self) -> int:
        ...


class DefaultCharSetAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def char_set(self) -> System.Runtime.InteropServices.CharSet:
        ...

    def __init__(self, char_set: System.Runtime.InteropServices.CharSet) -> None:
        ...


class OutAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class TypeMapAssociationAttribute(typing.Generic[System_Runtime_InteropServices_TypeMapAssociationAttribute_TTypeMapGroup], System.Attribute):
    """Create a type association between a type and its proxy."""

    def __init__(self, source: typing.Type, proxy: typing.Type) -> None:
        """
        Create an association between two types in the type map.
        
        :param source: Target type.
        :param proxy: Type to associated with .
        """
        ...


class UnmanagedFunctionPointerAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def calling_convention(self) -> System.Runtime.InteropServices.CallingConvention:
        ...

    @property
    def best_fit_mapping(self) -> bool:
        ...

    @best_fit_mapping.setter
    def best_fit_mapping(self, value: bool) -> None:
        ...

    @property
    def set_last_error(self) -> bool:
        ...

    @set_last_error.setter
    def set_last_error(self, value: bool) -> None:
        ...

    @property
    def throw_on_unmappable_char(self) -> bool:
        ...

    @throw_on_unmappable_char.setter
    def throw_on_unmappable_char(self, value: bool) -> None:
        ...

    @property
    def char_set(self) -> System.Runtime.InteropServices.CharSet:
        ...

    @char_set.setter
    def char_set(self, value: System.Runtime.InteropServices.CharSet) -> None:
        ...

    def __init__(self, calling_convention: System.Runtime.InteropServices.CallingConvention) -> None:
        ...


class DefaultDllImportSearchPathsAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def paths(self) -> System.Runtime.InteropServices.DllImportSearchPath:
        ...

    def __init__(self, paths: System.Runtime.InteropServices.DllImportSearchPath) -> None:
        ...


class GCHandleExtensions(System.Object):
    """Provides extension methods to operate with GC handles."""

    @staticmethod
    def get_address_of_string_data(handle: System.Runtime.InteropServices.PinnedGCHandle[str]) -> typing.Any:
        """
        Retrieves the address string data in .
        
        :param handle: The handle to retrieve pointer from.
        :returns: The address of 0th character of the pinned string, or null if the handle doesn't point to any object.
        """
        ...


class ComEventInterfaceAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def source_interface(self) -> typing.Type:
        ...

    @property
    def event_provider(self) -> typing.Type:
        ...

    def __init__(self, source_interface: typing.Type, event_provider: typing.Type) -> None:
        ...


class NativeLibrary(System.Object):
    """APIs for managing Native Libraries"""

    @staticmethod
    def free(handle: System.IntPtr) -> None:
        """
        Free a loaded library
        Given a library handle, free it.
        No action if the input handle is null.
        
        :param handle: The native library handle to be freed.
        """
        ...

    @staticmethod
    def get_export(handle: System.IntPtr, name: str) -> System.IntPtr:
        """
        Get the address of an exported Symbol
        This is a simple wrapper around OS calls, and does not perform any name mangling.
        
        :param handle: The native library handle.
        :param name: The name of the exported symbol.
        :returns: The address of the symbol.
        """
        ...

    @staticmethod
    def get_main_program_handle() -> System.IntPtr:
        """
        Get a handle that can be used with GetExport or TryGetExport to resolve exports from the entry point module.
        
        :returns: The handle that can be used to resolve exports from the entry point module.
        """
        ...

    @staticmethod
    @overload
    def load(library_path: str) -> System.IntPtr:
        """
        NativeLibrary Loader: Simple API
        This method is a wrapper around OS loader, using "default" flags.
        
        :param library_path: The name of the native library to be loaded.
        :returns: The handle for the loaded native library.
        """
        ...

    @staticmethod
    @overload
    def load(library_name: str, assembly: System.Reflection.Assembly, search_path: typing.Optional[System.Runtime.InteropServices.DllImportSearchPath]) -> System.IntPtr:
        """
        NativeLibrary Loader: High-level API
        Given a library name, this function searches specific paths based on the
        runtime configuration, input parameters, and attributes of the calling assembly.
        If DllImportSearchPath parameter is non-null, the flags in this enumeration are used.
        Otherwise, the flags specified by the DefaultDllImportSearchPaths attribute on the
        calling assembly (if any) are used.
        This method follows the native library resolution for the AssemblyLoadContext of the
        specified assembly. It will invoke the managed extension points:
        * AssemblyLoadContext.LoadUnmanagedDll()
        * AssemblyLoadContext.ResolvingUnmanagedDllEvent
        It does not invoke extension points that are not tied to the AssemblyLoadContext:
        * The per-assembly registered DllImportResolver callback
        
        :param library_name: The name of the native library to be loaded.
        :param assembly: The assembly loading the native library.
        :param search_path: The search path.
        :returns: The handle for the loaded library.
        """
        ...

    @staticmethod
    def set_dll_import_resolver(assembly: System.Reflection.Assembly, resolver: typing.Callable[[str, System.Reflection.Assembly, typing.Optional[System.Runtime.InteropServices.DllImportSearchPath]], System.IntPtr]) -> None:
        """
        Set a callback for resolving native library imports from an assembly.
        This per-assembly resolver is the first attempt to resolve native library loads
        initiated by this assembly.
        
        Only one resolver can be registered per assembly.
        Trying to register a second resolver fails with InvalidOperationException.
        
        :param assembly: The assembly for which the resolver is registered.
        :param resolver: The resolver callback to register.
        """
        ...

    @staticmethod
    def try_get_export(handle: System.IntPtr, name: str, address: typing.Optional[System.IntPtr]) -> typing.Tuple[bool, System.IntPtr]:
        """
        Get the address of an exported Symbol, but do not throw
        
        :param handle: The  native library handle.
        :param name: The name of the exported symbol.
        :param address: The out-parameter for the symbol address, if it exists.
        :returns: True on success, false otherwise.
        """
        ...

    @staticmethod
    @overload
    def try_load(library_path: str, handle: typing.Optional[System.IntPtr]) -> typing.Tuple[bool, System.IntPtr]:
        """
        NativeLibrary Loader: Simple API that doesn't throw
        
        :param library_path: The name of the native library to be loaded.
        :param handle: The out-parameter for the loaded native library handle.
        :returns: True on successful load, false otherwise.
        """
        ...

    @staticmethod
    @overload
    def try_load(library_name: str, assembly: System.Reflection.Assembly, search_path: typing.Optional[System.Runtime.InteropServices.DllImportSearchPath], handle: typing.Optional[System.IntPtr]) -> typing.Tuple[bool, System.IntPtr]:
        """
        NativeLibrary Loader: High-level API that doesn't throw.
        Given a library name, this function searches specific paths based on the
        runtime configuration, input parameters, and attributes of the calling assembly.
        If DllImportSearchPath parameter is non-null, the flags in this enumeration are used.
        Otherwise, the flags specified by the DefaultDllImportSearchPaths attribute on the
        calling assembly (if any) are used.
        This method follows the native library resolution for the AssemblyLoadContext of the
        specified assembly. It will invoke the managed extension points:
        * AssemblyLoadContext.LoadUnmanagedDll()
        * AssemblyLoadContext.ResolvingUnmanagedDllEvent
        It does not invoke extension points that are not tied to the AssemblyLoadContext:
        * The per-assembly registered DllImportResolver callback
        
        :param library_name: The name of the native library to be loaded.
        :param assembly: The assembly loading the native library.
        :param search_path: The search path.
        :param handle: The out-parameter for the loaded native library handle.
        :returns: True on successful load, false otherwise.
        """
        ...


class UnmanagedType(Enum):
    """This class has no documentation."""

    BOOL = ...

    I_1 = ...

    U_1 = ...

    I_2 = ...

    U_2 = ...

    I_4 = ...

    U_4 = ...

    I_8 = ...

    U_8 = ...

    R_4 = ...

    R_8 = ...

    CURRENCY = ...
    """Marshalling as Currency may be unavailable in future releases."""

    B_STR = ...

    LP_STR = ...

    LPW_STR = ...

    LPT_STR = ...

    BY_VAL_T_STR = ...

    I_UNKNOWN = ...

    I_DISPATCH = ...

    STRUCT = ...

    INTERFACE = ...

    SAFE_ARRAY = ...

    BY_VAL_ARRAY = ...

    SYS_INT = ...

    SYS_U_INT = ...

    VB_BY_REF_STR = ...
    """Marshalling as VBByRefString may be unavailable in future releases."""

    ANSI_B_STR = ...
    """Marshalling as AnsiBStr may be unavailable in future releases."""

    TB_STR = ...
    """Marshalling as TBstr may be unavailable in future releases."""

    VARIANT_BOOL = ...

    FUNCTION_PTR = ...

    AS_ANY = ...
    """Marshalling arbitrary types may be unavailable in future releases. Specify the type you wish to marshal as."""

    LP_ARRAY = ...

    LP_STRUCT = ...

    CUSTOM_MARSHALER = ...

    ERROR = ...

    I_INSPECTABLE = ...

    H_STRING = ...

    LPUTF_8_STR = ...


class VarEnum(Enum):
    """This class has no documentation."""

    VT_EMPTY = 0

    VT_NULL = 1

    VT_I_2 = 2

    VT_I_4 = 3

    VT_R_4 = 4

    VT_R_8 = 5

    VT_CY = 6

    VT_DATE = 7

    VT_BSTR = 8

    VT_DISPATCH = 9

    VT_ERROR = 10

    VT_BOOL = 11

    VT_VARIANT = 12

    VT_UNKNOWN = 13

    VT_DECIMAL = 14

    VT_I_1 = 16

    VT_UI_1 = 17

    VT_UI_2 = 18

    VT_UI_4 = 19

    VT_I_8 = 20

    VT_UI_8 = 21

    VT_INT = 22

    VT_UINT = 23

    VT_VOID = 24

    VT_HRESULT = 25

    VT_PTR = 26

    VT_SAFEARRAY = 27

    VT_CARRAY = 28

    VT_USERDEFINED = 29

    VT_LPSTR = 30

    VT_LPWSTR = 31

    VT_RECORD = 36

    VT_FILETIME = 64

    VT_BLOB = 65

    VT_STREAM = 66

    VT_STORAGE = 67

    VT_STREAMED_OBJECT = 68

    VT_STORED_OBJECT = 69

    VT_BLOB_OBJECT = 70

    VT_CF = 71

    VT_CLSID = 72

    VT_VECTOR = ...

    VT_ARRAY = ...

    VT_BYREF = ...


class MarshalAsAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def value(self) -> System.Runtime.InteropServices.UnmanagedType:
        ...

    @property
    def safe_array_sub_type(self) -> System.Runtime.InteropServices.VarEnum:
        ...

    @safe_array_sub_type.setter
    def safe_array_sub_type(self, value: System.Runtime.InteropServices.VarEnum) -> None:
        ...

    @property
    def safe_array_user_defined_sub_type(self) -> typing.Type:
        ...

    @safe_array_user_defined_sub_type.setter
    def safe_array_user_defined_sub_type(self, value: typing.Type) -> None:
        ...

    @property
    def iid_parameter_index(self) -> int:
        ...

    @iid_parameter_index.setter
    def iid_parameter_index(self, value: int) -> None:
        ...

    @property
    def array_sub_type(self) -> System.Runtime.InteropServices.UnmanagedType:
        ...

    @array_sub_type.setter
    def array_sub_type(self, value: System.Runtime.InteropServices.UnmanagedType) -> None:
        ...

    @property
    def size_param_index(self) -> int:
        ...

    @size_param_index.setter
    def size_param_index(self, value: int) -> None:
        ...

    @property
    def size_const(self) -> int:
        ...

    @size_const.setter
    def size_const(self, value: int) -> None:
        ...

    @property
    def marshal_type(self) -> str:
        ...

    @marshal_type.setter
    def marshal_type(self, value: str) -> None:
        ...

    @property
    def marshal_type_ref(self) -> typing.Type:
        ...

    @marshal_type_ref.setter
    def marshal_type_ref(self, value: typing.Type) -> None:
        ...

    @property
    def marshal_cookie(self) -> str:
        ...

    @marshal_cookie.setter
    def marshal_cookie(self, value: str) -> None:
        ...

    @overload
    def __init__(self, unmanaged_type: System.Runtime.InteropServices.UnmanagedType) -> None:
        ...

    @overload
    def __init__(self, unmanaged_type: int) -> None:
        ...


class CriticalHandle(System.Runtime.ConstrainedExecution.CriticalFinalizerObject, System.IDisposable, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    def handle(self) -> System.IntPtr:
        """This field is protected."""
        ...

    @handle.setter
    def handle(self, value: System.IntPtr) -> None:
        ...

    @property
    def is_closed(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def is_invalid(self) -> bool:
        ...

    def __init__(self, invalid_handle_value: System.IntPtr) -> None:
        """This method is protected."""
        ...

    def close(self) -> None:
        ...

    @overload
    def dispose(self) -> None:
        ...

    @overload
    def dispose(self, disposing: bool) -> None:
        """This method is protected."""
        ...

    def release_handle(self) -> bool:
        """This method is protected."""
        ...

    def set_handle(self, handle: System.IntPtr) -> None:
        """This method is protected."""
        ...

    def set_handle_as_invalid(self) -> None:
        ...


class CULong(System.IEquatable[System_Runtime_InteropServices_CULong]):
    """
    CULong is an immutable value type that represents the unsigned long type in C and C++.
    It is meant to be used as an exchange type at the managed/unmanaged boundary to accurately represent
    in managed code unmanaged APIs that use the unsigned long type.
    This type has 32-bits of storage on all Windows platforms and 32-bit Unix-based platforms.
    It has 64-bits of storage on 64-bit Unix platforms.
    """

    @property
    def value(self) -> System.UIntPtr:
        """The underlying integer value of this instance."""
        ...

    @overload
    def __init__(self, value: int) -> None:
        """
        Constructs an instance from a 32-bit unsigned integer.
        
        :param value: The integer value.
        """
        ...

    @overload
    def __init__(self, value: System.UIntPtr) -> None:
        """
        Constructs an instance from a native sized unsigned integer.
        
        :param value: The integer value.
        """
        ...

    @overload
    def equals(self, o: typing.Any) -> bool:
        """
        Returns a value indicating whether this instance is equal to a specified object.
        
        :param o: An object to compare with this instance.
        :returns: true if  is an instance of CULong and equals the value of this instance; otherwise, false.
        """
        ...

    @overload
    def equals(self, other: System.Runtime.InteropServices.CULong) -> bool:
        """
        Returns a value indicating whether this instance is equal to a specified CLong value.
        
        :param other: A CULong value to compare to this instance.
        :returns: true if  has the same value as this instance; otherwise, false.
        """
        ...

    def get_hash_code(self) -> int:
        """
        Returns the hash code for this instance.
        
        :returns: A 32-bit signed integer hash code.
        """
        ...

    def to_string(self) -> str:
        """
        Converts the numeric value of this instance to its equivalent string representation.
        
        :returns: The string representation of the value of this instance, consisting of a sequence of digits ranging from 0 to 9 with no leading zeroes.
        """
        ...


class ProgIdAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def value(self) -> str:
        ...

    def __init__(self, prog_id: str) -> None:
        ...


class GuidAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def value(self) -> str:
        ...

    def __init__(self, guid: str) -> None:
        ...


class StructLayoutAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def value(self) -> System.Runtime.InteropServices.LayoutKind:
        ...

    @property
    def pack(self) -> int:
        ...

    @pack.setter
    def pack(self, value: int) -> None:
        ...

    @property
    def size(self) -> int:
        ...

    @size.setter
    def size(self, value: int) -> None:
        ...

    @property
    def char_set(self) -> System.Runtime.InteropServices.CharSet:
        ...

    @char_set.setter
    def char_set(self, value: System.Runtime.InteropServices.CharSet) -> None:
        ...

    @overload
    def __init__(self, layout_kind: System.Runtime.InteropServices.LayoutKind) -> None:
        ...

    @overload
    def __init__(self, layout_kind: int) -> None:
        ...


class PreserveSigAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class ComEventsHelper(System.Object):
    """This class has no documentation."""

    @staticmethod
    def combine(rcw: typing.Any, iid: System.Guid, dispid: int, d: System.Delegate) -> None:
        ...

    @staticmethod
    def remove(rcw: typing.Any, iid: System.Guid, dispid: int, d: System.Delegate) -> System.Delegate:
        ...


class ComImportAttribute(System.Attribute):
    """This class has no documentation."""


class ComVisibleAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def value(self) -> bool:
        ...

    def __init__(self, visibility: bool) -> None:
        ...


class DispIdAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def value(self) -> int:
        ...

    def __init__(self, disp_id: int) -> None:
        ...


class LCIDConversionAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def value(self) -> int:
        ...

    def __init__(self, lcid: int) -> None:
        ...


class AllowReversePInvokeCallsAttribute(System.Attribute):
    """Obsoletions.CodeAccessSecurityMessage"""

    def __init__(self) -> None:
        ...


class TypeMapping(System.Object):
    """Entry type for interop type mapping logic."""


class CoClassAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def co_class(self) -> typing.Type:
        ...

    def __init__(self, co_class: typing.Type) -> None:
        ...


class TypeMapAttribute(typing.Generic[System_Runtime_InteropServices_TypeMapAttribute_TTypeMapGroup], System.Attribute):
    """Type mapping between a string and a type."""

    @overload
    def __init__(self, value: str, target: typing.Type) -> None:
        """
        Create a mapping between a value and a System.Type.
        
        :param value: String representation of key
        :param target: Type value
        """
        ...

    @overload
    def __init__(self, value: str, target: typing.Type, trim_target: typing.Type) -> None:
        """
        Create a mapping between a value and a System.Type.
        
        :param value: String representation of key
        :param target: Type value
        :param trim_target: Type used by Trimmer to determine type map inclusion.
        """
        ...


class SafeBuffer(Microsoft.Win32.SafeHandles.SafeHandleZeroOrMinusOneIsInvalid, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    def byte_length(self) -> int:
        """Returns the number of bytes in the memory region."""
        ...

    def __init__(self, owns_handle: bool) -> None:
        """This method is protected."""
        ...

    def acquire_pointer(self, pointer: typing.Any) -> None:
        ...

    @overload
    def initialize(self, num_bytes: int) -> None:
        """
        Specifies the size of the region of memory, in bytes.  Must be
        called before using the SafeBuffer.
        
        :param num_bytes: Number of valid bytes in memory.
        """
        ...

    @overload
    def initialize(self, num_elements: int, size_of_each_element: int) -> None:
        """
        Specifies the size of the region in memory, as the number of
        elements in an array.  Must be called before using the SafeBuffer.
        """
        ...

    def release_pointer(self) -> None:
        ...


class UnmanagedCallersOnlyAttribute(System.Attribute):
    """
    Any method marked with UnmanagedCallersOnlyAttribute can be directly called from
    native code. The function token can be loaded to a local variable using the https://learn.microsoft.com/dotnet/csharp/language-reference/operators/pointer-related-operators#address-of-operator- operator
    in C# and passed as a callback to a native method.
    """

    @property
    def call_convs(self) -> typing.List[typing.Type]:
        """Optional. If omitted, the runtime will use the default platform calling convention."""
        ...

    @call_convs.setter
    def call_convs(self, value: typing.List[typing.Type]) -> None:
        ...

    @property
    def entry_point(self) -> str:
        """Optional. If omitted, no named export is emitted during compilation."""
        ...

    @entry_point.setter
    def entry_point(self, value: str) -> None:
        ...

    def __init__(self) -> None:
        ...


class MarshalDirectiveException(System.SystemException):
    """The exception that is thrown by the marshaler when it encounters a MarshalAsAttribute it does not support."""

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
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """
        This method is protected.
        
        Obsoletions.LegacyFormatterImplMessage
        """
        ...


class OptionalAttribute(System.Attribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...


class TypeMapAssemblyTargetAttribute(typing.Generic[System_Runtime_InteropServices_TypeMapAssemblyTargetAttribute_TTypeMapGroup], System.Attribute):
    """Declare an assembly that should be inspected during type map building."""

    def __init__(self, assembly_name: str) -> None:
        """
        Provide the assembly to look for type mapping attributes.
        
        :param assembly_name: Assembly to reference
        """
        ...


class NFloat(System.Numerics.IBinaryFloatingPointIeee754[System_Runtime_InteropServices_NFloat], System.Numerics.IMinMaxValue[System_Runtime_InteropServices_NFloat], System.IUtf8SpanFormattable):
    """Defines an immutable value type that represents a floating type that has the same size as the native integer size."""

    EPSILON: System.Runtime.InteropServices.NFloat
    """Represents the smallest positive NFloat value that is greater than zero."""

    MAX_VALUE: System.Runtime.InteropServices.NFloat
    """Represents the largest finite value of a NFloat."""

    MIN_VALUE: System.Runtime.InteropServices.NFloat
    """Represents the smallest finite value of a NFloat."""

    NA_N: System.Runtime.InteropServices.NFloat
    """Represents a value that is not a number (NaN)."""

    NEGATIVE_INFINITY: System.Runtime.InteropServices.NFloat
    """Represents negative infinity."""

    POSITIVE_INFINITY: System.Runtime.InteropServices.NFloat
    """Represents positive infinity."""

    SIZE: int
    """Gets the size, in bytes, of an NFloat."""

    @property
    def value(self) -> float:
        """The underlying floating-point value of this instance."""
        ...

    E: System.Runtime.InteropServices.NFloat

    PI: System.Runtime.InteropServices.NFloat

    TAU: System.Runtime.InteropServices.NFloat

    NEGATIVE_ZERO: System.Runtime.InteropServices.NFloat

    @overload
    def __add__(self) -> System.Runtime.InteropServices.NFloat:
        """
        Computes the unary plus of a value.
        
        :param value: The value for which to compute its unary plus.
        :returns: The unary plus of .
        """
        ...

    @overload
    def __add__(self, right: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        """
        Adds two values together to compute their sum.
        
        :param left: The value to which  is added.
        :param right: The value which is added to .
        :returns: The sum of  and .
        """
        ...

    def __eq__(self, right: System.Runtime.InteropServices.NFloat) -> bool:
        """
        Compares two values to determine equality.
        
        :param left: The value to compare with .
        :param right: The value to compare with .
        :returns: true if  is equal to ; otherwise, false.
        """
        ...

    @overload
    def __ge__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __ge__(self, right: System.Runtime.InteropServices.NFloat) -> bool:
        """
        Compares two values to determine which is greater or equal.
        
        :param left: The value to compare with .
        :param right: The value to compare with .
        :returns: true if  is greater than or equal to ; otherwise, false.
        """
        ...

    @overload
    def __ge__(self, other: System.Runtime.InteropServices.NFloat) -> bool:
        ...

    @overload
    def __gt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __gt__(self, right: System.Runtime.InteropServices.NFloat) -> bool:
        """
        Compares two values to determine which is greater.
        
        :param left: The value to compare with .
        :param right: The value to compare with .
        :returns: true if  is greater than ; otherwise, false.
        """
        ...

    @overload
    def __gt__(self, other: System.Runtime.InteropServices.NFloat) -> bool:
        ...

    @overload
    def __iadd__(self) -> System.Runtime.InteropServices.NFloat:
        """
        Computes the unary plus of a value.
        
        :param value: The value for which to compute its unary plus.
        :returns: The unary plus of .
        """
        ...

    @overload
    def __iadd__(self, right: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        """
        Adds two values together to compute their sum.
        
        :param left: The value to which  is added.
        :param right: The value which is added to .
        :returns: The sum of  and .
        """
        ...

    def __imod__(self, right: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        """
        Divides two values together to compute their remainder.
        
        :param left: The value which  divides.
        :param right: The value which divides .
        :returns: The remainder of  divided-by .
        """
        ...

    def __imul__(self, right: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        """
        Multiplies two values together to compute their product.
        
        :param left: The value which  multiplies.
        :param right: The value which multiplies .
        :returns: The product of  multiplied-by .
        """
        ...

    def __init__(self, value: float) -> None:
        """
        Constructs an instance from a 32-bit floating point value.
        
        :param value: The floating-point value.
        """
        ...

    @overload
    def __isub__(self) -> System.Runtime.InteropServices.NFloat:
        """
        Computes the unary negation of a value.
        
        :param value: The value for which to compute its unary negation.
        :returns: The unary negation of .
        """
        ...

    @overload
    def __isub__(self, right: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        """
        Subtracts two values to compute their difference.
        
        :param left: The value from which  is subtracted.
        :param right: The value which is subtracted from .
        :returns: The difference of  subtracted from .
        """
        ...

    def __itruediv__(self, right: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        """
        Divides two values together to compute their quotient.
        
        :param left: The value which  divides.
        :param right: The value which divides .
        :returns: The quotient of  divided-by .
        """
        ...

    @overload
    def __le__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __le__(self, right: System.Runtime.InteropServices.NFloat) -> bool:
        """
        Compares two values to determine which is less or equal.
        
        :param left: The value to compare with .
        :param right: The value to compare with .
        :returns: true if  is less than or equal to ; otherwise, false.
        """
        ...

    @overload
    def __le__(self, other: System.Runtime.InteropServices.NFloat) -> bool:
        ...

    @overload
    def __lt__(self, other: typing.Any) -> bool:
        ...

    @overload
    def __lt__(self, right: System.Runtime.InteropServices.NFloat) -> bool:
        """
        Compares two values to determine which is less.
        
        :param left: The value to compare with .
        :param right: The value to compare with .
        :returns: true if  is less than ; otherwise, false.
        """
        ...

    @overload
    def __lt__(self, other: System.Runtime.InteropServices.NFloat) -> bool:
        ...

    def __mod__(self, right: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        """
        Divides two values together to compute their remainder.
        
        :param left: The value which  divides.
        :param right: The value which divides .
        :returns: The remainder of  divided-by .
        """
        ...

    def __mul__(self, right: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        """
        Multiplies two values together to compute their product.
        
        :param left: The value which  multiplies.
        :param right: The value which multiplies .
        :returns: The product of  multiplied-by .
        """
        ...

    def __ne__(self, right: System.Runtime.InteropServices.NFloat) -> bool:
        """
        Compares two values to determine inequality.
        
        :param left: The value to compare with .
        :param right: The value to compare with .
        :returns: true if  is not equal to ; otherwise, false.
        """
        ...

    @overload
    def __sub__(self) -> System.Runtime.InteropServices.NFloat:
        """
        Computes the unary negation of a value.
        
        :param value: The value for which to compute its unary negation.
        :returns: The unary negation of .
        """
        ...

    @overload
    def __sub__(self, right: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        """
        Subtracts two values to compute their difference.
        
        :param left: The value from which  is subtracted.
        :param right: The value which is subtracted from .
        :returns: The difference of  subtracted from .
        """
        ...

    def __truediv__(self, right: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        """
        Divides two values together to compute their quotient.
        
        :param left: The value which  divides.
        :param right: The value which divides .
        :returns: The quotient of  divided-by .
        """
        ...

    @staticmethod
    def abs(value: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def acos(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def acosh(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def acos_pi(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def asin(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def asinh(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def asin_pi(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def atan(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def atan_2(y: System.Runtime.InteropServices.NFloat, x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def atan_2_pi(y: System.Runtime.InteropServices.NFloat, x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def atanh(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def atan_pi(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def bit_decrement(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def bit_increment(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def cbrt(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def ceiling(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def clamp(value: System.Runtime.InteropServices.NFloat, min: System.Runtime.InteropServices.NFloat, max: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def clamp_native(value: System.Runtime.InteropServices.NFloat, min: System.Runtime.InteropServices.NFloat, max: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @overload
    def compare_to(self, obj: typing.Any) -> int:
        """
        Compares this instance to a specified object and returns an integer that indicates whether the value of this instance is less than, equal to, or greater than the value of the specified object.
        
        :param obj: An object to compare, or null.
        :returns: A signed number indicating the relative values of this instance and .Return ValueDescriptionLess than zeroThis instance is less than , or this instance is not a number and  is a number.ZeroThis instance is equal to , or both this instance and  are not a number.Greater than zeroThis instance is greater than , or this instance is a number and  is not a number or  is null.
        """
        ...

    @overload
    def compare_to(self, other: System.Runtime.InteropServices.NFloat) -> int:
        """
        Compares this instance to a specified floating-point number and returns an integer that indicates whether the value of this instance is less than, equal to, or greater than the value of the specified floating-point number.
        
        :param other: A floating-point number to compare.
        :returns: A signed number indicating the relative values of this instance and .Return ValueDescriptionLess than zeroThis instance is less than , or this instance is not a number and  is a number.ZeroThis instance is equal to , or both this instance and  are not a number.Greater than zeroThis instance is greater than , or this instance is a number and  is not a number.
        """
        ...

    @staticmethod
    def copy_sign(value: System.Runtime.InteropServices.NFloat, sign: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def cos(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def cosh(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def cos_pi(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def degrees_to_radians(degrees: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        """
        Returns a value indicating whether this instance is equal to a specified object.
        
        :param obj: An object to compare with this instance.
        :returns: true if  is an instance of NFloat and equals the value of this instance; otherwise, false.
        """
        ...

    @overload
    def equals(self, other: System.Runtime.InteropServices.NFloat) -> bool:
        """
        Returns a value indicating whether this instance is equal to a specified NFloat value.
        
        :param other: An NFloat value to compare to this instance.
        :returns: true if  has the same value as this instance; otherwise, false.
        """
        ...

    @staticmethod
    def exp(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def exp_10(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def exp_10_m_1(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def exp_2(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def exp_2_m_1(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def exp_m_1(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def floor(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def fused_multiply_add(left: System.Runtime.InteropServices.NFloat, right: System.Runtime.InteropServices.NFloat, addend: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    def get_hash_code(self) -> int:
        """
        Returns the hash code for this instance.
        
        :returns: A 32-bit signed integer hash code.
        """
        ...

    @staticmethod
    def hypot(x: System.Runtime.InteropServices.NFloat, y: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def ieee_754_remainder(left: System.Runtime.InteropServices.NFloat, right: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def i_log_b(x: System.Runtime.InteropServices.NFloat) -> int:
        ...

    @staticmethod
    def is_even_integer(value: System.Runtime.InteropServices.NFloat) -> bool:
        ...

    @staticmethod
    def is_finite(value: System.Runtime.InteropServices.NFloat) -> bool:
        """
        Determines whether the specified value is finite (zero, subnormal, or normal).
        
        :param value: The floating-point value.
        :returns: true if the value is finite (zero, subnormal or normal); false otherwise.
        """
        ...

    @staticmethod
    def is_infinity(value: System.Runtime.InteropServices.NFloat) -> bool:
        """
        Determines whether the specified value is infinite (positive or negative infinity).
        
        :param value: The floating-point value.
        :returns: true if the value is infinite (positive or negative infinity); false otherwise.
        """
        ...

    @staticmethod
    def is_integer(value: System.Runtime.InteropServices.NFloat) -> bool:
        ...

    @staticmethod
    def is_na_n(value: System.Runtime.InteropServices.NFloat) -> bool:
        """
        Determines whether the specified value is NaN (not a number).
        
        :param value: The floating-point value.
        :returns: true if the value is NaN (not a number); false otherwise.
        """
        ...

    @staticmethod
    def is_negative(value: System.Runtime.InteropServices.NFloat) -> bool:
        """
        Determines whether the specified value is negative.
        
        :param value: The floating-point value.
        :returns: true if the value is negative; false otherwise.
        """
        ...

    @staticmethod
    def is_negative_infinity(value: System.Runtime.InteropServices.NFloat) -> bool:
        """
        Determines whether the specified value is negative infinity.
        
        :param value: The floating-point value.
        :returns: true if the value is negative infinity; false otherwise.
        """
        ...

    @staticmethod
    def is_normal(value: System.Runtime.InteropServices.NFloat) -> bool:
        """
        Determines whether the specified value is normal.
        
        :param value: The floating-point value.
        :returns: true if the value is normal; false otherwise.
        """
        ...

    @staticmethod
    def is_odd_integer(value: System.Runtime.InteropServices.NFloat) -> bool:
        ...

    @staticmethod
    def is_positive(value: System.Runtime.InteropServices.NFloat) -> bool:
        ...

    @staticmethod
    def is_positive_infinity(value: System.Runtime.InteropServices.NFloat) -> bool:
        """
        Determines whether the specified value is positive infinity.
        
        :param value: The floating-point value.
        :returns: true if the value is positive infinity; false otherwise.
        """
        ...

    @staticmethod
    def is_pow_2(value: System.Runtime.InteropServices.NFloat) -> bool:
        ...

    @staticmethod
    def is_real_number(value: System.Runtime.InteropServices.NFloat) -> bool:
        ...

    @staticmethod
    def is_subnormal(value: System.Runtime.InteropServices.NFloat) -> bool:
        """
        Determines whether the specified value is subnormal.
        
        :param value: The floating-point value.
        :returns: true if the value is subnormal; false otherwise.
        """
        ...

    @staticmethod
    def lerp(value_1: System.Runtime.InteropServices.NFloat, value_2: System.Runtime.InteropServices.NFloat, amount: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    @overload
    def log(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    @overload
    def log(x: System.Runtime.InteropServices.NFloat, new_base: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def log_10(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def log_10_p_1(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def log_2(value: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def log_2_p_1(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def log_p_1(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def max(x: System.Runtime.InteropServices.NFloat, y: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def max_magnitude(x: System.Runtime.InteropServices.NFloat, y: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def max_magnitude_number(x: System.Runtime.InteropServices.NFloat, y: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def max_native(x: System.Runtime.InteropServices.NFloat, y: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def max_number(x: System.Runtime.InteropServices.NFloat, y: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def min(x: System.Runtime.InteropServices.NFloat, y: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def min_magnitude(x: System.Runtime.InteropServices.NFloat, y: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def min_magnitude_number(x: System.Runtime.InteropServices.NFloat, y: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def min_native(x: System.Runtime.InteropServices.NFloat, y: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def min_number(x: System.Runtime.InteropServices.NFloat, y: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def multiply_add_estimate(left: System.Runtime.InteropServices.NFloat, right: System.Runtime.InteropServices.NFloat, addend: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    @overload
    def parse(s: str) -> System.Runtime.InteropServices.NFloat:
        """
        Converts the string representation of a number to its floating-point number equivalent.
        
        :param s: A string that contains the number to convert.
        :returns: A floating-point number that is equivalent to the numeric value or symbol specified in .
        """
        ...

    @staticmethod
    @overload
    def parse(s: str, style: System.Globalization.NumberStyles) -> System.Runtime.InteropServices.NFloat:
        """
        Converts the string representation of a number in a specified style to its floating-point number equivalent.
        
        :param s: A string that contains the number to convert.
        :param style: A bitwise combination of enumeration values that indicate the style elements that can be present in .
        :returns: A floating-point number that is equivalent to the numeric value or symbol specified in .
        """
        ...

    @staticmethod
    @overload
    def parse(s: str, provider: System.IFormatProvider) -> System.Runtime.InteropServices.NFloat:
        """
        Converts the string representation of a number in a specified culture-specific format to its floating-point number equivalent.
        
        :param s: A string that contains the number to convert.
        :param provider: An object that supplies culture-specific formatting information about .
        :returns: A floating-point number that is equivalent to the numeric value or symbol specified in .
        """
        ...

    @staticmethod
    @overload
    def parse(s: str, style: System.Globalization.NumberStyles, provider: System.IFormatProvider) -> System.Runtime.InteropServices.NFloat:
        """
        Converts the string representation of a number in a specified style and culture-specific format to its floating-point number equivalent.
        
        :param s: A string that contains the number to convert.
        :param style: A bitwise combination of enumeration values that indicate the style elements that can be present in .
        :param provider: An object that supplies culture-specific formatting information about .
        :returns: A floating-point number that is equivalent to the numeric value or symbol specified in .
        """
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> System.Runtime.InteropServices.NFloat:
        """
        Converts a character span that contains the string representation of a number in a specified style and culture-specific format to its floating-point number equivalent.
        
        :param s: A character span that contains the number to convert.
        :param style: A bitwise combination of enumeration values that indicate the style elements that can be present in .
        :param provider: An object that supplies culture-specific formatting information about .
        :returns: A floating-point number that is equivalent to the numeric value or symbol specified in .
        """
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int], style: System.Globalization.NumberStyles = ..., provider: System.IFormatProvider = None) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int], provider: System.IFormatProvider) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def pow(x: System.Runtime.InteropServices.NFloat, y: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def radians_to_degrees(radians: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def reciprocal_estimate(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def reciprocal_sqrt_estimate(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def root_n(x: System.Runtime.InteropServices.NFloat, n: int) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    @overload
    def round(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    @overload
    def round(x: System.Runtime.InteropServices.NFloat, digits: int) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    @overload
    def round(x: System.Runtime.InteropServices.NFloat, mode: System.MidpointRounding) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    @overload
    def round(x: System.Runtime.InteropServices.NFloat, digits: int, mode: System.MidpointRounding) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def scale_b(x: System.Runtime.InteropServices.NFloat, n: int) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def sign(value: System.Runtime.InteropServices.NFloat) -> int:
        ...

    @staticmethod
    def sin(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def sin_cos(x: System.Runtime.InteropServices.NFloat) -> System.ValueTuple[System.Runtime.InteropServices.NFloat, System.Runtime.InteropServices.NFloat]:
        ...

    @staticmethod
    def sin_cos_pi(x: System.Runtime.InteropServices.NFloat) -> System.ValueTuple[System.Runtime.InteropServices.NFloat, System.Runtime.InteropServices.NFloat]:
        ...

    @staticmethod
    def sinh(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def sin_pi(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def sqrt(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def tan(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def tanh(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @staticmethod
    def tan_pi(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @overload
    def to_string(self) -> str:
        """
        Converts the numeric value of this instance to its equivalent string representation.
        
        :returns: The string representation of the value of this instance.
        """
        ...

    @overload
    def to_string(self, format: str) -> str:
        """
        Converts the numeric value of this instance to its equivalent string representation using the specified format.
        
        :param format: A numeric format string.
        :returns: The string representation of the value of this instance as specified by .
        """
        ...

    @overload
    def to_string(self, provider: System.IFormatProvider) -> str:
        """
        Converts the numeric value of this instance to its equivalent string representation using the specified culture-specific format information.
        
        :param provider: An object that supplies culture-specific formatting information.
        :returns: The string representation of the value of this instance as specified by .
        """
        ...

    @overload
    def to_string(self, format: str, provider: System.IFormatProvider) -> str:
        """
        Converts the numeric value of this instance to its equivalent string representation using the specified format and culture-specific format information.
        
        :param format: A numeric format string.
        :param provider: An object that supplies culture-specific formatting information.
        :returns: The string representation of the value of this instance as specified by  and .
        """
        ...

    @staticmethod
    def truncate(x: System.Runtime.InteropServices.NFloat) -> System.Runtime.InteropServices.NFloat:
        ...

    @overload
    def try_format(self, destination: System.Span[str], chars_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        """
        Tries to format the value of the current instance into the provided span of characters.
        
        :param destination: The span in which to write this instance's value formatted as a span of characters.
        :param chars_written: When this method returns, contains the number of characters that were written in .
        :param format: A span containing the characters that represent a standard or custom format string that defines the acceptable format for .
        :param provider: An optional object that supplies culture-specific formatting information for .
        :returns: true if the formatting was successful; otherwise, false.
        """
        ...

    @overload
    def try_format(self, utf_8_destination: System.Span[int], bytes_written: typing.Optional[int], format: System.ReadOnlySpan[str] = ..., provider: System.IFormatProvider = None) -> typing.Tuple[bool, int]:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, result: typing.Optional[System.Runtime.InteropServices.NFloat]) -> typing.Tuple[bool, System.Runtime.InteropServices.NFloat]:
        """
        Tries to convert the string representation of a number to its floating-point number equivalent.
        
        :param s: A read-only character span that contains the number to convert.
        :param result: When this method returns, contains a floating-point number equivalent of the numeric value or symbol contained in  if the conversion succeeded or zero if the conversion failed. The conversion fails if the  is null, string.Empty, or is not in a valid format. This parameter is passed uninitialized; any value originally supplied in result will be overwritten.
        :returns: true if  was converted successfully; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], result: typing.Optional[System.Runtime.InteropServices.NFloat]) -> typing.Tuple[bool, System.Runtime.InteropServices.NFloat]:
        """
        Tries to convert a character span containing the string representation of a number to its floating-point number equivalent.
        
        :param s: A read-only character span that contains the number to convert.
        :param result: When this method returns, contains a floating-point number equivalent of the numeric value or symbol contained in  if the conversion succeeded or zero if the conversion failed. The conversion fails if the  is ReadOnlySpan{T}.Empty or is not in a valid format. This parameter is passed uninitialized; any value originally supplied in result will be overwritten.
        :returns: true if  was converted successfully; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], result: typing.Optional[System.Runtime.InteropServices.NFloat]) -> typing.Tuple[bool, System.Runtime.InteropServices.NFloat]:
        """
        Tries to convert a UTF-8 character span containing the string representation of a number to its floating-point number equivalent.
        
        :param utf_8_text: A read-only UTF-8 character span that contains the number to convert.
        :param result: When this method returns, contains a floating-point number equivalent of the numeric value or symbol contained in  if the conversion succeeded or zero if the conversion failed. The conversion fails if the  is ReadOnlySpan{T}.Empty or is not in a valid format. This parameter is passed uninitialized; any value originally supplied in result will be overwritten.
        :returns: true if  was converted successfully; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def try_parse(s: str, style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[System.Runtime.InteropServices.NFloat]) -> typing.Tuple[bool, System.Runtime.InteropServices.NFloat]:
        """
        Tries to convert the string representation of a number in a specified style and culture-specific format to its floating-point number equivalent.
        
        :param s: A read-only character span that contains the number to convert.
        :param style: A bitwise combination of enumeration values that indicate the style elements that can be present in .
        :param provider: An object that supplies culture-specific formatting information about .
        :param result: When this method returns, contains a floating-point number equivalent of the numeric value or symbol contained in  if the conversion succeeded or zero if the conversion failed. The conversion fails if the  is null, string.Empty, or is not in a format compliant with , or if  is not a valid combination of NumberStyles enumeration constants. This parameter is passed uninitialized; any value originally supplied in result will be overwritten.
        :returns: true if  was converted successfully; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[System.Runtime.InteropServices.NFloat]) -> typing.Tuple[bool, System.Runtime.InteropServices.NFloat]:
        """
        Tries to convert a character span containing the string representation of a number in a specified style and culture-specific format to its floating-point number equivalent.
        
        :param s: A read-only character span that contains the number to convert.
        :param style: A bitwise combination of enumeration values that indicate the style elements that can be present in .
        :param provider: An object that supplies culture-specific formatting information about .
        :param result: When this method returns, contains a floating-point number equivalent of the numeric value or symbol contained in  if the conversion succeeded or zero if the conversion failed. The conversion fails if the  is string.Empty or is not in a format compliant with , or if  is not a valid combination of NumberStyles enumeration constants. This parameter is passed uninitialized; any value originally supplied in result will be overwritten.
        :returns: true if  was converted successfully; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def try_parse(s: str, provider: System.IFormatProvider, result: typing.Optional[System.Runtime.InteropServices.NFloat]) -> typing.Tuple[bool, System.Runtime.InteropServices.NFloat]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], provider: System.IFormatProvider, result: typing.Optional[System.Runtime.InteropServices.NFloat]) -> typing.Tuple[bool, System.Runtime.InteropServices.NFloat]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], style: System.Globalization.NumberStyles, provider: System.IFormatProvider, result: typing.Optional[System.Runtime.InteropServices.NFloat]) -> typing.Tuple[bool, System.Runtime.InteropServices.NFloat]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], provider: System.IFormatProvider, result: typing.Optional[System.Runtime.InteropServices.NFloat]) -> typing.Tuple[bool, System.Runtime.InteropServices.NFloat]:
        ...


class UnmanagedCallConvAttribute(System.Attribute):
    """
    Provides an equivalent to UnmanagedCallersOnlyAttribute for native
    functions declared in .NET.
    """

    @property
    def call_convs(self) -> typing.List[typing.Type]:
        """Types indicating calling conventions for the unmanaged target."""
        ...

    @call_convs.setter
    def call_convs(self, value: typing.List[typing.Type]) -> None:
        ...

    def __init__(self) -> None:
        ...


class SafeArrayRankMismatchException(System.SystemException):
    """
    The exception is thrown when the runtime rank of a safe array is different
    than the array rank specified in the metadata.
    """

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
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """
        This method is protected.
        
        Obsoletions.LegacyFormatterImplMessage
        """
        ...


class TypeIdentifierAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def scope(self) -> str:
        ...

    @property
    def identifier(self) -> str:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, scope: str, identifier: str) -> None:
        ...


class MemoryMarshal(System.Object):
    """
    Provides a collection of methods for interoperating with Memory{T}, ReadOnlyMemory{T},
    Span{T}, and ReadOnlySpan{T}.
    """

    @staticmethod
    def create_read_only_span_from_null_terminated(value: typing.Any) -> System.ReadOnlySpan[str]:
        """
        Creates a new read-only span for a null-terminated string.
        
        :param value: The pointer to the null-terminated string of characters.
        :returns: A read-only span representing the specified null-terminated string, or an empty span if the pointer is null.
        """
        ...

    @staticmethod
    def get_array_data_reference(array: System.Array) -> typing.Any:
        """
        Returns a reference to the 0th element of . If the array is empty, returns a reference to where the 0th element
        would have been stored. Such a reference may be used for pinning but must never be dereferenced.
        """
        ...

    @staticmethod
    def try_get_string(memory: System.ReadOnlyMemory[str], text: typing.Optional[str], start: typing.Optional[int], length: typing.Optional[int]) -> typing.Tuple[bool, str, int, int]:
        """
        Attempts to get the underlying string from a ReadOnlyMemory{T}.
        
        :param memory: The memory that may be wrapping a string object.
        :param text: The string.
        :param start: The starting location in .
        :param length: The number of items in .
        """
        ...


class ClassInterfaceType(Enum):
    """This class has no documentation."""

    NONE = 0

    AUTO_DISPATCH = 1

    AUTO_DUAL = 2


class ClassInterfaceAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def value(self) -> System.Runtime.InteropServices.ClassInterfaceType:
        ...

    @overload
    def __init__(self, class_interface_type: System.Runtime.InteropServices.ClassInterfaceType) -> None:
        ...

    @overload
    def __init__(self, class_interface_type: int) -> None:
        ...


class BestFitMappingAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def best_fit_mapping(self) -> bool:
        ...

    @property
    def throw_on_unmappable_char(self) -> bool:
        ...

    @throw_on_unmappable_char.setter
    def throw_on_unmappable_char(self, value: bool) -> None:
        ...

    def __init__(self, best_fit_mapping: bool) -> None:
        ...


class ICustomAdapter(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def get_underlying_object(self) -> System.Object:
        ...


class VariantWrapper(System.Object):
    """This class has no documentation."""

    @property
    def wrapped_object(self) -> System.Object:
        ...

    def __init__(self, obj: typing.Any) -> None:
        ...


class InvalidComObjectException(System.SystemException):
    """
    The exception thrown when an invalid COM object is used. This happens
    when a the __ComObject type is used directly without having a backing
    class factory.
    """

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
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """
        This method is protected.
        
        Obsoletions.LegacyFormatterImplMessage
        """
        ...


class InterfaceTypeAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def value(self) -> System.Runtime.InteropServices.ComInterfaceType:
        ...

    @overload
    def __init__(self, interface_type: System.Runtime.InteropServices.ComInterfaceType) -> None:
        ...

    @overload
    def __init__(self, interface_type: int) -> None:
        ...


class BStrWrapper(System.Object):
    """This class has no documentation."""

    @property
    def wrapped_object(self) -> str:
        ...

    @overload
    def __init__(self, value: typing.Any) -> None:
        ...

    @overload
    def __init__(self, value: str) -> None:
        ...


class FieldOffsetAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def value(self) -> int:
        ...

    def __init__(self, offset: int) -> None:
        ...


class WeakGCHandle(typing.Generic[System_Runtime_InteropServices_WeakGCHandle_T], System.IEquatable[System_Runtime_InteropServices_WeakGCHandle], System.IDisposable):
    """
    Represents a strongly-typed GC handle to a managed object.
    The object is allowed to be collected. When the object is collected, handle target is set to null.
    """

    @property
    def is_allocated(self) -> bool:
        """Determine whether this handle has been allocated or not."""
        ...

    def __init__(self, target: System_Runtime_InteropServices_WeakGCHandle_T, track_resurrection: bool = False) -> None:
        """
        Allocates a handle for the specified object.
        
        :param target: The object that uses the WeakGCHandle{T}.
        :param track_resurrection: Whether to track the object when it's resurrected in the finalizer.
        """
        ...

    def dispose(self) -> None:
        """Releases this WeakGCHandle{T}."""
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, other: System.Runtime.InteropServices.WeakGCHandle[System_Runtime_InteropServices_WeakGCHandle_T]) -> bool:
        ...

    @staticmethod
    def from_int_ptr(value: System.IntPtr) -> System.Runtime.InteropServices.WeakGCHandle[System_Runtime_InteropServices_WeakGCHandle_T]:
        """
        Returns a new WeakGCHandle{T} object created from a handle to a managed object.
        
        :param value: An IntPtr handle to a managed object to create a WeakGCHandle{T} object from.
        :returns: A new WeakGCHandle{T} object that corresponds to the value parameter.
        """
        ...

    def get_hash_code(self) -> int:
        """
        Returns the hash code for the current instance.
        
        :returns: A hash code for the current instance.
        """
        ...

    def set_target(self, target: System_Runtime_InteropServices_WeakGCHandle_T) -> None:
        """Sets the object this handle represents."""
        ...

    @staticmethod
    def to_int_ptr(value: System.Runtime.InteropServices.WeakGCHandle[System_Runtime_InteropServices_WeakGCHandle_T]) -> System.IntPtr:
        """
        Returns the internal integer representation of a WeakGCHandle{T} object.
        
        :param value: A WeakGCHandle{T} object to retrieve an internal integer representation from.
        :returns: An IntPtr object that represents a WeakGCHandle{T} object.
        """
        ...

    def try_get_target(self, target: typing.Optional[System_Runtime_InteropServices_WeakGCHandle_T]) -> typing.Tuple[bool, System_Runtime_InteropServices_WeakGCHandle_T]:
        """
        Tries to retrieve the target object that is referenced by the current WeakGCHandle{T} object.
        
        :param target: When this method returns, contains the target object, if it is available.
        :returns: true if the target was retrieved; otherwise, false.
        """
        ...


class ImmutableCollectionsMarshal(System.Object):
    """An unsafe class that provides a set of methods to access the underlying data representations of immutable collections."""


