# file not found

try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["doajisd"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("something")
except KeyError as error_message:
    print(f"The key {error_message} does not exist")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("file was closed")
