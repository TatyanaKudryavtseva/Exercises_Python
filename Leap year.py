def is_year_leap(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0

x = int(input("Введите год"))
var = (x % 400 == 0) or ((x % 4 == 0) and (x % 100 != 0))
print(var)