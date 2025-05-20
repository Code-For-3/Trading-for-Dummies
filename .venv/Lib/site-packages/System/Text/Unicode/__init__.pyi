from typing import overload
from enum import Enum
import typing

import System
import System.Buffers
import System.Text.Unicode


class Utf8(System.Object):
    """Provides static methods that convert chunked data between UTF-8 and UTF-16 encodings."""

    @staticmethod
    def from_utf_16(source: System.ReadOnlySpan[str], destination: System.Span[int], chars_read: typing.Optional[int], bytes_written: typing.Optional[int], replace_invalid_sequences: bool = True, is_final_block: bool = True) -> typing.Tuple[System.Buffers.OperationStatus, int, int]:
        """Transcodes the UTF-16  buffer to  as UTF-8."""
        ...

    @staticmethod
    def is_valid(value: System.ReadOnlySpan[int]) -> bool:
        """
        Validates that the value is well-formed UTF-8.
        
        :param value: The ReadOnlySpan{T} string.
        :returns: true if value is well-formed UTF-8, false otherwise.
        """
        ...

    @staticmethod
    def to_utf_16(source: System.ReadOnlySpan[int], destination: System.Span[str], bytes_read: typing.Optional[int], chars_written: typing.Optional[int], replace_invalid_sequences: bool = True, is_final_block: bool = True) -> typing.Tuple[System.Buffers.OperationStatus, int, int]:
        """Transcodes the UTF-8  buffer to  as UTF-16."""
        ...


