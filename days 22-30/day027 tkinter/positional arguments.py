def add(*args):
    for n in args:
        print(n)


add(5, 3, "thing", 5+7, "hello, world", 0000000, "sss")
print()
add(785, "this is a string", [1, 1, 2, 3, 5, 8, 13])


def summ(*args):
    sum = 0
    for n in args:
        sum += n
    return sum


print(summ(7, 4, 54, 333, 1+4, 9))
