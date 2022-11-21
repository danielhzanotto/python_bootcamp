def format_name(f, l):
    if not f.isalpha() or not l.isalpha():
        return "Type a valid name"
    return f"{f} {l}"


first_name = input("Type your first name").title()

last_name = input("Type your last name").title()

name = format_name(first_name, last_name)

print(name)
