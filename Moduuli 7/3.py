airports = {"001" : "Helsinki",
              "002" : "London",
              "003" : "Istanpul"}

while True:
    user_input_choise = input("Add a new airport[1] \nSearch for an airport[2] \nExit[3] \n\nWhat would you like to do? ")
    if user_input_choise == "1":
        user_input_key = input("Enter airport ICAO code: ")
        user_input_value = input("Enter airport name: ")
        airports[user_input_key] = user_input_value
    elif user_input_choise == "2":
        user_input_key = input("What is the airport ICAO code? ")
        print(airports[user_input_key])
    elif user_input_choise == "3":
        print("You have successfully exited.")
        break