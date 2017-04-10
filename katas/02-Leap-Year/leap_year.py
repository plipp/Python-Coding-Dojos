# actual code
def leap_year(year: int) -> bool:
    """
    Calculate if it is a leap year or not.
    A leap year is defined as one that
    - is divisible by 4,
    - but is not otherwise divisible by 100
    - unless it is also divisible by 400.

    :param year: the year
    :return: True if year is a leap year, False else

    >>> leap_year(1)
    False
    """
    result = False
    if year % 4 == 0:
        result = True
    if year % 100 == 0 and year % 400 != 0:
        result = False
    return result


# py-test
def test_leap_year_basic():
    assert leap_year(1) is False


def test_validate_leap_year():
    assert leap_year(4) is True


def test_leap_year_non_div_by_100():
    assert leap_year(100) is False


def test_leap_year_atypical():
    assert leap_year(400) is True
