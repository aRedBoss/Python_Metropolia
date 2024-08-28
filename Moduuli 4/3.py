my_list = []
while True:
    number = input("Give me a number: ")
    if number != "":
        my_list.append(int(number))
    else:
        break
#print(my_list)
print(f"Smallest: {min(my_list)} \nBiggest: {max(my_list)}")
