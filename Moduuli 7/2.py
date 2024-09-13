names = set()

while True:
    user_input = input("Give me name: ").strip()
    if user_input == "":
        print("Empty input detected, breaking the loop.")
        break
    elif user_input not in names:
        names.add(user_input)
        print("New name.")
    else:
        print("Previously entered name.")
for name in names:
    print(names)
    