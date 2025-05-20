from typing import overload
from enum import Enum
import abc
import datetime
import typing
import warnings

import System
import System.Collections
import System.Collections.Generic
import System.IO
import System.Net
import System.Net.Sockets
import System.Runtime.Serialization
import System.Security
import System.Security.Authentication.ExtendedProtection

System_Net_IPNetwork = typing.Any
System_Net_IPAddress = typing.Any


class WebUtility(System.Object):
    """This class has no documentation."""

    @staticmethod
    @overload
    def html_decode(value: str) -> str:
        ...

    @staticmethod
    @overload
    def html_decode(value: str, output: System.IO.TextWriter) -> None:
        ...

    @staticmethod
    @overload
    def html_encode(value: str) -> str:
        ...

    @staticmethod
    @overload
    def html_encode(value: str, output: System.IO.TextWriter) -> None:
        ...

    @staticmethod
    def url_decode(encoded_value: str) -> str:
        ...

    @staticmethod
    def url_decode_to_bytes(encoded_value: typing.List[int], offset: int, count: int) -> typing.List[int]:
        ...

    @staticmethod
    def url_encode(value: str) -> str:
        ...

    @staticmethod
    def url_encode_to_bytes(value: typing.List[int], offset: int, count: int) -> typing.List[int]:
        ...


class EndPoint(System.Object, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    def address_family(self) -> System.Net.Sockets.AddressFamily:
        ...

    def create(self, socket_address: System.Net.SocketAddress) -> System.Net.EndPoint:
        ...

    def serialize(self) -> System.Net.SocketAddress:
        ...


class ICredentials(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def get_credential(self, uri: System.Uri, auth_type: str) -> System.Net.NetworkCredential:
        ...


class NetworkCredential(System.Object, System.Net.ICredentials, System.Net.ICredentialsByHost):
    """This class has no documentation."""

    @property
    def user_name(self) -> str:
        ...

    @user_name.setter
    def user_name(self, value: str) -> None:
        ...

    @property
    def password(self) -> str:
        ...

    @password.setter
    def password(self, value: str) -> None:
        ...

    @property
    def secure_password(self) -> System.Security.SecureString:
        ...

    @secure_password.setter
    def secure_password(self, value: System.Security.SecureString) -> None:
        ...

    @property
    def domain(self) -> str:
        ...

    @domain.setter
    def domain(self, value: str) -> None:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, user_name: str, password: str) -> None:
        ...

    @overload
    def __init__(self, user_name: str, password: str, domain: str) -> None:
        ...

    @overload
    def __init__(self, user_name: str, password: System.Security.SecureString) -> None:
        ...

    @overload
    def __init__(self, user_name: str, password: System.Security.SecureString, domain: str) -> None:
        ...

    @overload
    def get_credential(self, uri: System.Uri, authentication_type: str) -> System.Net.NetworkCredential:
        ...

    @overload
    def get_credential(self, host: str, port: int, authentication_type: str) -> System.Net.NetworkCredential:
        ...


class ICredentialsByHost(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def get_credential(self, host: str, port: int, authentication_type: str) -> System.Net.NetworkCredential:
        ...


class IPAddress(System.Object, System.ISpanFormattable, System.ISpanParsable[System_Net_IPAddress], System.IUtf8SpanFormattable, System.IUtf8SpanParsable[System_Net_IPAddress]):
    """This class has no documentation."""

    ANY: System.Net.IPAddress = ...

    LOOPBACK: System.Net.IPAddress = ...

    BROADCAST: System.Net.IPAddress = ...

    NONE: System.Net.IPAddress = ...

    I_PV_6_ANY: System.Net.IPAddress = ...

    I_PV_6_LOOPBACK: System.Net.IPAddress = ...

    I_PV_6_NONE: System.Net.IPAddress = ...

    @property
    def address_family(self) -> System.Net.Sockets.AddressFamily:
        ...

    @property
    def scope_id(self) -> int:
        ...

    @scope_id.setter
    def scope_id(self, value: int) -> None:
        ...

    @property
    def is_i_pv_6_multicast(self) -> bool:
        ...

    @property
    def is_i_pv_6_link_local(self) -> bool:
        ...

    @property
    def is_i_pv_6_site_local(self) -> bool:
        ...

    @property
    def is_i_pv_6_teredo(self) -> bool:
        ...

    @property
    def is_i_pv_6_unique_local(self) -> bool:
        """Gets whether the address is an IPv6 Unique Local address."""
        ...

    @property
    def is_i_pv_4_mapped_to_i_pv_6(self) -> bool:
        ...

    @property
    def address(self) -> int:
        """IPAddress.Address is address family dependent and has been deprecated. Use IPAddress.Equals to perform comparisons instead."""
        warnings.warn("IPAddress.Address is address family dependent and has been deprecated. Use IPAddress.Equals to perform comparisons instead.", DeprecationWarning)

    @address.setter
    def address(self, value: int) -> None:
        warnings.warn("IPAddress.Address is address family dependent and has been deprecated. Use IPAddress.Equals to perform comparisons instead.", DeprecationWarning)

    @overload
    def __init__(self, new_address: int) -> None:
        ...

    @overload
    def __init__(self, address: typing.List[int], scopeid: int) -> None:
        ...

    @overload
    def __init__(self, address: System.ReadOnlySpan[int], scopeid: int) -> None:
        ...

    @overload
    def __init__(self, address: typing.List[int]) -> None:
        ...

    @overload
    def __init__(self, address: System.ReadOnlySpan[int]) -> None:
        ...

    def equals(self, comparand: typing.Any) -> bool:
        """Compares two IP addresses."""
        ...

    def get_address_bytes(self) -> typing.List[int]:
        ...

    def get_hash_code(self) -> int:
        ...

    @staticmethod
    def host_to_network_order(host: int) -> int:
        ...

    @staticmethod
    def is_loopback(address: System.Net.IPAddress) -> bool:
        ...

    @staticmethod
    def is_valid(ip_span: System.ReadOnlySpan[str]) -> bool:
        """
        Determines whether the provided span contains a valid IPAddress.
        
        :param ip_span: The text to parse.
        """
        ...

    @staticmethod
    def is_valid_utf_8(utf_8_text: System.ReadOnlySpan[int]) -> bool:
        """
        Determines whether the provided span contains a valid IPAddress.
        
        :param utf_8_text: The text to parse.
        """
        ...

    def map_to_i_pv_4(self) -> System.Net.IPAddress:
        ...

    def map_to_i_pv_6(self) -> System.Net.IPAddress:
        ...

    @staticmethod
    def network_to_host_order(network: int) -> int:
        ...

    @staticmethod
    @overload
    def parse(ip_string: str) -> System.Net.IPAddress:
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int]) -> System.Net.IPAddress:
        """
        Parses a span of UTF-8 characters into a value.
        
        :param utf_8_text: The span of UTF-8 characters to parse.
        :returns: The result of parsing .
        """
        ...

    @staticmethod
    @overload
    def parse(ip_span: System.ReadOnlySpan[str]) -> System.Net.IPAddress:
        ...

    def to_string(self) -> str:
        ...

    @overload
    def try_format(self, destination: System.Span[str], chars_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...

    @overload
    def try_format(self, utf_8_destination: System.Span[int], bytes_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        """
        Tries to format the current IP address into the provided span.
        
        :param utf_8_destination: When this method returns, the IP address as a span of UTF-8 bytes.
        :param bytes_written: When this method returns, the number of bytes written into the .
        :returns: true if the formatting was successful; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def try_parse(ip_string: str, address: typing.Optional[System.Net.IPAddress]) -> typing.Tuple[bool, System.Net.IPAddress]:
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], result: typing.Optional[System.Net.IPAddress]) -> typing.Tuple[bool, System.Net.IPAddress]:
        """
        Tries to parse a span of UTF-8 characters into a value.
        
        :param utf_8_text: The span of UTF-8 characters to parse.
        :param result: On return, contains the result of successfully parsing  or an undefined value on failure.
        :returns: true if  was successfully parsed; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def try_parse(ip_span: System.ReadOnlySpan[str], address: typing.Optional[System.Net.IPAddress]) -> typing.Tuple[bool, System.Net.IPAddress]:
        ...

    def try_write_bytes(self, destination: System.Span[int], bytes_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        ...


class IPNetwork(System.IEquatable[System_Net_IPNetwork], System.ISpanFormattable, System.ISpanParsable[System_Net_IPNetwork], System.IUtf8SpanFormattable, System.IUtf8SpanParsable[System_Net_IPNetwork]):
    """Represents an IP network with an IPAddress containing the network prefix and an int defining the prefix length."""

    @property
    def base_address(self) -> System.Net.IPAddress:
        """Gets the IPAddress that represents the prefix of the network."""
        ...

    @property
    def prefix_length(self) -> int:
        """Gets the length of the network prefix in bits."""
        ...

    def __eq__(self, right: System.Net.IPNetwork) -> bool:
        """
        Determines whether the specified instances of IPNetwork are equal.
        
        :returns: true if the networks are equal; otherwise false.
        """
        ...

    def __init__(self, base_address: System.Net.IPAddress, prefix_length: int) -> None:
        """
        Initializes a new instance of the IPNetwork class with the specified IPAddress and prefix length.
        
        :param base_address: The IPAddress that represents the prefix of the network.
        :param prefix_length: The length of the prefix in bits.
        """
        ...

    def __ne__(self, right: System.Net.IPNetwork) -> bool:
        """
        Determines whether the specified instances of IPNetwork are not equal.
        
        :returns: true if the networks are not equal; otherwise false.
        """
        ...

    def contains(self, address: System.Net.IPAddress) -> bool:
        """
        Determines whether a given IPAddress is part of the network.
        
        :param address: The IPAddress to check.
        :returns: true if the IPAddress is part of the network; otherwise, false.
        """
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        """
        Determines whether two IPNetwork instances are equal.
        
        :param obj: The IPNetwork instance to compare to this instance.
        :returns: true if  is an IPNetwork instance and the networks are equal; otherwise false.
        """
        ...

    @overload
    def equals(self, other: System.Net.IPNetwork) -> bool:
        """
        Determines whether two IPNetwork instances are equal.
        
        :param other: The IPNetwork instance to compare to this instance.
        :returns: true if the networks are equal; otherwise false.
        """
        ...

    def get_hash_code(self) -> int:
        """
        Returns the hash code for this instance.
        
        :returns: An integer hash value.
        """
        ...

    @staticmethod
    @overload
    def parse(s: str) -> System.Net.IPNetwork:
        """
        Converts a CIDR string to an IPNetwork instance.
        
        :param s: A string that defines an IP network in CIDR notation.
        :returns: An IPNetwork instance.
        """
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str]) -> System.Net.IPNetwork:
        """
        Converts a CIDR character span to an IPNetwork instance.
        
        :param s: A character span that defines an IP network in CIDR notation.
        :returns: An IPNetwork instance.
        """
        ...

    @staticmethod
    @overload
    def parse(utf_8_text: System.ReadOnlySpan[int]) -> System.Net.IPNetwork:
        """
        Converts a UTF-8 CIDR character span to an IPNetwork instance.
        
        :param utf_8_text: A UTF-8 character span that defines an IP network in CIDR notation.
        :returns: An IPNetwork instance.
        """
        ...

    def to_string(self) -> str:
        """
        Converts the instance to a string containing the IPNetwork's CIDR notation.
        
        :returns: The string containing the IPNetwork's CIDR notation.
        """
        ...

    @overload
    def try_format(self, destination: System.Span[str], chars_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        """
        Attempts to write the IPNetwork's CIDR notation to the given  span and returns a value indicating whether the operation succeeded.
        
        :param destination: The destination span of characters.
        :param chars_written: When this method returns, contains the number of characters that were written to .
        :returns: true if the formatting was succesful; otherwise false.
        """
        ...

    @overload
    def try_format(self, utf_8_destination: System.Span[int], bytes_written: typing.Optional[int]) -> typing.Tuple[bool, int]:
        """
        Attempts to write the IPNetwork's CIDR notation to the given  UTF-8 span and returns a value indicating whether the operation succeeded.
        
        :param utf_8_destination: The destination span of UTF-8 bytes.
        :param bytes_written: When this method returns, contains the number of bytes that were written to .
        :returns: true if the formatting was succesful; otherwise false.
        """
        ...

    @staticmethod
    @overload
    def try_parse(s: str, result: typing.Optional[System.Net.IPNetwork]) -> typing.Tuple[bool, System.Net.IPNetwork]:
        """
        Converts the specified CIDR string to an IPNetwork instance and returns a value indicating whether the conversion succeeded.
        
        :param s: A string that defines an IP network in CIDR notation.
        :param result: When the method returns, contains an IPNetwork instance if the conversion succeeds.
        :returns: true if the conversion was succesful; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], result: typing.Optional[System.Net.IPNetwork]) -> typing.Tuple[bool, System.Net.IPNetwork]:
        """
        Converts the specified CIDR character span to an IPNetwork instance and returns a value indicating whether the conversion succeeded.
        
        :param s: A string that defines an IP network in CIDR notation.
        :param result: When the method returns, contains an IPNetwork instance if the conversion succeeds.
        :returns: true if the conversion was successful; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def try_parse(utf_8_text: System.ReadOnlySpan[int], result: typing.Optional[System.Net.IPNetwork]) -> typing.Tuple[bool, System.Net.IPNetwork]:
        """
        Converts the specified UTF-8 CIDR character span to an IPNetwork instance and returns a value indicating whether the conversion succeeded.
        
        :param utf_8_text: A UTF-8 character span that defines an IP network in CIDR notation.
        :param result: When the method returns, contains an IPNetwork instance if the conversion succeeds.
        :returns: true if the conversion was successful; otherwise, false.
        """
        ...


class AuthenticationSchemes(Enum):
    """This class has no documentation."""

    NONE = ...

    DIGEST = ...

    NEGOTIATE = ...

    NTLM = ...

    BASIC = ...

    ANONYMOUS = ...

    INTEGRATED_WINDOWS_AUTHENTICATION = ...


class HttpStatusCode(Enum):
    """This class has no documentation."""

    CONTINUE = 100

    SWITCHING_PROTOCOLS = 101

    PROCESSING = 102

    EARLY_HINTS = 103

    OK = 200

    CREATED = 201

    ACCEPTED = 202

    NON_AUTHORITATIVE_INFORMATION = 203

    NO_CONTENT = 204

    RESET_CONTENT = 205

    PARTIAL_CONTENT = 206

    MULTI_STATUS = 207

    ALREADY_REPORTED = 208

    IM_USED = 226

    MULTIPLE_CHOICES = 300

    AMBIGUOUS = 300

    MOVED_PERMANENTLY = 301

    MOVED = 301

    FOUND = 302

    REDIRECT = 302

    SEE_OTHER = 303

    REDIRECT_METHOD = 303

    NOT_MODIFIED = 304

    USE_PROXY = 305

    UNUSED = 306

    TEMPORARY_REDIRECT = 307

    REDIRECT_KEEP_VERB = 307

    PERMANENT_REDIRECT = 308

    BAD_REQUEST = 400

    UNAUTHORIZED = 401

    PAYMENT_REQUIRED = 402

    FORBIDDEN = 403

    NOT_FOUND = 404

    METHOD_NOT_ALLOWED = 405

    NOT_ACCEPTABLE = 406

    PROXY_AUTHENTICATION_REQUIRED = 407

    REQUEST_TIMEOUT = 408

    CONFLICT = 409

    GONE = 410

    LENGTH_REQUIRED = 411

    PRECONDITION_FAILED = 412

    REQUEST_ENTITY_TOO_LARGE = 413

    REQUEST_URI_TOO_LONG = 414

    UNSUPPORTED_MEDIA_TYPE = 415

    REQUESTED_RANGE_NOT_SATISFIABLE = 416

    EXPECTATION_FAILED = 417

    MISDIRECTED_REQUEST = 421

    UNPROCESSABLE_ENTITY = 422

    UNPROCESSABLE_CONTENT = 422

    LOCKED = 423

    FAILED_DEPENDENCY = 424

    UPGRADE_REQUIRED = 426

    PRECONDITION_REQUIRED = 428

    TOO_MANY_REQUESTS = 429

    REQUEST_HEADER_FIELDS_TOO_LARGE = 431

    UNAVAILABLE_FOR_LEGAL_REASONS = 451

    INTERNAL_SERVER_ERROR = 500

    NOT_IMPLEMENTED = 501

    BAD_GATEWAY = 502

    SERVICE_UNAVAILABLE = 503

    GATEWAY_TIMEOUT = 504

    HTTP_VERSION_NOT_SUPPORTED = 505

    VARIANT_ALSO_NEGOTIATES = 506

    INSUFFICIENT_STORAGE = 507

    LOOP_DETECTED = 508

    NOT_EXTENDED = 510

    NETWORK_AUTHENTICATION_REQUIRED = 511


class CredentialCache(System.Object, System.Net.ICredentials, System.Net.ICredentialsByHost, System.Collections.IEnumerable):
    """This class has no documentation."""

    DEFAULT_CREDENTIALS: System.Net.ICredentials

    DEFAULT_NETWORK_CREDENTIALS: System.Net.NetworkCredential

    def __init__(self) -> None:
        ...

    @overload
    def add(self, uri_prefix: System.Uri, auth_type: str, cred: System.Net.NetworkCredential) -> None:
        ...

    @overload
    def add(self, host: str, port: int, authentication_type: str, credential: System.Net.NetworkCredential) -> None:
        ...

    @overload
    def get_credential(self, uri_prefix: System.Uri, auth_type: str) -> System.Net.NetworkCredential:
        ...

    @overload
    def get_credential(self, host: str, port: int, authentication_type: str) -> System.Net.NetworkCredential:
        ...

    def get_enumerator(self) -> System.Collections.IEnumerator:
        ...

    @overload
    def remove(self, uri_prefix: System.Uri, auth_type: str) -> None:
        ...

    @overload
    def remove(self, host: str, port: int, authentication_type: str) -> None:
        ...


class DnsEndPoint(System.Net.EndPoint):
    """This class has no documentation."""

    @property
    def host(self) -> str:
        ...

    @property
    def address_family(self) -> System.Net.Sockets.AddressFamily:
        ...

    @property
    def port(self) -> int:
        ...

    @overload
    def __init__(self, host: str, port: int) -> None:
        ...

    @overload
    def __init__(self, host: str, port: int, address_family: System.Net.Sockets.AddressFamily) -> None:
        ...

    def equals(self, comparand: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def to_string(self) -> str:
        ...


class DecompressionMethods(Enum):
    """This class has no documentation."""

    NONE = 0

    G_ZIP = ...

    DEFLATE = ...

    BROTLI = ...

    ALL = ...


class CookieVariant(Enum):
    """This class has no documentation."""

    UNKNOWN = 0

    PLAIN = 1

    RFC_2109 = 2

    RFC_2965 = 3

    DEFAULT = ...


class Cookie(System.Object):
    """This class has no documentation."""

    @property
    def comment(self) -> str:
        ...

    @comment.setter
    def comment(self, value: str) -> None:
        ...

    @property
    def comment_uri(self) -> System.Uri:
        ...

    @comment_uri.setter
    def comment_uri(self, value: System.Uri) -> None:
        ...

    @property
    def http_only(self) -> bool:
        ...

    @http_only.setter
    def http_only(self, value: bool) -> None:
        ...

    @property
    def discard(self) -> bool:
        ...

    @discard.setter
    def discard(self, value: bool) -> None:
        ...

    @property
    def domain(self) -> str:
        ...

    @domain.setter
    def domain(self, value: str) -> None:
        ...

    @property
    def expired(self) -> bool:
        ...

    @expired.setter
    def expired(self, value: bool) -> None:
        ...

    @property
    def expires(self) -> datetime.datetime:
        ...

    @expires.setter
    def expires(self, value: datetime.datetime) -> None:
        ...

    @property
    def name(self) -> str:
        ...

    @name.setter
    def name(self, value: str) -> None:
        ...

    @property
    def path(self) -> str:
        ...

    @path.setter
    def path(self, value: str) -> None:
        ...

    @property
    def port(self) -> str:
        ...

    @port.setter
    def port(self, value: str) -> None:
        ...

    @property
    def secure(self) -> bool:
        ...

    @secure.setter
    def secure(self, value: bool) -> None:
        ...

    @property
    def time_stamp(self) -> datetime.datetime:
        ...

    @property
    def value(self) -> str:
        ...

    @value.setter
    def value(self, value: str) -> None:
        ...

    @property
    def version(self) -> int:
        ...

    @version.setter
    def version(self, value: int) -> None:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, name: str, value: str) -> None:
        ...

    @overload
    def __init__(self, name: str, value: str, path: str) -> None:
        ...

    @overload
    def __init__(self, name: str, value: str, path: str, domain: str) -> None:
        ...

    def equals(self, comparand: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def to_string(self) -> str:
        ...


class CookieException(System.FormatException, System.Runtime.Serialization.ISerializable):
    """This class has no documentation."""

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, message: str) -> None:
        """
        Initializes a new instance of the CookieException class with the specified error message.
        
        :param message: A string that describes the error that occurred.
        """
        ...

    @overload
    def __init__(self, message: str, inner_exception: System.Exception) -> None:
        """
        Initializes a new instance of the CookieException class with the specified error message
        and a reference to the inner exception that is the cause of this exception.
        
        :param message: A string that describes the error that occurred.
        :param inner_exception: The exception that is the cause of the current exception.
        """
        ...

    @overload
    def __init__(self, serialization_info: System.Runtime.Serialization.SerializationInfo, streaming_context: System.Runtime.Serialization.StreamingContext) -> None:
        """
        This method is protected.
        
        Obsoletions.LegacyFormatterImplMessage
        """
        ...

    def get_object_data(self, serialization_info: System.Runtime.Serialization.SerializationInfo, streaming_context: System.Runtime.Serialization.StreamingContext) -> None:
        """Obsoletions.LegacyFormatterImplMessage"""
        warnings.warn("Obsoletions.LegacyFormatterImplMessage", DeprecationWarning)


class CookieCollection(System.Object, System.Collections.Generic.ICollection[System.Net.Cookie], System.Collections.Generic.IReadOnlyCollection[System.Net.Cookie], System.Collections.ICollection, typing.Iterable[System.Net.Cookie]):
    """This class has no documentation."""

    @property
    def is_read_only(self) -> bool:
        ...

    @property
    def count(self) -> int:
        ...

    @property
    def is_synchronized(self) -> bool:
        ...

    @property
    def sync_root(self) -> System.Object:
        ...

    @overload
    def __getitem__(self, index: int) -> System.Net.Cookie:
        ...

    @overload
    def __getitem__(self, name: str) -> System.Net.Cookie:
        ...

    def __init__(self) -> None:
        ...

    def __iter__(self) -> typing.Iterator[System.Net.Cookie]:
        ...

    @overload
    def add(self, cookie: System.Net.Cookie) -> None:
        ...

    @overload
    def add(self, cookies: System.Net.CookieCollection) -> None:
        ...

    def clear(self) -> None:
        ...

    def contains(self, cookie: System.Net.Cookie) -> bool:
        ...

    @overload
    def copy_to(self, array: System.Array, index: int) -> None:
        ...

    @overload
    def copy_to(self, array: typing.List[System.Net.Cookie], index: int) -> None:
        ...

    def get_enumerator(self) -> System.Collections.IEnumerator:
        ...

    def remove(self, cookie: System.Net.Cookie) -> bool:
        ...


class CookieContainer(System.Object):
    """This class has no documentation."""

    DEFAULT_COOKIE_LIMIT: int = 300

    DEFAULT_PER_DOMAIN_COOKIE_LIMIT: int = 20

    DEFAULT_COOKIE_LENGTH_LIMIT: int = 4096

    @property
    def capacity(self) -> int:
        ...

    @capacity.setter
    def capacity(self, value: int) -> None:
        ...

    @property
    def count(self) -> int:
        ...

    @property
    def max_cookie_size(self) -> int:
        ...

    @max_cookie_size.setter
    def max_cookie_size(self, value: int) -> None:
        ...

    @property
    def per_domain_capacity(self) -> int:
        ...

    @per_domain_capacity.setter
    def per_domain_capacity(self, value: int) -> None:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, capacity: int) -> None:
        ...

    @overload
    def __init__(self, capacity: int, per_domain_capacity: int, max_cookie_size: int) -> None:
        ...

    @overload
    def add(self, cookie: System.Net.Cookie) -> None:
        ...

    @overload
    def add(self, cookies: System.Net.CookieCollection) -> None:
        ...

    @overload
    def add(self, uri: System.Uri, cookie: System.Net.Cookie) -> None:
        ...

    @overload
    def add(self, uri: System.Uri, cookies: System.Net.CookieCollection) -> None:
        ...

    def get_all_cookies(self) -> System.Net.CookieCollection:
        """
        Gets a CookieCollection that contains all of the Cookie instances in the container.
        
        :returns: A CookieCollection that contains all of the Cookie instances in the container.
        """
        ...

    def get_cookie_header(self, uri: System.Uri) -> str:
        ...

    def get_cookies(self, uri: System.Uri) -> System.Net.CookieCollection:
        ...

    def set_cookies(self, uri: System.Uri, cookie_header: str) -> None:
        ...


class PathList(System.Object):
    """This class has no documentation."""


class HttpVersion(System.Object):
    """This class has no documentation."""

    UNKNOWN: System.Version = ...
    """Defines a Version instance that indicates an unknown version of HTTP."""

    VERSION_10: System.Version = ...
    """Defines a Version instance for HTTP 1.0."""

    VERSION_11: System.Version = ...
    """Defines a Version instance for HTTP 1.1."""

    VERSION_20: System.Version = ...
    """Defines a Version instance for HTTP 2.0."""

    VERSION_30: System.Version = ...
    """Defines a Version instance for HTTP 3.0."""


class IWebProxy(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def credentials(self) -> System.Net.ICredentials:
        ...

    @credentials.setter
    def credentials(self, value: System.Net.ICredentials) -> None:
        ...

    def get_proxy(self, destination: System.Uri) -> System.Uri:
        ...

    def is_bypassed(self, host: System.Uri) -> bool:
        ...


class TransportContext(System.Object, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def get_channel_binding(self, kind: System.Security.Authentication.ExtendedProtection.ChannelBindingKind) -> System.Security.Authentication.ExtendedProtection.ChannelBinding:
        ...


class IPEndPoint(System.Net.EndPoint):
    """Provides an IP address."""

    MIN_PORT: int = ...
    """Specifies the minimum acceptable value for the System.Net.IPEndPoint.Port property."""

    MAX_PORT: int = ...
    """Specifies the maximum acceptable value for the System.Net.IPEndPoint.Port property."""

    @property
    def address_family(self) -> System.Net.Sockets.AddressFamily:
        ...

    @property
    def address(self) -> System.Net.IPAddress:
        """Gets or sets the IP address."""
        ...

    @address.setter
    def address(self, value: System.Net.IPAddress) -> None:
        ...

    @property
    def port(self) -> int:
        """Gets or sets the port."""
        ...

    @port.setter
    def port(self, value: int) -> None:
        ...

    @overload
    def __init__(self, address: int, port: int) -> None:
        """Creates a new instance of the IPEndPoint class with the specified address and port."""
        ...

    @overload
    def __init__(self, address: System.Net.IPAddress, port: int) -> None:
        """Creates a new instance of the IPEndPoint class with the specified address and port."""
        ...

    def create(self, socket_address: System.Net.SocketAddress) -> System.Net.EndPoint:
        ...

    def equals(self, comparand: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    @staticmethod
    @overload
    def parse(s: str) -> System.Net.IPEndPoint:
        ...

    @staticmethod
    @overload
    def parse(s: System.ReadOnlySpan[str]) -> System.Net.IPEndPoint:
        ...

    def serialize(self) -> System.Net.SocketAddress:
        ...

    def to_string(self) -> str:
        ...

    @staticmethod
    @overload
    def try_parse(s: str, result: typing.Optional[System.Net.IPEndPoint]) -> typing.Tuple[bool, System.Net.IPEndPoint]:
        ...

    @staticmethod
    @overload
    def try_parse(s: System.ReadOnlySpan[str], result: typing.Optional[System.Net.IPEndPoint]) -> typing.Tuple[bool, System.Net.IPEndPoint]:
        ...


