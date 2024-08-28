while True:
    inches = float(input("Give me inches: "))
    cm = inches * 2.54
    if inches >= 0:
        print(f"{inches} inches is {cm} cm")
    else:
        break