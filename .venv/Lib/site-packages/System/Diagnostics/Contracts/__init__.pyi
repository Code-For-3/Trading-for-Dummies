from typing import overload
from enum import Enum
import typing
import warnings

import System
import System.Diagnostics.Contracts
import System.Runtime.Serialization

System_Diagnostics_Contracts__EventContainer_Callable = typing.TypeVar("System_Diagnostics_Contracts__EventContainer_Callable")
System_Diagnostics_Contracts__EventContainer_ReturnType = typing.TypeVar("System_Diagnostics_Contracts__EventContainer_ReturnType")


class ContractFailureKind(Enum):
    """This class has no documentation."""

    PRECONDITION = 0

    POSTCONDITION = 1

    POSTCONDITION_ON_EXCEPTION = 2

    INVARIANT = 3

    ASSERT = 4

    ASSUME = 5


class ContractException(System.Exception):
    """This class has no documentation."""

    @property
    def kind(self) -> System.Diagnostics.Contracts.ContractFailureKind:
        ...

    @property
    def failure(self) -> str:
        ...

    @property
    def user_message(self) -> str:
        ...

    @property
    def condition(self) -> str:
        ...

    def __init__(self, kind: System.Diagnostics.Contracts.ContractFailureKind, failure: str, user_message: str, condition: str, inner_exception: System.Exception) -> None:
        ...

    def get_object_data(self, info: System.Runtime.Serialization.SerializationInfo, context: System.Runtime.Serialization.StreamingContext) -> None:
        """Obsoletions.LegacyFormatterImplMessage"""
        warnings.warn("Obsoletions.LegacyFormatterImplMessage", DeprecationWarning)


class ContractFailedEventArgs(System.EventArgs):
    """This class has no documentation."""

    @property
    def message(self) -> str:
        ...

    @property
    def condition(self) -> str:
        ...

    @property
    def failure_kind(self) -> System.Diagnostics.Contracts.ContractFailureKind:
        ...

    @property
    def original_exception(self) -> System.Exception:
        ...

    @property
    def handled(self) -> bool:
        ...

    @property
    def unwind(self) -> bool:
        ...

    def __init__(self, failure_kind: System.Diagnostics.Contracts.ContractFailureKind, message: str, condition: str, original_exception: System.Exception) -> None:
        ...

    def set_handled(self) -> None:
        ...

    def set_unwind(self) -> None:
        ...


class PureAttribute(System.Attribute):
    """Methods and classes marked with this attribute can be used within calls to Contract methods. Such methods not make any visible state changes."""


class ContractClassAttribute(System.Attribute):
    """Types marked with this attribute specify that a separate type contains the contracts for this type."""

    @property
    def type_containing_contracts(self) -> typing.Type:
        ...

    def __init__(self, type_containing_contracts: typing.Type) -> None:
        ...


class ContractClassForAttribute(System.Attribute):
    """Types marked with this attribute specify that they are a contract for the type that is the argument of the constructor."""

    @property
    def type_contracts_are_for(self) -> typing.Type:
        ...

    def __init__(self, type_contracts_are_for: typing.Type) -> None:
        ...


class ContractInvariantMethodAttribute(System.Attribute):
    """
    This attribute is used to mark a method as being the invariant
    method for a class. The method can have any name, but it must
    return "void" and take no parameters. The body of the method
    must consist solely of one or more calls to the method
    Contract.Invariant. A suggested name for the method is
    "ObjectInvariant".
    """


class ContractReferenceAssemblyAttribute(System.Attribute):
    """Attribute that specifies that an assembly is a reference assembly with contracts."""


class ContractRuntimeIgnoredAttribute(System.Attribute):
    """Methods (and properties) marked with this attribute can be used within calls to Contract methods, but have no runtime behavior associated with them."""


class ContractVerificationAttribute(System.Attribute):
    """
    Instructs downstream tools whether to assume the correctness of this assembly, type or member without performing any verification or not.
    Can use [ContractVerification(false)] to explicitly mark assembly, type or member as one to *not* have verification performed on it.
    Most specific element found (member, type, then assembly) takes precedence.
    (That is useful if downstream tools allow a user to decide which polarity is the default, unmarked case.)
    """

    @property
    def value(self) -> bool:
        ...

    def __init__(self, value: bool) -> None:
        ...


class ContractPublicPropertyNameAttribute(System.Attribute):
    """
    Allows a field f to be used in the method contracts for a method m when f has less visibility than m.
    For instance, if the method is public, but the field is private.
    """

    @property
    def name(self) -> str:
        ...

    def __init__(self, name: str) -> None:
        ...


class ContractArgumentValidatorAttribute(System.Attribute):
    """
    Enables factoring legacy if-then-throw into separate methods for reuse and full control over
    thrown exception and arguments
    """


class ContractAbbreviatorAttribute(System.Attribute):
    """Enables writing abbreviations for contracts that get copied to other methods"""


class ContractOptionAttribute(System.Attribute):
    """Allows setting contract and tool options at assembly, type, or method granularity."""

    @property
    def category(self) -> str:
        ...

    @property
    def setting(self) -> str:
        ...

    @property
    def enabled(self) -> bool:
        ...

    @property
    def value(self) -> str:
        ...

    @overload
    def __init__(self, category: str, setting: str, enabled: bool) -> None:
        ...

    @overload
    def __init__(self, category: str, setting: str, value: str) -> None:
        ...


class Contract(System.Object):
    """Contains static methods for representing program contracts such as preconditions, postconditions, and invariants."""

    contract_failed: _EventContainer[typing.Callable[[System.Object, System.Diagnostics.Contracts.ContractFailedEventArgs], None], None]
    """
    Allows a managed application environment such as an interactive interpreter (IronPython)
    to be notified of contract failures and
    potentially "handle" them, either by throwing a particular exception type, etc.  If any of the
    event handlers sets the Cancel flag in the ContractFailedEventArgs, then the Contract class will
    not pop up an assert dialog box or trigger escalation policy.  Hooking this event requires
    full trust, because it will inform you of bugs in the appdomain and because the event handler
    could allow you to continue execution.
    """

    @staticmethod
    @overload
    def Assert(condition: bool) -> None:
        """
        In debug builds, perform a runtime check that  is true.
        
        :param condition: Expression to check to always be true.
        """
        ...

    @staticmethod
    @overload
    def Assert(condition: bool, userMessage: str) -> None:
        """
        In debug builds, perform a runtime check that  is true.
        
        :param condition: Expression to check to always be true.
        :param userMessage: If it is not a constant string literal, then the contract may not be understood by tools.
        """
        ...

    @staticmethod
    @overload
    def assume(condition: bool) -> None:
        """
        Instructs code analysis tools to assume the expression  is true even if it can not be statically proven to always be true.
        
        :param condition: Expression to assume will always be true.
        """
        ...

    @staticmethod
    @overload
    def assume(condition: bool, user_message: str) -> None:
        """
        Instructs code analysis tools to assume the expression  is true even if it can not be statically proven to always be true.
        
        :param condition: Expression to assume will always be true.
        :param user_message: If it is not a constant string literal, then the contract may not be understood by tools.
        """
        ...

    @staticmethod
    def end_contract_block() -> None:
        """Marker to indicate the end of the contract section of a method."""
        ...

    @staticmethod
    @overload
    def ensures(condition: bool) -> None:
        """
        Specifies a public contract such that the expression  will be true when the enclosing method or property returns normally.
        
        :param condition: Boolean expression representing the contract. May include OldValue and Result.
        """
        ...

    @staticmethod
    @overload
    def ensures(condition: bool, user_message: str) -> None:
        """
        Specifies a public contract such that the expression  will be true when the enclosing method or property returns normally.
        
        :param condition: Boolean expression representing the contract. May include OldValue and Result.
        :param user_message: If it is not a constant string literal, then the contract may not be understood by tools.
        """
        ...

    @staticmethod
    def exists(from_inclusive: int, to_exclusive: int, predicate: typing.Callable[[int], bool]) -> bool:
        """
        Returns whether the  returns true
        for any integer starting from  to  - 1.
        
        :param from_inclusive: First integer to pass to .
        :param to_exclusive: One greater than the last integer to pass to .
        :param predicate: Function that is evaluated from  to  - 1.
        :returns: true if  returns true for any integer starting from  to  - 1.
        """
        ...

    @staticmethod
    def for_all(from_inclusive: int, to_exclusive: int, predicate: typing.Callable[[int], bool]) -> bool:
        """
        Returns whether the  returns true
        for all integers starting from  to  - 1.
        
        :param from_inclusive: First integer to pass to .
        :param to_exclusive: One greater than the last integer to pass to .
        :param predicate: Function that is evaluated from  to  - 1.
        :returns: true if  returns true for all integers starting from  to  - 1.
        """
        ...

    @staticmethod
    @overload
    def invariant(condition: bool) -> None:
        """
        Specifies a contract such that the expression  will be true after every method or property on the enclosing class.
        
        :param condition: Boolean expression representing the contract.
        """
        ...

    @staticmethod
    @overload
    def invariant(condition: bool, user_message: str) -> None:
        """
        Specifies a contract such that the expression  will be true after every method or property on the enclosing class.
        
        :param condition: Boolean expression representing the contract.
        :param user_message: If it is not a constant string literal, then the contract may not be understood by tools.
        """
        ...

    @staticmethod
    @overload
    def requires(condition: bool) -> None:
        """
        Specifies a contract such that the expression  must be true before the enclosing method or property is invoked.
        
        :param condition: Boolean expression representing the contract.
        """
        ...

    @staticmethod
    @overload
    def requires(condition: bool, user_message: str) -> None:
        """
        Specifies a contract such that the expression  must be true before the enclosing method or property is invoked.
        
        :param condition: Boolean expression representing the contract.
        :param user_message: If it is not a constant string literal, then the contract may not be understood by tools.
        """
        ...


class _EventContainer(typing.Generic[System_Diagnostics_Contracts__EventContainer_Callable, System_Diagnostics_Contracts__EventContainer_ReturnType]):
    """This class is used to provide accurate autocomplete on events and cannot be imported."""

    def __call__(self, *args: typing.Any, **kwargs: typing.Any) -> System_Diagnostics_Contracts__EventContainer_ReturnType:
        """Fires the event."""
        ...

    def __iadd__(self, item: System_Diagnostics_Contracts__EventContainer_Callable) -> typing.Self:
        """Registers an event handler."""
        ...

    def __isub__(self, item: System_Diagnostics_Contracts__EventContainer_Callable) -> typing.Self:
        """Unregisters an event handler."""
        ...


