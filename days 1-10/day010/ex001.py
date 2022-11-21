def format_name(f, l):
    return f"{f} {l}"


first_name = input("Type your first name").title()

last_name = input("Type your last name").title()

name = format_name(first_name, last_name)

print(name)
