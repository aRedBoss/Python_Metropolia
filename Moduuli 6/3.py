def converter(gallons: int):
    liters = gallons * 3.785
    return liters
while True:
    user_input = int(input("Number of gallons: "))
    if user_input < 0:
        print("Invalid input!")
        break
    else:
        print(converter(user_input))