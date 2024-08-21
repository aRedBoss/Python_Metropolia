leivisköinä = float(input("Give me leiviskät: "))
nauloina = float(input("Give me naulat: "))
luoteina = float(input("Give me luodit: "))

leivisköinä = leivisköinä * 8512
nauloina = nauloina * 425.6
luoteina = luoteina * 13.3

totalInGram = leivisköinä + nauloina + luoteina

totalInKiloGram = totalInGram // 1000
remainInGram = totalInGram % 1000

print("Massa nykymittojen mukaan:")
print(f"{int(totalInKiloGram)} kilogrammaa ja {remainInGram: .2f} grammaa." )