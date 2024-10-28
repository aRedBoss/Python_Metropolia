from random import randint

class Car:
    def __init__(self, license_plate, top_speed):
        self.license_plate = license_plate
        self.top_speed = top_speed
        self.current_speed = 0
        self.distance_traveled = 0

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
        return f"Car {self.license_plate}: Speed = {self.current_speed} km/h, Distance traveled = {self.distance_traveled} km"


class Competitive:
    def __init__(self, name, length, cars):
        self.name = name
        self.length = length
        self.cars = cars

    def tunti_kuluu(self):
        for car in self.cars:
            car.accelerate(randint(-10, 15))
            car.drive(1)

    def tulosta_tilanne(self):
        print(f"\nStatus after hours:")
        for car in self.cars:
            print(car.info())
        print("-" * 40)

    def kilpailu_ohi(self):
        for car in self.cars:
            if car.distance_traveled >= self.length:
                return True
        return False


cars = [Car(f"ABC-{i}", randint(100, 200)) for i in range(1, 11)]
race = Competitive("rally", 8000, cars)

hours = 0
while not race.kilpailu_ohi():
    race.tunti_kuluu()
    hours += 1

    if hours % 10 == 0:
        race.tulosta_tilanne()

race.tulosta_tilanne()
print("\nThe race is over!")