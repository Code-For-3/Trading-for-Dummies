from typing import overload
from enum import Enum
import datetime
import typing

import System
import System.Buffers
import System.Buffers.Text


class Base64(System.Object):
    """Convert between binary data and UTF-8 encoded text that is represented in base 64."""

    @staticmethod
    def decode_from_utf_8(utf_8: System.ReadOnlySpan[int], bytes: System.Span[int], bytes_consumed: typing.Optional[int], bytes_written: typing.Optional[int], is_final_block: bool = True) -> typing.Tuple[System.Buffers.OperationStatus, int, int]:
        """
        Decode the span of UTF-8 encoded text represented as base64 into binary data.
        If the input is not a multiple of 4, it will decode as much as it can, to the closest multiple of 4.
        
        :param utf_8: The input span which contains UTF-8 encoded text in base64 that needs to be decoded.
        :param bytes: The output span which contains the result of the operation, i.e. the decoded binary data.
        :param bytes_consumed: The number of input bytes consumed during the operation. This can be used to slice the input for subsequent calls, if necessary.
        :param bytes_written: The number of bytes written into the output span. This can be used to slice the output for subsequent calls, if necessary.
        :param is_final_block: true (default) when the input span contains the entire data to decode. Set to true when the source buffer contains the entirety of the data to decode. Set to false if this method is being called in a loop and if more input data may follow. At the end of the loop, call this (potentially with an empty source buffer) passing true.
        :returns: It returns the OperationStatus enum values: - Done - on successful processing of the entire input span - DestinationTooSmall - if there is not enough space in the output span to fit the decoded input - NeedMoreData - only if  is false and the input is not a multiple of 4, otherwise the partial input would be considered as InvalidData - InvalidData - if the input contains bytes outside of the expected base64 range, or if it contains invalid/more than two padding characters,   or if the input is incomplete (i.e. not a multiple of 4) and  is true.
        """
        ...

    @staticmethod
    def decode_from_utf_8_in_place(buffer: System.Span[int], bytes_written: typing.Optional[int]) -> typing.Tuple[System.Buffers.OperationStatus, int]:
        """
        Decode the span of UTF-8 encoded text in base 64 (in-place) into binary data.
        The decoded binary output is smaller than the text data contained in the input (the operation deflates the data).
        If the input is not a multiple of 4, it will not decode any.
        
        :param buffer: The input span which contains the base 64 text data that needs to be decoded.
        :param bytes_written: The number of bytes written into the buffer.
        :returns: It returns the OperationStatus enum values: - Done - on successful processing of the entire input span - InvalidData - if the input contains bytes outside of the expected base 64 range, or if it contains invalid/more than two padding characters,   or if the input is incomplete (i.e. not a multiple of 4). It does not return DestinationTooSmall since that is not possible for base 64 decoding. It does not return NeedMoreData since this method tramples the data in the buffer and hence can only be called once with all the data in the buffer.
        """
        ...

    @staticmethod
    def encode_to_utf_8(bytes: System.ReadOnlySpan[int], utf_8: System.Span[int], bytes_consumed: typing.Optional[int], bytes_written: typing.Optional[int], is_final_block: bool = True) -> typing.Tuple[System.Buffers.OperationStatus, int, int]:
        """
        Encode the span of binary data into UTF-8 encoded text represented as base64.
        
        :param bytes: The input span which contains binary data that needs to be encoded.
        :param utf_8: The output span which contains the result of the operation, i.e. the UTF-8 encoded text in base64.
        :param bytes_consumed: The number of input bytes consumed during the operation. This can be used to slice the input for subsequent calls, if necessary.
        :param bytes_written: The number of bytes written into the output span. This can be used to slice the output for subsequent calls, if necessary.
        :param is_final_block: true (default) when the input span contains the entire data to encode. Set to true when the source buffer contains the entirety of the data to encode. Set to false if this method is being called in a loop and if more input data may follow. At the end of the loop, call this (potentially with an empty source buffer) passing true.
        :returns: It returns the OperationStatus enum values: - Done - on successful processing of the entire input span - DestinationTooSmall - if there is not enough space in the output span to fit the encoded input - NeedMoreData - only if  is false, otherwise the output is padded if the input is not a multiple of 3 It does not return InvalidData since that is not possible for base64 encoding.
        """
        ...

    @staticmethod
    def encode_to_utf_8_in_place(buffer: System.Span[int], data_length: int, bytes_written: typing.Optional[int]) -> typing.Tuple[System.Buffers.OperationStatus, int]:
        """
        Encode the span of binary data (in-place) into UTF-8 encoded text represented as base 64.
        The encoded text output is larger than the binary data contained in the input (the operation inflates the data).
        
        :param buffer: The input span which contains binary data that needs to be encoded. It needs to be large enough to fit the result of the operation.
        :param data_length: The amount of binary data contained within the buffer that needs to be encoded (and needs to be smaller than the buffer length).
        :param bytes_written: The number of bytes written into the buffer.
        :returns: It returns the OperationStatus enum values: - Done - on successful processing of the entire buffer - DestinationTooSmall - if there is not enough space in the buffer beyond data_length to fit the result of encoding the input It does not return NeedMoreData since this method tramples the data in the buffer and hence can only be called once with all the data in the buffer. It does not return InvalidData since that is not possible for base 64 encoding.
        """
        ...

    @staticmethod
    def get_max_decoded_from_utf_8_length(length: int) -> int:
        """Returns the maximum length (in bytes) of the result if you were to decode base 64 encoded text within a byte span of size "length"."""
        ...

    @staticmethod
    def get_max_encoded_to_utf_8_length(length: int) -> int:
        """Returns the maximum length (in bytes) of the result if you were to encode binary data within a byte span of size "length"."""
        ...

    @staticmethod
    @overload
    def is_valid(base_64_text: System.ReadOnlySpan[str]) -> bool:
        """
        Validates that the specified span of text is comprised of valid base-64 encoded data.
        
        :param base_64_text: A span of text to validate.
        :returns: true if  contains a valid, decodable sequence of base-64 encoded data; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def is_valid(base_64_text: System.ReadOnlySpan[str], decoded_length: typing.Optional[int]) -> typing.Tuple[bool, int]:
        """
        Validates that the specified span of text is comprised of valid base-64 encoded data.
        
        :param base_64_text: A span of text to validate.
        :param decoded_length: If the method returns true, the number of decoded bytes that will result from decoding the input text.
        :returns: true if  contains a valid, decodable sequence of base-64 encoded data; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def is_valid(base_64_text_utf_8: System.ReadOnlySpan[int]) -> bool:
        """
        Validates that the specified span of UTF-8 text is comprised of valid base-64 encoded data.
        
        :param base_64_text_utf_8: A span of UTF-8 text to validate.
        :returns: true if  contains a valid, decodable sequence of base-64 encoded data; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def is_valid(base_64_text_utf_8: System.ReadOnlySpan[int], decoded_length: typing.Optional[int]) -> typing.Tuple[bool, int]:
        """
        Validates that the specified span of UTF-8 text is comprised of valid base-64 encoded data.
        
        :param base_64_text_utf_8: A span of UTF-8 text to validate.
        :param decoded_length: If the method returns true, the number of decoded bytes that will result from decoding the input UTF-8 text.
        :returns: true if  contains a valid, decodable sequence of base-64 encoded data; otherwise, false.
        """
        ...


class Utf8Formatter(System.Object):
    """Methods to format common data types as Utf8 strings."""

    @staticmethod
    @overload
    def try_format(value: float, destination: System.Span[int], bytes_written: typing.Optional[int], format: System.Buffers.StandardFormat = ...) -> typing.Tuple[bool, int]:
        """
        Formats a Double as a UTF-8 string.
        
        :param value: Value to format
        :param destination: Buffer to write the UTF-8 formatted value to
        :param bytes_written: Receives the length of the formatted text in bytes
        :param format: The standard format to use
        :returns: true for success. "bytes_written" contains the length of the formatted text in bytes. false if buffer was too short. Iteratively increase the size of the buffer and retry until it succeeds.
        """
        ...

    @staticmethod
    @overload
    def try_format(value: System.Guid, destination: System.Span[int], bytes_written: typing.Optional[int], format: System.Buffers.StandardFormat = ...) -> typing.Tuple[bool, int]:
        """
        Formats a Guid as a UTF-8 string.
        
        :param value: Value to format
        :param destination: Buffer to write the UTF-8 formatted value to
        :param bytes_written: Receives the length of the formatted text in bytes
        :param format: The standard format to use
        :returns: true for success. "bytes_written" contains the length of the formatted text in bytes. false if buffer was too short. Iteratively increase the size of the buffer and retry until it succeeds.
        """
        ...

    @staticmethod
    @overload
    def try_format(value: System.DateTimeOffset, destination: System.Span[int], bytes_written: typing.Optional[int], format: System.Buffers.StandardFormat = ...) -> typing.Tuple[bool, int]:
        """
        Formats a DateTimeOffset as a UTF-8 string.
        
        :param value: Value to format
        :param destination: Buffer to write the UTF-8 formatted value to
        :param bytes_written: Receives the length of the formatted text in bytes
        :param format: The standard format to use
        :returns: true for success. "bytes_written" contains the length of the formatted text in bytes. false if buffer was too short. Iteratively increase the size of the buffer and retry until it succeeds.
        """
        ...

    @staticmethod
    @overload
    def try_format(value: typing.Union[datetime.datetime, datetime.date], destination: System.Span[int], bytes_written: typing.Optional[int], format: System.Buffers.StandardFormat = ...) -> typing.Tuple[bool, int]:
        """
        Formats a DateTime as a UTF-8 string.
        
        :param value: Value to format
        :param destination: Buffer to write the UTF-8 formatted value to
        :param bytes_written: Receives the length of the formatted text in bytes
        :param format: The standard format to use
        :returns: true for success. "bytes_written" contains the length of the formatted text in bytes. false if buffer was too short. Iteratively increase the size of the buffer and retry until it succeeds.
        """
        ...

    @staticmethod
    @overload
    def try_format(value: bool, destination: System.Span[int], bytes_written: typing.Optional[int], format: System.Buffers.StandardFormat = ...) -> typing.Tuple[bool, int]:
        """
        Formats a Boolean as a UTF-8 string.
        
        :param value: Value to format
        :param destination: Buffer to write the UTF-8 formatted value to
        :param bytes_written: Receives the length of the formatted text in bytes
        :param format: The standard format to use
        :returns: true for success. "bytes_written" contains the length of the formatted text in bytes. false if buffer was too short. Iteratively increase the size of the buffer and retry until it succeeds.
        """
        ...

    @staticmethod
    @overload
    def try_format(value: int, destination: System.Span[int], bytes_written: typing.Optional[int], format: System.Buffers.StandardFormat = ...) -> typing.Tuple[bool, int]:
        """
        Formats a Byte as a UTF-8 string.
        
        :param value: Value to format
        :param destination: Buffer to write the UTF-8 formatted value to
        :param bytes_written: Receives the length of the formatted text in bytes
        :param format: The standard format to use
        :returns: true for success. "bytes_written" contains the length of the formatted text in bytes. false if buffer was too short. Iteratively increase the size of the buffer and retry until it succeeds.
        """
        ...

    @staticmethod
    @overload
    def try_format(value: datetime.timedelta, destination: System.Span[int], bytes_written: typing.Optional[int], format: System.Buffers.StandardFormat = ...) -> typing.Tuple[bool, int]:
        """
        Formats a TimeSpan as a UTF-8 string.
        
        :param value: Value to format
        :param destination: Buffer to write the UTF-8 formatted value to
        :param bytes_written: Receives the length of the formatted text in bytes
        :param format: The standard format to use
        :returns: true for success. "bytes_written" contains the length of the formatted text in bytes. false if buffer was too short. Iteratively increase the size of the buffer and retry until it succeeds.
        """
        ...


class Utf8Parser(System.Object):
    """Methods to parse common data types to Utf8 strings."""

    @staticmethod
    @overload
    def try_parse(source: System.ReadOnlySpan[int], value: typing.Optional[float], bytes_consumed: typing.Optional[int], standard_format: str = ...) -> typing.Tuple[bool, float, int]:
        """
        Parses a Single at the start of a Utf8 string.
        
        :param source: The Utf8 string to parse
        :param value: Receives the parsed value
        :param bytes_consumed: On a successful parse, receives the length in bytes of the substring that was parsed
        :param standard_format: Expected format of the Utf8 string
        :returns: true for success. "bytes_consumed" contains the length in bytes of the substring that was parsed. false if the string was not syntactically valid or an overflow or underflow occurred. "bytes_consumed" is set to 0.
        """
        ...

    @staticmethod
    @overload
    def try_parse(source: System.ReadOnlySpan[int], value: typing.Optional[bool], bytes_consumed: typing.Optional[int], standard_format: str = ...) -> typing.Tuple[bool, bool, int]:
        """
        Parses a Boolean at the start of a Utf8 string.
        
        :param source: The Utf8 string to parse
        :param value: Receives the parsed value
        :param bytes_consumed: On a successful parse, receives the length in bytes of the substring that was parsed.
        :param standard_format: Expected format of the Utf8 string. Supported formats are 'G', 'l', and default.
        :returns: true for success. "bytes_consumed" contains the length in bytes of the substring that was parsed. false if the string was not syntactically valid or an overflow or underflow occurred. "bytes_consumed" is set to 0.
        """
        ...

    @staticmethod
    @overload
    def try_parse(source: System.ReadOnlySpan[int], value: typing.Optional[int], bytes_consumed: typing.Optional[int], standard_format: str = ...) -> typing.Tuple[bool, int, int]:
        """
        Parses a Byte at the start of a Utf8 string.
        
        :param source: The Utf8 string to parse
        :param value: Receives the parsed value
        :param bytes_consumed: On a successful parse, receives the length in bytes of the substring that was parsed
        :param standard_format: Expected format of the Utf8 string
        :returns: true for success. "bytes_consumed" contains the length in bytes of the substring that was parsed. false if the string was not syntactically valid or an overflow or underflow occurred. "bytes_consumed" is set to 0.
        """
        ...

    @staticmethod
    @overload
    def try_parse(source: System.ReadOnlySpan[int], value: typing.Optional[typing.Union[datetime.datetime, datetime.date]], bytes_consumed: typing.Optional[int], standard_format: str = ...) -> typing.Tuple[bool, typing.Union[datetime.datetime, datetime.date], int]:
        """
        Parses a DateTime at the start of a Utf8 string.
        
        :param source: The Utf8 string to parse
        :param value: Receives the parsed value
        :param bytes_consumed: On a successful parse, receives the length in bytes of the substring that was parsed
        :param standard_format: Expected format of the Utf8 string
        :returns: true for success. "bytes_consumed" contains the length in bytes of the substring that was parsed. false if the string was not syntactically valid or an overflow or underflow occurred. "bytes_consumed" is set to 0.
        """
        ...

    @staticmethod
    @overload
    def try_parse(source: System.ReadOnlySpan[int], value: typing.Optional[System.DateTimeOffset], bytes_consumed: typing.Optional[int], standard_format: str = ...) -> typing.Tuple[bool, System.DateTimeOffset, int]:
        """
        Parses a DateTimeOffset at the start of a Utf8 string.
        
        :param source: The Utf8 string to parse
        :param value: Receives the parsed value
        :param bytes_consumed: On a successful parse, receives the length in bytes of the substring that was parsed
        :param standard_format: Expected format of the Utf8 string
        :returns: true for success. "bytes_consumed" contains the length in bytes of the substring that was parsed. false if the string was not syntactically valid or an overflow or underflow occurred. "bytes_consumed" is set to 0.
        """
        ...

    @staticmethod
    @overload
    def try_parse(source: System.ReadOnlySpan[int], value: typing.Optional[System.Guid], bytes_consumed: typing.Optional[int], standard_format: str = ...) -> typing.Tuple[bool, System.Guid, int]:
        """
        Parses a Guid at the start of a Utf8 string.
        
        :param source: The Utf8 string to parse
        :param value: Receives the parsed value
        :param bytes_consumed: On a successful parse, receives the length in bytes of the substring that was parsed
        :param standard_format: Expected format of the Utf8 string
        :returns: true for success. "bytes_consumed" contains the length in bytes of the substring that was parsed. false if the string was not syntactically valid or an overflow or underflow occurred. "bytes_consumed" is set to 0.
        """
        ...

    @staticmethod
    @overload
    def try_parse(source: System.ReadOnlySpan[int], value: typing.Optional[datetime.timedelta], bytes_consumed: typing.Optional[int], standard_format: str = ...) -> typing.Tuple[bool, datetime.timedelta, int]:
        """
        Parses a TimeSpan at the start of a Utf8 string.
        
        :param source: The Utf8 string to parse
        :param value: Receives the parsed value
        :param bytes_consumed: On a successful parse, receives the length in bytes of the substring that was parsed
        :param standard_format: Expected format of the Utf8 string
        :returns: true for success. "bytes_consumed" contains the length in bytes of the substring that was parsed. false if the string was not syntactically valid or an overflow or underflow occurred. "bytes_consumed" is set to 0.
        """
        ...


class Base64Url(System.Object):
    """This class has no documentation."""

    @staticmethod
    @overload
    def decode_from_chars(source: System.ReadOnlySpan[str], destination: System.Span[int], chars_consumed: typing.Optional[int], bytes_written: typing.Optional[int], is_final_block: bool = True) -> typing.Tuple[System.Buffers.OperationStatus, int, int]:
        """
        Decodes the span of unicode ASCII chars represented as Base64Url into binary data.
        
        :param source: The input span which contains unicode ASCII chars in Base64Url that needs to be decoded.
        :param destination: The output span which contains the result of the operation, i.e. the decoded binary data.
        :param chars_consumed: When this method returns, contains the number of input chars consumed during the operation. This can be used to slice the input for subsequent calls, if necessary. This parameter is treated as uninitialized.
        :param bytes_written: When this method returns, contains the number of bytes written into the output span. This can be used to slice the output for subsequent calls, if necessary. This parameter is treated as uninitialized.
        :param is_final_block: true when the input span contains the entirety of data to encode; false when more data may follow, such as when calling in a loop. Calls with false should be followed up with another call where this parameter is true call. The default is true.
        :returns: One of the enumeration values that indicates the success or failure of the operation.
        """
        ...

    @staticmethod
    @overload
    def decode_from_chars(source: System.ReadOnlySpan[str], destination: System.Span[int]) -> int:
        """
        Decodes the span of unicode ASCII chars represented as Base64Url into binary data.
        
        :param source: The input span which contains ASCII chars in Base64Url that needs to be decoded.
        :param destination: The output span which contains the result of the operation, i.e. the decoded binary data.
        :returns: The number of bytes written into the output span. This can be used to slice the output for subsequent calls, if necessary.
        """
        ...

    @staticmethod
    @overload
    def decode_from_chars(source: System.ReadOnlySpan[str]) -> typing.List[int]:
        """
        Decodes the span of unicode ASCII chars represented as Base64Url into binary data.
        
        :param source: The input span which contains ASCII chars in Base64Url that needs to be decoded.
        :returns: A byte array which contains the result of the decoding operation.
        """
        ...

    @staticmethod
    @overload
    def decode_from_utf_8(source: System.ReadOnlySpan[int], destination: System.Span[int], bytes_consumed: typing.Optional[int], bytes_written: typing.Optional[int], is_final_block: bool = True) -> typing.Tuple[System.Buffers.OperationStatus, int, int]:
        """
        Decodes the span of UTF-8 encoded text represented as Base64Url into binary data.
        
        :param source: The input span which contains UTF-8 encoded text in Base64Url that needs to be decoded.
        :param destination: The output span which contains the result of the operation, i.e. the decoded binary data.
        :param bytes_consumed: When this method returns, contains the number of input bytes consumed during the operation. This can be used to slice the input for subsequent calls, if necessary. This parameter is treated as uninitialized.
        :param bytes_written: When this method returns, contains the number of bytes written into the output span. This can be used to slice the output for subsequent calls, if necessary. This parameter is treated as uninitialized.
        :param is_final_block: true when the input span contains the entirety of data to encode; false when more data may follow, such as when calling in a loop. Calls with false should be followed up with another call where this parameter is true call. The default is true.
        :returns: One of the enumeration values that indicates the success or failure of the operation.
        """
        ...

    @staticmethod
    @overload
    def decode_from_utf_8(source: System.ReadOnlySpan[int], destination: System.Span[int]) -> int:
        """
        Decodes the span of UTF-8 encoded text represented as Base64Url into binary data.
        
        :param source: The input span which contains UTF-8 encoded text in Base64Url that needs to be decoded.
        :param destination: The output span which contains the result of the operation, i.e. the decoded binary data.
        :returns: The number of bytes written into . This can be used to slice the output for subsequent calls, if necessary.
        """
        ...

    @staticmethod
    @overload
    def decode_from_utf_8(source: System.ReadOnlySpan[int]) -> typing.List[int]:
        """
        Decodes the span of UTF-8 encoded text represented as Base64Url into binary data.
        
        :param source: The input span which contains UTF-8 encoded text in Base64Url that needs to be decoded.
        :returns: >A byte array which contains the result of the decoding operation.
        """
        ...

    @staticmethod
    def decode_from_utf_8_in_place(buffer: System.Span[int]) -> int:
        """
        Decodes the span of UTF-8 encoded text in Base64Url into binary data, in-place.
        The decoded binary output is smaller than the text data contained in the input (the operation deflates the data).
        
        :param buffer: The input span which contains the base 64 text data that needs to be decoded.
        :returns: The number of bytes written into . This can be used to slice the output for subsequent calls, if necessary.
        """
        ...

    @staticmethod
    @overload
    def encode_to_chars(source: System.ReadOnlySpan[int], destination: System.Span[str], bytes_consumed: typing.Optional[int], chars_written: typing.Optional[int], is_final_block: bool = True) -> typing.Tuple[System.Buffers.OperationStatus, int, int]:
        """
        Encodes the span of binary data into unicode ASCII chars represented as Base64Url.
        
        :param source: The input span which contains binary data that needs to be encoded.
        :param destination: The output span which contains the result of the operation, i.e. the ASCII chars in Base64Url.
        :param bytes_consumed: >When this method returns, contains the number of input bytes consumed during the operation. This can be used to slice the input for subsequent calls, if necessary. This parameter is treated as uninitialized.
        :param chars_written: >When this method returns, contains the number of chars written into the output span. This can be used to slice the output for subsequent calls, if necessary. This parameter is treated as uninitialized.
        :param is_final_block: true when the input span contains the entirety of data to encode; false when more data may follow, such as when calling in a loop, subsequent calls with false should end with true call. The default is true.
        :returns: One of the enumeration values that indicates the success or failure of the operation.
        """
        ...

    @staticmethod
    @overload
    def encode_to_chars(source: System.ReadOnlySpan[int], destination: System.Span[str]) -> int:
        """
        Encodes the span of binary data into unicode ASCII chars represented as Base64Url.
        
        :param source: The input span which contains binary data that needs to be encoded.
        :param destination: The output span which contains the result of the operation, i.e. the ASCII chars in Base64Url.
        :returns: The number of bytes written into the destination span. This can be used to slice the output for subsequent calls, if necessary.
        """
        ...

    @staticmethod
    @overload
    def encode_to_chars(source: System.ReadOnlySpan[int]) -> typing.List[str]:
        """
        Encodes the span of binary data into unicode ASCII chars represented as Base64Url.
        
        :param source: The input span which contains binary data that needs to be encoded.
        :returns: A char array which contains the result of the operation, i.e. the ASCII chars in Base64Url.
        """
        ...

    @staticmethod
    def encode_to_string(source: System.ReadOnlySpan[int]) -> str:
        """
        Encodes the span of binary data into unicode string represented as Base64Url ASCII chars.
        
        :param source: The input span which contains binary data that needs to be encoded.
        :returns: A string which contains the result of the operation, i.e. the ASCII string in Base64Url.
        """
        ...

    @staticmethod
    @overload
    def encode_to_utf_8(source: System.ReadOnlySpan[int], destination: System.Span[int], bytes_consumed: typing.Optional[int], bytes_written: typing.Optional[int], is_final_block: bool = True) -> typing.Tuple[System.Buffers.OperationStatus, int, int]:
        """
        Encodes the span of binary data into UTF-8 encoded text represented as Base64Url.
        
        :param source: The input span which contains binary data that needs to be encoded.
        :param destination: The output span which contains the result of the operation, i.e. the UTF-8 encoded text in Base64Url.
        :param bytes_consumed: When this method returns, contains the number of input bytes consumed during the operation. This can be used to slice the input for subsequent calls, if necessary. This parameter is treated as uninitialized.
        :param bytes_written: When this method returns, contains the number of bytes written into the output span. This can be used to slice the output for subsequent calls, if necessary. This parameter is treated as uninitialized.
        :param is_final_block: true when the input span contains the entirety of data to encode; false when more data may follow, such as when calling in a loop, subsequent calls with false should end with true call. The default is true.
        :returns: One of the enumeration values that indicates the success or failure of the operation.
        """
        ...

    @staticmethod
    @overload
    def encode_to_utf_8(source: System.ReadOnlySpan[int], destination: System.Span[int]) -> int:
        """
        Encodes the span of binary data into UTF-8 encoded text represented as Base64Url.
        
        :param source: The input span which contains binary data that needs to be encoded.
        :param destination: The output span which contains the result of the operation, i.e. the UTF-8 encoded text in Base64Url.
        :returns: The number of bytes written into the destination span. This can be used to slice the output for subsequent calls, if necessary.
        """
        ...

    @staticmethod
    @overload
    def encode_to_utf_8(source: System.ReadOnlySpan[int]) -> typing.List[int]:
        """
        Encodes the span of binary data into UTF-8 encoded text represented as Base64Url.
        
        :param source: The input span which contains binary data that needs to be encoded.
        :returns: The output byte array which contains the result of the operation, i.e. the UTF-8 encoded text in Base64Url.
        """
        ...

    @staticmethod
    def get_encoded_length(bytes_length: int) -> int:
        """Returns the length (in bytes) of the result if you were to encode binary data within a byte span of size ."""
        ...

    @staticmethod
    def get_max_decoded_length(base_64_length: int) -> int:
        """Returns the maximum length (in bytes) of the result if you were to decode base 64 encoded text from a span of size ."""
        ...

    @staticmethod
    @overload
    def is_valid(base_64_url_text: System.ReadOnlySpan[str]) -> bool:
        """
        Validates that the specified span of text is comprised of valid base-64 encoded data.
        
        :param base_64_url_text: A span of text to validate.
        :returns: true if  contains a valid, decodable sequence of base-64 encoded data; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def is_valid(base_64_url_text: System.ReadOnlySpan[str], decoded_length: typing.Optional[int]) -> typing.Tuple[bool, int]:
        """
        Validates that the specified span of text is comprised of valid base-64 encoded data.
        
        :param base_64_url_text: A span of text to validate.
        :param decoded_length: If the method returns true, the number of decoded bytes that will result from decoding the input text.
        :returns: true if  contains a valid, decodable sequence of base-64 encoded data; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def is_valid(utf_8_base_64_url_text: System.ReadOnlySpan[int]) -> bool:
        """
        Validates that the specified span of UTF-8 text is comprised of valid base-64 encoded data.
        
        :param utf_8_base_64_url_text: A span of UTF-8 text to validate.
        :returns: true if  contains a valid, decodable sequence of base-64 encoded data; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def is_valid(utf_8_base_64_url_text: System.ReadOnlySpan[int], decoded_length: typing.Optional[int]) -> typing.Tuple[bool, int]:
        """
        Validates that the specified span of UTF-8 text is comprised of valid base-64 encoded data.
        
        :param utf_8_base_64_url_text: A span of UTF-8 text to validate.
        :param decoded_length: If the method returns true, the number of decoded bytes that will result from decoding the input UTF-8 text.
        :returns: true if  contains a valid, decodable sequence of base-64 encoded data; otherwise, false.
        """
        ...

    @staticmethod
    def try_decode_from_chars(source: System.ReadOnlySpan[str], destination: System.Span[int], bytes_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        """
        Decodes the span of unicode ASCII chars represented as Base64Url into binary data.
        
        :param source: The input span which contains ASCII chars in Base64Url that needs to be decoded.
        :param destination: The output span which contains the result of the operation, i.e. the decoded binary data.
        :param bytes_written: When this method returns, contains the number of bytes written into the output span. This can be used to slice the output for subsequent calls, if necessary. This parameter is treated as uninitialized.
        :returns: true if bytes decoded successfully, otherwise false.
        """
        ...

    @staticmethod
    def try_decode_from_utf_8(source: System.ReadOnlySpan[int], destination: System.Span[int], bytes_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        """
        Decodes the span of UTF-8 encoded text represented as Base64Url into binary data.
        
        :param source: The input span which contains UTF-8 encoded text in Base64Url that needs to be decoded.
        :param destination: The output span which contains the result of the operation, i.e. the decoded binary data.
        :param bytes_written: When this method returns, contains the number of bytes written into the output span. This can be used to slice the output for subsequent calls, if necessary. This parameter is treated as uninitialized.
        :returns: true if bytes decoded successfully, otherwise false.
        """
        ...

    @staticmethod
    def try_encode_to_chars(source: System.ReadOnlySpan[int], destination: System.Span[str], chars_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        """
        Encodes the span of binary data into unicode ASCII chars represented as Base64Url.
        
        :param source: The input span which contains binary data that needs to be encoded.
        :param destination: The output span which contains the result of the operation, i.e. the ASCII chars in Base64Url.
        :param chars_written: When this method returns, contains the number of chars written into the output span. This can be used to slice the output for subsequent calls, if necessary. This parameter is treated as uninitialized.
        :returns: true if chars encoded successfully, otherwise false.
        """
        ...

    @staticmethod
    def try_encode_to_utf_8(source: System.ReadOnlySpan[int], destination: System.Span[int], bytes_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        """
        Encodes the span of binary data into UTF-8 encoded chars represented as Base64Url.
        
        :param source: The input span which contains binary data that needs to be encoded.
        :param destination: The output span which contains the result of the operation, i.e. the UTF-8 encoded text in Base64Url.
        :param bytes_written: When this method returns, contains the number of chars written into the output span. This can be used to slice the output for subsequent calls, if necessary. This parameter is treated as uninitialized.
        :returns: true if bytes encoded successfully, otherwise false.
        """
        ...

    @staticmethod
    def try_encode_to_utf_8_in_place(buffer: System.Span[int], data_length: int, bytes_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        """
        Encodes the span of binary data (in-place) into UTF-8 encoded text represented as base 64.
        The encoded text output is larger than the binary data contained in the input (the operation inflates the data).
        
        :param buffer: The input span which contains binary data that needs to be encoded. It needs to be large enough to fit the result of the operation.
        :param data_length: The amount of binary data contained within the buffer that needs to be encoded (and needs to be smaller than the buffer length).
        :param bytes_written: When this method returns, contains the number of bytes written into the buffer. This parameter is treated as uninitialized.
        :returns: true if bytes encoded successfully, otherwise false.
        """
        ...


