def leap_year(year):
    if year % 100 == 0:
        return bool(year % 400 == 0)
    return bool(year % 4 == 0)
