from typing import overload
from enum import Enum
import abc
import datetime
import typing
import warnings

import System
import System.Collections
import System.Globalization
import System.Reflection
import System.Runtime.Serialization
import System.Text

System_Globalization_SortVersion = typing.Any


class CalendarAlgorithmType(Enum):
    """This class has no documentation."""

    UNKNOWN = 0

    SOLAR_CALENDAR = 1

    LUNAR_CALENDAR = 2

    LUNISOLAR_CALENDAR = 3


class CalendarWeekRule(Enum):
    """This class has no documentation."""

    FIRST_DAY = 0

    FIRST_FULL_WEEK = 1

    FIRST_FOUR_DAY_WEEK = 2


class Calendar(System.Object, System.ICloneable, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    def min_supported_date_time(self) -> datetime.datetime:
        ...

    @property
    def max_supported_date_time(self) -> datetime.datetime:
        ...

    @property
    def algorithm_type(self) -> System.Globalization.CalendarAlgorithmType:
        ...

    @property
    def is_read_only(self) -> bool:
        ...

    CURRENT_ERA: int = 0

    @property
    @abc.abstractmethod
    def eras(self) -> typing.List[int]:
        """Get the list of era values."""
        ...

    @property
    def days_in_year_before_min_supported_year(self) -> int:
        """This property is protected."""
        ...

    @property
    def two_digit_year_max(self) -> int:
        """
        Returns and assigns the maximum value to represent a two digit year.
        This value is the upper boundary of a 100 year range that allows a
        two digit year to be properly translated to a four digit year.
        For example, if 2049 is the upper boundary, then a two digit value of
        30 should be interpreted as 1950 while a two digit value of 49 should
        be interpreted as 2049.  In this example, the 100 year range would be
        from 1950-2049.  See ToFourDigitYear().
        """
        ...

    @two_digit_year_max.setter
    def two_digit_year_max(self, value: int) -> None:
        ...

    def __init__(self) -> None:
        """This method is protected."""
        ...

    def add_days(self, time: typing.Union[datetime.datetime, datetime.date], days: int) -> datetime.datetime:
        """
        Returns the DateTime resulting from adding a fractional number of
        days to the specified DateTime. The result is computed by rounding the
        fractional number of days given by value to the nearest
        millisecond, and adding that interval to the specified DateTime. The
        value argument is permitted to be negative.
        """
        ...

    def add_hours(self, time: typing.Union[datetime.datetime, datetime.date], hours: int) -> datetime.datetime:
        """
        Returns the DateTime resulting from adding a fractional number of
        hours to the specified DateTime. The result is computed by rounding the
        fractional number of hours given by value to the nearest
        millisecond, and adding that interval to the specified DateTime. The
        value argument is permitted to be negative.
        """
        ...

    def add_milliseconds(self, time: typing.Union[datetime.datetime, datetime.date], milliseconds: float) -> datetime.datetime:
        """
        Returns the DateTime resulting from adding the given number of
        milliseconds to the specified DateTime. The result is computed by rounding
        the number of milliseconds given by value to the nearest integer,
        and adding that interval to the specified DateTime. The value
        argument is permitted to be negative.
        """
        ...

    def add_minutes(self, time: typing.Union[datetime.datetime, datetime.date], minutes: int) -> datetime.datetime:
        """
        Returns the DateTime resulting from adding a fractional number of
        minutes to the specified DateTime. The result is computed by rounding the
        fractional number of minutes given by value to the nearest
        millisecond, and adding that interval to the specified DateTime. The
        value argument is permitted to be negative.
        """
        ...

    def add_months(self, time: typing.Union[datetime.datetime, datetime.date], months: int) -> datetime.datetime:
        """
        Returns the DateTime resulting from adding the given number of
        months to the specified DateTime. The result is computed by incrementing
        (or decrementing) the year and month parts of the specified DateTime by
        value months, and, if required, adjusting the day part of the
        resulting date downwards to the last day of the resulting month in the
        resulting year. The time-of-day part of the result is the same as the
        time-of-day part of the specified DateTime.
        
        In more precise terms, considering the specified DateTime to be of the
        form y / m / d + t, where y is the
        year, m is the month, d is the day, and t is the
        time-of-day, the result is y1 / m1 / d1 + t,
        where y1 and m1 are computed by adding value months
        to y and m, and d1 is the largest value less than
        or equal to d that denotes a valid day in month m1 of year
        y1.
        """
        ...

    def add_seconds(self, time: typing.Union[datetime.datetime, datetime.date], seconds: int) -> datetime.datetime:
        """
        Returns the DateTime resulting from adding a number of
        seconds to the specified DateTime. The result is computed by rounding the
        fractional number of seconds given by value to the nearest
        millisecond, and adding that interval to the specified DateTime. The
        value argument is permitted to be negative.
        """
        ...

    def add_weeks(self, time: typing.Union[datetime.datetime, datetime.date], weeks: int) -> datetime.datetime:
        ...

    def add_years(self, time: typing.Union[datetime.datetime, datetime.date], years: int) -> datetime.datetime:
        """
        Returns the DateTime resulting from adding the given number of
        years to the specified DateTime. The result is computed by incrementing
        (or decrementing) the year part of the specified DateTime by value
        years. If the month and day of the specified DateTime is 2/29, and if the
        resulting year is not a leap year, the month and day of the resulting
        DateTime becomes 2/28. Otherwise, the month, day, and time-of-day
        parts of the result are the same as those of the specified DateTime.
        """
        ...

    def clone(self) -> System.Object:
        ...

    def get_day_of_month(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        """
        Returns the day-of-month part of the specified DateTime. The returned
        value is an integer between 1 and 31.
        """
        ...

    def get_day_of_week(self, time: typing.Union[datetime.datetime, datetime.date]) -> System.DayOfWeek:
        """
        Returns the day-of-week part of the specified DateTime. The returned value
        is an integer between 0 and 6, where 0 indicates Sunday, 1 indicates
        Monday, 2 indicates Tuesday, 3 indicates Wednesday, 4 indicates
        Thursday, 5 indicates Friday, and 6 indicates Saturday.
        """
        ...

    def get_day_of_year(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        """
        Returns the day-of-year part of the specified DateTime. The returned value
        is an integer between 1 and 366.
        """
        ...

    @overload
    def get_days_in_month(self, year: int, month: int) -> int:
        """
        Returns the number of days in the month given by the year and
        month arguments.
        """
        ...

    @overload
    def get_days_in_month(self, year: int, month: int, era: int) -> int:
        """
        Returns the number of days in the month given by the year and
        month arguments for the specified era.
        """
        ...

    @overload
    def get_days_in_year(self, year: int) -> int:
        """
        Returns the number of days in the year given by the year argument
        for the current era.
        """
        ...

    @overload
    def get_days_in_year(self, year: int, era: int) -> int:
        """
        Returns the number of days in the year given by the year argument
        for the current era.
        """
        ...

    def get_era(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        """Returns the era for the specified DateTime value."""
        ...

    def get_hour(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    @overload
    def get_leap_month(self, year: int) -> int:
        """
        Returns  the leap month in a calendar year of the current era.
        This method returns 0 if this calendar does not have leap month,
        or this year is not a leap year.
        """
        ...

    @overload
    def get_leap_month(self, year: int, era: int) -> int:
        """
        Returns  the leap month in a calendar year of the specified era.
        This method returns 0 if this calendar does not have leap month,
        or this year is not a leap year.
        """
        ...

    def get_milliseconds(self, time: typing.Union[datetime.datetime, datetime.date]) -> float:
        ...

    def get_minute(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_month(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    @overload
    def get_months_in_year(self, year: int) -> int:
        ...

    @overload
    def get_months_in_year(self, year: int, era: int) -> int:
        ...

    def get_second(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_week_of_year(self, time: typing.Union[datetime.datetime, datetime.date], rule: System.Globalization.CalendarWeekRule, first_day_of_week: System.DayOfWeek) -> int:
        """
        Returns the week of year for the specified DateTime. The returned value is an
        integer between 1 and 53.
        """
        ...

    def get_year(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        """
        Returns the year part of the specified DateTime. The returned value is an
        integer between 1 and 9999.
        """
        ...

    @overload
    def is_leap_day(self, year: int, month: int, day: int) -> bool:
        """
        Checks whether a given day in the current era is a leap day.
        This method returns true if the date is a leap day, or false if not.
        """
        ...

    @overload
    def is_leap_day(self, year: int, month: int, day: int, era: int) -> bool:
        """
        Checks whether a given day in the specified era is a leap day.
        This method returns true if the date is a leap day, or false if not.
        """
        ...

    @overload
    def is_leap_month(self, year: int, month: int) -> bool:
        """
        Checks whether a given month in the current era is a leap month.
        This method returns true if month is a leap month, or false if not.
        """
        ...

    @overload
    def is_leap_month(self, year: int, month: int, era: int) -> bool:
        """
        Checks whether a given month in the specified era is a leap month. This method returns true if
        month is a leap month, or false if not.
        """
        ...

    @overload
    def is_leap_year(self, year: int) -> bool:
        """
        Checks whether a given year in the current era is a leap year.
        This method returns true if year is a leap year, or false if not.
        """
        ...

    @overload
    def is_leap_year(self, year: int, era: int) -> bool:
        """
        Checks whether a given year in the specified era is a leap year.
        This method returns true if year is a leap year, or false if not.
        """
        ...

    @staticmethod
    def read_only(calendar: System.Globalization.Calendar) -> System.Globalization.Calendar:
        ...

    @overload
    def to_date_time(self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int) -> datetime.datetime:
        """
        Returns the date and time converted to a DateTime value.
        Throws an exception if the n-tuple is invalid.
        """
        ...

    @overload
    def to_date_time(self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, era: int) -> datetime.datetime:
        """
        Returns the date and time converted to a DateTime value.
        Throws an exception if the n-tuple is invalid.
        """
        ...

    def to_four_digit_year(self, year: int) -> int:
        """
        Converts the year value to the appropriate century by using the
        TwoDigitYearMax property.  For example, if the TwoDigitYearMax value is 2049,
        then a two digit value of 50 will get converted to 1950 while a two digit
        value of 49 will get converted to 2049.
        """
        ...


class EastAsianLunisolarCalendar(System.Globalization.Calendar, metaclass=abc.ABCMeta):
    """This class has no documentation."""

    @property
    def algorithm_type(self) -> System.Globalization.CalendarAlgorithmType:
        ...

    @property
    def two_digit_year_max(self) -> int:
        ...

    @two_digit_year_max.setter
    def two_digit_year_max(self, value: int) -> None:
        ...

    def add_months(self, time: typing.Union[datetime.datetime, datetime.date], months: int) -> datetime.datetime:
        """
        Returns the DateTime resulting from adding the given number of
        months to the specified DateTime. The result is computed by incrementing
        (or decrementing) the year and month parts of the specified DateTime by
        value months, and, if required, adjusting the day part of the
        resulting date downwards to the last day of the resulting month in the
        resulting year. The time-of-day part of the result is the same as the
        time-of-day part of the specified DateTime.
        """
        ...

    def add_years(self, time: typing.Union[datetime.datetime, datetime.date], years: int) -> datetime.datetime:
        ...

    def get_celestial_stem(self, sexagenary_year: int) -> int:
        """
        Return the celestial year from the 60-year cycle.
        The returned value is from 1 ~ 10.
        """
        ...

    def get_day_of_month(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        """
        Returns the day-of-month part of the specified DateTime. The returned
        value is an integer between 1 and 29 or 30.
        """
        ...

    def get_day_of_week(self, time: typing.Union[datetime.datetime, datetime.date]) -> System.DayOfWeek:
        """
        Returns the day-of-week part of the specified DateTime. The returned value
        is an integer between 0 and 6, where 0 indicates Sunday, 1 indicates
        Monday, 2 indicates Tuesday, 3 indicates Wednesday, 4 indicates
        Thursday, 5 indicates Friday, and 6 indicates Saturday.
        """
        ...

    def get_day_of_year(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        """
        Returns the day-of-year part of the specified DateTime. The returned value
        is an integer between 1 and [354|355 |383|384].
        """
        ...

    def get_days_in_month(self, year: int, month: int, era: int) -> int:
        """
        Returns the number of days in the month given by the year and
        month arguments.
        """
        ...

    def get_days_in_year(self, year: int, era: int) -> int:
        """Returns the number of days in the year given by the year argument for the current era."""
        ...

    def get_leap_month(self, year: int, era: int) -> int:
        """
        Returns  the leap month in a calendar year of the specified era. This method returns 0
        if this year is not a leap year.
        """
        ...

    def get_month(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        """
        Returns the month part of the specified DateTime.
        The returned value is an integer between 1 and 13.
        """
        ...

    def get_months_in_year(self, year: int, era: int) -> int:
        """Returns the number of months in the specified year and era."""
        ...

    def get_sexagenary_year(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        """Return the year number in the 60-year cycle."""
        ...

    def get_terrestrial_branch(self, sexagenary_year: int) -> int:
        """
        Return the Terrestial Branch from the 60-year cycle.
        The returned value is from 1 ~ 12.
        """
        ...

    def get_year(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        """
        Returns the year part of the specified DateTime.
        The returned value is an integer between 1 and MaxCalendarYear.
        """
        ...

    def is_leap_day(self, year: int, month: int, day: int, era: int) -> bool:
        """
        Checks whether a given day in the specified era is a leap day.
        This method returns true if the date is a leap day, or false if not.
        """
        ...

    def is_leap_month(self, year: int, month: int, era: int) -> bool:
        """
        Checks whether a given month in the specified era is a leap month.
        This method returns true if month is a leap month, or false if not.
        """
        ...

    def is_leap_year(self, year: int, era: int) -> bool:
        """
        Checks whether a given year in the specified era is a leap year.
        This method returns true if year is a leap year, or false if not.
        """
        ...

    def to_date_time(self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, era: int) -> datetime.datetime:
        """
        Returns the date and time converted to a DateTime value.
        Throws an exception if the n-tuple is invalid.
        """
        ...

    def to_four_digit_year(self, year: int) -> int:
        ...


class TaiwanLunisolarCalendar(System.Globalization.EastAsianLunisolarCalendar):
    """This class has no documentation."""

    @property
    def min_supported_date_time(self) -> datetime.datetime:
        ...

    @property
    def max_supported_date_time(self) -> datetime.datetime:
        ...

    @property
    def days_in_year_before_min_supported_year(self) -> int:
        """This property is protected."""
        ...

    @property
    def eras(self) -> typing.List[int]:
        ...

    def __init__(self) -> None:
        ...

    def get_era(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...


class PersianCalendar(System.Globalization.Calendar):
    """
    Modern Persian calendar is a solar observation based calendar. Each new year begins on the day when the vernal equinox occurs before noon.
    The epoch is the date of the vernal equinox prior to the epoch of the Islamic calendar (March 19, 622 Julian or March 22, 622 Gregorian)
    There is no Persian year 0. Ordinary years have 365 days. Leap years have 366 days with the last month (Esfand) gaining the extra day.
    """

    PERSIAN_ERA: int = 1

    @property
    def min_supported_date_time(self) -> datetime.datetime:
        ...

    @property
    def max_supported_date_time(self) -> datetime.datetime:
        ...

    @property
    def algorithm_type(self) -> System.Globalization.CalendarAlgorithmType:
        ...

    @property
    def eras(self) -> typing.List[int]:
        ...

    @property
    def two_digit_year_max(self) -> int:
        ...

    @two_digit_year_max.setter
    def two_digit_year_max(self, value: int) -> None:
        ...

    def __init__(self) -> None:
        ...

    def add_months(self, time: typing.Union[datetime.datetime, datetime.date], months: int) -> datetime.datetime:
        ...

    def add_years(self, time: typing.Union[datetime.datetime, datetime.date], years: int) -> datetime.datetime:
        ...

    def get_day_of_month(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_day_of_week(self, time: typing.Union[datetime.datetime, datetime.date]) -> System.DayOfWeek:
        ...

    def get_day_of_year(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_days_in_month(self, year: int, month: int, era: int) -> int:
        ...

    def get_days_in_year(self, year: int, era: int) -> int:
        ...

    def get_era(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_leap_month(self, year: int, era: int) -> int:
        ...

    def get_month(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_months_in_year(self, year: int, era: int) -> int:
        ...

    def get_year(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def is_leap_day(self, year: int, month: int, day: int, era: int) -> bool:
        ...

    def is_leap_month(self, year: int, month: int, era: int) -> bool:
        ...

    def is_leap_year(self, year: int, era: int) -> bool:
        ...

    def to_date_time(self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, era: int) -> datetime.datetime:
        ...

    def to_four_digit_year(self, year: int) -> int:
        ...


class HijriCalendar(System.Globalization.Calendar):
    """This class has no documentation."""

    HIJRI_ERA: int = 1

    @property
    def min_supported_date_time(self) -> datetime.datetime:
        ...

    @property
    def max_supported_date_time(self) -> datetime.datetime:
        ...

    @property
    def algorithm_type(self) -> System.Globalization.CalendarAlgorithmType:
        ...

    @property
    def days_in_year_before_min_supported_year(self) -> int:
        """This property is protected."""
        ...

    @property
    def hijri_adjustment(self) -> int:
        ...

    @hijri_adjustment.setter
    def hijri_adjustment(self, value: int) -> None:
        ...

    @property
    def eras(self) -> typing.List[int]:
        ...

    @property
    def two_digit_year_max(self) -> int:
        ...

    @two_digit_year_max.setter
    def two_digit_year_max(self, value: int) -> None:
        ...

    def __init__(self) -> None:
        ...

    def add_months(self, time: typing.Union[datetime.datetime, datetime.date], months: int) -> datetime.datetime:
        ...

    def add_years(self, time: typing.Union[datetime.datetime, datetime.date], years: int) -> datetime.datetime:
        ...

    def get_day_of_month(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_day_of_week(self, time: typing.Union[datetime.datetime, datetime.date]) -> System.DayOfWeek:
        ...

    def get_day_of_year(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_days_in_month(self, year: int, month: int, era: int) -> int:
        ...

    def get_days_in_year(self, year: int, era: int) -> int:
        ...

    def get_era(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_leap_month(self, year: int, era: int) -> int:
        ...

    def get_month(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_months_in_year(self, year: int, era: int) -> int:
        ...

    def get_year(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def is_leap_day(self, year: int, month: int, day: int, era: int) -> bool:
        ...

    def is_leap_month(self, year: int, month: int, era: int) -> bool:
        ...

    def is_leap_year(self, year: int, era: int) -> bool:
        ...

    def to_date_time(self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, era: int) -> datetime.datetime:
        ...

    def to_four_digit_year(self, year: int) -> int:
        ...


class TimeSpanStyles(Enum):
    """This class has no documentation."""

    NONE = ...

    ASSUME_NEGATIVE = ...


class SortVersion(System.Object, System.IEquatable[System_Globalization_SortVersion]):
    """This class has no documentation."""

    @property
    def full_version(self) -> int:
        ...

    @property
    def sort_id(self) -> System.Guid:
        ...

    def __eq__(self, right: System.Globalization.SortVersion) -> bool:
        ...

    def __init__(self, full_version: int, sort_id: System.Guid) -> None:
        ...

    def __ne__(self, right: System.Globalization.SortVersion) -> bool:
        ...

    @overload
    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def equals(self, other: System.Globalization.SortVersion) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...


class CompareOptions(Enum):
    """Defines the string comparison options to use with CompareInfo."""

    NONE = ...
    """Indicates the default option settings for string comparisons"""

    IGNORE_CASE = ...
    """Indicates that the string comparison must ignore case."""

    IGNORE_NON_SPACE = ...
    """
    Indicates that the string comparison must ignore nonspacing combining characters, such as diacritics.
    The https://go.microsoft.com/fwlink/?linkid=37123 defines combining characters as
    characters that are combined with base characters to produce a new character. Nonspacing combining characters do not
    occupy a spacing position by themselves when rendered.
    """

    IGNORE_SYMBOLS = ...
    """
    Indicates that the string comparison must ignore symbols, such as white-space characters, punctuation, currency symbols,
    the percent sign, mathematical symbols, the ampersand, and so on.
    """

    IGNORE_KANA_TYPE = ...
    """
    Indicates that the string comparison must ignore the Kana type. Kana type refers to Japanese hiragana and katakana characters, which represent phonetic sounds in the Japanese language.
    Hiragana is used for native Japanese expressions and words, while katakana is used for words borrowed from other languages, such as "computer" or "Internet".
    A phonetic sound can be expressed in both hiragana and katakana. If this value is selected, the hiragana character for one sound is considered equal to the katakana character for the same sound.
    """

    IGNORE_WIDTH = ...
    """
    Indicates that the string comparison must ignore the character width. For example, Japanese katakana characters can be written as full-width or half-width.
    If this value is selected, the katakana characters written as full-width are considered equal to the same characters written as half-width.
    """

    NUMERIC_ORDERING = ...
    """
    Indicates that the string comparison must sort sequences of digits (Unicode general category "Nd") based on their numeric value.
    For example, "2" comes before "10". Non-digit characters such as decimal points, minus or plus signs, etc.
    are not considered as part of the sequence and will terminate it. This flag is not valid for indexing
    (such as CompareInfo.IndexOf(string, string, CompareOptions), CompareInfo.IsPrefix(string, string, CompareOptions), etc.).
    """

    ORDINAL_IGNORE_CASE = ...
    """
    String comparison must ignore case, then perform an ordinal comparison. This technique is equivalent to
    converting the string to uppercase using the invariant culture and then performing an ordinal comparison on the result.
    This value cannot be combined with other CompareOptions values and must be used alone.
    """

    STRING_SORT = ...
    """
    Indicates that the string comparison must use the string sort algorithm. In a string sort, the hyphen and the apostrophe,
    as well as other nonalphanumeric symbols, come before alphanumeric characters.
    """

    ORDINAL = ...
    """
    Indicates that the string comparison must use successive Unicode UTF-16 encoded values of the string (code unit by code unit comparison),
    leading to a fast comparison but one that is culture-insensitive. A string starting with a code unit XXXX16 comes before a string starting with YYYY16,
    if XXXX16 is less than YYYY16. This value cannot be combined with other CompareOptions values and must be used alone.
    """


class SortKey(System.Object):
    """Represents the result of mapping a string to its sort key."""

    @property
    def original_string(self) -> str:
        """
        Returns the original string used to create the current instance
        of SortKey.
        """
        ...

    @property
    def key_data(self) -> typing.List[int]:
        """
        Returns a byte array representing the current instance of the
        sort key.
        """
        ...

    @staticmethod
    def compare(sortkey_1: System.Globalization.SortKey, sortkey_2: System.Globalization.SortKey) -> int:
        """
        Compares the two sort keys.  Returns 0 if the two sort keys are
        equal, a number less than 0 if sortkey_1 is less than sortkey_2,
        and a number greater than 0 if sortkey_1 is greater than sortkey_2.
        """
        ...

    def equals(self, value: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    def to_string(self) -> str:
        ...


class CompareInfo(System.Object, System.Runtime.Serialization.IDeserializationCallback):
    """This class implements a set of methods for comparing strings."""

    @property
    def name(self) -> str:
        """
        Returns the name of the culture (well actually, of the sort).
         Very important for providing a non-LCID way of identifying
         what the sort is.
        
         Note that this name isn't dereferenced in case the CompareInfo is a different locale
         which is consistent with the behaviors of earlier versions.  (so if you ask for a sort
         and the locale's changed behavior, then you'll get changed behavior, which is like
         what happens for a version update)
        """
        ...

    @property
    def version(self) -> System.Globalization.SortVersion:
        ...

    @property
    def lcid(self) -> int:
        ...

    @overload
    def compare(self, string_1: str, string_2: str) -> int:
        """
        Compares the two strings with the given options.  Returns 0 if the
        two strings are equal, a number less than 0 if string_1 is less
        than string_2, and a number greater than 0 if string_1 is greater
        than string_2.
        """
        ...

    @overload
    def compare(self, string_1: str, string_2: str, options: System.Globalization.CompareOptions) -> int:
        ...

    @overload
    def compare(self, string_1: str, offset_1: int, length_1: int, string_2: str, offset_2: int, length_2: int) -> int:
        """
        Compares the specified regions of the two strings with the given
        options.
        Returns 0 if the two strings are equal, a number less than 0 if
        string_1 is less than string_2, and a number greater than 0 if
        string_1 is greater than string_2.
        """
        ...

    @overload
    def compare(self, string_1: str, offset_1: int, string_2: str, offset_2: int, options: System.Globalization.CompareOptions) -> int:
        ...

    @overload
    def compare(self, string_1: str, offset_1: int, string_2: str, offset_2: int) -> int:
        ...

    @overload
    def compare(self, string_1: str, offset_1: int, length_1: int, string_2: str, offset_2: int, length_2: int, options: System.Globalization.CompareOptions) -> int:
        ...

    @overload
    def compare(self, string_1: System.ReadOnlySpan[str], string_2: System.ReadOnlySpan[str], options: System.Globalization.CompareOptions = ...) -> int:
        """
        Compares two strings.
        
        :param string_1: The first string to compare.
        :param string_2: The second string to compare.
        :param options: The CompareOptions to use during the comparison.
        :returns: Zero if  and  are equal; or a negative value if  sorts before ; or a positive value if  sorts after .
        """
        ...

    def equals(self, value: typing.Any) -> bool:
        ...

    @staticmethod
    @overload
    def get_compare_info(culture: int, assembly: System.Reflection.Assembly) -> System.Globalization.CompareInfo:
        """
        Get the CompareInfo constructed from the data table in the specified
        assembly for the specified culture.
        Warning: The assembly versioning mechanism is dead!
        """
        ...

    @staticmethod
    @overload
    def get_compare_info(name: str, assembly: System.Reflection.Assembly) -> System.Globalization.CompareInfo:
        """
        Get the CompareInfo constructed from the data table in the specified
        assembly for the specified culture.
        The purpose of this method is to provide version for CompareInfo tables.
        """
        ...

    @staticmethod
    @overload
    def get_compare_info(culture: int) -> System.Globalization.CompareInfo:
        """
        Get the CompareInfo for the specified culture.
        This method is provided for ease of integration with NLS-based software.
        """
        ...

    @staticmethod
    @overload
    def get_compare_info(name: str) -> System.Globalization.CompareInfo:
        """Get the CompareInfo for the specified culture."""
        ...

    @overload
    def get_hash_code(self) -> int:
        ...

    @overload
    def get_hash_code(self, source: str, options: System.Globalization.CompareOptions) -> int:
        """
        This method performs the equivalent of of creating a Sortkey for a string from CompareInfo,
        then generates a randomized hashcode value from the sort key.
        
        The hash code is guaranteed to be the same for string A and B where A.Equals(B) is true and both
        the CompareInfo and the CompareOptions are the same. If two different CompareInfo objects
        treat the string the same way, this implementation will treat them differently (the same way that
        Sortkey does at the moment).
        """
        ...

    @overload
    def get_hash_code(self, source: System.ReadOnlySpan[str], options: System.Globalization.CompareOptions) -> int:
        ...

    @overload
    def get_sort_key(self, source: str, options: System.Globalization.CompareOptions) -> System.Globalization.SortKey:
        """Gets the SortKey for the given string with the given options."""
        ...

    @overload
    def get_sort_key(self, source: str) -> System.Globalization.SortKey:
        ...

    @overload
    def get_sort_key(self, source: System.ReadOnlySpan[str], destination: System.Span[int], options: System.Globalization.CompareOptions = ...) -> int:
        """
        Computes a sort key over the specified input.
        
        :param source: The text over which to compute the sort key.
        :param destination: The buffer into which to write the resulting sort key bytes.
        :param options: The CompareOptions used for computing the sort key.
        :returns: The number of bytes written to .
        """
        ...

    def get_sort_key_length(self, source: System.ReadOnlySpan[str], options: System.Globalization.CompareOptions = ...) -> int:
        """
        Returns the length (in bytes) of the sort key that would be produced from the specified input.
        
        :param source: The text over which to compute the sort key.
        :param options: The CompareOptions used for computing the sort key.
        :returns: The length (in bytes) of the sort key.
        """
        ...

    @overload
    def index_of(self, source: str, value: str) -> int:
        """
        Returns the first index where value is found in string.  The
        search starts from startIndex and ends at endIndex.  Returns -1 if
        the specified value is not found.  If value equals string.Empty,
        startIndex is returned.  Throws IndexOutOfRange if startIndex or
        endIndex is less than zero or greater than the length of string.
        Throws ArgumentException if value (as a string) is null.
        """
        ...

    @overload
    def index_of(self, source: str, value: str, options: System.Globalization.CompareOptions) -> int:
        ...

    @overload
    def index_of(self, source: str, value: str, start_index: int) -> int:
        ...

    @overload
    def index_of(self, source: str, value: str, start_index: int, options: System.Globalization.CompareOptions) -> int:
        ...

    @overload
    def index_of(self, source: str, value: str, start_index: int, count: int) -> int:
        ...

    @overload
    def index_of(self, source: str, value: str, start_index: int, count: int, options: System.Globalization.CompareOptions) -> int:
        ...

    @overload
    def index_of(self, source: System.ReadOnlySpan[str], value: System.ReadOnlySpan[str], options: System.Globalization.CompareOptions = ...) -> int:
        """
        Searches for the first occurrence of a substring within a source string.
        
        :param source: The string to search within.
        :param value: The substring to locate within .
        :param options: The CompareOptions to use during the search.
        :returns: The zero-based index into  where the substring  first appears; or -1 if  cannot be found within .
        """
        ...

    @overload
    def index_of(self, source: System.ReadOnlySpan[str], value: System.ReadOnlySpan[str], options: System.Globalization.CompareOptions, match_length: typing.Optional[int]) -> typing.Tuple[int, int]:
        """
        Searches for the first occurrence of a substring within a source string.
        
        :param source: The string to search within.
        :param value: The substring to locate within .
        :param options: The CompareOptions to use during the search.
        :param match_length: When this method returns, contains the number of characters of  that matched the desired value. This may be different than the length of  if a linguistic comparison is performed. Set to 0 if  is not found within .
        :returns: The zero-based index into  where the substring  first appears; or -1 if  cannot be found within .
        """
        ...

    @overload
    def index_of(self, source: System.ReadOnlySpan[str], value: System.Text.Rune, options: System.Globalization.CompareOptions = ...) -> int:
        """
        Searches for the first occurrence of a Rune within a source string.
        
        :param source: The string to search within.
        :param value: The Rune to locate within .
        :param options: The CompareOptions to use during the search.
        :returns: The zero-based index into  where  first appears; or -1 if  cannot be found within .
        """
        ...

    @overload
    def is_prefix(self, source: str, prefix: str, options: System.Globalization.CompareOptions) -> bool:
        """
        Determines whether prefix is a prefix of string.  If prefix equals
        string.Empty, true is returned.
        """
        ...

    @overload
    def is_prefix(self, source: System.ReadOnlySpan[str], prefix: System.ReadOnlySpan[str], options: System.Globalization.CompareOptions = ...) -> bool:
        """
        Determines whether a string starts with a specific prefix.
        
        :param source: The string to search within.
        :param prefix: The prefix to attempt to match at the start of .
        :param options: The CompareOptions to use during the match.
        :returns: true if  occurs at the start of ; otherwise, false.
        """
        ...

    @overload
    def is_prefix(self, source: System.ReadOnlySpan[str], prefix: System.ReadOnlySpan[str], options: System.Globalization.CompareOptions, match_length: typing.Optional[int]) -> typing.Tuple[bool, int]:
        """
        Determines whether a string starts with a specific prefix.
        
        :param source: The string to search within.
        :param prefix: The prefix to attempt to match at the start of .
        :param options: The CompareOptions to use during the match.
        :param match_length: When this method returns, contains the number of characters of  that matched the desired prefix. This may be different than the length of  if a linguistic comparison is performed. Set to 0 if the prefix did not match.
        :returns: true if  occurs at the start of ; otherwise, false.
        """
        ...

    @overload
    def is_prefix(self, source: str, prefix: str) -> bool:
        ...

    @staticmethod
    @overload
    def is_sortable(ch: str) -> bool:
        ...

    @staticmethod
    @overload
    def is_sortable(text: str) -> bool:
        ...

    @staticmethod
    @overload
    def is_sortable(text: System.ReadOnlySpan[str]) -> bool:
        """
        Indicates whether a specified Unicode string is sortable.
        
        :param text: A string of zero or more Unicode characters.
        :returns: true if  is non-empty and contains only sortable Unicode characters; otherwise, false.
        """
        ...

    @staticmethod
    @overload
    def is_sortable(value: System.Text.Rune) -> bool:
        """
        Indicates whether a specified Rune is sortable.
        
        :param value: A Unicode scalar value.
        :returns: true if  is a sortable Unicode scalar value; otherwise, false.
        """
        ...

    @overload
    def is_suffix(self, source: str, suffix: str, options: System.Globalization.CompareOptions) -> bool:
        """
        Determines whether suffix is a suffix of string.  If suffix equals
        string.Empty, true is returned.
        """
        ...

    @overload
    def is_suffix(self, source: System.ReadOnlySpan[str], suffix: System.ReadOnlySpan[str], options: System.Globalization.CompareOptions = ...) -> bool:
        """
        Determines whether a string ends with a specific suffix.
        
        :param source: The string to search within.
        :param suffix: The suffix to attempt to match at the end of .
        :param options: The CompareOptions to use during the match.
        :returns: true if  occurs at the end of ; otherwise, false.
        """
        ...

    @overload
    def is_suffix(self, source: System.ReadOnlySpan[str], suffix: System.ReadOnlySpan[str], options: System.Globalization.CompareOptions, match_length: typing.Optional[int]) -> typing.Tuple[bool, int]:
        """
        Determines whether a string ends with a specific suffix.
        
        :param source: The string to search within.
        :param suffix: The suffix to attempt to match at the end of .
        :param options: The CompareOptions to use during the match.
        :param match_length: When this method returns, contains the number of characters of  that matched the desired suffix. This may be different than the length of  if a linguistic comparison is performed. Set to 0 if the suffix did not match.
        :returns: true if  occurs at the end of ; otherwise, false.
        """
        ...

    @overload
    def is_suffix(self, source: str, suffix: str) -> bool:
        ...

    @overload
    def last_index_of(self, source: str, value: str) -> int:
        """
        Returns the last index where value is found in string.  The
        search starts from startIndex and ends at endIndex.  Returns -1 if
        the specified value is not found.  If value equals string.Empty,
        endIndex is returned.  Throws IndexOutOfRange if startIndex or
        endIndex is less than zero or greater than the length of string.
        Throws ArgumentException if value (as a string) is null.
        """
        ...

    @overload
    def last_index_of(self, source: str, value: str, options: System.Globalization.CompareOptions) -> int:
        ...

    @overload
    def last_index_of(self, source: str, value: str, start_index: int) -> int:
        ...

    @overload
    def last_index_of(self, source: str, value: str, start_index: int, options: System.Globalization.CompareOptions) -> int:
        ...

    @overload
    def last_index_of(self, source: str, value: str, start_index: int, count: int) -> int:
        ...

    @overload
    def last_index_of(self, source: str, value: str, start_index: int, count: int, options: System.Globalization.CompareOptions) -> int:
        ...

    @overload
    def last_index_of(self, source: System.ReadOnlySpan[str], value: System.ReadOnlySpan[str], options: System.Globalization.CompareOptions = ...) -> int:
        """
        Searches for the last occurrence of a substring within a source string.
        
        :param source: The string to search within.
        :param value: The substring to locate within .
        :param options: The CompareOptions to use during the search.
        :returns: The zero-based index into  where the substring  last appears; or -1 if  cannot be found within .
        """
        ...

    @overload
    def last_index_of(self, source: System.ReadOnlySpan[str], value: System.ReadOnlySpan[str], options: System.Globalization.CompareOptions, match_length: typing.Optional[int]) -> typing.Tuple[int, int]:
        """
        Searches for the last occurrence of a substring within a source string.
        
        :param source: The string to search within.
        :param value: The substring to locate within .
        :param options: The CompareOptions to use during the search.
        :param match_length: When this method returns, contains the number of characters of  that matched the desired value. This may be different than the length of  if a linguistic comparison is performed. Set to 0 if  is not found within .
        :returns: The zero-based index into  where the substring  last appears; or -1 if  cannot be found within .
        """
        ...

    @overload
    def last_index_of(self, source: System.ReadOnlySpan[str], value: System.Text.Rune, options: System.Globalization.CompareOptions = ...) -> int:
        """
        Searches for the last occurrence of a Rune within a source string.
        
        :param source: The string to search within.
        :param value: The Rune to locate within .
        :param options: The CompareOptions to use during the search.
        :returns: The zero-based index into  where  last appears; or -1 if  cannot be found within .
        """
        ...

    def to_string(self) -> str:
        ...


class JapaneseCalendar(System.Globalization.Calendar):
    """
    JapaneseCalendar is based on Gregorian calendar.  The month and day values are the same as
    Gregorian calendar. However, the year value is an offset to the Gregorian
    year based on the era.
    
    This system is adopted by Emperor Meiji in 1868. The year value is counted based on the reign of an emperor,
    and the era begins on the day an emperor ascends the throne and continues until his death.
    The era changes at 12:00AM.
    
    For example, the current era is Reiwa. It started on 2019/5/1 A.D.  Therefore, Gregorian year 2019 is also Reiwa 1st.
    2019/5/1 A.D. is also Reiwa 1st 5/1.
    
    Any date in the year during which era is changed can be reckoned in either era. For example,
    2019/1/1 can be 1/1 Reiwa 1st year or 1/1 Heisei 31st year.
    
    Note:
     The DateTime can be represented by the JapaneseCalendar are limited to two factors:
         1. The min value and max value of DateTime class.
         2. The available era information.
    """

    @property
    def min_supported_date_time(self) -> datetime.datetime:
        ...

    @property
    def max_supported_date_time(self) -> datetime.datetime:
        ...

    @property
    def algorithm_type(self) -> System.Globalization.CalendarAlgorithmType:
        ...

    @property
    def eras(self) -> typing.List[int]:
        ...

    @property
    def two_digit_year_max(self) -> int:
        ...

    @two_digit_year_max.setter
    def two_digit_year_max(self, value: int) -> None:
        ...

    def __init__(self) -> None:
        ...

    def add_months(self, time: typing.Union[datetime.datetime, datetime.date], months: int) -> datetime.datetime:
        ...

    def add_years(self, time: typing.Union[datetime.datetime, datetime.date], years: int) -> datetime.datetime:
        ...

    def get_day_of_month(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_day_of_week(self, time: typing.Union[datetime.datetime, datetime.date]) -> System.DayOfWeek:
        ...

    def get_day_of_year(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_days_in_month(self, year: int, month: int, era: int) -> int:
        ...

    def get_days_in_year(self, year: int, era: int) -> int:
        ...

    def get_era(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_leap_month(self, year: int, era: int) -> int:
        ...

    def get_month(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_months_in_year(self, year: int, era: int) -> int:
        ...

    def get_week_of_year(self, time: typing.Union[datetime.datetime, datetime.date], rule: System.Globalization.CalendarWeekRule, first_day_of_week: System.DayOfWeek) -> int:
        ...

    def get_year(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def is_leap_day(self, year: int, month: int, day: int, era: int) -> bool:
        ...

    def is_leap_month(self, year: int, month: int, era: int) -> bool:
        ...

    def is_leap_year(self, year: int, era: int) -> bool:
        ...

    def to_date_time(self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, era: int) -> datetime.datetime:
        ...

    def to_four_digit_year(self, year: int) -> int:
        """
        For Japanese calendar, four digit year is not used. Few emperors will live for more than one hundred years.
        Therefore, for any two digit number, we just return the original number.
        """
        ...


class RegionInfo(System.Object):
    """
    This class represents settings specified by de jure or de facto
    standards for a particular country/region. In contrast to
    CultureInfo, the RegionInfo does not represent preferences of the
    user and does not depend on the user's language or culture.
    """

    CURRENT_REGION: System.Globalization.RegionInfo
    """This instance provides methods based on the current user settings."""

    @property
    def name(self) -> str:
        """Returns the name of the region (ie: en-US)"""
        ...

    @property
    def english_name(self) -> str:
        """Returns the name of the region in English. (ie: United States)"""
        ...

    @property
    def display_name(self) -> str:
        """
        Returns the display name (localized) of the region. (ie: United States
        if the current UI language is en-US)
        """
        ...

    @property
    def native_name(self) -> str:
        """
        Returns the native name of the region. (ie: Deutschland)
         WARNING: You need a full locale name for this to make sense.
        """
        ...

    @property
    def two_letter_iso_region_name(self) -> str:
        """Returns the two letter ISO region name (ie: US)"""
        ...

    @property
    def three_letter_iso_region_name(self) -> str:
        """Returns the three letter ISO region name (ie: USA)"""
        ...

    @property
    def three_letter_windows_region_name(self) -> str:
        """Returns the three letter windows region name (ie: USA)"""
        ...

    @property
    def is_metric(self) -> bool:
        """Returns true if this region uses the metric measurement system"""
        ...

    @property
    def geo_id(self) -> int:
        ...

    @property
    def currency_english_name(self) -> str:
        """English name for this region's currency, ie: Swiss Franc"""
        ...

    @property
    def currency_native_name(self) -> str:
        """
        Native name for this region's currency, ie: Schweizer Franken
        WARNING: You need a full locale name for this to make sense.
        """
        ...

    @property
    def currency_symbol(self) -> str:
        """Currency Symbol for this locale, ie: Fr. or $"""
        ...

    @property
    def iso_currency_symbol(self) -> str:
        """ISO Currency Symbol for this locale, ie: CHF"""
        ...

    @overload
    def __init__(self, name: str) -> None:
        ...

    @overload
    def __init__(self, culture: int) -> None:
        ...

    def equals(self, value: typing.Any) -> bool:
        """
        Implements Object.Equals().  Returns a boolean indicating whether
        or not object refers to the same RegionInfo as the current instance.
        RegionInfos are considered equal if and only if they have the same name
        (ie: en-US)
        """
        ...

    def get_hash_code(self) -> int:
        ...

    def to_string(self) -> str:
        ...


class UmAlQuraCalendar(System.Globalization.Calendar):
    """This class has no documentation."""

    UM_AL_QURA_ERA: int = 1

    @property
    def min_supported_date_time(self) -> datetime.datetime:
        ...

    @property
    def max_supported_date_time(self) -> datetime.datetime:
        ...

    @property
    def algorithm_type(self) -> System.Globalization.CalendarAlgorithmType:
        ...

    @property
    def days_in_year_before_min_supported_year(self) -> int:
        """This property is protected."""
        ...

    @property
    def eras(self) -> typing.List[int]:
        ...

    @property
    def two_digit_year_max(self) -> int:
        ...

    @two_digit_year_max.setter
    def two_digit_year_max(self, value: int) -> None:
        ...

    def __init__(self) -> None:
        ...

    def add_months(self, time: typing.Union[datetime.datetime, datetime.date], months: int) -> datetime.datetime:
        ...

    def add_years(self, time: typing.Union[datetime.datetime, datetime.date], years: int) -> datetime.datetime:
        ...

    def get_day_of_month(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_day_of_week(self, time: typing.Union[datetime.datetime, datetime.date]) -> System.DayOfWeek:
        ...

    def get_day_of_year(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_days_in_month(self, year: int, month: int, era: int) -> int:
        ...

    def get_days_in_year(self, year: int, era: int) -> int:
        ...

    def get_era(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_leap_month(self, year: int, era: int) -> int:
        ...

    def get_month(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_months_in_year(self, year: int, era: int) -> int:
        ...

    def get_year(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def is_leap_day(self, year: int, month: int, day: int, era: int) -> bool:
        ...

    def is_leap_month(self, year: int, month: int, era: int) -> bool:
        ...

    def is_leap_year(self, year: int, era: int) -> bool:
        ...

    def to_date_time(self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, era: int) -> datetime.datetime:
        ...

    def to_four_digit_year(self, year: int) -> int:
        ...


class TextInfo(System.Object, System.ICloneable, System.Runtime.Serialization.IDeserializationCallback):
    """
    This Class defines behaviors specific to a writing system.
    A writing system is the collection of scripts and orthographic rules
    required to represent a language as text.
    """

    @property
    def ansi_code_page(self) -> int:
        ...

    @property
    def oem_code_page(self) -> int:
        ...

    @property
    def mac_code_page(self) -> int:
        ...

    @property
    def ebcdic_code_page(self) -> int:
        ...

    @property
    def lcid(self) -> int:
        ...

    @property
    def culture_name(self) -> str:
        ...

    @property
    def is_read_only(self) -> bool:
        ...

    @property
    def list_separator(self) -> str:
        """Returns the string used to separate items in a list."""
        ...

    @list_separator.setter
    def list_separator(self, value: str) -> None:
        ...

    @property
    def is_right_to_left(self) -> bool:
        """
        Returns true if the dominant direction of text and UI such as the
        relative position of buttons and scroll bars
        """
        ...

    def clone(self) -> System.Object:
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    @staticmethod
    def read_only(text_info: System.Globalization.TextInfo) -> System.Globalization.TextInfo:
        """
        Create a cloned readonly instance or return the input one if it is
        readonly.
        """
        ...

    @overload
    def to_lower(self, c: str) -> str:
        """
        Converts the character or string to lower case.  Certain locales
        have different casing semantics from the file systems in Win32.
        """
        ...

    @overload
    def to_lower(self, str: str) -> str:
        ...

    def to_string(self) -> str:
        ...

    def to_title_case(self, str: str) -> str:
        """
        Titlecasing refers to a casing practice wherein the first letter of a word is an uppercase letter
        and the rest of the letters are lowercase.  The choice of which words to titlecase in headings
        and titles is dependent on language and local conventions.  For example, "The Merry Wives of Windor"
        is the appropriate titlecasing of that play's name in English, with the word "of" not titlecased.
        In German, however, the title is "Die lustigen Weiber von Windsor," and both "lustigen" and "von"
        are not titlecased.  In French even fewer words are titlecased: "Les joyeuses commeres de Windsor."
        
        Moreover, the determination of what actually constitutes a word is language dependent, and this can
        influence which letter or letters of a "word" are uppercased when titlecasing strings.  For example
        "l'arbre" is considered two words in French, whereas "can't" is considered one word in English.
        """
        ...

    @overload
    def to_upper(self, c: str) -> str:
        """
        Converts the character or string to upper case.  Certain locales
        have different casing semantics from the file systems in Win32.
        """
        ...

    @overload
    def to_upper(self, str: str) -> str:
        ...


class UnicodeCategory(Enum):
    """This class has no documentation."""

    UPPERCASE_LETTER = 0

    LOWERCASE_LETTER = 1

    TITLECASE_LETTER = 2

    MODIFIER_LETTER = 3

    OTHER_LETTER = 4

    NON_SPACING_MARK = 5

    SPACING_COMBINING_MARK = 6

    ENCLOSING_MARK = 7

    DECIMAL_DIGIT_NUMBER = 8

    LETTER_NUMBER = 9

    OTHER_NUMBER = 10

    SPACE_SEPARATOR = 11

    LINE_SEPARATOR = 12

    PARAGRAPH_SEPARATOR = 13

    CONTROL = 14

    FORMAT = 15

    SURROGATE = 16

    PRIVATE_USE = 17

    CONNECTOR_PUNCTUATION = 18

    DASH_PUNCTUATION = 19

    OPEN_PUNCTUATION = 20

    CLOSE_PUNCTUATION = 21

    INITIAL_QUOTE_PUNCTUATION = 22

    FINAL_QUOTE_PUNCTUATION = 23

    OTHER_PUNCTUATION = 24

    MATH_SYMBOL = 25

    CURRENCY_SYMBOL = 26

    MODIFIER_SYMBOL = 27

    OTHER_SYMBOL = 28

    OTHER_NOT_ASSIGNED = 29


class CharUnicodeInfo(System.Object):
    """
    This class implements a set of methods for retrieving character type
    information. Character type information is independent of culture
    and region.
    """

    @staticmethod
    @overload
    def get_decimal_digit_value(ch: str) -> int:
        ...

    @staticmethod
    @overload
    def get_decimal_digit_value(s: str, index: int) -> int:
        ...

    @staticmethod
    @overload
    def get_digit_value(ch: str) -> int:
        ...

    @staticmethod
    @overload
    def get_digit_value(s: str, index: int) -> int:
        ...

    @staticmethod
    @overload
    def get_numeric_value(ch: str) -> float:
        ...

    @staticmethod
    @overload
    def get_numeric_value(s: str, index: int) -> float:
        ...

    @staticmethod
    @overload
    def get_unicode_category(ch: str) -> System.Globalization.UnicodeCategory:
        ...

    @staticmethod
    @overload
    def get_unicode_category(code_point: int) -> System.Globalization.UnicodeCategory:
        ...

    @staticmethod
    @overload
    def get_unicode_category(s: str, index: int) -> System.Globalization.UnicodeCategory:
        ...


class DateTimeStyles(Enum):
    """Defines the formatting options that customize string parsing for some date and time parsing methods."""

    NONE = ...

    ALLOW_LEADING_WHITE = ...

    ALLOW_TRAILING_WHITE = ...

    ALLOW_INNER_WHITE = ...

    ALLOW_WHITE_SPACES = ...

    NO_CURRENT_DATE_DEFAULT = ...

    ADJUST_TO_UNIVERSAL = ...

    ASSUME_LOCAL = ...

    ASSUME_UNIVERSAL = ...

    ROUNDTRIP_KIND = ...


class DaylightTime(System.Object):
    """This class has no documentation."""

    @property
    def start(self) -> datetime.datetime:
        ...

    @property
    def end(self) -> datetime.datetime:
        ...

    @property
    def delta(self) -> datetime.timedelta:
        ...

    def __init__(self, start: typing.Union[datetime.datetime, datetime.date], end: typing.Union[datetime.datetime, datetime.date], delta: datetime.timedelta) -> None:
        ...


class ChineseLunisolarCalendar(System.Globalization.EastAsianLunisolarCalendar):
    """This class has no documentation."""

    CHINESE_ERA: int = 1

    @property
    def min_supported_date_time(self) -> datetime.datetime:
        ...

    @property
    def max_supported_date_time(self) -> datetime.datetime:
        ...

    @property
    def days_in_year_before_min_supported_year(self) -> int:
        """This property is protected."""
        ...

    @property
    def eras(self) -> typing.List[int]:
        ...

    def __init__(self) -> None:
        ...

    def get_era(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...


class IdnMapping(System.Object):
    """This class has no documentation."""

    @property
    def allow_unassigned(self) -> bool:
        ...

    @allow_unassigned.setter
    def allow_unassigned(self, value: bool) -> None:
        ...

    @property
    def use_std_3_ascii_rules(self) -> bool:
        ...

    @use_std_3_ascii_rules.setter
    def use_std_3_ascii_rules(self, value: bool) -> None:
        ...

    def __init__(self) -> None:
        ...

    def equals(self, obj: typing.Any) -> bool:
        ...

    @overload
    def get_ascii(self, unicode: str) -> str:
        ...

    @overload
    def get_ascii(self, unicode: str, index: int) -> str:
        ...

    @overload
    def get_ascii(self, unicode: str, index: int, count: int) -> str:
        ...

    def get_hash_code(self) -> int:
        ...

    @overload
    def get_unicode(self, ascii: str) -> str:
        ...

    @overload
    def get_unicode(self, ascii: str, index: int) -> str:
        ...

    @overload
    def get_unicode(self, ascii: str, index: int, count: int) -> str:
        ...


class CultureTypes(Enum):
    """This class has no documentation."""

    NEUTRAL_CULTURES = ...

    SPECIFIC_CULTURES = ...

    INSTALLED_WIN_32_CULTURES = ...

    ALL_CULTURES = ...

    USER_CUSTOM_CULTURE = ...

    REPLACEMENT_CULTURES = ...

    WINDOWS_ONLY_CULTURES = ...
    """CultureTypes.WindowsOnlyCultures has been deprecated. Use other values in CultureTypes instead."""

    FRAMEWORK_CULTURES = ...
    """CultureTypes.FrameworkCultures has been deprecated. Use other values in CultureTypes instead."""


class DigitShapes(Enum):
    """This class has no documentation."""

    CONTEXT = ...

    NONE = ...

    NATIVE_NATIONAL = ...


class NumberFormatInfo(System.Object, System.IFormatProvider, System.ICloneable):
    """This class has no documentation."""

    INVARIANT_INFO: System.Globalization.NumberFormatInfo
    """
    Returns a default NumberFormatInfo that will be universally
    supported and constant irrespective of the current culture.
    Used by FromString methods.
    """

    @property
    def currency_decimal_digits(self) -> int:
        ...

    @currency_decimal_digits.setter
    def currency_decimal_digits(self, value: int) -> None:
        ...

    @property
    def currency_decimal_separator(self) -> str:
        ...

    @currency_decimal_separator.setter
    def currency_decimal_separator(self, value: str) -> None:
        ...

    @property
    def is_read_only(self) -> bool:
        ...

    @property
    def currency_group_sizes(self) -> typing.List[int]:
        ...

    @currency_group_sizes.setter
    def currency_group_sizes(self, value: typing.List[int]) -> None:
        ...

    @property
    def number_group_sizes(self) -> typing.List[int]:
        ...

    @number_group_sizes.setter
    def number_group_sizes(self, value: typing.List[int]) -> None:
        ...

    @property
    def percent_group_sizes(self) -> typing.List[int]:
        ...

    @percent_group_sizes.setter
    def percent_group_sizes(self, value: typing.List[int]) -> None:
        ...

    @property
    def currency_group_separator(self) -> str:
        ...

    @currency_group_separator.setter
    def currency_group_separator(self, value: str) -> None:
        ...

    @property
    def currency_symbol(self) -> str:
        ...

    @currency_symbol.setter
    def currency_symbol(self, value: str) -> None:
        ...

    CURRENT_INFO: System.Globalization.NumberFormatInfo
    """Returns the current culture's NumberFormatInfo. Used by Parse methods."""

    @property
    def na_n_symbol(self) -> str:
        ...

    @na_n_symbol.setter
    def na_n_symbol(self, value: str) -> None:
        ...

    @property
    def currency_negative_pattern(self) -> int:
        ...

    @currency_negative_pattern.setter
    def currency_negative_pattern(self, value: int) -> None:
        ...

    @property
    def number_negative_pattern(self) -> int:
        ...

    @number_negative_pattern.setter
    def number_negative_pattern(self, value: int) -> None:
        ...

    @property
    def percent_positive_pattern(self) -> int:
        ...

    @percent_positive_pattern.setter
    def percent_positive_pattern(self, value: int) -> None:
        ...

    @property
    def percent_negative_pattern(self) -> int:
        ...

    @percent_negative_pattern.setter
    def percent_negative_pattern(self, value: int) -> None:
        ...

    @property
    def negative_infinity_symbol(self) -> str:
        ...

    @negative_infinity_symbol.setter
    def negative_infinity_symbol(self, value: str) -> None:
        ...

    @property
    def negative_sign(self) -> str:
        ...

    @negative_sign.setter
    def negative_sign(self, value: str) -> None:
        ...

    @property
    def number_decimal_digits(self) -> int:
        ...

    @number_decimal_digits.setter
    def number_decimal_digits(self, value: int) -> None:
        ...

    @property
    def number_decimal_separator(self) -> str:
        ...

    @number_decimal_separator.setter
    def number_decimal_separator(self, value: str) -> None:
        ...

    @property
    def number_group_separator(self) -> str:
        ...

    @number_group_separator.setter
    def number_group_separator(self, value: str) -> None:
        ...

    @property
    def currency_positive_pattern(self) -> int:
        ...

    @currency_positive_pattern.setter
    def currency_positive_pattern(self, value: int) -> None:
        ...

    @property
    def positive_infinity_symbol(self) -> str:
        ...

    @positive_infinity_symbol.setter
    def positive_infinity_symbol(self, value: str) -> None:
        ...

    @property
    def positive_sign(self) -> str:
        ...

    @positive_sign.setter
    def positive_sign(self, value: str) -> None:
        ...

    @property
    def percent_decimal_digits(self) -> int:
        ...

    @percent_decimal_digits.setter
    def percent_decimal_digits(self, value: int) -> None:
        ...

    @property
    def percent_decimal_separator(self) -> str:
        ...

    @percent_decimal_separator.setter
    def percent_decimal_separator(self, value: str) -> None:
        ...

    @property
    def percent_group_separator(self) -> str:
        ...

    @percent_group_separator.setter
    def percent_group_separator(self, value: str) -> None:
        ...

    @property
    def percent_symbol(self) -> str:
        ...

    @percent_symbol.setter
    def percent_symbol(self, value: str) -> None:
        ...

    @property
    def per_mille_symbol(self) -> str:
        ...

    @per_mille_symbol.setter
    def per_mille_symbol(self, value: str) -> None:
        ...

    @property
    def native_digits(self) -> typing.List[str]:
        ...

    @native_digits.setter
    def native_digits(self, value: typing.List[str]) -> None:
        ...

    @property
    def digit_substitution(self) -> System.Globalization.DigitShapes:
        ...

    @digit_substitution.setter
    def digit_substitution(self, value: System.Globalization.DigitShapes) -> None:
        ...

    def __init__(self) -> None:
        ...

    def clone(self) -> System.Object:
        ...

    def get_format(self, format_type: typing.Type) -> System.Object:
        ...

    @staticmethod
    def get_instance(format_provider: System.IFormatProvider) -> System.Globalization.NumberFormatInfo:
        ...

    @staticmethod
    def read_only(nfi: System.Globalization.NumberFormatInfo) -> System.Globalization.NumberFormatInfo:
        ...


class DateTimeFormatInfo(System.Object, System.IFormatProvider, System.ICloneable):
    """This class has no documentation."""

    INVARIANT_INFO: System.Globalization.DateTimeFormatInfo
    """
    Returns a default DateTimeFormatInfo that will be universally
    supported and constant irrespective of the current culture.
    """

    CURRENT_INFO: System.Globalization.DateTimeFormatInfo
    """Returns the current culture's DateTimeFormatInfo."""

    @property
    def am_designator(self) -> str:
        ...

    @am_designator.setter
    def am_designator(self, value: str) -> None:
        ...

    @property
    def calendar(self) -> System.Globalization.Calendar:
        ...

    @calendar.setter
    def calendar(self, value: System.Globalization.Calendar) -> None:
        ...

    @property
    def date_separator(self) -> str:
        ...

    @date_separator.setter
    def date_separator(self, value: str) -> None:
        ...

    @property
    def first_day_of_week(self) -> System.DayOfWeek:
        ...

    @first_day_of_week.setter
    def first_day_of_week(self, value: System.DayOfWeek) -> None:
        ...

    @property
    def calendar_week_rule(self) -> System.Globalization.CalendarWeekRule:
        ...

    @calendar_week_rule.setter
    def calendar_week_rule(self, value: System.Globalization.CalendarWeekRule) -> None:
        ...

    @property
    def full_date_time_pattern(self) -> str:
        ...

    @full_date_time_pattern.setter
    def full_date_time_pattern(self, value: str) -> None:
        ...

    @property
    def long_date_pattern(self) -> str:
        """
        For our "patterns" arrays we have 2 variables, a string and a string[]
        The string[] contains the list of patterns, EXCEPT the default may not be included.
        The string contains the default pattern.
        When we initially construct our string[], we set the string to string[0]
        """
        ...

    @long_date_pattern.setter
    def long_date_pattern(self, value: str) -> None:
        ...

    @property
    def long_time_pattern(self) -> str:
        """
        For our "patterns" arrays we have 2 variables, a string and a string[]
        
        The string[] contains the list of patterns, EXCEPT the default may not be included.
        The string contains the default pattern.
        When we initially construct our string[], we set the string to string[0]
        """
        ...

    @long_time_pattern.setter
    def long_time_pattern(self, value: str) -> None:
        ...

    @property
    def month_day_pattern(self) -> str:
        ...

    @month_day_pattern.setter
    def month_day_pattern(self, value: str) -> None:
        ...

    @property
    def pm_designator(self) -> str:
        ...

    @pm_designator.setter
    def pm_designator(self, value: str) -> None:
        ...

    @property
    def rfc_1123_pattern(self) -> str:
        ...

    @property
    def short_date_pattern(self) -> str:
        """
        For our "patterns" arrays we have 2 variables, a string and a string[]
        
        The string[] contains the list of patterns, EXCEPT the default may not be included.
        The string contains the default pattern.
        When we initially construct our string[], we set the string to string[0]
        """
        ...

    @short_date_pattern.setter
    def short_date_pattern(self, value: str) -> None:
        ...

    @property
    def short_time_pattern(self) -> str:
        """
        For our "patterns" arrays we have 2 variables, a string and a string[]
        
        The string[] contains the list of patterns, EXCEPT the default may not be included.
        The string contains the default pattern.
        When we initially construct our string[], we set the string to string[0]
        """
        ...

    @short_time_pattern.setter
    def short_time_pattern(self, value: str) -> None:
        ...

    @property
    def sortable_date_time_pattern(self) -> str:
        ...

    @property
    def time_separator(self) -> str:
        ...

    @time_separator.setter
    def time_separator(self, value: str) -> None:
        ...

    @property
    def universal_sortable_date_time_pattern(self) -> str:
        ...

    @property
    def year_month_pattern(self) -> str:
        """
        For our "patterns" arrays we have 2 variables, a string and a string[]
        
        The string[] contains the list of patterns, EXCEPT the default may not be included.
        The string contains the default pattern.
        When we initially construct our string[], we set the string to string[0]
        """
        ...

    @year_month_pattern.setter
    def year_month_pattern(self, value: str) -> None:
        ...

    @property
    def abbreviated_day_names(self) -> typing.List[str]:
        ...

    @abbreviated_day_names.setter
    def abbreviated_day_names(self, value: typing.List[str]) -> None:
        ...

    @property
    def shortest_day_names(self) -> typing.List[str]:
        """Returns the string array of the one-letter day of week names."""
        ...

    @shortest_day_names.setter
    def shortest_day_names(self, value: typing.List[str]) -> None:
        ...

    @property
    def day_names(self) -> typing.List[str]:
        ...

    @day_names.setter
    def day_names(self, value: typing.List[str]) -> None:
        ...

    @property
    def abbreviated_month_names(self) -> typing.List[str]:
        ...

    @abbreviated_month_names.setter
    def abbreviated_month_names(self, value: typing.List[str]) -> None:
        ...

    @property
    def month_names(self) -> typing.List[str]:
        ...

    @month_names.setter
    def month_names(self, value: typing.List[str]) -> None:
        ...

    @property
    def is_read_only(self) -> bool:
        ...

    @property
    def native_calendar_name(self) -> str:
        """
        Return the native name for the calendar in DTFI.Calendar.  The native name is referred to
        the culture used to create the DTFI.  E.g. in the following example, the native language is Japanese.
        DateTimeFormatInfo dtfi = new CultureInfo("ja-JP", false).DateTimeFormat.Calendar = new JapaneseCalendar();
        String nativeName = dtfi.NativeCalendarName; // Get the Japanese name for the Japanese calendar.
        DateTimeFormatInfo dtfi = new CultureInfo("ja-JP", false).DateTimeFormat.Calendar = new GregorianCalendar(GregorianCalendarTypes.Localized);
        String nativeName = dtfi.NativeCalendarName; // Get the Japanese name for the Gregorian calendar.
        """
        ...

    @property
    def abbreviated_month_genitive_names(self) -> typing.List[str]:
        ...

    @abbreviated_month_genitive_names.setter
    def abbreviated_month_genitive_names(self, value: typing.List[str]) -> None:
        ...

    @property
    def month_genitive_names(self) -> typing.List[str]:
        ...

    @month_genitive_names.setter
    def month_genitive_names(self, value: typing.List[str]) -> None:
        ...

    def __init__(self) -> None:
        ...

    def clone(self) -> System.Object:
        ...

    def get_abbreviated_day_name(self, dayofweek: System.DayOfWeek) -> str:
        ...

    def get_abbreviated_era_name(self, era: int) -> str:
        ...

    def get_abbreviated_month_name(self, month: int) -> str:
        ...

    @overload
    def get_all_date_time_patterns(self) -> typing.List[str]:
        ...

    @overload
    def get_all_date_time_patterns(self, format: str) -> typing.List[str]:
        ...

    def get_day_name(self, dayofweek: System.DayOfWeek) -> str:
        ...

    def get_era(self, era_name: str) -> int:
        """Get the era value by parsing the name of the era."""
        ...

    def get_era_name(self, era: int) -> str:
        """
        Get the name of the era for the specified era value.
        Era names are 1 indexed
        """
        ...

    def get_format(self, format_type: typing.Type) -> System.Object:
        ...

    @staticmethod
    def get_instance(provider: System.IFormatProvider) -> System.Globalization.DateTimeFormatInfo:
        ...

    def get_month_name(self, month: int) -> str:
        ...

    def get_shortest_day_name(self, day_of_week: System.DayOfWeek) -> str:
        """Returns the super short day of week names for the specified day of week."""
        ...

    @staticmethod
    def read_only(dtfi: System.Globalization.DateTimeFormatInfo) -> System.Globalization.DateTimeFormatInfo:
        ...

    def set_all_date_time_patterns(self, patterns: typing.List[str], format: str) -> None:
        """
        Used by custom cultures and others to set the list of available formats. Note that none of them are
        explicitly used unless someone calls GetAllDateTimePatterns and subsequently uses one of the items
        from the list.
        
        Most of the format characters that can be used in GetAllDateTimePatterns are
        not really needed since they are one of the following:
        
         r/R/s/u     locale-independent constants -- cannot be changed!
         m/M/y/Y     fields with a single string in them -- that can be set through props directly
         f/F/g/G/U   derived fields based on combinations of various of the below formats
        
        NOTE: No special validation is done here beyond what is done when the actual respective fields
        are used (what would be the point of disallowing here what we allow in the appropriate property?)
        
        WARNING: If more validation is ever done in one place, it should be done in the other.
        """
        ...


class CultureInfo(System.Object, System.IFormatProvider, System.ICloneable):
    """
    This class represents the software preferences of a particular culture
    or community. It includes information such as the language, writing
    system and a calendar used by the culture as well as methods for
    common operations such as printing dates and sorting strings.
    """

    current_culture: System.Globalization.CultureInfo
    """
    This instance provides methods based on the current user settings.
    These settings are volatile and may change over the lifetime of the
    thread.
    """

    current_ui_culture: System.Globalization.CultureInfo

    INSTALLED_UI_CULTURE: System.Globalization.CultureInfo

    default_thread_current_culture: System.Globalization.CultureInfo

    default_thread_current_ui_culture: System.Globalization.CultureInfo

    INVARIANT_CULTURE: System.Globalization.CultureInfo
    """
    This instance provides methods, for example for casing and sorting,
    that are independent of the system and current user settings.  It
    should be used only by processes such as some system services that
    require such invariant results (eg. file systems).  In general,
    the results are not linguistically correct and do not match any
    culture info.
    """

    @property
    def parent(self) -> System.Globalization.CultureInfo:
        """Return the parent CultureInfo for the current instance."""
        ...

    @property
    def lcid(self) -> int:
        ...

    @property
    def keyboard_layout_id(self) -> int:
        ...

    @property
    def name(self) -> str:
        """
        Returns the full name of the CultureInfo. The name is in format like
        "en-US" This version does NOT include sort information in the name.
        """
        ...

    @property
    def ietf_language_tag(self) -> str:
        ...

    @property
    def display_name(self) -> str:
        """
        Returns the full name of the CultureInfo in the localized language.
        For example, if the localized language of the runtime is Spanish and the CultureInfo is
        US English, "Ingles (Estados Unidos)" will be returned.
        """
        ...

    @property
    def native_name(self) -> str:
        """
        Returns the full name of the CultureInfo in the native language.
        For example, if the CultureInfo is US English, "English
        (United States)" will be returned.
        """
        ...

    @property
    def english_name(self) -> str:
        """
        Returns the full name of the CultureInfo in English.
        For example, if the CultureInfo is US English, "English
        (United States)" will be returned.
        """
        ...

    @property
    def two_letter_iso_language_name(self) -> str:
        """ie: en"""
        ...

    @property
    def three_letter_iso_language_name(self) -> str:
        """ie: eng"""
        ...

    @property
    def three_letter_windows_language_name(self) -> str:
        """
        Returns the 3 letter windows language name for the current instance.  eg: "ENU"
        The ISO names are much preferred
        """
        ...

    @property
    def compare_info(self) -> System.Globalization.CompareInfo:
        """Gets the CompareInfo for this culture."""
        ...

    @property
    def text_info(self) -> System.Globalization.TextInfo:
        """Gets the TextInfo for this culture."""
        ...

    @property
    def is_neutral_culture(self) -> bool:
        ...

    @property
    def culture_types(self) -> System.Globalization.CultureTypes:
        ...

    @property
    def number_format(self) -> System.Globalization.NumberFormatInfo:
        ...

    @number_format.setter
    def number_format(self, value: System.Globalization.NumberFormatInfo) -> None:
        ...

    @property
    def date_time_format(self) -> System.Globalization.DateTimeFormatInfo:
        """
        Create a DateTimeFormatInfo, and fill in the properties according to
        the CultureID.
        """
        ...

    @date_time_format.setter
    def date_time_format(self, value: System.Globalization.DateTimeFormatInfo) -> None:
        ...

    @property
    def calendar(self) -> System.Globalization.Calendar:
        """
        Return/set the default calendar used by this culture.
        This value can be overridden by regional option if this is a current culture.
        """
        ...

    @property
    def optional_calendars(self) -> typing.List[System.Globalization.Calendar]:
        """Return an array of the optional calendar for this culture."""
        ...

    @property
    def use_user_override(self) -> bool:
        ...

    @property
    def is_read_only(self) -> bool:
        ...

    @overload
    def __init__(self, name: str) -> None:
        ...

    @overload
    def __init__(self, name: str, use_user_override: bool) -> None:
        ...

    @overload
    def __init__(self, culture: int) -> None:
        ...

    @overload
    def __init__(self, culture: int, use_user_override: bool) -> None:
        ...

    def clear_cached_data(self) -> None:
        ...

    def clone(self) -> System.Object:
        ...

    @staticmethod
    def create_specific_culture(name: str) -> System.Globalization.CultureInfo:
        """
        Return a specific culture. A tad irrelevant now since we always
        return valid data for neutral locales.
        
        Note that there's interesting behavior that tries to find a
        smaller name, ala RFC4647, if we can't find a bigger name.
        That doesn't help with things like "zh" though, so the approach
        is of questionable value
        """
        ...

    def equals(self, value: typing.Any) -> bool:
        ...

    def get_console_fallback_ui_culture(self) -> System.Globalization.CultureInfo:
        ...

    @staticmethod
    @overload
    def get_culture_info(culture: int) -> System.Globalization.CultureInfo:
        """
        Gets a cached copy of the specified culture from an internal
        hashtable (or creates it if not found). (LCID version)
        """
        ...

    @staticmethod
    @overload
    def get_culture_info(name: str) -> System.Globalization.CultureInfo:
        """
        Gets a cached copy of the specified culture from an internal
        hashtable (or creates it if not found). (Named version)
        """
        ...

    @staticmethod
    @overload
    def get_culture_info(name: str, alt_name: str) -> System.Globalization.CultureInfo:
        """
        Gets a cached copy of the specified culture from an internal
        hashtable (or creates it if not found).
        """
        ...

    @staticmethod
    @overload
    def get_culture_info(name: str, predefined_only: bool) -> System.Globalization.CultureInfo:
        ...

    @staticmethod
    def get_culture_info_by_ietf_language_tag(name: str) -> System.Globalization.CultureInfo:
        ...

    @staticmethod
    def get_cultures(types: System.Globalization.CultureTypes) -> typing.List[System.Globalization.CultureInfo]:
        ...

    def get_format(self, format_type: typing.Type) -> System.Object:
        ...

    def get_hash_code(self) -> int:
        ...

    @staticmethod
    def read_only(ci: System.Globalization.CultureInfo) -> System.Globalization.CultureInfo:
        ...

    def to_string(self) -> str:
        """
        Implements object.ToString(). Returns the name of the CultureInfo,
        eg. "de-DE_phoneb", "en-US", or "fj-FJ".
        """
        ...


class GlobalizationExtensions(System.Object):
    """This class has no documentation."""

    @staticmethod
    def get_string_comparer(compare_info: System.Globalization.CompareInfo, options: System.Globalization.CompareOptions) -> System.StringComparer:
        ...


class KoreanLunisolarCalendar(System.Globalization.EastAsianLunisolarCalendar):
    """This class has no documentation."""

    GREGORIAN_ERA: int = 1

    @property
    def min_supported_date_time(self) -> datetime.datetime:
        ...

    @property
    def max_supported_date_time(self) -> datetime.datetime:
        ...

    @property
    def days_in_year_before_min_supported_year(self) -> int:
        """This property is protected."""
        ...

    @property
    def eras(self) -> typing.List[int]:
        ...

    def __init__(self) -> None:
        ...

    def get_era(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...


class CultureNotFoundException(System.ArgumentException):
    """This class has no documentation."""

    @property
    def invalid_culture_id(self) -> typing.Optional[int]:
        ...

    @property
    def invalid_culture_name(self) -> str:
        ...

    @property
    def message(self) -> str:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, message: str) -> None:
        ...

    @overload
    def __init__(self, param_name: str, message: str) -> None:
        ...

    @overload
    def __init__(self, message: str, inner_exception: System.Exception) -> None:
        ...

    @overload
    def __init__(self, param_name: str, invalid_culture_name: str, message: str) -> None:
        ...

    @overload
    def __init__(self, message: str, invalid_culture_name: str, inner_exception: System.Exception) -> None:
        ...

    @overload
    def __init__(self, message: str, invalid_culture_id: int, inner_exception: System.Exception) -> None:
        ...

    @overload
    def __init__(self, param_name: str, invalid_culture_id: int, message: str) -> None:
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


class KoreanCalendar(System.Globalization.Calendar):
    """
    Korean calendar is based on the Gregorian calendar.  And the year is an offset to Gregorian calendar.
    That is,
         Korean year = Gregorian year + 2333.  So 2000/01/01 A.D. is Korean 4333/01/01
    
    0001/1/1 A.D. is Korean year 2334.
    """

    KOREAN_ERA: int = 1

    @property
    def min_supported_date_time(self) -> datetime.datetime:
        ...

    @property
    def max_supported_date_time(self) -> datetime.datetime:
        ...

    @property
    def algorithm_type(self) -> System.Globalization.CalendarAlgorithmType:
        ...

    @property
    def eras(self) -> typing.List[int]:
        ...

    @property
    def two_digit_year_max(self) -> int:
        ...

    @two_digit_year_max.setter
    def two_digit_year_max(self, value: int) -> None:
        ...

    def __init__(self) -> None:
        ...

    def add_months(self, time: typing.Union[datetime.datetime, datetime.date], months: int) -> datetime.datetime:
        ...

    def add_years(self, time: typing.Union[datetime.datetime, datetime.date], years: int) -> datetime.datetime:
        ...

    def get_day_of_month(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_day_of_week(self, time: typing.Union[datetime.datetime, datetime.date]) -> System.DayOfWeek:
        ...

    def get_day_of_year(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_days_in_month(self, year: int, month: int, era: int) -> int:
        ...

    def get_days_in_year(self, year: int, era: int) -> int:
        ...

    def get_era(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_leap_month(self, year: int, era: int) -> int:
        ...

    def get_month(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_months_in_year(self, year: int, era: int) -> int:
        ...

    def get_week_of_year(self, time: typing.Union[datetime.datetime, datetime.date], rule: System.Globalization.CalendarWeekRule, first_day_of_week: System.DayOfWeek) -> int:
        ...

    def get_year(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def is_leap_day(self, year: int, month: int, day: int, era: int) -> bool:
        ...

    def is_leap_month(self, year: int, month: int, era: int) -> bool:
        ...

    def is_leap_year(self, year: int, era: int) -> bool:
        ...

    def to_date_time(self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, era: int) -> datetime.datetime:
        ...

    def to_four_digit_year(self, year: int) -> int:
        ...


class TextElementEnumerator(System.Object, System.Collections.IEnumerator):
    """This class has no documentation."""

    @property
    def current(self) -> System.Object:
        ...

    @property
    def element_index(self) -> int:
        ...

    def get_text_element(self) -> str:
        ...

    def move_next(self) -> bool:
        ...

    def reset(self) -> None:
        ...


class StringInfo(System.Object):
    """
    This class defines behaviors specific to a writing system.
    A writing system is the collection of scripts and orthographic rules
    required to represent a language as text.
    """

    @property
    def string(self) -> str:
        ...

    @string.setter
    def string(self, value: str) -> None:
        ...

    @property
    def length_in_text_elements(self) -> int:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, value: str) -> None:
        ...

    def equals(self, value: typing.Any) -> bool:
        ...

    def get_hash_code(self) -> int:
        ...

    @staticmethod
    @overload
    def get_next_text_element(str: str) -> str:
        """
        Returns the first text element (extended grapheme cluster) that occurs in the input string.
        
        :param str: The input string to analyze.
        :returns: The substring corresponding to the first text element within , or the empty string if  is empty.
        """
        ...

    @staticmethod
    @overload
    def get_next_text_element(str: str, index: int) -> str:
        """
        Returns the first text element (extended grapheme cluster) that occurs in the input string
        starting at the specified index.
        
        :param str: The input string to analyze.
        :param index: The char offset in  at which to begin analysis.
        :returns: The substring corresponding to the first text element within  starting at index , or the empty string if  corresponds to the end of .
        """
        ...

    @staticmethod
    @overload
    def get_next_text_element_length(str: str) -> int:
        """
        Returns the length of the first text element (extended grapheme cluster) that occurs in the input string.
        
        :param str: The input string to analyze.
        :returns: The length (in chars) of the substring corresponding to the first text element within , or 0 if  is empty.
        """
        ...

    @staticmethod
    @overload
    def get_next_text_element_length(str: str, index: int) -> int:
        """
        Returns the length of the first text element (extended grapheme cluster) that occurs in the input string
        starting at the specified index.
        
        :param str: The input string to analyze.
        :param index: The char offset in  at which to begin analysis.
        :returns: The length (in chars) of the substring corresponding to the first text element within  starting at index , or 0 if  corresponds to the end of .
        """
        ...

    @staticmethod
    @overload
    def get_next_text_element_length(str: System.ReadOnlySpan[str]) -> int:
        """
        Returns the length of the first text element (extended grapheme cluster) that occurs in the input span.
        
        :param str: The input span to analyze.
        :returns: The length (in chars) of the substring corresponding to the first text element within , or 0 if  is empty.
        """
        ...

    @staticmethod
    @overload
    def get_text_element_enumerator(str: str) -> System.Globalization.TextElementEnumerator:
        ...

    @staticmethod
    @overload
    def get_text_element_enumerator(str: str, index: int) -> System.Globalization.TextElementEnumerator:
        ...

    @staticmethod
    def parse_combining_characters(str: str) -> typing.List[int]:
        """
        Returns the indices of each base character or properly formed surrogate
        pair  within the str. It recognizes a base character plus one or more
        combining characters or a properly formed surrogate pair as a text
        element and returns the index of the base character or high surrogate.
        Each index is the beginning of a text element within a str. The length
        of each element is easily computed as the difference between successive
        indices. The length of the array will always be less than or equal to
        the length of the str. For example, given the str
        \\u4f00\\u302a\\ud800\\udc00\\u4f01, this method would return the indices:
        0, 2, 4.
        """
        ...

    @overload
    def substring_by_text_elements(self, starting_text_element: int) -> str:
        ...

    @overload
    def substring_by_text_elements(self, starting_text_element: int, length_in_text_elements: int) -> str:
        ...


class TaiwanCalendar(System.Globalization.Calendar):
    """
    Taiwan calendar is based on the Gregorian calendar.  And the year is an offset to Gregorian calendar.
    That is,
         Taiwan year = Gregorian year - 1911.  So 1912/01/01 A.D. is Taiwan 1/01/01
    """

    @property
    def min_supported_date_time(self) -> datetime.datetime:
        ...

    @property
    def max_supported_date_time(self) -> datetime.datetime:
        ...

    @property
    def algorithm_type(self) -> System.Globalization.CalendarAlgorithmType:
        ...

    @property
    def eras(self) -> typing.List[int]:
        ...

    @property
    def two_digit_year_max(self) -> int:
        ...

    @two_digit_year_max.setter
    def two_digit_year_max(self, value: int) -> None:
        ...

    def __init__(self) -> None:
        ...

    def add_months(self, time: typing.Union[datetime.datetime, datetime.date], months: int) -> datetime.datetime:
        ...

    def add_years(self, time: typing.Union[datetime.datetime, datetime.date], years: int) -> datetime.datetime:
        ...

    def get_day_of_month(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_day_of_week(self, time: typing.Union[datetime.datetime, datetime.date]) -> System.DayOfWeek:
        ...

    def get_day_of_year(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_days_in_month(self, year: int, month: int, era: int) -> int:
        ...

    def get_days_in_year(self, year: int, era: int) -> int:
        ...

    def get_era(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_leap_month(self, year: int, era: int) -> int:
        ...

    def get_month(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_months_in_year(self, year: int, era: int) -> int:
        ...

    def get_week_of_year(self, time: typing.Union[datetime.datetime, datetime.date], rule: System.Globalization.CalendarWeekRule, first_day_of_week: System.DayOfWeek) -> int:
        ...

    def get_year(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def is_leap_day(self, year: int, month: int, day: int, era: int) -> bool:
        ...

    def is_leap_month(self, year: int, month: int, era: int) -> bool:
        ...

    def is_leap_year(self, year: int, era: int) -> bool:
        ...

    def to_date_time(self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, era: int) -> datetime.datetime:
        ...

    def to_four_digit_year(self, year: int) -> int:
        """
        For Taiwan calendar, four digit year is not used.
        Therefore, for any two digit number, we just return the original number.
        """
        ...


class JulianCalendar(System.Globalization.Calendar):
    """
    This class implements the Julian calendar. In 48 B.C. Julius Caesar
    ordered a calendar reform, and this calendar is called Julian calendar.
    It consisted of a solar year of twelve months and of 365 days with an
    extra day every fourth year.
    """

    JULIAN_ERA: int = 1

    @property
    def min_supported_date_time(self) -> datetime.datetime:
        ...

    @property
    def max_supported_date_time(self) -> datetime.datetime:
        ...

    @property
    def algorithm_type(self) -> System.Globalization.CalendarAlgorithmType:
        ...

    @property
    def eras(self) -> typing.List[int]:
        ...

    @property
    def two_digit_year_max(self) -> int:
        ...

    @two_digit_year_max.setter
    def two_digit_year_max(self, value: int) -> None:
        ...

    def __init__(self) -> None:
        ...

    def add_months(self, time: typing.Union[datetime.datetime, datetime.date], months: int) -> datetime.datetime:
        ...

    def add_years(self, time: typing.Union[datetime.datetime, datetime.date], years: int) -> datetime.datetime:
        ...

    def get_day_of_month(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_day_of_week(self, time: typing.Union[datetime.datetime, datetime.date]) -> System.DayOfWeek:
        ...

    def get_day_of_year(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_days_in_month(self, year: int, month: int, era: int) -> int:
        ...

    def get_days_in_year(self, year: int, era: int) -> int:
        ...

    def get_era(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_leap_month(self, year: int, era: int) -> int:
        ...

    def get_month(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_months_in_year(self, year: int, era: int) -> int:
        ...

    def get_year(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def is_leap_day(self, year: int, month: int, day: int, era: int) -> bool:
        ...

    def is_leap_month(self, year: int, month: int, era: int) -> bool:
        ...

    def is_leap_year(self, year: int, era: int) -> bool:
        ...

    def to_date_time(self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, era: int) -> datetime.datetime:
        ...

    def to_four_digit_year(self, year: int) -> int:
        ...


class ThaiBuddhistCalendar(System.Globalization.Calendar):
    """
    ThaiBuddhistCalendar is based on Gregorian calendar.
    Its year value has an offset to the Gregorain calendar.
    """

    THAI_BUDDHIST_ERA: int = 1

    @property
    def min_supported_date_time(self) -> datetime.datetime:
        ...

    @property
    def max_supported_date_time(self) -> datetime.datetime:
        ...

    @property
    def algorithm_type(self) -> System.Globalization.CalendarAlgorithmType:
        ...

    @property
    def eras(self) -> typing.List[int]:
        ...

    @property
    def two_digit_year_max(self) -> int:
        ...

    @two_digit_year_max.setter
    def two_digit_year_max(self, value: int) -> None:
        ...

    def __init__(self) -> None:
        ...

    def add_months(self, time: typing.Union[datetime.datetime, datetime.date], months: int) -> datetime.datetime:
        ...

    def add_years(self, time: typing.Union[datetime.datetime, datetime.date], years: int) -> datetime.datetime:
        ...

    def get_day_of_month(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_day_of_week(self, time: typing.Union[datetime.datetime, datetime.date]) -> System.DayOfWeek:
        ...

    def get_day_of_year(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_days_in_month(self, year: int, month: int, era: int) -> int:
        ...

    def get_days_in_year(self, year: int, era: int) -> int:
        ...

    def get_era(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_leap_month(self, year: int, era: int) -> int:
        ...

    def get_month(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_months_in_year(self, year: int, era: int) -> int:
        ...

    def get_week_of_year(self, time: typing.Union[datetime.datetime, datetime.date], rule: System.Globalization.CalendarWeekRule, first_day_of_week: System.DayOfWeek) -> int:
        ...

    def get_year(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def is_leap_day(self, year: int, month: int, day: int, era: int) -> bool:
        ...

    def is_leap_month(self, year: int, month: int, era: int) -> bool:
        ...

    def is_leap_year(self, year: int, era: int) -> bool:
        ...

    def to_date_time(self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, era: int) -> datetime.datetime:
        ...

    def to_four_digit_year(self, year: int) -> int:
        ...


class JapaneseLunisolarCalendar(System.Globalization.EastAsianLunisolarCalendar):
    """This class has no documentation."""

    JAPANESE_ERA: int = 1

    @property
    def min_supported_date_time(self) -> datetime.datetime:
        ...

    @property
    def max_supported_date_time(self) -> datetime.datetime:
        ...

    @property
    def days_in_year_before_min_supported_year(self) -> int:
        """This property is protected."""
        ...

    @property
    def eras(self) -> typing.List[int]:
        ...

    def __init__(self) -> None:
        ...

    def get_era(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...


class GregorianCalendarTypes(Enum):
    """This class has no documentation."""

    LOCALIZED = ...

    US_ENGLISH = ...

    MIDDLE_EAST_FRENCH = ...

    ARABIC = ...

    TRANSLITERATED_ENGLISH = ...

    TRANSLITERATED_FRENCH = ...


class GregorianCalendar(System.Globalization.Calendar):
    """This class has no documentation."""

    AD_ERA: int = 1

    @property
    def min_supported_date_time(self) -> datetime.datetime:
        ...

    @property
    def max_supported_date_time(self) -> datetime.datetime:
        ...

    @property
    def algorithm_type(self) -> System.Globalization.CalendarAlgorithmType:
        ...

    @property
    def calendar_type(self) -> System.Globalization.GregorianCalendarTypes:
        ...

    @calendar_type.setter
    def calendar_type(self, value: System.Globalization.GregorianCalendarTypes) -> None:
        ...

    @property
    def eras(self) -> typing.List[int]:
        ...

    @property
    def two_digit_year_max(self) -> int:
        ...

    @two_digit_year_max.setter
    def two_digit_year_max(self, value: int) -> None:
        ...

    @overload
    def __init__(self) -> None:
        ...

    @overload
    def __init__(self, type: System.Globalization.GregorianCalendarTypes) -> None:
        ...

    def add_months(self, time: typing.Union[datetime.datetime, datetime.date], months: int) -> datetime.datetime:
        """
        Returns the DateTime resulting from adding the given number of
        months to the specified DateTime. The result is computed by incrementing
        (or decrementing) the year and month parts of the specified DateTime by
        value months, and, if required, adjusting the day part of the
        resulting date downwards to the last day of the resulting month in the
        resulting year. The time-of-day part of the result is the same as the
        time-of-day part of the specified DateTime.
        
        In more precise terms, considering the specified DateTime to be of the
        form y / m / d + t, where y is the
        year, m is the month, d is the day, and t is the
        time-of-day, the result is y1 / m1 / d1 + t,
        where y1 and m1 are computed by adding value months
        to y and m, and d1 is the largest value less than
        or equal to d that denotes a valid day in month m1 of year
        y1.
        """
        ...

    def add_years(self, time: typing.Union[datetime.datetime, datetime.date], years: int) -> datetime.datetime:
        """
        Returns the DateTime resulting from adding the given number of
        years to the specified DateTime. The result is computed by incrementing
        (or decrementing) the year part of the specified DateTime by value
        years. If the month and day of the specified DateTime is 2/29, and if the
        resulting year is not a leap year, the month and day of the resulting
        DateTime becomes 2/28. Otherwise, the month, day, and time-of-day
        parts of the result are the same as those of the specified DateTime.
        """
        ...

    def get_day_of_month(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        """
        Returns the day-of-month part of the specified DateTime. The returned
        value is an integer between 1 and 31.
        """
        ...

    def get_day_of_week(self, time: typing.Union[datetime.datetime, datetime.date]) -> System.DayOfWeek:
        """
        Returns the day-of-week part of the specified DateTime. The returned value
        is an integer between 0 and 6, where 0 indicates Sunday, 1 indicates
        Monday, 2 indicates Tuesday, 3 indicates Wednesday, 4 indicates
        Thursday, 5 indicates Friday, and 6 indicates Saturday.
        """
        ...

    def get_day_of_year(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        """
        Returns the day-of-year part of the specified DateTime. The returned value
        is an integer between 1 and 366.
        """
        ...

    def get_days_in_month(self, year: int, month: int, era: int) -> int:
        """
        Returns the number of days in the month given by the year and
        month arguments.
        """
        ...

    def get_days_in_year(self, year: int, era: int) -> int:
        """
        Returns the number of days in the year given by the year argument for
        the current era.
        """
        ...

    def get_era(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_leap_month(self, year: int, era: int) -> int:
        """
        Returns the leap month in a calendar year of the specified era.
        This method returns 0 if this calendar does not have leap month, or
        this year is not a leap year.
        """
        ...

    def get_month(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        """
        Returns the month part of the specified DateTime.
        The returned value is an integer between 1 and 12.
        """
        ...

    def get_months_in_year(self, year: int, era: int) -> int:
        """Returns the number of months in the specified year and era."""
        ...

    def get_year(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        """
        Returns the year part of the specified DateTime. The returned value is an
        integer between 1 and 9999.
        """
        ...

    def is_leap_day(self, year: int, month: int, day: int, era: int) -> bool:
        """
        Checks whether a given day in the specified era is a leap day. This method returns true if
        the date is a leap day, or false if not.
        """
        ...

    def is_leap_month(self, year: int, month: int, era: int) -> bool:
        """
        Checks whether a given month in the specified era is a leap month.
        This method returns true if month is a leap month, or false if not.
        """
        ...

    def is_leap_year(self, year: int, era: int) -> bool:
        """
        Checks whether a given year in the specified era is a leap year. This method returns true if
        year is a leap year, or false if not.
        """
        ...

    def to_date_time(self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, era: int) -> datetime.datetime:
        """
        Returns the date and time converted to a DateTime value.
        Throws an exception if the n-tuple is invalid.
        """
        ...

    def to_four_digit_year(self, year: int) -> int:
        ...


class HebrewCalendar(System.Globalization.Calendar):
    """This class has no documentation."""

    HEBREW_ERA: int = 1

    @property
    def min_supported_date_time(self) -> datetime.datetime:
        ...

    @property
    def max_supported_date_time(self) -> datetime.datetime:
        ...

    @property
    def algorithm_type(self) -> System.Globalization.CalendarAlgorithmType:
        ...

    @property
    def eras(self) -> typing.List[int]:
        ...

    @property
    def two_digit_year_max(self) -> int:
        ...

    @two_digit_year_max.setter
    def two_digit_year_max(self, value: int) -> None:
        ...

    def __init__(self) -> None:
        ...

    def add_months(self, time: typing.Union[datetime.datetime, datetime.date], months: int) -> datetime.datetime:
        ...

    def add_years(self, time: typing.Union[datetime.datetime, datetime.date], years: int) -> datetime.datetime:
        ...

    def get_day_of_month(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_day_of_week(self, time: typing.Union[datetime.datetime, datetime.date]) -> System.DayOfWeek:
        ...

    def get_day_of_year(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_days_in_month(self, year: int, month: int, era: int) -> int:
        ...

    def get_days_in_year(self, year: int, era: int) -> int:
        ...

    def get_era(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_leap_month(self, year: int, era: int) -> int:
        ...

    def get_month(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def get_months_in_year(self, year: int, era: int) -> int:
        ...

    def get_year(self, time: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    def is_leap_day(self, year: int, month: int, day: int, era: int) -> bool:
        ...

    def is_leap_month(self, year: int, month: int, era: int) -> bool:
        ...

    def is_leap_year(self, year: int, era: int) -> bool:
        ...

    def to_date_time(self, year: int, month: int, day: int, hour: int, minute: int, second: int, millisecond: int, era: int) -> datetime.datetime:
        ...

    def to_four_digit_year(self, year: int) -> int:
        ...


class ISOWeek(System.Object):
    """This class has no documentation."""

    @staticmethod
    @overload
    def get_week_of_year(date: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    @staticmethod
    @overload
    def get_week_of_year(date: System.DateOnly) -> int:
        """
        Calculates the ISO week number of a given Gregorian date.
        
        :param date: A date in the Gregorian calendar.
        :returns: A number between 1 and 53 representing the ISO week number of the given Gregorian date.
        """
        ...

    @staticmethod
    def get_weeks_in_year(year: int) -> int:
        ...

    @staticmethod
    @overload
    def get_year(date: typing.Union[datetime.datetime, datetime.date]) -> int:
        ...

    @staticmethod
    @overload
    def get_year(date: System.DateOnly) -> int:
        """
        Calculates the ISO week-numbering year (also called ISO year informally) mapped to the input Gregorian date.
        
        :param date: A date in the Gregorian calendar.
        :returns: The ISO week-numbering year, between 1 and 9999.
        """
        ...

    @staticmethod
    def get_year_end(year: int) -> datetime.datetime:
        ...

    @staticmethod
    def get_year_start(year: int) -> datetime.datetime:
        ...

    @staticmethod
    def to_date_only(year: int, week: int, day_of_week: System.DayOfWeek) -> System.DateOnly:
        """
        Maps the ISO week date represented by a specified ISO year, week number, and day of week to the equivalent Gregorian date.
        
        :param year: An ISO week-numbering year (also called an ISO year informally).
        :param week: The ISO week number in the given ISO week-numbering year.
        :param day_of_week: The day of week inside the given ISO week.
        :returns: The Gregorian date equivalent to the input ISO week date.
        """
        ...

    @staticmethod
    def to_date_time(year: int, week: int, day_of_week: System.DayOfWeek) -> datetime.datetime:
        ...


class NumberStyles(Enum):
    """
    Contains valid formats for Numbers recognized by the Number
    class' parsing code.
    """

    NONE = ...

    ALLOW_LEADING_WHITE = ...
    """
    Bit flag indicating that leading whitespace is allowed. Character values
    0x0009, 0x000A, 0x000B, 0x000C, 0x000D, and 0x0020 are considered to be
    whitespace.
    """

    ALLOW_TRAILING_WHITE = ...
    """Bitflag indicating trailing whitespace is allowed."""

    ALLOW_LEADING_SIGN = ...
    """
    Can the number start with a sign char specified by
    NumberFormatInfo.PositiveSign and NumberFormatInfo.NegativeSign
    """

    ALLOW_TRAILING_SIGN = ...
    """Allow the number to end with a sign char"""

    ALLOW_PARENTHESES = ...
    """Allow the number to be enclosed in parens"""

    ALLOW_DECIMAL_POINT = ...

    ALLOW_THOUSANDS = ...

    ALLOW_EXPONENT = ...

    ALLOW_CURRENCY_SYMBOL = ...

    ALLOW_HEX_SPECIFIER = ...

    ALLOW_BINARY_SPECIFIER = ...
    """
    Indicates that the numeric string represents a binary value. Valid binary values include the numeric digits 0 and 1.
    Strings that are parsed using this style do not employ a prefix; "0b" cannot be used. A string that is parsed with
    the AllowBinarySpecifier style will always be interpreted as a binary value. The only flags that can
    be combined with AllowBinarySpecifier are AllowLeadingWhite and AllowTrailingWhite.
    The NumberStyles enumeration includes a composite style, BinaryNumber, that consists of
    these three flags.
    """

    INTEGER = ...

    HEX_NUMBER = ...

    BINARY_NUMBER = ...
    """Indicates that the AllowLeadingWhite, AllowTrailingWhite, and AllowBinarySpecifier styles are used. This is a composite number style."""

    NUMBER = ...

    FLOAT = ...

    CURRENCY = ...

    ANY = ...


