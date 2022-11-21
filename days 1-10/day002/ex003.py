years = int(input("how old are you?"))
years_left = 90 - years
months_left = years_left * 12
weeks_left = years_left * 52
days_left = years_left * 365

print(
    f"you have {days_left} days, {weeks_left} months and {months_left} months left.")
