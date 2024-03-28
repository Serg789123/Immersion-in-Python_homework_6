# __all__ = ['check_date']

def is_not_leap(year: int) -> bool: # проверка на високосность
    return not(year % 400 == 0 or year % 100 != 0 and year % 4 == 0)

day, month, year = map(int, input('Введите дату в формате чч мм гггг через пробел:').split())
def check_date(day, month, year):

    if year < 1 or year > 9999 or month < 1 or month > 12 or day < 1 or day > 31:
        return  False
    if month in (4, 6, 9, 11) and day > 30:
        return False
    elif month == 2 and day > 29:
        return False
    elif month == 2 and day > 28 and is_not_leap(year):
        return False
    else:
        return True

if __name__ == '__main__':
    print(check_date(day, month, year))
