from .drone import Drone


class Quadcopter(Drone):

    def __init__(self, id, x, y, commands):
        super().__init__(f"QC:{id}", x, y, commands)

    def execute(self, command):
        command.execute(self)
        self.report(f"Position: {self.get_position()}")
    
    def get_position(self):
        return self.x, self.y
    
    def get_distance_to_base(self):
        return abs(self.x) + abs(self.y)
    
    def report(self, message):
        print(f"{self.id}: {message} - Battery: {self.battery}%")

    