import pytest

from my_date import Date, TimeDelta


@pytest.mark.parametrize("date,expected", [
    ("01.01.2001", "01.01.2001"),
    ("01.01.0001", "01.01.0001"),
    ("01.01.0011", "01.01.0011"),
    ("01.01.0111", "01.01.0111")
])
def test_create_date(date, expected):
    date = Date(date)
    assert date == expected
