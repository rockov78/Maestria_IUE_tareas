"""
test_download_temperatures.py

Este script importa la función `download_temperatures` del módulo download_temperatures
y la ejecuta, mostrando los resultados y midiendo el tiempo de ejecución para fines de benchmark.
"""

import asyncio
import time
from concurrence_py.download_temperatures import download_temperatures


def main():
    start = time.perf_counter()
    # Ejecuta la función asíncrona usando asyncio.run
    data = asyncio.run(download_temperatures())
    elapsed = time.perf_counter() - start

    for city, temps in data:
        print(f"Ciudad: {city} -> Temps: {temps}")
    
    print(f"\nTiempo de ejecución: {elapsed:.2f} segundos")

if __name__ == "__main__":
    main()
