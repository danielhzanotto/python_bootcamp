print("Type a year")
year = int(input())
print("Type a month")
month = int(input())


def leap(year):
    is_leap = True

    if year % 4 == 0:
        is_leap = True
        if year % 100 == 0:
            is_leap = False
            if year % 400 == 0:
                is_leap = True
            else:
                is_leap = False
        else:
            is_leap = True
    else:
        is_leap = False

    return is_leap


def days_in_month(y, m):
    if month > 12 or month < 1:
        print('Type a valid month')
    month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if m == 2 and leap(y):
        return 29
    return month_days[m - 1]


days = days_in_month(year, month)
print(days)
