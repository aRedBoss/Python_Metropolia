from random import randint

def dice(maximum: int):
    return randint(1, maximum)

user_input = int(input("Give me number: "))

while True:
    roll = dice(user_input)
    print(roll)
    if roll == user_input:
        break