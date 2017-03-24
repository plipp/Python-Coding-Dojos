# actual code
def leap_year(year: int) -> bool:
    """
    Calculate if it is a leap year or not.
    A leap year is defined as one that
    - is divisible by 4,
    - but is not otherwise divisible by 100
    - unless it is also divisble by 400.

    :param year: the year
    :return: True if year is a leap year, False else

    >>> leap_year(1)
    False
    """
    pass


# py-test
def test_leap_year():
    assert leap_year(1) == False
