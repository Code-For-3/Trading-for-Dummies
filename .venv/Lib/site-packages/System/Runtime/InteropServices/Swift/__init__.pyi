from typing import overload
from enum import Enum
import typing

import System.Runtime.InteropServices.Swift

System_Runtime_InteropServices_Swift_SwiftSelf_T = typing.TypeVar("System_Runtime_InteropServices_Swift_SwiftSelf_T")


class SwiftSelf(typing.Generic[System_Runtime_InteropServices_Swift_SwiftSelf_T]):
    """
    Represents the Swift 'self' context when the argument is Swift frozen struct T, which is either enregistered into multiple registers,
    or passed by reference in the 'self' register.
    """

    @property
    def value(self) -> typing.Any:
        """Gets the pointer of the self context."""
        ...

    @overload
    def __init__(self, value: typing.Any) -> None:
        """
        Creates a new instance of the SwiftSelf struct with the specified pointer value.
        
        :param value: The pointer value representing the self context.
        """
        ...

    @overload
    def __init__(self, value: System_Runtime_InteropServices_Swift_SwiftSelf_T) -> None:
        """
        Creates a new instance of the SwiftSelf struct with the specified value.
        
        :param value: The value representing the self context.
        """
        ...


class SwiftError:
    """Represents the Swift error context, indicating that the argument is the error context."""

    @property
    def value(self) -> typing.Any:
        """Gets the pointer of the error context."""
        ...

    def __init__(self, value: typing.Any) -> None:
        """
        Creates a new instance of the SwiftError struct with the specified pointer value.
        
        :param value: The pointer value representing the error context.
        """
        ...


class SwiftIndirectResult:
    """Represents the Swift return buffer context."""

    @property
    def value(self) -> typing.Any:
        """Gets the pointer of the return buffer register."""
        ...

    def __init__(self, value: typing.Any) -> None:
        """
        Creates a new instance of the SwiftIndirectResult struct with the specified pointer value.
        
        :param value: The pointer value representing return buffer context.
        """
        ...


