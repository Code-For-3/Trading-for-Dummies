from typing import overload
from enum import Enum
import typing

import System
import System.CodeDom.Compiler
import System.IO
import System.Text
import System.Threading
import System.Threading.Tasks


class GeneratedCodeAttribute(System.Attribute):
    """This class has no documentation."""

    @property
    def tool(self) -> str:
        ...

    @property
    def version(self) -> str:
        ...

    def __init__(self, tool: str, version: str) -> None:
        ...


class IndentedTextWriter(System.IO.TextWriter):
    """This class has no documentation."""

    DEFAULT_TAB_STRING: str = "    "

    @property
    def encoding(self) -> System.Text.Encoding:
        ...

    @property
    def new_line(self) -> str:
        ...

    @new_line.setter
    def new_line(self, value: str) -> None:
        ...

    @property
    def indent(self) -> int:
        ...

    @indent.setter
    def indent(self, value: int) -> None:
        ...

    @property
    def inner_writer(self) -> System.IO.TextWriter:
        ...

    @overload
    def __init__(self, writer: System.IO.TextWriter) -> None:
        ...

    @overload
    def __init__(self, writer: System.IO.TextWriter, tab_string: str) -> None:
        ...

    def close(self) -> None:
        ...

    def dispose_async(self) -> System.Threading.Tasks.ValueTask:
        ...

    def flush(self) -> None:
        ...

    @overload
    def flush_async(self) -> System.Threading.Tasks.Task:
        ...

    @overload
    def flush_async(self, cancellation_token: System.Threading.CancellationToken) -> System.Threading.Tasks.Task:
        """
        Clears all buffers for this IndentedTextWriter asynchronously and causes any buffered data to be
        written to the underlying device.
        
        :param cancellation_token: The CancellationToken to monitor for cancellation requests.
        :returns: A Task representing the asynchronous flush operation.
        """
        ...

    def output_tabs(self) -> None:
        """This method is protected."""
        ...

    def output_tabs_async(self) -> System.Threading.Tasks.Task:
        """
        Asynchronously outputs tabs to the underlying TextWriter based on the current Indent.
        
        This method is protected.
        
        :returns: A Task representing the asynchronous operation.
        """
        ...

    @overload
    def write(self, value: typing.Any) -> None:
        ...

    @overload
    def write(self, format: str, arg_0: typing.Any) -> None:
        ...

    @overload
    def write(self, format: str, arg_0: typing.Any, arg_1: typing.Any) -> None:
        ...

    @overload
    def write(self, s: str) -> None:
        ...

    @overload
    def write(self, value: bool) -> None:
        ...

    @overload
    def write(self, value: str) -> None:
        ...

    @overload
    def write(self, buffer: typing.List[str]) -> None:
        ...

    @overload
    def write(self, buffer: typing.List[str], index: int, count: int) -> None:
        ...

    @overload
    def write(self, value: float) -> None:
        ...

    @overload
    def write(self, value: int) -> None:
        ...

    @overload
    def write(self, format: str, *arg: typing.Union[System.Object, typing.Iterable[System.Object]]) -> None:
        ...

    @overload
    def write_async(self, value: str) -> System.Threading.Tasks.Task:
        """
        Asynchronously writes the specified char to the underlying TextWriter, inserting
        tabs at the start of every line.
        
        :param value: The char to write.
        :returns: A Task representing the asynchronous operation.
        """
        ...

    @overload
    def write_async(self, buffer: typing.List[str], index: int, count: int) -> System.Threading.Tasks.Task:
        """
        Asynchronously writes the specified number of chars from the specified buffer
        to the underlying TextWriter, starting at the specified index, and outputting tabs at the
        start of every new line.
        
        :param buffer: The array to write from.
        :param index: Index in the array to stort writing at.
        :param count: The number of characters to write.
        :returns: A Task representing the asynchronous operation.
        """
        ...

    @overload
    def write_async(self, buffer: System.ReadOnlyMemory[str], cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        """
        Asynchronously writes the specified characters to the underlying TextWriter, inserting tabs at the
        start of every line.
        
        :param buffer: The characters to write.
        :param cancellation_token: Token for canceling the operation.
        :returns: A Task representing the asynchronous operation.
        """
        ...

    @overload
    def write_async(self, value: System.Text.StringBuilder, cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        """
        Asynchronously writes the contents of the specified StringBuilder to the underlying TextWriter, inserting tabs at the
        start of every line.
        
        :param value: The text to write.
        :param cancellation_token: Token for canceling the operation.
        :returns: A Task representing the asynchronous operation.
        """
        ...

    @overload
    def write_line(self, value: typing.Any) -> None:
        ...

    @overload
    def write_line(self, format: str, arg_0: typing.Any) -> None:
        ...

    @overload
    def write_line(self, format: str, arg_0: typing.Any, arg_1: typing.Any) -> None:
        ...

    @overload
    def write_line(self, s: str) -> None:
        ...

    @overload
    def write_line(self) -> None:
        ...

    @overload
    def write_line(self, value: bool) -> None:
        ...

    @overload
    def write_line(self, value: str) -> None:
        ...

    @overload
    def write_line(self, buffer: typing.List[str]) -> None:
        ...

    @overload
    def write_line(self, buffer: typing.List[str], index: int, count: int) -> None:
        ...

    @overload
    def write_line(self, value: float) -> None:
        ...

    @overload
    def write_line(self, value: int) -> None:
        ...

    @overload
    def write_line(self, format: str, *arg: typing.Union[System.Object, typing.Iterable[System.Object]]) -> None:
        ...

    @overload
    def write_line_async(self) -> System.Threading.Tasks.Task:
        ...

    @overload
    def write_line_async(self, value: str) -> System.Threading.Tasks.Task:
        """
        Asynchronously writes the specified char to the underlying TextWriter followed by a line terminator, inserting tabs
        at the start of every line.
        
        :param value: The character to write.
        :returns: A Task representing the asynchronous operation.
        """
        ...

    @overload
    def write_line_async(self, buffer: typing.List[str], index: int, count: int) -> System.Threading.Tasks.Task:
        """
        Asynchronously writes the specified number of characters from the specified buffer followed by a line terminator,
        to the underlying TextWriter, starting at the specified index within the buffer, inserting tabs at the start of every line.
        
        :param buffer: The buffer containing characters to write.
        :param index: The index within the buffer to start writing at.
        :param count: The number of characters to write.
        :returns: A Task representing the asynchronous operation.
        """
        ...

    @overload
    def write_line_async(self, buffer: System.ReadOnlyMemory[str], cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        """
        Asynchronously writes the specified characters followed by a line terminator to the underlying TextWriter, inserting
        tabs at the start of every line.
        
        :param buffer: The characters to write.
        :param cancellation_token: Token for canceling the operation.
        :returns: A Task representing the asynchronous operation.
        """
        ...

    @overload
    def write_line_async(self, value: System.Text.StringBuilder, cancellation_token: System.Threading.CancellationToken = ...) -> System.Threading.Tasks.Task:
        """
        Asynchronously writes the contents of the specified StringBuilder followed by a line terminator to the
        underlying TextWriter, inserting tabs at the start of every line.
        
        :param value: The text to write.
        :param cancellation_token: Token for canceling the operation.
        :returns: A Task representing the asynchronous operation.
        """
        ...

    def write_line_no_tabs(self, s: str) -> None:
        ...

    def write_line_no_tabs_async(self, s: str) -> System.Threading.Tasks.Task:
        """
        Asynchronously writes the specified string to the underlying TextWriter without inserting tabs.
        
        :param s: The string to write.
        :returns: A Task representing the asynchronous operation.
        """
        ...


