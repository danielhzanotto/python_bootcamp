print("Welcome to the python calculator!")


def operation(num1, op, num2):
    result = 0
    if op == "+":
        result = num1 + num2
    elif op == "-":
        result = num1 - num2
    elif op == "*":
        result = num1 * num2
    elif op == "/":
        result = num1 / num2
    else:
        print("wrong operator")

    return result


keep_on = "N"

final_result = 0

while keep_on == "Y" or keep_on == "N":
    if keep_on == "Y":
        number1 = final_result
    else:
        print("Type a number:")
        number1 = float(input())

    print("Choose an operation:\n+\n-\n*\n/")
    operator = input()

    print("Type another number")
    number2 = float(input())

    final_result = operation(number1, operator, number2)

    print(f"{number1} {operator} {number2} = {final_result}")

    print(
        f"Type Y to continue calculating with {final_result}, type N to start a new calculation or type any other letter to close")
    keep_on = input().upper()
