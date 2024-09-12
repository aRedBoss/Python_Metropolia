from random import randint

def dice():
    return randint(1, 6)

while True:
    roll = dice()
    print(roll)
    if roll == 6:
        break