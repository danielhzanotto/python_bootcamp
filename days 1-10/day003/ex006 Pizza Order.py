print("Welcome to Pizza Box")

print("Would you like a small, medium or large pizza? S, M, L")
size = input()
bill = 0

if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25

print("Would you like extra toppings? Y, N")
extra_toppings = input()
if extra_toppings == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

print("Would you like extra cheese? Y, N")
extra_cheese = input()
if extra_cheese == "Y":
    bill += 1

print(f"The total is {bill}")
