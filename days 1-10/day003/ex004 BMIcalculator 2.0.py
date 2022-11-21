print("type your weight (kg)")
weight = float(input("type your weight"))

print("type your height (m)")
height = float(input("type your height"))

print("weight: ", weight)
print("height: ", height)

bmi = weight / height**2
print("bmi: {:.2f}".format(bmi))

if bmi < 18.5:
    print("You are underwheight")
elif bmi < 25:
    print("You have a normal weight")
elif bmi < 30:
    print("You are overweight")
elif bmi < 35:
    print("You are obese")
elif bmi >= 35:
    print("You are clinically obese")
