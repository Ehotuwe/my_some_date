import pytest

from my_date import Date, TimeDelta


@pytest.mark.parametrize("day, month, year, expected", [
    (50, 20, 2001, "50.20.2001"),
    (0, 20, 2001, "0.20.2001"),
    (50, 0, 2001, "50.0.2001"),
    (50, 20, 0, "50.20.0"),

])
def test_timedelta(day, month, year, expected):
    date_ = TimeDelta(days=day, months=month, years=year)
    assert f'{date_.day}.{date_.month}.{date_.year}' == expected


@pytest.mark.parametrize("date_,expected", [
    ("1.1.2001", "01.01.2001"),
    ("1.1.1", "01.01.0001"),
    ("29.2.16", "29.02.0016"),
    ("28.2.111", "28.02.0111")
])
def test_date_1arg_str(date_, expected):
    date_ = Date(date_)
    assert str(date_) == expected


@pytest.mark.parametrize("day, month, year, expected", [
    (1, 1, 2001, "01.01.2001"),
    (1, 1, 1, "01.01.0001"),
    (29, 2, 16, "29.02.0016"),
    (28, 2, 111, "28.02.0111")
])
def test_date_3arg_str(day, month, year, expected):
    date_ = Date(day, month, year)
    assert str(date_) == expected


@pytest.mark.parametrize("date_,expected", [
    ("01.01.2001", "(1,1,2001)"),
    ("01.01.0001", "(1,1,1)"),

])
def test_date_1arg_repr(date_, expected):
    date_ = Date(date_)
    assert repr(date_) == expected


@pytest.mark.parametrize("date_,value, expected", [
    ("01.01.2001", 20, "20.01.2001"),
    ("01.01.0001", 5, "05.01.0001"),

])
def test_setter_day(date_, value, expected):
    date_ = Date(date_)
    date_.day = value
    assert str(date_) == expected


@pytest.mark.parametrize("date_,value, expected", [
    ("01.01.2001", 5, "01.05.2001"),
    ("01.01.0001", 10, "01.10.0001"),

])
def test_setter_month(date_, value, expected):
    date_ = Date(date_)
    date_.month = value
    assert str(date_) == expected


@pytest.mark.parametrize("date_,value, expected", [
    ("01.01.2001", 2005, "01.01.2005"),
    ("01.01.0001", 2010, "01.01.2010"),

])
def test_setter_year(date_, value, expected):
    date_ = Date(date_)
    date_.year = value
    assert str(date_) == expected


@pytest.mark.parametrize("day,month,year", [
    (41, 1, 2005),
    (28, 14, 2004),
    (27, 11, 10000),
    ('some_str', 11, 10000)

])
def test_create_3date_bad(day, month, year):
    with pytest.raises(ValueError):
        Date(day, month, year)


@pytest.mark.parametrize("date_", [
    ("01.01.2001.44"),

])
def test_create_1date_bad(date_):
    with pytest.raises(ValueError):
        Date(date_)


@pytest.mark.parametrize("date_1, date_2, expected", [
    ("1.2.2016", "2.3.2007", 3258),

])
def test_sub(date_1, date_2, expected):
    date_1 = Date(date_1)
    date_2 = Date(date_2)
    assert date_1 - date_2 == expected


@pytest.mark.parametrize("date_1, day_delta, month_delta, year_delta , expected", [
    ("1.2.2016", 27, 9, 10, '28.11.2026'),
    ("1.2.2016", 30, 0, 10, '02.03.2026'),
    ("1.2.2017", 30, 0, 10, '03.03.2027'),
    ("01.12.2014", 31, 1, 1, '01.02.2016'),
    ("1.11.2015", 31, 3, 3, '02.03.2019'),
    ("01.12.2014", 31, 2, 1, '01.03.2016')


])
def test_add(date_1, day_delta, month_delta, year_delta, expected):
    date_1 = Date(date_1)
    assert str(date_1 + TimeDelta(days=day_delta, months=month_delta, years=year_delta)) == expected


@pytest.mark.parametrize("date_1, day_delta, month_delta, year_delta , expected", [
    ("1.2.2016", 27, 9, 10, '28.11.2026'),
    ("1.2.2016", 30, 0, 10, '02.03.2026'),
    ("1.2.2017", 30, 0, 10, '03.03.2027'),
    ("01.12.2014", 31, 1, 1, '01.02.2016')
])
def test_iadd(date_1, day_delta, month_delta, year_delta, expected):
    date_1 = Date(date_1)
    date_1 += TimeDelta(days=day_delta, months=month_delta, years=year_delta)
    assert str(date_1) == expected
