import math
def calculator(diameter: float, price: float):
    radios = diameter / 2
    area = math.pi * radios**2
    area = area / 10000
    unit_price = area / price
    return unit_price
first_pizza=calculator(44.3, 5.0)

second_pizza=calculator(56.5, 6.0)

if first_pizza > second_pizza:
    print("first pizza bigger")
else:
    print(f"second pizza bigger")



