from typing import overload
from enum import Enum
import abc
import typing

import System
import System.Collections
import System.ComponentModel
import System.ComponentModel.Design
import System.Globalization
import System.IO
import System.Reflection
import System.Resources
import System.Runtime.InteropServices
import System.Runtime.Serialization

IServiceProvider = typing.Any

System_ComponentModel_Design__EventContainer_Callable = typing.TypeVar("System_ComponentModel_Design__EventContainer_Callable")
System_ComponentModel_Design__EventContainer_ReturnType = typing.TypeVar("System_ComponentModel_Design__EventContainer_ReturnType")


class TypeDescriptionProviderService(System.Object, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @overload
    def get_provider(self, instance: typing.Any) -> System.ComponentModel.TypeDescriptionProvider:
        ...

    @overload
    def get_provider(self, type: typing.Type) -> System.ComponentModel.TypeDescriptionProvider:
        ...


class HelpKeywordType(Enum):
    """Specifies identifiers that can be used to indicate the type of a help keyword."""

    F_1_KEYWORD = 0
    """Indicates the keyword is a word F1 was pressed to request help regarding."""

    GENERAL_KEYWORD = 1
    """Indicates the keyword is a general keyword."""

    FILTER_KEYWORD = 2
    """Indicates the keyword is a filter keyword."""


class HelpContextType(Enum):
    """This class has no documentation."""

    AMBIENT = 0

    WINDOW = 1

    SELECTION = 2

    TOOL_WINDOW_SELECTION = 3


class IHelpService(metaclass=abc.ABCMeta):
    """
    Provides the Integrated Development Environment (IDE) help
    system with contextual information for the current task.
    """

    def add_context_attribute(self, name: str, value: str, keyword_type: System.ComponentModel.Design.HelpKeywordType) -> None:
        """Adds a context attribute to the document."""
        ...

    def clear_context_attributes(self) -> None:
        """Clears all existing context attributes from the document."""
        ...

    def create_local_context(self, context_type: System.ComponentModel.Design.HelpContextType) -> System.ComponentModel.Design.IHelpService:
        """Creates a Local IHelpService to manage subcontexts."""
        ...

    def remove_context_attribute(self, name: str, value: str) -> None:
        """Removes a previously added context attribute."""
        ...

    def remove_local_context(self, local_context: System.ComponentModel.Design.IHelpService) -> None:
        """Removes a context that was created with CreateLocalContext"""
        ...

    def show_help_from_keyword(self, help_keyword: str) -> None:
        """Shows the help topic that corresponds to the specified keyword."""
        ...

    def show_help_from_url(self, help_url: str) -> None:
        """Shows the help topic that corresponds with the specified Url and topic navigation ID."""
        ...


class CommandID(System.Object):
    """
    Represents a numeric Command ID and globally unique ID (GUID) menu
    identifier that together uniquely identify a command.
    """

    @property
    def id(self) -> int:
        """Gets or sets the numeric command ID."""
        ...

    @property
    def guid(self) -> System.Guid:
        """
        Gets or sets the globally unique ID (GUID) of the menu group that the
        menu command this CommandID represents belongs to.
        """
        ...

    def __init__(self, menu_group: System.Guid, command_id: int) -> None:
        """
        Initializes a new instance of the System.ComponentModel.Design.CommandID
        class. Creates a new command ID.
        """
        ...

    def equals(self, obj: typing.Any) -> bool:
        """Overrides Object's Equals method."""
        ...

    def get_hash_code(self) -> int:
        ...

    def to_string(self) -> str:
        """Overrides Object's ToString method."""
        ...


class MenuCommand(System.Object):
    """Represents a Windows menu or toolbar item."""

    @property
    def checked(self) -> bool:
        """Gets or sets a value indicating whether this menu item is checked."""
        ...

    @checked.setter
    def checked(self, value: bool) -> None:
        ...

    @property
    def enabled(self) -> bool:
        """Gets or sets a value indicating whether this menu item is available."""
        ...

    @enabled.setter
    def enabled(self, value: bool) -> None:
        ...

    @property
    def properties(self) -> System.Collections.IDictionary:
        ...

    @property
    def supported(self) -> bool:
        """Gets or sets a value indicating whether this menu item is supported."""
        ...

    @supported.setter
    def supported(self, value: bool) -> None:
        ...

    @property
    def visible(self) -> bool:
        """Gets or sets a value indicating if this menu item is visible."""
        ...

    @visible.setter
    def visible(self, value: bool) -> None:
        ...

    @property
    def command_changed(self) -> _EventContainer[typing.Callable[[System.Object, System.EventArgs], None], None]:
        """Occurs when the menu command changes."""
        ...

    @command_changed.setter
    def command_changed(self, value: _EventContainer[typing.Callable[[System.Object, System.EventArgs], None], None]) -> None:
        ...

    @property
    def command_id(self) -> System.ComponentModel.Design.CommandID:
        """Gets the System.ComponentModel.Design.CommandID associated with this menu command."""
        ...

    @property
    def ole_status(self) -> int:
        """Gets the OLE command status code for this menu item."""
        ...

    def __init__(self, handler: typing.Callable[[System.Object, System.EventArgs], None], command: System.ComponentModel.Design.CommandID) -> None:
        """Initializes a new instance of System.ComponentModel.Design.MenuCommand."""
        ...

    @overload
    def invoke(self, arg: typing.Any) -> None:
        """
        Invokes a menu item. The default implementation of this method ignores
        the argument, but deriving classes may override this method.
        """
        ...

    @overload
    def invoke(self) -> None:
        """Invokes a menu item."""
        ...

    def on_command_changed(self, e: System.EventArgs) -> None:
        """
        Provides notification and is called in response to
        a System.ComponentModel.Design.MenuCommand.CommandChanged event.
        
        This method is protected.
        """
        ...

    def to_string(self) -> str:
        """Overrides object's ToString()."""
        ...


class DesignerVerb(System.ComponentModel.Design.MenuCommand):
    """Represents a verb that can be executed by a component's designer."""

    @property
    def description(self) -> str:
        """Gets or sets the description of the menu item for the verb."""
        ...

    @description.setter
    def description(self, value: str) -> None:
        ...

    @property
    def text(self) -> str:
        """Gets or sets the text to show on the menu item for the verb."""
        ...

    @overload
    def __init__(self, text: str, handler: typing.Callable[[System.Object, System.EventArgs], None]) -> None:
        """Initializes a new instance of the System.ComponentModel.Design.DesignerVerb class."""
        ...

    @overload
    def __init__(self, text: str, handler: typing.Callable[[System.Object, System.EventArgs], None], start_command_id: System.ComponentModel.Design.CommandID) -> None:
        """
        Initializes a new instance of the System.ComponentModel.Design.DesignerVerb
        class.
        """
        ...

    def to_string(self) -> str:
        """Overrides object's ToString()."""
        ...


class DesignerVerbCollection(System.Collections.CollectionBase):
    """This class has no documentation."""

    def __getitem__(self, index: int) -> System.ComponentModel.Design.DesignerVerb:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, value: typing.List[System.ComponentModel.Design.DesignerVerb]) -> None:
        ...

    def __setitem__(self, index: int, value: System.ComponentModel.Design.DesignerVerb) -> None:
        ...

    def add(self, value: System.ComponentModel.Design.DesignerVerb) -> int:
        ...

    @overload
    def add_range(self, value: typing.List[System.ComponentModel.Design.DesignerVerb]) -> None:
        ...

    @overload
    def add_range(self, value: System.ComponentModel.Design.DesignerVerbCollection) -> None:
        ...

    def contains(self, value: System.ComponentModel.Design.DesignerVerb) -> bool:
        ...

    def copy_to(self, array: typing.List[System.ComponentModel.Design.DesignerVerb], index: int) -> None:
        ...

    def index_of(self, value: System.ComponentModel.Design.DesignerVerb) -> int:
        ...

    def insert(self, index: int, value: System.ComponentModel.Design.DesignerVerb) -> None:
        ...

    def on_validate(self, value: typing.Any) -> None:
        """This method is protected."""
        ...

    def remove(self, value: System.ComponentModel.Design.DesignerVerb) -> None:
        ...


class IDesigner(System.IDisposable, metaclass=abc.ABCMeta):
    """
    Provides the basic framework for building a custom designer.
    This interface stores the verbs available to the designer, as well as basic
    services for the designer.
    """

    @property
    @abc.abstractmethod
    def component(self) -> System.ComponentModel.IComponent:
        """Gets or sets the base component this designer is designing."""
        ...

    @property
    @abc.abstractmethod
    def verbs(self) -> System.ComponentModel.Design.DesignerVerbCollection:
        """Gets or sets the design-time verbs supported by the designer."""
        ...

    def do_default_action(self) -> None:
        """Performs the default action for this designer."""
        ...

    def initialize(self, component: System.ComponentModel.IComponent) -> None:
        """Initializes the designer with the given component."""
        ...


class DesignerTransactionCloseEventArgs(System.EventArgs):
    """This class has no documentation."""

    @property
    def transaction_committed(self) -> bool:
        ...

    @property
    def last_transaction(self) -> bool:
        ...

    @overload
    def __init__(self, commit: bool, last_transaction: bool) -> None:
        """
        Creates a new event args. Commit is true if the transaction is committed, and
        last_transaction is true if this is the last transaction to close.
        """
        ...

    @overload
    def __init__(self, commit: bool) -> None:
        """
        Creates a new event args. Commit is true if the transaction is committed. This
        defaults the LastTransaction property to true.
        
        This constructor has been deprecated. Use DesignerTransactionCloseEventArgs(bool, bool) instead.
        """
        ...


class IMenuCommandService(metaclass=abc.ABCMeta):
    """
    Provides an interface for a designer to add menu items to the Visual Studio
    7.0 menu.
    """

    @property
    @abc.abstractmethod
    def verbs(self) -> System.ComponentModel.Design.DesignerVerbCollection:
        """
        Gets or sets an array of type System.ComponentModel.Design.DesignerVerb
        that indicates the verbs that are currently available.
        """
        ...

    def add_command(self, command: System.ComponentModel.Design.MenuCommand) -> None:
        """Adds a menu command to the document."""
        ...

    def add_verb(self, verb: System.ComponentModel.Design.DesignerVerb) -> None:
        """Adds a verb to the set of global verbs."""
        ...

    def find_command(self, command_id: System.ComponentModel.Design.CommandID) -> System.ComponentModel.Design.MenuCommand:
        """
        Searches for the given command ID and returns the System.ComponentModel.Design.MenuCommand
        associated with it.
        """
        ...

    def global_invoke(self, command_id: System.ComponentModel.Design.CommandID) -> bool:
        """Invokes a command on the local form or in the global environment."""
        ...

    def remove_command(self, command: System.ComponentModel.Design.MenuCommand) -> None:
        """Removes the specified System.ComponentModel.Design.MenuCommand from the document."""
        ...

    def remove_verb(self, verb: System.ComponentModel.Design.DesignerVerb) -> None:
        """Removes the specified verb from the document."""
        ...

    def show_context_menu(self, menu_id: System.ComponentModel.Design.CommandID, x: int, y: int) -> None:
        """Shows the context menu with the specified command ID at the specified location."""
        ...


class IDictionaryService(metaclass=abc.ABCMeta):
    """
    Provides a generic dictionary service that a designer can use
    to store user-defined data on the site.
    """

    def get_key(self, value: typing.Any) -> System.Object:
        """Gets the key corresponding to the specified value."""
        ...

    def get_value(self, key: typing.Any) -> System.Object:
        """Gets the value corresponding to the specified key."""
        ...

    def set_value(self, key: typing.Any, value: typing.Any) -> None:
        """Sets the specified key-value pair."""
        ...


class IServiceContainer(IServiceProvider, metaclass=abc.ABCMeta):
    """
    This interface provides a container for services. A service container
    is, by definition, a service provider. In addition to providing services
    it also provides a mechanism for adding and removing services.
    """

    @overload
    def add_service(self, service_type: typing.Type, service_instance: typing.Any) -> None:
        """Adds the given service to the service container."""
        ...

    @overload
    def add_service(self, service_type: typing.Type, service_instance: typing.Any, promote: bool) -> None:
        """Adds the given service to the service container."""
        ...

    @overload
    def add_service(self, service_type: typing.Type, callback: typing.Callable[[System.ComponentModel.Design.IServiceContainer, typing.Type], System.Object]) -> None:
        """Adds the given service to the service container."""
        ...

    @overload
    def add_service(self, service_type: typing.Type, callback: typing.Callable[[System.ComponentModel.Design.IServiceContainer, typing.Type], System.Object], promote: bool) -> None:
        """Adds the given service to the service container."""
        ...

    @overload
    def remove_service(self, service_type: typing.Type) -> None:
        """Removes the given service type from the service container."""
        ...

    @overload
    def remove_service(self, service_type: typing.Type, promote: bool) -> None:
        """Removes the given service type from the service container."""
        ...


class DesignerTransaction(System.Object, System.IDisposable, metaclass=abc.ABCMeta):
    """
    Identifies a transaction within a designer. Transactions are
    used to wrap several changes into one unit of work, which
    helps performance.
    """

    @property
    def canceled(self) -> bool:
        ...

    @property
    def committed(self) -> bool:
        ...

    @property
    def description(self) -> str:
        ...

    @overload
    def __init__(self) -> None:
        """This method is protected."""
        ...

    @overload
    def __init__(self, description: str) -> None:
        """This method is protected."""
        ...

    def cancel(self) -> None:
        ...

    def commit(self) -> None:
        """
        Commits this transaction. Once a transaction has been committed, further
        calls to this method will do nothing. You should always call this method
        after creating a transaction to ensure that the transaction is closed properly.
        """
        ...

    def dispose(self, disposing: bool) -> None:
        """This method is protected."""
        ...

    def on_cancel(self) -> None:
        """
        User code should implement this method to perform the actual work of
        committing a transaction.
        
        This method is protected.
        """
        ...

    def on_commit(self) -> None:
        """
        User code should implement this method to perform the actual work of
        committing a transaction.
        
        This method is protected.
        """
        ...


class IDesignerHost(System.ComponentModel.Design.IServiceContainer, metaclass=abc.ABCMeta):
    """
    Provides methods to adjust the configuration of and retrieve
    information about the services and behavior of a designer.
    """

    @property
    @abc.abstractmethod
    def loading(self) -> bool:
        """
        Gets or sets a value indicating whether the designer host
        is currently loading the document.
        """
        ...

    @property
    @abc.abstractmethod
    def in_transaction(self) -> bool:
        """Gets a value indicating whether the designer host is currently in a transaction."""
        ...

    @property
    @abc.abstractmethod
    def container(self) -> System.ComponentModel.IContainer:
        """Gets the container for this designer host."""
        ...

    @property
    @abc.abstractmethod
    def root_component(self) -> System.ComponentModel.IComponent:
        """Gets the instance of the base class used as the base class for the current design."""
        ...

    @property
    @abc.abstractmethod
    def root_component_class_name(self) -> str:
        """Gets the fully qualified name of the class that is being designed."""
        ...

    @property
    @abc.abstractmethod
    def transaction_description(self) -> str:
        """Gets the description of the current transaction."""
        ...

    @property
    @abc.abstractmethod
    def activated(self) -> _EventContainer[typing.Callable[[System.Object, System.EventArgs], None], None]:
        """Adds an event handler for the System.ComponentModel.Design.IDesignerHost.Activated event."""
        ...

    @activated.setter
    def activated(self, value: _EventContainer[typing.Callable[[System.Object, System.EventArgs], None], None]) -> None:
        ...

    @property
    @abc.abstractmethod
    def deactivated(self) -> _EventContainer[typing.Callable[[System.Object, System.EventArgs], None], None]:
        """Adds an event handler for the System.ComponentModel.Design.IDesignerHost.Deactivated event."""
        ...

    @deactivated.setter
    def deactivated(self, value: _EventContainer[typing.Callable[[System.Object, System.EventArgs], None], None]) -> None:
        ...

    @property
    @abc.abstractmethod
    def load_complete(self) -> _EventContainer[typing.Callable[[System.Object, System.EventArgs], None], None]:
        """Adds an event handler for the System.ComponentModel.Design.IDesignerHost.LoadComplete event."""
        ...

    @load_complete.setter
    def load_complete(self, value: _EventContainer[typing.Callable[[System.Object, System.EventArgs], None], None]) -> None:
        ...

    @property
    @abc.abstractmethod
    def transaction_closed(self) -> _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.DesignerTransactionCloseEventArgs], None], None]:
        """Adds an event handler for the System.ComponentModel.Design.IDesignerHost.TransactionClosed event."""
        ...

    @transaction_closed.setter
    def transaction_closed(self, value: _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.DesignerTransactionCloseEventArgs], None], None]) -> None:
        ...

    @property
    @abc.abstractmethod
    def transaction_closing(self) -> _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.DesignerTransactionCloseEventArgs], None], None]:
        """Adds an event handler for the System.ComponentModel.Design.IDesignerHost.TransactionClosing event."""
        ...

    @transaction_closing.setter
    def transaction_closing(self, value: _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.DesignerTransactionCloseEventArgs], None], None]) -> None:
        ...

    @property
    @abc.abstractmethod
    def transaction_opened(self) -> _EventContainer[typing.Callable[[System.Object, System.EventArgs], None], None]:
        """Adds an event handler for the System.ComponentModel.Design.IDesignerHost.TransactionOpened event."""
        ...

    @transaction_opened.setter
    def transaction_opened(self, value: _EventContainer[typing.Callable[[System.Object, System.EventArgs], None], None]) -> None:
        ...

    @property
    @abc.abstractmethod
    def transaction_opening(self) -> _EventContainer[typing.Callable[[System.Object, System.EventArgs], None], None]:
        """Adds an event handler for the System.ComponentModel.Design.IDesignerHost.TransactionOpening event."""
        ...

    @transaction_opening.setter
    def transaction_opening(self, value: _EventContainer[typing.Callable[[System.Object, System.EventArgs], None], None]) -> None:
        ...

    def activate(self) -> None:
        """Activates the designer that this host is hosting."""
        ...

    @overload
    def create_component(self, component_class: typing.Type) -> System.ComponentModel.IComponent:
        """Creates a component of the specified class type."""
        ...

    @overload
    def create_component(self, component_class: typing.Type, name: str) -> System.ComponentModel.IComponent:
        """Creates a component of the given class type and name and places it into the designer container."""
        ...

    @overload
    def create_transaction(self) -> System.ComponentModel.Design.DesignerTransaction:
        """
        Lengthy operations that involve multiple components may raise many events. These events
        may cause other side-effects, such as flicker or performance degradation. When operating
        on multiple components at one time, or setting multiple properties on a single component,
        you should encompass these changes inside a transaction. Transactions are used
        to improve performance and reduce flicker. Slow operations can listen to
        transaction events and only do work when the transaction completes.
        """
        ...

    @overload
    def create_transaction(self, description: str) -> System.ComponentModel.Design.DesignerTransaction:
        """
        Lengthy operations that involve multiple components may raise many events. These events
        may cause other side-effects, such as flicker or performance degradation. When operating
        on multiple components at one time, or setting multiple properties on a single component,
        you should encompass these changes inside a transaction. Transactions are used
        to improve performance and reduce flicker. Slow operations can listen to
        transaction events and only do work when the transaction completes.
        """
        ...

    def destroy_component(self, component: System.ComponentModel.IComponent) -> None:
        """Destroys the given component, removing it from the design container."""
        ...

    def get_designer(self, component: System.ComponentModel.IComponent) -> System.ComponentModel.Design.IDesigner:
        """Gets the designer instance for the specified component."""
        ...

    def get_type(self, type_name: str) -> typing.Type:
        """Gets the type instance for the specified fully qualified type name ."""
        ...


class DesignerCollection(System.Object, System.Collections.ICollection):
    """Provides a read-only collection of documents."""

    @property
    def count(self) -> int:
        """Gets or sets the number of documents in the collection."""
        ...

    def __getitem__(self, index: int) -> System.ComponentModel.Design.IDesignerHost:
        """Gets or sets the document at the specified index."""
        ...

    @overload
    def __init__(self, designers: typing.List[System.ComponentModel.Design.IDesignerHost]) -> None:
        """
        Initializes a new instance of the System.ComponentModel.Design.DesignerCollection class
        that stores an array with a pointer to each System.ComponentModel.Design.IDesignerHost
        for each document in the collection.
        """
        ...

    @overload
    def __init__(self, designers: System.Collections.IList) -> None:
        """
        Initializes a new instance of the System.ComponentModel.Design.DesignerCollection class
        that stores an array with a pointer to each System.ComponentModel.Design.IDesignerHost
        for each document in the collection.
        """
        ...

    def get_enumerator(self) -> System.Collections.IEnumerator:
        """Creates and retrieves a new enumerator for this collection."""
        ...


class CheckoutException(System.Runtime.InteropServices.ExternalException):
    """
    The exception thrown when an attempt is made to edit a file that is checked into
    a source control program.
    """

    CANCELED: System.ComponentModel.Design.CheckoutException = ...
    """
    Initializes a System.ComponentModel.Design.CheckoutException that specifies that the checkout
    was canceled. This field is read-only.
    """

    @overload
    def __init__(self) -> None:
        """
        Initializes a new instance of the System.ComponentModel.Design.CheckoutException class with
        no associated message or error code.
        """
        ...

    @overload
    def __init__(self, message: str) -> None:
        """
        Initializes a new instance of the System.ComponentModel.Design.CheckoutException
        class with the specified message.
        """
        ...

    @overload
    def __init__(self, message: str, error_code: int) -> None:
        """
        Initializes a new instance of the System.ComponentModel.Design.CheckoutException
        class with the specified message and error code.
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
    def __init__(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """
        Need this constructor since Exception implements ISerializable. We don't have any fields,
        so just forward this to base.
        
        This method is protected.
        
        Obsoletions.LegacyFormatterImplMessage
        """
        ...


class IDesignerOptionService(metaclass=abc.ABCMeta):
    """Provides access to get and set option values for a designer."""

    def get_option_value(self, page_name: str, value_name: str) -> System.Object:
        """Gets the value of an option defined in this package."""
        ...

    def set_option_value(self, page_name: str, value_name: str, value: typing.Any) -> None:
        """Sets the value of an option defined in this package."""
        ...


class DesignerOptionService(System.Object, System.ComponentModel.Design.IDesignerOptionService, metaclass=abc.ABCMeta):
    """Provides access to get and set option values for a designer."""

    class DesignerOptionCollection(System.Object, System.Collections.IList):
        """
        The DesignerOptionCollection class is a collection that contains
        other DesignerOptionCollection objects. This forms a tree of options,
        with each branch of the tree having a name and a possible collection of
        properties. Each parent branch of the tree contains a union of the
        properties if all the branch's children.
        """

        @property
        def count(self) -> int:
            """The count of child options collections this collection contains."""
            ...

        @property
        def name(self) -> str:
            """
            The name of this collection. Names are programmatic names and are not
            localized. A name search is case insensitive.
            """
            ...

        @property
        def parent(self) -> System.ComponentModel.Design.DesignerOptionService.DesignerOptionCollection:
            """Returns the parent collection object, or null if there is no parent."""
            ...

        @property
        def properties(self) -> System.ComponentModel.PropertyDescriptorCollection:
            """
            The collection of properties that this OptionCollection, along with all of
            its children, offers. PropertyDescriptors are taken directly from the
            value passed to CreateObjectCollection and wrapped in an additional property
            descriptor that hides the value object from the user. This means that any
            value may be passed into the "component" parameter of the various
            PropertyDescriptor methods. The value is ignored and is replaced with
            the correct value internally.
            """
            ...

        @overload
        def __getitem__(self, index: int) -> System.ComponentModel.Design.DesignerOptionService.DesignerOptionCollection:
            """Retrieves the child collection at the given index."""
            ...

        @overload
        def __getitem__(self, name: str) -> System.ComponentModel.Design.DesignerOptionService.DesignerOptionCollection:
            """
            Retrieves the child collection at the given name. The name search is case
            insensitive.
            """
            ...

        def copy_to(self, array: System.Array, index: int) -> None:
            """Copies this collection to an array."""
            ...

        def get_enumerator(self) -> System.Collections.IEnumerator:
            """Returns an enumerator that can be used to iterate this collection."""
            ...

        def index_of(self, value: System.ComponentModel.Design.DesignerOptionService.DesignerOptionCollection) -> int:
            """Returns the numerical index of the given value."""
            ...

        def show_dialog(self) -> bool:
            """
            Displays a dialog-based user interface that allows the user to
            configure the various options.
            """
            ...

    @property
    def options(self) -> System.ComponentModel.Design.DesignerOptionService.DesignerOptionCollection:
        """
        Returns the options collection for this service. There is
        always a global options collection that contains child collections.
        """
        ...

    def create_option_collection(self, parent: System.ComponentModel.Design.DesignerOptionService.DesignerOptionCollection, name: str, value: typing.Any) -> System.ComponentModel.Design.DesignerOptionService.DesignerOptionCollection:
        """
        Creates a new DesignerOptionCollection with the given name, and adds it to
        the given parent. The "value" parameter specifies an object whose public
        properties will be used in the Properties collection of the option collection.
        The value parameter can be null if this options collection does not offer
        any properties. Properties will be wrapped in such a way that passing
        anything into the component parameter of the property descriptor will be
        ignored and the value object will be substituted.
        
        This method is protected.
        """
        ...

    def populate_option_collection(self, options: System.ComponentModel.Design.DesignerOptionService.DesignerOptionCollection) -> None:
        """
        This method is called on demand the first time a user asks for child
        options or properties of an options collection.
        
        This method is protected.
        """
        ...

    def show_dialog(self, options: System.ComponentModel.Design.DesignerOptionService.DesignerOptionCollection, option_object: typing.Any) -> bool:
        """
        This method must be implemented to show the options dialog UI for the given object.
        
        This method is protected.
        """
        ...


class IComponentInitializer(metaclass=abc.ABCMeta):
    """
    IComponentInitializer can be implemented on an object that also implements IDesigner.
    This interface allows a newly created component to be given some stock default values,
    such as a caption, default size, or other values. Recommended default values for
    the component's properties are passed in as a dictionary.
    """

    def initialize_existing_component(self, default_values: System.Collections.IDictionary) -> None:
        """
        This method is called when an existing component is being re-initialized. This may occur after
        dragging a component to another container, for example. The default_values
        property contains a name/value dictionary of default values that should be applied
        to properties. This dictionary may be null if no default values are specified.
        You may use the default_values dictionary to apply recommended defaults to properties
        but you should not modify component properties beyond what is stored in the
        dictionary, because this is an existing component that may already have properties
        set on it.
        """
        ...

    def initialize_new_component(self, default_values: System.Collections.IDictionary) -> None:
        """
        This method is called when a component is first initialized, typically after being first added
        to a design surface. The default_values property contains a name/value dictionary of default
        values that should be applied to properties. This dictionary may be null if no default values
        are specified. You may perform any initialization of this component that you like, and you
        may even ignore the default_values dictionary altogether if you wish.
        """
        ...


class ITypeResolutionService(metaclass=abc.ABCMeta):
    """The type resolution service is used to load types at design time."""

    @overload
    def get_assembly(self, name: System.Reflection.AssemblyName) -> System.Reflection.Assembly:
        """Retrieves the requested assembly."""
        ...

    @overload
    def get_assembly(self, name: System.Reflection.AssemblyName, throw_on_error: bool) -> System.Reflection.Assembly:
        """Retrieves the requested assembly."""
        ...

    def get_path_of_assembly(self, name: System.Reflection.AssemblyName) -> str:
        """Returns the path to the file name from which the assembly was loaded."""
        ...

    @overload
    def get_type(self, name: str) -> typing.Type:
        """Loads a type with the given name."""
        ...

    @overload
    def get_type(self, name: str, throw_on_error: bool) -> typing.Type:
        """Loads a type with the given name."""
        ...

    @overload
    def get_type(self, name: str, throw_on_error: bool, ignore_case: bool) -> typing.Type:
        """Loads a type with the given name."""
        ...

    def reference_assembly(self, name: System.Reflection.AssemblyName) -> None:
        """
        References the given assembly name. Once an assembly has
        been referenced types may be loaded from it without
        qualifying them with the assembly.
        """
        ...


class StandardToolWindows(System.Object):
    """
    Defines GUID specifiers that contain GUIDs which reference the standard set of tool windows that are available in
    the design environment.
    """

    OBJECT_BROWSER: System.Guid = ...
    """Gets the GUID for the object browser."""

    OUTPUT_WINDOW: System.Guid = ...
    """Gets the GUID for the output window."""

    PROJECT_EXPLORER: System.Guid = ...
    """Gets the GUID for the project explorer."""

    PROPERTY_BROWSER: System.Guid = ...
    """Gets the GUID for the properties window."""

    RELATED_LINKS: System.Guid = ...
    """Gets the GUID for the related links frame."""

    SERVER_EXPLORER: System.Guid = ...
    """Gets the GUID for the server explorer."""

    TASK_LIST: System.Guid = ...
    """Gets the GUID for the task list."""

    TOOLBOX: System.Guid = ...
    """Gets the GUID for the toolbox."""


class ComponentEventArgs(System.EventArgs):
    """
    Provides data for the System.ComponentModel.Design.IComponentChangeService.ComponentEvent
    event raised for component-level events.
    """

    @property
    def component(self) -> System.ComponentModel.IComponent:
        """Gets or sets the component associated with the event."""
        ...

    def __init__(self, component: System.ComponentModel.IComponent) -> None:
        """Initializes a new instance of the System.ComponentModel.Design.ComponentEventArgs class."""
        ...


class ComponentChangedEventArgs(System.EventArgs):
    """Provides data for the System.ComponentModel.Design.IComponentChangeService.ComponentChanged event."""

    @property
    def component(self) -> System.Object:
        """Gets or sets the component that is the cause of this event."""
        ...

    @property
    def member(self) -> System.ComponentModel.MemberDescriptor:
        """Gets or sets the member that is about to change."""
        ...

    @property
    def new_value(self) -> System.Object:
        """Gets or sets the new value of the changed member."""
        ...

    @property
    def old_value(self) -> System.Object:
        """Gets or sets the old value of the changed member."""
        ...

    def __init__(self, component: typing.Any, member: System.ComponentModel.MemberDescriptor, old_value: typing.Any, new_value: typing.Any) -> None:
        """Initializes a new instance of the System.ComponentModel.Design.ComponentChangedEventArgs class."""
        ...


class ComponentChangingEventArgs(System.EventArgs):
    """Provides data for the System.ComponentModel.Design.IComponentChangeService.ComponentChanging event."""

    @property
    def component(self) -> System.Object:
        """Gets or sets the component that is being changed or that is the parent container of the member being changed."""
        ...

    @property
    def member(self) -> System.ComponentModel.MemberDescriptor:
        """Gets or sets the member of the component that is about to be changed."""
        ...

    def __init__(self, component: typing.Any, member: System.ComponentModel.MemberDescriptor) -> None:
        """Initializes a new instance of the System.ComponentModel.Design.ComponentChangingEventArgs class."""
        ...


class ComponentRenameEventArgs(System.EventArgs):
    """Provides data for the System.ComponentModel.Design.IComponentChangeService.ComponentRename event."""

    @property
    def component(self) -> System.Object:
        """Gets or sets the component that is being renamed."""
        ...

    @property
    def old_name(self) -> str:
        """Gets or sets the name of the component before the rename."""
        ...

    @property
    def new_name(self) -> str:
        """Gets or sets the current name of the component."""
        ...

    def __init__(self, component: typing.Any, old_name: str, new_name: str) -> None:
        """
        Initializes a new instance of the System.ComponentModel.Design.ComponentRenameEventArgs
        class.
        """
        ...


class IComponentChangeService(metaclass=abc.ABCMeta):
    """Provides an interface to add and remove the event handlers for System.ComponentModel.Design.IComponentChangeService.ComponentAdded, System.ComponentModel.Design.IComponentChangeService.ComponentAdding, System.ComponentModel.Design.IComponentChangeService.ComponentChanged, System.ComponentModel.Design.IComponentChangeService.ComponentChanging, System.ComponentModel.Design.IComponentChangeService.ComponentRemoved, System.ComponentModel.Design.IComponentChangeService.ComponentRemoving, and System.ComponentModel.Design.IComponentChangeService.ComponentRename events."""

    @property
    @abc.abstractmethod
    def component_added(self) -> _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.ComponentEventArgs], None], None]:
        """Adds an event handler for the System.ComponentModel.Design.IComponentChangeService.ComponentAdded event."""
        ...

    @component_added.setter
    def component_added(self, value: _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.ComponentEventArgs], None], None]) -> None:
        ...

    @property
    @abc.abstractmethod
    def component_adding(self) -> _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.ComponentEventArgs], None], None]:
        """Adds an event handler for the System.ComponentModel.Design.IComponentChangeService.ComponentAdding event."""
        ...

    @component_adding.setter
    def component_adding(self, value: _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.ComponentEventArgs], None], None]) -> None:
        ...

    @property
    @abc.abstractmethod
    def component_changed(self) -> _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.ComponentChangedEventArgs], None], None]:
        """Adds an event handler for the System.ComponentModel.Design.IComponentChangeService.ComponentChanged event."""
        ...

    @component_changed.setter
    def component_changed(self, value: _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.ComponentChangedEventArgs], None], None]) -> None:
        ...

    @property
    @abc.abstractmethod
    def component_changing(self) -> _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.ComponentChangingEventArgs], None], None]:
        """Adds an event handler for the System.ComponentModel.Design.IComponentChangeService.ComponentChanging event."""
        ...

    @component_changing.setter
    def component_changing(self, value: _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.ComponentChangingEventArgs], None], None]) -> None:
        ...

    @property
    @abc.abstractmethod
    def component_removed(self) -> _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.ComponentEventArgs], None], None]:
        """Adds an event handler for the System.ComponentModel.Design.IComponentChangeService.OnComponentRemoved event."""
        ...

    @component_removed.setter
    def component_removed(self, value: _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.ComponentEventArgs], None], None]) -> None:
        ...

    @property
    @abc.abstractmethod
    def component_removing(self) -> _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.ComponentEventArgs], None], None]:
        """Adds an event handler for the System.ComponentModel.Design.IComponentChangeService.OnComponentRemoving event."""
        ...

    @component_removing.setter
    def component_removing(self, value: _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.ComponentEventArgs], None], None]) -> None:
        ...

    @property
    @abc.abstractmethod
    def component_rename(self) -> _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.ComponentRenameEventArgs], None], None]:
        """Adds an event handler for the System.ComponentModel.Design.IComponentChangeService.OnComponentRename event."""
        ...

    @component_rename.setter
    def component_rename(self, value: _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.ComponentRenameEventArgs], None], None]) -> None:
        ...

    def on_component_changed(self, component: typing.Any, member: System.ComponentModel.MemberDescriptor, old_value: typing.Any, new_value: typing.Any) -> None:
        """Announces to the component change service that a particular component has changed."""
        ...

    def on_component_changing(self, component: typing.Any, member: System.ComponentModel.MemberDescriptor) -> None:
        """Announces to the component change service that a particular component is changing."""
        ...


class DesignerEventArgs(System.EventArgs):
    """
    Provides data for the System.ComponentModel.Design.IDesignerEventService.DesignerEvent
    event that is generated when a document is created or disposed.
    """

    @property
    def designer(self) -> System.ComponentModel.Design.IDesignerHost:
        """Gets or sets the host of the document."""
        ...

    def __init__(self, host: System.ComponentModel.Design.IDesignerHost) -> None:
        """
        Initializes a new instance of the System.ComponentModel.Design.DesignerEventArgs
        class.
        """
        ...


class IExtenderProviderService(metaclass=abc.ABCMeta):
    """Provides an interface to add and remove extender providers."""

    def add_extender_provider(self, provider: System.ComponentModel.IExtenderProvider) -> None:
        """Adds an extender provider."""
        ...

    def remove_extender_provider(self, provider: System.ComponentModel.IExtenderProvider) -> None:
        """Removes an extender provider."""
        ...


class ActiveDesignerEventArgs(System.EventArgs):
    """
    Provides data for the System.ComponentModel.Design.IDesignerEventService.ActiveDesigner
    event.
    """

    @property
    def old_designer(self) -> System.ComponentModel.Design.IDesignerHost:
        """Gets or sets the document that is losing activation."""
        ...

    @property
    def new_designer(self) -> System.ComponentModel.Design.IDesignerHost:
        """Gets or sets the document that is gaining activation."""
        ...

    def __init__(self, old_designer: System.ComponentModel.Design.IDesignerHost, new_designer: System.ComponentModel.Design.IDesignerHost) -> None:
        """
        Initializes a new instance of the System.ComponentModel.Design.ActiveDesignerEventArgs
        class.
        """
        ...


class IReferenceService(metaclass=abc.ABCMeta):
    """
    Provides an interface to get names and references to objects. These
    methods can search using the specified name or reference.
    """

    def get_component(self, reference: typing.Any) -> System.ComponentModel.IComponent:
        """Gets the base component that anchors this reference."""
        ...

    def get_name(self, reference: typing.Any) -> str:
        """Gets the name for this reference."""
        ...

    def get_reference(self, name: str) -> System.Object:
        """Gets a reference for the specified name."""
        ...

    @overload
    def get_references(self) -> typing.List[System.Object]:
        """Gets all available references."""
        ...

    @overload
    def get_references(self, base_type: typing.Type) -> typing.List[System.Object]:
        """Gets all available references of this type."""
        ...


class IDesignerEventService(metaclass=abc.ABCMeta):
    """Provides global event notifications and the ability to create designers."""

    @property
    @abc.abstractmethod
    def active_designer(self) -> System.ComponentModel.Design.IDesignerHost:
        """Gets the currently active designer."""
        ...

    @property
    @abc.abstractmethod
    def designers(self) -> System.ComponentModel.Design.DesignerCollection:
        """Gets or sets a collection of running design documents in the development environment."""
        ...

    @property
    @abc.abstractmethod
    def active_designer_changed(self) -> _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.ActiveDesignerEventArgs], None], None]:
        """Adds an event that will be raised when the currently active designer changes."""
        ...

    @active_designer_changed.setter
    def active_designer_changed(self, value: _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.ActiveDesignerEventArgs], None], None]) -> None:
        ...

    @property
    @abc.abstractmethod
    def designer_created(self) -> _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.DesignerEventArgs], None], None]:
        """Adds an event that will be raised when a designer is created."""
        ...

    @designer_created.setter
    def designer_created(self, value: _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.DesignerEventArgs], None], None]) -> None:
        ...

    @property
    @abc.abstractmethod
    def designer_disposed(self) -> _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.DesignerEventArgs], None], None]:
        """Adds an event that will be raised when a designer is disposed."""
        ...

    @designer_disposed.setter
    def designer_disposed(self, value: _EventContainer[typing.Callable[[System.Object, System.ComponentModel.Design.DesignerEventArgs], None], None]) -> None:
        ...

    @property
    @abc.abstractmethod
    def selection_changed(self) -> _EventContainer[typing.Callable[[System.Object, System.EventArgs], None], None]:
        """Adds an event that will be raised when the global selection changes."""
        ...

    @selection_changed.setter
    def selection_changed(self, value: _EventContainer[typing.Callable[[System.Object, System.EventArgs], None], None]) -> None:
        ...


class SelectionTypes(Enum):
    """
    Specifies identifiers that indicate the type of selection for a component or
    group of components that are selected.
    """

    AUTO = ...
    """
    A Normal selection. With this type of selection, the selection service responds
    to the control and shift keys to support appending or toggling components into the
    selection as needed.
    """

    NORMAL = ...
    """
    A Normal selection. With this type of selection, the selection service responds
    to the control and shift keys to support appending or toggling components into the
    selection as needed.
    
    SelectionTypes.Normal has been deprecated. Use SelectionTypes.Auto instead.
    """

    REPLACE = ...
    """
    A Replace selection. This causes the selection service to always replace the
    current selection with the replacement.
    """

    MOUSE_DOWN = ...
    """
    A MouseDown selection. Happens when the user presses down on
    the mouse button when the pointer is over a control (or component). If a
    component in the selection list is already selected, it does not remove the
    existing selection, but promotes that component to be the primary selection.
    
    SelectionTypes.MouseDown has been deprecated and is not supported.
    """

    MOUSE_UP = ...
    """
    A MouseUp selection. Happens when the user releases the
    mouse button when a control (or component) has been selected. If a component
    in the selection list is already selected, it does not remove the
    existing selection, but promotes that component to be the primary selection.
    
    SelectionTypes.MouseUp has been deprecated and is not supported.
    """

    CLICK = ...
    """
    A Click selection.
    Happens when a user clicks on a component. If a component in the selection list is already
    selected, it does not remove the existing selection, but promotes that component to be the
    primary selection.
    
    SelectionTypes.Click has been deprecated. Use SelectionTypes.Primary instead.
    """

    PRIMARY = ...
    """
    A Primary selection.
    Happens when a user clicks on a component. If a component in the selection list is already
    selected, it does not remove the existing selection, but promotes that component to be the
    primary selection.
    """

    TOGGLE = ...
    """
    A toggle selection.
    This selection toggles the current selection with the provided selection. So, if
    a component is already selected and is passed into SetSelectedComponents with a
    selection type of Toggle, it will be unselected.
    """

    ADD = ...
    """
    An Add selection.
    This selection adds the selected components to the current selection,
    maintaining the current set of selected components.
    """

    REMOVE = ...
    """
    A Remove selection.
    This selection removes the selected components from the current selection,
    maintaining the current set of selected components.
    """

    VALID = ...
    """
    Limits valid selection types to Normal, Replace, MouseDown, MouseUp,
    Click, Toggle or Add.
    
    SelectionTypes.Valid has been deprecated. Use Enum class methods to determine valid values, or use a type converter instead.
    """


class ISelectionService(metaclass=abc.ABCMeta):
    """Provides an interface for a designer to select components."""

    @property
    @abc.abstractmethod
    def primary_selection(self) -> System.Object:
        """Gets the object that is currently the primary selection."""
        ...

    @property
    @abc.abstractmethod
    def selection_count(self) -> int:
        """Gets the count of selected objects."""
        ...

    @property
    @abc.abstractmethod
    def selection_changed(self) -> _EventContainer[typing.Callable[[System.Object, System.EventArgs], None], None]:
        """Adds a System.ComponentModel.Design.ISelectionService.SelectionChanged event handler to the selection service."""
        ...

    @selection_changed.setter
    def selection_changed(self, value: _EventContainer[typing.Callable[[System.Object, System.EventArgs], None], None]) -> None:
        ...

    @property
    @abc.abstractmethod
    def selection_changing(self) -> _EventContainer[typing.Callable[[System.Object, System.EventArgs], None], None]:
        """Adds an event handler to the selection service."""
        ...

    @selection_changing.setter
    def selection_changing(self, value: _EventContainer[typing.Callable[[System.Object, System.EventArgs], None], None]) -> None:
        ...

    def get_component_selected(self, component: typing.Any) -> bool:
        """Gets a value indicating whether the component is currently selected."""
        ...

    def get_selected_components(self) -> System.Collections.ICollection:
        """Gets a collection of components that are currently part of the user's selection."""
        ...

    @overload
    def set_selected_components(self, components: System.Collections.ICollection) -> None:
        """Sets the currently selected set of components."""
        ...

    @overload
    def set_selected_components(self, components: System.Collections.ICollection, selection_type: System.ComponentModel.Design.SelectionTypes) -> None:
        """Sets the currently selected set of components to those with the specified selection type within the specified array of components."""
        ...


class IResourceService(metaclass=abc.ABCMeta):
    """Provides designers a way to access a resource for the current design-time object."""

    def get_resource_reader(self, info: System.Globalization.CultureInfo) -> System.Resources.IResourceReader:
        """
        Locates the resource reader for the specified culture and
        returns it.
        """
        ...

    def get_resource_writer(self, info: System.Globalization.CultureInfo) -> typing.Any:
        """
        Locates the resource writer for the specified culture
        and returns it. This will create a new resource for
        the specified culture and destroy any existing resource,
        should it exist.
        """
        ...


class ITreeDesigner(System.ComponentModel.Design.IDesigner, metaclass=abc.ABCMeta):
    """
    ITreeDesigner is a variation of IDesigner that provides support for
    generically indicating parent / child relationships within a designer.
    """

    @property
    @abc.abstractmethod
    def children(self) -> System.Collections.ICollection:
        """
        Retrieves the children of this designer. This will return an empty collection
        if this designer has no children.
        """
        ...

    @property
    @abc.abstractmethod
    def parent(self) -> System.ComponentModel.Design.IDesigner:
        """
        Retrieves the parent designer for this designer. This may return null if
        there is no parent.
        """
        ...


class IInheritanceService(metaclass=abc.ABCMeta):
    """Provides a set of utilities for analyzing and identifying inherited components."""

    def add_inherited_components(self, component: System.ComponentModel.IComponent, container: System.ComponentModel.IContainer) -> None:
        """Adds inherited components from the specified component to the specified container."""
        ...

    def get_inheritance_attribute(self, component: System.ComponentModel.IComponent) -> System.ComponentModel.InheritanceAttribute:
        """
        Gets the inheritance attribute of the specified
        component. If the component is not being inherited, this method will return the
        value System.ComponentModel.InheritanceAttribute.NotInherited.
        Otherwise it will return the inheritance attribute for this component.
        """
        ...


class DesigntimeLicenseContext(System.ComponentModel.LicenseContext):
    """Provides design-time support for licensing."""

    @property
    def usage_mode(self) -> System.ComponentModel.LicenseUsageMode:
        """Gets or sets the license usage mode."""
        ...

    def get_saved_license_key(self, type: typing.Type, resource_assembly: System.Reflection.Assembly) -> str:
        """Gets a saved license key."""
        ...

    def set_saved_license_key(self, type: typing.Type, key: str) -> None:
        """Sets a saved license key."""
        ...


class DesigntimeLicenseContextSerializer(System.Object):
    """Provides support for design-time license context serialization."""

    @staticmethod
    def serialize(o: System.IO.Stream, crypto_key: str, context: System.ComponentModel.Design.DesigntimeLicenseContext) -> None:
        """
        Serializes the licenses within the specified design-time license context
        using the specified key and output stream.
        """
        ...


class IEventBindingService(metaclass=abc.ABCMeta):
    """Provides a set of useful methods for binding System.ComponentModel.EventDescriptor objects to user code."""

    def create_unique_method_name(self, component: System.ComponentModel.IComponent, e: System.ComponentModel.EventDescriptor) -> str:
        """
        This creates a name for an event handling method for the given component
        and event. The name that is created is guaranteed to be unique in the user's source
        code.
        """
        ...

    def get_compatible_methods(self, e: System.ComponentModel.EventDescriptor) -> System.Collections.ICollection:
        """
        Retrieves a collection of strings. Each string is the name of a method
        in user code that has a signature that is compatible with the given event.
        """
        ...

    def get_event(self, property: System.ComponentModel.PropertyDescriptor) -> System.ComponentModel.EventDescriptor:
        """
        For properties that are representing events, this will return the event
        that the property represents.
        """
        ...

    def get_event_properties(self, events: System.ComponentModel.EventDescriptorCollection) -> System.ComponentModel.PropertyDescriptorCollection:
        """Converts a set of event descriptors to a set of property descriptors."""
        ...

    def get_event_property(self, e: System.ComponentModel.EventDescriptor) -> System.ComponentModel.PropertyDescriptor:
        """Converts a single event to a property."""
        ...

    @overload
    def show_code(self) -> bool:
        """
        Displays the user code for the designer. This will return true if the user
        code could be displayed, or false otherwise.
        """
        ...

    @overload
    def show_code(self, line_number: int) -> bool:
        """
        Displays the user code for the designer. This will return true if the user
        code could be displayed, or false otherwise.
        """
        ...

    @overload
    def show_code(self, component: System.ComponentModel.IComponent, e: System.ComponentModel.EventDescriptor) -> bool:
        """
        Displays the user code for the given event. This will return true if the user
        code could be displayed, or false otherwise.
        """
        ...


class ServiceContainer(System.Object, System.ComponentModel.Design.IServiceContainer, System.IDisposable):
    """This is a simple implementation of IServiceContainer."""

    @property
    def default_services(self) -> typing.List[typing.Type]:
        """
        This property returns the default services that are implemented directly on this IServiceContainer.
        the default implementation of this property is to return the IServiceContainer and ServiceContainer
        types. You may override this property and return your own types, modifying the default behavior
        of GetService.
        
        This property is protected.
        """
        ...

    @overload
    def __init__(self) -> None:
        """Creates a new service object container."""
        ...

    @overload
    def __init__(self, parent_provider: typing.Optional[IServiceProvider]) -> None:
        """Creates a new service object container."""
        ...

    @overload
    def add_service(self, service_type: typing.Type, service_instance: typing.Any) -> None:
        """Adds the given service to the service container."""
        ...

    @overload
    def add_service(self, service_type: typing.Type, service_instance: typing.Any, promote: bool) -> None:
        """Adds the given service to the service container."""
        ...

    @overload
    def add_service(self, service_type: typing.Type, callback: typing.Callable[[System.ComponentModel.Design.IServiceContainer, typing.Type], System.Object]) -> None:
        """Adds the given service to the service container."""
        ...

    @overload
    def add_service(self, service_type: typing.Type, callback: typing.Callable[[System.ComponentModel.Design.IServiceContainer, typing.Type], System.Object], promote: bool) -> None:
        """Adds the given service to the service container."""
        ...

    @overload
    def dispose(self) -> None:
        """
        Disposes this service container. This also walks all instantiated services within the container
        and disposes any that implement IDisposable, and clears the service list.
        """
        ...

    @overload
    def dispose(self, disposing: bool) -> None:
        """
        Disposes this service container. This also walks all instantiated services within the container
        and disposes any that implement IDisposable, and clears the service list.
        
        This method is protected.
        """
        ...

    def get_service(self, service_type: typing.Type) -> System.Object:
        """Retrieves the requested service."""
        ...

    @overload
    def remove_service(self, service_type: typing.Type) -> None:
        """Removes the given service type from the service container."""
        ...

    @overload
    def remove_service(self, service_type: typing.Type, promote: bool) -> None:
        """Removes the given service type from the service container."""
        ...


class ITypeDiscoveryService(metaclass=abc.ABCMeta):
    """
    The type discovery service is used to discover available types at design time,
    when the consumer doesn't know the names of existing types or referenced assemblies.
    """

    def get_types(self, base_type: typing.Type, exclude_global_types: bool) -> System.Collections.ICollection:
        """
        Retrieves the list of available types. If base_type is null, all
        types are returned. Otherwise, only types deriving from the
        specified base type are returned. If bool exclude_global_types is false,
        types from all referenced assemblies are checked. Otherwise,
        only types from non-GAC referenced assemblies are checked.
        """
        ...


class IDesignerFilter(metaclass=abc.ABCMeta):
    """
    Provides access to, and an interface for filtering, the dictionaries that store the
    properties, attributes, or events of a component.
    """

    def post_filter_attributes(self, attributes: System.Collections.IDictionary) -> None:
        """
        Allows a designer to filter the set of attributes the component being designed will expose
        through the System.ComponentModel.TypeDescriptor object.
        """
        ...

    def post_filter_events(self, events: System.Collections.IDictionary) -> None:
        """
        Allows a designer to filter the set of events the component being designed will expose
        through the System.ComponentModel.TypeDescriptor object.
        """
        ...

    def post_filter_properties(self, properties: System.Collections.IDictionary) -> None:
        """
        Allows a designer to filter the set of properties the component being designed will expose
        through the System.ComponentModel.TypeDescriptor object.
        """
        ...

    def pre_filter_attributes(self, attributes: System.Collections.IDictionary) -> None:
        """
        Allows a designer to filter the set of attributes the component being designed will expose
        through the System.ComponentModel.TypeDescriptor object.
        """
        ...

    def pre_filter_events(self, events: System.Collections.IDictionary) -> None:
        """
        Allows a designer to filter the set of events the component being designed will expose
        through the System.ComponentModel.TypeDescriptor object.
        """
        ...

    def pre_filter_properties(self, properties: System.Collections.IDictionary) -> None:
        """
        Allows a designer to filter the set of properties the component being designed will expose
        through the System.ComponentModel.TypeDescriptor object.
        """
        ...


class ViewTechnology(Enum):
    """Specifies a set of technologies designer hosts should support."""

    PASSTHROUGH = 0
    """
    Specifies that the view for a root designer is defined by some
    private interface contract between the designer and the
    development environment. This implies a tight coupling
    between the development environment and the designer, and should
    be avoided. This does allow older COM2 technologies to
    be shown in development environments that support
    COM2 interface technologies such as doc objects and ActiveX
    controls.
    
    ViewTechnology.Passthrough has been deprecated. Use ViewTechnology.Default instead.
    """

    WINDOWS_FORMS = 1
    """
    Specifies that the view for a root designer is supplied through
    a Windows Forms control object. The designer host will fill the
    development environment's document window with this control.
    
    ViewTechnology.WindowsForms has been deprecated. Use ViewTechnology.Default instead.
    """

    DEFAULT = 2
    """
    Specifies the default view technology support. Here, the root designer may return
    any type of object it wishes, but it must be an object that can be "fitted" with
    an adapter to the technology of the host. Hosting environments such as Visual
    Studio will provide a way to plug in new view technology adapters. The default
    view object for the Windows Forms designer is a Control instance, while the
    default view object for the Avalon designer is an Element instance.
    """


class IDesignerHostTransactionState(metaclass=abc.ABCMeta):
    """Methods for the Designer host to report on the state of transactions."""

    @property
    @abc.abstractmethod
    def is_closing_transaction(self) -> bool:
        ...


class HelpKeywordAttribute(System.Attribute):
    """
    Allows specification of the context keyword that will be specified for this class or member. By default,
    the help keyword for a class is the Type's full name, and for a member it's the full name of the type that declared the property,
    plus the property name itself.
    
    For example, consider System.Windows.Forms.Button and it's Text property:
    
    The class keyword is "System.Windows.Forms.Button", but the Text property keyword is "System.Windows.Forms.Control.Text", because the Text
    property is declared on the System.Windows.Forms.Control class rather than the Button class itself; the Button class inherits the property.
    By contrast, the DialogResult property is declared on the Button so its keyword would be "System.Windows.Forms.Button.DialogResult".
    
    When the help system gets the keywords, it will first look at this attribute. At the class level, it will return the string specified by the
    HelpContextAttribute. Note this will not be used for members of the Type in question. They will still reflect the declaring Type's actual
    full name, plus the member name. To override this, place the attribute on the member itself.
    
    Example:
    
    [HelpKeywordAttribute(typeof(Component))]
    public class MyComponent : Component {
    
    
    public string Property1 { get{return "";};
    
    [HelpKeywordAttribute("SomeNamespace.SomeOtherClass.Property2")]
    public string Property2 { get{return "";};
    
    }
    
    
    For the above class (default without attribution):
    
    Class keyword: "System.ComponentModel.Component" ("MyNamespace.MyComponent')
    Property1 keyword: "MyNamespace.MyComponent.Property1" (default)
    Property2 keyword: "SomeNamespace.SomeOtherClass.Property2" ("MyNamespace.MyComponent.Property2")
    """

    DEFAULT: System.ComponentModel.Design.HelpKeywordAttribute = ...
    """Default value for HelpKeywordAttribute, which is null."""

    @property
    def help_keyword(self) -> str:
        """Retrieves the HelpKeyword this attribute supplies."""
        ...

    @overload
    def __init__(self) -> None:
        """Default constructor, which creates an attribute with a null HelpKeyword."""
        ...

    @overload
    def __init__(self, keyword: str) -> None:
        """Creates a HelpKeywordAttribute with the value being the given keyword string."""
        ...

    @overload
    def __init__(self, t: typing.Type) -> None:
        """Creates a HelpKeywordAttribute with the value being the full name of the given type."""
        ...

    def equals(self, obj: typing.Any) -> bool:
        """Two instances of a HelpKeywordAttribute are equal if they're HelpKeywords are equal."""
        ...

    def get_hash_code(self) -> int:
        """"""
        ...

    def is_default_attribute(self) -> bool:
        """Returns true if this Attribute's HelpKeyword is null."""
        ...


class IExtenderListService(metaclass=abc.ABCMeta):
    """Provides an interface to list extender providers."""

    def get_extender_providers(self) -> typing.List[System.ComponentModel.IExtenderProvider]:
        """Gets the set of extender providers for the component."""
        ...


class StandardCommands(System.Object):
    """
    Specifies identifiers for the standard set of commands that are available to
    most applications.
    """

    ALIGN_BOTTOM: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the AlignBottom command. Read only."""

    ALIGN_HORIZONTAL_CENTERS: System.ComponentModel.Design.CommandID = ...
    """
    Gets the GUID/integer value pair for the AlignHorizontalCenters command. Read
    only.
    """

    ALIGN_LEFT: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the AlignLeft command. Read only."""

    ALIGN_RIGHT: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the AlignRight command. Read only."""

    ALIGN_TO_GRID: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the AlignToGrid command. Read only."""

    ALIGN_TOP: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the AlignTop command. Read only."""

    ALIGN_VERTICAL_CENTERS: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the AlignVerticalCenters command. Read only."""

    ARRANGE_BOTTOM: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the ArrangeBottom command. Read only."""

    ARRANGE_RIGHT: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the ArrangeRight command. Read only."""

    BRING_FORWARD: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the BringForward command. Read only."""

    BRING_TO_FRONT: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the BringToFront command. Read only."""

    CENTER_HORIZONTALLY: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the CenterHorizontally command. Read only."""

    CENTER_VERTICALLY: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the CenterVertically command. Read only."""

    VIEW_CODE: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the Code command. Read only."""

    DOCUMENT_OUTLINE: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the DocumentOutline command. Read only."""

    COPY: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the Copy command. Read only."""

    CUT: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the Cut command. Read only."""

    DELETE: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the Delete command. Read only."""

    GROUP: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the Group command. Read only."""

    HORIZ_SPACE_CONCATENATE: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the HorizSpaceConcatenate command. Read only."""

    HORIZ_SPACE_DECREASE: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the HorizSpaceDecrease command. Read only."""

    HORIZ_SPACE_INCREASE: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the HorizSpaceIncrease command. Read only."""

    HORIZ_SPACE_MAKE_EQUAL: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the HorizSpaceMakeEqual command. Read only."""

    PASTE: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the Paste command. Read only."""

    PROPERTIES: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the Properties command. Read only."""

    REDO: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the Redo command. Read only."""

    MULTI_LEVEL_REDO: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the MultiLevelRedo command. Read only."""

    SELECT_ALL: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the SelectAll command. Read only."""

    SEND_BACKWARD: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the SendBackward command. Read only."""

    SEND_TO_BACK: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the SendToBack command. Read only."""

    SIZE_TO_CONTROL: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the SizeToControl command. Read only."""

    SIZE_TO_CONTROL_HEIGHT: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the SizeToControlHeight command. Read only."""

    SIZE_TO_CONTROL_WIDTH: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the SizeToControlWidth command. Read only."""

    SIZE_TO_FIT: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the SizeToFit command. Read only."""

    SIZE_TO_GRID: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the SizeToGrid command. Read only."""

    SNAP_TO_GRID: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the SnapToGrid command. Read only."""

    TAB_ORDER: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the TabOrder command. Read only."""

    UNDO: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the Undo command. Read only."""

    MULTI_LEVEL_UNDO: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the MultiLevelUndo command. Read only."""

    UNGROUP: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the Ungroup command. Read only."""

    VERT_SPACE_CONCATENATE: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the VertSpaceConcatenate command. Read only."""

    VERT_SPACE_DECREASE: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the VertSpaceDecrease command. Read only."""

    VERT_SPACE_INCREASE: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the VertSpaceIncrease command. Read only."""

    VERT_SPACE_MAKE_EQUAL: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the VertSpaceMakeEqual command. Read only."""

    SHOW_GRID: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the ShowGrid command. Read only."""

    VIEW_GRID: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the ViewGrid command. Read only."""

    REPLACE: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the Replace command. Read only."""

    PROPERTIES_WINDOW: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the PropertiesWindow command. Read only."""

    LOCK_CONTROLS: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the LockControls command. Read only."""

    F_1_HELP: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the F1Help command. Read only."""

    ARRANGE_ICONS: System.ComponentModel.Design.CommandID = ...

    LINEUP_ICONS: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the LineupIcons command. Read only."""

    SHOW_LARGE_ICONS: System.ComponentModel.Design.CommandID = ...
    """Gets the GUID/integer value pair for the ShowLargeIcons command. Read only."""

    VERB_FIRST: System.ComponentModel.Design.CommandID = ...
    """Gets the first of a set of verbs. Read only."""

    VERB_LAST: System.ComponentModel.Design.CommandID = ...
    """Gets the last of a set of verbs.Read only."""


class IRootDesigner(System.ComponentModel.Design.IDesigner, metaclass=abc.ABCMeta):
    """
    Defines the root designer. A root designer is the designer that sits
    at the top, or root, of the object hierarchy. The root designer's job
    is to provide the design-time user interface for the design surface.
    It does this through the View property.
    """

    @property
    @abc.abstractmethod
    def supported_technologies(self) -> typing.List[System.ComponentModel.Design.ViewTechnology]:
        """
        The list of technologies that this designer can support
        for its view. Examples of different technologies are
        Windows Forms and Web Forms. Other object models can be
        supported at design time, but they most be able to
        provide a view in one of the supported technologies.
        """
        ...

    def get_view(self, technology: System.ComponentModel.Design.ViewTechnology) -> System.Object:
        """
        The user interface to present to the user. The returning
        data type is an object because there can be a variety
        of different user interface technologies. Development
        environments typically support more than one technology.
        """
        ...


class ITypeDescriptorFilterService(metaclass=abc.ABCMeta):
    """Modifies the set of type descriptors that a component provides."""

    def filter_attributes(self, component: System.ComponentModel.IComponent, attributes: System.Collections.IDictionary) -> bool:
        """Provides a way to filter the attributes from a component that are displayed to the user."""
        ...

    def filter_events(self, component: System.ComponentModel.IComponent, events: System.Collections.IDictionary) -> bool:
        """Provides a way to filter the events from a component that are displayed to the user."""
        ...

    def filter_properties(self, component: System.ComponentModel.IComponent, properties: System.Collections.IDictionary) -> bool:
        """Provides a way to filter the properties from a component that are displayed to the user."""
        ...


class IComponentDiscoveryService(metaclass=abc.ABCMeta):
    """
    This service allows design-time enumeration of components across the toolbox
    and other available types at design-time.
    """

    def get_component_types(self, designer_host: System.ComponentModel.Design.IDesignerHost, base_type: typing.Type) -> System.Collections.ICollection:
        """
        Retrieves the list of available component types, i.e. types implementing
        IComponent. If base_type is null, all components are retrieved; otherwise
        only component types derived from the specified base_type are returned.
        """
        ...


class _EventContainer(typing.Generic[System_ComponentModel_Design__EventContainer_Callable, System_ComponentModel_Design__EventContainer_ReturnType]):
    """This class is used to provide accurate autocomplete on events and cannot be imported."""

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> System_ComponentModel_Design__EventContainer_ReturnType:
        """Fires the event."""
        ...

    def __iadd__(self, item: System_ComponentModel_Design__EventContainer_Callable) -> typing.Self:
        """Registers an event handler."""
        ...

    def __isub__(self, item: System_ComponentModel_Design__EventContainer_Callable) -> typing.Self:
        """Unregisters an event handler."""
        ...


