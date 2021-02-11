# 1. Реализовать класс Date и TimeDelta
# 2. Протестировать (полностью покрыть тестами). Не забудь проверить даты на корректность.

# При разработке использовать github
# * Настроить Jenkins CI для проекта на странице github
# * Создать пакет (модуль) из проекта и выгрузить на https://test.pypi.org/

# * - подробно разберем на следующей практике

self_day=1
self_month=2
self_year=2008

def is_valid_date(day: int, month: int, year: int):
    """Проверяет, является ли дата корректной"""

    if not year > 0:
        raise ValueError('год')
    if not (1 <= month <= 12):
        raise ValueError('месяц')
    if not (1 <= day <=29):
        raise ValueError('число')
# print(is_valid_date(30,2,2020))
is_valid_date(30,2,2020)
# print(is_valid_date(self_day,self_month,self_year))