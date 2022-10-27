from leap_year import isLeapYear

# Divisible by 4 but not divisible by 100.
def test_isLeapYear_div4ButNot100() -> None:
    assert isLeapYear(2020)

# Divisible by 400.
def test_iLeapYear_div400() -> None:
    assert isLeapYear(2000)

# Not divisible by 4.
def test_isLeapYear_notDiv4() -> None:
    assert not isLeapYear(1999)

# Divisible by 100, but not by 400.
def test_isLeapYear_div100Not400() -> None:
    assert not isLeapYear(1700)
