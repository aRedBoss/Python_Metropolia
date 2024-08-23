year_given = int(input("Give me a year: "))

if year_given % 4 == 0 and year_given % 100 != 0 or year_given % 400 == 0:
    print("This is a leap year.")
else:
    print("This is not a leap year.")