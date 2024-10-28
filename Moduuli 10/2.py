class Elevator:
    def __init__(self, lowest, highest):
        self.lowest_floor = lowest
        self.highest_floor = highest
        self.current_floor = lowest
    def move_up(self):
        self.current_floor += 1
    def move_down(self):
        self.current_floor -= 1
    def move_to_floor(self, target_floor):
        while self.current_floor != target_floor:
            if self.current_floor < target_floor:
                self.move_up()
                print("Elevator has moved up")
            else:
                self.move_down()
                print("Elevator has moved down")
        print(self.current_floor)
class House:
    def __init__(self, lowest, highest, amount):
        self.lowest_floor = lowest
        self.highest_floor = highest
        self.elevators = []
        for _ in range(1, amount + 1):
            self.elevators.append(Elevator(lowest, highest))
    def run_elevator(self, elevator_number, target_floor):
        elevator = self.elevators[elevator_number - 1]
        elevator.move_to_floor(target_floor)
h = House(1, 10, 4)
h.run_elevator(1, 5)
h.run_elevator(2, 7)
h.run_elevator(2, 5)

 
        


            
    