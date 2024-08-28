my_list = []

while True:
    number = (input("Give me number: "))
    if number != "":
        my_list.append(int(number))
    else:
        break
    
sorted_list = sorted(my_list, reverse=True)
print(sorted_list[:5])