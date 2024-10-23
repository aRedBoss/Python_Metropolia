class Car:
    current_speed = 0
    distance_traveled = 0
    def __init__(self, license_plate, top_speed):
        self.license_plate = license_plate
        self.top_speed = top_speed
    def info(self):
        print(f"{self.current_speed}\n{self.distance_traveled}\n{self.license_plate}\n{self.top_speed} Km/h")

car_1 = Car("ABC-123", 142)
car_1.info()