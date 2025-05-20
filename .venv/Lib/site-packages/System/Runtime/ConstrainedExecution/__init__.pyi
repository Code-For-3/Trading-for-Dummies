from typing import overload
from enum import Enum
import abc

import System
import System.Runtime.ConstrainedExecution


class CriticalFinalizerObject(System.Object, metaclass=abc.ABCMeta):
    """Ensures that all finalization code in derived classes is marked as critical."""

    def __init__(self) -> None:
        """This method is protected."""
        ...


class PrePrepareMethodAttribute(System.Attribute):
    """Obsoletions.ConstrainedExecutionRegionMessage"""

    def __init__(self) -> None:
        ...


class Cer(Enum):
    """Obsoletions.ConstrainedExecutionRegionMessage"""

    NONE = 0

    MAY_FAIL = 1

    SUCCESS = 2


class Consistency(Enum):
    """Obsoletions.ConstrainedExecutionRegionMessage"""

    MAY_CORRUPT_PROCESS = 0

    MAY_CORRUPT_APP_DOMAIN = 1

    MAY_CORRUPT_INSTANCE = 2

    WILL_NOT_CORRUPT_STATE = 3


class ReliabilityContractAttribute(System.Attribute):
    """
    Defines a contract for reliability between the author of some code, and the developers who have a dependency on that code.
    
    Obsoletions.ConstrainedExecutionRegionMessage
    """

    @property
    def consistency_guarantee(self) -> System.Runtime.ConstrainedExecution.Consistency:
        ...

    @property
    def cer(self) -> System.Runtime.ConstrainedExecution.Cer:
        ...

    def __init__(self, consistency_guarantee: System.Runtime.ConstrainedExecution.Consistency, cer: System.Runtime.ConstrainedExecution.Cer) -> None:
        ...


