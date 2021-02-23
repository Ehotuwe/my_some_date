import pytest

from my_date import Date, TimeDelta


@pytest.mark.parametrize("date,expected", [
    ("1.1.2001", "01.01.2001"),
    ("1.1.1", "01.01.0001"),
    ("29.2.16", "29.02.0016"),
    ("28.2.111", "28.02.0111")
])
def test_date_1arg_str(date, expected):
    date = Date(date)
    assert str(date) == expected


@pytest.mark.parametrize("day, month, year, expected", [
    (1, 1, 2001, "01.01.2001"),
    (1, 1, 1, "01.01.0001"),
    (29, 2, 16, "29.02.0016"),
    (28, 2, 111, "28.02.0111")
])
def test_date_3arg_str(day, month, year, expected):
    date = Date(day, month, year)
    assert str(date) == expected


@pytest.mark.parametrize("day", [41, -1, "some_str"])
def test_create_day_bad(day):
    with pytest.raises(ValueError):
        Date(day)


@pytest.mark.parametrize("month", [14, -1, "some_str"])
def test_create_month_bad(month):
    with pytest.raises(ValueError):
        Date(month)

@pytest.mark.parametrize("year", [-1, "some_str"])
def test_create_year_bad(year):
    with pytest.raises(ValueError):
        Date(year)
