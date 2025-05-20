from typing import overload
from enum import Enum
import abc
import typing

import System
import System.Collections
import System.ComponentModel
import System.ComponentModel.Design
import System.ComponentModel.Design.Serialization
import System.IO
import System.Reflection

IServiceProvider = typing.Any
System_ComponentModel_Design_Serialization_MemberRelationship = typing.Any

System_ComponentModel_Design_Serialization__EventContainer_Callable = typing.TypeVar("System_ComponentModel_Design_Serialization__EventContainer_Callable")
System_ComponentModel_Design_Serialization__EventContainer_ReturnType = typing.TypeVar("System_ComponentModel_Design_Serialization__EventContainer_ReturnType")


class ContextStack(System.Object):
    """
    A context stack is an object that can be used by serializers
    to push various context objects. Serialization is often
    a deeply nested operation, involving many different
    serialization classes. These classes often need additional
    context information when performing serialization. As
    an example, an object with a property named "Enabled" may have
    a data type of System.Boolean. If a serializer is writing
    this value to a data stream it may want to know what property
    it is writing. It won't have this information, however, because
    it is only instructed to write the boolean value. In this
    case the parent serializer may push a PropertyDescriptor
    pointing to the "Enabled" property on the context stack.
    What objects get pushed on this stack are up to the
    individual serializer objects.
    """

    @property
    def current(self) -> System.Object:
        """
        Retrieves the current object on the stack, or null
        if no objects have been pushed.
        """
        ...

    @overload
    def __getitem__(self, level: int) -> typing.Any:
        """
        Retrieves the object on the stack at the given
        level, or null if no object exists at that level.
        """
        ...

    @overload
    def __getitem__(self, type: typing.Type) -> typing.Any:
        """
        Retrieves the first object on the stack that
        inherits from or implements the given type, or
        null if no object on the stack implements the type.
        """
        ...

    def append(self, context: typing.Any) -> None:
        """
        Appends an object to the end of the stack, rather than pushing it
        onto the top of the stack. This method allows a serializer to communicate
        with other serializers by adding contextual data that does not have to
        be popped in order. There is no way to remove an object that was
        appended to the end of the stack without popping all other objects.
        """
        ...

    def pop(self) -> System.Object:
        """
        Pops the current object off of the stack, returning
        its value.
        """
        ...

    def push(self, context: typing.Any) -> None:
        """Pushes the given object onto the stack."""
        ...


class IDesignerSerializationProvider(metaclass=abc.ABCMeta):
    """
    This interface defines a custom serialization provider. This
    allows outside objects to control serialization by providing
    their own serializer objects.
    """

    def get_serializer(self, manager: System.ComponentModel.Design.Serialization.IDesignerSerializationManager, current_serializer: typing.Any, object_type: typing.Type, serializer_type: typing.Type) -> System.Object:
        """
        This will be called by the serialization manager when it
        is trying to locate a serializer for an object type.
        If this serialization provider can provide a serializer
        that is of the correct type, it should return it.
        Otherwise, it should return null.
        
        In order to break order dependencies between multiple
        serialization providers the serialization manager will
        loop through all serialization providers until the
        serializer returned reaches steady state. Because
        of this you should always check current_serializer
        before returning a new serializer. If current_serializer
        is an instance of your serializer, then you should
        either return it or return null to prevent an infinite
        loop.
        """
        ...


class ResolveNameEventArgs(System.EventArgs):
    """
    EventArgs for the ResolveNameEventHandler. This event is used
    by the serialization process to match a name to an object
    instance.
    """

    @property
    def name(self) -> str:
        """The name of the object that needs to be resolved."""
        ...

    @property
    def value(self) -> System.Object:
        """The object that matches the name."""
        ...

    @value.setter
    def value(self, value: System.Object) -> None:
        ...

    def __init__(self, name: str) -> None:
        """Creates a new resolve name event args object."""
        ...


class IDesignerSerializationManager(IServiceProvider, metaclass=abc.ABCMeta):
    """
    This interface is passed to a designer serializer to provide
    assistance in the serialization process.
    """

    @property
    @abc.abstractmethod
    def context(self) -> System.ComponentModel.Design.Serialization.ContextStack:
        """
        The Context property provides a user-defined storage area
        implemented as a stack. This storage area is a useful way
        to provide communication across serializers, as serialization
        is a generally hierarchical process.
        """
        ...

    @property
    @abc.abstractmethod
    def properties(self) -> System.ComponentModel.PropertyDescriptorCollection:
        """
        The Properties property provides a set of custom properties
        the serialization manager may surface. The set of properties
        exposed here is defined by the implementor of
        IDesignerSerializationManager.
        """
        ...

    @property
    @abc.abstractmethod
    def resolve_name(self) -> _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.Serialization.ResolveNameEventArgs], None], None]:
        """
        ResolveName event. This event
        is raised when GetName is called, but the name is not found
        in the serialization manager's name table. It provides a
        way for a serializer to demand-create an object so the serializer
        does not have to order object creation by dependency. This
        delegate is cleared immediately after serialization or deserialization
        is complete.
        """
        ...

    @resolve_name.setter
    def resolve_name(self, value: _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.Serialization.ResolveNameEventArgs], None], None]) -> None:
        ...

    @property
    @abc.abstractmethod
    def serialization_complete(self) -> _EventContainer[typing.Callable[[System.Object, System.EventArgs], None], None]:
        """
        This event is raised when serialization or deserialization
        has been completed. Generally, serialization code should
        be written to be stateless. Should some sort of state
        be necessary to maintain, a serializer can listen to
        this event to know when that state should be cleared.
        An example of this is if a serializer needs to write
        to another file, such as a resource file. In this case
        it would be inefficient to design the serializer
        to close the file when finished because serialization of
        an object graph generally requires several serializers.
        The resource file would be opened and closed many times.
        Instead, the resource file could be accessed through
        an object that listened to the SerializationComplete
        event, and that object could close the resource file
        at the end of serialization.
        """
        ...

    @serialization_complete.setter
    def serialization_complete(self, value: _EventContainer[typing.Callable[[System.Object, System.EventArgs], None], None]) -> None:
        ...

    def add_serialization_provider(self, provider: System.ComponentModel.Design.Serialization.IDesignerSerializationProvider) -> None:
        """
        This method adds a custom serialization provider to the
        serialization manager. A custom serialization provider will
        get the opportunity to return a serializer for a data type
        before the serialization manager looks in the type's
        metadata.
        """
        ...

    def create_instance(self, type: typing.Type, arguments: System.Collections.ICollection, name: str, add_to_container: bool) -> System.Object:
        """
        Creates an instance of the given type and adds it to a collection
        of named instances. Objects that implement IComponent will be
        added to the design time container if add_to_container is true.
        """
        ...

    def get_instance(self, name: str) -> System.Object:
        """
        Retrieves an instance of a created object of the given name, or
        null if that object does not exist.
        """
        ...

    def get_name(self, value: typing.Any) -> str:
        """
        Retrieves a name for the specified object, or null if the object
        has no name.
        """
        ...

    def get_serializer(self, object_type: typing.Type, serializer_type: typing.Type) -> System.Object:
        """
        Retrieves a serializer of the requested type for the given
        object type.
        """
        ...

    def get_type(self, type_name: str) -> typing.Type:
        """Retrieves a type of the given name."""
        ...

    def remove_serialization_provider(self, provider: System.ComponentModel.Design.Serialization.IDesignerSerializationProvider) -> None:
        """Removes a previously added serialization provider."""
        ...

    def report_error(self, error_information: typing.Any) -> None:
        """
        Reports a non-fatal error in serialization. The serialization
        manager may implement a logging scheme to alert the caller
        to all non-fatal errors at once. If it doesn't, it should
        immediately throw in this method, which should abort
        serialization.
        Serialization may continue after calling this function.
        """
        ...

    def set_name(self, instance: typing.Any, name: str) -> None:
        """
        Provides a way to set the name of an existing object.
        This is useful when it is necessary to create an
        instance of an object without going through CreateInstance.
        An exception will be thrown if you try to rename an existing
        object or if you try to give a new object a name that
        is already taken.
        """
        ...


class IDesignerSerializationService(metaclass=abc.ABCMeta):
    """
    This service provides a way to exchange a collection of objects
    for a serializable object that represents them. The returned
    object contains live references to objects in the collection.
    This returned object can then be passed to any runtime
    serialization mechanism. The object itself serializes
    components the same way designers write source for them; by picking
    them apart property by property. Many objects do not support
    runtime serialization because their internal state cannot be
    adequately duplicated. All components that support a designer,
    however, must support serialization by walking their public
    properties, methods and events. This interface uses this
    technique to convert a collection of components into a single
    opaque object that does support runtime serialization.
    """

    def deserialize(self, serialization_data: typing.Any) -> System.Collections.ICollection:
        """
        Deserializes the provided serialization data object and
        returns a collection of objects contained within that data.
        """
        ...

    def serialize(self, objects: System.Collections.ICollection) -> System.Object:
        """
        Serializes the given collection of objects and
        stores them in an opaque serialization data object.
        The returning object fully supports runtime serialization.
        """
        ...


class MemberRelationship(System.IEquatable[System_ComponentModel_Design_Serialization_MemberRelationship]):
    """This class represents a single relationship between an object and a member."""

    EMPTY: System.ComponentModel.Design.Serialization.MemberRelationship

    @property
    def is_empty(self) -> bool:
        """Returns true if this relationship is empty."""
        ...

    @property
    def member(self) -> System.ComponentModel.MemberDescriptor:
        """The member in this relationship."""
        ...

    @property
    def owner(self) -> System.Object:
        """The object owning the member."""
        ...

    def __eq__(self, right: System.ComponentModel.Design.Serialization.MemberRelationship) -> bool:
        """Infrastructure support to make this a first class struct"""
        ...

    def __init__(self, owner: typing.Any, member: System.ComponentModel.MemberDescriptor) -> None:
        """Creates a new member relationship."""
        ...

    def __ne__(self, right: System.ComponentModel.Design.Serialization.MemberRelationship) -> bool:
        """Infrastructure support to make this a first class struct"""
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        """Infrastructure support to make this a first class struct"""
        ...

    @overload
    def equals(self, other: System.ComponentModel.Design.Serialization.MemberRelationship) -> bool:
        """Infrastructure support to make this a first class struct"""
        ...

    def get_hash_code(self) -> int:
        """Infrastructure support to make this a first class struct"""
        ...


class MemberRelationshipService(System.Object, metaclass=abc.ABCMeta):
    """
    A member relationship service is used by a serializer to announce that one
    property is related to a property on another object. Consider a code
    based serialization scheme where code is of the following form:
    
    object1.Property1 = object2.Property2
    
    Upon interpretation of this code, Property1 on object1 will be
    set to the return value of object2.Property2. But the relationship
    between these two objects is lost. Serialization schemes that
    wish to maintain this relationship may install a MemberRelationshipService
    into the serialization manager. When an object is deserialized
    this service will be notified of these relationships. It is up to the service
    to act on these notifications if it wishes. During serialization, the
    service is also consulted. If a relationship exists the same
    relationship is maintained by the serializer.
    """

    @overload
    def __getitem__(self, source_owner: typing.Any, source_member: System.ComponentModel.MemberDescriptor) -> System.ComponentModel.Design.Serialization.MemberRelationship:
        """
        Returns the current relationship associated with the source, or null if there is no relationship.
        Also sets a relationship between two objects. Null can be passed as the property value, in which
        case the relationship will be cleared.
        """
        ...

    @overload
    def __getitem__(self, source: System.ComponentModel.Design.Serialization.MemberRelationship) -> System.ComponentModel.Design.Serialization.MemberRelationship:
        """
        Returns the current relationship associated with the source, or MemberRelationship.Empty if
        there is no relationship. Also sets a relationship between two objects. Empty
        can also be passed as the property value, in which case the relationship will
        be cleared.
        """
        ...

    @overload
    def __setitem__(self, source_owner: typing.Any, source_member: System.ComponentModel.MemberDescriptor, value: System.ComponentModel.Design.Serialization.MemberRelationship) -> None:
        """
        Returns the current relationship associated with the source, or null if there is no relationship.
        Also sets a relationship between two objects. Null can be passed as the property value, in which
        case the relationship will be cleared.
        """
        ...

    @overload
    def __setitem__(self, source: System.ComponentModel.Design.Serialization.MemberRelationship, value: System.ComponentModel.Design.Serialization.MemberRelationship) -> None:
        """
        Returns the current relationship associated with the source, or MemberRelationship.Empty if
        there is no relationship. Also sets a relationship between two objects. Empty
        can also be passed as the property value, in which case the relationship will
        be cleared.
        """
        ...

    def get_relationship(self, source: System.ComponentModel.Design.Serialization.MemberRelationship) -> System.ComponentModel.Design.Serialization.MemberRelationship:
        """
        This is the implementation API for returning relationships. The default implementation stores the
        relationship in a table. Relationships are stored weakly, so they do not keep an object alive.
        
        This method is protected.
        """
        ...

    def set_relationship(self, source: System.ComponentModel.Design.Serialization.MemberRelationship, relationship: System.ComponentModel.Design.Serialization.MemberRelationship) -> None:
        """
        This is the implementation API for returning relationships. The default implementation stores the
        relationship in a table. Relationships are stored weakly, so they do not keep an object alive. Empty can be
        passed in for relationship to remove the relationship.
        
        This method is protected.
        """
        ...

    def supports_relationship(self, source: System.ComponentModel.Design.Serialization.MemberRelationship, relationship: System.ComponentModel.Design.Serialization.MemberRelationship) -> bool:
        """Returns true if the provided relationship is supported."""
        ...


class DefaultSerializationProviderAttribute(System.Attribute):
    """
    The default serialization provider attribute is placed on a serializer
    to indicate the class to use as a default provider of that type of
    serializer. To be a default serialization provider, a class must
    implement IDesignerSerilaizationProvider and have an empty
    constructor. The class itself can be internal to the assembly.
    """

    @property
    def provider_type_name(self) -> str:
        """Returns the type name for the default serialization provider."""
        ...

    @overload
    def __init__(self, provider_type: typing.Type) -> None:
        """Creates a new DefaultSerializationProviderAttribute"""
        ...

    @overload
    def __init__(self, provider_type_name: str) -> None:
        """Creates a new DefaultSerializationProviderAttribute"""
        ...


class InstanceDescriptor(System.Object):
    """
    EventArgs for the ResolveNameEventHandler. This event is used
    by the serialization process to match a name to an object
    instance.
    """

    @property
    def arguments(self) -> System.Collections.ICollection:
        """
        The collection of arguments that should be passed to
        MemberInfo in order to create an instance.
        """
        ...

    @property
    def is_complete(self) -> bool:
        """
        Determines if the contents of this instance descriptor completely identify the instance.
        This will normally be the case, but some objects may be too complex for a single method
        or constructor to represent. IsComplete can be used to identify these objects and take
        additional steps to further describe their state.
        """
        ...

    @property
    def member_info(self) -> System.Reflection.MemberInfo:
        """
        The MemberInfo object that was passed into the constructor
        of this InstanceDescriptor.
        """
        ...

    @overload
    def __init__(self, member: System.Reflection.MemberInfo, arguments: System.Collections.ICollection) -> None:
        """Creates a new InstanceDescriptor."""
        ...

    @overload
    def __init__(self, member: System.Reflection.MemberInfo, arguments: System.Collections.ICollection, is_complete: bool) -> None:
        """Creates a new InstanceDescriptor."""
        ...

    def invoke(self) -> System.Object:
        """
        Invokes this instance descriptor, returning the object
        the descriptor describes.
        """
        ...


class IDesignerLoaderHost(System.ComponentModel.Design.IDesignerHost, metaclass=abc.ABCMeta):
    """
    IDesignerLoaderHost. This is an extension of IDesignerHost that is passed
    to the designer loader in the BeginLoad method. It is isolated from
    IDesignerHost to emphasize that all loading and reloading of the design
    document actually should be initiated by the designer loader, and not by
    the designer host. However, the loader must inform the designer host that
    it wishes to invoke a load or reload.
    """

    def end_load(self, base_class_name: str, successful: bool, error_collection: System.Collections.ICollection) -> None:
        """
        This is called by the designer loader to indicate that the load has
        terminated. If there were errors, they should be passed in the error_collection
        as a collection of exceptions (if they are not exceptions the designer
        loader host may just call ToString on them). If the load was successful then
        error_collection should either be null or contain an empty collection.
        """
        ...

    def reload(self) -> None:
        """
        This is called by the designer loader when it wishes to reload the
        design document. The reload will happen immediately so the caller
        should ensure that it is in a state where BeginLoad may be called again.
        """
        ...


class IDesignerLoaderHost2(System.ComponentModel.Design.Serialization.IDesignerLoaderHost, metaclass=abc.ABCMeta):
    """
    IgnoreErrorsDuringReload - specifies whether errors should be ignored when Reload() is called.
                      We only allow to set to true if we CanReloadWithErrors. If we cannot
                      we simply ignore rather than throwing an exception. We probably should,
                      but we are avoiding localization.
    CanReloadWithErrors - specifies whether it is possible to reload with errors. There are certain
                 scenarios where errors cannot be ignored.
    """

    @property
    @abc.abstractmethod
    def ignore_errors_during_reload(self) -> bool:
        ...

    @ignore_errors_during_reload.setter
    def ignore_errors_during_reload(self, value: bool) -> None:
        ...

    @property
    @abc.abstractmethod
    def can_reload_with_errors(self) -> bool:
        ...

    @can_reload_with_errors.setter
    def can_reload_with_errors(self, value: bool) -> None:
        ...


class SerializationStore(System.Object, System.IDisposable, metaclass=abc.ABCMeta):
    """
    The SerializationStore class is an implementation-specific class that stores
    serialization data for the component serialization service. The
    service adds state to this serialization store. Once the store is
    closed it can be saved to a stream. A serialization store can be
    deserialized at a later date by the same type of serialization service.
    SerializationStore implements the IDisposable interface such that Dispose
    simply calls the Close method. Dispose is implemented as a private
    interface to avoid confusion. The IDisposable pattern is provided
    for languages that support a "using" syntax like C# and VB .NET.
    """

    @property
    @abc.abstractmethod
    def errors(self) -> System.Collections.ICollection:
        """
        If there were errors generated during serialization or deserialization of the store, they will be
        added to this collection.
        """
        ...

    def close(self) -> None:
        """
        The Close method closes this store and prevents any objects
        from being serialized into it. Once closed, the serialization store may be saved.
        """
        ...

    def dispose(self, disposing: bool) -> None:
        """This method is protected."""
        ...

    def save(self, stream: System.IO.Stream) -> None:
        """
        The Save method saves the store to the given stream. If the store
        is open, Save will automatically close it for you. You
        can call save as many times as you wish to save the store
        to different streams.
        """
        ...


class DesignerLoader(System.Object, metaclass=abc.ABCMeta):
    """
    DesignerLoader. This class is responsible for loading a designer document.
    Where and how this load occurs is a private matter for the designer loader.
    The designer loader will be handed to an IDesignerHost instance. This instance,
    when it is ready to load the document, will call BeginLoad, passing an instance
    of IDesignerLoaderHost. The designer loader will load up the design surface
    using the host interface, and call EndLoad on the interface when it is done.
    The error collection passed into EndLoad should be empty or null to indicate a
    successful load, or it should contain a collection of exceptions that
    describe the error.
    
    Once a document is loaded, the designer loader is also responsible for
    writing any changes made to the document back whatever storage the
    loader used when loading the document.
    """

    @property
    def loading(self) -> bool:
        """
        Returns true when the designer is in the process of loading. Clients that are
        sinking notifications from the designer often want to ignore them while the designer is loading
        and only respond to them if they result from user interactions.
        """
        ...

    def begin_load(self, host: System.ComponentModel.Design.Serialization.IDesignerLoaderHost) -> None:
        """
        Called by the designer host to begin the loading process. The designer
        host passes in an instance of a designer loader host (which is typically
        the same object as the designer host. This loader host allows
        the designer loader to reload the design document and also allows
        the designer loader to indicate that it has finished loading the
        design document.
        """
        ...

    def dispose(self) -> None:
        """
        Disposes this designer loader. The designer host will call this method
        when the design document itself is being destroyed. Once called, the
        designer loader will never be called again.
        """
        ...

    def flush(self) -> None:
        """
        The designer host will call this periodically when it wants to
        ensure that any changes that have been made to the document
        have been saved by the designer loader. This method allows
        designer loaders to implement a lazy-write scheme to improve
        performance. The default implementation does nothing.
        """
        ...


class ComponentSerializationService(System.Object, metaclass=abc.ABCMeta):
    """
    This class serializes a set of components or serializable objects into a
    serialization store. The store can then be deserialized at a later
    date. ComponentSerializationService differs from other serialization
    schemes in that the serialization format is opaque, and it allows for
    partial serialization of objects. For example, you can choose to
    serialize only selected properties for an object.
    
    This class is abstract. Typically a DesignerLoader will provide a
    concrete implementation of this class and add it as a service to
    its DesignSurface. This allows objects to be serialized in the
    format best suited for them.
    """

    def create_store(self) -> System.ComponentModel.Design.Serialization.SerializationStore:
        """
        This method creates a new SerializationStore. The serialization store can
        be passed to any of the various Serialize methods to build up serialization
        state for a group of objects.
        """
        ...

    @overload
    def deserialize(self, store: System.ComponentModel.Design.Serialization.SerializationStore) -> System.Collections.ICollection:
        """
        This method deserializes the given store to produce a collection of
        objects contained within it. If a container is provided, objects
        that are created that implement IComponent will be added to the container.
        """
        ...

    @overload
    def deserialize(self, store: System.ComponentModel.Design.Serialization.SerializationStore, container: System.ComponentModel.IContainer) -> System.Collections.ICollection:
        """
        This method deserializes the given store to produce a collection of
        objects contained within it. If a container is provided, objects
        that are created that implement IComponent will be added to the container.
        """
        ...

    @overload
    def deserialize_to(self, store: System.ComponentModel.Design.Serialization.SerializationStore, container: System.ComponentModel.IContainer, validate_recycled_types: bool, apply_defaults: bool) -> None:
        """
        This method deserializes the given store, but rather than produce
        new objects, the data in the store is applied to an existing
        set of objects that are taken from the provided container. This
        allows the caller to pre-create an object however it sees fit. If
        an object has deserialization state and the object is not named in
        the set of existing objects, a new object will be created. If that
        object also implements IComponent, it will be added to the given
        container. Objects in the container must have names that
        match objects in the serialization store in order for an existing
        object to be used. If validate_recycled_types is true it is guaranteed
        that the deserialization will only work if applied to an object of the
        same type.
        """
        ...

    @overload
    def deserialize_to(self, store: System.ComponentModel.Design.Serialization.SerializationStore, container: System.ComponentModel.IContainer) -> None:
        ...

    @overload
    def deserialize_to(self, store: System.ComponentModel.Design.Serialization.SerializationStore, container: System.ComponentModel.IContainer, validate_recycled_types: bool) -> None:
        ...

    def load_store(self, stream: System.IO.Stream) -> System.ComponentModel.Design.Serialization.SerializationStore:
        """
        This method loads a SerializationStore and from the given
        stream. This store can then be used to deserialize objects by passing it to
        the various Deserialize methods.
        """
        ...

    def serialize(self, store: System.ComponentModel.Design.Serialization.SerializationStore, value: typing.Any) -> None:
        """
        This method serializes the given object to the store. The store
        can be used to serialize more than one object by calling this method
        more than once.
        """
        ...

    def serialize_absolute(self, store: System.ComponentModel.Design.Serialization.SerializationStore, value: typing.Any) -> None:
        """
        Normal serialization only serializes values that differ from the component's default state.
        This provides the most compact serialization mechanism but assumes that during deserialization
        a new, freshly created object will be used. If an existing object is used properties that
        contained default values during serialization would not be reset back to their defaults.
        The SerializeAbsolute method does not require this assumption on the deserializing end.
        Instead, it saves data in the serialization store about default values as well so that
        deserialization can reset non-default properties back to their default values. This is
        especially true for collection objects, where the collections are either cleared and
        items re-added, or individual items are removed and added.
        """
        ...

    def serialize_member(self, store: System.ComponentModel.Design.Serialization.SerializationStore, owning_object: typing.Any, member: System.ComponentModel.MemberDescriptor) -> None:
        """
        This method serializes the given member on the given object. This method
        can be invoked multiple times for the same object to build up a list of
        serialized members within the serialization store. The member generally
        has to be a property or an event.
        """
        ...

    def serialize_member_absolute(self, store: System.ComponentModel.Design.Serialization.SerializationStore, owning_object: typing.Any, member: System.ComponentModel.MemberDescriptor) -> None:
        """
        This method serializes the given member on the given object,
        but also serializes the member if it contains the default value.
        Note that for some members, containing the default value and setting
        the same value back to the member are different concepts. For example,
        if a property inherits its value from a parent object if no local value
        is set, setting the value back to the property can may not be what is desired.
        SerializeMemberAbsolute takes this into account and would clear the state of
        the property in this case.
        """
        ...


class IDesignerLoaderService(metaclass=abc.ABCMeta):
    """
    This interface may be optionally implemented by the designer loader to provide
    load services to outside components. It provides support for asynchronous loading
    of the designer and allows other objects to initiate a reload of othe
    design surface. Designer loaders do not need to implement this but it is
    recommended. We do not directly put this on DesignerLoader so we can prevent
    outside objects from interacting with the main methods of a designer loader.
    These should only be called by the designer host.
    """

    def add_load_dependency(self) -> None:
        """
        Adds a load dependency to this loader. This indicates that some other
        object is also participating in the load, and that the designer loader
        should not call EndLoad on the loader host until all load dependencies
        have called DependentLoadComplete on the designer loader.
        """
        ...

    def dependent_load_complete(self, successful: bool, error_collection: System.Collections.ICollection) -> None:
        """
        This is called by any object that has previously called
        AddLoadDependency to signal that the dependent load has completed.
        The caller should pass either an empty collection or null to indicate
        a successful load, or a collection of exceptions that indicate the
        reason(s) for failure.
        """
        ...

    def reload(self) -> bool:
        """
        This can be called by an outside object to request that the loader
        reload the design document. If it supports reloading and wants to
        comply with the reload, the designer loader should return true. Otherwise
        it should return false, indicating that the reload will not occur.
        Callers should not rely on the reload happening immediately; the
        designer loader may schedule this for some other time, or it may
        try to reload at once.
        """
        ...


class INameCreationService(metaclass=abc.ABCMeta):
    """
    This service may be provided by a designer loader to provide
    a way for the designer to fabricate new names for objects.
    If this service isn't available the designer will choose a
    default implementation.
    """

    def create_name(self, container: System.ComponentModel.IContainer, data_type: typing.Type) -> str:
        """
        Creates a new name that is unique to all the components
        in the given container. The name will be used to create
        an object of the given data type, so the service may
        derive a name from the data type's name. The container
        parameter can be null if no container search is needed.
        """
        ...

    def is_valid_name(self, name: str) -> bool:
        """
        Determines if the given name is valid. A name
        creation service may have rules defining a valid
        name, and this method allows the service to enforce
        those rules.
        """
        ...

    def validate_name(self, name: str) -> None:
        """
        Determines if the given name is valid. A name
        creation service may have rules defining a valid
        name, and this method allows the service to enforce
        those rules. It is similar to IsValidName, except
        that this method will throw an exception if the
        name is invalid. This allows implementors to provide
        rich information in the exception message.
        """
        ...


class RootDesignerSerializerAttribute(System.Attribute):
    """
    This attribute can be placed on a class to indicate what serialization
    object should be used to serialize the class at design time if it is
    being used as a root object.
    
    RootDesignerSerializerAttribute has been deprecated. Use DesignerSerializerAttribute instead. For example, to specify a root designer for CodeDom, use DesignerSerializerAttribute(...,typeof(TypeCodeDomSerializer)) instead.
    """

    @property
    def reloadable(self) -> bool:
        """
        Indicates that this root serializer supports reloading. If false, the design document
        will not automatically perform a reload on behalf of the user. It will be the user's
        responsibility to reload the document themselves.
        """
        ...

    @property
    def serializer_type_name(self) -> str:
        """Retrieves the fully qualified type name of the serializer."""
        ...

    @property
    def serializer_base_type_name(self) -> str:
        """Retrieves the fully qualified type name of the serializer base type."""
        ...

    @property
    def type_id(self) -> System.Object:
        """
        This defines a unique ID for this attribute type. It is used
        by filtering algorithms to identify two attributes that are
        the same type. For most attributes, this just returns the
        Type instance for the attribute. EditorAttribute overrides
        this to include the type of the editor base type.
        """
        ...

    @overload
    def __init__(self, serializer_type: typing.Type, base_serializer_type: typing.Type, reloadable: bool) -> None:
        """Creates a new designer serialization attribute."""
        ...

    @overload
    def __init__(self, serializer_type_name: str, base_serializer_type: typing.Type, reloadable: bool) -> None:
        """Creates a new designer serialization attribute."""
        ...

    @overload
    def __init__(self, serializer_type_name: str, base_serializer_type_name: str, reloadable: bool) -> None:
        """Creates a new designer serialization attribute."""
        ...


class _EventContainer(typing.Generic[System_ComponentModel_Design_Serialization__EventContainer_Callable, System_ComponentModel_Design_Serialization__EventContainer_ReturnType]):
    """This class is used to provide accurate autocomplete on events and cannot be imported."""

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> System_ComponentModel_Design_Serialization__EventContainer_ReturnType:
        """Fires the event."""
        ...

    def __iadd__(self, item: System_ComponentModel_Design_Serialization__EventContainer_Callable) -> typing.Self:
        """Registers an event handler."""
        ...

    def __isub__(self, item: System_ComponentModel_Design_Serialization__EventContainer_Callable) -> typing.Self:
        """Unregisters an event handler."""
        ...


