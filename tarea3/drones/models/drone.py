import asyncio
from abc import ABC, abstractmethod

class Drone(ABC):
    def __init__(self, id, x, y, commands):
        self.id = id
        self.x = x
        self.y = y
        self.battery = 100
        self.delta_battery = 5
        self.speed = 1
        self.direction = "N"
        self.flying = True
        self.commands = commands

    @abstractmethod
    def execute(self, command):
        pass

    @abstractmethod
    def get_position(self):
        pass

    @abstractmethod
    def get_distance_to_base(self):
        pass

    @abstractmethod
    def report(self, message):
        pass

    def consume_battery(self):
        self.battery -= self.delta_battery
        if self.battery <= 0:
            self.battery = 0
            self.report("Battery empty - landing")
            self.flying = False  # El dron ya no está volando
            return True
        return False

    async def follow_commands(self):
        """Ejecuta comandos de manera asíncrona evitando recursión infinita."""
        while self.battery > 0 and self.flying:
            for command in self.commands:
                self.execute(command)
                if self.consume_battery():
                    self.report("Battery empty - landing")
                    return
                self.report(f"Posición actual: {self.get_position()}")  # ✅ Reportar la posición
                await asyncio.sleep(1)  # Simula tiempo de ejecución de comandos
            self.report("Sequence completed - repeating")
