import time

# def add(n1, n2):
#     return n1 + n2


# def subtract(n1, n2):
#     return n1 - n2


# def multiply(n1, n2):
#     return n1 - n2


# def divide(n1, n2):
#     return n1 / n2


# def calculate(calc, n1, n2):
#     return calc(n1, n2)


# print(calculate(add, 2, 3))


# def outer_function():
#     print("I'm outer")

#     def nested_function():
#         print("I'm inner")

#     return nested_function


# inner_function = outer_function()
# inner_function()

def delay_decorator(function):
    def wrapper_function():
        time.sleep(2)
        function()

    return wrapper_function


@delay_decorator
def say_hello():
    print("Hello")


@delay_decorator
def say_bye():
    print("Bye")


def say_greetings():
    print("Greetings")


say_hello()
