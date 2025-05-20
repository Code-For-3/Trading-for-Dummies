from typing import overload
from enum import Enum
import typing

import System
import System.ComponentModel.DataAnnotations.Schema


class ComplexTypeAttribute(System.Attribute):
    """
    Denotes that the class is a complex type.
        Complex types are non-scalar properties of entity types that enable scalar properties to be organized within
        entities.
        Complex types do not have keys and cannot be managed by the Entity Framework apart from the parent object.
    """


class ForeignKeyAttribute(System.Attribute):
    """
    Denotes a property used as a foreign key in a relationship.
        The annotation may be placed on the foreign key property and specify the associated navigation property name,
        or placed on a navigation property and specify the associated foreign key name.
    """

    @property
    def name(self) -> str:
        """
        If placed on a foreign key property, the name of the associated navigation property.
            If placed on a navigation property, the name of the associated foreign key(s).
        """
        ...

    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of the ForeignKeyAttribute class.
        
        :param name: If placed on a foreign key property, the name of the associated navigation property.     If placed on a navigation property, the name of the associated foreign key(s).     If a navigation property has multiple foreign keys, a comma separated list should be supplied.
        """
        ...


class DatabaseGeneratedOption(Enum):
    """The pattern used to generate values for a property in the database."""

    NONE = 0
    """The database does not generate values."""

    IDENTITY = 1
    """The database generates a value when a row is inserted."""

    COMPUTED = 2
    """The database generates a value when a row is inserted or updated."""


class NotMappedAttribute(System.Attribute):
    """Denotes that a property or class should be excluded from database mapping."""


class ColumnAttribute(System.Attribute):
    """Specifies the database column that a property is mapped to."""

    @property
    def name(self) -> str:
        """The name of the column the property is mapped to."""
        ...

    @property
    def order(self) -> int:
        """The zero-based order of the column the property is mapped to."""
        ...

    @order.setter
    def order(self, value: int) -> None:
        ...

    @property
    def type_name(self) -> str:
        """The database provider specific data type of the column the property is mapped to."""
        ...

    @type_name.setter
    def type_name(self, value: str) -> None:
        ...

    @overload
    def __init__(self) -> None:
        """Initializes a new instance of the ColumnAttribute class."""
        ...

    @overload
    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of the ColumnAttribute class.
        
        :param name: The name of the column the property is mapped to.
        """
        ...


class DatabaseGeneratedAttribute(System.Attribute):
    """Specifies how the database generates values for a property."""

    @property
    def database_generated_option(self) -> System.ComponentModel.DataAnnotations.Schema.DatabaseGeneratedOption:
        """The pattern used to generate values for the property in the database."""
        ...

    def __init__(self, database_generated_option: System.ComponentModel.DataAnnotations.Schema.DatabaseGeneratedOption) -> None:
        """
        Initializes a new instance of the DatabaseGeneratedAttribute class.
        
        :param database_generated_option: The pattern used to generate values for the property in the database.
        """
        ...


class InversePropertyAttribute(System.Attribute):
    """Specifies the inverse of a navigation property that represents the other end of the same relationship."""

    @property
    def property(self) -> str:
        """The navigation property representing the other end of the same relationship."""
        ...

    def __init__(self, property: str) -> None:
        """
        Initializes a new instance of the InversePropertyAttribute class.
        
        :param property: The navigation property representing the other end of the same relationship.
        """
        ...


class TableAttribute(System.Attribute):
    """Specifies the database table that a class is mapped to."""

    @property
    def name(self) -> str:
        """The name of the table the class is mapped to."""
        ...

    @property
    def schema(self) -> str:
        """The schema of the table the class is mapped to."""
        ...

    @schema.setter
    def schema(self, value: str) -> None:
        ...

    def __init__(self, name: str) -> None:
        """
        Initializes a new instance of the TableAttribute class.
        
        :param name: The name of the table the class is mapped to.
        """
        ...


