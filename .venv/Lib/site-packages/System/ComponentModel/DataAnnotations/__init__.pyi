from typing import overload
from enum import Enum
import abc
import datetime
import typing

import System
import System.Collections.Generic
import System.ComponentModel
import System.ComponentModel.DataAnnotations
import System.Runtime.Serialization

IServiceProvider = typing.Any


class DisplayColumnAttribute(System.Attribute):
    """
    Sets the display column, the sort column, and the sort order for when a table is used as a parent table in FK
        relationships.
    """

    @property
    def display_column(self) -> str:
        ...

    @property
    def sort_column(self) -> str:
        ...

    @property
    def sort_descending(self) -> bool:
        ...

    @overload
    def __init__(self, display_column: str) -> None:
        ...

    @overload
    def __init__(self, display_column: str, sort_column: str) -> None:
        ...

    @overload
    def __init__(self, display_column: str, sort_column: str, sort_descending: bool) -> None:
        ...


class DataType(Enum):
    """Enumeration of logical data types that may appear in DataTypeAttribute"""

    CUSTOM = 0
    """Custom data type, not one of the static data types we know"""

    DATE_TIME = 1
    """DateTime data type"""

    DATE = 2
    """Date data type"""

    TIME = 3
    """Time data type"""

    DURATION = 4
    """Duration data type"""

    PHONE_NUMBER = 5
    """Phone number data type"""

    CURRENCY = 6
    """Currency data type"""

    TEXT = 7
    """Plain text data type"""

    HTML = 8
    """Html data type"""

    MULTILINE_TEXT = 9
    """Multiline text data type"""

    EMAIL_ADDRESS = 10
    """Email address data type"""

    PASSWORD = 11
    """Password data type -- do not echo in UI"""

    URL = 12
    """URL data type"""

    IMAGE_URL = 13
    """URL to an Image -- to be displayed as an image instead of text"""

    CREDIT_CARD = 14
    """Credit card data type"""

    POSTAL_CODE = 15
    """Postal code data type"""

    UPLOAD = 16
    """File upload data type"""


class ScaffoldColumnAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def scaffold(self) -> bool:
        ...

    def __init__(self, scaffold: bool) -> None:
        ...


class ValidationResult(System.Object):
    """
    Container class for the results of a validation request.
        
            Use the static  to represent successful validation.
    """

    SUCCESS: System.ComponentModel.DataAnnotations.ValidationResult
    """Gets a ValidationResult that indicates Success."""

    @property
    def member_names(self) -> typing.Iterable[str]:
        """Gets the collection of member names affected by this result.  The collection may be empty but will never be null."""
        ...

    @property
    def error_message(self) -> str:
        """Gets the error message for this result.  It may be null."""
        ...

    @error_message.setter
    def error_message(self, value: str) -> None:
        ...

    @overload
    def __init__(self, error_message: str) -> None:
        """
        Constructor that accepts an error message.  This error message would override any error message
            provided on the ValidationAttribute.
        
        :param error_message: The user-visible error message.  If null, ValidationAttribute.GetValidationResult     will use ValidationAttribute.FormatErrorMessage for its error message.
        """
        ...

    @overload
    def __init__(self, error_message: str, member_names: System.Collections.Generic.IEnumerable[str]) -> None:
        """
        Constructor that accepts an error message as well as a list of member names involved in the validation.
            This error message would override any error message provided on the ValidationAttribute.
        
        :param error_message: The user-visible error message.  If null, ValidationAttribute.GetValidationResult     will use ValidationAttribute.FormatErrorMessage for its error message.
        :param member_names: The list of member names affected by this result.     This list of member names is meant to be used by presentation layers to indicate which fields are in error.
        """
        ...

    @overload
    def __init__(self, validation_result: System.ComponentModel.DataAnnotations.ValidationResult) -> None:
        """
        Constructor that creates a copy of an existing ValidationResult.
        
        This method is protected.
        
        :param validation_result: The validation result.
        """
        ...

    def to_string(self) -> str:
        """
        Override the string representation of this instance, returning
            the ErrorMessage if not null, otherwise
            the base object.ToString result.
        
        :returns: The ErrorMessage property value if specified,     otherwise, the base object.ToString result.
        """
        ...


class ValidationContext(IServiceProvider):
    """Describes the context in which a validation is being performed."""

    @property
    def object_instance(self) -> System.Object:
        """
        Gets the object instance being validated.  While it will not be null, the state of the instance is indeterminate
            as it might only be partially initialized during validation.
            Consume this instance with caution!
        """
        ...

    @property
    def object_type(self) -> typing.Type:
        """Gets the type of the object being validated.  It will not be null."""
        ...

    @property
    def display_name(self) -> str:
        """Gets or sets the user-visible name of the type or property being validated."""
        ...

    @display_name.setter
    def display_name(self, value: str) -> None:
        ...

    @property
    def member_name(self) -> str:
        """Gets or sets the name of the type or property being validated."""
        ...

    @member_name.setter
    def member_name(self, value: str) -> None:
        ...

    @property
    def items(self) -> System.Collections.Generic.IDictionary[System.Object, System.Object]:
        """Gets the dictionary of key/value pairs associated with this context."""
        ...

    @overload
    def __init__(self, instance: typing.Any) -> None:
        """
        Construct a ValidationContext for a given object instance being validated.
        
        :param instance: The object instance being validated.  It cannot be null.
        """
        ...

    @overload
    def __init__(self, instance: typing.Any, items: System.Collections.Generic.IDictionary[System.Object, System.Object]) -> None:
        """
        Construct a ValidationContext for a given object instance and an optional
            property bag of .
        
        :param instance: The object instance being validated.  It cannot be null.
        :param items: Optional set of key/value pairs to make available to consumers via Items.     If null, an empty dictionary will be created.  If not null, the set of key/value pairs will be copied into a     new dictionary, preventing consumers from modifying the original dictionary.
        """
        ...

    @overload
    def __init__(self, instance: typing.Any, service_provider: typing.Optional[IServiceProvider], items: System.Collections.Generic.IDictionary[System.Object, System.Object]) -> None:
        """
        Construct a ValidationContext for a given object instance, an optional
            , and an optional
            property bag of .
        
        :param instance: The object instance being validated.  It cannot be null.
        :param service_provider: Optional IServiceProvider to use when GetService is called.     If it is null, GetService will always return null.
        :param items: Optional set of key/value pairs to make available to consumers via Items.     If null, an empty dictionary will be created.  If not null, the set of key/value pairs will be copied into a     new dictionary, preventing consumers from modifying the original dictionary.
        """
        ...

    @overload
    def __init__(self, instance: typing.Any, display_name: str, service_provider: typing.Optional[IServiceProvider], items: System.Collections.Generic.IDictionary[System.Object, System.Object]) -> None:
        """
        Construct a ValidationContext for a given object instance with
            a , an optional ,
            and an optional property bag of .
        
        :param instance: The object instance being validated.  It cannot be null.
        :param display_name: The display name associated with the object instance.
        :param service_provider: Optional IServiceProvider to use when GetService is called.     If it is null, GetService will always return null.
        :param items: Optional set of key/value pairs to make available to consumers via Items.     If null, an empty dictionary will be created.  If not null, the set of key/value pairs will be copied into a     new dictionary, preventing consumers from modifying the original dictionary.
        """
        ...

    def get_service(self, service_type: typing.Type) -> System.Object:
        """
        See IServiceProvider.GetService(Type).
        
        :param service_type: The type of the service needed.
        :returns: An instance of that service or null if it is not available.
        """
        ...

    def initialize_service_provider(self, service_provider: typing.Callable[[typing.Type], System.Object]) -> None:
        """
        Initializes the ValidationContext with a service provider that can return
            service instances by Type when GetService is called.
        
        :param service_provider: A Func{T, TResult} that can return service instances given the     desired Type when GetService is called.     If it is null, GetService will always return null.
        """
        ...


class ValidationAttribute(System.Attribute, metaclass=abc.ABCMeta):
    """
    Base class for all validation attributes.
        Override  to implement validation logic.
    """

    @property
    def error_message_string(self) -> str:
        """
        Gets the localized error message string, coming either from ErrorMessage, or from evaluating the
            ErrorMessageResourceType and ErrorMessageResourceName pair.
        
        This property is protected.
        """
        ...

    @property
    def requires_validation_context(self) -> bool:
        """
        A flag indicating that the attribute requires a non-null
            ValidationContext to perform validation.
            Base class returns false. Override in child classes as appropriate.
        """
        ...

    @property
    def error_message(self) -> str:
        """Gets or sets the explicit error message string."""
        ...

    @error_message.setter
    def error_message(self, value: str) -> None:
        ...

    @property
    def error_message_resource_name(self) -> str:
        """Gets or sets the resource name (property name) to use as the key for lookups on the resource type."""
        ...

    @error_message_resource_name.setter
    def error_message_resource_name(self, value: str) -> None:
        ...

    @property
    def error_message_resource_type(self) -> typing.Type:
        """Gets or sets the resource type to use for error message lookups."""
        ...

    @error_message_resource_type.setter
    def error_message_resource_type(self, value: typing.Type) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """
        Default constructor for any validation attribute.
        
        This method is protected.
        """
        ...

    @overload
    def __init__(self, error_message: str) -> None:
        """
        Constructor that accepts a fixed validation error message.
        
        This method is protected.
        
        :param error_message: A non-localized error message to use in ErrorMessageString.
        """
        ...

    @overload
    def __init__(self, error_message_accessor: typing.Callable[[], str]) -> None:
        """
        Allows for providing a resource accessor function that will be used by the ErrorMessageString
            property to retrieve the error message.  An example would be to have something like
            CustomAttribute() : base( () => MyResources.MyErrorMessage ) {}.
        
        This method is protected.
        
        :param error_message_accessor: The Func{T} that will return an error message.
        """
        ...

    def format_error_message(self, name: str) -> str:
        """
        Formats the error message to present to the user.
        
        :param name: The user-visible name to include in the formatted message.
        :returns: The localized string describing the validation error.
        """
        ...

    def get_validation_result(self, value: typing.Any, validation_context: System.ComponentModel.DataAnnotations.ValidationContext) -> System.ComponentModel.DataAnnotations.ValidationResult:
        """
        Tests whether the given  is valid with respect to the current
            validation attribute without throwing a ValidationException
        
        :param value: The value to validate
        :param validation_context: A ValidationContext instance that provides     context about the validation operation, such as the object and member being validated.
        :returns: When validation is valid, ValidationResult.Success.              When validation is invalid, an instance of .
        """
        ...

    @overload
    def is_valid(self, value: typing.Any) -> bool:
        """
        Gets the value indicating whether or not the specified  is valid
            with respect to the current validation attribute.
            
                Derived classes should not override this method as it is only available for backwards compatibility.
                Instead, implement .
        
        :param value: The value to validate
        :returns: true if the  is acceptable, false if it is not acceptable.
        """
        ...

    @overload
    def is_valid(self, value: typing.Any, validation_context: System.ComponentModel.DataAnnotations.ValidationContext) -> System.ComponentModel.DataAnnotations.ValidationResult:
        """
        Protected virtual method to override and implement validation logic.
            
                Derived classes should override this method instead of , which is deprecated.
        
        This method is protected.
        
        :param value: The value to validate.
        :param validation_context: A ValidationContext instance that provides     context about the validation operation, such as the object and member being validated.
        :returns: When validation is valid, ValidationResult.Success.              When validation is invalid, an instance of .
        """
        ...

    @overload
    def validate(self, value: typing.Any, name: str) -> None:
        """
        Validates the specified  and throws ValidationException if it is not.
            
                The overloaded  is the recommended entry point as it
                can provide additional context to the  being validated.
        
        :param value: The value to validate
        :param name: The string to be included in the validation error message if  is not valid
        """
        ...

    @overload
    def validate(self, value: typing.Any, validation_context: System.ComponentModel.DataAnnotations.ValidationContext) -> None:
        """
        Validates the specified  and throws ValidationException if it is not.
        
        :param value: The value to validate
        :param validation_context: Additional context that may be used for validation.  It cannot be null.
        """
        ...


class RegularExpressionAttribute(System.ComponentModel.DataAnnotations.ValidationAttribute):
    """Regular expression validation attribute"""

    @property
    def match_timeout_in_milliseconds(self) -> int:
        """
        Gets or sets the timeout to use when matching the regular expression pattern (in milliseconds)
            (-1 means never timeout).
        """
        ...

    @match_timeout_in_milliseconds.setter
    def match_timeout_in_milliseconds(self, value: int) -> None:
        ...

    @property
    def match_timeout(self) -> datetime.timedelta:
        """Gets the timeout to use when matching the regular expression pattern"""
        ...

    @property
    def pattern(self) -> str:
        """Gets the regular expression pattern to use"""
        ...

    def __init__(self, pattern: str) -> None:
        """
        Constructor that accepts the regular expression pattern
        
        :param pattern: The regular expression to use.  It cannot be null.
        """
        ...

    def format_error_message(self, name: str) -> str:
        """
        Override of ValidationAttribute.FormatErrorMessage
        
        :param name: The user-visible name to include in the formatted message.
        :returns: The localized message to present to the user.
        """
        ...

    def is_valid(self, value: typing.Any) -> bool:
        """
        Override of ValidationAttribute.IsValid(object)
        
        :param value: The value to test for validity.
        :returns: true if the given value matches the current regular expression pattern.
        """
        ...


class DisplayFormatAttribute(System.Attribute):
    """
    Allows overriding various display-related options for a given field. The options have the same meaning as in
        BoundField.
    """

    @property
    def data_format_string(self) -> str:
        """Gets or sets the format string"""
        ...

    @data_format_string.setter
    def data_format_string(self, value: str) -> None:
        ...

    @property
    def null_display_text(self) -> str:
        """
        Gets or sets the string to display when the value is null, which may be a resource key string.
            
                Consumers should use the  method to retrieve the UI display string.
        """
        ...

    @null_display_text.setter
    def null_display_text(self, value: str) -> None:
        ...

    @property
    def convert_empty_string_to_null(self) -> bool:
        """Gets or sets a value indicating whether empty strings should be set to null"""
        ...

    @convert_empty_string_to_null.setter
    def convert_empty_string_to_null(self, value: bool) -> None:
        ...

    @property
    def apply_format_in_edit_mode(self) -> bool:
        """Gets or sets a value indicating whether the format string should be used in edit mode"""
        ...

    @apply_format_in_edit_mode.setter
    def apply_format_in_edit_mode(self, value: bool) -> None:
        ...

    @property
    def html_encode(self) -> bool:
        """Gets or sets a value indicating whether the field should be html encoded"""
        ...

    @html_encode.setter
    def html_encode(self, value: bool) -> None:
        ...

    @property
    def null_display_text_resource_type(self) -> typing.Type:
        """
        Gets or sets the Type that contains the resources for NullDisplayText.
            Using NullDisplayTextResourceType along with NullDisplayText, allows the GetNullDisplayText
            method to return localized values.
        """
        ...

    @null_display_text_resource_type.setter
    def null_display_text_resource_type(self, value: typing.Type) -> None:
        ...

    def __init__(self) -> None:
        """Default constructor"""
        ...

    def get_null_display_text(self) -> str:
        """
        Gets the UI display string for NullDisplayText.
            
                This can be either a literal, non-localized string provided to  or the
                localized string found when  has been specified and 
                represents a resource key within that resource type.
        
        :returns: When NullDisplayTextResourceType has not been specified, the value of     NullDisplayText will be returned.              When  has been specified and          represents a resource key within that resource type, then the localized value will be returned.              When  and  have not been set, returns null.
        """
        ...


class DataTypeAttribute(System.ComponentModel.DataAnnotations.ValidationAttribute):
    """
    Allows for clarification of the DataType represented by a given
        property (such as System.ComponentModel.DataAnnotations.DataType.PhoneNumber
        or System.ComponentModel.DataAnnotations.DataType.Url)
    """

    @property
    def data_type(self) -> System.ComponentModel.DataAnnotations.DataType:
        """Gets the DataType. If it equals DataType.Custom, CustomDataType should also be retrieved."""
        ...

    @property
    def custom_data_type(self) -> str:
        """
        Gets the string representing a custom data type. Returns a non-null value only if DataType is
            DataType.Custom.
        """
        ...

    @property
    def display_format(self) -> System.ComponentModel.DataAnnotations.DisplayFormatAttribute:
        """Gets the default display format that gets used along with this DataType."""
        ...

    @display_format.setter
    def display_format(self, value: System.ComponentModel.DataAnnotations.DisplayFormatAttribute) -> None:
        ...

    @overload
    def __init__(self, data_type: System.ComponentModel.DataAnnotations.DataType) -> None:
        """
        Constructor that accepts a data type enumeration
        
        :param data_type: The DataType enum value indicating the type to apply.
        """
        ...

    @overload
    def __init__(self, custom_data_type: str) -> None:
        """
        Constructor that accepts the string name of a custom data type
        
        :param custom_data_type: The string name of the custom data type.
        """
        ...

    def get_data_type_name(self) -> str:
        """
        Return the name of the data type, either using the DataType enum or CustomDataType
            string
        
        :returns: The name of the data type enum.
        """
        ...

    def is_valid(self, value: typing.Any) -> bool:
        """
        Override of ValidationAttribute.IsValid(object)
        
        :param value: The value to validate
        :returns: Unconditionally returns true.
        """
        ...


class PhoneAttribute(System.ComponentModel.DataAnnotations.DataTypeAttribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...

    def is_valid(self, value: typing.Any) -> bool:
        ...


class CustomValidationAttribute(System.ComponentModel.DataAnnotations.ValidationAttribute):
    """
    Validation attribute that executes a user-supplied method at runtime, using one of these signatures:
        
            public static  Method(object value) { ... }
        
            public static  Method(object value,  context) {
            ... }
        
            The value can be strongly typed as type conversion will be attempted.
    """

    @property
    def validator_type(self) -> typing.Type:
        """Gets the type that contains the validation method identified by Method."""
        ...

    @property
    def type_id(self) -> System.Object:
        """Gets a unique identifier for this attribute."""
        ...

    @property
    def method(self) -> str:
        """Gets the name of the method in ValidatorType to invoke to perform validation."""
        ...

    @property
    def requires_validation_context(self) -> bool:
        ...

    def __init__(self, validator_type: typing.Type, method: str) -> None:
        """
        Instantiates a custom validation attribute that will invoke a method in the
            specified type.
        
        :param validator_type: The type that will contain the method to invoke.  It cannot be null.  See     Method.
        :param method: The name of the method to invoke in .
        """
        ...

    def format_error_message(self, name: str) -> str:
        """
        Override of ValidationAttribute.FormatErrorMessage
        
        :param name: The name to include in the formatted string
        :returns: A localized string to describe the problem.
        """
        ...

    def is_valid(self, value: typing.Any, validation_context: System.ComponentModel.DataAnnotations.ValidationContext) -> System.ComponentModel.DataAnnotations.ValidationResult:
        """
        Override of validation method.  See ValidationAttribute.IsValid(object, ValidationContext).
        
        This method is protected.
        
        :param value: The value to validate.
        :param validation_context: A ValidationContext instance that provides     context about the validation operation, such as the object and member being validated.
        :returns: Whatever the Method in ValidatorType returns.
        """
        ...


class Base64StringAttribute(System.ComponentModel.DataAnnotations.ValidationAttribute):
    """Specifies that a data field value is a well-formed Base64 string."""

    def __init__(self) -> None:
        """Initializes a new instance of the Base64StringAttribute class."""
        ...

    def is_valid(self, value: typing.Any) -> bool:
        """
        Determines whether a specified object is valid. (Overrides ValidationAttribute.IsValid(object))
        
        :param value: The object to validate.
        :returns: true if  is null or is a valid Base64 string,     otherwise false.
        """
        ...


class ValidationException(System.Exception):
    """Exception used for validation using ValidationAttribute."""

    @property
    def validation_attribute(self) -> System.ComponentModel.DataAnnotations.ValidationAttribute:
        """Gets the ValidationAttribute instance that triggered this exception."""
        ...

    @property
    def validation_result(self) -> System.ComponentModel.DataAnnotations.ValidationResult:
        """Gets the ValidationResult instance that describes the validation error."""
        ...

    @property
    def value(self) -> System.Object:
        """Gets the value that caused the validating attribute to trigger the exception"""
        ...

    @overload
    def __init__(self, validation_result: System.ComponentModel.DataAnnotations.ValidationResult, validating_attribute: System.ComponentModel.DataAnnotations.ValidationAttribute, value: typing.Any) -> None:
        """
        Constructor that accepts a structured ValidationResult describing the problem.
        
        :param validation_result: The value describing the validation error
        :param validating_attribute: The attribute that triggered this exception
        :param value: The value that caused the validating attribute to trigger the exception
        """
        ...

    @overload
    def __init__(self, error_message: str, validating_attribute: System.ComponentModel.DataAnnotations.ValidationAttribute, value: typing.Any) -> None:
        """
        Constructor that accepts an error message, the failing attribute, and the invalid value.
        
        :param error_message: The localized error message
        :param validating_attribute: The attribute that triggered this exception
        :param value: The value that caused the validating attribute to trigger the exception
        """
        ...

    @overload
    def __init__(self) -> None:
        """Default constructor."""
        ...

    @overload
    def __init__(self, message: str) -> None:
        """
        Constructor that accepts only a localized message
        
        :param message: The localized message
        """
        ...

    @overload
    def __init__(self, message: str, inner_exception: System.Exception) -> None:
        """
        Constructor that accepts a localized message and an inner exception
        
        :param message: The localized error message
        :param inner_exception: inner exception
        """
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """
        Constructor that takes a SerializationInfo.
        
        This method is protected.
        
        Obsoletions.LegacyFormatterImplMessage
        
        :param info: The SerializationInfo.
        :param context: The StreamingContext.
        """
        ...


class DisplayAttribute(System.Attribute):
    """
    DisplayAttribute is a general-purpose attribute to specify user-visible globalizable strings for types and members.
        The string properties of this class can be used either as literals or as resource identifiers into a specified
        ResourceType
    """

    @property
    def short_name(self) -> str:
        """
        Gets or sets the ShortName attribute property, which may be a resource key string.
            
                Consumers must use the  method to retrieve the UI display string.
        """
        ...

    @short_name.setter
    def short_name(self, value: str) -> None:
        ...

    @property
    def name(self) -> str:
        """
        Gets or sets the Name attribute property, which may be a resource key string.
            
                Consumers must use the  method to retrieve the UI display string.
        """
        ...

    @name.setter
    def name(self, value: str) -> None:
        ...

    @property
    def description(self) -> str:
        """
        Gets or sets the Description attribute property, which may be a resource key string.
            
                Consumers must use the  method to retrieve the UI display string.
        """
        ...

    @description.setter
    def description(self, value: str) -> None:
        ...

    @property
    def prompt(self) -> str:
        """
        Gets or sets the Prompt attribute property, which may be a resource key string.
            
                Consumers must use the  method to retrieve the UI display string.
        """
        ...

    @prompt.setter
    def prompt(self, value: str) -> None:
        ...

    @property
    def group_name(self) -> str:
        """
        Gets or sets the GroupName attribute property, which may be a resource key string.
            
                Consumers must use the  method to retrieve the UI display string.
        """
        ...

    @group_name.setter
    def group_name(self, value: str) -> None:
        ...

    @property
    def resource_type(self) -> typing.Type:
        """
        Gets or sets the System.Type that contains the resources for ShortName,
            Name, Description, Prompt, and GroupName.
            Using ResourceType along with these Key properties, allows the GetShortName,
            GetName, GetDescription, GetPrompt, and GetGroupName
            methods to return localized values.
        """
        ...

    @resource_type.setter
    def resource_type(self, value: typing.Type) -> None:
        ...

    @property
    def auto_generate_field(self) -> bool:
        """
        Gets or sets whether UI should be generated automatically to display this field. If this property is not
            set then the presentation layer will automatically determine whether UI should be generated. Setting this
            property allows an override of the default behavior of the presentation layer.
            
                Consumers must use the  method to retrieve the value, as this property
                getter will throw an exception if the value has not been set.
        """
        ...

    @auto_generate_field.setter
    def auto_generate_field(self, value: bool) -> None:
        ...

    @property
    def auto_generate_filter(self) -> bool:
        """
        Gets or sets whether UI should be generated automatically to display filtering for this field. If this property is
            not set then the presentation layer will automatically determine whether filtering UI should be generated. Setting this
            property allows an override of the default behavior of the presentation layer.
            
                Consumers must use the  method to retrieve the value, as this property
                getter will throw
                an exception if the value has not been set.
        """
        ...

    @auto_generate_filter.setter
    def auto_generate_filter(self, value: bool) -> None:
        ...

    @property
    def order(self) -> int:
        """
        Gets or sets the order in which this field should be displayed.  If this property is not set then
            the presentation layer will automatically determine the order.  Setting this property explicitly
            allows an override of the default behavior of the presentation layer.
            
                Consumers must use the  method to retrieve the value, as this property getter will throw
                an exception if the value has not been set.
        """
        ...

    @order.setter
    def order(self, value: int) -> None:
        ...

    def get_auto_generate_field(self) -> typing.Optional[bool]:
        """
        Gets the value of AutoGenerateField if it has been set, or null.
        
        :returns: When AutoGenerateField has been set returns the value of that property.              When  has not been set returns null.
        """
        ...

    def get_auto_generate_filter(self) -> typing.Optional[bool]:
        """
        Gets the value of AutoGenerateFilter if it has been set, or null.
        
        :returns: When AutoGenerateFilter has been set returns the value of that property.              When  has not been set returns null.
        """
        ...

    def get_description(self) -> str:
        """
        Gets the UI display string for Description.
            
                This can be either a literal, non-localized string provided to  or the
                localized string found when  has been specified and 
                represents a resource key within that resource type.
        
        :returns: When ResourceType has not been specified, the value of     Description will be returned.              When  has been specified and          represents a resource key within that resource type, then the localized value will be returned.
        """
        ...

    def get_group_name(self) -> str:
        """
        Gets the UI display string for GroupName.
            
                This can be either a literal, non-localized string provided to  or the
                localized string found when  has been specified and 
                represents a resource key within that resource type.
        
        :returns: When ResourceType has not been specified, the value of     GroupName will be returned.              When  has been specified and          represents a resource key within that resource type, then the localized value will be returned.
        """
        ...

    def get_name(self) -> str:
        """
        Gets the UI display string for Name.
            
                This can be either a literal, non-localized string provided to  or the
                localized string found when  has been specified and 
                represents a resource key within that resource type.
        
        :returns: When ResourceType has not been specified, the value of     Name will be returned.              When  has been specified and          represents a resource key within that resource type, then the localized value will be returned.              Can return null and will not fall back onto other values, as it's more likely for the         consumer to want to fall back onto the property name.
        """
        ...

    def get_order(self) -> typing.Optional[int]:
        """
        Gets the value of Order if it has been set, or null.
        
        :returns: When Order has been set returns the value of that property.              When  has not been set returns null.
        """
        ...

    def get_prompt(self) -> str:
        """
        Gets the UI display string for Prompt.
            
                This can be either a literal, non-localized string provided to  or the
                localized string found when  has been specified and 
                represents a resource key within that resource type.
        
        :returns: When ResourceType has not been specified, the value of     Prompt will be returned.              When  has been specified and          represents a resource key within that resource type, then the localized value will be returned.
        """
        ...

    def get_short_name(self) -> str:
        """
        Gets the UI display string for ShortName.
            
                This can be either a literal, non-localized string provided to  or the
                localized string found when  has been specified and 
                represents a resource key within that resource type.
        
        :returns: When ResourceType has not been specified, the value of     ShortName will be returned.              When  has been specified and          represents a resource key within that resource type, then the localized value will be returned.              If  is null, the value from  will be returned.
        """
        ...


class AssociatedMetadataTypeTypeDescriptionProvider(System.ComponentModel.TypeDescriptionProvider):
    """
    Extends the metadata information for a class by adding attributes and property
    information that is defined in an associated class.
    """

    @overload
    def __init__(self, type: typing.Type) -> None:
        """
        Initializes a new instance of the System.ComponentModel.DataAnnotations.AssociatedMetadataTypeTypeDescriptionProvider
        class by using the specified type.
        
        :param type: The type for which the metadata provider is created.
        """
        ...

    @overload
    def __init__(self, type: typing.Type, associated_metadata_type: typing.Type) -> None:
        """
        Initializes a new instance of the System.ComponentModel.DataAnnotations.AssociatedMetadataTypeTypeDescriptionProvider
        class by using the specified metadata provider type and associated type.
        
        :param type: The type for which the metadata provider is created.
        :param associated_metadata_type: The associated type that contains the metadata.
        """
        ...

    def get_type_descriptor(self, object_type: typing.Type, instance: typing.Any) -> System.ComponentModel.ICustomTypeDescriptor:
        """
        Gets a type descriptor for the specified type and object.
        
        :param object_type: The type of object to retrieve the type descriptor for.
        :param instance: An instance of the type.
        :returns: The descriptor that provides metadata for the type.
        """
        ...


class CreditCardAttribute(System.ComponentModel.DataAnnotations.DataTypeAttribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...

    def is_valid(self, value: typing.Any) -> bool:
        ...


class EmailAddressAttribute(System.ComponentModel.DataAnnotations.DataTypeAttribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...

    def is_valid(self, value: typing.Any) -> bool:
        ...


class IValidatableObject(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def validate(self, validation_context: System.ComponentModel.DataAnnotations.ValidationContext) -> System.Collections.Generic.IEnumerable[System.ComponentModel.DataAnnotations.ValidationResult]:
        ...


class MaxLengthAttribute(System.ComponentModel.DataAnnotations.ValidationAttribute):
    """Specifies the maximum length of collection/string data allowed in a property."""

    @property
    def length(self) -> int:
        """Gets the maximum allowable length of the collection/string data."""
        ...

    @overload
    def __init__(self, length: int) -> None:
        """
        Initializes a new instance of the MaxLengthAttribute class.
        
        :param length: The maximum allowable length of collection/string data.     Value must be greater than zero.
        """
        ...

    @overload
    def __init__(self) -> None:
        """
        Initializes a new instance of the MaxLengthAttribute class.
            The maximum allowable length supported by the database will be used.
        """
        ...

    def format_error_message(self, name: str) -> str:
        """
        Applies formatting to a specified error message. (Overrides ValidationAttribute.FormatErrorMessage)
        
        :param name: The name to include in the formatted string.
        :returns: A localized string to describe the maximum acceptable length.
        """
        ...

    def is_valid(self, value: typing.Any) -> bool:
        """
        Determines whether a specified object is valid. (Overrides ValidationAttribute.IsValid(object))
        
        :param value: The object to validate.
        :returns: true if the value is null or less than or equal to the specified maximum length, otherwise false.
        """
        ...


class TimestampAttribute(System.Attribute):
    """This attribute is used to mark a Timestamp member of a Type."""


class LengthAttribute(System.ComponentModel.DataAnnotations.ValidationAttribute):
    """Specifies the minimum and maximum length of collection/string data allowed in a property."""

    @property
    def minimum_length(self) -> int:
        """Gets the minimum allowable length of the collection/string data."""
        ...

    @property
    def maximum_length(self) -> int:
        """Gets the maximum allowable length of the collection/string data."""
        ...

    def __init__(self, minimum_length: int, maximum_length: int) -> None:
        ...

    def format_error_message(self, name: str) -> str:
        """
        Applies formatting to a specified error message. (Overrides ValidationAttribute.FormatErrorMessage)
        
        :param name: The name to include in the formatted string.
        :returns: A localized string to describe the minimum acceptable length.
        """
        ...

    def is_valid(self, value: typing.Any) -> bool:
        """
        Determines whether a specified object is valid. (Overrides ValidationAttribute.IsValid(object))
        
        :param value: The object to validate.
        :returns: true if the value is null or its length is between the specified minimum length and maximum length, otherwise     false.
        """
        ...


class StringLengthAttribute(System.ComponentModel.DataAnnotations.ValidationAttribute):
    """Validation attribute to assert a string property, field or parameter does not exceed a maximum length"""

    @property
    def maximum_length(self) -> int:
        """Gets the maximum acceptable length of the string"""
        ...

    @property
    def minimum_length(self) -> int:
        """Gets or sets the minimum acceptable length of the string"""
        ...

    @minimum_length.setter
    def minimum_length(self, value: int) -> None:
        ...

    def __init__(self, maximum_length: int) -> None:
        """
        Constructor that accepts the maximum length of the string.
        
        :param maximum_length: The maximum length, inclusive.  It may not be negative.
        """
        ...

    def format_error_message(self, name: str) -> str:
        """
        Override of ValidationAttribute.FormatErrorMessage
        
        :param name: The name to include in the formatted string
        :returns: A localized string to describe the maximum acceptable length.
        """
        ...

    def is_valid(self, value: typing.Any) -> bool:
        """
        Override of ValidationAttribute.IsValid(object)
        
        :param value: The value to test.
        :returns: true if the value is null or less than or equal to the set maximum length.
        """
        ...


class EditableAttribute(System.Attribute):
    """
    Indicates whether the consumer of a field or property, such as a client application,
        should allow editing of the value.
    """

    @property
    def allow_edit(self) -> bool:
        """
        Indicates whether or not the field/property allows editing of the
            value.
        """
        ...

    @property
    def allow_initial_value(self) -> bool:
        """
        Indicates whether or not the field/property allows an initial value
            to be specified.
        """
        ...

    @allow_initial_value.setter
    def allow_initial_value(self, value: bool) -> None:
        ...

    def __init__(self, allow_edit: bool) -> None:
        """
        Indicate whether or not a field/property is editable.
        
        :param allow_edit: Indicates whether the field/property is editable.  The value provided     will apply to both AllowEdit and     AllowInitialValue unless the AllowInitialValue     property is explicitly specified.
        """
        ...


class FileExtensionsAttribute(System.ComponentModel.DataAnnotations.DataTypeAttribute):
    """This class has no documentation."""

    @property
    def extensions(self) -> str:
        ...

    @extensions.setter
    def extensions(self, value: str) -> None:
        ...

    def __init__(self) -> None:
        ...

    def format_error_message(self, name: str) -> str:
        ...

    def is_valid(self, value: typing.Any) -> bool:
        ...


class UIHintAttribute(System.Attribute):
    """Attribute to provide a hint to the presentation layer about what control it should use"""

    @property
    def ui_hint(self) -> str:
        """Gets the name of the control that is most appropriate for this associated property or field"""
        ...

    @property
    def presentation_layer(self) -> str:
        """Gets the name of the presentation layer that supports the control type in UIHint"""
        ...

    @property
    def control_parameters(self) -> System.Collections.Generic.IDictionary[str, System.Object]:
        """Gets the name-value pairs used as parameters to the control's constructor"""
        ...

    @overload
    def __init__(self, ui_hint: str) -> None:
        """
        Constructor that accepts the name of the control, without specifying which presentation layer to use
        
        :param ui_hint: The name of the UI control.
        """
        ...

    @overload
    def __init__(self, ui_hint: str, presentation_layer: str) -> None:
        """
        Constructor that accepts both the name of the control as well as the presentation layer
        
        :param ui_hint: The name of the control to use
        :param presentation_layer: The name of the presentation layer that supports this control
        """
        ...

    @overload
    def __init__(self, ui_hint: str, presentation_layer: str, *control_parameters: typing.Union[System.Object, typing.Iterable[System.Object]]) -> None:
        """
        Full constructor that accepts the name of the control, presentation layer, and optional parameters
            to use when constructing the control
        
        :param ui_hint: The name of the control
        :param presentation_layer: The presentation layer
        :param control_parameters: The list of parameters for the control
        """
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...


class CompareAttribute(System.ComponentModel.DataAnnotations.ValidationAttribute):
    """This class has no documentation."""

    @property
    def other_property(self) -> str:
        ...

    @property
    def other_property_display_name(self) -> str:
        ...

    @property
    def requires_validation_context(self) -> bool:
        ...

    def __init__(self, other_property: str) -> None:
        ...

    def format_error_message(self, name: str) -> str:
        ...

    def is_valid(self, value: typing.Any, validation_context: System.ComponentModel.DataAnnotations.ValidationContext) -> System.ComponentModel.DataAnnotations.ValidationResult:
        """This method is protected."""
        ...


class DeniedValuesAttribute(System.ComponentModel.DataAnnotations.ValidationAttribute):
    """Specifies a list of values that should not be allowed in a property."""

    @property
    def values(self) -> typing.List[System.Object]:
        """Gets the list of values denied by this attribute."""
        ...

    def __init__(self, *values: typing.Union[System.Object, typing.Iterable[System.Object]]) -> None:
        """
        Initializes a new instance of the DeniedValuesAttribute class.
        
        :param values: A list of values that the validated value should not be equal to.
        """
        ...

    def is_valid(self, value: typing.Any) -> bool:
        """
        Determines whether a specified object is valid. (Overrides ValidationAttribute.IsValid(object))
        
        :param value: The object to validate.
        :returns: true if none of the Values are equal to ,     otherwise false.
        """
        ...


class AssociationAttribute(System.Attribute):
    """
    Used to mark an Entity member as an association
    
    AssociationAttribute has been deprecated and is not supported.
    """

    @property
    def name(self) -> str:
        """
        Gets the name of the association. For bi-directional associations, the name must
        be the same on both sides of the association
        """
        ...

    @property
    def this_key(self) -> str:
        """
        Gets a comma separated list of the property names of the key values
        on this side of the association
        """
        ...

    @property
    def other_key(self) -> str:
        """
        Gets a comma separated list of the property names of the key values
        on the other side of the association
        """
        ...

    @property
    def is_foreign_key(self) -> bool:
        """
        Gets or sets a value indicating whether this association member represents
        the foreign key side of an association
        """
        ...

    @is_foreign_key.setter
    def is_foreign_key(self, value: bool) -> None:
        ...

    @property
    def this_key_members(self) -> typing.Iterable[str]:
        """Gets the collection of individual key members specified in the ThisKey string."""
        ...

    @property
    def other_key_members(self) -> typing.Iterable[str]:
        """Gets the collection of individual key members specified in the OtherKey string."""
        ...

    def __init__(self, name: str, this_key: str, other_key: str) -> None:
        """
        Full form of constructor
        
        :param name: The name of the association. For bi-directional associations, the name must be the same on both sides of the association
        :param this_key: Comma separated list of the property names of the key values on this side of the association
        :param other_key: Comma separated list of the property names of the key values on the other side of the association
        """
        ...


class EnumDataTypeAttribute(System.ComponentModel.DataAnnotations.DataTypeAttribute):
    """This class has no documentation."""

    @property
    def enum_type(self) -> typing.Type:
        ...

    def __init__(self, enum_type: typing.Type) -> None:
        ...

    def is_valid(self, value: typing.Any) -> bool:
        ...


class UrlAttribute(System.ComponentModel.DataAnnotations.DataTypeAttribute):
    """This class has no documentation."""

    def __init__(self) -> None:
        ...

    def is_valid(self, value: typing.Any) -> bool:
        ...


class MetadataTypeAttribute(System.Attribute):
    """Specifies the metadata class to associate with a data model class."""

    @property
    def metadata_class_type(self) -> typing.Type:
        """Gets the metadata class that is associated with a data-model partial class."""
        ...

    def __init__(self, metadata_class_type: typing.Type) -> None:
        """
        Initializes a new instance of the System.ComponentModel.DataAnnotations.MetadataTypeAttribute
        class.
        
        :param metadata_class_type: The metadata class to reference.
        """
        ...


class AllowedValuesAttribute(System.ComponentModel.DataAnnotations.ValidationAttribute):
    """Specifies a list of values that should be allowed in a property."""

    @property
    def values(self) -> typing.List[System.Object]:
        """Gets the list of values allowed by this attribute."""
        ...

    def __init__(self, *values: typing.Union[System.Object, typing.Iterable[System.Object]]) -> None:
        """
        Initializes a new instance of the AllowedValuesAttribute class.
        
        :param values: A list of values that the validated value should be equal to.
        """
        ...

    def is_valid(self, value: typing.Any) -> bool:
        """
        Determines whether a specified object is valid. (Overrides ValidationAttribute.IsValid(object))
        
        :param value: The object to validate.
        :returns: true if any of the Values are equal to ,     otherwise false.
        """
        ...


class Validator(System.Object):
    """
    Helper class to validate objects, properties and other values using their associated
        ValidationAttribute
        custom attributes.
    """

    @staticmethod
    @overload
    def try_validate_object(instance: typing.Any, validation_context: System.ComponentModel.DataAnnotations.ValidationContext, validation_results: System.Collections.Generic.ICollection[System.ComponentModel.DataAnnotations.ValidationResult]) -> bool:
        """
        Tests whether the given object instance is valid.
        
        :param instance: The object instance to test.  It cannot be null.
        :param validation_context: Describes the object to validate and provides services and context for the validators.
        :param validation_results: Optional collection to receive ValidationResults for the failures.
        :returns: true if the object is valid, false if any validation errors are encountered.
        """
        ...

    @staticmethod
    @overload
    def try_validate_object(instance: typing.Any, validation_context: System.ComponentModel.DataAnnotations.ValidationContext, validation_results: System.Collections.Generic.ICollection[System.ComponentModel.DataAnnotations.ValidationResult], validate_all_properties: bool) -> bool:
        """
        Tests whether the given object instance is valid.
        
        :param instance: The object instance to test.  It cannot be null.
        :param validation_context: Describes the object to validate and provides services and context for the validators.
        :param validation_results: Optional collection to receive ValidationResults for the failures.
        :param validate_all_properties: If true, also evaluates all properties of the object (this process is not     recursive over properties of the properties).
        :returns: true if the object is valid, false if any validation errors are encountered.
        """
        ...

    @staticmethod
    def try_validate_property(value: typing.Any, validation_context: System.ComponentModel.DataAnnotations.ValidationContext, validation_results: System.Collections.Generic.ICollection[System.ComponentModel.DataAnnotations.ValidationResult]) -> bool:
        """
        Tests whether the given property value is valid.
        
        :param value: The value to test.
        :param validation_context: Describes the property member to validate and provides services and context for the     validators.
        :param validation_results: Optional collection to receive ValidationResults for the failures.
        :returns: true if the value is valid, false if any validation errors are encountered.
        """
        ...

    @staticmethod
    def try_validate_value(value: typing.Any, validation_context: System.ComponentModel.DataAnnotations.ValidationContext, validation_results: System.Collections.Generic.ICollection[System.ComponentModel.DataAnnotations.ValidationResult], validation_attributes: System.Collections.Generic.IEnumerable[System.ComponentModel.DataAnnotations.ValidationAttribute]) -> bool:
        """
        Tests whether the given value is valid against a specified list of ValidationAttributes.
        
        :param value: The value to test.
        :param validation_context: Describes the object being validated and provides services and context for the     validators.
        :param validation_results: Optional collection to receive ValidationResults for the failures.
        :param validation_attributes: The list of ValidationAttributes to validate this      against.
        :returns: true if the object is valid, false if any validation errors are encountered.
        """
        ...

    @staticmethod
    @overload
    def validate_object(instance: typing.Any, validation_context: System.ComponentModel.DataAnnotations.ValidationContext) -> None:
        """
        Throws a ValidationException if the given  is not valid.
        
        :param instance: The object instance to test.  It cannot be null.
        :param validation_context: Describes the object being validated and provides services and context for the     validators.  It cannot be null.
        """
        ...

    @staticmethod
    @overload
    def validate_object(instance: typing.Any, validation_context: System.ComponentModel.DataAnnotations.ValidationContext, validate_all_properties: bool) -> None:
        """
        Throws a ValidationException if the given object instance is not valid.
        
        :param instance: The object instance to test.  It cannot be null.
        :param validation_context: Describes the object being validated and provides services and context for the     validators.  It cannot be null.
        :param validate_all_properties: If true, also validates all the 's properties.
        """
        ...

    @staticmethod
    def validate_property(value: typing.Any, validation_context: System.ComponentModel.DataAnnotations.ValidationContext) -> None:
        """
        Throws a ValidationException if the given property  is not valid.
        
        :param value: The value to test.
        :param validation_context: Describes the object being validated and provides services and context for the     validators.  It cannot be null.
        """
        ...

    @staticmethod
    def validate_value(value: typing.Any, validation_context: System.ComponentModel.DataAnnotations.ValidationContext, validation_attributes: System.Collections.Generic.IEnumerable[System.ComponentModel.DataAnnotations.ValidationAttribute]) -> None:
        """
        Throw a ValidationException if the given value is not valid for the
            ValidationAttributes.
        
        :param value: The value to test.
        :param validation_context: Describes the object being tested.
        :param validation_attributes: The list of ValidationAttributes to validate against this instance.
        """
        ...


class MinLengthAttribute(System.ComponentModel.DataAnnotations.ValidationAttribute):
    """Specifies the minimum length of collection/string data allowed in a property."""

    @property
    def length(self) -> int:
        """Gets the minimum allowable length of the collection/string data."""
        ...

    def __init__(self, length: int) -> None:
        """
        Initializes a new instance of the MinLengthAttribute class.
        
        :param length: The minimum allowable length of collection/string data.     Value must be greater than or equal to zero.
        """
        ...

    def format_error_message(self, name: str) -> str:
        """
        Applies formatting to a specified error message. (Overrides ValidationAttribute.FormatErrorMessage)
        
        :param name: The name to include in the formatted string.
        :returns: A localized string to describe the minimum acceptable length.
        """
        ...

    def is_valid(self, value: typing.Any) -> bool:
        """
        Determines whether a specified object is valid. (Overrides ValidationAttribute.IsValid(object))
        
        :param value: The object to validate.
        :returns: true if the value is null or greater than or equal to the specified minimum length, otherwise     false.
        """
        ...


class KeyAttribute(System.Attribute):
    """Used to mark one or more entity properties that provide the entity's unique identity"""


class RequiredAttribute(System.ComponentModel.DataAnnotations.ValidationAttribute):
    """Validation attribute to indicate that a property, field or parameter is required."""

    @property
    def allow_empty_strings(self) -> bool:
        """Gets or sets a flag indicating whether the attribute should allow empty strings."""
        ...

    @allow_empty_strings.setter
    def allow_empty_strings(self, value: bool) -> None:
        ...

    def __init__(self) -> None:
        """Default constructor."""
        ...

    def is_valid(self, value: typing.Any) -> bool:
        """
        Override of ValidationAttribute.IsValid(object)
        
        :param value: The value to test
        :returns: Returns false if the  is null or an empty string.     If AllowEmptyStrings then true is returned for empty strings.
        """
        ...


class FilterUIHintAttribute(System.Attribute):
    """
    An attribute used to specify the filtering behavior for a column.
    
    FilterUIHintAttribute has been deprecated and is not supported.
    """

    @property
    def filter_ui_hint(self) -> str:
        """
        Gets the name of the control that is most appropriate for this associated
        property or field
        """
        ...

    @property
    def presentation_layer(self) -> str:
        """
        Gets the name of the presentation layer that supports the control type
        in FilterUIHint
        """
        ...

    @property
    def control_parameters(self) -> System.Collections.Generic.IDictionary[str, System.Object]:
        """Gets the name-value pairs used as parameters to the control's constructor"""
        ...

    @overload
    def __init__(self, filter_ui_hint: str) -> None:
        """
        Constructor that accepts the name of the control, without specifying
        which presentation layer to use
        
        :param filter_ui_hint: The name of the UI control.
        """
        ...

    @overload
    def __init__(self, filter_ui_hint: str, presentation_layer: str) -> None:
        """
        Constructor that accepts both the name of the control as well as the
        presentation layer
        
        :param filter_ui_hint: The name of the control to use
        :param presentation_layer: The name of the presentation layer that supports this control
        """
        ...

    @overload
    def __init__(self, filter_ui_hint: str, presentation_layer: str, *control_parameters: typing.Union[System.Object, typing.Iterable[System.Object]]) -> None:
        """
        Full constructor that accepts the name of the control, presentation layer,
        and optional parameters to use when constructing the control
        
        :param filter_ui_hint: The name of the control
        :param presentation_layer: The presentation layer
        :param control_parameters: The list of parameters for the control
        """
        ...

    def equals(self, obj: typing.Any) -> bool:
        """
        Determines whether this instance of FilterUIHintAttribute and a specified object,
        which must also be a FilterUIHintAttribute object, have the same value.
        
        :param obj: An System.Object.
        :returns: true if obj is a FilterUIHintAttribute and its value is the same as this instance; otherwise, false.
        """
        ...

    def get_hash_code(self) -> int:
        """
        Returns the hash code for this FilterUIHintAttribute.
        
        :returns: A 32-bit signed integer hash code.
        """
        ...


class RangeAttribute(System.ComponentModel.DataAnnotations.ValidationAttribute):
    """Used for specifying a range constraint"""

    @property
    def minimum(self) -> System.Object:
        """Gets the minimum value for the range"""
        ...

    @property
    def maximum(self) -> System.Object:
        """Gets the maximum value for the range"""
        ...

    @property
    def minimum_is_exclusive(self) -> bool:
        """Specifies whether validation should fail for values that are equal to Minimum."""
        ...

    @minimum_is_exclusive.setter
    def minimum_is_exclusive(self, value: bool) -> None:
        ...

    @property
    def maximum_is_exclusive(self) -> bool:
        """Specifies whether validation should fail for values that are equal to Maximum."""
        ...

    @maximum_is_exclusive.setter
    def maximum_is_exclusive(self, value: bool) -> None:
        ...

    @property
    def operand_type(self) -> typing.Type:
        """
        Gets the type of the Minimum and Maximum values (e.g. Int32, Double, or some custom
            type)
        """
        ...

    @property
    def parse_limits_in_invariant_culture(self) -> bool:
        """
        Determines whether string values for Minimum and Maximum are parsed in the invariant
        culture rather than the current culture in effect at the time of the validation.
        """
        ...

    @parse_limits_in_invariant_culture.setter
    def parse_limits_in_invariant_culture(self, value: bool) -> None:
        ...

    @property
    def convert_value_in_invariant_culture(self) -> bool:
        """
        Determines whether any conversions necessary from the value being validated to OperandType as set
        by the type parameter of the RangeAttribute(Type, string, string) constructor are carried
        out in the invariant culture rather than the current culture in effect at the time of the validation.
        """
        ...

    @convert_value_in_invariant_culture.setter
    def convert_value_in_invariant_culture(self, value: bool) -> None:
        ...

    @overload
    def __init__(self, minimum: int, maximum: int) -> None:
        """
        Constructor that takes integer minimum and maximum values
        
        :param minimum: The minimum value, inclusive
        :param maximum: The maximum value, inclusive
        """
        ...

    @overload
    def __init__(self, minimum: float, maximum: float) -> None:
        """
        Constructor that takes double minimum and maximum values
        
        :param minimum: The minimum value, inclusive
        :param maximum: The maximum value, inclusive
        """
        ...

    @overload
    def __init__(self, type: typing.Type, minimum: str, maximum: str) -> None:
        """
        Allows for specifying range for arbitrary types. The minimum and maximum strings
            will be converted to the target type.
        
        :param type: The type of the range parameters. Must implement IComparable.
        :param minimum: The minimum allowable value.
        :param maximum: The maximum allowable value.
        """
        ...

    def format_error_message(self, name: str) -> str:
        """
        Override of ValidationAttribute.FormatErrorMessage
        
        :param name: The user-visible name to include in the formatted message.
        :returns: A localized string describing the minimum and maximum values.
        """
        ...

    def is_valid(self, value: typing.Any) -> bool:
        """
        Returns true if the value falls between min and max, inclusive.
        
        :param value: The value to test for validity.
        :returns: true means the  is valid.
        """
        ...


class ConcurrencyCheckAttribute(System.Attribute):
    """
    This attribute is used to mark the members of a Type that participate in
        optimistic concurrency checks.
    """


