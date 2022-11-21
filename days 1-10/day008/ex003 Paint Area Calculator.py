print("What's the wall length?")
wall_length = float(input())

print("What's the wall heigth?")
wall_heigth = float(input())

print("How many liters do you need to paint a m²?")
liters_of_paint = float(input())

print("How many layers does the paint need?")
num_of_layers = float(input())


def amount_of_paint(length, height, liters, layers):
    total = length * height / liters * layers
    print(f"You need {total} liters of paint")


amount_of_paint(wall_length, wall_length, liters_of_paint, num_of_layers)
