from typing import Optional, overload
import logging

logger = logging.getLogger(__name__)


class TimeDelta:
    def __init__(self, days: Optional[int] = None, months: Optional[int] = None, years: Optional[int] = None):
        ...


class Date:
    """Класс для работы с датами"""
    day_in_month = ((31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31), (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31))

    @overload
    def __init__(self, day: int, month: int, year: int):
        """Создание даты из трех чисел"""

    @overload
    def __init__(self, date: str):
        """Создание даты из строки формата dd.mm.yyyy"""

    def __init__(self, *args):
        logger.debug('start init')
        if len(args) == 3 and all(isinstance(i, int) for i in args):

            self._day, self._month, self._year = int(args[0]), int(args[1]), int(args[2])
            logger.debug('created (day, month, year)')
            self.is_valid_date(self._day, self._month, self._year)
        elif len(args) == 1 and isinstance(args[0], str):
            values = args[0].split('.')
            if len(values) != 3:
                raise ValueError('ошибка в строке')
            self._day, self._month, self._year = int(values[0]), int(values[1]), int(values[2])
            logger.debug('created (day.month.year)')
            self.is_valid_date(self._day, self._month, self._year)
        else:
            raise ValueError('много или мало значений')
        logger.debug('end init')

    def __str__(self) -> str:
        """Возвращает дату в формате dd.mm.yyyy"""
        logger.debug('call __str__')
        return f"{self.day:02d}.{self.month:02d}.{self.year:04d}"

    def __repr__(self) -> str:
        """Возвращает дату в формате Date(day, month, year)"""
        logger.debug('call __repr__')
        return f"({self.day},{self.month},{self.year})"

    @classmethod
    def is_leap_year(cls, year: int) -> bool:
        """Проверяет, является ли год високосным"""
        if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
            return True
        else:
            return False

    @classmethod
    def get_max_day(cls, month: int, year: int) -> int:
        """Возвращает максимальное количество дней в месяце для указанного года"""
        return cls.day_in_month[cls.is_leap_year(year)][month - 1]

    @classmethod
    def is_valid_date(cls, day: int, month: int, year: int):
        """Проверяет, является ли дата корректной"""

        if not (1 <= int(year) <= 2021):
            raise ValueError('проблемы с годом')
        if not (1 <= int(month) <= 12):
            raise ValueError('проблемы с месяцем')
        if not (1 <= int(day) <= cls.get_max_day(month, year)):
            raise ValueError('проблемы с днем')

    @property
    def day(self):
        logger.debug('call property day')
        return self._day

    @day.setter
    def day(self, value: int):
        """value от 1 до 31. Проверять значение и корректность даты"""
        logger.debug('call setter day with value %s', value)

        self.is_valid_date(value, self.month, self.year)
        logger.debug('valid day')
        self._day = value

    @property
    def month(self):
        logger.debug('call property month')
        return self._month

    @month.setter
    def month(self, value: int):
        """value от 1 до 12. Проверять значение и корректность даты"""
        logger.debug('call setter month with value %s', value)
        self.is_valid_date(self.day, value, self.year)
        logger.debug('valid month')
        self._month = value

    @property
    def year(self):
        logger.debug('call property year')
        return self._year

    @year.setter
    def year(self, value: int):
        """value от 1 до ... . Проверять значение и корректность даты"""
        logger.debug('call setter year with value %s', value)
        self.is_valid_date(self.day, self.month, value)
        logger.debug('valid year')
        self._year = value

    @classmethod
    def count_day(cls, day: int, month: int, year: int):
        """Возвращает количество дней от 01.01.01 по текущую дату"""
        all_year_s = 0

        delta_days_s = day

        for leap in range(1, year):
            if cls.is_leap_year(leap):
                all_year_s += 366
            else:
                all_year_s += 365

        for month_a in range(1, month):
            delta_days_s += cls.get_max_day(month_a, year)

        return all_year_s + delta_days_s

    def __sub__(self, other: "Date") -> int:
        """Разница между датой self и other (-)"""
        if isinstance(other, Date):
            all_self_day = self.count_day(self.day, self.month, self.year)
            all_other_day = other.count_day(other.day, other.month, other.year)
            return all_self_day - all_other_day

    def __add__(self, other: TimeDelta) -> "Date":
        """Складывает self и некий timedeltа. Возвращает НОВЫЙ инстанс Date, self не меняет (+)"""

    def __iadd__(self, other: TimeDelta) -> "Date":
        """Добавляет к self некий timedelta меняя сам self (+=)"""


def main():
    logging.basicConfig()
    logger.setLevel(logging.DEBUG)
    logger.debug('start main')
    date = Date(1, 2, 2016)
    logger.debug('created date')
    date2 = Date('1.1.2001')
    logger.debug('created date2')
    date3 = Date(1, 3, 2018)
    logger.debug('created date')
    print(date - date3)
    # print(repr(date2.month))

    # print(date)
    # print(date2)
    # print()
    logger.debug('end main')
    # date.day=3
    # print(date)


if __name__ == '__main__':
    main()
