from typing import overload
from enum import Enum
import typing

import System
import System.Windows.Markup


class ValueSerializerAttribute(System.Attribute):
    """
    Attribute to associate a ValueSerializer class with a value type or to override
    which value serializer to use for a property. A value serializer can be associated
    with an attached property by placing the attribute on the static accessor for the
    attached property.
    """

    @property
    def value_serializer_type(self) -> typing.Type:
        """The type of the value serializer to create for this type or property."""
        ...

    @property
    def value_serializer_type_name(self) -> str:
        """The assembly qualified name of the value serializer type for this type or property."""
        ...

    @overload
    def __init__(self, value_serializer_type: typing.Type) -> None:
        """
        Constructor for the ValueSerializerAttribute
        
        :param value_serializer_type: Type of the value serializer being associated with a type or property
        """
        ...

    @overload
    def __init__(self, value_serializer_type_name: str) -> None:
        """
        Constructor for the ValueSerializerAttribute
        
        :param value_serializer_type_name: Fully qualified type name of the value serializer being associated with a type or property
        """
        ...


