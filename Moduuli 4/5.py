attempts = 5
correct_user_name = "name"
correct_password = "12345"
while True:
    print(f"You have {attempts} attempts!")
    user_name_given = input(f"You have attempts. Enter user name:")
    password_given = input(f"You have attempts. Enter password:")
    attempts -= 1
    if attempts == 0:
        print("Access denied!")
        break
    if user_name_given == correct_user_name:
        if password_given == correct_password:
            print("Wellcome!")
            break

    