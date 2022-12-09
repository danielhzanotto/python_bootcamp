# kwargs create an dictionary with arguments from the function


def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)


calculate(2, add=3, multiply=5)


class Car:
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")


# create a class with key words arguments

my_car = Car(make="FIAT", model="Uno", color="Red", seats=5)
print(my_car)
