print("Welcome to the rollercoaster")

height = int(input("What's your height in cm?"))
bill = 0

if height > 130:
    age = int(input("How old are you?"))
    print("Just hop on!")
    if age < 12:
        bill = 5
        print("Child tickets are $5")
    elif age >= 12 and age < 18:
        bill = 7
        print("Youth tickets are $7")
    else:
        bill = 12
        print("Adult tickets are $12")

    photo = input("Do you want a photo taken? Y or N")
    if photo == "Y":
        bill += 3

    print(f"Total is ${bill}")

else:
    print("Sorry, you can't ride the rollercoaster")
