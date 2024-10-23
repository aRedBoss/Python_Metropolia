from random import randint

class Car:
    current_speed = 0
    distance_traveled = 0
    def __init__(self, license_plate, top_speed):
        self.license_plate = license_plate
        self.top_speed = top_speed
    def accelerate(self, change):
        self.current_speed += change
        if self.current_speed > self.top_speed:
            self.current_speed = self.top_speed
        elif self.current_speed < 0:
            self.current_speed = 0
    def drive(self, hours):
        distance = self.current_speed * hours
        self.distance_traveled += distance
    def info(self):
        return f"Car {self.license_plate}: Distance traveled = {self.distance_traveled} km"

cars = [Car(f"ABC-{i}", randint(100, 200)) for i in range(1, 11)]
while True:
    for car in cars:
        car.accelerate(randint(-10, 15))
        car.drive(1)
        
    if car.distance_traveled >= 10000:
        break
    else:
        continue
    break

print("\nFinal status of all cars: \n")

for car in cars:
    print(car.info())

