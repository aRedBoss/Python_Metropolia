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
            else:
                self.move_down()
        print(self.current_floor)

a = Elevator(1, 10)
a.move_to_floor(7)
a.move_to_floor(2)
