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
        print(self.distance_traveled)
car_1 = Car("ABC-123", 160)

car_1.accelerate(30)
car_1.accelerate(50)
car_1.accelerate(70)
car_1.accelerate(-80)
car_1.drive(1.5)
car_1.info()