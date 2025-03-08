import unittest
import asyncio
from drones.models.quadcopter import Quadcopter
from drones.models.commands import Forward, Take_off, Land

class TestSimulacion(unittest.TestCase):

    def setUp(self):
        """Prepara un dron de prueba antes de cada test."""
        self.dron = Quadcopter("test", 0, 0, [Take_off(), Forward(3), Land()])

    def test_dron_creation(self):
        """Verifica que el dron se crea correctamente."""
        self.assertEqual(self.dron.id, "QC:test")
        self.assertEqual(self.dron.x, 0)
        self.assertEqual(self.dron.y, 0)

    def test_dron_execution(self):
        """Verifica que el dron ejecuta comandos sin fallar."""
        async def run_sim():
            await self.dron.follow_commands()

        asyncio.run(run_sim())

if __name__ == "__main__":
    unittest.main()
