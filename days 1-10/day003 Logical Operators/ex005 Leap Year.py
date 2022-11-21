print("Type a year")
year_test = int(input())
is_leap = True


def leap(year):
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

    if is_leap == True:
        print("Leap Year")
    else:
        print("Not Leap Year")


leap(year_test)
