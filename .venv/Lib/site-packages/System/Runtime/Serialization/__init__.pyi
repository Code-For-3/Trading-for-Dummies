from typing import overload
from enum import Enum
import abc
import datetime
import typing
import warnings

import System
import System.Collections
import System.Runtime.Serialization


class StreamingContextStates(Enum):
    """Obsoletions.LegacyFormatterMessage"""

    CROSS_PROCESS = ...

    CROSS_MACHINE = ...

    FILE = ...

    PERSISTENCE = ...

    REMOTING = ...

    OTHER = ...

    CLONE = ...

    CROSS_APP_DOMAIN = ...

    ALL = ...


class StreamingContext:
    """This class has no documentation."""

    @property
    def state(self) -> System.Runtime.Serialization.StreamingContextStates:
        """Obsoletions.LegacyFormatterMessage"""
        warnings.warn("Obsoletions.LegacyFormatterMessage", DeprecationWarning)

    @property
    def context(self) -> System.Object:
        ...

    @overload
    def __init__(self, state: System.Runtime.Serialization.StreamingContextStates, additional: typing.Any) -> None:
        """Obsoletions.LegacyFormatterMessage"""
        ...

    @overload
    def __init__(self, state: System.Runtime.Serialization.StreamingContextStates) -> None:
        """Obsoletions.LegacyFormatterMessage"""
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...


class OnSerializingAttribute(System.Attribute):
    """This class has no documentation."""


class IFormatterConverter(metaclass=abc.ABCMeta):
    """Obsoletions.LegacyFormatterMessage"""

    @overload
    def convert(self, value: typing.Any, type: typing.Type) -> System.Object:
        ...

    @overload
    def convert(self, value: typing.Any, type_code: System.TypeCode) -> System.Object:
        ...

    def to_boolean(self, value: typing.Any) -> bool:
        ...

    def to_byte(self, value: typing.Any) -> int:
        ...

    def to_char(self, value: typing.Any) -> str:
        ...

    def to_date_time(self, value: typing.Any) -> datetime.datetime:
        ...

    def to_decimal(self, value: typing.Any) -> float:
        ...

    def to_double(self, value: typing.Any) -> float:
        ...

    def to_int_16(self, value: typing.Any) -> int:
        ...

    def to_int_32(self, value: typing.Any) -> int:
        ...

    def to_int_64(self, value: typing.Any) -> int:
        ...

    def to_s_byte(self, value: typing.Any) -> int:
        ...

    def to_single(self, value: typing.Any) -> float:
        ...

    def to_string(self, value: typing.Any) -> str:
        ...

    def to_u_int_16(self, value: typing.Any) -> int:
        ...

    def to_u_int_32(self, value: typing.Any) -> int:
        ...

    def to_u_int_64(self, value: typing.Any) -> int:
        ...


class SerializationEntry:
    """This class has no documentation."""

    @property
    def value(self) -> System.Object:
        ...

    @property
    def name(self) -> str:
        ...

    @property
    def object_type(self) -> typing.Type:
        ...


class SerializationInfoEnumerator(System.Object, System.Collections.IEnumerator):
    """This class has no documentation."""

    @property
    def current(self) -> System.Runtime.Serialization.SerializationEntry:
        ...

    @property
    def name(self) -> str:
        ...

    @property
    def value(self) -> System.Object:
        ...

    @property
    def object_type(self) -> typing.Type:
        ...

    def move_next(self) -> bool:
        ...

    def reset(self) -> None:
        ...


class DeserializationToken(System.IDisposable):
    """This class has no documentation."""

    def dispose(self) -> None:
        ...


class SerializationInfo(System.Object):
    """The structure for holding all of the data needed for object serialization and deserialization."""

    @property
    def full_type_name(self) -> str:
        ...

    @full_type_name.setter
    def full_type_name(self, value: str) -> None:
        ...

    @property
    def assembly_name(self) -> str:
        ...

    @assembly_name.setter
    def assembly_name(self, value: str) -> None:
        ...

    @property
    def is_full_type_name_set_explicit(self) -> bool:
        ...

    @property
    def is_assembly_name_set_explicit(self) -> bool:
        ...

    @property
    def member_count(self) -> int:
        ...

    @property
    def object_type(self) -> typing.Type:
        ...

    @overload
    def __init__(self, type: typing.Type, converter: System.Runtime.Serialization.IFormatterConverter) -> None:
        """Obsoletions.LegacyFormatterMessage"""
        ...

    @overload
    def __init__(self, type: typing.Type, converter: System.Runtime.Serialization.IFormatterConverter, require_same_token_in_partial_trust: bool) -> None:
        """Obsoletions.LegacyFormatterMessage"""
        ...

    @overload
    def add_value(self, name: str, value: typing.Any, type: typing.Type) -> None:
        ...

    @overload
    def add_value(self, name: str, value: typing.Any) -> None:
        ...

    @overload
    def add_value(self, name: str, value: bool) -> None:
        ...

    @overload
    def add_value(self, name: str, value: str) -> None:
        ...

    @overload
    def add_value(self, name: str, value: int) -> None:
        ...

    @overload
    def add_value(self, name: str, value: float) -> None:
        ...

    @overload
    def add_value(self, name: str, value: typing.Union[datetime.datetime, datetime.date]) -> None:
        ...

    def get_boolean(self, name: str) -> bool:
        ...

    def get_byte(self, name: str) -> int:
        ...

    def get_char(self, name: str) -> str:
        ...

    def get_date_time(self, name: str) -> datetime.datetime:
        ...

    def get_decimal(self, name: str) -> float:
        ...

    def get_double(self, name: str) -> float:
        ...

    def get_enumerator(self) -> System.Runtime.Serialization.SerializationInfoEnumerator:
        ...

    def get_int_16(self, name: str) -> int:
        ...

    def get_int_32(self, name: str) -> int:
        ...

    def get_int_64(self, name: str) -> int:
        ...

    def get_s_byte(self, name: str) -> int:
        ...

    def get_single(self, name: str) -> float:
        ...

    def get_string(self, name: str) -> str:
        ...

    def get_u_int_16(self, name: str) -> int:
        ...

    def get_u_int_32(self, name: str) -> int:
        ...

    def get_u_int_64(self, name: str) -> int:
        ...

    def get_value(self, name: str, type: typing.Type) -> System.Object:
        ...

    def set_type(self, type: typing.Type) -> None:
        ...

    @staticmethod
    def start_deserialization() -> System.Runtime.Serialization.DeserializationToken:
        ...


class SerializationException(System.SystemException):
    """This class has no documentation."""

    @overload
    def __init__(self) -> None:
        """
        Creates a new SerializationException with its message
        string set to a default message.
        """
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


class OnDeserializingAttribute(System.Attribute):
    """This class has no documentation."""


class IDeserializationCallback(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def on_deserialization(self, sender: typing.Any) -> None:
        ...


class ISafeSerializationData(metaclass=abc.ABCMeta):
    """Obsoletions.LegacyFormatterMessage"""

    def complete_deserialization(self, deserialized: typing.Any) -> None:
        ...


class OnSerializedAttribute(System.Attribute):
    """This class has no documentation."""


class OnDeserializedAttribute(System.Attribute):
    """This class has no documentation."""


class OptionalFieldAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def version_added(self) -> int:
        ...

    @version_added.setter
    def version_added(self, value: int) -> None:
        ...


class IObjectReference(metaclass=abc.ABCMeta):
    """Obsoletions.LegacyFormatterMessage"""

    def get_real_object(self, context: System.Runtime.Serialization.StreamingContext) -> System.Object:
        ...


class ISerializable(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def get_object_data(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """Obsoletions.LegacyFormatterMessage"""
        warnings.warn("Obsoletions.LegacyFormatterMessage", DeprecationWarning)


class SafeSerializationEventArgs(System.EventArgs):
    """Obsoletions.LegacyFormatterMessage"""

    @property
    def streaming_context(self) -> System.Runtime.Serialization.StreamingContext:
        ...

    def add_serialized_state(self, serialized_state: System.Runtime.Serialization.ISafeSerializationData) -> None:
        ...


