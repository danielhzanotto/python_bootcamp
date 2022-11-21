def prime_checker(n):
    number = int(n)
    while not type(number) == int:
        number = int(input())

    prime_counter = 0

    numbers_until = []

    for n in range(1, number + 1):
        numbers_until.append(n)

    for n in numbers_until:
        if number % n == 0:
            prime_counter += 1

    if prime_counter == 2:
        print(f"The number {number} is prime")
    else:
        print(f"The number {number} is NOT prime")


prime_checker(input())
