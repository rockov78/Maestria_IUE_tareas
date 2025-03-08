from abc import ABC, abstractmethod
class Command(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def execute(self, drone):
        pass

class Forward(Command):
    def __init__(self, distance):
        self.distance = distance
    def execute(self, drone):
        if drone.consume_battery():
            return
        if not drone.flying:
            drone.report("Drone is not flying - unable to follow command")
            return
        
        drone.report(f"Moving forward {self.distance} units")
        if drone.direction == "N":
            drone.y += self.distance
        elif drone.direction == "S":
            drone.y -= self.distance
        elif drone.direction == "E":
            drone.x += self.distance
        elif drone.direction == "W":
            drone.x -= self.distance

class Backward(Command):
    def __init__(self, distance):
        self.distance = distance
    def execute(self, drone):
        if drone.consume_battery():
            return
        if not drone.flying:
            drone.report("Drone is not flying - unable to follow command")
            return
        drone.report(f"Moving backward {self.distance} units")
        if drone.direction == "N":
            drone.y -= self.distance
        elif drone.direction == "S":
            drone.y += self.distance
        elif drone.direction == "E":
            drone.x -= self.distance
        elif drone.direction == "W":
            drone.x += self.distance


class Turn_left(Command):
    def __init__(self):
        pass
    def execute(self, drone):
        if drone.consume_battery():
            return
        if not drone.flying:
            drone.report("Drone is not flying - unable to follow command")
            return
        drone.report("Turning left")
        if drone.direction == "N":
            drone.direction = "W"
        elif drone.direction == "S":
            drone.direction = "E"
        elif drone.direction == "E":
            drone.direction = "N"
        elif drone.direction == "W":
            drone.direction = "S"

class Turn_right(Command):
    def __init__(self):
        pass
    def execute(self, drone):
        if drone.consume_battery():
            return
        if not drone.flying:
            drone.report("Drone is not flying - unable to follow command")
            return
        drone.report("Turning right")
        if drone.direction == "N":
            drone.direction = "E"
        elif drone.direction == "S":
            drone.direction = "W"
        elif drone.direction == "E":
            drone.direction = "S"
        elif drone.direction == "W":
            drone.direction = "N"

class Land(Command):
    def __init__(self):
        pass
    def execute(self, drone):
        if not drone.flying:
            drone.report("Drone is not flying - unable to follow command")
            return
        drone.flying = False
        drone.report("landing")

class Take_off(Command):
    def __init__(self):
        pass
    def execute(self, drone):
        if drone.flying:
            drone.report("Drone is already flying")
            return
        if drone.battery > 0:
            drone.report("Taking off")
            if drone.consume_battery():
                return
            drone.flying = True
            
        
