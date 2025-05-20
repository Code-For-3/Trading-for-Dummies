from typing import overload
from enum import Enum
import System
import System.Diagnostics.CodeAnalysis


class SuppressMessageAttribute(System.Attribute):
    """Suppresses reporting of a specific code analysis rule violation, allowing multiple suppressions on a single code artifact. Does not apply to compiler diagnostics."""

    @property
    def category(self) -> str:
        ...

    @property
    def check_id(self) -> str:
        ...

    @property
    def scope(self) -> str:
        ...

    @scope.setter
    def scope(self, value: str) -> None:
        ...

    @property
    def target(self) -> str:
        ...

    @target.setter
    def target(self, value: str) -> None:
        ...

    @property
    def message_id(self) -> str:
        ...

    @message_id.setter
    def message_id(self, value: str) -> None:
        ...

    @property
    def justification(self) -> str:
        ...

    @justification.setter
    def justification(self, value: str) -> None:
        ...

    def __init__(self, category: str, check_id: str) -> None:
        ...


class ExcludeFromCodeCoverageAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def justification(self) -> str:
        """Gets or sets the justification for excluding the member from code coverage."""
        ...

    @justification.setter
    def justification(self, value: str) -> None:
        ...

    def __init__(self) -> None:
        ...


class ConstantExpectedAttribute(System.Attribute):
    """Indicates that the specified method parameter expects a constant."""

    @property
    def min(self) -> System.Object:
        """Indicates the minimum bound of the expected constant, inclusive."""
        ...

    @min.setter
    def min(self, value: System.Object) -> None:
        ...

    @property
    def max(self) -> System.Object:
        """Indicates the maximum bound of the expected constant, inclusive."""
        ...

    @max.setter
    def max(self, value: System.Object) -> None:
        ...


class UnscopedRefAttribute(System.Attribute):
    """Used to indicate a byref escapes and is not scoped."""

    def __init__(self) -> None:
        """Initializes a new instance of the UnscopedRefAttribute class."""
        ...


