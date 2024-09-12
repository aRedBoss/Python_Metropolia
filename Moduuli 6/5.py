def lista(numbers: list):
    new_lista = []
    for number in numbers:
        if number % 2 == 0:
            new_lista.append(number)
    return new_lista
print(lista([1, 2,3, 4, 5, 6, 7, 11, 12]))
