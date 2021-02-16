import pytest

from my_date import Date, TimeDelta


@pytest.mark.parametrize("date,expected", [
    ("01.01.2001", "01.01.2001"),
    ("01.01.0001", "01.01.0001"),
    ("29.02.0016", "29.02.0016"),
    ("28.02.0111", "28.02.0111")
])
def test_create_date(date, expected):
    date = Date(date)
    assert str(date) == expected
