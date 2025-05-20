from typing import overload
from enum import Enum
import abc
import typing

import Microsoft.Win32.SafeHandles
import System
import System.Runtime.InteropServices


class SafeHandleMinusOneIsInvalid(System.Runtime.InteropServices.SafeHandle, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    def is_invalid(self) -> bool:
        ...

    def __init__(self, owns_handle: bool) -> None:
        """This method is protected."""
        ...


class SafeHandleZeroOrMinusOneIsInvalid(System.Runtime.InteropServices.SafeHandle, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    def is_invalid(self) -> bool:
        ...

    def __init__(self, owns_handle: bool) -> None:
        """This method is protected."""
        ...


class SafeWaitHandle(Microsoft.Win32.SafeHandles.SafeHandleZeroOrMinusOneIsInvalid):
    """This class has no documentation."""

    @overload
    def __init__(self) -> None:
        """Creates a Microsoft.Win32.SafeHandles.SafeWaitHandle."""
        ...

    @overload
    def __init__(self, existing_handle: System.IntPtr, owns_handle: bool) -> None:
        """
        Creates a Microsoft.Win32.SafeHandles.SafeWaitHandle around a wait handle.
        
        :param existing_handle: Handle to wrap
        :param owns_handle: Whether to control the handle lifetime
        """
        ...

    def release_handle(self) -> bool:
        """This method is protected."""
        ...


class SafeFileHandle(Microsoft.Win32.SafeHandles.SafeHandleZeroOrMinusOneIsInvalid):
    """This class has no documentation."""

    @property
    def is_async(self) -> bool:
        ...

    @property
    def is_invalid(self) -> bool:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, preexisting_handle: System.IntPtr, owns_handle: bool) -> None:
        """
        Creates a Microsoft.Win32.SafeHandles.SafeFileHandle around a file handle.
        
        :param preexisting_handle: Handle to wrap
        :param owns_handle: Whether to control the handle lifetime
        """
        ...

    def release_handle(self) -> bool:
        """This method is protected."""
        ...


class CriticalHandleZeroOrMinusOneIsInvalid(System.Runtime.InteropServices.CriticalHandle, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    def is_invalid(self) -> bool:
        ...

    def __init__(self) -> None:
        """This method is protected."""
        ...


class CriticalHandleMinusOneIsInvalid(System.Runtime.InteropServices.CriticalHandle, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    def is_invalid(self) -> bool:
        ...

    def __init__(self) -> None:
        """This method is protected."""
        ...


