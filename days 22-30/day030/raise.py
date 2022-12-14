height = float(input("Height (m): "))
weight = float(input("Weight (kg): "))

if height > 2.5:
    raise ValueError("Human height should not be over 2.5m")

bmi = weight / height ** 2
