print("type your weight (kg)")
weight = float(input("type your weight"))

print("type your height (m)")
height = float(input("type your height"))

print("weight: ", weight)
print("height: ", height)

bmi = weight / height**2
print("bmi: {:.2f}".format(bmi))
