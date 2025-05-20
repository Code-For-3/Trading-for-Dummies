from typing import overload
from enum import Enum
import datetime
import typing
import warnings

import System
import System.Runtime
import System.Runtime.ConstrainedExecution
import System.Threading


class AmbiguousImplementationException(System.Exception):
    """This class has no documentation."""

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, message: str) -> None:
        ...

    @overload
    def __init__(self, message: str, inner_exception: System.Exception) -> None:
        ...


class GCLargeObjectHeapCompactionMode(Enum):
    """This class has no documentation."""

    DEFAULT = 1

    COMPACT_ONCE = 2


class GCLatencyMode(Enum):
    """This class has no documentation."""

    BATCH = 0

    INTERACTIVE = 1

    LOW_LATENCY = 2

    SUSTAINED_LOW_LATENCY = 3

    NO_GC_REGION = 4


class GCSettings(System.Object):
    """This class has no documentation."""

    latency_mode: System.Runtime.GCLatencyMode

    large_object_heap_compaction_mode: System.Runtime.GCLargeObjectHeapCompactionMode

    IS_SERVER_GC: bool


class MemoryFailPoint(System.Runtime.ConstrainedExecution.CriticalFinalizerObject, System.IDisposable):
    """This class has no documentation."""

    def __init__(self, size_in_megabytes: int) -> None:
        ...

    def dispose(self) -> None:
        ...


class JitInfo(System.Object):
    """A static class for getting information about the Just In Time compiler."""

    @staticmethod
    def get_compilation_time(current_thread: bool = False) -> datetime.timedelta:
        """
        Get the amount of time the JIT Compiler has spent compiling methods. If  is true,
        then this value is scoped to the current thread, otherwise, this is a global value.
        
        :param current_thread: Whether the returned value should be specific to the current thread. Default: false
        :returns: The amount of time the JIT Compiler has spent compiling methods.
        """
        ...

    @staticmethod
    def get_compiled_il_bytes(current_thread: bool = False) -> int:
        """
        Get the number of bytes of IL that have been compiled. If  is true,
        then this value is scoped to the current thread, otherwise, this is a global value.
        
        :param current_thread: Whether the returned value should be specific to the current thread. Default: false
        :returns: The number of bytes of IL the JIT has compiled.
        """
        ...

    @staticmethod
    def get_compiled_method_count(current_thread: bool = False) -> int:
        """
        Get the number of methods that have been compiled. If  is true,
        then this value is scoped to the current thread, otherwise, this is a global value.
        
        :param current_thread: Whether the returned value should be specific to the current thread. Default: false
        :returns: The number of methods the JIT has compiled.
        """
        ...


class AssemblyTargetedPatchBandAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def targeted_patch_band(self) -> str:
        ...

    def __init__(self, targeted_patch_band: str) -> None:
        ...


class TargetedPatchingOptOutAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def reason(self) -> str:
        ...

    def __init__(self, reason: str) -> None:
        ...


class ProfileOptimization(System.Object):
    """This class has no documentation."""

    @staticmethod
    def set_profile_root(directory_path: str) -> None:
        ...

    @staticmethod
    def start_profile(profile: str) -> None:
        ...


class ControlledExecution(System.Object):
    """This class has no documentation."""

    @staticmethod
    def run(action: typing.Callable[[], None], cancellation_token: System.Threading.CancellationToken) -> None:
        """Obsoletions.ControlledExecutionRunMessage"""
        warnings.warn("Obsoletions.ControlledExecutionRunMessage", DeprecationWarning)


