from typing import overload
from enum import Enum
import typing

import System
import System.Runtime.Remoting


class ObjectHandle(System.MarshalByRefObject):
    """This class has no documentation."""

    def __init__(self, o: typing.Any) -> None:
        ...

    def unwrap(self) -> System.Object:
        ...


