import random
correct_number = random.randint(1, 10)

while True:
    guess = int(input("Give me a guess: "))
    if guess != correct_number:
        if guess > correct_number:
            print("Your guess is bigger than correct number!")
        elif guess < correct_number:
            print("Your guess is smaller than correct number!")
    elif guess == correct_number:
        print("Correct!")
        break
