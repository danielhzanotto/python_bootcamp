alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y",
            "z", " ", "a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]


print("Type a message")
message = input().lower()
print("Whats the shift code?")
shift_index = int(input())
print("Would you like to encode or decode?")
operation = input().lower()

shift_index = shift_index % (len(alphabet) / 2)


def encrypt(code, text, shift):
    encrypted_message = ""

    for letter in text:
        position = alphabet.index(letter)
        new_position = 0
        if code == "encode":
            new_position = position + shift
        elif code == "decode":
            new_position = position - shift
        else:
            print("End of program")
            break
        new_letter = alphabet[int(new_position)]
        encrypted_message += new_letter
    print(encrypted_message)


encrypt(operation, message, shift_index)

print("Would you like to run again? Y / N")
keep_on = input()

while keep_on == "Y":

    print("Type a message")
    message = input().lower()
    print("Whats the shift code?")
    shift_index = int(input())
    shift_index = shift_index % (len(alphabet) / 2)
    print("Would you like to encode or decode?")
    operation = input().lower()
    encrypt(operation, message, shift_index)
    print("Would you like to run again? Y / N")
    keep_on = input()
