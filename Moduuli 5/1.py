import random

my_list = []

number_of_dice = int(input("Give me number of dice: "))

for number in range(number_of_dice):
    random_number = random.randint(1, 6)
    my_list.append(random_number)
print(sum(my_list))

