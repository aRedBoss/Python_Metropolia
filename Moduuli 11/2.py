class Car:
    def __init__(self, license_plate, top_speed):
        self.license_plate = license_plate
        self.top_speed = top_speed
        self.current_speed = 0
        self.odometer = 0
    def drive(self, hours, current_speed):
        self.current_speed = current_speed
        distance = self.current_speed * hours
        self.odometer += distance
    def info(self):
        print(f"License Plate: {self.license_plate}")
        print(f"Top Speed: {self.top_speed} km/h")
        print(f"Current Speed: {self.current_speed} km/h")
        print(f"Odometer Reading: {self.odometer} km")
class ElectricCar(Car):
    def __init__(self, license_plate, top_speed, battery_capacity):
        super().__init__(license_plate, top_speed)
        self.battery_capacity = battery_capacity
class GasolineCar(Car):
    def __init__(self, license_plate, top_speed, tank_capacity):
        super().__init__(license_plate, top_speed)
        self.tank_capacity = tank_capacity

car1 = ElectricCar("ABC-15", 180, 52.5)
car2 = GasolineCar("ACD-123", 165, 32.3)
car1.drive(3, 180)
car2.drive(3, 165)
car1.info()
car2.info()