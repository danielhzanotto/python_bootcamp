def switch(first, sec):
    a = first
    b = sec
    print("a: {} \nb: {}".format(a, b))
    c = a
    a = b
    b = c
    print("a: {} \nb: {}".format(a, b))


switch(input("a: "), input("b: "))
