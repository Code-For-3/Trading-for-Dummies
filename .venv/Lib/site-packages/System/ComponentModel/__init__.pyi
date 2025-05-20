from typing import overload
from enum import Enum
import abc
import typing
import warnings

import System
import System.Collections
import System.Collections.Generic
import System.Collections.ObjectModel
import System.ComponentModel
import System.ComponentModel.Design
import System.Globalization
import System.Reflection
import System.Resources
import System.Runtime.InteropServices
import System.Runtime.Serialization

IServiceProvider = typing.Any

System_ComponentModel_BindingList_T = typing.TypeVar("System_ComponentModel_BindingList_T")
System_ComponentModel__EventContainer_Callable = typing.TypeVar("System_ComponentModel__EventContainer_Callable")
System_ComponentModel__EventContainer_ReturnType = typing.TypeVar("System_ComponentModel__EventContainer_ReturnType")


class EditorBrowsableState(Enum):
    """This class has no documentation."""

    ALWAYS = 0

    NEVER = 1

    ADVANCED = 2


class EditorBrowsableAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def state(self) -> System.ComponentModel.EditorBrowsableState:
        ...

    @overload
    def __init__(self, state: System.ComponentModel.EditorBrowsableState) -> None:
        ...

    @overload
    def __init__(self) -> None:
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...


class DefaultValueAttribute(System.Attribute):
    """Specifies the default value for a property."""

    @property
    def value(self) -> System.Object:
        """Gets the default value of the property this attribute is bound to."""
        ...

    @overload
    def __init__(self, value: typing.Any) -> None:
        """
        Initializes a new instance of the DefaultValueAttribute
        class.
        """
        ...

    @overload
    def __init__(self, type: typing.Type, value: str) -> None:
        """
        Initializes a new instance of the DefaultValueAttribute
        class, converting the specified value to the specified type, and using the U.S. English
        culture as the translation context.
        """
        ...

    @overload
    def __init__(self, value: str) -> None:
        """
        Initializes a new instance of the DefaultValueAttribute
        class using a Unicode character.
        """
        ...

    @overload
    def __init__(self, value: int) -> None:
        """
        Initializes a new instance of the DefaultValueAttribute
        class using an 8-bit unsigned integer.
        """
        ...

    @overload
    def __init__(self, value: float) -> None:
        """
        Initializes a new instance of the DefaultValueAttribute
        class using a single-precision floating point number.
        """
        ...

    @overload
    def __init__(self, value: bool) -> None:
        """
        Initializes a new instance of the DefaultValueAttribute
        class using a bool value.
        """
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def set_value(self, value: typing.Any) -> None:
        """This method is protected."""
        ...


class Win32Exception(System.Runtime.InteropServices.ExternalException):
    """The exception that is thrown for a Win32 error code."""

    @property
    def native_error_code(self) -> int:
        """Represents the Win32 error code associated with this exception. This field is read-only."""
        ...

    @overload
    def __init__(self) -> None:
        """
        Initializes a new instance of the Win32Exception class with the last Win32 error
        that occurred.
        """
        ...

    @overload
    def __init__(self, error: int) -> None:
        """Initializes a new instance of the Win32Exception class with the specified error."""
        ...

    @overload
    def __init__(self, error: int, message: str) -> None:
        """
        Initializes a new instance of the Win32Exception class with the specified error and the
        specified detailed description.
        """
        ...

    @overload
    def __init__(self, message: str) -> None:
        """Initializes a new instance of the Exception class with a specified error message."""
        ...

    @overload
    def __init__(self, message: str, inner_exception: System.Exception) -> None:
        """
        Initializes a new instance of the Exception class with a specified error message and a
        reference to the inner exception that is the cause of this exception.
        """
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """
        This method is protected.
        
        Obsoletions.LegacyFormatterImplMessage
        """
        ...

    def get_object_data(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """Obsoletions.LegacyFormatterImplMessage"""
        warnings.warn("Obsoletions.LegacyFormatterImplMessage", DeprecationWarning)

    def to_string(self) -> str:
        """
        Returns a string that contains the NativeErrorCode, or Exception.HResult, or both.
        
        :returns: A string that represents the NativeErrorCode, or Exception.HResult, or both.
        """
        ...


class TypeConverterAttribute(System.Attribute):
    """
    Specifies what type to use as a converter for the object this attribute is
    bound to. This class cannot be inherited.
    """

    DEFAULT: System.ComponentModel.TypeConverterAttribute = ...
    """
    Specifies the type to use as a converter for the object this attribute is
    bound to. This static field is read-only.
    """

    @property
    def converter_type_name(self) -> str:
        """
        Gets the fully qualified type name of the System.Type to use as a
        converter for the object this attribute is bound to.
        """
        ...

    @overload
    def __init__(self) -> None:
        """
        Initializes a new instance of the System.ComponentModel.TypeConverterAttribute
        class with the default type converter, which is an empty string ("").
        """
        ...

    @overload
    def __init__(self, type: typing.Type) -> None:
        """
        Initializes a new instance of the System.ComponentModel.TypeConverterAttribute
        class, using the specified type as the data converter for the object this attribute
        is bound to.
        """
        ...

    @overload
    def __init__(self, type_name: str) -> None:
        """
        Initializes a new instance of the System.ComponentModel.TypeConverterAttribute
        class, using the specified type name as the data converter for the object this attribute
        is bound to.
        """
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...


class PropertyChangingEventArgs(System.EventArgs):
    """Provides data for the PropertyChanging event."""

    @property
    def property_name(self) -> str:
        """Indicates the name of the property that is changing."""
        ...

    def __init__(self, property_name: str) -> None:
        """
        Initializes a new instance of the System.ComponentModel.PropertyChangingEventArgs
        class.
        """
        ...


class INotifyPropertyChanging(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def property_changing(self) -> _EventContainer[typing.Callable[[System.Object, System.ComponentModel.PropertyChangingEventArgs], None], None]:
        ...

    @property_changing.setter
    def property_changing(self, value: _EventContainer[typing.Callable[[System.Object, System.ComponentModel.PropertyChangingEventArgs], None], None]) -> None:
        ...


class PropertyChangedEventArgs(System.EventArgs):
    """Provides data for the PropertyChanged event."""

    @property
    def property_name(self) -> str:
        """Indicates the name of the property that changed."""
        ...

    def __init__(self, property_name: str) -> None:
        """
        Initializes a new instance of the System.ComponentModel.PropertyChangedEventArgs
        class.
        """
        ...


class TypeDescriptionProviderAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def type_name(self) -> str:
        """
        The TypeName property returns the assembly qualified type name
        for the type description provider.
        """
        ...

    @overload
    def __init__(self, type_name: str) -> None:
        """Creates a new TypeDescriptionProviderAttribute object."""
        ...

    @overload
    def __init__(self, type: typing.Type) -> None:
        """Creates a new TypeDescriptionProviderAttribute object."""
        ...


class INotifyPropertyChanged(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def property_changed(self) -> _EventContainer[typing.Callable[[System.Object, System.ComponentModel.PropertyChangedEventArgs], None], None]:
        ...

    @property_changed.setter
    def property_changed(self, value: _EventContainer[typing.Callable[[System.Object, System.ComponentModel.PropertyChangedEventArgs], None], None]) -> None:
        ...


class DataErrorsChangedEventArgs(System.EventArgs):
    """Provides data for the ErrorsChanged event."""

    @property
    def property_name(self) -> str:
        """Indicates the name of the property whose errors changed."""
        ...

    def __init__(self, property_name: str) -> None:
        """
        Initializes a new instance of the System.ComponentModel.DataErrorsChangedEventArgs
        class.
        """
        ...


class INotifyDataErrorInfo(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def has_errors(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def errors_changed(self) -> _EventContainer[typing.Callable[[System.Object, System.ComponentModel.DataErrorsChangedEventArgs], None], None]:
        ...

    @errors_changed.setter
    def errors_changed(self, value: _EventContainer[typing.Callable[[System.Object, System.ComponentModel.DataErrorsChangedEventArgs], None], None]) -> None:
        ...

    def get_errors(self, property_name: str) -> System.Collections.IEnumerable:
        ...


class AttributeCollection(System.Object, System.Collections.ICollection):
    """Represents a collection of attributes."""

    EMPTY: System.ComponentModel.AttributeCollection = ...
    """An empty AttributeCollection that can used instead of creating a new one."""

    @property
    def count(self) -> int:
        """Gets the number of attributes."""
        ...

    @overload
    def __getitem__(self, index: int) -> System.Attribute:
        """Gets the attribute with the specified index number."""
        ...

    @overload
    def __getitem__(self, attribute_type: typing.Type) -> System.Attribute:
        """Gets the attribute with the specified type."""
        ...

    @overload
    def __init__(self, *attributes: typing.Union[System.Attribute, typing.Iterable[System.Attribute]]) -> None:
        """Creates a new AttributeCollection."""
        ...

    @overload
    def __init__(self) -> None:
        """This method is protected."""
        ...

    @overload
    def contains(self, attribute: System.Attribute) -> bool:
        """Determines if this collection of attributes has the specified attribute."""
        ...

    @overload
    def contains(self, attributes: typing.List[System.Attribute]) -> bool:
        """
        Determines if this attribute collection contains the all
        the specified attributes in the attribute array.
        """
        ...

    def copy_to(self, array: System.Array, index: int) -> None:
        """Copies this collection to an array."""
        ...

    @staticmethod
    def from_existing(existing: System.ComponentModel.AttributeCollection, *new_attributes: typing.Union[System.Attribute, typing.Iterable[System.Attribute]]) -> System.ComponentModel.AttributeCollection:
        """Creates a new AttributeCollection from an existing AttributeCollection"""
        ...

    def get_default_attribute(self, attribute_type: typing.Type) -> System.Attribute:
        """
        Returns the default value for an attribute. This uses the following heuristic:
        1. It looks for a public static field named "Default".
        
        This method is protected.
        """
        ...

    def get_enumerator(self) -> System.Collections.IEnumerator:
        """Gets an enumerator for this collection."""
        ...

    @overload
    def matches(self, attribute: System.Attribute) -> bool:
        """
        Determines if a specified attribute is the same as an attribute
        in the collection.
        """
        ...

    @overload
    def matches(self, attributes: typing.List[System.Attribute]) -> bool:
        """
        Determines if the attributes in the specified array are
        the same as the attributes in the collection.
        """
        ...


class MemberDescriptor(System.Object, metaclass=abc.ABCMeta):
    """
    Declares an array of attributes for a member and defines
    the properties and methods that give you access to the attributes in the array.
    All attributes must derive from System.Attribute.
    """

    @property
    def attribute_array(self) -> typing.List[System.Attribute]:
        """
        Gets or sets an array of attributes.
        
        This property is protected.
        """
        ...

    @attribute_array.setter
    def attribute_array(self, value: typing.List[System.Attribute]) -> None:
        ...

    @property
    def attributes(self) -> System.ComponentModel.AttributeCollection:
        """Gets the collection of attributes for this member."""
        ...

    @property
    def category(self) -> str:
        """
        Gets the name of the category that the member belongs to, as specified
        in the System.ComponentModel.CategoryAttribute.
        """
        ...

    @property
    def description(self) -> str:
        """Gets the description of the member as specified in the System.ComponentModel.DescriptionAttribute."""
        ...

    @property
    def is_browsable(self) -> bool:
        """
        Gets a value indicating whether the member is browsable as specified in the
        System.ComponentModel.BrowsableAttribute.
        """
        ...

    @property
    def name(self) -> str:
        """Gets the name of the member."""
        ...

    @property
    def name_hash_code(self) -> int:
        """
        Gets the hash code for the name of the member as specified in string.GetHashCode().
        
        This property is protected.
        """
        ...

    @property
    def design_time_only(self) -> bool:
        """
        Determines whether this member should be set only at
        design time as specified in the System.ComponentModel.DesignOnlyAttribute.
        """
        ...

    @property
    def display_name(self) -> str:
        """Gets the name that can be displayed in a window like a properties window."""
        ...

    @overload
    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of the System.ComponentModel.MemberDescriptor class with the specified  and no attributes.
        
        This method is protected.
        """
        ...

    @overload
    def __init__(self, name: str, attributes: typing.List[System.Attribute]) -> None:
        """
        Initializes a new instance of the System.ComponentModel.MemberDescriptor class with the specified  and  array.
        
        This method is protected.
        """
        ...

    @overload
    def __init__(self, descr: System.ComponentModel.MemberDescriptor) -> None:
        """
        Initializes a new instance of the System.ComponentModel.MemberDescriptor class with the specified System.ComponentModel.MemberDescriptor.
        
        This method is protected.
        """
        ...

    @overload
    def __init__(self, old_member_descriptor: System.ComponentModel.MemberDescriptor, new_attributes: typing.List[System.Attribute]) -> None:
        """
        Initializes a new instance of the System.ComponentModel.MemberDescriptor class with the name in the specified
        System.ComponentModel.MemberDescriptor and the attributes
        in both the old System.ComponentModel.MemberDescriptor and the System.Attribute array.
        
        This method is protected.
        """
        ...

    def create_attribute_collection(self) -> System.ComponentModel.AttributeCollection:
        """
        Creates a collection of attributes using the
        array of attributes that you passed to the constructor.
        
        This method is protected.
        """
        ...

    def equals(self, obj: typing.Any) -> bool:
        """
        Compares this instance to the specified System.ComponentModel.MemberDescriptor to see if they are equivalent.
        NOTE: If you make a change here, you likely need to change GetHashCode() as well.
        """
        ...

    def fill_attributes(self, attribute_list: System.Collections.IList) -> None:
        """
        In an inheriting class, adds the attributes of the inheriting class to the
        specified list of attributes in the parent class. For duplicate attributes,
        the last one added to the list will be kept.
        
        This method is protected.
        """
        ...

    @staticmethod
    @overload
    def find_method(component_class: typing.Type, name: str, args: typing.List[typing.Type], return_type: typing.Type) -> System.Reflection.MethodInfo:
        """
        Finds the given method through reflection. This method only looks for public methods.
        
        This method is protected.
        """
        ...

    @staticmethod
    @overload
    def find_method(component_class: typing.Type, name: str, args: typing.List[typing.Type], return_type: typing.Type, public_only: bool) -> System.Reflection.MethodInfo:
        """
        Finds the given method through reflection.
        
        This method is protected.
        """
        ...

    def get_hash_code(self) -> int:
        """
        Try to keep this reasonable in [....] with Equals(). Specifically,
        if A.Equals(B) returns true, A & B should have the same hash code.
        """
        ...

    def get_invocation_target(self, type: typing.Type, instance: typing.Any) -> System.Object:
        """
        This method returns the object that should be used during invocation of members.
        Normally the return value will be the same as the instance passed in. If
        someone associated another object with this instance, or if the instance is a
        custom type descriptor, GetInvocationTarget may return a different value.
        
        This method is protected.
        """
        ...

    @staticmethod
    def get_invokee(component_class: typing.Type, component: typing.Any) -> System.Object:
        """
        This method is protected.
        
        MemberDescriptor.GetInvokee has been deprecated. Use GetInvocationTarget instead.
        """
        warnings.warn("MemberDescriptor.GetInvokee has been deprecated. Use GetInvocationTarget instead.", DeprecationWarning)

    @staticmethod
    def get_site(component: typing.Any) -> System.ComponentModel.ISite:
        """
        Gets a component site for the given component.
        
        This method is protected.
        """
        ...


class PropertyDescriptor(System.ComponentModel.MemberDescriptor, metaclass=abc.ABCMeta):
    """Provides a description of a property."""

    @property
    @abc.abstractmethod
    def component_type(self) -> typing.Type:
        """
        When overridden in a derived class, gets the type of the
        component this property is bound to.
        """
        ...

    @property
    def converter(self) -> System.ComponentModel.TypeConverter:
        """Gets the type converter for this property."""
        ...

    @property
    def converter_from_registered_type(self) -> System.ComponentModel.TypeConverter:
        """Gets the type converter for this property."""
        ...

    @property
    def is_localizable(self) -> bool:
        """
        Gets a value
        indicating whether this property should be localized, as
        specified in the System.ComponentModel.LocalizableAttribute.
        """
        ...

    @property
    @abc.abstractmethod
    def is_read_only(self) -> bool:
        """
        When overridden in a derived class, gets a value indicating whether this
        property is read-only.
        """
        ...

    @property
    def serialization_visibility(self) -> System.ComponentModel.DesignerSerializationVisibility:
        """
        Gets a value indicating whether this property should be serialized as specified
        in the System.ComponentModel.DesignerSerializationVisibilityAttribute.
        """
        ...

    @property
    @abc.abstractmethod
    def property_type(self) -> typing.Type:
        """When overridden in a derived class, gets the type of the property."""
        ...

    @property
    def supports_change_events(self) -> bool:
        """
        Indicates whether value change notifications for this property may originate from outside the property
        descriptor, such as from the component itself (value=true), or whether notifications will only originate
        from direct calls made to PropertyDescriptor.SetValue (value=false). For example, the component may
        implement the INotifyPropertyChanged interface, or may have an explicit '{name}Changed' event for this property.
        """
        ...

    @overload
    def __init__(self, name: str, attrs: typing.List[System.Attribute]) -> None:
        """
        Initializes a new instance of the System.ComponentModel.PropertyDescriptor class with the specified name and
        attributes.
        
        This method is protected.
        """
        ...

    @overload
    def __init__(self, descr: System.ComponentModel.MemberDescriptor) -> None:
        """
        Initializes a new instance of the System.ComponentModel.PropertyDescriptor class with
        the name and attributes in the specified System.ComponentModel.MemberDescriptor.
        
        This method is protected.
        """
        ...

    @overload
    def __init__(self, descr: System.ComponentModel.MemberDescriptor, attrs: typing.List[System.Attribute]) -> None:
        """
        Initializes a new instance of the System.ComponentModel.PropertyDescriptor class with
        the name in the specified System.ComponentModel.MemberDescriptor and the
        attributes in both the System.ComponentModel.MemberDescriptor and the
        System.Attribute array.
        
        This method is protected.
        """
        ...

    def add_value_changed(self, component: typing.Any, handler: typing.Callable[[System.Object, System.EventArgs], None]) -> None:
        """Allows interested objects to be notified when this property changes."""
        ...

    def can_reset_value(self, component: typing.Any) -> bool:
        """
        When overridden in a derived class, indicates whether
        resetting the will change the value of the
        .
        """
        ...

    def create_instance(self, type: typing.Type) -> System.Object:
        """
        Creates an instance of the specified type.
        
        This method is protected.
        """
        ...

    def equals(self, obj: typing.Any) -> bool:
        """
        Compares this to another System.ComponentModel.PropertyDescriptor
        to see if they are equivalent.
        NOTE: If you make a change here, you likely need to change GetHashCode() as well.
        """
        ...

    def fill_attributes(self, attribute_list: System.Collections.IList) -> None:
        """
        In an inheriting class, adds the attributes of the inheriting class to the
        specified list of attributes in the parent class. For duplicate attributes,
        the last one added to the list will be kept.
        
        This method is protected.
        """
        ...

    @overload
    def get_child_properties(self, instance: typing.Any) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    @overload
    def get_child_properties(self, instance: typing.Any, filter: typing.List[System.Attribute]) -> System.ComponentModel.PropertyDescriptorCollection:
        """Retrieves the properties"""
        ...

    @overload
    def get_child_properties(self) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    @overload
    def get_child_properties(self, filter: typing.List[System.Attribute]) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    def get_editor(self, editor_base_type: typing.Type) -> System.Object:
        """Gets an editor of the specified type."""
        ...

    def get_hash_code(self) -> int:
        """
        Try to keep this reasonable in [....] with Equals(). Specifically,
        if A.Equals(B) returns true, A & B should have the same hash code.
        """
        ...

    def get_invocation_target(self, type: typing.Type, instance: typing.Any) -> System.Object:
        """
        This method returns the object that should be used during invocation of members.
        Normally the return value will be the same as the instance passed in. If
        someone associated another object with this instance, or if the instance is a
        custom type descriptor, GetInvocationTarget may return a different value.
        
        This method is protected.
        """
        ...

    def get_type_from_name(self, type_name: str) -> typing.Type:
        """
        Gets a type using its name.
        
        This method is protected.
        """
        ...

    def get_value(self, component: typing.Any) -> System.Object:
        """When overridden in a derived class, gets the current value of the property on a component."""
        ...

    def on_value_changed(self, component: typing.Any, e: System.EventArgs) -> None:
        """
        This should be called by your property descriptor implementation
        when the property value has changed.
        
        This method is protected.
        """
        ...

    def remove_value_changed(self, component: typing.Any, handler: typing.Callable[[System.Object, System.EventArgs], None]) -> None:
        """Allows interested objects to be notified when this property changes."""
        ...

    def reset_value(self, component: typing.Any) -> None:
        """When overridden in a derived class, resets the value for this property of the component."""
        ...

    def set_value(self, component: typing.Any, value: typing.Any) -> None:
        """
        When overridden in a derived class, sets the value of
        the component to a different value.
        """
        ...

    def should_serialize_value(self, component: typing.Any) -> bool:
        """
        When overridden in a derived class, indicates whether the
        value of this property needs to be persisted.
        """
        ...


class ITypeDescriptorContext(IServiceProvider, metaclass=abc.ABCMeta):
    """
    Provides information about a context to a type converter or a value editor,
    so that the type converter or editor can perform a conversion.
    """

    @property
    @abc.abstractmethod
    def container(self) -> System.ComponentModel.IContainer:
        """Gets the container with the set of objects for this formatter."""
        ...

    @property
    @abc.abstractmethod
    def instance(self) -> System.Object:
        """Gets the instance that is invoking the method on the formatter object."""
        ...

    @property
    @abc.abstractmethod
    def property_descriptor(self) -> System.ComponentModel.PropertyDescriptor:
        """Retrieves the PropertyDescriptor that is surfacing the given context item."""
        ...

    def on_component_changed(self) -> None:
        """
        Raises the System.ComponentModel.Design.IComponentChangeService.ComponentChanged
        event.
        """
        ...

    def on_component_changing(self) -> bool:
        """Gets a value indicating whether this object can be changed."""
        ...


class PropertyDescriptorCollection(System.Object, System.Collections.IList, System.Collections.IDictionary):
    """Represents a collection of properties."""

    EMPTY: System.ComponentModel.PropertyDescriptorCollection = ...
    """An empty PropertyDescriptorCollection that can used instead of creating a new one with no items."""

    @property
    def count(self) -> int:
        """Gets the number of property descriptors in the  collection."""
        ...

    @overload
    def __getitem__(self, index: int) -> System.ComponentModel.PropertyDescriptor:
        """Gets the property with the specified index number."""
        ...

    @overload
    def __getitem__(self, name: str) -> System.ComponentModel.PropertyDescriptor:
        """Gets the property with the specified name."""
        ...

    @overload
    def __init__(self, properties: typing.List[System.ComponentModel.PropertyDescriptor]) -> None:
        """
        Initializes a new instance of the System.ComponentModel.PropertyDescriptorCollection
        class.
        """
        ...

    @overload
    def __init__(self, properties: typing.List[System.ComponentModel.PropertyDescriptor], read_only: bool) -> None:
        """
        Initializes a new instance of a property descriptor collection, and allows you to mark the
        collection as read-only so it cannot be modified.
        """
        ...

    def add(self, value: System.ComponentModel.PropertyDescriptor) -> int:
        ...

    def clear(self) -> None:
        ...

    def contains(self, value: System.ComponentModel.PropertyDescriptor) -> bool:
        ...

    def copy_to(self, array: System.Array, index: int) -> None:
        ...

    def find(self, name: str, ignore_case: bool) -> System.ComponentModel.PropertyDescriptor:
        """Gets the description of the property with the specified name."""
        ...

    def get_enumerator(self) -> System.Collections.IEnumerator:
        """Gets an enumerator for this System.ComponentModel.PropertyDescriptorCollection."""
        ...

    def index_of(self, value: System.ComponentModel.PropertyDescriptor) -> int:
        ...

    def insert(self, index: int, value: System.ComponentModel.PropertyDescriptor) -> None:
        ...

    @overload
    def internal_sort(self, names: typing.List[str]) -> None:
        """
        Sorts the members of this PropertyDescriptorCollection. Any specified NamedSort arguments will
        be applied first, followed by sort using the specified IComparer.
        
        This method is protected.
        """
        ...

    @overload
    def internal_sort(self, sorter: System.Collections.IComparer) -> None:
        """
        Sorts the members of this PropertyDescriptorCollection using the specified IComparer.
        
        This method is protected.
        """
        ...

    def remove(self, value: System.ComponentModel.PropertyDescriptor) -> None:
        ...

    def remove_at(self, index: int) -> None:
        ...

    @overload
    def sort(self) -> System.ComponentModel.PropertyDescriptorCollection:
        """
        Sorts the members of this PropertyDescriptorCollection, using the default sort for this collection,
        which is usually alphabetical.
        """
        ...

    @overload
    def sort(self, names: typing.List[str]) -> System.ComponentModel.PropertyDescriptorCollection:
        """
        Sorts the members of this PropertyDescriptorCollection. Any specified NamedSort arguments will
        be applied first, followed by sort using the specified IComparer.
        """
        ...

    @overload
    def sort(self, names: typing.List[str], comparer: System.Collections.IComparer) -> System.ComponentModel.PropertyDescriptorCollection:
        """
        Sorts the members of this PropertyDescriptorCollection. Any specified NamedSort arguments will
        be applied first, followed by sort using the specified IComparer.
        """
        ...

    @overload
    def sort(self, comparer: System.Collections.IComparer) -> System.ComponentModel.PropertyDescriptorCollection:
        """
        Sorts the members of this PropertyDescriptorCollection, using the specified IComparer to compare,
        the PropertyDescriptors contained in the collection.
        """
        ...


class TypeConverter(System.Object):
    """Converts the value of an object into a different data type."""

    class SimplePropertyDescriptor(System.ComponentModel.PropertyDescriptor, metaclass=abc.ABCMeta):
        """
        An abstract  class that provides properties for objects that do not have properties.
        
        This class is protected.
        """

        @property
        def component_type(self) -> typing.Type:
            """Gets the type of the component this property description is bound to."""
            ...

        @property
        def is_read_only(self) -> bool:
            """Gets a value indicating whether this property is read-only."""
            ...

        @property
        def property_type(self) -> typing.Type:
            """Gets the type of the property."""
            ...

        @overload
        def __init__(self, component_type: typing.Type, name: str, property_type: typing.Type) -> None:
            """
            Initializes a new instance of the System.ComponentModel.TypeConverter.SimplePropertyDescriptor class.
            
            This method is protected.
            """
            ...

        @overload
        def __init__(self, component_type: typing.Type, name: str, property_type: typing.Type, attributes: typing.List[System.Attribute]) -> None:
            """
            Initializes a new instance of the System.ComponentModel.TypeConverter.SimplePropertyDescriptor class.
            
            This method is protected.
            """
            ...

        def can_reset_value(self, component: typing.Any) -> bool:
            """Gets a value indicating whether resetting the component will change the value of the component."""
            ...

        def reset_value(self, component: typing.Any) -> None:
            """Resets the value for this property of the component."""
            ...

        def should_serialize_value(self, component: typing.Any) -> bool:
            """Gets a value indicating whether the value of this property needs to be persisted."""
            ...

    class StandardValuesCollection(System.Object, System.Collections.ICollection):
        """Represents a collection of values."""

        @property
        def count(self) -> int:
            """Gets the number of objects in the collection."""
            ...

        def __getitem__(self, index: int) -> typing.Any:
            """Gets the object at the specified index number."""
            ...

        def __init__(self, values: System.Collections.ICollection) -> None:
            """Initializes a new instance of the System.ComponentModel.TypeConverter.StandardValuesCollection class."""
            ...

        def copy_to(self, array: System.Array, index: int) -> None:
            """Copies the contents of this collection to an array."""
            ...

        def get_enumerator(self) -> System.Collections.IEnumerator:
            """Gets an enumerator for this collection."""
            ...

    @overload
    def can_convert_from(self, source_type: typing.Type) -> bool:
        """
        Gets a value indicating whether this converter can convert an object in the
        given source type to the native type of the converter.
        """
        ...

    @overload
    def can_convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, source_type: typing.Type) -> bool:
        """
        Gets a value indicating whether this converter can convert an object in the given
        source type to the native type of the converter using the context.
        """
        ...

    @overload
    def can_convert_to(self, destination_type: typing.Type) -> bool:
        """
        Gets a value indicating whether this converter can convert an object to the given
        destination type using the context.
        """
        ...

    @overload
    def can_convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, destination_type: typing.Type) -> bool:
        """
        Gets a value indicating whether this converter can convert an object to the given
        destination type using the context.
        """
        ...

    @overload
    def convert_from(self, value: typing.Any) -> System.Object:
        """Converts the given value to the converter's native type."""
        ...

    @overload
    def convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any) -> System.Object:
        """Converts the given object to the converter's native type."""
        ...

    @overload
    def convert_from_invariant_string(self, text: str) -> System.Object:
        """Converts the given string to the converter's native type using the invariant culture."""
        ...

    @overload
    def convert_from_invariant_string(self, context: System.ComponentModel.ITypeDescriptorContext, text: str) -> System.Object:
        """Converts the given string to the converter's native type using the invariant culture."""
        ...

    @overload
    def convert_from_string(self, text: str) -> System.Object:
        """Converts the specified text into an object."""
        ...

    @overload
    def convert_from_string(self, context: System.ComponentModel.ITypeDescriptorContext, text: str) -> System.Object:
        """Converts the specified text into an object."""
        ...

    @overload
    def convert_from_string(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, text: str) -> System.Object:
        """Converts the specified text into an object."""
        ...

    @overload
    def convert_to(self, value: typing.Any, destination_type: typing.Type) -> System.Object:
        """
        Converts the given
        value object to the specified destination type using the arguments.
        """
        ...

    @overload
    def convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any, destination_type: typing.Type) -> System.Object:
        """
        Converts the given value object to
        the specified destination type using the specified context and arguments.
        """
        ...

    @overload
    def convert_to_invariant_string(self, value: typing.Any) -> str:
        """Converts the specified value to a culture-invariant string representation."""
        ...

    @overload
    def convert_to_invariant_string(self, context: System.ComponentModel.ITypeDescriptorContext, value: typing.Any) -> str:
        """Converts the specified value to a culture-invariant string representation."""
        ...

    @overload
    def convert_to_string(self, value: typing.Any) -> str:
        """Converts the specified value to a string representation."""
        ...

    @overload
    def convert_to_string(self, context: System.ComponentModel.ITypeDescriptorContext, value: typing.Any) -> str:
        """Converts the specified value to a string representation."""
        ...

    @overload
    def convert_to_string(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any) -> str:
        """Converts the specified value to a string representation."""
        ...

    @overload
    def create_instance(self, property_values: System.Collections.IDictionary) -> System.Object:
        """Re-creates an object given a set of property values for the object."""
        ...

    @overload
    def create_instance(self, context: System.ComponentModel.ITypeDescriptorContext, property_values: System.Collections.IDictionary) -> System.Object:
        """Re-creates an object given a set of property values for the object."""
        ...

    def get_convert_from_exception(self, value: typing.Any) -> System.Exception:
        """
        Gets a suitable exception to throw when a conversion cannot be performed.
        
        This method is protected.
        """
        ...

    def get_convert_to_exception(self, value: typing.Any, destination_type: typing.Type) -> System.Exception:
        """
        Retrieves a suitable exception to throw when a conversion cannot
        be performed.
        
        This method is protected.
        """
        ...

    @overload
    def get_create_instance_supported(self) -> bool:
        """
        Gets a value indicating whether changing a value on this object requires a call to
        System.ComponentModel.TypeConverter.CreateInstance(IDictionary) to create a new value.
        """
        ...

    @overload
    def get_create_instance_supported(self, context: System.ComponentModel.ITypeDescriptorContext) -> bool:
        """
        Gets a value indicating whether changing a value on this object requires a call to
        System.ComponentModel.TypeConverter.CreateInstance(IDictionary) to create a new value,
        using the specified context.
        """
        ...

    @overload
    def get_properties(self, value: typing.Any) -> System.ComponentModel.PropertyDescriptorCollection:
        """Gets a collection of properties for the type of array specified by the value parameter."""
        ...

    @overload
    def get_properties(self, context: System.ComponentModel.ITypeDescriptorContext, value: typing.Any) -> System.ComponentModel.PropertyDescriptorCollection:
        """
        Gets a collection of properties for the type of array specified by the value parameter using
        the specified context.
        """
        ...

    @overload
    def get_properties(self, context: System.ComponentModel.ITypeDescriptorContext, value: typing.Any, attributes: typing.List[System.Attribute]) -> System.ComponentModel.PropertyDescriptorCollection:
        """
        Gets a collection of properties for the type of array specified by the value parameter using
        the specified context and attributes.
        """
        ...

    @overload
    def get_properties_supported(self) -> bool:
        """Gets a value indicating whether this object supports properties."""
        ...

    @overload
    def get_properties_supported(self, context: System.ComponentModel.ITypeDescriptorContext) -> bool:
        """Gets a value indicating whether this object supports properties using the specified context."""
        ...

    @overload
    def get_standard_values(self) -> System.Collections.ICollection:
        """Gets a collection of standard values for the data type this type converter is designed for."""
        ...

    @overload
    def get_standard_values(self, context: System.ComponentModel.ITypeDescriptorContext) -> System.ComponentModel.TypeConverter.StandardValuesCollection:
        """Gets a collection of standard values for the data type this type converter is designed for."""
        ...

    @overload
    def get_standard_values_exclusive(self) -> bool:
        """
        Gets a value indicating whether the collection of standard values returned from
        System.ComponentModel.TypeConverter.GetStandardValues() is an exclusive list.
        """
        ...

    @overload
    def get_standard_values_exclusive(self, context: System.ComponentModel.ITypeDescriptorContext) -> bool:
        """
        Gets a value indicating whether the collection of standard values returned from
        System.ComponentModel.TypeConverter.GetStandardValues() is an exclusive
        list of possible values, using the specified context.
        """
        ...

    @overload
    def get_standard_values_supported(self) -> bool:
        """
        Gets a value indicating whether this object supports a standard set of values
        that can be picked from a list.
        """
        ...

    @overload
    def get_standard_values_supported(self, context: System.ComponentModel.ITypeDescriptorContext) -> bool:
        """
        Gets a value indicating whether this object supports a standard set of values that can be picked
        from a list using the specified context.
        """
        ...

    @overload
    def is_valid(self, value: typing.Any) -> bool:
        """Gets a value indicating whether the given value object is valid for this type."""
        ...

    @overload
    def is_valid(self, context: System.ComponentModel.ITypeDescriptorContext, value: typing.Any) -> bool:
        """Gets a value indicating whether the given value object is valid for this type."""
        ...

    def sort_properties(self, props: System.ComponentModel.PropertyDescriptorCollection, names: typing.List[str]) -> System.ComponentModel.PropertyDescriptorCollection:
        """
        Sorts a collection of properties.
        
        This method is protected.
        """
        ...


class BaseNumberConverter(System.ComponentModel.TypeConverter, metaclass=abc.ABCMeta):
    """Provides a base type converter for integral types."""

    def can_convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, source_type: typing.Type) -> bool:
        """
        Gets a value indicating whether this converter can convert an object in the
        given source type to the TargetType object using the specified context.
        """
        ...

    def can_convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, destination_type: typing.Type) -> bool:
        ...

    def convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any) -> System.Object:
        """Converts the given value object to an object of Type TargetType."""
        ...

    def convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any, destination_type: typing.Type) -> System.Object:
        """Converts the given value object to the destination type."""
        ...


class UInt16Converter(System.ComponentModel.BaseNumberConverter):
    """
    Provides a type converter to convert 16-bit unsigned integer objects to and
    from various other representations.
    """


class ListSortDirection(Enum):
    """Specifies the direction of a sort."""

    ASCENDING = 0
    """Sort in ascending order."""

    DESCENDING = 1
    """Sort in descending order."""


class ListChangedType(Enum):
    """This class has no documentation."""

    RESET = 0

    ITEM_ADDED = 1

    ITEM_DELETED = 2

    ITEM_MOVED = 3

    ITEM_CHANGED = 4

    PROPERTY_DESCRIPTOR_ADDED = 5

    PROPERTY_DESCRIPTOR_DELETED = 6

    PROPERTY_DESCRIPTOR_CHANGED = 7


class ListChangedEventArgs(System.EventArgs):
    """This class has no documentation."""

    @property
    def list_changed_type(self) -> System.ComponentModel.ListChangedType:
        ...

    @property
    def new_index(self) -> int:
        ...

    @property
    def old_index(self) -> int:
        ...

    @property
    def property_descriptor(self) -> System.ComponentModel.PropertyDescriptor:
        ...

    @overload
    def __init__(self, list_changed_type: System.ComponentModel.ListChangedType, new_index: int) -> None:
        ...

    @overload
    def __init__(self, list_changed_type: System.ComponentModel.ListChangedType, new_index: int, prop_desc: System.ComponentModel.PropertyDescriptor) -> None:
        ...

    @overload
    def __init__(self, list_changed_type: System.ComponentModel.ListChangedType, prop_desc: System.ComponentModel.PropertyDescriptor) -> None:
        ...

    @overload
    def __init__(self, list_changed_type: System.ComponentModel.ListChangedType, new_index: int, old_index: int) -> None:
        ...


class IBindingList(System.Collections.IList, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def allow_new(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def allow_edit(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def allow_remove(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def supports_change_notification(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def supports_searching(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def supports_sorting(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def is_sorted(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def sort_property(self) -> System.ComponentModel.PropertyDescriptor:
        ...

    @property
    @abc.abstractmethod
    def sort_direction(self) -> System.ComponentModel.ListSortDirection:
        ...

    @property
    @abc.abstractmethod
    def list_changed(self) -> _EventContainer[typing.Callable[[System.Object, System.ComponentModel.ListChangedEventArgs], None], None]:
        ...

    @list_changed.setter
    def list_changed(self, value: _EventContainer[typing.Callable[[System.Object, System.ComponentModel.ListChangedEventArgs], None], None]) -> None:
        ...

    def add_index(self, property: System.ComponentModel.PropertyDescriptor) -> None:
        ...

    def add_new(self) -> System.Object:
        ...

    def apply_sort(self, property: System.ComponentModel.PropertyDescriptor, direction: System.ComponentModel.ListSortDirection) -> None:
        ...

    def find(self, property: System.ComponentModel.PropertyDescriptor, key: typing.Any) -> int:
        ...

    def remove_index(self, property: System.ComponentModel.PropertyDescriptor) -> None:
        ...

    def remove_sort(self) -> None:
        ...


class License(System.Object, System.IDisposable, metaclass=abc.ABCMeta):
    """
    Provides the abstract base class for all licenses. A license is
    granted to a specific instance of a component.
    """

    @property
    @abc.abstractmethod
    def license_key(self) -> str:
        """When overridden in a derived class, gets the license key granted to this component."""
        ...

    def dispose(self) -> None:
        """When overridden in a derived class, releases the license."""
        ...


class LicenseUsageMode(Enum):
    """Specifies when the license can be used."""

    RUNTIME = 0
    """Used during runtime."""

    DESIGNTIME = 1
    """Used during design time by a visual designer or the compiler."""


class LicenseContext(IServiceProvider):
    """Specifies when the licensed object can be used."""

    @property
    def usage_mode(self) -> System.ComponentModel.LicenseUsageMode:
        """When overridden in a derived class, gets a value that specifies when a license can be used."""
        ...

    def get_saved_license_key(self, type: typing.Type, resource_assembly: System.Reflection.Assembly) -> str:
        """
        When overridden in a derived class, gets a saved license
        key for the specified type, from the specified resource assembly.
        """
        ...

    def get_service(self, type: typing.Type) -> System.Object:
        """When overridden in a derived class, will return an object that implements the asked for service."""
        ...

    def set_saved_license_key(self, type: typing.Type, key: str) -> None:
        """When overridden in a derived class, sets a license key for the specified type."""
        ...


class LicenseProvider(System.Object, metaclass=abc.ABCMeta):
    """Provides the abstract base class for implementing a System.ComponentModel.LicenseProvider."""

    def get_license(self, context: System.ComponentModel.LicenseContext, type: typing.Type, instance: typing.Any, allow_exceptions: bool) -> System.ComponentModel.License:
        """
        When overridden in a derived class, gets a license for an or 
        of component.
        """
        ...


class LicFileLicenseProvider(System.ComponentModel.LicenseProvider):
    """
    Provides an implementation of a System.ComponentModel.LicenseProvider. The provider works in
    a similar fashion to Microsoft .NET Framework standard licensing module.
    """

    def get_key(self, type: typing.Type) -> str:
        """
        Creates a key for the specified type.
        
        This method is protected.
        """
        ...

    def get_license(self, context: System.ComponentModel.LicenseContext, type: typing.Type, instance: typing.Any, allow_exceptions: bool) -> System.ComponentModel.License:
        """Gets a license for the instance of the component and determines if it is valid."""
        ...

    def is_key_valid(self, key: str, type: typing.Type) -> bool:
        """
        Determines if the key retrieved by the System.ComponentModel.LicFileLicenseProvider.GetLicense method is valid
        for the specified type.
        
        This method is protected.
        """
        ...


class LicenseManager(System.Object):
    """
    Provides properties and methods to add a license
    to a component and to manage a System.ComponentModel.LicenseProvider. This class cannot be inherited.
    """

    current_context: System.ComponentModel.LicenseContext
    """
    Gets or sets the current System.ComponentModel.LicenseContext which specifies when the licensed object can be
    used.
    """

    USAGE_MODE: System.ComponentModel.LicenseUsageMode
    """
    Gets the System.ComponentModel.LicenseUsageMode that
    specifies when the licensed object can be used, for the System.ComponentModel.LicenseManager.CurrentContext.
    """

    @staticmethod
    @overload
    def create_with_context(type: typing.Type, creation_context: System.ComponentModel.LicenseContext) -> System.Object:
        """
        Creates an instance of the specified type, using
        creation_context
        as the context in which the licensed instance can be used.
        """
        ...

    @staticmethod
    @overload
    def create_with_context(type: typing.Type, creation_context: System.ComponentModel.LicenseContext, args: typing.List[System.Object]) -> System.Object:
        """
        Creates an instance of the specified type with the
        specified arguments, using creation_context as the context in which the licensed
        instance can be used.
        """
        ...

    @staticmethod
    def is_licensed(type: typing.Type) -> bool:
        """Determines if the given type has a valid license or not."""
        ...

    @staticmethod
    @overload
    def is_valid(type: typing.Type, instance: typing.Any, license: typing.Optional[System.ComponentModel.License]) -> typing.Tuple[bool, System.ComponentModel.License]:
        """
        Determines if a valid license can be granted for the
        specified instance of the type. This method creates a valid System.ComponentModel.License.
        """
        ...

    @staticmethod
    @overload
    def is_valid(type: typing.Type) -> bool:
        """Determines if a valid license can be granted for the specified type."""
        ...

    @staticmethod
    def lock_context(context_user: typing.Any) -> None:
        ...

    @staticmethod
    def unlock_context(context_user: typing.Any) -> None:
        ...

    @staticmethod
    @overload
    def validate(type: typing.Type, instance: typing.Any) -> System.ComponentModel.License:
        """Determines if a license can be granted for the instance of the specified type."""
        ...

    @staticmethod
    @overload
    def validate(type: typing.Type) -> None:
        """Determines if a license can be granted for the specified type."""
        ...


class DefaultBindingPropertyAttribute(System.Attribute):
    """Specifies the default binding property for a component."""

    @property
    def name(self) -> str:
        """
        Gets the name of the default binding property for the component this attribute is
        bound to.
        """
        ...

    DEFAULT: System.ComponentModel.DefaultBindingPropertyAttribute = ...
    """
    Specifies the default value for the System.ComponentModel.DefaultBindingPropertyAttribute, which is null. This
    static field is read-only.
    """

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the System.ComponentModel.DefaultBindingPropertyAttribute class."""
        ...

    @overload
    def __init__(self, name: str) -> None:
        """Initializes a new instance of the System.ComponentModel.DefaultBindingPropertyAttribute class."""
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...


class BooleanConverter(System.ComponentModel.TypeConverter):
    """Provides a type converter to convert Boolean objects to and from various other representations."""

    def can_convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, source_type: typing.Type) -> bool:
        """
        Gets a value indicating whether this converter can convert an object
        in the given source type to a Boolean object using the specified context.
        """
        ...

    def convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any) -> System.Object:
        """
        Converts the given value
        object to a Boolean object.
        """
        ...

    def get_standard_values(self, context: System.ComponentModel.ITypeDescriptorContext) -> System.ComponentModel.TypeConverter.StandardValuesCollection:
        """Gets a collection of standard values for the Boolean data type."""
        ...

    def get_standard_values_exclusive(self, context: System.ComponentModel.ITypeDescriptorContext) -> bool:
        """
        Gets a value indicating whether the list of standard values returned from
        System.ComponentModel.BooleanConverter.GetStandardValues is an exclusive list.
        """
        ...

    def get_standard_values_supported(self, context: System.ComponentModel.ITypeDescriptorContext) -> bool:
        """
        Gets a value indicating whether this object supports a standard set of values that can
        be picked from a list.
        """
        ...


class CollectionConverter(System.ComponentModel.TypeConverter):
    """
    Provides a type converter to convert collection objects to and from various other
    representations.
    """

    def convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any, destination_type: typing.Type) -> System.Object:
        """Converts the given value object to the specified destination type."""
        ...

    def get_properties(self, context: System.ComponentModel.ITypeDescriptorContext, value: typing.Any, attributes: typing.List[System.Attribute]) -> System.ComponentModel.PropertyDescriptorCollection:
        """
        Gets a collection of properties for the type of array specified by the value
        parameter using the specified context and attributes.
        """
        ...


class ArrayConverter(System.ComponentModel.CollectionConverter):
    """
    Provides a type converter to convert System.Array
    objects to and from various other representations.
    """

    def convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any, destination_type: typing.Type) -> System.Object:
        """Converts the given value object to the specified destination type."""
        ...

    def get_properties(self, context: System.ComponentModel.ITypeDescriptorContext, value: typing.Any, attributes: typing.List[System.Attribute]) -> System.ComponentModel.PropertyDescriptorCollection:
        """Gets a collection of properties for the type of array specified by the value parameter."""
        ...

    def get_properties_supported(self, context: System.ComponentModel.ITypeDescriptorContext) -> bool:
        """Gets a value indicating whether this object supports properties."""
        ...


class ListSortDescription(System.Object):
    """This class has no documentation."""

    @property
    def property_descriptor(self) -> System.ComponentModel.PropertyDescriptor:
        ...

    @property_descriptor.setter
    def property_descriptor(self, value: System.ComponentModel.PropertyDescriptor) -> None:
        ...

    @property
    def sort_direction(self) -> System.ComponentModel.ListSortDirection:
        ...

    @sort_direction.setter
    def sort_direction(self, value: System.ComponentModel.ListSortDirection) -> None:
        ...

    def __init__(self, property: System.ComponentModel.PropertyDescriptor, direction: System.ComponentModel.ListSortDirection) -> None:
        ...


class ListSortDescriptionCollection(System.Object, System.Collections.IList):
    """This class has no documentation."""

    @property
    def count(self) -> int:
        ...

    def __getitem__(self, index: int) -> System.ComponentModel.ListSortDescription:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, sorts: typing.List[System.ComponentModel.ListSortDescription]) -> None:
        ...

    def __setitem__(self, index: int, value: System.ComponentModel.ListSortDescription) -> None:
        ...

    def contains(self, value: typing.Any) -> bool:
        ...

    def copy_to(self, array: System.Array, index: int) -> None:
        ...

    def index_of(self, value: typing.Any) -> int:
        ...


class IBindingListView(System.ComponentModel.IBindingList, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def filter(self) -> str:
        ...

    @filter.setter
    def filter(self, value: str) -> None:
        ...

    @property
    @abc.abstractmethod
    def sort_descriptions(self) -> System.ComponentModel.ListSortDescriptionCollection:
        ...

    @property
    @abc.abstractmethod
    def supports_advanced_sorting(self) -> bool:
        ...

    @property
    @abc.abstractmethod
    def supports_filtering(self) -> bool:
        ...

    def apply_sort(self, sorts: System.ComponentModel.ListSortDescriptionCollection) -> None:
        ...

    def remove_filter(self) -> None:
        ...


class DataObjectMethodType(Enum):
    """This class has no documentation."""

    FILL = 0

    SELECT = 1

    UPDATE = 2

    INSERT = 3

    DELETE = 4


class DataObjectMethodAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def is_default(self) -> bool:
        ...

    @property
    def method_type(self) -> System.ComponentModel.DataObjectMethodType:
        ...

    @overload
    def __init__(self, method_type: System.ComponentModel.DataObjectMethodType) -> None:
        ...

    @overload
    def __init__(self, method_type: System.ComponentModel.DataObjectMethodType, is_default: bool) -> None:
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def match(self, obj: typing.Any) -> bool:
        ...


class ComplexBindingPropertiesAttribute(System.Attribute):
    """Specifies the data source and data member properties for a component."""

    @property
    def data_source(self) -> str:
        """
        Gets the name of the data source property for the component this attribute is
        bound to.
        """
        ...

    @property
    def data_member(self) -> str:
        """
        Gets the name of the data member property for the component this attribute is
        bound to.
        """
        ...

    DEFAULT: System.ComponentModel.ComplexBindingPropertiesAttribute = ...
    """
    Specifies the default value for the System.ComponentModel.ComplexBindingPropertiesAttribute, which is null. This
    static field is read-only.
    """

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the System.ComponentModel.ComplexBindingPropertiesAttribute class."""
        ...

    @overload
    def __init__(self, data_source: str) -> None:
        """Initializes a new instance of the System.ComponentModel.ComplexBindingPropertiesAttribute class."""
        ...

    @overload
    def __init__(self, data_source: str, data_member: str) -> None:
        """Initializes a new instance of the System.ComponentModel.ComplexBindingPropertiesAttribute class."""
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...


class UInt64Converter(System.ComponentModel.BaseNumberConverter):
    """
    Provides a type converter to convert 64-bit unsigned integer objects to and
    from various other representations.
    """


class ToolboxItemFilterType(Enum):
    """Specifies the type of filter in a ToolboxItemFilterAttribute."""

    ALLOW = 0
    """
    Specifies that a toolbox item filter string may be allowed. Allowed is typically used to
    specify that you support the filter string, but don't care if it is accepted or rejected.
    """

    CUSTOM = 1
    """
    Specifies that a toolbox item filter string will require custom processing. This is generally
    specified on the root designer class to indicate that the designer wishes to accept or reject
    a toolbox item through code. The designer must implement IToolboxUser's IsSupported method.
    """

    PREVENT = 2
    """
    Specifies that a toolbox item filter string should be rejected. If a designer and a component
    class both have the filter string and one has a type of Prevent, the toolbox item will not
    be available.
    """

    REQUIRE = 3
    """
    Specifies that a toolbox item filter string must be present for a toolbox item to be enabled.
    A designer and component class must both have the filter string, and neither may have a filter
    type of Prevent.
    """


class ToolboxItemFilterAttribute(System.Attribute):
    """
    This attribute allows you to configure a filter that is used enable or disable toolbox items
    from being used on particular designers. For example, you may have a class of components
    that can only be used on a certain type of designer. You can configure a toolbox item
    filter to enforce that rule. For example, take a report designer that uses a component
    base class of ReportElement. You may want to make ReportElement toolbox items enabled only
    when a ReportDesigner is the active designer. To do this, you would add the following
    ToolboxItemFilter attributes to each class:
    
    [ToolboxItemFilter("MyReportFilterString", ToolboxItemFilterType.Require)]
    public class ReportElement : Component {}
    
    [ToolboxItemFilter("MyReportFilterString", ToolboxItemFilterType.Require)]
    public class ReportDesigner : Component {}
    
    These two filters specify that ReportElement toolbox items will only be
    enabled when a ReportDesigner is visible. By specifying a filter type of
    Require on the report designer class, this will disable any toolbox items
    that are not report elements. If the report designer specified a filter type
    of "Allow" instead of "Require", other components would be enabled when the
    report designer was active. ReportElements would still be disabled when
    other designers were active, however, because ReportElement requires designers
    to have the given filter string.
    
    Toolbox item filtering is a useful way to restrict toolbox item visibility to
    cases where it is appropriate. This can help to avoid confusion for users, but
    you should use caution not to make items unusually restrictive. If you have a
    general purpose component, for example, you should allow the component to appear
    on any designer.
    
    The ASP.NET and Windows Forms designers both use filter attributes to prevent
    each other's components from being enabled. This is a useful restriction because,
    since each has several duplicate class names, it may be confusing to users and
    they may not know which controls to choose.
    """

    @property
    def filter_string(self) -> str:
        """
        Retrieves the filter string for this attribute. The filter string is a user-defined string that
        is used to identify matching attributes.
        """
        ...

    @property
    def filter_type(self) -> System.ComponentModel.ToolboxItemFilterType:
        """
        Retrieves the filter type for this attribute. The filter type determines how the filter string should
        be applied.
        """
        ...

    @property
    def type_id(self) -> System.Object:
        """
        The unique identifier for this attribute. All ToolboxItemFilterAttributes with the same filter string
        are considered the same, so they return the same TypeId.
        """
        ...

    @overload
    def __init__(self, filter_string: str) -> None:
        """
        Initializes a new ToolboxItemFilterAttribute with the provide filter string and a filter type of
        "Allow".
        """
        ...

    @overload
    def __init__(self, filter_string: str, filter_type: System.ComponentModel.ToolboxItemFilterType) -> None:
        """Initializes a new ToolboxItemFilterAttribute with the provide filter string and filter type."""
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def match(self, obj: typing.Any) -> bool:
        ...

    def to_string(self) -> str:
        ...


class TimeSpanConverter(System.ComponentModel.TypeConverter):
    """
    Provides a type converter to convert System.TimeSpan objects to and from
    various other representations.
    """

    def can_convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, source_type: typing.Type) -> bool:
        """
        Gets a value indicating whether this converter can
        convert an object in the given source type to a System.TimeSpan object using the
        specified context.
        """
        ...

    def can_convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, destination_type: typing.Type) -> bool:
        """
        Gets a value indicating whether this converter can convert an object to the given
        destination type using the context.
        """
        ...

    def convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any) -> System.Object:
        """
        Converts the given object to a System.TimeSpan
        object.
        """
        ...

    def convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any, destination_type: typing.Type) -> System.Object:
        """
        Converts the given object to another type. The most common types to convert
        are to and from a string object. The default implementation will make a call
        to ToString on the object if the object is valid and if the destination
        type is string. If this cannot convert to the destination type, this will
        throw a NotSupportedException.
        """
        ...


class CollectionChangeAction(Enum):
    """Specifies how the collection is changed."""

    ADD = 1
    """Specifies that an element is added to the collection."""

    REMOVE = 2
    """Specifies that an element is removed from the collection."""

    REFRESH = 3
    """Specifies that the entire collection has changed."""


class VersionConverter(System.ComponentModel.TypeConverter):
    """
    Provides a type converter to convert Version objects to and
          from various other representations.
    """

    def can_convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, source_type: typing.Type) -> bool:
        """
        Gets a value indicating whether this converter can convert an object in the
              given source type to a Version.
        """
        ...

    def can_convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, destination_type: typing.Type) -> bool:
        """
        Gets a value indicating whether this converter can
              convert an object to the given destination type using the context.
        """
        ...

    def convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any) -> System.Object:
        """Converts the given object to a Version."""
        ...

    def convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any, destination_type: typing.Type) -> System.Object:
        """
        Converts the given value object to
              the specified destination type using the specified context and arguments.
        """
        ...

    def is_valid(self, context: System.ComponentModel.ITypeDescriptorContext, value: typing.Any) -> bool:
        ...


class ReferenceConverter(System.ComponentModel.TypeConverter):
    """
    Provides a type converter to convert object references to and from various
    other representations.
    """

    def __init__(self, type: typing.Type) -> None:
        """Initializes a new instance of the System.ComponentModel.ReferenceConverter class."""
        ...

    def can_convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, source_type: typing.Type) -> bool:
        """
        Gets a value indicating whether this converter can convert an object in the
        given source type to a reference object using the specified context.
        """
        ...

    def convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any) -> System.Object:
        """Converts the given object to the reference type."""
        ...

    def convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any, destination_type: typing.Type) -> System.Object:
        """Converts the given value object to the reference type using the specified context and arguments."""
        ...

    def get_standard_values(self, context: System.ComponentModel.ITypeDescriptorContext) -> System.ComponentModel.TypeConverter.StandardValuesCollection:
        """Gets a collection of standard values for the reference data type."""
        ...

    def get_standard_values_exclusive(self, context: System.ComponentModel.ITypeDescriptorContext) -> bool:
        """
        Gets a value indicating whether the list of standard values returned from
        System.ComponentModel.ReferenceConverter.GetStandardValues is an exclusive list.
        """
        ...

    def get_standard_values_supported(self, context: System.ComponentModel.ITypeDescriptorContext) -> bool:
        """
        Gets a value indicating whether this object supports a standard set of values
        that can be picked from a list.
        """
        ...

    def is_value_allowed(self, context: System.ComponentModel.ITypeDescriptorContext, value: typing.Any) -> bool:
        """
        Gets a value indicating whether a particular value can be added to
        the standard values collection.
        
        This method is protected.
        """
        ...


class DecimalConverter(System.ComponentModel.BaseNumberConverter):
    """
    Provides a type converter to convert decimal
    objects to and from various other representations.
    """

    def can_convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, destination_type: typing.Type) -> bool:
        """
        Gets a value indicating whether this converter can convert an
        object to the given destination type using the context.
        """
        ...

    def convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any, destination_type: typing.Type) -> System.Object:
        """
        Converts the given object to another type. The most common types to convert
        are to and from a string object. The default implementation will make a call
        to ToString on the object if the object is valid and if the destination
        type is string. If this cannot convert to the destination type, this will
        throw a NotSupportedException.
        """
        ...


class GuidConverter(System.ComponentModel.TypeConverter):
    """
    Provides a type converter to convert globally unique identifier objects to and from various
    other representations.
    """

    def can_convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, source_type: typing.Type) -> bool:
        """
        Gets a value indicating whether this converter can convert an object in the given source
        type to a globally unique identifier object using the context.
        """
        ...

    def can_convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, destination_type: typing.Type) -> bool:
        """
        Gets a value indicating whether this converter can convert an object to
        the given destination type using the context.
        """
        ...

    def convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any) -> System.Object:
        """Converts the given object to a globally unique identifier object."""
        ...

    def convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any, destination_type: typing.Type) -> System.Object:
        """
        Converts the given object to another type. The most common types to convert
        are to and from a string object. The default implementation will make a call
        to ToString on the object if the object is valid and if the destination
        type is string. If this cannot convert to the destination type, this will
        throw a NotSupportedException.
        """
        ...


class SByteConverter(System.ComponentModel.BaseNumberConverter):
    """
    Provides a type converter to convert 8-bit unsigned integer objects to and from
    various other representations.
    """


class EventDescriptor(System.ComponentModel.MemberDescriptor, metaclass=abc.ABCMeta):
    """Provides a description of an event."""

    @property
    @abc.abstractmethod
    def component_type(self) -> typing.Type:
        """When overridden in a derived class, gets the type of the component this event is bound to."""
        ...

    @property
    @abc.abstractmethod
    def event_type(self) -> typing.Type:
        """When overridden in a derived class, gets the type of delegate for the event."""
        ...

    @property
    @abc.abstractmethod
    def is_multicast(self) -> bool:
        """
        When overridden in a derived class, gets a value indicating whether the event delegate is
        a multicast delegate.
        """
        ...

    @overload
    def __init__(self, name: str, attrs: typing.List[System.Attribute]) -> None:
        """
        Initializes a new instance of the System.ComponentModel.EventDescriptor class with the
        specified name and attribute array.
        
        This method is protected.
        """
        ...

    @overload
    def __init__(self, descr: System.ComponentModel.MemberDescriptor) -> None:
        """
        Initializes a new instance of the System.ComponentModel.EventDescriptor class with the name and attributes in
        the specified System.ComponentModel.MemberDescriptor.
        
        This method is protected.
        """
        ...

    @overload
    def __init__(self, descr: System.ComponentModel.MemberDescriptor, attrs: typing.List[System.Attribute]) -> None:
        """
        Initializes a new instance of the System.ComponentModel.EventDescriptor class with
        the name in the specified System.ComponentModel.MemberDescriptor and the
        attributes in both the System.ComponentModel.MemberDescriptor and the System.Attribute array.
        
        This method is protected.
        """
        ...

    def add_event_handler(self, component: typing.Any, value: System.Delegate) -> None:
        """When overridden in a derived class, binds the event to the component."""
        ...

    def remove_event_handler(self, component: typing.Any, value: System.Delegate) -> None:
        """
        When overridden in a derived class, unbinds the delegate from the component
        so that the delegate will no longer receive events from the component.
        """
        ...


class EventDescriptorCollection(System.Object, System.Collections.IList):
    """Represents a collection of events."""

    EMPTY: System.ComponentModel.EventDescriptorCollection = ...
    """An empty AttributeCollection that can used instead of creating a new one with no items."""

    @property
    def count(self) -> int:
        """Gets the number of event descriptors in the collection."""
        ...

    @overload
    def __getitem__(self, index: int) -> System.ComponentModel.EventDescriptor:
        """Gets the event with the specified index number."""
        ...

    @overload
    def __getitem__(self, name: str) -> System.ComponentModel.EventDescriptor:
        """Gets the event with the specified name."""
        ...

    @overload
    def __init__(self, events: typing.List[System.ComponentModel.EventDescriptor]) -> None:
        """Initializes a new instance of the System.ComponentModel.EventDescriptorCollection class."""
        ...

    @overload
    def __init__(self, events: typing.List[System.ComponentModel.EventDescriptor], read_only: bool) -> None:
        """
        Initializes a new instance of an event descriptor collection, and allows you to mark the
        collection as read-only so it cannot be modified.
        """
        ...

    def add(self, value: System.ComponentModel.EventDescriptor) -> int:
        ...

    def clear(self) -> None:
        ...

    def contains(self, value: System.ComponentModel.EventDescriptor) -> bool:
        ...

    def find(self, name: str, ignore_case: bool) -> System.ComponentModel.EventDescriptor:
        """
        Gets the description of the event with the specified
        name in the collection.
        """
        ...

    def get_enumerator(self) -> System.Collections.IEnumerator:
        """Gets an enumerator for this System.ComponentModel.EventDescriptorCollection."""
        ...

    def index_of(self, value: System.ComponentModel.EventDescriptor) -> int:
        ...

    def insert(self, index: int, value: System.ComponentModel.EventDescriptor) -> None:
        ...

    @overload
    def internal_sort(self, names: typing.List[str]) -> None:
        """
        Sorts the members of this EventDescriptorCollection. Any specified NamedSort arguments will
        be applied first, followed by sort using the specified IComparer.
        
        This method is protected.
        """
        ...

    @overload
    def internal_sort(self, sorter: System.Collections.IComparer) -> None:
        """
        Sorts the members of this EventDescriptorCollection using the specified IComparer.
        
        This method is protected.
        """
        ...

    def remove(self, value: System.ComponentModel.EventDescriptor) -> None:
        ...

    def remove_at(self, index: int) -> None:
        ...

    @overload
    def sort(self) -> System.ComponentModel.EventDescriptorCollection:
        """
        Sorts the members of this EventDescriptorCollection, using the default sort for this collection,
        which is usually alphabetical.
        """
        ...

    @overload
    def sort(self, names: typing.List[str]) -> System.ComponentModel.EventDescriptorCollection:
        """
        Sorts the members of this EventDescriptorCollection. Any specified NamedSort arguments will
        be applied first, followed by sort using the specified IComparer.
        """
        ...

    @overload
    def sort(self, names: typing.List[str], comparer: System.Collections.IComparer) -> System.ComponentModel.EventDescriptorCollection:
        """
        Sorts the members of this EventDescriptorCollection. Any specified NamedSort arguments will
        be applied first, followed by sort using the specified IComparer.
        """
        ...

    @overload
    def sort(self, comparer: System.Collections.IComparer) -> System.ComponentModel.EventDescriptorCollection:
        """
        Sorts the members of this EventDescriptorCollection, using the specified IComparer to compare,
        the EventDescriptors contained in the collection.
        """
        ...


class ICustomTypeDescriptor(metaclass=abc.ABCMeta):
    """Provides an interface that provides custom type information for an object."""

    @property
    @abc.abstractmethod
    def require_registered_types(self) -> typing.Optional[bool]:
        """Whether types are required to be registered through TypeDescriptionProvider.RegisterType{T}."""
        ...

    def get_attributes(self) -> System.ComponentModel.AttributeCollection:
        """
        Gets a collection of type System.Attribute with the attributes
        for this object.
        """
        ...

    def get_class_name(self) -> str:
        """Gets the class name of this object."""
        ...

    def get_component_name(self) -> str:
        """Gets the name of this object."""
        ...

    def get_converter(self) -> System.ComponentModel.TypeConverter:
        """Gets a type converter for this object."""
        ...

    def get_converter_from_registered_type(self) -> System.ComponentModel.TypeConverter:
        """Gets a type converter for this object that may be registered."""
        ...

    def get_default_event(self) -> System.ComponentModel.EventDescriptor:
        """Gets the default event for this object."""
        ...

    def get_default_property(self) -> System.ComponentModel.PropertyDescriptor:
        """Gets the default property for this object."""
        ...

    def get_editor(self, editor_base_type: typing.Type) -> System.Object:
        """Gets an editor of the specified type for this object."""
        ...

    @overload
    def get_events(self) -> System.ComponentModel.EventDescriptorCollection:
        """Gets the events for this instance of a component."""
        ...

    @overload
    def get_events(self, attributes: typing.List[System.Attribute]) -> System.ComponentModel.EventDescriptorCollection:
        """
        Gets the events for this instance of a component using the attribute array as a
        filter.
        """
        ...

    def get_events_from_registered_type(self) -> System.ComponentModel.EventDescriptorCollection:
        """Gets the events for this instance of a component that may be registered."""
        ...

    @overload
    def get_properties(self) -> System.ComponentModel.PropertyDescriptorCollection:
        """Gets the properties for this instance of a component."""
        ...

    @overload
    def get_properties(self, attributes: typing.List[System.Attribute]) -> System.ComponentModel.PropertyDescriptorCollection:
        """Gets the properties for this instance of a component using the attribute array as a filter."""
        ...

    def get_properties_from_registered_type(self) -> System.ComponentModel.PropertyDescriptorCollection:
        """Gets the properties for this instance of a component that may be registered."""
        ...

    def get_property_owner(self, pd: System.ComponentModel.PropertyDescriptor) -> System.Object:
        """Gets the object that directly depends on this value being edited."""
        ...


class TypeDescriptionProvider(System.Object, metaclass=abc.ABCMeta):
    """
    The TypeDescriptionProvider class can be thought of as a "plug-in" for
    TypeDescriptor. There can be multiple type description provider classes
    all offering metadata to TypeDescriptor
    """

    @property
    def require_registered_types(self) -> typing.Optional[bool]:
        """
        Whether the provider uses reflection and requires types to be registered through TypeDescriptor.RegisterType{T}
        to support trimmed applications. For backwards compatibility, this is typically only enforced when calling members that have
        a "FromRegisteredType" suffix.
        """
        ...

    @overload
    def __init__(self) -> None:
        """
        There are two versions of the constructor for this class. The empty
        constructor is identical to using TypeDescriptionProvider(null).
        If a child type description provider is passed into the constructor,
        the "base" versions of all methods will call to this parent provider.
        If no such provider is given, the base versions of the methods will
        return empty, but valid values.
        
        This method is protected.
        """
        ...

    @overload
    def __init__(self, parent: System.ComponentModel.TypeDescriptionProvider) -> None:
        """
        There are two versions of the constructor for this class. The empty
        constructor is identical to using TypeDescriptionProvider(null).
        If a child type description provider is passed into the constructor,
        the "base" versions of all methods will call to this parent provider.
        If no such provider is given, the base versions of the methods will
        return empty, but valid values.
        
        This method is protected.
        """
        ...

    def create_instance(self, provider: typing.Optional[IServiceProvider], object_type: typing.Type, arg_types: typing.List[typing.Type], args: typing.List[System.Object]) -> System.Object:
        """
        This method is used to create an instance that can substitute for another
        data type. If the method is not interested in providing a substitute
        instance, it should call base.
        
        This method is prototyped as virtual, and by default returns null if no
        parent provider was passed. If a parent provider was passed, this
        method will invoke the parent provider's CreateInstance method.
        """
        ...

    def get_cache(self, instance: typing.Any) -> System.Collections.IDictionary:
        """
        TypeDescriptor may need to perform complex operations on collections of metadata.
        Since types are not unloaded for the life of a domain, TypeDescriptor will
        automatically cache the results of these operations based on type. There are a
        number of operations that use live object instances, however. These operations
        cannot be cached within TypeDescriptor because caching them would prevent the
        object from garbage collecting. Instead, TypeDescriptor allows for a per-object
        cache, accessed as an IDictionary of key/value pairs, to exist on an object.
        The GetCache method returns an instance of this cache. GetCache will return
        null if there is no supported cache for an object.
        """
        ...

    def get_extended_type_descriptor(self, instance: typing.Any) -> System.ComponentModel.ICustomTypeDescriptor:
        """
        This method returns an extended custom type descriptor for the given object.
        An extended type descriptor is a custom type descriptor that offers properties
        that other objects have added to this object, but are not actually defined on
        the object. For example, in the .NET Framework Component Model, objects that
        implement the interface IExtenderProvider can "attach" properties to other
        objects that reside in the same logical container. The GetTypeDescriptor
        method does not return a type descriptor that provides these extra extended
        properties. GetExtendedTypeDescriptor returns the set of these extended
        properties. TypeDescriptor will automatically merge the results of these
        two property collections. Note that while the .NET Framework component
        model only supports extended properties this API can be used for extended
        attributes and events as well, if the type description provider supports it.
        """
        ...

    def get_extended_type_descriptor_from_registered_type(self, instance: typing.Any) -> System.ComponentModel.ICustomTypeDescriptor:
        """
        This method returns an extended custom type descriptor for the given object.
        An extended type descriptor is a custom type descriptor that offers properties
        that other objects have added to this object, but are not actually defined on
        the object. For example, in the .NET Framework Component Model, objects that
        implement the interface IExtenderProvider can "attach" properties to other
        objects that reside in the same logical container. The GetTypeDescriptor
        method does not return a type descriptor that provides these extra extended
        properties. GetExtendedTypeDescriptor returns the set of these extended
        properties. TypeDescriptor will automatically merge the results of these
        two property collections. Note that while the .NET Framework component
        model only supports extended properties this API can be used for extended
        attributes and events as well, if the type description provider supports it.
        """
        ...

    def get_full_component_name(self, component: typing.Any) -> str:
        """
        The name of the specified component, or null if the component has no name.
        In many cases this will return the same value as GetComponentName. If the
        component resides in a nested container or has other nested semantics, it may
        return a different fully qualified name.
        
        If not overridden, the default implementation of this method will call
        GetTypeDescriptor.GetComponentName.
        """
        ...

    @overload
    def get_reflection_type(self, instance: typing.Any) -> typing.Type:
        """
        The GetReflection method is a lower level version of GetTypeDescriptor.
        If no custom type descriptor can be located for an object, GetReflectionType
        is called to perform normal reflection against the object.
        
        This method is prototyped as virtual, and by default returns the
        object type if no parent provider was passed. If a parent provider was passed, this
        method will invoke the parent provider's GetReflectionType method.
        """
        ...

    @overload
    def get_reflection_type(self, object_type: typing.Type, instance: typing.Any) -> typing.Type:
        """
        The GetReflection method is a lower level version of GetTypeDescriptor.
        If no custom type descriptor can be located for an object, GetReflectionType
        is called to perform normal reflection against the object.
        
        This method is prototyped as virtual, and by default returns the
        object type if no parent provider was passed. If a parent provider was passed, this
        method will invoke the parent provider's GetReflectionType method.
        """
        ...

    @overload
    def get_reflection_type(self, object_type: typing.Type) -> typing.Type:
        """
        The GetReflection method is a lower level version of GetTypeDescriptor.
        If no custom type descriptor can be located for an object, GetReflectionType
        is called to perform normal reflection against the object.
        """
        ...

    def get_runtime_type(self, reflection_type: typing.Type) -> typing.Type:
        """
        The GetRuntimeType method reverses GetReflectionType to convert a reflection type
        back into a runtime type. Historically the Type.UnderlyingSystemType property has
        been used to return the runtime type. This isn't exactly correct, but it needs
        to be preserved unless all type description providers are revised.
        """
        ...

    @overload
    def get_type_descriptor(self, instance: typing.Any) -> System.ComponentModel.ICustomTypeDescriptor:
        """
        This method returns a custom type descriptor for the given type / object.
        The objectType parameter is always valid, but the instance parameter may
        be null if no instance was passed to TypeDescriptor. The method should
        return a custom type descriptor for the object. If the method is not
        interested in providing type information for the object it should
        return base.
        """
        ...

    @overload
    def get_type_descriptor(self, object_type: typing.Type, instance: typing.Any) -> System.ComponentModel.ICustomTypeDescriptor:
        """
        This method returns a custom type descriptor for the given type / object.
        The object_type parameter is always valid, but the instance parameter may
        be null if no instance was passed to TypeDescriptor. The method should
        return a custom type descriptor for the object. If the method is not
        interested in providing type information for the object it should
        return base.
        
        This method is prototyped as virtual, and by default returns a
        custom type descriptor that returns empty collections for all values
        if no parent provider was passed. If a parent provider was passed,
        this method will invoke the parent provider's GetTypeDescriptor
        method.
        """
        ...

    @overload
    def get_type_descriptor(self, object_type: typing.Type) -> System.ComponentModel.ICustomTypeDescriptor:
        """
        This method returns a custom type descriptor for the given type / object.
        The object_type parameter is always valid, but the instance parameter may
        be null if no instance was passed to TypeDescriptor. The method should
        return a custom type descriptor for the object. If the method is not
        interested in providing type information for the object it should
        return base.
        """
        ...

    @overload
    def get_type_descriptor_from_registered_type(self, instance: typing.Any) -> System.ComponentModel.ICustomTypeDescriptor:
        """
        This method returns a custom type descriptor for the given type / object.
        The objectType parameter is always valid, but the instance parameter may
        be null if no instance was passed to TypeDescriptor. The method should
        return a custom type descriptor for the object. If the method is not
        interested in providing type information for the object it should
        return base.
        """
        ...

    @overload
    def get_type_descriptor_from_registered_type(self, object_type: typing.Type, instance: typing.Any) -> System.ComponentModel.ICustomTypeDescriptor:
        """
        This method returns a custom type descriptor for the given type / object.
        The object_type parameter is always valid, but the instance parameter may
        be null if no instance was passed to TypeDescriptor. The method should
        return a custom type descriptor for the object. If the method is not
        interested in providing type information for the object it should
        return base.
        
        This method is prototyped as virtual, and by default returns a
        custom type descriptor that returns empty collections for all values
        if no parent provider was passed. If a parent provider was passed,
        this method will invoke the parent provider's GetTypeDescriptorFromRegisteredType
        method.
        """
        ...

    @overload
    def get_type_descriptor_from_registered_type(self, object_type: typing.Type) -> System.ComponentModel.ICustomTypeDescriptor:
        """
        This method returns a custom type descriptor for the given type / object.
        The object_type parameter is always valid, but the instance parameter may
        be null if no instance was passed to TypeDescriptor. The method should
        return a custom type descriptor for the object. If the method is not
        interested in providing type information for the object it should
        return base.
        """
        ...

    def is_registered_type(self, type: typing.Type) -> bool:
        """Returns whether the type was registered with its provider through TypeDescriptor.RegisterType{T}."""
        ...

    def is_supported_type(self, type: typing.Type) -> bool:
        """
        This method returns true if the type is "supported" by the type descriptor
        and its chain of type description providers.
        """
        ...


class PasswordPropertyTextAttribute(System.Attribute):
    """
    If this attribute is placed on a property or a type, its text representation in a property window
    will appear as dots or asterisks to indicate a password field. This indication in no way
    represents any type of encryption or security.
    """

    YES: System.ComponentModel.PasswordPropertyTextAttribute = ...
    """
    Sets the System.ComponentModel.Design.PasswordPropertyText
    attribute by default to true.
    """

    NO: System.ComponentModel.PasswordPropertyTextAttribute = ...
    """
    Sets the System.ComponentModel.Design.PasswordPropertyText
    attribute by default to false.
    """

    DEFAULT: System.ComponentModel.PasswordPropertyTextAttribute = ...
    """
    Sets the System.ComponentModel.Design.PasswordPropertyText
    attribute by default to false.
    """

    @property
    def password(self) -> bool:
        """Gets a value indicating if the property this attribute is defined for should be shown as password text."""
        ...

    @overload
    def __init__(self) -> None:
        """Creates a default PasswordPropertyTextAttribute."""
        ...

    @overload
    def __init__(self, password: bool) -> None:
        """Creates a PasswordPropertyTextAttribute with the given password value."""
        ...

    def equals(self, o: typing.Any) -> bool:
        """Overload for object equality"""
        ...

    def get_hash_code(self) -> int:
        """Returns the hashcode for this object."""
        ...

    def is_default_attribute(self) -> bool:
        """Gets a value indicating whether this attribute is set to true by default."""
        ...


class AttributeProviderAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def type_name(self) -> str:
        """
        The TypeName property returns the assembly qualified type name
        passed into the constructor.
        """
        ...

    @property
    def property_name(self) -> str:
        """The TypeName property returns the property name that will be used to query attributes from."""
        ...

    @overload
    def __init__(self, type_name: str) -> None:
        """Creates a new AttributeProviderAttribute object."""
        ...

    @overload
    def __init__(self, type_name: str, property_name: str) -> None:
        """Creates a new AttributeProviderAttribute object."""
        ...

    @overload
    def __init__(self, type: typing.Type) -> None:
        """Creates a new AttributeProviderAttribute object."""
        ...


class BindableSupport(Enum):
    """
    Specifies which values to say if property or event value can be bound to a data
    element or another property or event's value.
    """

    NO = ...
    """The property or event is bindable."""

    YES = ...
    """The property or event is not bindable."""

    DEFAULT = ...
    """The property or event is the default."""


class CollectionChangeEventArgs(System.EventArgs):
    """Provides data for the CollectionChange  event."""

    @property
    def action(self) -> System.ComponentModel.CollectionChangeAction:
        """Gets an action that specifies how the collection changed."""
        ...

    @property
    def element(self) -> System.Object:
        """Gets the instance of the collection with the change."""
        ...

    def __init__(self, action: System.ComponentModel.CollectionChangeAction, element: typing.Any) -> None:
        """Initializes a new instance of the System.ComponentModel.CollectionChangeEventArgs class."""
        ...


class ComponentConverter(System.ComponentModel.ReferenceConverter):
    """
    Provides a type converter to convert component objects to and
    from various other representations.
    """

    def __init__(self, type: typing.Type) -> None:
        """Initializes a new instance of the System.ComponentModel.ComponentConverter class."""
        ...

    def get_properties(self, context: System.ComponentModel.ITypeDescriptorContext, value: typing.Any, attributes: typing.List[System.Attribute]) -> System.ComponentModel.PropertyDescriptorCollection:
        """
        Gets a collection of properties for the type of component
        specified by the value parameter.
        """
        ...

    def get_properties_supported(self, context: System.ComponentModel.ITypeDescriptorContext) -> bool:
        """
        Gets a value indicating whether this object supports properties using the
        specified context.
        """
        ...


class DateTimeOffsetConverter(System.ComponentModel.TypeConverter):
    """
    Provides a type converter to convert System.DateTimeOffset
    objects to and from various other representations.
    """

    def can_convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, source_type: typing.Type) -> bool:
        """
        Gets a value indicating whether this converter can convert an
        object in the given source type to a System.DateTimeOffset
        object using the specified context.
        """
        ...

    def can_convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, destination_type: typing.Type) -> bool:
        """
        Gets a value indicating whether this converter can convert an
        object to the given destination type using the context.
        """
        ...

    def convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any) -> System.Object:
        """
        Converts the given value object to a System.DateTime
        object.
        """
        ...

    def convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any, destination_type: typing.Type) -> System.Object:
        """
        Converts the given value object to a System.DateTimeOffset
        object using the arguments.
        """
        ...


class ComponentEditor(System.Object, metaclass=abc.ABCMeta):
    """Provides the base class for a custom component editor."""

    @overload
    def edit_component(self, component: typing.Any) -> bool:
        """Gets a value indicating whether the component was modified."""
        ...

    @overload
    def edit_component(self, context: System.ComponentModel.ITypeDescriptorContext, component: typing.Any) -> bool:
        """Gets a value indicating whether the component was modified."""
        ...


class AddingNewEventArgs(System.EventArgs):
    """
    Provides data for an event that signals the adding of a new object
    to a list, allowing any event handler to supply the new object. If
    no event handler supplies a new object to use, the list should create
    one itself.
    """

    @property
    def new_object(self) -> System.Object:
        """Gets or sets the new object that will be added to the list."""
        ...

    @new_object.setter
    def new_object(self, value: System.Object) -> None:
        ...

    @overload
    def __init__(self, new_object: typing.Any) -> None:
        """
        Initializes a new instance of the System.ComponentModel.AddingNewEventArgs class,
        with the specified object defined as the default new object.
        """
        ...

    @overload
    def __init__(self) -> None:
        """
        Initializes a new instance of the System.ComponentModel.AddingNewEventArgs class,
        with no new object defined.
        """
        ...


class DataObjectAttribute(System.Attribute):
    """This class has no documentation."""

    DATA_OBJECT: System.ComponentModel.DataObjectAttribute = ...

    NON_DATA_OBJECT: System.ComponentModel.DataObjectAttribute = ...

    DEFAULT: System.ComponentModel.DataObjectAttribute = ...

    @property
    def is_data_object(self) -> bool:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, is_data_object: bool) -> None:
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def is_default_attribute(self) -> bool:
        ...


class IComNativeDescriptorHandler(metaclass=abc.ABCMeta):
    """
    Top level mapping layer between a COM object and TypeDescriptor.
    
    IComNativeDescriptorHandler has been deprecated. Add a TypeDescriptionProvider to handle type TypeDescriptor.ComObjectType instead.
    """

    def get_attributes(self, component: typing.Any) -> System.ComponentModel.AttributeCollection:
        ...

    def get_class_name(self, component: typing.Any) -> str:
        ...

    def get_converter(self, component: typing.Any) -> System.ComponentModel.TypeConverter:
        ...

    def get_default_event(self, component: typing.Any) -> System.ComponentModel.EventDescriptor:
        ...

    def get_default_property(self, component: typing.Any) -> System.ComponentModel.PropertyDescriptor:
        ...

    def get_editor(self, component: typing.Any, base_editor_type: typing.Type) -> System.Object:
        ...

    @overload
    def get_events(self, component: typing.Any) -> System.ComponentModel.EventDescriptorCollection:
        ...

    @overload
    def get_events(self, component: typing.Any, attributes: typing.List[System.Attribute]) -> System.ComponentModel.EventDescriptorCollection:
        ...

    def get_name(self, component: typing.Any) -> str:
        ...

    def get_properties(self, component: typing.Any, attributes: typing.List[System.Attribute]) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    @overload
    def get_property_value(self, component: typing.Any, property_name: str, success: bool) -> System.Object:
        ...

    @overload
    def get_property_value(self, component: typing.Any, dispid: int, success: bool) -> System.Object:
        ...


class RefreshEventArgs(System.EventArgs):
    """Provides data for the System.ComponentModel.TypeDescriptor.Refresh(object) event."""

    @property
    def component_changed(self) -> System.Object:
        """Gets the component that has changed its properties, events, or extenders."""
        ...

    @property
    def type_changed(self) -> typing.Type:
        """Gets the type that has changed its properties, or events."""
        ...

    @overload
    def __init__(self, component_changed: typing.Any) -> None:
        """
        Initializes a new instance of the System.ComponentModel.RefreshEventArgs class with
        the component that has changed.
        """
        ...

    @overload
    def __init__(self, type_changed: typing.Type) -> None:
        """
        Initializes a new instance of the System.ComponentModel.RefreshEventArgs class with
        the type of component that has changed.
        """
        ...


class TypeDescriptor(System.Object):
    """
    Provides information about the properties and events for a component.
    This class cannot be inherited.
    """

    INTERFACE_TYPE: typing.Type
    """
    This property returns a Type object that can be passed to the various
    AddProvider methods to define a type description provider for interface types.
    """

    refreshed: _EventContainer[typing.Callable[[System.ComponentModel.RefreshEventArgs], None], None]
    """Occurs when Refreshed is raised for a component."""

    COM_OBJECT_TYPE: typing.Type

    com_native_descriptor_handler: System.ComponentModel.IComNativeDescriptorHandler
    """TypeDescriptor.ComNativeDescriptorHandler has been deprecated. Use a type description provider to supply type information for COM types instead."""

    @staticmethod
    @overload
    def add_attributes(instance: typing.Any, *attributes: typing.Union[System.Attribute, typing.Iterable[System.Attribute]]) -> System.ComponentModel.TypeDescriptionProvider:
        """
        The AddAttributes method allows you to add class-level attributes for a
        type or an instance. This method simply implements a type description provider
        that merges the provided attributes with the attributes that already exist on
        the class. This is a short cut for such a behavior. Adding additional
        attributes is common need for applications using the Windows Forms property
        window. The return value form AddAttributes is the TypeDescriptionProvider
        that was used to add the attributes. This provider can later be passed to
        RemoveProvider if the added attributes are no longer needed.
        """
        ...

    @staticmethod
    @overload
    def add_attributes(type: typing.Type, *attributes: typing.Union[System.Attribute, typing.Iterable[System.Attribute]]) -> System.ComponentModel.TypeDescriptionProvider:
        """
        The AddAttributes method allows you to add class-level attributes for a
        type or an instance. This method simply implements a type description provider
        that merges the provided attributes with the attributes that already exist on
        the class. This is a short cut for such a behavior. Adding additional
        attributes is common need for applications using the Windows Forms property
        window. The return value form AddAttributes is the TypeDescriptionProvider
        that was used to add the attributes. This provider can later be passed to
        RemoveProvider if the added attributes are no longer needed.
        """
        ...

    @staticmethod
    def add_editor_table(editor_base_type: typing.Type, table: System.Collections.Hashtable) -> None:
        """
        Adds an editor table for the given editor base type. Typically, editors are
        specified as metadata on an object. If no metadata for a requested editor
        base type can be found on an object, however, the TypeDescriptor will search
        an editor table for the editor type, if one can be found.
        """
        ...

    @staticmethod
    @overload
    def add_provider(provider: System.ComponentModel.TypeDescriptionProvider, instance: typing.Any) -> None:
        """
        Adds a type description provider that will be called on to provide
        type information for a single object instance. A provider added
        using this method will never have its CreateInstance method called
        because the instance already exists. This method does not prevent
        the object from finalizing.
        """
        ...

    @staticmethod
    @overload
    def add_provider(provider: System.ComponentModel.TypeDescriptionProvider, type: typing.Type) -> None:
        """
        Adds a type description provider that will be called on to provide
        type and instance information for any object that is of, or a subtype
        of, the provided type. Type can be any type, including interfaces.
        For example, to provide custom type and instance information for all
        components, you would pass typeof(IComponent). Passing typeof(object)
        will cause the provider to be called to provide type information for
        all types.
        """
        ...

    @staticmethod
    @overload
    def add_provider_transparent(provider: System.ComponentModel.TypeDescriptionProvider, instance: typing.Any) -> None:
        """
        Adds a type description provider that will be called on to provide
        type information for a single object instance. A provider added
        using this method will never have its CreateInstance method called
        because the instance already exists. This method does not prevent
        the object from finalizing.
        """
        ...

    @staticmethod
    @overload
    def add_provider_transparent(provider: System.ComponentModel.TypeDescriptionProvider, type: typing.Type) -> None:
        """
        Adds a type description provider that will be called on to provide
        type and instance information for any object that is of, or a subtype
        of, the provided type. Type can be any type, including interfaces.
        For example, to provide custom type and instance information for all
        components, you would pass typeof(IComponent). Passing typeof(object)
        will cause the provider to be called to provide type information for
        all types.
        """
        ...

    @staticmethod
    def create_association(primary: typing.Any, secondary: typing.Any) -> None:
        """
        The CreateAssociation method creates an association between two objects.
        Once an association is created, a designer or other filtering mechanism
        can add properties that route to either object into the primary object's
        property set. When a property invocation is made against the primary
        object, GetAssociation will be called to resolve the actual object
        instance that is related to its type parameter.
        """
        ...

    @staticmethod
    def create_designer(component: System.ComponentModel.IComponent, designer_base_type: typing.Type) -> System.ComponentModel.Design.IDesigner:
        ...

    @staticmethod
    @overload
    def create_event(component_type: typing.Type, name: str, type: typing.Type, *attributes: typing.Union[System.Attribute, typing.Iterable[System.Attribute]]) -> System.ComponentModel.EventDescriptor:
        """This dynamically binds an EventDescriptor to a type."""
        ...

    @staticmethod
    @overload
    def create_event(component_type: typing.Type, old_event_descriptor: System.ComponentModel.EventDescriptor, *attributes: typing.Union[System.Attribute, typing.Iterable[System.Attribute]]) -> System.ComponentModel.EventDescriptor:
        """
        This creates a new event descriptor identical to an existing event descriptor. The new event descriptor
        has the specified metadata attributes merged with the existing metadata attributes.
        """
        ...

    @staticmethod
    def create_instance(provider: typing.Optional[IServiceProvider], object_type: typing.Type, arg_types: typing.List[typing.Type], args: typing.List[System.Object]) -> System.Object:
        """
        This method will search internal tables within TypeDescriptor for
        a TypeDescriptionProvider object that is associated with the given
        data type. If it finds one, it will delegate the call to that object.
        """
        ...

    @staticmethod
    @overload
    def create_property(component_type: typing.Type, name: str, type: typing.Type, *attributes: typing.Union[System.Attribute, typing.Iterable[System.Attribute]]) -> System.ComponentModel.PropertyDescriptor:
        """This dynamically binds a PropertyDescriptor to a type."""
        ...

    @staticmethod
    @overload
    def create_property(component_type: typing.Type, old_property_descriptor: System.ComponentModel.PropertyDescriptor, *attributes: typing.Union[System.Attribute, typing.Iterable[System.Attribute]]) -> System.ComponentModel.PropertyDescriptor:
        """
        This creates a new property descriptor identical to an existing property descriptor. The new property descriptor
        has the specified metadata attributes merged with the existing metadata attributes.
        """
        ...

    @staticmethod
    def get_association(type: typing.Type, primary: typing.Any) -> System.Object:
        """
        The GetAssociation method returns the correct object to invoke
        for the requested type. It never returns null.
        """
        ...

    @staticmethod
    @overload
    def get_attributes(component: typing.Any) -> System.ComponentModel.AttributeCollection:
        """Gets a collection of attributes for the specified component."""
        ...

    @staticmethod
    @overload
    def get_attributes(component: typing.Any, no_custom_type_desc: bool) -> System.ComponentModel.AttributeCollection:
        """Gets a collection of attributes for the specified component."""
        ...

    @staticmethod
    @overload
    def get_attributes(component_type: typing.Type) -> System.ComponentModel.AttributeCollection:
        """Gets a collection of attributes for the specified type of component."""
        ...

    @staticmethod
    @overload
    def get_class_name(component: typing.Any) -> str:
        """Gets the name of the class for the specified component."""
        ...

    @staticmethod
    @overload
    def get_class_name(component: typing.Any, no_custom_type_desc: bool) -> str:
        """Gets the name of the class for the specified component."""
        ...

    @staticmethod
    @overload
    def get_class_name(component_type: typing.Type) -> str:
        """Gets the name of the class for the specified type."""
        ...

    @staticmethod
    @overload
    def get_component_name(component: typing.Any) -> str:
        """The name of the class for the specified component."""
        ...

    @staticmethod
    @overload
    def get_component_name(component: typing.Any, no_custom_type_desc: bool) -> str:
        """Gets the name of the class for the specified component."""
        ...

    @staticmethod
    @overload
    def get_converter(component: typing.Any) -> System.ComponentModel.TypeConverter:
        """Gets a type converter for the type of the specified component."""
        ...

    @staticmethod
    @overload
    def get_converter(component: typing.Any, no_custom_type_desc: bool) -> System.ComponentModel.TypeConverter:
        """Gets a type converter for the type of the specified component."""
        ...

    @staticmethod
    @overload
    def get_converter(type: typing.Type) -> System.ComponentModel.TypeConverter:
        """Gets a type converter for the specified type."""
        ...

    @staticmethod
    @overload
    def get_converter_from_registered_type(component: typing.Any) -> System.ComponentModel.TypeConverter:
        """Gets a type converter for the type of the specified component."""
        ...

    @staticmethod
    @overload
    def get_converter_from_registered_type(type: typing.Type) -> System.ComponentModel.TypeConverter:
        """Gets a type converter for the specified registered type."""
        ...

    @staticmethod
    @overload
    def get_default_event(component: typing.Any) -> System.ComponentModel.EventDescriptor:
        """Gets the default event for the specified component."""
        ...

    @staticmethod
    @overload
    def get_default_event(component: typing.Any, no_custom_type_desc: bool) -> System.ComponentModel.EventDescriptor:
        """Gets the default event for a component."""
        ...

    @staticmethod
    @overload
    def get_default_event(component_type: typing.Type) -> System.ComponentModel.EventDescriptor:
        """Gets the default event for the specified type of component."""
        ...

    @staticmethod
    @overload
    def get_default_property(component: typing.Any) -> System.ComponentModel.PropertyDescriptor:
        """Gets the default property for the specified component."""
        ...

    @staticmethod
    @overload
    def get_default_property(component: typing.Any, no_custom_type_desc: bool) -> System.ComponentModel.PropertyDescriptor:
        """Gets the default property for the specified component."""
        ...

    @staticmethod
    @overload
    def get_default_property(component_type: typing.Type) -> System.ComponentModel.PropertyDescriptor:
        """Gets the default property for the specified type of component."""
        ...

    @staticmethod
    @overload
    def get_editor(component: typing.Any, editor_base_type: typing.Type) -> System.Object:
        """
        Gets an editor with the specified base type for the
        specified component.
        """
        ...

    @staticmethod
    @overload
    def get_editor(component: typing.Any, editor_base_type: typing.Type, no_custom_type_desc: bool) -> System.Object:
        """
        Gets an editor with the specified base type for the
        specified component.
        """
        ...

    @staticmethod
    @overload
    def get_editor(type: typing.Type, editor_base_type: typing.Type) -> System.Object:
        """Gets an editor with the specified base type for the specified type."""
        ...

    @staticmethod
    @overload
    def get_events(component: typing.Any) -> System.ComponentModel.EventDescriptorCollection:
        """Gets a collection of events for a specified component."""
        ...

    @staticmethod
    @overload
    def get_events(component: typing.Any, no_custom_type_desc: bool) -> System.ComponentModel.EventDescriptorCollection:
        """Gets a collection of events for a specified component."""
        ...

    @staticmethod
    @overload
    def get_events(component: typing.Any, attributes: typing.List[System.Attribute]) -> System.ComponentModel.EventDescriptorCollection:
        """
        Gets a collection of events for a specified component
        using a specified array of attributes as a filter.
        """
        ...

    @staticmethod
    @overload
    def get_events(component: typing.Any, attributes: typing.List[System.Attribute], no_custom_type_desc: bool) -> System.ComponentModel.EventDescriptorCollection:
        """
        Gets a collection of events for a specified component
        using a specified array of attributes as a filter.
        """
        ...

    @staticmethod
    @overload
    def get_events(component_type: typing.Type) -> System.ComponentModel.EventDescriptorCollection:
        """Gets a collection of events for a specified type of component."""
        ...

    @staticmethod
    @overload
    def get_events(component_type: typing.Type, attributes: typing.List[System.Attribute]) -> System.ComponentModel.EventDescriptorCollection:
        """
        Gets a collection of events for a specified type of
        component using a specified array of attributes as a filter.
        """
        ...

    @staticmethod
    def get_events_from_registered_type(component_type: typing.Type) -> System.ComponentModel.EventDescriptorCollection:
        """Gets a collection of events for a specified type of component."""
        ...

    @staticmethod
    def get_full_component_name(component: typing.Any) -> str:
        """
        The name of the specified component, or null if the component has no name.
        In many cases this will return the same value as GetComponentName. If the
        component resides in a nested container or has other nested semantics, it may
        return a different fully qualified name.
        """
        ...

    @staticmethod
    @overload
    def get_properties(component: typing.Any) -> System.ComponentModel.PropertyDescriptorCollection:
        """Gets a collection of properties for a specified component."""
        ...

    @staticmethod
    @overload
    def get_properties(component: typing.Any, no_custom_type_desc: bool) -> System.ComponentModel.PropertyDescriptorCollection:
        """Gets a collection of properties for a specified component."""
        ...

    @staticmethod
    @overload
    def get_properties(component: typing.Any, attributes: typing.List[System.Attribute]) -> System.ComponentModel.PropertyDescriptorCollection:
        """
        Gets a collection of properties for a specified
        component using a specified array of attributes
        as a filter.
        """
        ...

    @staticmethod
    @overload
    def get_properties(component: typing.Any, attributes: typing.List[System.Attribute], no_custom_type_desc: bool) -> System.ComponentModel.PropertyDescriptorCollection:
        """
        Gets a collection of properties for a specified
        component using a specified array of attributes
        as a filter.
        """
        ...

    @staticmethod
    @overload
    def get_properties(component_type: typing.Type) -> System.ComponentModel.PropertyDescriptorCollection:
        """Gets a collection of properties for a specified type of component."""
        ...

    @staticmethod
    @overload
    def get_properties(component_type: typing.Type, attributes: typing.List[System.Attribute]) -> System.ComponentModel.PropertyDescriptorCollection:
        """
        Gets a collection of properties for a specified type of
        component using a specified array of attributes as a filter.
        """
        ...

    @staticmethod
    @overload
    def get_properties_from_registered_type(component: typing.Any) -> System.ComponentModel.PropertyDescriptorCollection:
        """Gets a collection of properties for a specified component."""
        ...

    @staticmethod
    @overload
    def get_properties_from_registered_type(component_type: typing.Type) -> System.ComponentModel.PropertyDescriptorCollection:
        """Gets a collection of properties for a specified type."""
        ...

    @staticmethod
    @overload
    def get_provider(instance: typing.Any) -> System.ComponentModel.TypeDescriptionProvider:
        """
        The GetProvider method returns a type description provider for
        the given object or type. This will always return a type description
        provider. Even the default TypeDescriptor implementation is built on
        a TypeDescriptionProvider, and this will be returned unless there is
        another provider that someone else has added.
        """
        ...

    @staticmethod
    @overload
    def get_provider(type: typing.Type) -> System.ComponentModel.TypeDescriptionProvider:
        """
        The GetProvider method returns a type description provider for
        the given object or type. This will always return a type description
        provider. Even the default TypeDescriptor implementation is built on
        a TypeDescriptionProvider, and this will be returned unless there is
        another provider that someone else has added.
        """
        ...

    @staticmethod
    @overload
    def get_reflection_type(instance: typing.Any) -> typing.Type:
        """Returns an Type instance that can be used to perform reflection."""
        ...

    @staticmethod
    @overload
    def get_reflection_type(type: typing.Type) -> typing.Type:
        """Returns an Type instance that can be used to perform reflection."""
        ...

    @staticmethod
    @overload
    def refresh(component: typing.Any) -> None:
        """
        Clears the properties and events for the specified
        component from the cache.
        """
        ...

    @staticmethod
    @overload
    def refresh(type: typing.Type) -> None:
        """
        Clears the properties and events for the specified type
        of component from the cache.
        """
        ...

    @staticmethod
    @overload
    def refresh(module: System.Reflection.Module) -> None:
        """
        Clears the properties and events for the specified
        module from the cache.
        """
        ...

    @staticmethod
    @overload
    def refresh(assembly: System.Reflection.Assembly) -> None:
        """
        Clears the properties and events for the specified
        assembly from the cache.
        """
        ...

    @staticmethod
    def remove_association(primary: typing.Any, secondary: typing.Any) -> None:
        """The RemoveAssociation method removes an association with an object."""
        ...

    @staticmethod
    def remove_associations(primary: typing.Any) -> None:
        """The RemoveAssociations method removes all associations for a primary object."""
        ...

    @staticmethod
    @overload
    def remove_provider(provider: System.ComponentModel.TypeDescriptionProvider, instance: typing.Any) -> None:
        """
        The RemoveProvider method removes a previously added type
        description provider. Removing a provider causes a Refresh
        event to be raised for the object or type the provider is
        associated with.
        """
        ...

    @staticmethod
    @overload
    def remove_provider(provider: System.ComponentModel.TypeDescriptionProvider, type: typing.Type) -> None:
        """
        The RemoveProvider method removes a previously added type
        description provider. Removing a provider causes a Refresh
        event to be raised for the object or type the provider is
        associated with.
        """
        ...

    @staticmethod
    @overload
    def remove_provider_transparent(provider: System.ComponentModel.TypeDescriptionProvider, instance: typing.Any) -> None:
        """
        The RemoveProvider method removes a previously added type
        description provider. Removing a provider causes a Refresh
        event to be raised for the object or type the provider is
        associated with.
        """
        ...

    @staticmethod
    @overload
    def remove_provider_transparent(provider: System.ComponentModel.TypeDescriptionProvider, type: typing.Type) -> None:
        """
        The RemoveProvider method removes a previously added type
        description provider. Removing a provider causes a Refresh
        event to be raised for the object or type the provider is
        associated with.
        """
        ...

    @staticmethod
    def sort_descriptor_array(infos: System.Collections.IList) -> None:
        """Sorts descriptors by name of the descriptor."""
        ...


class DefaultPropertyAttribute(System.Attribute):
    """Specifies the default property for a component."""

    @property
    def name(self) -> str:
        """
        Gets the name of the default property for the component this attribute is
        bound to.
        """
        ...

    DEFAULT: System.ComponentModel.DefaultPropertyAttribute = ...
    """
    Specifies the default value for the System.ComponentModel.DefaultPropertyAttribute, which is null. This
    static field is read-only.
    """

    def __init__(self, name: str) -> None:
        """Initializes a new instance of the System.ComponentModel.DefaultPropertyAttribute class."""
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...


class MaskedTextResultHint(Enum):
    """Enum defining hints about the reason of the result of a particular operation."""

    UNKNOWN = 0

    CHARACTER_ESCAPED = 1

    NO_EFFECT = 2

    SIDE_EFFECT = 3

    SUCCESS = 4

    ASCII_CHARACTER_EXPECTED = -1

    ALPHANUMERIC_CHARACTER_EXPECTED = -2

    DIGIT_EXPECTED = -3

    LETTER_EXPECTED = -4

    SIGNED_DIGIT_EXPECTED = -5

    INVALID_INPUT = -51

    PROMPT_CHAR_NOT_ALLOWED = -52

    UNAVAILABLE_EDIT_POSITION = -53

    NON_EDIT_POSITION = -54

    POSITION_OUT_OF_RANGE = -55


class AmbientValueAttribute(System.Attribute):
    """
    Specifies the ambient value for a property. The ambient value is the value you
    can set into a property to make it inherit its ambient.
    """

    @property
    def value(self) -> System.Object:
        """Gets the ambient value of the property this attribute is bound to."""
        ...

    @overload
    def __init__(self, value: typing.Any) -> None:
        """
        Initializes a new instance of the System.ComponentModel.AmbientValueAttribute
        class.
        """
        ...

    @overload
    def __init__(self, type: typing.Type, value: str) -> None:
        """
        Initializes a new instance of the System.ComponentModel.AmbientValueAttribute class, converting the
        specified value to the specified type, and using the U.S. English culture as the
        translation context.
        """
        ...

    @overload
    def __init__(self, value: str) -> None:
        """
        Initializes a new instance of the System.ComponentModel.AmbientValueAttribute class using a Unicode
        character.
        """
        ...

    @overload
    def __init__(self, value: int) -> None:
        """
        Initializes a new instance of the System.ComponentModel.AmbientValueAttribute class using an 8-bit unsigned
        integer.
        """
        ...

    @overload
    def __init__(self, value: float) -> None:
        """
        Initializes a new instance of the System.ComponentModel.AmbientValueAttribute class using a
        single-precision floating point number.
        """
        ...

    @overload
    def __init__(self, value: bool) -> None:
        """
        Initializes a new instance of the System.ComponentModel.AmbientValueAttribute class using a bool
        value.
        """
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...


class CharConverter(System.ComponentModel.TypeConverter):
    """
    Provides a type converter to convert Unicode character objects to and from various
    other representations.
    """

    def can_convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, source_type: typing.Type) -> bool:
        """
        Gets a value indicating whether this converter can convert an object in the given
        source type to a Unicode character object using the specified context.
        """
        ...

    def convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any) -> System.Object:
        """Converts the given object to a Unicode character object."""
        ...

    def convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any, destination_type: typing.Type) -> System.Object:
        """Converts the given object to another type."""
        ...


class SyntaxCheck(System.Object):
    """
    SyntaxCheck
    Helper class to check for path and machine name syntax.
    """

    @staticmethod
    def check_machine_name(value: str) -> bool:
        """Checks the syntax of the machine name (no "\\" anywhere in it)."""
        ...

    @staticmethod
    def check_path(value: str) -> bool:
        """Checks the syntax of the path (must start with "\\\\")."""
        ...

    @staticmethod
    def check_rooted_path(value: str) -> bool:
        """
        Checks the syntax of the path (must start with "\\" or drive letter "C:").
        NOTE:  These denote a file or directory path!!
        """
        ...


class ITypedList(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    def get_item_properties(self, list_accessors: typing.List[System.ComponentModel.PropertyDescriptor]) -> System.ComponentModel.PropertyDescriptorCollection:
        ...

    def get_list_name(self, list_accessors: typing.List[System.ComponentModel.PropertyDescriptor]) -> str:
        ...


class UInt32Converter(System.ComponentModel.BaseNumberConverter):
    """
    Provides a type converter to convert 32-bit unsigned integer objects to and
    from various other representations.
    """


class MarshalByValueComponent(System.Object, System.ComponentModel.IComponent, IServiceProvider):
    """
    Provides the base implementation for System.ComponentModel.IComponent,
    which is the base class for all components in Win Forms.
    """

    @property
    def disposed(self) -> _EventContainer[typing.Callable[[System.Object, System.EventArgs], None], None]:
        """Adds an event handler to listen to the Disposed event on the component."""
        ...

    @disposed.setter
    def disposed(self, value: _EventContainer[typing.Callable[[System.Object, System.EventArgs], None], None]) -> None:
        ...

    @property
    def events(self) -> System.ComponentModel.EventHandlerList:
        """
        Gets the list of event handlers that are attached to this component.
        
        This property is protected.
        """
        ...

    @property
    def site(self) -> System.ComponentModel.ISite:
        """Gets or sets the site of the component."""
        ...

    @site.setter
    def site(self, value: System.ComponentModel.ISite) -> None:
        ...

    @property
    def container(self) -> System.ComponentModel.IContainer:
        """Gets the container for the component."""
        ...

    @property
    def design_mode(self) -> bool:
        """Gets a value indicating whether the component is currently in design mode."""
        ...

    def __init__(self) -> None:
        """Initializes a new instance of the System.ComponentModel.MarshalByValueComponent class."""
        ...

    @overload
    def dispose(self) -> None:
        """Disposes of the resources (other than memory) used by the component."""
        ...

    @overload
    def dispose(self, disposing: bool) -> None:
        """
        Disposes all the resources associated with this component.
        If disposing is false then you must never touch any other
        managed objects, as they may already be finalized. When
        in this state you should dispose any native resources
        that you have a reference to.
        
        
        When disposing is true then you should dispose all data
        and objects you have references to. The normal implementation
        of this method would look something like:
        
        
        public void Dispose() {
        Dispose(true);
        GC.SuppressFinalize(this);
        }
        
        protected virtual void Dispose(bool disposing) {
        if (disposing) {
          if (myobject != null) {
              myobject.Dispose();
              myobject = null;
          }
        }
        if (myhandle != IntPtr.Zero) {
          NativeMethods.Release(myhandle);
          myhandle = IntPtr.Zero;
        }
        }
        
        ~MyClass() {
        Dispose(false);
        }
        
        
        For base classes, you should never override the Finalizer (~Class in C#)
        or the Dispose method that takes no arguments, rather you should
        always override the Dispose method that takes a bool.
        
        
        protected override void Dispose(bool disposing) {
        if (disposing) {
          if (myobject != null) {
              myobject.Dispose();
              myobject = null;
          }
        }
        if (myhandle != IntPtr.Zero) {
          NativeMethods.Release(myhandle);
          myhandle = IntPtr.Zero;
        }
        base.Dispose(disposing);
        }
        
        This method is protected.
        """
        ...

    def get_service(self, service: typing.Type) -> System.Object:
        """Gets the implementer of the System.IServiceProvider."""
        ...

    def to_string(self) -> str:
        """
        Returns a string containing the name of the System.ComponentModel.Component , if any. This method should not be
        overridden. For
        internal use only.
        """
        ...


class NullableConverter(System.ComponentModel.TypeConverter):
    """TypeConverter to convert Nullable types to and from strings or the underlying simple type."""

    @property
    def nullable_type(self) -> typing.Type:
        """The type this converter was initialized with."""
        ...

    @property
    def underlying_type(self) -> typing.Type:
        """The simple type that is represented as a nullable."""
        ...

    @property
    def underlying_type_converter(self) -> System.ComponentModel.TypeConverter:
        """Converter associated with the underlying simple type."""
        ...

    def __init__(self, type: typing.Type) -> None:
        """Nullable converter is initialized with the underlying simple type."""
        ...

    def can_convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, source_type: typing.Type) -> bool:
        """
        Gets a value indicating whether this converter can convert an object in the
        given source type to the underlying simple type or a null.
        """
        ...

    def can_convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, destination_type: typing.Type) -> bool:
        """Gets a value indicating whether this converter can convert a value object to the destination type."""
        ...

    def convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any) -> System.Object:
        """Converts the given value to the converter's underlying simple type or a null."""
        ...

    def convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any, destination_type: typing.Type) -> System.Object:
        """Converts the given value object to the destination type."""
        ...

    def create_instance(self, context: System.ComponentModel.ITypeDescriptorContext, property_values: System.Collections.IDictionary) -> System.Object:
        """"""
        ...

    def get_create_instance_supported(self, context: System.ComponentModel.ITypeDescriptorContext) -> bool:
        """
        Gets a value indicating whether changing a value on this object requires a call to
        System.ComponentModel.TypeConverter.CreateInstance(IDictionary) to create a new value,
        using the specified context.
        """
        ...

    def get_properties(self, context: System.ComponentModel.ITypeDescriptorContext, value: typing.Any, attributes: typing.List[System.Attribute]) -> System.ComponentModel.PropertyDescriptorCollection:
        """
        Gets a collection of properties for the type of array specified by the value
        parameter using the specified context and attributes.
        """
        ...

    def get_properties_supported(self, context: System.ComponentModel.ITypeDescriptorContext) -> bool:
        """Gets a value indicating whether this object supports properties using the specified context."""
        ...

    def get_standard_values(self, context: System.ComponentModel.ITypeDescriptorContext) -> System.ComponentModel.TypeConverter.StandardValuesCollection:
        """Gets a collection of standard values for the data type this type converter is designed for."""
        ...

    def get_standard_values_exclusive(self, context: System.ComponentModel.ITypeDescriptorContext) -> bool:
        """
        Gets a value indicating whether the collection of standard values returned from
        System.ComponentModel.TypeConverter.GetStandardValues() is an exclusive
        list of possible values, using the specified context.
        """
        ...

    def get_standard_values_supported(self, context: System.ComponentModel.ITypeDescriptorContext) -> bool:
        """
        Gets a value indicating whether this object supports a standard set of values that can
        be picked from a list using the specified context.
        """
        ...

    def is_valid(self, context: System.ComponentModel.ITypeDescriptorContext, value: typing.Any) -> bool:
        """Gets a value indicating whether the given value object is valid for this type."""
        ...


class DataObjectFieldAttribute(System.Attribute):
    """
    Represents a field of a DataObject. Use this attribute on a field to indicate
    properties such as primary key, identity, nullability, and length.
    """

    @property
    def is_identity(self) -> bool:
        ...

    @property
    def is_nullable(self) -> bool:
        ...

    @property
    def length(self) -> int:
        ...

    @property
    def primary_key(self) -> bool:
        ...

    @overload
    def __init__(self, primary_key: bool) -> None:
        ...

    @overload
    def __init__(self, primary_key: bool, is_identity: bool) -> None:
        ...

    @overload
    def __init__(self, primary_key: bool, is_identity: bool, is_nullable: bool) -> None:
        ...

    @overload
    def __init__(self, primary_key: bool, is_identity: bool, is_nullable: bool, length: int) -> None:
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...


class Int64Converter(System.ComponentModel.BaseNumberConverter):
    """
    Provides a type converter to convert 64-bit signed integer objects to and
    from various other representations.
    """


class DefaultEventAttribute(System.Attribute):
    """Specifies the default event for a component."""

    @property
    def name(self) -> str:
        """Gets the name of the default event for the component this attribute is bound to."""
        ...

    DEFAULT: System.ComponentModel.DefaultEventAttribute = ...
    """
    Specifies the default value for the System.ComponentModel.DefaultEventAttribute, which is
    null.
    This static field is read-only.
    """

    def __init__(self, name: str) -> None:
        """Initializes a new instance of the System.ComponentModel.DefaultEventAttribute class."""
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...


class SingleConverter(System.ComponentModel.BaseNumberConverter):
    """
    Provides a type converter to convert single-precision, floating point number objects to and
    from various other representations.
    """


class IExtenderProvider(metaclass=abc.ABCMeta):
    """Defines the interface for extending properties to other components in a container."""

    def can_extend(self, extendee: typing.Any) -> bool:
        """
        Specifies whether this object can provide its extender properties to
        the specified object.
        """
        ...


class ExtenderProvidedPropertyAttribute(System.Attribute):
    """
    ExtenderProvidedPropertyAttribute is an attribute that marks that a property
    was actually offered up by and extender provider.
    """

    @property
    def extender_property(self) -> System.ComponentModel.PropertyDescriptor:
        """PropertyDescriptor of the property that is being provided."""
        ...

    @property
    def provider(self) -> System.ComponentModel.IExtenderProvider:
        """Extender provider that is providing the property."""
        ...

    @property
    def receiver_type(self) -> typing.Type:
        """The type of object that can receive these properties."""
        ...

    def __init__(self) -> None:
        """Creates an empty ExtenderProvidedPropertyAttribute."""
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def is_default_attribute(self) -> bool:
        ...


class IIntellisenseBuilder(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def name(self) -> str:
        """Return a localized name."""
        ...

    def show(self, language: str, value: str, new_value: str) -> bool:
        """
        Show the builder and return a boolean indicating whether value should be replaced with new_value
        - false if the user cancels for example
        
        language - indicates which language service is calling the builder
        value - expression being edited
        new_value - return the new value
        """
        ...


class ICancelAddNew(metaclass=abc.ABCMeta):
    """
    Interface implemented by a list that allows the addition of a new item
    to be either cancelled or committed.
    
    Note: In some scenarios, specifically Windows Forms complex data binding,
    the list may receive CancelNew or EndNew calls for items other than the
    new item. These calls should be ignored, ie. the new item should only be
    cancelled or committed when that item's index is specified.
    """

    def cancel_new(self, item_index: int) -> None:
        """
        If a new item has been added to the list, and  is the position of that item,
        then this method should remove it from the list and cancel the add operation.
        """
        ...

    def end_new(self, item_index: int) -> None:
        """
        If a new item has been added to the list, and  is the position of that item,
        then this method should leave it in the list and complete the add operation.
        """
        ...


class IRaiseItemChangedEvents(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def raises_item_changed_events(self) -> bool:
        ...


class BindingList(typing.Generic[System_ComponentModel_BindingList_T], System.Collections.ObjectModel.Collection[System_ComponentModel_BindingList_T], System.ComponentModel.IBindingList, System.ComponentModel.ICancelAddNew, System.ComponentModel.IRaiseItemChangedEvents):
    """This class has no documentation."""

    @property
    def adding_new(self) -> _EventContainer[typing.Callable[[System.Object, System.ComponentModel.AddingNewEventArgs], None], None]:
        """Event that allows a custom item to be provided as the new item added to the list by AddNew()."""
        ...

    @adding_new.setter
    def adding_new(self, value: _EventContainer[typing.Callable[[System.Object, System.ComponentModel.AddingNewEventArgs], None], None]) -> None:
        ...

    @property
    def list_changed(self) -> _EventContainer[typing.Callable[[System.Object, System.ComponentModel.ListChangedEventArgs], None], None]:
        """Event that reports changes to the list or to items in the list."""
        ...

    @list_changed.setter
    def list_changed(self, value: _EventContainer[typing.Callable[[System.Object, System.ComponentModel.ListChangedEventArgs], None], None]) -> None:
        ...

    @property
    def raise_list_changed_events(self) -> bool:
        ...

    @raise_list_changed_events.setter
    def raise_list_changed_events(self, value: bool) -> None:
        ...

    @property
    def allow_new(self) -> bool:
        ...

    @allow_new.setter
    def allow_new(self, value: bool) -> None:
        ...

    @property
    def allow_edit(self) -> bool:
        ...

    @allow_edit.setter
    def allow_edit(self, value: bool) -> None:
        ...

    @property
    def allow_remove(self) -> bool:
        ...

    @allow_remove.setter
    def allow_remove(self, value: bool) -> None:
        ...

    @property
    def supports_change_notification_core(self) -> bool:
        """This property is protected."""
        ...

    @property
    def supports_searching_core(self) -> bool:
        """This property is protected."""
        ...

    @property
    def supports_sorting_core(self) -> bool:
        """This property is protected."""
        ...

    @property
    def is_sorted_core(self) -> bool:
        """This property is protected."""
        ...

    @property
    def sort_property_core(self) -> System.ComponentModel.PropertyDescriptor:
        """This property is protected."""
        ...

    @property
    def sort_direction_core(self) -> System.ComponentModel.ListSortDirection:
        """This property is protected."""
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, list: System.Collections.Generic.IList[System_ComponentModel_BindingList_T]) -> None:
        """Constructor that allows substitution of the inner list with a custom list."""
        ...

    def add_new(self) -> System_ComponentModel_BindingList_T:
        """
        Adds a new item to the list. Calls AddNewCore to create and add the item.
        
        Add operations are cancellable via the ICancelAddNew interface. The position of the
        new item is tracked until the add operation is either cancelled by a call to CancelNew,
        explicitly committed by a call to EndNew, or implicitly commmited some other operation
        changes the contents of the list (such as an Insert or Remove). When an add operation is
        cancelled, the new item is removed from the list.
        """
        ...

    def add_new_core(self) -> System.Object:
        """
        Creates a new item and adds it to the list.
        
        The base implementation raises the AddingNew event to allow an event handler to
        supply a custom item to add to the list. Otherwise an item of type T is created.
        The new item is then added to the end of the list.
        
        This method is protected.
        """
        ...

    def apply_sort_core(self, prop: System.ComponentModel.PropertyDescriptor, direction: System.ComponentModel.ListSortDirection) -> None:
        """This method is protected."""
        ...

    def cancel_new(self, item_index: int) -> None:
        """If item added using AddNew() is still cancellable, then remove that item from the list."""
        ...

    def clear_items(self) -> None:
        """This method is protected."""
        ...

    def end_new(self, item_index: int) -> None:
        """If item added using AddNew() is still cancellable, then commit that item."""
        ...

    def find_core(self, prop: System.ComponentModel.PropertyDescriptor, key: typing.Any) -> int:
        """This method is protected."""
        ...

    def insert_item(self, index: int, item: System_ComponentModel_BindingList_T) -> None:
        """This method is protected."""
        ...

    def on_adding_new(self, e: System.ComponentModel.AddingNewEventArgs) -> None:
        """
        Raises the AddingNew event.
        
        This method is protected.
        """
        ...

    def on_list_changed(self, e: System.ComponentModel.ListChangedEventArgs) -> None:
        """
        Raises the ListChanged event.
        
        This method is protected.
        """
        ...

    def remove_item(self, index: int) -> None:
        """This method is protected."""
        ...

    def remove_sort_core(self) -> None:
        """This method is protected."""
        ...

    def reset_bindings(self) -> None:
        ...

    def reset_item(self, position: int) -> None:
        ...

    def set_item(self, index: int, item: System_ComponentModel_BindingList_T) -> None:
        """This method is protected."""
        ...


class CultureInfoConverter(System.ComponentModel.TypeConverter):
    """
    Provides a type converter to convert System.Globalization.CultureInfo
    objects to and from various other representations.
    """

    def can_convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, source_type: typing.Type) -> bool:
        """
        Gets a value indicating whether this converter can convert an object in the given
        source type to a System.Globalization.CultureInfo object using the specified context.
        """
        ...

    def can_convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, destination_type: typing.Type) -> bool:
        """
        Gets a value indicating whether this converter can convert an object to
        the given destination type using the context.
        """
        ...

    def convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any) -> System.Object:
        """
        Converts the specified value object to a System.Globalization.CultureInfo
        object.
        """
        ...

    def convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any, destination_type: typing.Type) -> System.Object:
        """Converts the given value object to the specified destination type."""
        ...

    def get_culture_name(self, culture: System.Globalization.CultureInfo) -> str:
        """
        Retrieves the Name for a input CultureInfo.
        
        This method is protected.
        """
        ...

    def get_standard_values(self, context: System.ComponentModel.ITypeDescriptorContext) -> System.ComponentModel.TypeConverter.StandardValuesCollection:
        """
        Gets a collection of standard values collection for a System.Globalization.CultureInfo
        object using the specified context.
        """
        ...

    def get_standard_values_exclusive(self, context: System.ComponentModel.ITypeDescriptorContext) -> bool:
        """
        Gets a value indicating whether the list of standard values returned from
        System.ComponentModel.CultureInfoConverter.GetStandardValues is an exclusive list.
        """
        ...

    def get_standard_values_supported(self, context: System.ComponentModel.ITypeDescriptorContext) -> bool:
        """
        Gets a value indicating whether this object supports a standard set
        of values that can be picked from a list using the specified context.
        """
        ...


class IDataErrorInfo(metaclass=abc.ABCMeta):
    """
    Suppose that you have some data that can be indexed by use of string:
    then there are two types of errors:
    1. an error for each piece of data that can be indexed
    2. an error that is valid on the entire data
    """

    @property
    @abc.abstractmethod
    def error(self) -> str:
        ...

    def __getitem__(self, column_name: str) -> str:
        ...


class ExpandableObjectConverter(System.ComponentModel.TypeConverter):
    """
    Provides a type converter to convert expandable objects to and from various
    other representations.
    """

    def __init__(self) -> None:
        """Initializes a new instance of the System.ComponentModel.ExpandableObjectConverter class."""
        ...

    def get_properties(self, context: System.ComponentModel.ITypeDescriptorContext, value: typing.Any, attributes: typing.List[System.Attribute]) -> System.ComponentModel.PropertyDescriptorCollection:
        """
        Gets a collection of properties for the type of object
        specified by the value parameter.
        """
        ...

    def get_properties_supported(self, context: System.ComponentModel.ITypeDescriptorContext) -> bool:
        """
        Gets a value indicating whether this object supports properties using the
        specified context.
        """
        ...


class Int16Converter(System.ComponentModel.BaseNumberConverter):
    """
    Provides a type converter to convert 16-bit signed integer objects to and
    from various other representations.
    """


class Container(System.Object, System.ComponentModel.IContainer):
    """Encapsulates zero or more components."""

    @property
    def components(self) -> System.ComponentModel.ComponentCollection:
        """Gets all the components in the System.ComponentModel.Container."""
        ...

    @overload
    def add(self, component: System.ComponentModel.IComponent) -> None:
        """
        Adds the specified component to the System.ComponentModel.Container
        The component is unnamed.
        """
        ...

    @overload
    def add(self, component: System.ComponentModel.IComponent, name: str) -> None:
        ...

    def create_site(self, component: System.ComponentModel.IComponent, name: str) -> System.ComponentModel.ISite:
        """
        Creates a Site System.ComponentModel.ISite for the given System.ComponentModel.IComponent
        and assigns the given name to the site.
        
        This method is protected.
        """
        ...

    @overload
    def dispose(self) -> None:
        """
        Disposes of the container. A call to the Dispose method indicates that
        the user of the container has no further need for it.
        
        The implementation of Dispose must:
        
        (1) Remove any references the container is holding to other components.
        This is typically accomplished by assigning null to any fields that
        contain references to other components.
        
        (2) Release any system resources that are associated with the container,
        such as file handles, window handles, or database connections.
        
        (3) Dispose of child components by calling the Dispose method of each.
        
        Ideally, a call to Dispose will revert a container to the state it was
        in immediately after it was created. However, this is not a requirement.
        Following a call to its Dispose method, a container is permitted to raise
        exceptions for operations that cannot meaningfully be performed.
        """
        ...

    @overload
    def dispose(self, disposing: bool) -> None:
        """This method is protected."""
        ...

    def get_service(self, service: typing.Type) -> System.Object:
        """This method is protected."""
        ...

    def remove(self, component: System.ComponentModel.IComponent) -> None:
        """Removes a component from the System.ComponentModel.Container."""
        ...

    def remove_without_unsiting(self, component: System.ComponentModel.IComponent) -> None:
        """This method is protected."""
        ...

    def validate_name(self, component: System.ComponentModel.IComponent, name: str) -> None:
        """
        Validates that the given name is valid for a component. The default implementation
        verifies that name is either null or unique compared to the names of other
        components in the container.
        
        This method is protected.
        """
        ...


class INestedContainer(System.ComponentModel.IContainer, metaclass=abc.ABCMeta):
    """
    A "nested container" is an object that logically contains zero or more child
    components and is controlled (owned) by some parent component.
    
    In this context, "containment" refers to logical containment, not visual
    containment. Components and containers can be used in a variety of
    scenarios, including both visual and non-visual scenarios.
    """

    @property
    @abc.abstractmethod
    def owner(self) -> System.ComponentModel.IComponent:
        """The component that owns this nested container."""
        ...


class NestedContainer(System.ComponentModel.Container, System.ComponentModel.INestedContainer):
    """
    A nested container is a container that is owned by another component. Nested
    containers can be found by querying a component site's services for NestedConainter.
    Nested containers are a useful tool to establish owner relationships among components.
    All components within a nested container are named with the owning component's name
    as a prefix.
    """

    @property
    def owner(self) -> System.ComponentModel.IComponent:
        """The component that owns this nested container."""
        ...

    @property
    def owner_name(self) -> str:
        """
        Retrieves the name of the owning component. This may be overridden to
        provide a custom owner name. The default searches the owner's site for
        INestedSite and calls FullName, or ISite.Name if there is no nested site.
        If neither is available, this returns null.
        
        This property is protected.
        """
        ...

    def __init__(self, owner: System.ComponentModel.IComponent) -> None:
        """Creates a new NestedContainer."""
        ...

    def create_site(self, component: System.ComponentModel.IComponent, name: str) -> System.ComponentModel.ISite:
        """
        Creates a site for the component within the container.
        
        This method is protected.
        """
        ...

    def dispose(self, disposing: bool) -> None:
        """
        Override of Container's dispose.
        
        This method is protected.
        """
        ...

    def get_service(self, service: typing.Type) -> System.Object:
        """This method is protected."""
        ...


class TimeOnlyConverter(System.ComponentModel.TypeConverter):
    """Provides a type converter to convert System.TimeOnly objects to and from various other representations."""

    def can_convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, source_type: typing.Type) -> bool:
        """
        Gets a value indicating whether this converter can convert an object in the given source type to a System.TimeOnly
        object using the specified context.
        """
        ...

    def can_convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, destination_type: typing.Type) -> bool:
        ...

    def convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any) -> System.Object:
        """Converts the given value object to a System.TimeOnly object."""
        ...

    def convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any, destination_type: typing.Type) -> System.Object:
        """Converts the given value object from a System.TimeOnly object using the arguments."""
        ...


class DateOnlyConverter(System.ComponentModel.TypeConverter):
    """Provides a type converter to convert System.DateOnly objects to and from various other representations."""

    def can_convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, source_type: typing.Type) -> bool:
        """
        Gets a value indicating whether this converter can convert an object in the given source type to a System.DateOnly
        object using the specified context.
        """
        ...

    def can_convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, destination_type: typing.Type) -> bool:
        ...

    def convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any) -> System.Object:
        """Converts the given value object to a System.DateOnly object."""
        ...

    def convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any, destination_type: typing.Type) -> System.Object:
        """Converts the given value object from a System.DateOnly object using the arguments."""
        ...


class EnumConverter(System.ComponentModel.TypeConverter):
    """
    Provides a type converter to convert System.Enum objects to and
    from various other representations
    """

    @property
    def enum_type(self) -> typing.Type:
        """This property is protected."""
        ...

    @property
    def values(self) -> System.ComponentModel.TypeConverter.StandardValuesCollection:
        """This property is protected."""
        ...

    @values.setter
    def values(self, value: System.ComponentModel.TypeConverter.StandardValuesCollection) -> None:
        ...

    @property
    def comparer(self) -> System.Collections.IComparer:
        """
        Gets an System.Collections.IComparer interface that can
        be used to sort the values of the enumerator.
        
        This property is protected.
        """
        ...

    def __init__(self, type: typing.Type) -> None:
        """
        Initializes a new instance of the System.ComponentModel.EnumConverter class for the given
        type.
        """
        ...

    def can_convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, source_type: typing.Type) -> bool:
        """
        Gets a value indicating whether this converter can convert an object in the given
        source type to an enumeration object using the specified context.
        """
        ...

    def can_convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, destination_type: typing.Type) -> bool:
        """
        Gets a value indicating whether this converter can convert an object to the
        given destination type using the context.
        """
        ...

    def convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any) -> System.Object:
        """Converts the specified value object to an enumeration object."""
        ...

    def convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any, destination_type: typing.Type) -> System.Object:
        """Converts the given value object to the specified destination type."""
        ...

    def get_standard_values(self, context: System.ComponentModel.ITypeDescriptorContext) -> System.ComponentModel.TypeConverter.StandardValuesCollection:
        """
        Gets a collection of standard values for the data type this validator is
        designed for.
        """
        ...

    def get_standard_values_exclusive(self, context: System.ComponentModel.ITypeDescriptorContext) -> bool:
        """
        Gets a value indicating whether the list of standard values returned from
        System.ComponentModel.TypeConverter.GetStandardValues()
        is an exclusive list using the specified context.
        """
        ...

    def get_standard_values_supported(self, context: System.ComponentModel.ITypeDescriptorContext) -> bool:
        """
        Gets a value indicating whether this object supports a standard set of values
        that can be picked from a list using the specified context.
        """
        ...

    def is_valid(self, context: System.ComponentModel.ITypeDescriptorContext, value: typing.Any) -> bool:
        """Gets a value indicating whether the given object value is valid for this type."""
        ...


class LicenseProviderAttribute(System.Attribute):
    """
    Specifies the System.ComponentModel.LicenseProvider
    to use with a class.
    """

    DEFAULT: System.ComponentModel.LicenseProviderAttribute = ...
    """Specifies the default value, which is no provider. This static field is read-only."""

    @property
    def license_provider(self) -> typing.Type:
        """Gets the license provider to use with the associated class."""
        ...

    @property
    def type_id(self) -> System.Object:
        """
        This defines a unique ID for this attribute type. It is used
        by filtering algorithms to identify two attributes that are
        the same type. For most attributes, this just returns the
        Type instance for the attribute. LicenseProviderAttribute overrides this to include the type name and the
        provider type name.
        """
        ...

    @overload
    def __init__(self) -> None:
        """
        Initializes a new instance of the System.ComponentModel.LicenseProviderAttribute class without a license
        provider.
        """
        ...

    @overload
    def __init__(self, type_name: str) -> None:
        """
        Initializes a new instance of the System.ComponentModel.LicenseProviderAttribute class with
        the specified type.
        """
        ...

    @overload
    def __init__(self, type: typing.Type) -> None:
        """
        Initializes a new instance of the System.ComponentModel.LicenseProviderAttribute class with
        the specified type of license provider.
        """
        ...

    def equals(self, value: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        """Returns the hashcode for this object."""
        ...


class WarningException(System.SystemException):
    """Specifies an exception that is handled as a warning instead of an error."""

    @property
    def help_url(self) -> str:
        """Specifies the Help file associated with the warning. This field is read-only."""
        ...

    @property
    def help_topic(self) -> str:
        """Specifies the Help topic associated with the warning. This field is read-only."""
        ...

    @overload
    def __init__(self) -> None:
        """
        Initializes a new instance of the System.ComponentModel.WarningException class with the last Win32 error
        that occurred.
        """
        ...

    @overload
    def __init__(self, message: str) -> None:
        """
        Initializes a new instance of the System.ComponentModel.WarningException class with
        the specified message and no Help file.
        """
        ...

    @overload
    def __init__(self, message: str, help_url: str) -> None:
        """
        Initializes a new instance of the System.ComponentModel.WarningException class with
        the specified message, and with access to the specified Help file.
        """
        ...

    @overload
    def __init__(self, message: str, inner_exception: System.Exception) -> None:
        """
        Initializes a new instance of the Exception class with a specified error message and a
        reference to the inner exception that is the cause of this exception.
        FxCop CA1032: Multiple constructors are required to correctly implement a custom exception.
        """
        ...

    @overload
    def __init__(self, message: str, help_url: str, help_topic: str) -> None:
        """
        Initializes a new instance of the System.ComponentModel.WarningException class with the
        specified message, and with access to the specified Help file and topic.
        """
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """
        Need this constructor since Exception implements ISerializable.
        
        This method is protected.
        
        Obsoletions.LegacyFormatterImplMessage
        """
        ...

    def get_object_data(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """Obsoletions.LegacyFormatterImplMessage"""
        warnings.warn("Obsoletions.LegacyFormatterImplMessage", DeprecationWarning)


class RecommendedAsConfigurableAttribute(System.Attribute):
    """
    Specifies that the property can be used as an application setting.
    
    RecommendedAsConfigurableAttribute has been deprecated. Use System.ComponentModel.SettingsBindableAttribute instead.
    """

    @property
    def recommended_as_configurable(self) -> bool:
        """
        Gets a value indicating whether the property this
        attribute is bound to can be used as an application setting.
        """
        ...

    NO: System.ComponentModel.RecommendedAsConfigurableAttribute = ...
    """
    Specifies that a property cannot be used as an application setting. This
    static field is read-only.
    """

    YES: System.ComponentModel.RecommendedAsConfigurableAttribute = ...
    """
    Specifies
    that a property can be used as an application setting. This static field is read-only.
    """

    DEFAULT: System.ComponentModel.RecommendedAsConfigurableAttribute = ...
    """
    Specifies the default value for the System.ComponentModel.RecommendedAsConfigurableAttribute, which is System.ComponentModel.RecommendedAsConfigurableAttribute.No. This static field is
    read-only.
    """

    def __init__(self, recommended_as_configurable: bool) -> None:
        """
        Initializes a new instance of
        the System.ComponentModel.RecommendedAsConfigurableAttribute class.
        """
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        """Returns the hashcode for this object."""
        ...

    def is_default_attribute(self) -> bool:
        ...


class RunInstallerAttribute(System.Attribute):
    """
    Specifies whether an installer should be invoked during
    installation of an assembly.
    """

    @property
    def run_installer(self) -> bool:
        """
        Gets a value indicating whether an installer should be
        invoked during installation of an assembly.
        """
        ...

    YES: System.ComponentModel.RunInstallerAttribute = ...
    """
    Specifies that a
    component is visible in a visual designer. This static field is
    read-only.
    """

    NO: System.ComponentModel.RunInstallerAttribute = ...
    """
    Specifies that a
    component
    is not visible in a visual designer. This static field is
    read-only.
    """

    DEFAULT: System.ComponentModel.RunInstallerAttribute = ...
    """
    Specifies the default visibility, which is System.ComponentModel.RunInstallerAttribute.No. This static field is
    read-only.
    """

    def __init__(self, run_installer: bool) -> None:
        """
        Initializes a new instance of
        the System.ComponentModel.RunInstallerAttribute class.
        """
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        """Returns the hashcode for this object."""
        ...

    def is_default_attribute(self) -> bool:
        ...


class IListSource(metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    @abc.abstractmethod
    def contains_list_collection(self) -> bool:
        ...

    def get_list(self) -> System.Collections.IList:
        ...


class BindingDirection(Enum):
    """Specifies whether the template can be bound one-way or two-way."""

    ONE_WAY = 0
    """The template can only accept property values. Used with a generic ITemplate."""

    TWO_WAY = 1
    """The template can accept and expose property values. Used with an IBindableTemplate."""


class BindableAttribute(System.Attribute):
    """Specifies whether a property is appropriate to bind data to."""

    YES: System.ComponentModel.BindableAttribute = ...
    """
    Specifies that a property is appropriate to bind data to. This
    static field is read-only.
    """

    NO: System.ComponentModel.BindableAttribute = ...
    """
    Specifies that a property is not appropriate to bind data to.
    This static field is read-only.
    """

    DEFAULT: System.ComponentModel.BindableAttribute = ...
    """
    Specifies the default value for the System.ComponentModel.BindableAttribute, which
    is System.ComponentModel.BindableAttribute.No. This static field is
    read-only.
    """

    @property
    def bindable(self) -> bool:
        """Gets a value indicating whether a property is appropriate to bind data to."""
        ...

    @property
    def direction(self) -> System.ComponentModel.BindingDirection:
        """Gets a value indicating the direction(s) this property be bound to data."""
        ...

    @overload
    def __init__(self, bindable: bool) -> None:
        """Initializes a new instance of the System.ComponentModel.BindableAttribute class."""
        ...

    @overload
    def __init__(self, bindable: bool, direction: System.ComponentModel.BindingDirection) -> None:
        """Initializes a new instance of the System.ComponentModel.BindableAttribute class."""
        ...

    @overload
    def __init__(self, flags: System.ComponentModel.BindableSupport) -> None:
        """Initializes a new instance of the System.ComponentModel.BindableAttribute class."""
        ...

    @overload
    def __init__(self, flags: System.ComponentModel.BindableSupport, direction: System.ComponentModel.BindingDirection) -> None:
        """Initializes a new instance of the System.ComponentModel.BindableAttribute class."""
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def is_default_attribute(self) -> bool:
        ...


class MultilineStringConverter(System.ComponentModel.TypeConverter):
    """Provides a type converter to convert multiline strings to a simple string."""

    def convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any, destination_type: typing.Type) -> System.Object:
        """Converts the given value object to the specified destination type."""
        ...

    def get_properties(self, context: System.ComponentModel.ITypeDescriptorContext, value: typing.Any, attributes: typing.List[System.Attribute]) -> System.ComponentModel.PropertyDescriptorCollection:
        """
        Gets a collection of properties for the type of array specified by the value
        parameter using the specified context and attributes.
        """
        ...

    def get_properties_supported(self, context: System.ComponentModel.ITypeDescriptorContext) -> bool:
        """Gets a value indicating whether this object supports properties."""
        ...


class InstanceCreationEditor(System.Object, metaclass=abc.ABCMeta):
    """
    An InstanceCreationEditor allows the user to create an instance of a particular type of property from a dropdown
    Within the PropertyGrid. Usually, the text specified by InstanceCreationEditor.Text will be displayed on the
    dropdown from the PropertyGrid as a link or button. When clicked, the InstanceCreationEditor.CreateInstance
    method will be called with the Type of the object to create.
    """

    @property
    def text(self) -> str:
        ...

    def create_instance(self, context: System.ComponentModel.ITypeDescriptorContext, instance_type: typing.Type) -> System.Object:
        """
        This method is invoked when you user chooses the link displayed by the PropertyGrid for the InstanceCreationEditor.
        The object returned from this method must be an instance of the specified type, or null in which case the editor will do nothing.
        """
        ...


class InstallerTypeAttribute(System.Attribute):
    """Specifies the installer to use for a type to install components."""

    @property
    def installer_type(self) -> typing.Type:
        """Gets the type of installer associated with this attribute."""
        ...

    @overload
    def __init__(self, installer_type: typing.Type) -> None:
        """Initializes a new instance of the System.Windows.Forms.ComponentModel.InstallerTypeAttribute class."""
        ...

    @overload
    def __init__(self, type_name: str) -> None:
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...


class ComponentResourceManager(System.Resources.ResourceManager):
    """
    The ComponentResourceManager is a resource manager object that
    provides simple functionality for enumerating resources for
    a component or object.
    """

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, t: typing.Type) -> None:
        ...

    @overload
    def apply_resources(self, value: typing.Any, object_name: str) -> None:
        """
        This method examines all the resources for the current culture.
        When it finds a resource with a key in the format of
        "[object_name].[property name]" it will apply that resource's value
        to the corresponding property on the object. If there is no matching
        property the resource will be ignored.
        """
        ...

    @overload
    def apply_resources(self, value: typing.Any, object_name: str, culture: System.Globalization.CultureInfo) -> None:
        """
        This method examines all the resources for the provided culture.
        When it finds a resource with a key in the format of
        "[object_name].[property name]" or "[object_name]-[property name]" it will apply that resource's value
        to the corresponding property on the object. If there is no matching
        property the resource will be ignored.
        """
        ...

    def apply_resources_to_registered_type(self, value: typing.Any, object_name: str, culture: System.Globalization.CultureInfo) -> None:
        """
        This method examines all the resources for the provided culture.
        When it finds a resource with a key in the format of
        "[object_name].[property name]" or "[object_name]-[property name]" it will apply that resource's value
        to the corresponding property on the object. If there is no matching
        property the resource will be ignored.
        """
        ...


class ByteConverter(System.ComponentModel.BaseNumberConverter):
    """
    Provides a type converter to convert 8-bit unsigned integer objects
    to and from various other representations.
    """


class DateTimeConverter(System.ComponentModel.TypeConverter):
    """
    Provides a type converter to convert System.DateTime
    objects to and from various other representations.
    """

    def can_convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, source_type: typing.Type) -> bool:
        """
        Gets a value indicating whether this converter can convert an
        object in the given source type to a System.DateTime
        object using the specified context.
        """
        ...

    def can_convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, destination_type: typing.Type) -> bool:
        """
        Gets a value indicating whether this converter can convert an object
        to the given destination type using the context.
        """
        ...

    def convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any) -> System.Object:
        """Converts the given value object to a System.DateTime object."""
        ...

    def convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any, destination_type: typing.Type) -> System.Object:
        """
        Converts the given value object to a System.DateTime
        object using the arguments.
        """
        ...


class ContainerFilterService(System.Object, metaclass=abc.ABCMeta):
    """
    The Container and NestedContainer classes will call GetService for ContainerFilterService
    each time they need to construct a Components collection for return to a caller.
    ContainerFilterService may return an updated collection of components. This allows
    an external service to modify the view of components that are returned from a container.
    """

    def __init__(self) -> None:
        """This method is protected."""
        ...

    def filter_components(self, components: System.ComponentModel.ComponentCollection) -> System.ComponentModel.ComponentCollection:
        """
        Filters the components collection by optionally returning a new, modified collection.
        The default implementation returns the input collection, thereby performing no filtering.
        """
        ...


class HandledEventArgs(System.EventArgs):
    """
    Provides data for the System.ComponentModel.HandledEventArgs.Handled
    event.
    """

    @property
    def handled(self) -> bool:
        """Gets or sets a value indicating whether the event was handled in the application's event handler."""
        ...

    @handled.setter
    def handled(self, value: bool) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """
        Initializes a new instance of the System.ComponentModel.HandledEventArgs class with
        handled set to false.
        """
        ...

    @overload
    def __init__(self, default_handled_value: bool) -> None:
        """
        Initializes a new instance of the System.ComponentModel.HandledEventArgs class with
        handled set to the given value.
        """
        ...


class ProvidePropertyAttribute(System.Attribute):
    """Specifies which methods are extender properties."""

    @property
    def property_name(self) -> str:
        """Gets the name of a property that this class provides."""
        ...

    @property
    def receiver_type_name(self) -> str:
        """Gets the name of the data type this property can extend"""
        ...

    @property
    def type_id(self) -> System.Object:
        ...

    @overload
    def __init__(self, property_name: str, receiver_type: typing.Type) -> None:
        """Initializes a new instance of the System.ComponentModel.ProvidePropertyAttribute class."""
        ...

    @overload
    def __init__(self, property_name: str, receiver_type_name: str) -> None:
        """Initializes a new instance of the System.ComponentModel.ProvidePropertyAttribute class."""
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...


class INestedSite(System.ComponentModel.ISite, metaclass=abc.ABCMeta):
    """
    Nested containers site objects using INestedSite. A nested site is simply a site with
    an additional property that can retrieve the full nested name of a component.
    """

    @property
    @abc.abstractmethod
    def full_name(self) -> str:
        """
        Returns the full name of the component in this site in the format of <owner>.<component>.
        If this component's site has a null name, FullName also returns null.
        """
        ...


class HalfConverter(System.ComponentModel.BaseNumberConverter):
    """
    Provides a type converter to convert half-precision, floating point number objects to and
    from various other representations.
    """


class InheritanceLevel(Enum):
    """Specifies numeric IDs for different inheritance levels."""

    INHERITED = 1
    """Indicates that the object is inherited."""

    INHERITED_READ_ONLY = 2
    """Indicates that the object is inherited, but has read-only access."""

    NOT_INHERITED = 3
    """Indicates that the object is not inherited."""


class InheritanceAttribute(System.Attribute):
    """
    Marks instances of objects that are inherited from their base class. This
    class cannot be inherited.
    """

    INHERITED: System.ComponentModel.InheritanceAttribute = ...
    """
    Specifies that the component is inherited. This field is
    read-only.
    """

    INHERITED_READ_ONLY: System.ComponentModel.InheritanceAttribute = ...
    """
    Specifies that
    the component is inherited and is read-only. This field is
    read-only.
    """

    NOT_INHERITED: System.ComponentModel.InheritanceAttribute = ...
    """
    Specifies that the component is not inherited. This field is
    read-only.
    """

    DEFAULT: System.ComponentModel.InheritanceAttribute = ...
    """
    Specifies the default value for
    the InheritanceAttribute as NotInherited.
    """

    @property
    def inheritance_level(self) -> System.ComponentModel.InheritanceLevel:
        """
        Gets or sets
        the current inheritance level stored in this attribute.
        """
        ...

    @overload
    def __init__(self) -> None:
        """
        Initializes a new instance of the System.ComponentModel.Design.InheritanceAttribute
        class.
        """
        ...

    @overload
    def __init__(self, inheritance_level: System.ComponentModel.InheritanceLevel) -> None:
        """
        Initializes a new instance of the System.ComponentModel.Design.InheritanceAttribute class
        with the specified inheritance
        level.
        """
        ...

    def equals(self, value: typing.Any) -> bool:
        """Override to test for equality."""
        ...

    def get_hash_code(self) -> int:
        """Returns the hashcode for this object."""
        ...

    def is_default_attribute(self) -> bool:
        """Gets whether this attribute is the default."""
        ...

    def to_string(self) -> str:
        """Converts this attribute to a string."""
        ...


class ISupportInitializeNotification(System.ComponentModel.ISupportInitialize, metaclass=abc.ABCMeta):
    """Extends ISupportInitialize to allow dependent components to be notified when initialization is complete."""

    @property
    @abc.abstractmethod
    def is_initialized(self) -> bool:
        """Indicates whether initialization is complete yet."""
        ...

    @property
    @abc.abstractmethod
    def initialized(self) -> _EventContainer[typing.Callable[[System.Object, System.EventArgs], None], None]:
        """Sent when initialization is complete."""
        ...

    @initialized.setter
    def initialized(self, value: _EventContainer[typing.Callable[[System.Object, System.EventArgs], None], None]) -> None:
        ...


class LicenseException(System.SystemException):
    """Represents the exception thrown when a component cannot be granted a license."""

    @property
    def licensed_type(self) -> typing.Type:
        """Gets the type of the component that was not granted a license."""
        ...

    @overload
    def __init__(self, type: typing.Type, instance: typing.Any) -> None:
        """
        Initializes a new instance of the System.ComponentModel.LicenseException class for the
        specified type and instance.
        """
        ...

    @overload
    def __init__(self, type: typing.Type, instance: typing.Any, message: str) -> None:
        """
        Initializes a new instance of the System.ComponentModel.LicenseException class for the
        specified type and instance with the specified message.
        """
        ...

    @overload
    def __init__(self, type: typing.Type, instance: typing.Any, message: str, inner_exception: System.Exception) -> None:
        """
        Initializes a new instance of the System.ComponentModel.LicenseException class for the
        specified inner_exception, type and instance with the specified message.
        """
        ...

    @overload
    def __init__(self, type: typing.Type) -> None:
        """
        Initializes a new instance of the System.ComponentModel.LicenseException class for the
        specified type.
        """
        ...

    @overload
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """
        Need this constructor since Exception implements ISerializable.
        
        This method is protected.
        
        Obsoletions.LegacyFormatterImplMessage
        """
        ...

    def get_object_data(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """
        Need this since Exception implements ISerializable.
        
        Obsoletions.LegacyFormatterImplMessage
        """
        warnings.warn("Obsoletions.LegacyFormatterImplMessage", DeprecationWarning)


class Int32Converter(System.ComponentModel.BaseNumberConverter):
    """
    Provides a type converter to convert 32-bit signed integer objects to and
    from various other representations.
    """


class DoubleConverter(System.ComponentModel.BaseNumberConverter):
    """
    Provides a type converter to convert double-precision, floating point number objects
    to and from various other representations.
    """


class TypeListConverter(System.ComponentModel.TypeConverter, metaclass=abc.ABCMeta):
    """Provides a type converter that can be used to populate a list box with available types."""

    def __init__(self, types: typing.List[typing.Type]) -> None:
        """
        Initializes a new instance of the System.ComponentModel.TypeListConverter class using
        the type array as the available types.
        
        This method is protected.
        """
        ...

    def can_convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, source_type: typing.Type) -> bool:
        """
        Gets a value indicating whether this converter
        can convert an object in the given source type to an enumeration object using
        the specified context.
        """
        ...

    def can_convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, destination_type: typing.Type) -> bool:
        """
        Gets a value indicating whether this converter can convert an object
        to the given destination type using the context.
        """
        ...

    def convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any) -> System.Object:
        """Converts the specified value object to an enumeration object."""
        ...

    def convert_to(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any, destination_type: typing.Type) -> System.Object:
        """Converts the given value object to the specified destination type."""
        ...

    def get_standard_values(self, context: System.ComponentModel.ITypeDescriptorContext) -> System.ComponentModel.TypeConverter.StandardValuesCollection:
        """Gets a collection of standard values for the data type this validator is designed for."""
        ...

    def get_standard_values_exclusive(self, context: System.ComponentModel.ITypeDescriptorContext) -> bool:
        """
        Gets a value indicating whether the list of standard values returned from
        System.ComponentModel.TypeListConverter.GetStandardValues is an exclusive list.
        """
        ...

    def get_standard_values_supported(self, context: System.ComponentModel.ITypeDescriptorContext) -> bool:
        """
        Gets a value indicating whether this object supports a standard set of values that can be
        picked from a list using the specified context.
        """
        ...


class DesignTimeVisibleAttribute(System.Attribute):
    """
    DesignTimeVisibileAttribute marks a component's visibility. If
    DesignTimeVisibileAttribute.Yes is present, a visual designer can show
    this component on a designer.
    """

    @property
    def visible(self) -> bool:
        """
        True if this component should be shown at design time, or false
        if it shouldn't.
        """
        ...

    YES: System.ComponentModel.DesignTimeVisibleAttribute = ...
    """Marks a component as visible in a visual designer."""

    NO: System.ComponentModel.DesignTimeVisibleAttribute = ...
    """Marks a component as not visible in a visual designer."""

    DEFAULT: System.ComponentModel.DesignTimeVisibleAttribute = ...
    """The default visibility. (equal to Yes.)"""

    @overload
    def __init__(self, visible: bool) -> None:
        """
        Creates a new DesignTimeVisibleAttribute with the visible
        property set to the given value.
        """
        ...

    @overload
    def __init__(self) -> None:
        """
        Creates a new DesignTimeVisibleAttribute set to the default
        value of true.
        """
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def is_default_attribute(self) -> bool:
        ...


class UInt128Converter(System.ComponentModel.BaseNumberConverter):
    """
    Provides a type converter to convert 128-bit unsigned integer objects to and
    from various other representations.
    """


class Int128Converter(System.ComponentModel.BaseNumberConverter):
    """
    Provides a type converter to convert 128-bit signed integer objects to and
    from various other representations.
    """


class MaskedTextProvider(System.Object, System.ICloneable):
    """
    Provides functionality for formatting a test string against a mask string.
    MaskedTextProvider is stateful, it keeps information about the input characters so
    multiple call to Add/Remove will work in the same buffer.
    Most of the operations are performed on a virtual string containing the input characters as opposed
    to the test string itself, since mask literals cannot be modified (i.e: replacing on a literal position
    will actually replace on the nearest edit position forward).
    """

    @property
    def allow_prompt_as_input(self) -> bool:
        """Specifies whether the prompt character should be treated as a valid input character or not."""
        ...

    @property
    def assigned_edit_position_count(self) -> int:
        """Retrieves the number of editable characters that have been set."""
        ...

    @property
    def available_edit_position_count(self) -> int:
        """Retrieves the number of editable characters that have been set."""
        ...

    @property
    def culture(self) -> System.Globalization.CultureInfo:
        """The culture that determines the value of the localizable mask language separators and placeholders."""
        ...

    DEFAULT_PASSWORD_CHAR: str
    """The system password char."""

    @property
    def edit_position_count(self) -> int:
        """The number of editable positions in the test string."""
        ...

    @property
    def edit_positions(self) -> System.Collections.IEnumerator:
        """Returns a new IEnumerator object containing the editable positions in the test string."""
        ...

    @property
    def include_literals(self) -> bool:
        """Specifies whether the formatted string should include literals."""
        ...

    @include_literals.setter
    def include_literals(self, value: bool) -> None:
        ...

    @property
    def include_prompt(self) -> bool:
        """
        Specifies whether or not the prompt character should be included in the formatted text when there are
        character slots available in the mask.
        """
        ...

    @include_prompt.setter
    def include_prompt(self, value: bool) -> None:
        ...

    @property
    def ascii_only(self) -> bool:
        """Specifies whether only ASCII characters are accepted as valid input."""
        ...

    @property
    def is_password(self) -> bool:
        """Specifies whether the user text is to be rendered as password characters."""
        ...

    @is_password.setter
    def is_password(self, value: bool) -> None:
        ...

    INVALID_INDEX: int
    """A negative value representing an index outside the test string."""

    @property
    def last_assigned_position(self) -> int:
        """
        The last edit position (relative to the origin not to time) in the test string where
        an input character has been placed. If no position has been assigned, InvalidIndex is returned.
        """
        ...

    @property
    def length(self) -> int:
        """Specifies the length of the test string."""
        ...

    @property
    def mask(self) -> str:
        """The mask to be applied to the test string."""
        ...

    @property
    def mask_completed(self) -> bool:
        """Specifies whether all required inputs have been provided into the mask successfully."""
        ...

    @property
    def mask_full(self) -> bool:
        """Specifies whether all inputs (required and optional) have been provided into the mask successfully."""
        ...

    @property
    def password_char(self) -> str:
        """
        Specifies the character to be used in the formatted string in place of editable characters.
        Use the null character '\\0' to reset this property.
        """
        ...

    @password_char.setter
    def password_char(self, value: str) -> None:
        ...

    @property
    def prompt_char(self) -> str:
        """Specifies the prompt character to be used in the formatted string for unsupplied characters."""
        ...

    @prompt_char.setter
    def prompt_char(self, value: str) -> None:
        ...

    @property
    def reset_on_prompt(self) -> bool:
        """
        Specifies whether to reset and skip the current position if editable, when the input character has
        the same value as the prompt.
        
        This is useful when assigning text that was saved including the prompt; in this case
        we don't want to take the prompt character as valid input but don't want to fail the test either.
        """
        ...

    @reset_on_prompt.setter
    def reset_on_prompt(self, value: bool) -> None:
        ...

    @property
    def reset_on_space(self) -> bool:
        """
        Specifies whether to reset and skip the current position if editable, when the input is the space character.
        
        This is useful when assigning text that was saved excluding the prompt (prompt replaced with spaces);
        in this case we don't want to take the space but instead, reset the position (or just skip it) so the
        next input character gets positioned correctly.
        """
        ...

    @reset_on_space.setter
    def reset_on_space(self, value: bool) -> None:
        ...

    @property
    def skip_literals(self) -> bool:
        """
        Specifies whether to skip the current position if non-editable and the input character has the same
        value as the literal at that position.
        
        This is useful for round-tripping the text when saved with literals; when assigned back we don't want
        to treat literals as input.
        """
        ...

    @skip_literals.setter
    def skip_literals(self, value: bool) -> None:
        ...

    def __getitem__(self, index: int) -> str:
        """Indexer."""
        ...

    @overload
    def __init__(self, mask: str) -> None:
        """Creates a MaskedTextProvider object from the specified mask."""
        ...

    @overload
    def __init__(self, mask: str, restrict_to_ascii: bool) -> None:
        """
        Creates a MaskedTextProvider object from the specified mask.
        'restrict_to_ascii' specifies whether the input characters should be restricted to ASCII characters only.
        """
        ...

    @overload
    def __init__(self, mask: str, culture: System.Globalization.CultureInfo) -> None:
        """
        Creates a MaskedTextProvider object from the specified mask.
        'culture' is used to set the separator characters to the corresponding locale character; if null, the current
             culture is used.
        """
        ...

    @overload
    def __init__(self, mask: str, culture: System.Globalization.CultureInfo, restrict_to_ascii: bool) -> None:
        """
        Creates a MaskedTextProvider object from the specified mask.
        'culture' is used to set the separator characters to the corresponding locale character; if null, the current
             culture is used.
        'restrict_to_ascii' specifies whether the input characters should be restricted to ASCII characters only.
        """
        ...

    @overload
    def __init__(self, mask: str, password_char: str, allow_prompt_as_input: bool) -> None:
        """
        Creates a MaskedTextProvider object from the specified mask .
        'password_char' specifies the character to be used in the password string.
        'allow_prompt_as_input' specifies whether the prompt character should be accepted as a valid input or not.
        """
        ...

    @overload
    def __init__(self, mask: str, culture: System.Globalization.CultureInfo, password_char: str, allow_prompt_as_input: bool) -> None:
        """
        Creates a MaskedTextProvider object from the specified mask .
        'password_char' specifies the character to be used in the password string.
        'allow_prompt_as_input' specifies whether the prompt character should be accepted as a valid input or not.
        """
        ...

    @overload
    def __init__(self, mask: str, culture: System.Globalization.CultureInfo, allow_prompt_as_input: bool, prompt_char: str, password_char: str, restrict_to_ascii: bool) -> None:
        """
        Creates a MaskedTextProvider object from the specified mask.
        'culture' is used to set the separator characters to the corresponding locale character; if null, the current
             culture is used.
        'allow_prompt_as_input' specifies whether the prompt character should be accepted as a valid input or not.
        'prompt_char' specifies the character to be used for the prompt.
        'password_char' specifies the character to be used in the password string.
        'restrict_to_ascii' specifies whether the input characters should be restricted to ASCII characters only.
        """
        ...

    @overload
    def add(self, input: str) -> bool:
        """
        Attempts to add the specified charactert to the last unoccupied positions in the test string (append text to
        the virtual string).
        Returns true on success, false otherwise.
        """
        ...

    @overload
    def add(self, input: str, test_position: typing.Optional[int], result_hint: typing.Optional[System.ComponentModel.MaskedTextResultHint]) -> typing.Tuple[bool, int, System.ComponentModel.MaskedTextResultHint]:
        """
        Attempts to add the specified charactert to the last unoccupied positions in the test string (append text to
        the virtual string).
        On exit the test_position contains last position where the primary operation was actually performed if successful,
        otherwise the first position that made the test fail. This position is relative to the test string.
        The MaskedTextResultHint out param gives a hint about the operation result reason.
        Returns true on success, false otherwise.
        """
        ...

    @overload
    def clear(self) -> None:
        """Resets the state of the test string edit chars. (Remove all characters from the virtual string)."""
        ...

    @overload
    def clear(self, result_hint: typing.Optional[System.ComponentModel.MaskedTextResultHint]) -> typing.Tuple[None, System.ComponentModel.MaskedTextResultHint]:
        """
        Resets the state of the test string edit chars. (Remove all characters from the virtual string).
        The MaskedTextResultHint out param gives more information about the operation result.
        """
        ...

    def clone(self) -> System.Object:
        """
        Creates a 'clean' (no text assigned) MaskedTextProvider instance with the same property values as the
        current instance.
        Derived classes can override this method and call base.Clone to get proper cloning semantics but must
        implement the full-parameter constructor (passing parameters to the base constructor as well).
        """
        ...

    def find_assigned_edit_position_from(self, position: int, direction: bool) -> int:
        """
        Gets the position of the first edit char in the test string, the search starts from the specified
        position included.
        Returns InvalidIndex if it doesn't find one.
        """
        ...

    def find_assigned_edit_position_in_range(self, start_position: int, end_position: int, direction: bool) -> int:
        """
        Gets the position of the first edit char in the test string in the specified range, the search starts from
        the specified  position included.
        Returns InvalidIndex if it doesn't find one.
        """
        ...

    def find_edit_position_from(self, position: int, direction: bool) -> int:
        """
        Gets the position of the first assigned edit char in the test string, the search starts from the specified
        position included and in the direction specified (true == forward). The positions are relative to the test
        string.
        Returns InvalidIndex if it doesn't find one.
        """
        ...

    def find_edit_position_in_range(self, start_position: int, end_position: int, direction: bool) -> int:
        """
        Gets the position of the first assigned edit char in the test string; the search is performed in the specified
        positions range and in the specified direction.
        The positions are relative to the test string.
        Returns InvalidIndex if it doesn't find one.
        """
        ...

    def find_non_edit_position_from(self, position: int, direction: bool) -> int:
        """
        Gets the position of the first non edit position in the test string; the search is performed from the specified
        position and in the specified direction.
        The positions are relative to the test string.
        Returns InvalidIndex if it doesn't find one.
        """
        ...

    def find_non_edit_position_in_range(self, start_position: int, end_position: int, direction: bool) -> int:
        """
        Gets the position of the first non edit position in the test string; the search is performed in the specified
        positions range and in the specified direction.
        The positions are relative to the test string.
        Returns InvalidIndex if it doesn't find one.
        """
        ...

    def find_unassigned_edit_position_from(self, position: int, direction: bool) -> int:
        """
        Gets the position of the first edit char in the test string, the search starts from the specified
        position included.
        Returns InvalidIndex if it doesn't find one.
        """
        ...

    def find_unassigned_edit_position_in_range(self, start_position: int, end_position: int, direction: bool) -> int:
        """
        Gets the position of the first edit char in the test string in the specified range; the search starts
        from the specified position included.
        Returns InvalidIndex if it doesn't find one.
        """
        ...

    @staticmethod
    def get_operation_result_from_hint(hint: System.ComponentModel.MaskedTextResultHint) -> bool:
        """Specifies whether the specified MaskedTextResultHint denotes success or not."""
        ...

    @overload
    def insert_at(self, input: str, position: int) -> bool:
        """
        Attempts to insert the specified character at the specified position in the test string.
        (Insert character in the virtual string).
        Returns true on success, false otherwise.
        """
        ...

    @overload
    def insert_at(self, input: str, position: int, test_position: typing.Optional[int], result_hint: typing.Optional[System.ComponentModel.MaskedTextResultHint]) -> typing.Tuple[bool, int, System.ComponentModel.MaskedTextResultHint]:
        """
        Attempts to insert the specified character at the specified position in the test string, shifting characters
        at upper positions (if any) to make room for the input.
        On exit the test_position contains last position where the primary operation was actually performed if successful,
        otherwise the first position that made the test fail. This position is relative to the test string.
        The MaskedTextResultHint out param gives more information about the operation result.
        Returns true on success, false otherwise.
        """
        ...

    def is_available_position(self, position: int) -> bool:
        """
        Checks whether the specified position is available for assignment. Returns false if it is assigned
        or it is not editable, true otherwise.
        """
        ...

    def is_edit_position(self, position: int) -> bool:
        """Checks whether the specified position in the test string is editable."""
        ...

    @staticmethod
    def is_valid_input_char(c: str) -> bool:
        """Checks whether the specified character is a valid input char."""
        ...

    @staticmethod
    def is_valid_mask_char(c: str) -> bool:
        """Checks whether the specified character is a valid input char."""
        ...

    @staticmethod
    def is_valid_password_char(c: str) -> bool:
        """Checks whether the specified character is a valid password char."""
        ...

    @overload
    def remove(self) -> bool:
        """Removes the last character from the formatted string. (Remove last character in virtual string)."""
        ...

    @overload
    def remove(self, test_position: typing.Optional[int], result_hint: typing.Optional[System.ComponentModel.MaskedTextResultHint]) -> typing.Tuple[bool, int, System.ComponentModel.MaskedTextResultHint]:
        """
        Removes the last character from the formatted string. (Remove last character in virtual string).
        On exit the out param contains the position where the operation was actually performed.
        This position is relative to the test string.
        The MaskedTextResultHint out param gives more information about the operation result.
        Returns true on success, false otherwise.
        """
        ...

    @overload
    def remove_at(self, position: int) -> bool:
        """
        Removes the character from the formatted string at the specified position and shifts characters
        left.
        True if character shifting is successful.
        """
        ...

    @overload
    def remove_at(self, start_position: int, end_position: int) -> bool:
        """
        Removes all characters in edit position from in the test string at the specified start and end positions
        and shifts any remaining characters left. (Remove characters from the virtual string).
        Returns true on success, false otherwise.
        """
        ...

    @overload
    def remove_at(self, start_position: int, end_position: int, test_position: typing.Optional[int], result_hint: typing.Optional[System.ComponentModel.MaskedTextResultHint]) -> typing.Tuple[bool, int, System.ComponentModel.MaskedTextResultHint]:
        """
        Removes all characters in edit position from in the test string at the specified start and end positions
        and shifts any remaining characters left.
        On exit the test_position contains last position where the primary operation was actually performed if successful,
        otherwise the first position that made the test fail. This position is relative to the test string.
        The MaskedTextResultHint out param gives more information about the operation result.
        Returns true on success, false otherwise.
        """
        ...

    @overload
    def replace(self, input: str, position: int) -> bool:
        """
        Replaces the first editable character in the test string from the specified position, with the specified
        character (Replace is performed in the virtual string), unless the character at the specified position
        is to be escaped.
        Returns true on success, false otherwise.
        """
        ...

    @overload
    def replace(self, input: str, position: int, test_position: typing.Optional[int], result_hint: typing.Optional[System.ComponentModel.MaskedTextResultHint]) -> typing.Tuple[bool, int, System.ComponentModel.MaskedTextResultHint]:
        """
        Replaces the first editable character in the test string from the specified position, with the specified
        character, unless the character at the specified position is to be escaped.
        On exit the test_position contains last position where the primary operation was actually performed if successful,
        otherwise the first position that made the test fail. This position is relative to the test string.
        The MaskedTextResultHint out param gives more information about the operation result.
        Returns true on success, false otherwise.
        """
        ...

    @overload
    def replace(self, input: str, start_position: int, end_position: int, test_position: typing.Optional[int], result_hint: typing.Optional[System.ComponentModel.MaskedTextResultHint]) -> typing.Tuple[bool, int, System.ComponentModel.MaskedTextResultHint]:
        """
        Replaces the first editable character in the test string from the specified position, with the specified
        character and removes any remaining characters in the range unless the character at the specified position
        is to be escaped.
        If specified range covers more than one assigned edit character, shift-left is performed after replacing
        the first character. This is useful when in an edit box the user selects text and types a character to replace it.
        On exit the test_position contains last position where the primary operation was actually performed if successful,
        otherwise the first position that made the test fail. This position is relative to the test string.
        The MaskedTextResultHint out param gives more information about the operation result.
        Returns true on success, false otherwise.
        """
        ...

    @overload
    def set(self, input: str) -> bool:
        """
        Sets the edit characters in the test string to the ones specified in the input string if all characters
        are valid.
        If passwordChar is assigned, it is rendered in the output string instead of the user-supplied values.
        """
        ...

    @overload
    def set(self, input: str, test_position: typing.Optional[int], result_hint: typing.Optional[System.ComponentModel.MaskedTextResultHint]) -> typing.Tuple[bool, int, System.ComponentModel.MaskedTextResultHint]:
        """
        Sets the edit characters in the test string to the ones specified in the input string if all characters
        are valid.
        On exit the test_position contains last position where the primary operation was actually performed if successful,
        otherwise the first position that made the test fail. This position is relative to the test string.
        The MaskedTextResultHint out param gives more information about the operation result.
        If passwordChar is assigned, it is rendered in the output string instead of the user-supplied values.
        """
        ...

    def to_display_string(self) -> str:
        """
        Returns a formatted string based on the mask, honoring only the PasswordChar property. prompt character
        and literals are always included. This is the text to be shown in a control when it has the focus.
        """
        ...

    @overload
    def to_string(self) -> str:
        """
        Returns a formatted string based on the mask, honoring  IncludePrompt and IncludeLiterals but ignoring
        PasswordChar.
        """
        ...

    @overload
    def to_string(self, ignore_password_char: bool) -> str:
        """
        Returns a formatted string based on the mask, honoring the IncludePrompt and IncludeLiterals properties,
        and PasswordChar depending on the value of the 'ignore_password_char' parameter.
        """
        ...

    @overload
    def to_string(self, start_position: int, length: int) -> str:
        """
        Returns a formatted string starting at the specified position and for the specified number of character,
        based on the mask, honoring IncludePrompt and IncludeLiterals but ignoring PasswordChar.
        Parameters are relative to the test string.
        """
        ...

    @overload
    def to_string(self, ignore_password_char: bool, start_position: int, length: int) -> str:
        """
        Returns a formatted string starting at the specified position and for the specified number of character,
        based on the mask, honoring the IncludePrompt, IncludeLiterals properties and PasswordChar depending on
        the 'ignore_password_char' parameter.
        Parameters are relative to the test string.
        """
        ...

    @overload
    def to_string(self, include_prompt: bool, include_literals: bool) -> str:
        """
        Returns a formatted string based on the mask, ignoring the PasswordChar and according to the include_prompt
        and include_literals parameters.
        """
        ...

    @overload
    def to_string(self, include_prompt: bool, include_literals: bool, start_position: int, length: int) -> str:
        """
        Returns a formatted string starting at the specified position and for the specified number of character,
        based on the mask, according to the ignorePasswordChar, include_prompt and include_literals parameters.
        Parameters are relative to the test string.
        """
        ...

    @overload
    def to_string(self, ignore_password_char: bool, include_prompt: bool, include_literals: bool, start_position: int, length: int) -> str:
        """
        Returns a formatted string starting at the specified position and for the specified number of character,
        based on the mask, according to the ignore_password_char, include_prompt and include_literals parameters.
        Parameters are relative to the test string.
        """
        ...

    def verify_char(self, input: str, position: int, hint: typing.Optional[System.ComponentModel.MaskedTextResultHint]) -> typing.Tuple[bool, System.ComponentModel.MaskedTextResultHint]:
        """Tests whether the specified character would be set successfully at the specified position."""
        ...

    def verify_escape_char(self, input: str, position: int) -> bool:
        """Tests whether the specified character would be escaped at the specified position."""
        ...

    @overload
    def verify_string(self, input: str) -> bool:
        """Verifies the test string against the mask."""
        ...

    @overload
    def verify_string(self, input: str, test_position: typing.Optional[int], result_hint: typing.Optional[System.ComponentModel.MaskedTextResultHint]) -> typing.Tuple[bool, int, System.ComponentModel.MaskedTextResultHint]:
        """
        Verifies the test string against the mask.
        On exit the test_position contains last position where the primary operation was actually performed if successful,
        otherwise the first position that made the test fail. This position is relative to the test string.
        The MaskedTextResultHint out param gives more information about the operation result.
        Returns true on success, false otherwise.
        """
        ...


class CustomTypeDescriptor(System.Object, System.ComponentModel.ICustomTypeDescriptor, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    def require_registered_types(self) -> typing.Optional[bool]:
        """Whether types are required to be registered through TypeDescriptionProvider.RegisterType{T}."""
        ...

    @overload
    def __init__(self) -> None:
        """
        Creates a new CustomTypeDescriptor object. There are two versions
        of this constructor. The version that takes no parameters simply
        calls the version that takes a parent and passes null as the
        parent value. If the parent is null, CustomTypeDescriptor returns
        the defined default values for each method. If the parent is
        non-null, CustomTypeDescriptor calls the parent's version of
        the method.
        
        This method is protected.
        """
        ...

    @overload
    def __init__(self, parent: System.ComponentModel.ICustomTypeDescriptor) -> None:
        """
        Creates a new CustomTypeDescriptor object. There are two versions
        of this constructor. The version that takes no parameters simply
        calls the version that takes a parent and passes null as the
        parent value. If the parent is null, CustomTypeDescriptor returns
        the defined default values for each method. If the parent is
        non-null, CustomTypeDescriptor calls the parent's version of
        the method.
        
        This method is protected.
        """
        ...

    def get_attributes(self) -> System.ComponentModel.AttributeCollection:
        """
        The GetAttributes method returns the type-level attributes for
        the type this custom type descriptor is providing information for.
        You must always return a valid collection from this method.
        """
        ...

    def get_class_name(self) -> str:
        """
        The GetClassName method returns the fully qualified name of the
        class this type descriptor is representing. Returning null from
        this method causes the TypeDescriptor object to return the
        default class name.
        """
        ...

    def get_component_name(self) -> str:
        """
        The GetComponentName method returns the name of the component instance
        this type descriptor is describing.
        """
        ...

    def get_converter(self) -> System.ComponentModel.TypeConverter:
        """
        The GetConverter method returns a type converter for the type this type
        descriptor is representing.
        """
        ...

    def get_converter_from_registered_type(self) -> System.ComponentModel.TypeConverter:
        """
        The GetConverterFromRegisteredType method returns a type converter for the type this type
        descriptor is representing.
        """
        ...

    def get_default_event(self) -> System.ComponentModel.EventDescriptor:
        """
        The GetDefaultEvent method returns the event descriptor for the default
        event on the object this type descriptor is representing.
        """
        ...

    def get_default_property(self) -> System.ComponentModel.PropertyDescriptor:
        """
        The GetDefaultProperty method returns the property descriptor for the
        default property on the object this type descriptor is representing.
        """
        ...

    def get_editor(self, editor_base_type: typing.Type) -> System.Object:
        """
        The GetEditor method returns an editor of the given type that is
        to be associated with the class this type descriptor is representing.
        """
        ...

    @overload
    def get_events(self) -> System.ComponentModel.EventDescriptorCollection:
        """
        The GetEvents method returns a collection of event descriptors
        for the object this type descriptor is representing.
        """
        ...

    @overload
    def get_events(self, attributes: typing.List[System.Attribute]) -> System.ComponentModel.EventDescriptorCollection:
        """
        The GetEvents method returns a collection of event descriptors
        for the object this type descriptor is representing. An optional
        attribute array may be provided to filter the collection that is
        returned. If no parent is provided,this will return an empty
        event collection.
        """
        ...

    def get_events_from_registered_type(self) -> System.ComponentModel.EventDescriptorCollection:
        """
        Returns a collection of event descriptors
        for the object this type descriptor is representing.
        """
        ...

    @overload
    def get_properties(self) -> System.ComponentModel.PropertyDescriptorCollection:
        """
        The GetProperties method returns a collection of property descriptors
        for the object this type descriptor is representing.
        """
        ...

    @overload
    def get_properties(self, attributes: typing.List[System.Attribute]) -> System.ComponentModel.PropertyDescriptorCollection:
        """
        The GetProperties method returns a collection of property descriptors
        for the object this type descriptor is representing. An optional
        attribute array may be provided to filter the collection that is returned.
        If no parent is provided,this will return an empty
        property collection.
        """
        ...

    def get_properties_from_registered_type(self) -> System.ComponentModel.PropertyDescriptorCollection:
        """
        The GetProperties method returns a collection of property descriptors
        for the object this type descriptor is representing.
        """
        ...

    def get_property_owner(self, pd: System.ComponentModel.PropertyDescriptor) -> System.Object:
        """
        The GetPropertyOwner method returns an instance of an object that
        owns the given property for the object this type descriptor is representing.
        An optional attribute array may be provided to filter the collection that is
        returned. Returning null from this method causes the TypeDescriptor object
        to use its default type description services.
        """
        ...


class LookupBindingPropertiesAttribute(System.Attribute):
    """Specifies the data source and data member properties for a component."""

    @property
    def data_source(self) -> str:
        """
        Gets the name of the data source property for the component this attribute is
        bound to.
        """
        ...

    @property
    def display_member(self) -> str:
        """
        Gets the name of the display member property for the component this attribute is
        bound to.
        """
        ...

    @property
    def value_member(self) -> str:
        """
        Gets the name of the value member property for the component this attribute is
        bound to.
        """
        ...

    @property
    def lookup_member(self) -> str:
        """
        Gets the name of the  member property for the component this attribute is
        bound to.
        """
        ...

    DEFAULT: System.ComponentModel.LookupBindingPropertiesAttribute = ...
    """
    Specifies the default value for the System.ComponentModel.LookupBindingPropertiesAttribute, which is null. This
    static field is read-only.
    """

    @overload
    def __init__(self) -> None:
        """
        Initializes a new instance of
        the System.ComponentModel.LookupBindingPropertiesAttribute class.
        """
        ...

    @overload
    def __init__(self, data_source: str, display_member: str, value_member: str, lookup_member: str) -> None:
        """
        Initializes a new instance of
        the System.ComponentModel.LookupBindingPropertiesAttribute class.
        """
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...


class ListBindableAttribute(System.Attribute):
    """This class has no documentation."""

    YES: System.ComponentModel.ListBindableAttribute = ...

    NO: System.ComponentModel.ListBindableAttribute = ...

    DEFAULT: System.ComponentModel.ListBindableAttribute = ...

    @property
    def list_bindable(self) -> bool:
        ...

    @overload
    def __init__(self, list_bindable: bool) -> None:
        ...

    @overload
    def __init__(self, flags: System.ComponentModel.BindableSupport) -> None:
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        """Returns the hashcode for this object."""
        ...

    def is_default_attribute(self) -> bool:
        ...


class StringConverter(System.ComponentModel.TypeConverter):
    """
    Provides a type converter to convert string objects to and from various other
    representations.
    """

    def can_convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, source_type: typing.Type) -> bool:
        """
        Gets a value indicating whether this converter can convert an object in the
        given source type to a string using the specified context.
        """
        ...

    def convert_from(self, context: System.ComponentModel.ITypeDescriptorContext, culture: System.Globalization.CultureInfo, value: typing.Any) -> System.Object:
        """Converts the specified value object to a string object."""
        ...


class ToolboxItemAttribute(System.Attribute):
    """Specifies attributes for a toolbox item."""

    DEFAULT: System.ComponentModel.ToolboxItemAttribute = ...
    """Initializes a new instance of ToolboxItemAttribute and sets the type to"""

    NONE: System.ComponentModel.ToolboxItemAttribute = ...
    """
    Initializes a new instance of ToolboxItemAttribute and sets the type to
    null.
    """

    @property
    def toolbox_item_type(self) -> typing.Type:
        """Gets the toolbox item's type."""
        ...

    @property
    def toolbox_item_type_name(self) -> str:
        ...

    @overload
    def __init__(self, default_type: bool) -> None:
        """Initializes a new instance of ToolboxItemAttribute and specifies if default values should be used."""
        ...

    @overload
    def __init__(self, toolbox_item_type_name: str) -> None:
        """Initializes a new instance of ToolboxItemAttribute and specifies the name of the type."""
        ...

    @overload
    def __init__(self, toolbox_item_type: typing.Type) -> None:
        """Initializes a new instance of ToolboxItemAttribute and specifies the type of the toolbox item."""
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def is_default_attribute(self) -> bool:
        """Gets whether the attribute is the default attribute."""
        ...


class SettingsBindableAttribute(System.Attribute):
    """
    Use this attribute to specify typical properties on components that can be bound
    to application settings.
    """

    YES: System.ComponentModel.SettingsBindableAttribute = ...
    """Specifies that a property is appropriate to bind settings to."""

    NO: System.ComponentModel.SettingsBindableAttribute = ...
    """Specifies that a property is not appropriate to bind settings to."""

    @property
    def bindable(self) -> bool:
        """Gets a value indicating whether a property is appropriate to bind settings to."""
        ...

    def __init__(self, bindable: bool) -> None:
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...


class PropertyTabScope(Enum):
    """Specifies the function scope of a tab in the properties window."""

    STATIC = 0
    """This tab will be added to the properties window and can never be removed."""

    GLOBAL = 1
    """
    This tab will be added to the properties window and can only be explicitly removed by a
    component outside the properties window.
    """

    DOCUMENT = 2
    """
    This tab will be added to the properties window and will be removed when the currently selected document changes.
    This tab is relevant to items on the current document.
    """

    COMPONENT = 3
    """
    This tab will be added to the properties window for the current component only, and is
    removed when the component is no longer selected.
    """


class PropertyTabAttribute(System.Attribute):
    """
    Identifies the property tab or tabs that should be displayed for the
    specified class or classes.
    """

    @property
    def tab_classes(self) -> typing.List[typing.Type]:
        """Gets the types of tab that this attribute specifies."""
        ...

    @property
    def tab_class_names(self) -> typing.List[str]:
        """This property is protected."""
        ...

    @property
    def tab_scopes(self) -> typing.List[System.ComponentModel.PropertyTabScope]:
        """Gets the scopes of tabs for this System.ComponentModel.Design.PropertyTabAttribute, from System.ComponentModel.Design.PropertyTabScope."""
        ...

    @overload
    def __init__(self) -> None:
        """
        Basic constructor that creates a PropertyTabAttribute. Use this ctor to derive from this
        attribute and specify multiple tab types by calling InitializeArrays.
        """
        ...

    @overload
    def __init__(self, tab_class: typing.Type) -> None:
        """
        Basic constructor that creates a property tab attribute that will create a tab
        of the specified type.
        """
        ...

    @overload
    def __init__(self, tab_class_name: str) -> None:
        """
        Basic constructor that creates a property tab attribute that will create a tab
        of the specified type.
        """
        ...

    @overload
    def __init__(self, tab_class: typing.Type, tab_scope: System.ComponentModel.PropertyTabScope) -> None:
        """
        Basic constructor that creates a property tab attribute that will create a tab
        of the specified type.
        """
        ...

    @overload
    def __init__(self, tab_class_name: str, tab_scope: System.ComponentModel.PropertyTabScope) -> None:
        """
        Basic constructor that creates a property tab attribute that will create a tab
        of the specified type.
        """
        ...

    @overload
    def equals(self, other: typing.Any) -> bool:
        ...

    @overload
    def equals(self, other: System.ComponentModel.PropertyTabAttribute) -> bool:
        ...

    def get_hash_code(self) -> int:
        """Returns the hashcode for this object."""
        ...

    @overload
    def initialize_arrays(self, tab_class_names: typing.List[str], tab_scopes: typing.List[System.ComponentModel.PropertyTabScope]) -> None:
        """
        Utiliity function to set the types of tab classes this PropertyTabAttribute specifies.
        
        This method is protected.
        """
        ...

    @overload
    def initialize_arrays(self, tab_classes: typing.List[typing.Type], tab_scopes: typing.List[System.ComponentModel.PropertyTabScope]) -> None:
        """
        Utiliity function to set the types of tab classes this PropertyTabAttribute specifies.
        
        This method is protected.
        """
        ...


class _EventContainer(typing.Generic[System_ComponentModel__EventContainer_Callable, System_ComponentModel__EventContainer_ReturnType]):
    """This class is used to provide accurate autocomplete on events and cannot be imported."""

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> System_ComponentModel__EventContainer_ReturnType:
        """Fires the event."""
        ...

    def __iadd__(self, item: System_ComponentModel__EventContainer_Callable) -> typing.Self:
        """Registers an event handler."""
        ...

    def __isub__(self, item: System_ComponentModel__EventContainer_Callable) -> typing.Self:
        """Unregisters an event handler."""
        ...


