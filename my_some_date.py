from typing import Optional, overload


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

        if len(args) == 3 and all(isinstance(i, int) for i in args):

            self._day, self._month, self._year = int(args[0]), int(args[1]), int(args[2])
            self.is_valid_date(self._day, self._month, self._year)
        elif len(args) == 1 and isinstance(args[0], str):
            values = args[0].split('.')
            if len(values) != 3:
                raise ValueError('ошибка в строке')
            self._day, self._month, self._year = int(values[0]), int(values[1]), int(values[2])
            self.is_valid_date(self._day, self._month, self._year)
        else:
            raise ValueError('много или мало значений')

    def __str__(self) -> str:
        """Возвращает дату в формате dd.mm.yyyy"""
        return f"{self.day}.{self.month}.{self.year}"

    def __repr__(self) -> str:
        """Возвращает дату в формате Date(day, month, year)"""
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
        if cls.is_leap_year(year) == True:
            return cls.day_in_month[1][month - 1]
        else:
            return cls.day_in_month[0][month - 1]

    @classmethod
    def is_valid_date(cls, day: int, month: int, year: int):
        """Проверяет, является ли дата корректной"""

        if not (1 <= int(year) <= 2021):
            raise ValueError
        if not (1 <= int(month) <= 12):
            raise ValueError
        if not (1 <= int(day) <= cls.get_max_day(month, year)):
            raise ValueError

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, value: int):
        """value от 1 до 31. Проверять значение и корректность даты"""
        self.is_valid_date(value, self.month, self.year)
        self._day = value



    @property
    def month(self):

        return self._month

    @month.setter
    def month(self, value: int):
        """value от 1 до 12. Проверять значение и корректность даты"""
        if 1 <= value <= 12:
            self._month = value
        else:
            raise ValueError


    @property
    def year(self):

        return self._year

    @year.setter
    def year(self, value: int):
        """value от 1 до ... . Проверять значение и корректность даты"""
        if 1 <= value <= 2021:
            self._year = value
        else:
            raise ValueError

    def __sub__(self, other: "Date") -> int:
        """Разница между датой self и other (-)"""

    def __add__(self, other: TimeDelta) -> "Date":
        """Складывает self и некий timedeltа. Возвращает НОВЫЙ инстанс Date, self не меняет (+)"""

    def __iadd__(self, other: TimeDelta) -> "Date":
        """Добавляет к self некий timedelta меняя сам self (+=)"""


def main():
    date = Date(30, 4, 2016)
    date2 = Date('30.02.2020')
    print(repr(date.day))

    print(date)
    print(date2)


if __name__ == '__main__':
    main()
