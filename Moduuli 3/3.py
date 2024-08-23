gender = input("What is your gender: ").lower()
hemoglobin_level = int(input("What is your hemoglobin level: "))

if gender == "women":
    if hemoglobin_level >= 117 and hemoglobin_level <= 175:
        print("Hemoglobin level is normal.")
    elif hemoglobin_level < 117 and hemoglobin_level > 0:
        print("Hemoglobin level is low.")
    elif hemoglobin_level > 175:
        print("Hemoglobin level is high.")
    else:
        print("Error.")

if gender == "men":
    if hemoglobin_level >= 134 and hemoglobin_level <= 195 :
        print("Hemoglobin level is normal.")
    elif hemoglobin_level < 134 and hemoglobin_level > 0:
        print("Hemoglobin level is low.")
    elif hemoglobin_level > 195:
        print("Hemoglobin level is high.")
    else:
        print("Error.")