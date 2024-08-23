fish_size = int(input("How long is the fish? Give answar in cm: "))

missing_size = 37 - fish_size

if fish_size >= 37:
    print("Nice catch!")
elif fish_size < 37 and fish_size > 0:
    print(f"throw the fish back. Your fish needs to be {missing_size} cm bigger")
else:
    print("Huh!")
