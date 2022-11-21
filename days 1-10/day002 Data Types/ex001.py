# num_char = len(input("What's your name?"))
# print("Your name has", num_char, "characters")


number = str(input("number"))
i = 0
final = "0"
print(number)

for x in number:
    print("{}º: {} + {} = {}". format(number.index(x) + 1, i, x, i + int(x)))
    final = final + " + " + x
    i = i + int(x)

print(final, "=", i)
