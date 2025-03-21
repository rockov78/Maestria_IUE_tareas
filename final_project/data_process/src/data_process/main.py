"""
process_data.py

Este módulo integra dos funcionalidades:
  1. Descarga de datos de temperatura para una lista de ciudades, 
     utilizando la función asíncrona `download_temperatures` del paquete concurrence_py.
  2. Procesamiento en paralelo de dichos datos, mediante dos implementaciones:
     - La función `process_temperatures` expuesta desde el módulo Rust (parallel_rs), que
       calcula el promedio y la desviación estándar para cada ciudad.
     - La función `process_temperatures_py` implementada en Python (parallel_py).

Se compara el tiempo de ejecución de ambas implementaciones para realizar benchmarks.

Para ejecutar este módulo:
    python process_data.py
"""

import asyncio
import time

# Función asíncrona que descarga los datos del servidor en Python.
from concurrence_py.download_temperatures import download_temperatures

# Implementación en Python (por ejemplo, en parallel_py)
from parallel_py.paralelismo import process_temperatures_py

# Implementación en Rust (expuesta desde parallel_rs)
from parallel_rs import process_temperatures

async def main():
    """
    Función principal asíncrona que:
      1. Descarga los datos de temperatura para una lista de ciudades.
      2. Procesa los datos en paralelo usando la implementación en Rust y en Python.
      3. Imprime los resultados y el tiempo de ejecución de cada implementación.
    """
    try:
        data = await download_temperatures()
    except Exception as e:
        print(f"Error al descargar temperaturas: {e}")
        return

    # Benchmark: procesamiento en Rust (parallel_rs)
    start_rust = time.perf_counter()
    results_rust = process_temperatures(data)
    elapsed_rust = time.perf_counter() - start_rust

    # Benchmark: procesamiento en Python (parallel_py)
    start_py = time.perf_counter()
    results_py = process_temperatures_py(data)
    elapsed_py = time.perf_counter() - start_py

    print("Resultados del procesamiento con Rust (parallel_rs):")
    for city, avg, std_dev in results_rust:
        print(f"Ciudad: {city}\n  Promedio: {avg}\n  Desviación Estándar: {std_dev}\n")
    print(f"Tiempo de ejecución (Rust): {elapsed_rust:.6f} segundos\n")

    print("Resultados del procesamiento con Python (parallel_py):")
    for city, avg, std_dev in results_py:
        print(f"Ciudad: {city}\n  Promedio: {avg}\n  Desviación Estándar: {std_dev}\n")
    print(f"Tiempo de ejecución (Python): {elapsed_py:.6f} segundos\n")

if __name__ == "__main__":
    asyncio.run(main())

