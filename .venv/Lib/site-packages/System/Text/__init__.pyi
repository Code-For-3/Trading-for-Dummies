from typing import overload
from enum import Enum
import abc
import typing

import System
import System.Buffers
import System.Collections.Generic
import System.IO
import System.Runtime.Serialization
import System.Text


class EncoderFallbackBuffer(System.Object, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def remaining(self) -> int:
        ...

    @overload
    def fallback(self, char_unknown: str, index: int) -> bool:
        ...

    @overload
    def fallback(self, char_unknown_high: str, char_unknown_low: str, index: int) -> bool:
        ...

    def get_next_char(self) -> str:
        ...

    def move_previous(self) -> bool:
        ...

    def reset(self) -> None:
        ...


class EncoderFallback(System.Object, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    REPLACEMENT_FALLBACK: System.Text.EncoderFallback

    EXCEPTION_FALLBACK: System.Text.EncoderFallback

    @property
    @abc.abstractmethod
    def max_char_count(self) -> int:
        ...

    def create_fallback_buffer(self) -> System.Text.EncoderFallbackBuffer:
        ...


class DecoderFallbackBuffer(System.Object, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def remaining(self) -> int:
        ...

    def fallback(self, bytes_unknown: typing.List[int], index: int) -> bool:
        ...

    def get_next_char(self) -> str:
        ...

    def move_previous(self) -> bool:
        ...

    def reset(self) -> None:
        ...


class DecoderFallback(System.Object, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    REPLACEMENT_FALLBACK: System.Text.DecoderFallback

    EXCEPTION_FALLBACK: System.Text.DecoderFallback

    @property
    @abc.abstractmethod
    def max_char_count(self) -> int:
        ...

    def create_fallback_buffer(self) -> System.Text.DecoderFallbackBuffer:
        ...


class EncodingInfo(System.Object):
    """This class has no documentation."""

    @property
    def code_page(self) -> int:
        """Get the encoding codepage number"""
        ...

    @property
    def name(self) -> str:
        """Get the encoding name"""
        ...

    @property
    def display_name(self) -> str:
        """Get the encoding display name"""
        ...

    def __init__(self, provider: System.Text.EncodingProvider, code_page: int, name: str, display_name: str) -> None:
        """
        Construct an EncodingInfo object.
        
        :param provider: The EncodingProvider object which created this EncodingInfo object
        :param code_page: The encoding codepage
        :param name: The encoding name
        :param display_name: The encoding display name
        """
        ...

    def equals(self, value: typing.Any) -> bool:
        """
        Compare this EncodingInfo object to other object.
        
        :param value: The other object to compare with this object
        :returns: True if the value object is EncodingInfo object and has a codepage equals to this EncodingInfo object codepage. Otherwise, it returns False.
        """
        ...

    def get_encoding(self) -> System.Text.Encoding:
        """
        Get the Encoding object match the information in the EncodingInfo object
        
        :returns: The Encoding object.
        """
        ...

    def get_hash_code(self) -> int:
        """
        Get a hashcode representing the current EncodingInfo object.
        
        :returns: The integer value representing the hash code of the EncodingInfo object.
        """
        ...


class EncodingProvider(System.Object, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...

    @overload
    def get_encoding(self, name: str) -> System.Text.Encoding:
        ...

    @overload
    def get_encoding(self, codepage: int) -> System.Text.Encoding:
        ...

    @overload
    def get_encoding(self, name: str, encoder_fallback: System.Text.EncoderFallback, decoder_fallback: System.Text.DecoderFallback) -> System.Text.Encoding:
        ...

    @overload
    def get_encoding(self, codepage: int, encoder_fallback: System.Text.EncoderFallback, decoder_fallback: System.Text.DecoderFallback) -> System.Text.Encoding:
        ...

    def get_encodings(self) -> System.Collections.Generic.IEnumerable[System.Text.EncodingInfo]:
        ...


class NormalizationForm(Enum):
    """This class has no documentation."""

    FORM_C = 1

    FORM_D = 2

    FORM_KC = 5

    FORM_KD = 6


class Decoder(System.Object, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    def fallback(self) -> System.Text.DecoderFallback:
        ...

    @fallback.setter
    def fallback(self, value: System.Text.DecoderFallback) -> None:
        ...

    @property
    def fallback_buffer(self) -> System.Text.DecoderFallbackBuffer:
        ...

    def __init__(self) -> None:
        """This method is protected."""
        ...

    @overload
    def convert(self, bytes: typing.Any, byte_count: int, chars: typing.Any, char_count: int, flush: bool, bytes_used: typing.Optional[int], chars_used: typing.Optional[int], completed: typing.Optional[bool]) -> typing.Tuple[None, int, int, bool]:
        ...

    @overload
    def convert(self, bytes: typing.List[int], byte_index: int, byte_count: int, chars: typing.List[str], char_index: int, char_count: int, flush: bool, bytes_used: typing.Optional[int], chars_used: typing.Optional[int], completed: typing.Optional[bool]) -> typing.Tuple[None, int, int, bool]:
        ...

    @overload
    def convert(self, bytes: System.ReadOnlySpan[int], chars: System.Span[str], flush: bool, bytes_used: typing.Optional[int], chars_used: typing.Optional[int], completed: typing.Optional[bool]) -> typing.Tuple[None, int, int, bool]:
        ...

    @overload
    def get_char_count(self, bytes: typing.Any, count: int, flush: bool) -> int:
        ...

    @overload
    def get_char_count(self, bytes: typing.List[int], index: int, count: int) -> int:
        ...

    @overload
    def get_char_count(self, bytes: typing.List[int], index: int, count: int, flush: bool) -> int:
        ...

    @overload
    def get_char_count(self, bytes: System.ReadOnlySpan[int], flush: bool) -> int:
        ...

    @overload
    def get_chars(self, bytes: typing.Any, byte_count: int, chars: typing.Any, char_count: int, flush: bool) -> int:
        ...

    @overload
    def get_chars(self, bytes: typing.List[int], byte_index: int, byte_count: int, chars: typing.List[str], char_index: int) -> int:
        ...

    @overload
    def get_chars(self, bytes: typing.List[int], byte_index: int, byte_count: int, chars: typing.List[str], char_index: int, flush: bool) -> int:
        ...

    @overload
    def get_chars(self, bytes: System.ReadOnlySpan[int], chars: System.Span[str], flush: bool) -> int:
        ...

    def reset(self) -> None:
        ...


class Encoder(System.Object, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    def fallback(self) -> System.Text.EncoderFallback:
        ...

    @fallback.setter
    def fallback(self, value: System.Text.EncoderFallback) -> None:
        ...

    @property
    def fallback_buffer(self) -> System.Text.EncoderFallbackBuffer:
        ...

    def __init__(self) -> None:
        """This method is protected."""
        ...

    @overload
    def convert(self, chars: typing.Any, char_count: int, bytes: typing.Any, byte_count: int, flush: bool, chars_used: typing.Optional[int], bytes_used: typing.Optional[int], completed: typing.Optional[bool]) -> typing.Tuple[None, int, int, bool]:
        ...

    @overload
    def convert(self, chars: typing.List[str], char_index: int, char_count: int, bytes: typing.List[int], byte_index: int, byte_count: int, flush: bool, chars_used: typing.Optional[int], bytes_used: typing.Optional[int], completed: typing.Optional[bool]) -> typing.Tuple[None, int, int, bool]:
        ...

    @overload
    def convert(self, chars: System.ReadOnlySpan[str], bytes: System.Span[int], flush: bool, chars_used: typing.Optional[int], bytes_used: typing.Optional[int], completed: typing.Optional[bool]) -> typing.Tuple[None, int, int, bool]:
        ...

    @overload
    def get_byte_count(self, chars: typing.Any, count: int, flush: bool) -> int:
        ...

    @overload
    def get_byte_count(self, chars: typing.List[str], index: int, count: int, flush: bool) -> int:
        ...

    @overload
    def get_byte_count(self, chars: System.ReadOnlySpan[str], flush: bool) -> int:
        ...

    @overload
    def get_bytes(self, chars: typing.Any, char_count: int, bytes: typing.Any, byte_count: int, flush: bool) -> int:
        ...

    @overload
    def get_bytes(self, chars: typing.List[str], char_index: int, char_count: int, bytes: typing.List[int], byte_index: int, flush: bool) -> int:
        ...

    @overload
    def get_bytes(self, chars: System.ReadOnlySpan[str], bytes: System.Span[int], flush: bool) -> int:
        ...

    def reset(self) -> None:
        ...


class Encoding(System.Object, System.ICloneable):
    """This class has no documentation."""

    DEFAULT: System.Text.Encoding

    @property
    def preamble(self) -> System.ReadOnlySpan[int]:
        ...

    @property
    def body_name(self) -> str:
        ...

    @property
    def encoding_name(self) -> str:
        ...

    @property
    def header_name(self) -> str:
        ...

    @property
    def web_name(self) -> str:
        ...

    @property
    def windows_code_page(self) -> int:
        ...

    @property
    def is_browser_display(self) -> bool:
        ...

    @property
    def is_browser_save(self) -> bool:
        ...

    @property
    def is_mail_news_display(self) -> bool:
        ...

    @property
    def is_mail_news_save(self) -> bool:
        ...

    @property
    def is_single_byte(self) -> bool:
        ...

    @property
    def encoder_fallback(self) -> System.Text.EncoderFallback:
        ...

    @encoder_fallback.setter
    def encoder_fallback(self, value: System.Text.EncoderFallback) -> None:
        ...

    @property
    def decoder_fallback(self) -> System.Text.DecoderFallback:
        ...

    @decoder_fallback.setter
    def decoder_fallback(self, value: System.Text.DecoderFallback) -> None:
        ...

    @property
    def is_read_only(self) -> bool:
        ...

    ASCII: System.Text.Encoding

    LATIN_1: System.Text.Encoding
    """Gets an encoding for the Latin1 character set (ISO-8859-1)."""

    @property
    def code_page(self) -> int:
        ...

    UNICODE: System.Text.Encoding

    BIG_ENDIAN_UNICODE: System.Text.Encoding

    UTF_7: System.Text.Encoding
    """Obsoletions.SystemTextEncodingUTF7Message"""

    UTF_8: System.Text.Encoding

    UTF_32: System.Text.Encoding

    @overload
    def __init__(self) -> None:
        """This method is protected."""
        ...

    @overload
    def __init__(self, code_page: int) -> None:
        """This method is protected."""
        ...

    @overload
    def __init__(self, code_page: int, encoder_fallback: System.Text.EncoderFallback, decoder_fallback: System.Text.DecoderFallback) -> None:
        """This method is protected."""
        ...

    def clone(self) -> System.Object:
        ...

    @staticmethod
    @overload
    def convert(src_encoding: System.Text.Encoding, dst_encoding: System.Text.Encoding, bytes: typing.List[int]) -> typing.List[int]:
        ...

    @staticmethod
    @overload
    def convert(src_encoding: System.Text.Encoding, dst_encoding: System.Text.Encoding, bytes: typing.List[int], index: int, count: int) -> typing.List[int]:
        ...

    @staticmethod
    def create_transcoding_stream(inner_stream: System.IO.Stream, inner_stream_encoding: System.Text.Encoding, outer_stream_encoding: System.Text.Encoding, leave_open: bool = False) -> System.IO.Stream:
        """
        Creates a Stream which serves to transcode data between an inner Encoding
        and an outer Encoding, similar to Convert.
        
        :param inner_stream: The Stream to wrap.
        :param inner_streamEncoding: The Encoding associated with .
        :param outer_stream_encoding: The Encoding associated with the Stream returned by this method.
        :param leave_open: true if disposing the Stream returned by this method should not dispose .
        :returns: A Stream which transcodes the contents of  as .
        """
        ...

    def equals(self, value: typing.Any) -> bool:
        ...

    @overload
    def get_byte_count(self, chars: typing.Any, count: int) -> int:
        ...

    @overload
    def get_byte_count(self, chars: typing.List[str]) -> int:
        ...

    @overload
    def get_byte_count(self, s: str) -> int:
        ...

    @overload
    def get_byte_count(self, chars: typing.List[str], index: int, count: int) -> int:
        ...

    @overload
    def get_byte_count(self, s: str, index: int, count: int) -> int:
        ...

    @overload
    def get_byte_count(self, chars: System.ReadOnlySpan[str]) -> int:
        ...

    @overload
    def get_bytes(self, chars: typing.Any, char_count: int, bytes: typing.Any, byte_count: int) -> int:
        ...

    @overload
    def get_bytes(self, chars: typing.List[str]) -> typing.List[int]:
        ...

    @overload
    def get_bytes(self, chars: typing.List[str], index: int, count: int) -> typing.List[int]:
        ...

    @overload
    def get_bytes(self, chars: typing.List[str], char_index: int, char_count: int, bytes: typing.List[int], byte_index: int) -> int:
        ...

    @overload
    def get_bytes(self, s: str) -> typing.List[int]:
        ...

    @overload
    def get_bytes(self, s: str, index: int, count: int) -> typing.List[int]:
        ...

    @overload
    def get_bytes(self, s: str, char_index: int, char_count: int, bytes: typing.List[int], byte_index: int) -> int:
        ...

    @overload
    def get_bytes(self, chars: System.ReadOnlySpan[str], bytes: System.Span[int]) -> int:
        ...

    @overload
    def get_char_count(self, bytes: typing.Any, count: int) -> int:
        ...

    @overload
    def get_char_count(self, bytes: typing.List[int]) -> int:
        ...

    @overload
    def get_char_count(self, bytes: typing.List[int], index: int, count: int) -> int:
        ...

    @overload
    def get_char_count(self, bytes: System.ReadOnlySpan[int]) -> int:
        ...

    @overload
    def get_chars(self, bytes: typing.Any, byte_count: int, chars: typing.Any, char_count: int) -> int:
        ...

    @overload
    def get_chars(self, bytes: typing.List[int]) -> typing.List[str]:
        ...

    @overload
    def get_chars(self, bytes: typing.List[int], index: int, count: int) -> typing.List[str]:
        ...

    @overload
    def get_chars(self, bytes: typing.List[int], byte_index: int, byte_count: int, chars: typing.List[str], char_index: int) -> int:
        ...

    @overload
    def get_chars(self, bytes: System.ReadOnlySpan[int], chars: System.Span[str]) -> int:
        ...

    def get_decoder(self) -> System.Text.Decoder:
        ...

    def get_encoder(self) -> System.Text.Encoder:
        ...

    @staticmethod
    @overload
    def get_encoding(codepage: int) -> System.Text.Encoding:
        ...

    @staticmethod
    @overload
    def get_encoding(codepage: int, encoder_fallback: System.Text.EncoderFallback, decoder_fallback: System.Text.DecoderFallback) -> System.Text.Encoding:
        ...

    @staticmethod
    @overload
    def get_encoding(name: str) -> System.Text.Encoding:
        ...

    @staticmethod
    @overload
    def get_encoding(name: str, encoder_fallback: System.Text.EncoderFallback, decoder_fallback: System.Text.DecoderFallback) -> System.Text.Encoding:
        ...

    @staticmethod
    def get_encodings() -> typing.List[System.Text.EncodingInfo]:
        """
        Get the EncodingInfo list from the runtime and all registered encoding providers
        
        :returns: The list of the EncodingProvider objects.
        """
        ...

    def get_hash_code(self) -> int:
        ...

    def get_max_byte_count(self, char_count: int) -> int:
        ...

    def get_max_char_count(self, byte_count: int) -> int:
        ...

    def get_preamble(self) -> typing.List[int]:
        ...

    @overload
    def get_string(self, bytes: typing.Any, byte_count: int) -> str:
        ...

    @overload
    def get_string(self, bytes: System.ReadOnlySpan[int]) -> str:
        ...

    @overload
    def get_string(self, bytes: typing.List[int]) -> str:
        ...

    @overload
    def get_string(self, bytes: typing.List[int], index: int, count: int) -> str:
        ...

    @overload
    def is_always_normalized(self) -> bool:
        ...

    @overload
    def is_always_normalized(self, form: System.Text.NormalizationForm) -> bool:
        ...

    @staticmethod
    def register_provider(provider: System.Text.EncodingProvider) -> None:
        ...

    def try_get_bytes(self, chars: System.ReadOnlySpan[str], bytes: System.Span[int], bytes_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        """
        Encodes into a span of bytes a set of characters from the specified read-only span if the destination is large enough.
        
        :param chars: The span containing the set of characters to encode.
        :param bytes: The byte span to hold the encoded bytes.
        :param bytes_written: Upon successful completion of the operation, the number of bytes encoded into .
        :returns: true if all of the characters were encoded into the destination; false if the destination was too small to contain all the encoded bytes.
        """
        ...

    def try_get_chars(self, bytes: System.ReadOnlySpan[int], chars: System.Span[str], chars_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        """
        Decodes into a span of chars a set of bytes from the specified read-only span if the destination is large enough.
        
        :param bytes: A read-only span containing the sequence of bytes to decode.
        :param chars: The character span receiving the decoded bytes.
        :param chars_written: Upon successful completion of the operation, the number of chars decoded into .
        :returns: true if all of the characters were decoded into the destination; false if the destination was too small to contain all the decoded chars.
        """
        ...


class UnicodeEncoding(System.Text.Encoding):
    """This class has no documentation."""

    CHAR_SIZE: int = 2

    @property
    def preamble(self) -> System.ReadOnlySpan[int]:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, big_endian: bool, byte_order_mark: bool) -> None:
        ...

    @overload
    def __init__(self, big_endian: bool, byte_order_mark: bool, throw_on_invalid_bytes: bool) -> None:
        ...

    def equals(self, value: typing.Any) -> bool:
        ...

    @overload
    def get_byte_count(self, chars: typing.Any, count: int) -> int:
        ...

    @overload
    def get_byte_count(self, chars: typing.List[str], index: int, count: int) -> int:
        ...

    @overload
    def get_byte_count(self, s: str) -> int:
        ...

    @overload
    def get_bytes(self, chars: typing.Any, char_count: int, bytes: typing.Any, byte_count: int) -> int:
        ...

    @overload
    def get_bytes(self, s: str, char_index: int, char_count: int, bytes: typing.List[int], byte_index: int) -> int:
        ...

    @overload
    def get_bytes(self, chars: typing.List[str], char_index: int, char_count: int, bytes: typing.List[int], byte_index: int) -> int:
        ...

    @overload
    def get_char_count(self, bytes: typing.Any, count: int) -> int:
        ...

    @overload
    def get_char_count(self, bytes: typing.List[int], index: int, count: int) -> int:
        ...

    @overload
    def get_chars(self, bytes: typing.Any, byte_count: int, chars: typing.Any, char_count: int) -> int:
        ...

    @overload
    def get_chars(self, bytes: typing.List[int], byte_index: int, byte_count: int, chars: typing.List[str], char_index: int) -> int:
        ...

    def get_decoder(self) -> System.Text.Decoder:
        ...

    def get_encoder(self) -> System.Text.Encoder:
        ...

    def get_hash_code(self) -> int:
        ...

    def get_max_byte_count(self, char_count: int) -> int:
        ...

    def get_max_char_count(self, byte_count: int) -> int:
        ...

    def get_preamble(self) -> typing.List[int]:
        ...

    def get_string(self, bytes: typing.List[int], index: int, count: int) -> str:
        ...


class Ascii(System.Object):
    """This class has no documentation."""

    @staticmethod
    @overload
    def equals(left: System.ReadOnlySpan[int], right: System.ReadOnlySpan[int]) -> bool:
        """
        Determines whether the provided buffers contain equal ASCII characters.
        
        :param left: The buffer to compare with .
        :param right: The buffer to compare with .
        :returns: true if the corresponding elements in  and  were equal and ASCII. false otherwise.
        """
        ...

    @staticmethod
    @overload
    def equals(left: System.ReadOnlySpan[int], right: System.ReadOnlySpan[str]) -> bool:
        ...

    @staticmethod
    @overload
    def equals(left: System.ReadOnlySpan[str], right: System.ReadOnlySpan[int]) -> bool:
        ...

    @staticmethod
    @overload
    def equals(left: System.ReadOnlySpan[str], right: System.ReadOnlySpan[str]) -> bool:
        ...

    @staticmethod
    @overload
    def equals_ignore_case(left: System.ReadOnlySpan[int], right: System.ReadOnlySpan[int]) -> bool:
        """
        Determines whether the provided buffers contain equal ASCII characters, ignoring case considerations.
        
        :param left: The buffer to compare with .
        :param right: The buffer to compare with .
        :returns: true if the corresponding elements in  and  were equal ignoring case considerations and ASCII. false otherwise.
        """
        ...

    @staticmethod
    @overload
    def equals_ignore_case(left: System.ReadOnlySpan[int], right: System.ReadOnlySpan[str]) -> bool:
        ...

    @staticmethod
    @overload
    def equals_ignore_case(left: System.ReadOnlySpan[str], right: System.ReadOnlySpan[int]) -> bool:
        ...

    @staticmethod
    @overload
    def equals_ignore_case(left: System.ReadOnlySpan[str], right: System.ReadOnlySpan[str]) -> bool:
        ...

    @staticmethod
    def from_utf_16(source: System.ReadOnlySpan[str], destination: System.Span[int], bytes_written: typing.Optional[int]) -> typing.Tuple[System.Buffers.OperationStatus, int]:
        """
        Copies text from a source buffer to a destination buffer, converting
        from UTF-16 to ASCII during the copy.
        
        :param source: The source buffer from which UTF-16 text is read.
        :param destination: The destination buffer to which ASCII text is written.
        :param bytes_written: The number of bytes actually written to . It's the same as the number of chars actually read from .
        :returns: An OperationStatus describing the result of the operation.
        """
        ...

    @staticmethod
    @overload
    def is_valid(value: System.ReadOnlySpan[int]) -> bool:
        """
        Determines whether the provided value contains only ASCII bytes.
        
        :param value: The value to inspect.
        :returns: True if  contains only ASCII bytes or is empty; False otherwise.
        """
        ...

    @staticmethod
    @overload
    def is_valid(value: System.ReadOnlySpan[str]) -> bool:
        """
        Determines whether the provided value contains only ASCII chars.
        
        :param value: The value to inspect.
        :returns: True if  contains only ASCII chars or is empty; False otherwise.
        """
        ...

    @staticmethod
    @overload
    def is_valid(value: int) -> bool:
        """
        Determines whether the provided value is ASCII byte.
        
        :param value: The value to inspect.
        :returns: True if  is ASCII, False otherwise.
        """
        ...

    @staticmethod
    @overload
    def is_valid(value: str) -> bool:
        """
        Determines whether the provided value is ASCII char.
        
        :param value: The value to inspect.
        :returns: True if  is ASCII, False otherwise.
        """
        ...

    @staticmethod
    @overload
    def to_lower(source: System.ReadOnlySpan[int], destination: System.Span[int], bytes_written: typing.Optional[int]) -> typing.Tuple[System.Buffers.OperationStatus, int]:
        """
        Copies text from a source buffer to a destination buffer, converting
        ASCII letters to lowercase during the copy.
        
        :param source: The source buffer from which ASCII text is read.
        :param destination: The destination buffer to which lowercase text is written.
        :param bytes_written: The number of bytes actually written to . It's the same as the number of bytes actually read from .
        :returns: An OperationStatus describing the result of the operation.
        """
        ...

    @staticmethod
    @overload
    def to_lower(source: System.ReadOnlySpan[str], destination: System.Span[str], chars_written: typing.Optional[int]) -> typing.Tuple[System.Buffers.OperationStatus, int]:
        """
        Copies text from a source buffer to a destination buffer, converting
        ASCII letters to lowercase during the copy.
        
        :param source: The source buffer from which ASCII text is read.
        :param destination: The destination buffer to which lowercase text is written.
        :param chars_written: The number of characters actually written to . It's the same as the number of characters actually read from .
        :returns: An OperationStatus describing the result of the operation.
        """
        ...

    @staticmethod
    @overload
    def to_lower(source: System.ReadOnlySpan[int], destination: System.Span[str], chars_written: typing.Optional[int]) -> typing.Tuple[System.Buffers.OperationStatus, int]:
        """
        Copies text from a source buffer to a destination buffer, converting
        ASCII letters to lowercase during the copy.
        
        :param source: The source buffer from which ASCII text is read.
        :param destination: The destination buffer to which lowercase text is written.
        :param chars_written: The number of characters actually written to . It's the same as the number of bytes actually read from .
        :returns: An OperationStatus describing the result of the operation.
        """
        ...

    @staticmethod
    @overload
    def to_lower(source: System.ReadOnlySpan[str], destination: System.Span[int], bytes_written: typing.Optional[int]) -> typing.Tuple[System.Buffers.OperationStatus, int]:
        """
        Copies text from a source buffer to a destination buffer, converting
        ASCII letters to lowercase during the copy.
        
        :param source: The source buffer from which ASCII text is read.
        :param destination: The destination buffer to which lowercase text is written.
        :param bytes_written: The number of bytes actually written to . It's the same as the number of characters actually read from .
        :returns: An OperationStatus describing the result of the operation.
        """
        ...

    @staticmethod
    @overload
    def to_lower_in_place(value: System.Span[int], bytes_written: typing.Optional[int]) -> typing.Tuple[System.Buffers.OperationStatus, int]:
        """
        Performs in-place uppercase conversion.
        
        :param value: The ASCII text buffer.
        :param bytes_written: The number of processed bytes.
        :returns: An OperationStatus describing the result of the operation.
        """
        ...

    @staticmethod
    @overload
    def to_lower_in_place(value: System.Span[str], chars_written: typing.Optional[int]) -> typing.Tuple[System.Buffers.OperationStatus, int]:
        """
        Performs in-place uppercase conversion.
        
        :param value: The ASCII text buffer.
        :param chars_written: The number of processed characters.
        :returns: An OperationStatus describing the result of the operation.
        """
        ...

    @staticmethod
    @overload
    def to_upper(source: System.ReadOnlySpan[int], destination: System.Span[int], bytes_written: typing.Optional[int]) -> typing.Tuple[System.Buffers.OperationStatus, int]:
        """
        Copies text from a source buffer to a destination buffer, converting
        ASCII letters to uppercase during the copy.
        
        :param source: The source buffer from which ASCII text is read.
        :param destination: The destination buffer to which uppercase text is written.
        :param bytes_written: The number of bytes actually written to . It's the same as the number of bytes actually read from .
        :returns: An OperationStatus describing the result of the operation.
        """
        ...

    @staticmethod
    @overload
    def to_upper(source: System.ReadOnlySpan[str], destination: System.Span[str], chars_written: typing.Optional[int]) -> typing.Tuple[System.Buffers.OperationStatus, int]:
        """
        Copies text from a source buffer to a destination buffer, converting
        ASCII letters to uppercase during the copy.
        
        :param source: The source buffer from which ASCII text is read.
        :param destination: The destination buffer to which uppercase text is written.
        :param chars_written: The number of characters actually written to . It's the same as the number of characters actually read from .
        :returns: An OperationStatus describing the result of the operation.
        """
        ...

    @staticmethod
    @overload
    def to_upper(source: System.ReadOnlySpan[int], destination: System.Span[str], chars_written: typing.Optional[int]) -> typing.Tuple[System.Buffers.OperationStatus, int]:
        """
        Copies text from a source buffer to a destination buffer, converting
        ASCII letters to uppercase during the copy.
        
        :param source: The source buffer from which ASCII text is read.
        :param destination: The destination buffer to which uppercase text is written.
        :param chars_written: The number of characters actually written to . It's the same as the number of bytes actually read from .
        :returns: An OperationStatus describing the result of the operation.
        """
        ...

    @staticmethod
    @overload
    def to_upper(source: System.ReadOnlySpan[str], destination: System.Span[int], bytes_written: typing.Optional[int]) -> typing.Tuple[System.Buffers.OperationStatus, int]:
        """
        Copies text from a source buffer to a destination buffer, converting
        ASCII letters to uppercase during the copy.
        
        :param source: The source buffer from which ASCII text is read.
        :param destination: The destination buffer to which uppercase text is written.
        :param bytes_written: The number of bytes actually written to . It's the same as the number of characters actually read from .
        :returns: An OperationStatus describing the result of the operation.
        """
        ...

    @staticmethod
    @overload
    def to_upper_in_place(value: System.Span[int], bytes_written: typing.Optional[int]) -> typing.Tuple[System.Buffers.OperationStatus, int]:
        """
        Performs in-place lowercase conversion.
        
        :param value: The ASCII text buffer.
        :param bytes_written: The number of processed bytes.
        :returns: An OperationStatus describing the result of the operation.
        """
        ...

    @staticmethod
    @overload
    def to_upper_in_place(value: System.Span[str], chars_written: typing.Optional[int]) -> typing.Tuple[System.Buffers.OperationStatus, int]:
        """
        Performs in-place lowercase conversion.
        
        :param value: The ASCII text buffer.
        :param chars_written: The number of processed characters.
        :returns: An OperationStatus describing the result of the operation.
        """
        ...

    @staticmethod
    def to_utf_16(source: System.ReadOnlySpan[int], destination: System.Span[str], chars_written: typing.Optional[int]) -> typing.Tuple[System.Buffers.OperationStatus, int]:
        """
        Copies text from a source buffer to a destination buffer, converting
        from ASCII to UTF-16 during the copy.
        
        :param source: The source buffer from which ASCII text is read.
        :param destination: The destination buffer to which UTF-16 text is written.
        :param chars_written: The number of chars actually written to . It's the same as the number of bytes actually read from
        :returns: An OperationStatus describing the result of the operation.
        """
        ...

    @staticmethod
    @overload
    def trim(value: System.ReadOnlySpan[int]) -> System.Range:
        """
        Trims all leading and trailing ASCII whitespaces from the buffer.
        
        :param value: The ASCII buffer.
        :returns: The Range of the untrimmed data.
        """
        ...

    @staticmethod
    @overload
    def trim(value: System.ReadOnlySpan[str]) -> System.Range:
        ...

    @staticmethod
    @overload
    def trim_end(value: System.ReadOnlySpan[int]) -> System.Range:
        """
        Trims all trailing ASCII whitespaces from the buffer.
        
        :param value: The ASCII buffer.
        :returns: The Range of the untrimmed data.
        """
        ...

    @staticmethod
    @overload
    def trim_end(value: System.ReadOnlySpan[str]) -> System.Range:
        ...

    @staticmethod
    @overload
    def trim_start(value: System.ReadOnlySpan[int]) -> System.Range:
        """
        Trims all leading ASCII whitespaces from the buffer.
        
        :param value: The ASCII buffer.
        :returns: The Range of the untrimmed data.
        """
        ...

    @staticmethod
    @overload
    def trim_start(value: System.ReadOnlySpan[str]) -> System.Range:
        ...


class CompositeFormat(System.Object):
    """Represents a parsed composite format string."""

    @property
    def format(self) -> str:
        """Gets the original composite format string used to create this CompositeFormat instance."""
        ...

    @property
    def minimum_argument_count(self) -> int:
        """Gets the minimum number of arguments that must be passed to a formatting operation using this CompositeFormat."""
        ...

    @staticmethod
    def parse(format: str) -> System.Text.CompositeFormat:
        """
        Parse the composite format string .
        
        :param format: The string to parse.
        :returns: The parsed CompositeFormat.
        """
        ...


class StringBuilder(System.Object, System.Runtime.Serialization.ISerializable):
    """This class has no documentation."""

    class ChunkEnumerator:
        """
        ChunkEnumerator supports both the IEnumerable and IEnumerator pattern so foreach
        works (see GetChunks).  It needs to be public (so the compiler can use it
        when building a foreach statement) but users typically don't use it explicitly.
        (which is why it is a nested type).
        """

        @property
        def current(self) -> System.ReadOnlyMemory[str]:
            """Implements the IEnumerator pattern."""
            ...

        def get_enumerator(self) -> System.Text.StringBuilder.ChunkEnumerator:
            """Implement IEnumerable.GetEnumerator() to return  'this' as the IEnumerator"""
            ...

        def move_next(self) -> bool:
            """Implements the IEnumerator pattern."""
            ...

    class AppendInterpolatedStringHandler:
        """Provides a handler used by the language compiler to append interpolated strings into StringBuilder instances."""

        @overload
        def __init__(self, literal_length: int, formatted_count: int, string_builder: System.Text.StringBuilder) -> None:
            """
            Creates a handler used to append an interpolated string into a StringBuilder.
            
            :param literal_length: The number of constant characters outside of interpolation expressions in the interpolated string.
            :param formatted_count: The number of interpolation expressions in the interpolated string.
            :param string_builder: The associated StringBuilder to which to append.
            """
            ...

        @overload
        def __init__(self, literal_length: int, formatted_count: int, string_builder: System.Text.StringBuilder, provider: System.IFormatProvider) -> None:
            """
            Creates a handler used to translate an interpolated string into a string.
            
            :param literal_length: The number of constant characters outside of interpolation expressions in the interpolated string.
            :param formatted_count: The number of interpolation expressions in the interpolated string.
            :param string_builder: The associated StringBuilder to which to append.
            :param provider: An object that supplies culture-specific formatting information.
            """
            ...

        @overload
        def append_formatted(self, value: typing.Any, alignment: int = 0, format: str = None) -> None:
            ...

        @overload
        def append_formatted(self, value: System.ReadOnlySpan[str]) -> None:
            ...

        @overload
        def append_formatted(self, value: System.ReadOnlySpan[str], alignment: int = 0, format: str = None) -> None:
            """
            Writes the specified string of chars to the handler.
            
            :param value: The span to write.
            :param alignment: Minimum number of characters that should be written for this value.  If the value is negative, it indicates left-aligned and the required minimum is the absolute value.
            :param format: The format string.
            """
            ...

        @overload
        def append_formatted(self, value: str) -> None:
            ...

        @overload
        def append_formatted(self, value: str, alignment: int = 0, format: str = None) -> None:
            """
            Writes the specified value to the handler.
            
            :param value: The value to write.
            :param alignment: Minimum number of characters that should be written for this value.  If the value is negative, it indicates left-aligned and the required minimum is the absolute value.
            :param format: The format string.
            """
            ...

        def append_literal(self, value: str) -> None:
            """
            Writes the specified string to the handler.
            
            :param value: The string to write.
            """
            ...

    @property
    def capacity(self) -> int:
        ...

    @capacity.setter
    def capacity(self, value: int) -> None:
        ...

    @property
    def max_capacity(self) -> int:
        """Gets the maximum capacity this builder is allowed to have."""
        ...

    @property
    def length(self) -> int:
        """Gets or sets the length of this builder."""
        ...

    @length.setter
    def length(self, value: int) -> None:
        ...

    def __getitem__(self, index: int) -> str:
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the StringBuilder class."""
        ...

    @overload
    def __init__(self, capacity: int) -> None:
        """
        Initializes a new instance of the StringBuilder class.
        
        :param capacity: The initial capacity of this builder.
        """
        ...

    @overload
    def __init__(self, value: str) -> None:
        """
        Initializes a new instance of the StringBuilder class.
        
        :param value: The initial contents of this builder.
        """
        ...

    @overload
    def __init__(self, value: str, capacity: int) -> None:
        """
        Initializes a new instance of the StringBuilder class.
        
        :param value: The initial contents of this builder.
        :param capacity: The initial capacity of this builder.
        """
        ...

    @overload
    def __init__(self, value: str, start_index: int, length: int, capacity: int) -> None:
        """
        Initializes a new instance of the StringBuilder class.
        
        :param value: The initial contents of this builder.
        :param start_index: The index to start in .
        :param length: The number of characters to read in .
        :param capacity: The initial capacity of this builder.
        """
        ...

    @overload
    def __init__(self, capacity: int, max_capacity: int) -> None:
        """
        Initializes a new instance of the StringBuilder class.
        
        :param capacity: The initial capacity of this builder.
        :param max_capacity: The maximum capacity of this builder.
        """
        ...

    def __setitem__(self, index: int, value: str) -> None:
        ...

    @overload
    def append(self, value: typing.Any) -> System.Text.StringBuilder:
        ...

    @overload
    def append(self, value: typing.Any, value_count: int) -> System.Text.StringBuilder:
        """
        Appends a character buffer to this builder.
        
        :param value: The pointer to the start of the buffer.
        :param value_count: The number of characters in the buffer.
        """
        ...

    @overload
    def append(self, value: str, repeat_count: int) -> System.Text.StringBuilder:
        """
        Appends a character 0 or more times to the end of this builder.
        
        :param value: The character to append.
        :param repeat_count: The number of times to append .
        """
        ...

    @overload
    def append(self, value: typing.List[str], start_index: int, char_count: int) -> System.Text.StringBuilder:
        """
        Appends a range of characters to the end of this builder.
        
        :param value: The characters to append.
        :param start_index: The index to start in .
        :param char_count: The number of characters to read in .
        """
        ...

    @overload
    def append(self, value: str) -> System.Text.StringBuilder:
        """
        Appends a string to the end of this builder.
        
        :param value: The string to append.
        """
        ...

    @overload
    def append(self, value: str, start_index: int, count: int) -> System.Text.StringBuilder:
        """
        Appends part of a string to the end of this builder.
        
        :param value: The string to append.
        :param start_index: The index to start in .
        :param count: The number of characters to read in .
        """
        ...

    @overload
    def append(self, value: System.Text.StringBuilder) -> System.Text.StringBuilder:
        ...

    @overload
    def append(self, value: System.Text.StringBuilder, start_index: int, count: int) -> System.Text.StringBuilder:
        ...

    @overload
    def append(self, value: bool) -> System.Text.StringBuilder:
        ...

    @overload
    def append(self, value: int) -> System.Text.StringBuilder:
        ...

    @overload
    def append(self, value: float) -> System.Text.StringBuilder:
        ...

    @overload
    def append(self, value: typing.List[str]) -> System.Text.StringBuilder:
        ...

    @overload
    def append(self, value: System.ReadOnlySpan[str]) -> System.Text.StringBuilder:
        ...

    @overload
    def append(self, value: System.ReadOnlyMemory[str]) -> System.Text.StringBuilder:
        ...

    @overload
    def append(self, handler: System.Text.StringBuilder.AppendInterpolatedStringHandler) -> System.Text.StringBuilder:
        """
        Appends the specified interpolated string to this instance.
        
        :param handler: The interpolated string to append.
        :returns: A reference to this instance after the append operation has completed.
        """
        ...

    @overload
    def append(self, provider: System.IFormatProvider, handler: System.Text.StringBuilder.AppendInterpolatedStringHandler) -> System.Text.StringBuilder:
        """
        Appends the specified interpolated string to this instance.
        
        :param provider: An object that supplies culture-specific formatting information.
        :param handler: The interpolated string to append.
        :returns: A reference to this instance after the append operation has completed.
        """
        ...

    @overload
    def append_format(self, format: str, arg_0: typing.Any) -> System.Text.StringBuilder:
        ...

    @overload
    def append_format(self, format: str, arg_0: typing.Any, arg_1: typing.Any) -> System.Text.StringBuilder:
        ...

    @overload
    def append_format(self, format: str, arg_0: typing.Any, arg_1: typing.Any, arg_2: typing.Any) -> System.Text.StringBuilder:
        ...

    @overload
    def append_format(self, provider: System.IFormatProvider, format: str, arg_0: typing.Any) -> System.Text.StringBuilder:
        ...

    @overload
    def append_format(self, provider: System.IFormatProvider, format: str, arg_0: typing.Any, arg_1: typing.Any) -> System.Text.StringBuilder:
        ...

    @overload
    def append_format(self, provider: System.IFormatProvider, format: str, arg_0: typing.Any, arg_1: typing.Any, arg_2: typing.Any) -> System.Text.StringBuilder:
        ...

    @overload
    def append_format(self, format: str, *args: typing.Union[System.Object, typing.Iterable[System.Object]]) -> System.Text.StringBuilder:
        ...

    @overload
    def append_format(self, provider: System.IFormatProvider, format: str, *args: typing.Union[System.Object, typing.Iterable[System.Object]]) -> System.Text.StringBuilder:
        ...

    @overload
    def append_format(self, provider: System.IFormatProvider, format: System.Text.CompositeFormat, *args: typing.Union[System.Object, typing.Iterable[System.Object]]) -> System.Text.StringBuilder:
        """
        Appends the string returned by processing a composite format string, which contains zero or more format items, to this instance.
        Each format item is replaced by the string representation of any of the arguments using a specified format provider.
        
        :param provider: An object that supplies culture-specific formatting information.
        :param format: A CompositeFormat.
        :param args: An array of objects to format.
        :returns: A reference to this instance after the append operation has completed.
        """
        ...

    @overload
    def append_join(self, separator: str, *values: typing.Union[System.Object, typing.Iterable[System.Object]]) -> System.Text.StringBuilder:
        ...

    @overload
    def append_join(self, separator: str, *values: typing.Union[str, typing.Iterable[str]]) -> System.Text.StringBuilder:
        ...

    @overload
    def append_line(self) -> System.Text.StringBuilder:
        ...

    @overload
    def append_line(self, value: str) -> System.Text.StringBuilder:
        ...

    @overload
    def append_line(self, handler: System.Text.StringBuilder.AppendInterpolatedStringHandler) -> System.Text.StringBuilder:
        """
        Appends the specified interpolated string followed by the default line terminator to the end of the current StringBuilder object.
        
        :param handler: The interpolated string to append.
        :returns: A reference to this instance after the append operation has completed.
        """
        ...

    @overload
    def append_line(self, provider: System.IFormatProvider, handler: System.Text.StringBuilder.AppendInterpolatedStringHandler) -> System.Text.StringBuilder:
        """
        Appends the specified interpolated string followed by the default line terminator to the end of the current StringBuilder object.
        
        :param provider: An object that supplies culture-specific formatting information.
        :param handler: The interpolated string to append.
        :returns: A reference to this instance after the append operation has completed.
        """
        ...

    def clear(self) -> System.Text.StringBuilder:
        ...

    @overload
    def copy_to(self, source_index: int, destination: typing.List[str], destination_index: int, count: int) -> None:
        ...

    @overload
    def copy_to(self, source_index: int, destination: System.Span[str], count: int) -> None:
        ...

    def ensure_capacity(self, capacity: int) -> int:
        """
        Ensures that the capacity of this builder is at least the specified value.
        
        :param capacity: The new capacity for this builder.
        """
        ...

    @overload
    def equals(self, sb: System.Text.StringBuilder) -> bool:
        """
        Determines if the contents of this builder are equal to the contents of another builder.
        
        :param sb: The other builder.
        """
        ...

    @overload
    def equals(self, span: System.ReadOnlySpan[str]) -> bool:
        """
        Determines if the contents of this builder are equal to the contents of ReadOnlySpan{Char}.
        
        :param span: The ReadOnlySpan{Char}.
        """
        ...

    def get_chunks(self) -> System.Text.StringBuilder.ChunkEnumerator:
        """
        GetChunks returns ChunkEnumerator that follows the IEnumerable pattern and
        thus can be used in a C# 'foreach' statements to retrieve the data in the StringBuilder
        as chunks (ReadOnlyMemory) of characters.  An example use is:
        
             foreach (ReadOnlyMemory<char> chunk in sb.GetChunks())
                foreach (char c in chunk.Span)
                    { /* operation on c }
        
        It is undefined what happens if the StringBuilder is modified while the chunk
        enumeration is incomplete.  StringBuilder is also not thread-safe, so operating
        on it with concurrent threads is illegal.  Finally the ReadOnlyMemory chunks returned
        are NOT guaranteed to remain unchanged if the StringBuilder is modified, so do
        not cache them for later use either.  This API's purpose is efficiently extracting
        the data of a CONSTANT StringBuilder.
        
        Creating a ReadOnlySpan from a ReadOnlyMemory  (the .Span property) is expensive
        compared to the fetching of the character, so create a local variable for the SPAN
        if you need to use it in a nested for statement.  For example
        
           foreach (ReadOnlyMemory<char> chunk in sb.GetChunks())
           {
                var span = chunk.Span;
                for (int i = 0; i < span.Length; i++)
                    { /* operation on span[i] */ }
           }
        """
        ...

    @overload
    def insert(self, index: int, value: typing.Any) -> System.Text.StringBuilder:
        ...

    @overload
    def insert(self, index: int, value: str, count: int) -> System.Text.StringBuilder:
        """
        Inserts a string 0 or more times into this builder at the specified position.
        
        :param index: The index to insert in this builder.
        :param value: The string to insert.
        :param count: The number of times to insert the string.
        """
        ...

    @overload
    def insert(self, index: int, value: str) -> System.Text.StringBuilder:
        ...

    @overload
    def insert(self, index: int, value: bool) -> System.Text.StringBuilder:
        ...

    @overload
    def insert(self, index: int, value: int) -> System.Text.StringBuilder:
        ...

    @overload
    def insert(self, index: int, value: typing.List[str]) -> System.Text.StringBuilder:
        ...

    @overload
    def insert(self, index: int, value: typing.List[str], start_index: int, char_count: int) -> System.Text.StringBuilder:
        ...

    @overload
    def insert(self, index: int, value: float) -> System.Text.StringBuilder:
        ...

    @overload
    def insert(self, index: int, value: System.ReadOnlySpan[str]) -> System.Text.StringBuilder:
        ...

    def remove(self, start_index: int, length: int) -> System.Text.StringBuilder:
        """Removes a range of characters from this builder."""
        ...

    @overload
    def replace(self, old_value: str, new_value: str) -> System.Text.StringBuilder:
        """
        Replaces all instances of one string with another in this builder.
        
        :param old_value: The string to replace.
        :param new_value: The string to replace  with.
        """
        ...

    @overload
    def replace(self, old_value: System.ReadOnlySpan[str], new_value: System.ReadOnlySpan[str]) -> System.Text.StringBuilder:
        """
        Replaces all instances of one read-only character span with another in this builder.
        
        :param old_value: The read-only character span to replace.
        :param new_value: The read-only character span to replace  with.
        """
        ...

    @overload
    def replace(self, old_value: str, new_value: str, start_index: int, count: int) -> System.Text.StringBuilder:
        """
        Replaces all instances of one string with another in part of this builder.
        
        :param old_value: The string to replace.
        :param new_value: The string to replace  with.
        :param start_index: The index to start in this builder.
        :param count: The number of characters to read in this builder.
        """
        ...

    @overload
    def replace(self, old_value: System.ReadOnlySpan[str], new_value: System.ReadOnlySpan[str], start_index: int, count: int) -> System.Text.StringBuilder:
        """
        Replaces all instances of one read-only character span with another in part of this builder.
        
        :param old_value: The read-only character span to replace.
        :param new_value: The read-only character span to replace  with.
        :param start_index: The index to start in this builder.
        :param count: The number of characters to read in this builder.
        """
        ...

    @overload
    def replace(self, old_char: str, new_char: str) -> System.Text.StringBuilder:
        """
        Replaces all instances of one character with another in this builder.
        
        :param old_char: The character to replace.
        :param new_char: The character to replace  with.
        """
        ...

    @overload
    def replace(self, old_char: str, new_char: str, start_index: int, count: int) -> System.Text.StringBuilder:
        """
        Replaces all instances of one character with another in this builder.
        
        :param old_char: The character to replace.
        :param new_char: The character to replace  with.
        :param start_index: The index to start in this builder.
        :param count: The number of characters to read in this builder.
        """
        ...

    @overload
    def to_string(self) -> str:
        ...

    @overload
    def to_string(self, start_index: int, length: int) -> str:
        """
        Creates a string from a substring of this builder.
        
        :param start_index: The index to start in this builder.
        :param length: The number of characters to read in this builder.
        """
        ...


class ASCIIEncoding(System.Text.Encoding):
    """This class has no documentation."""

    @property
    def is_single_byte(self) -> bool:
        ...

    def __init__(self) -> None:
        ...

    @overload
    def get_byte_count(self, chars: typing.Any, count: int) -> int:
        ...

    @overload
    def get_byte_count(self, chars: typing.List[str], index: int, count: int) -> int:
        ...

    @overload
    def get_byte_count(self, chars: str) -> int:
        ...

    @overload
    def get_byte_count(self, chars: System.ReadOnlySpan[str]) -> int:
        ...

    @overload
    def get_bytes(self, chars: typing.Any, char_count: int, bytes: typing.Any, byte_count: int) -> int:
        ...

    @overload
    def get_bytes(self, chars: str, char_index: int, char_count: int, bytes: typing.List[int], byte_index: int) -> int:
        ...

    @overload
    def get_bytes(self, chars: typing.List[str], char_index: int, char_count: int, bytes: typing.List[int], byte_index: int) -> int:
        ...

    @overload
    def get_bytes(self, chars: System.ReadOnlySpan[str], bytes: System.Span[int]) -> int:
        ...

    @overload
    def get_char_count(self, bytes: typing.Any, count: int) -> int:
        ...

    @overload
    def get_char_count(self, bytes: typing.List[int], index: int, count: int) -> int:
        ...

    @overload
    def get_char_count(self, bytes: System.ReadOnlySpan[int]) -> int:
        ...

    @overload
    def get_chars(self, bytes: typing.Any, byte_count: int, chars: typing.Any, char_count: int) -> int:
        ...

    @overload
    def get_chars(self, bytes: typing.List[int], byte_index: int, byte_count: int, chars: typing.List[str], char_index: int) -> int:
        ...

    @overload
    def get_chars(self, bytes: System.ReadOnlySpan[int], chars: System.Span[str]) -> int:
        ...

    def get_decoder(self) -> System.Text.Decoder:
        ...

    def get_encoder(self) -> System.Text.Encoder:
        ...

    def get_max_byte_count(self, char_count: int) -> int:
        ...

    def get_max_char_count(self, byte_count: int) -> int:
        ...

    def get_string(self, bytes: typing.List[int], byte_index: int, byte_count: int) -> str:
        ...

    def try_get_bytes(self, chars: System.ReadOnlySpan[str], bytes: System.Span[int], bytes_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    def try_get_chars(self, bytes: System.ReadOnlySpan[int], chars: System.Span[str], chars_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...


class UTF8Encoding(System.Text.Encoding):
    """This class has no documentation."""

    @property
    def preamble(self) -> System.ReadOnlySpan[int]:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, encoder_should_emit_utf_8_identifier: bool) -> None:
        ...

    @overload
    def __init__(self, encoder_should_emit_utf_8_identifier: bool, throw_on_invalid_bytes: bool) -> None:
        ...

    def equals(self, value: typing.Any) -> bool:
        ...

    @overload
    def get_byte_count(self, chars: typing.Any, count: int) -> int:
        ...

    @overload
    def get_byte_count(self, chars: typing.List[str], index: int, count: int) -> int:
        ...

    @overload
    def get_byte_count(self, chars: str) -> int:
        ...

    @overload
    def get_byte_count(self, chars: System.ReadOnlySpan[str]) -> int:
        ...

    @overload
    def get_bytes(self, chars: typing.Any, char_count: int, bytes: typing.Any, byte_count: int) -> int:
        ...

    @overload
    def get_bytes(self, s: str, char_index: int, char_count: int, bytes: typing.List[int], byte_index: int) -> int:
        ...

    @overload
    def get_bytes(self, chars: typing.List[str], char_index: int, char_count: int, bytes: typing.List[int], byte_index: int) -> int:
        ...

    @overload
    def get_bytes(self, chars: System.ReadOnlySpan[str], bytes: System.Span[int]) -> int:
        ...

    @overload
    def get_char_count(self, bytes: typing.Any, count: int) -> int:
        ...

    @overload
    def get_char_count(self, bytes: typing.List[int], index: int, count: int) -> int:
        ...

    @overload
    def get_char_count(self, bytes: System.ReadOnlySpan[int]) -> int:
        ...

    @overload
    def get_chars(self, bytes: typing.Any, byte_count: int, chars: typing.Any, char_count: int) -> int:
        ...

    @overload
    def get_chars(self, bytes: typing.List[int], byte_index: int, byte_count: int, chars: typing.List[str], char_index: int) -> int:
        ...

    @overload
    def get_chars(self, bytes: System.ReadOnlySpan[int], chars: System.Span[str]) -> int:
        ...

    def get_decoder(self) -> System.Text.Decoder:
        ...

    def get_encoder(self) -> System.Text.Encoder:
        ...

    def get_hash_code(self) -> int:
        ...

    def get_max_byte_count(self, char_count: int) -> int:
        ...

    def get_max_char_count(self, byte_count: int) -> int:
        ...

    def get_preamble(self) -> typing.List[int]:
        ...

    def get_string(self, bytes: typing.List[int], index: int, count: int) -> str:
        ...

    def try_get_bytes(self, chars: System.ReadOnlySpan[str], bytes: System.Span[int], bytes_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    def try_get_chars(self, bytes: System.ReadOnlySpan[int], chars: System.Span[str], chars_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...


class UTF7Encoding(System.Text.Encoding):
    """This class has no documentation."""

    @overload
    def __init__(self) -> None:
        """Obsoletions.SystemTextEncodingUTF7Message"""
        ...

    @overload
    def __init__(self, allow_optionals: bool) -> None:
        """Obsoletions.SystemTextEncodingUTF7Message"""
        ...

    def equals(self, value: typing.Any) -> bool:
        ...

    @overload
    def get_byte_count(self, chars: typing.Any, count: int) -> int:
        ...

    @overload
    def get_byte_count(self, chars: typing.List[str], index: int, count: int) -> int:
        ...

    @overload
    def get_byte_count(self, s: str) -> int:
        ...

    @overload
    def get_bytes(self, chars: typing.Any, char_count: int, bytes: typing.Any, byte_count: int) -> int:
        ...

    @overload
    def get_bytes(self, s: str, char_index: int, char_count: int, bytes: typing.List[int], byte_index: int) -> int:
        ...

    @overload
    def get_bytes(self, chars: typing.List[str], char_index: int, char_count: int, bytes: typing.List[int], byte_index: int) -> int:
        ...

    @overload
    def get_char_count(self, bytes: typing.Any, count: int) -> int:
        ...

    @overload
    def get_char_count(self, bytes: typing.List[int], index: int, count: int) -> int:
        ...

    @overload
    def get_chars(self, bytes: typing.Any, byte_count: int, chars: typing.Any, char_count: int) -> int:
        ...

    @overload
    def get_chars(self, bytes: typing.List[int], byte_index: int, byte_count: int, chars: typing.List[str], char_index: int) -> int:
        ...

    def get_decoder(self) -> System.Text.Decoder:
        ...

    def get_encoder(self) -> System.Text.Encoder:
        ...

    def get_hash_code(self) -> int:
        ...

    def get_max_byte_count(self, char_count: int) -> int:
        ...

    def get_max_char_count(self, byte_count: int) -> int:
        ...

    def get_string(self, bytes: typing.List[int], index: int, count: int) -> str:
        ...


class SpanLineEnumerator:
    """Enumerates the lines of a ReadOnlySpan{Char}."""

    @property
    def current(self) -> System.ReadOnlySpan[str]:
        """Gets the line at the current position of the enumerator."""
        ...

    def get_enumerator(self) -> System.Text.SpanLineEnumerator:
        """Returns this instance as an enumerator."""
        ...

    def move_next(self) -> bool:
        """
        Advances the enumerator to the next line of the span.
        
        :returns: True if the enumerator successfully advanced to the next line; false if the enumerator has advanced past the end of the span.
        """
        ...


class UTF32Encoding(System.Text.Encoding):
    """This class has no documentation."""

    @property
    def preamble(self) -> System.ReadOnlySpan[int]:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, big_endian: bool, byte_order_mark: bool) -> None:
        ...

    @overload
    def __init__(self, big_endian: bool, byte_order_mark: bool, throw_on_invalid_characters: bool) -> None:
        ...

    def equals(self, value: typing.Any) -> bool:
        ...

    @overload
    def get_byte_count(self, chars: typing.Any, count: int) -> int:
        ...

    @overload
    def get_byte_count(self, chars: typing.List[str], index: int, count: int) -> int:
        ...

    @overload
    def get_byte_count(self, s: str) -> int:
        ...

    @overload
    def get_bytes(self, chars: typing.Any, char_count: int, bytes: typing.Any, byte_count: int) -> int:
        ...

    @overload
    def get_bytes(self, s: str, char_index: int, char_count: int, bytes: typing.List[int], byte_index: int) -> int:
        ...

    @overload
    def get_bytes(self, chars: typing.List[str], char_index: int, char_count: int, bytes: typing.List[int], byte_index: int) -> int:
        ...

    @overload
    def get_char_count(self, bytes: typing.Any, count: int) -> int:
        ...

    @overload
    def get_char_count(self, bytes: typing.List[int], index: int, count: int) -> int:
        ...

    @overload
    def get_chars(self, bytes: typing.Any, byte_count: int, chars: typing.Any, char_count: int) -> int:
        ...

    @overload
    def get_chars(self, bytes: typing.List[int], byte_index: int, byte_count: int, chars: typing.List[str], char_index: int) -> int:
        ...

    def get_decoder(self) -> System.Text.Decoder:
        ...

    def get_encoder(self) -> System.Text.Encoder:
        ...

    def get_hash_code(self) -> int:
        ...

    def get_max_byte_count(self, char_count: int) -> int:
        ...

    def get_max_char_count(self, byte_count: int) -> int:
        ...

    def get_preamble(self) -> typing.List[int]:
        ...

    def get_string(self, bytes: typing.List[int], index: int, count: int) -> str:
        ...


class SpanRuneEnumerator:
    """This class has no documentation."""

    @property
    def current(self) -> System.Text.Rune:
        ...

    def get_enumerator(self) -> System.Text.SpanRuneEnumerator:
        ...

    def move_next(self) -> bool:
        ...


class EncoderReplacementFallback(System.Text.EncoderFallback):
    """This class has no documentation."""

    @property
    def default_string(self) -> str:
        ...

    @property
    def max_char_count(self) -> int:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, replacement: str) -> None:
        ...

    def create_fallback_buffer(self) -> System.Text.EncoderFallbackBuffer:
        ...

    def equals(self, value: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...


class EncoderReplacementFallbackBuffer(System.Text.EncoderFallbackBuffer):
    """This class has no documentation."""

    @property
    def remaining(self) -> int:
        ...

    def __init__(self, fallback: System.Text.EncoderReplacementFallback) -> None:
        ...

    @overload
    def fallback(self, char_unknown: str, index: int) -> bool:
        ...

    @overload
    def fallback(self, char_unknown_high: str, char_unknown_low: str, index: int) -> bool:
        ...

    def get_next_char(self) -> str:
        ...

    def move_previous(self) -> bool:
        ...

    def reset(self) -> None:
        ...


class DecoderReplacementFallback(System.Text.DecoderFallback):
    """This class has no documentation."""

    @property
    def default_string(self) -> str:
        ...

    @property
    def max_char_count(self) -> int:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, replacement: str) -> None:
        ...

    def create_fallback_buffer(self) -> System.Text.DecoderFallbackBuffer:
        ...

    def equals(self, value: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...


class DecoderReplacementFallbackBuffer(System.Text.DecoderFallbackBuffer):
    """This class has no documentation."""

    @property
    def remaining(self) -> int:
        ...

    def __init__(self, fallback: System.Text.DecoderReplacementFallback) -> None:
        ...

    def fallback(self, bytes_unknown: typing.List[int], index: int) -> bool:
        ...

    def get_next_char(self) -> str:
        ...

    def move_previous(self) -> bool:
        ...

    def reset(self) -> None:
        ...


class DecoderExceptionFallback(System.Text.DecoderFallback):
    """This class has no documentation."""

    @property
    def max_char_count(self) -> int:
        ...

    def create_fallback_buffer(self) -> System.Text.DecoderFallbackBuffer:
        ...

    def equals(self, value: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...


class DecoderExceptionFallbackBuffer(System.Text.DecoderFallbackBuffer):
    """This class has no documentation."""

    @property
    def remaining(self) -> int:
        ...

    def fallback(self, bytes_unknown: typing.List[int], index: int) -> bool:
        ...

    def get_next_char(self) -> str:
        ...

    def move_previous(self) -> bool:
        ...


class DecoderFallbackException(System.ArgumentException):
    """This class has no documentation."""

    @property
    def bytes_unknown(self) -> typing.List[int]:
        ...

    @property
    def index(self) -> int:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, message: str) -> None:
        ...

    @overload
    def __init__(self, message: str, inner_exception: System.Exception) -> None:
        ...

    @overload
    def __init__(self, message: str, bytes_unknown: typing.List[int], index: int) -> None:
        ...


class EncoderExceptionFallback(System.Text.EncoderFallback):
    """This class has no documentation."""

    @property
    def max_char_count(self) -> int:
        ...

    def __init__(self) -> None:
        ...

    def create_fallback_buffer(self) -> System.Text.EncoderFallbackBuffer:
        ...

    def equals(self, value: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...


class EncoderExceptionFallbackBuffer(System.Text.EncoderFallbackBuffer):
    """This class has no documentation."""

    @property
    def remaining(self) -> int:
        ...

    def __init__(self) -> None:
        ...

    @overload
    def fallback(self, char_unknown: str, index: int) -> bool:
        ...

    @overload
    def fallback(self, char_unknown_high: str, char_unknown_low: str, index: int) -> bool:
        ...

    def get_next_char(self) -> str:
        ...

    def move_previous(self) -> bool:
        ...


class EncoderFallbackException(System.ArgumentException):
    """This class has no documentation."""

    @property
    def char_unknown(self) -> str:
        ...

    @property
    def char_unknown_high(self) -> str:
        ...

    @property
    def char_unknown_low(self) -> str:
        ...

    @property
    def index(self) -> int:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, message: str) -> None:
        ...

    @overload
    def __init__(self, message: str, inner_exception: System.Exception) -> None:
        ...

    def is_unknown_surrogate(self) -> bool:
        ...


class StringRuneEnumerator(System.Collections.Generic.IEnumerable[System.Text.Rune], System.Collections.Generic.IEnumerator[System.Text.Rune], typing.Iterable[System.Text.Rune]):
    """This class has no documentation."""

    @property
    def current(self) -> System.Text.Rune:
        ...

    def __iter__(self) -> typing.Iterator[System.Text.Rune]:
        ...

    def get_enumerator(self) -> System.Text.StringRuneEnumerator:
        ...

    def move_next(self) -> bool:
        ...


