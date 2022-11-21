print("Write a number")
number = int(input())
modulo = number % 2  # calculo do resto usando %, o resultado é o resto da divisão inteira

if modulo == 0:
    print("This is an even number")
else:
    print("This is an odd number")
