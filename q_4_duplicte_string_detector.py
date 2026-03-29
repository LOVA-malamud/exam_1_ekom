words = []
duplicates = False

while True:
    user_input = input("enter string")
    if user_input == "quit":
        break

    if user_input in words:
        duplicates = True

    words.append(user_input)

if duplicates:
    print("duplicates found")
else:
    print("no duplicates found")
