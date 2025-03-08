import asyncio
from drones.models.quadcopter import Quadcopter
from drones.models.commands import Forward, Backward, Turn_left, Take_off, Land, Turn_right

class DroneSimulator:
    def __init__(self, drones):
        self.drones = drones

    async def ejecutar_drones(self):
        """Ejecuta múltiples drones en paralelo y detecta colisiones."""
        while any(d.flying for d in self.drones):  # Mientras haya drones en vuelo
            await asyncio.gather(*(d.follow_commands() for d in self.drones))
            self.detect_collisions()  # Verifica colisiones en cada iteración

    def detect_collisions(self):
        """Detecta si dos o más drones están en la misma posición."""
        posiciones = {}
        for dron in self.drones:
            pos = dron.get_position()
            if pos in posiciones:
                print(f"⚠️ COLISIÓN DETECTADA en {pos} entre {posiciones[pos]} y {dron.id} ⚠️")
            else:
                posiciones[pos] = dron.id  # Guardamos la posición ocupada

async def main():
    drones = [
        Quadcopter("raptor", 0, 0, [Take_off(), Forward(3), Turn_left(), Forward(2), Land()]),
        Quadcopter("falcon", 1, 1, [Take_off(), Forward(2), Turn_right(), Forward(3), Land()])
    ]
    
    simulador = DroneSimulator(drones)
    await simulador.ejecutar_drones()

if __name__ == "__main__":
    asyncio.run(main())
