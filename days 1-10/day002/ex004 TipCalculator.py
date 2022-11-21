print("What was the total bill ($)?")
bill = float(input())
print(bill)

print("What percentage tip would you like to give (%)?")
tip_percentage = float(input())
print(tip_percentage, "%")

print("How many people to split the bill?")
number_of_people = int(input())
print(number_of_people)

total_bill = bill + bill * (tip_percentage / 100)

split_bill = total_bill / number_of_people

print(f"Each person will pay ${split_bill:.2f}")
