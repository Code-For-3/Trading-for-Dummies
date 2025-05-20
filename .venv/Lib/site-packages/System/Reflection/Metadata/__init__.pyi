from typing import overload
from enum import Enum
import typing

import System
import System.Reflection.Metadata


class MetadataUpdateHandlerAttribute(System.Attribute):
    """Specifies a type that should receive notifications of metadata updates."""

    @property
    def handler_type(self) -> typing.Type:
        """Gets the type that handles metadata updates and that should be notified when any occur."""
        ...

    def __init__(self, handler_type: typing.Type) -> None:
        """
        Initializes the attribute.
        
        :param handler_type: A type that handles metadata updates and that should be notified when any occur.
        """
        ...


