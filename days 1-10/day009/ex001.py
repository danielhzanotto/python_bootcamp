programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again.",
    "Loop": "The action of doing something over and over again",
}

print(programming_dictionary["Bug"])

# here we are changing the value of a key
programming_dictionary["Loop"] = "A piece of code that you can easily call over and over again."

# creating an empty dictionary
empty_dictionary = {}

#loop through a dictionary
for thing in programming_dictionary:
    print(thing) #vai puxar só as chaves
    print(programming_dictionary[thing]) #vai puxar os valores