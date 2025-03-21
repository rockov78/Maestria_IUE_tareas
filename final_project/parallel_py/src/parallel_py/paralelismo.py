"""
paralelismo.py

Este módulo implementa la función `process_temperatures_py` en Python para procesar, en paralelo,
una lista de tuplas (ciudad, cadena_de_temperaturas). Para cada entrada, se calcula el promedio y la
desviación estándar de los números contenidos en la cadena, utilizando funciones internas. El
procesamiento paralelo se realiza con ThreadPoolExecutor.
"""

import math
from concurrent.futures import ThreadPoolExecutor

def promedio(data: str) -> float:
    """
    Calcula el promedio de números contenidos en una cadena separada por comas.
    
    Si algún valor no puede ser convertido a float (por ejemplo, un mensaje de error), se ignora.
    
    Args:
        data (str): Cadena con números separados por comas.
    
    Returns:
        float: El promedio de los números válidos. Si no hay números válidos, retorna 0.0.
    """
    numeros = []
    for s in data.split(','):
        s = s.strip()
        try:
            numero = float(s)
            numeros.append(numero)
        except ValueError:
            # Ignoramos los valores que no pueden convertirse a float.
            pass
    if not numeros:
        return 0.0
    return sum(numeros) / len(numeros)

def desviacion_estandar(data: str) -> float:
    """
    Calcula la desviación estándar de los números contenidos en una cadena separada por comas.
    
    Los valores que no pueden convertirse a float se ignoran.
    
    Args:
        data (str): Cadena con números separados por comas.
    
    Returns:
        float: La desviación estándar de los números válidos. Retorna 0.0 si no hay números válidos.
    """
    numeros = []
    for s in data.split(','):
        s = s.strip()
        try:
            numero = float(s)
            numeros.append(numero)
        except ValueError:
            # Ignoramos los valores no numéricos.
            pass
    n = len(numeros)
    if n == 0:
        return 0.0
    avg = sum(numeros) / n
    varianza = sum((x - avg) ** 2 for x in numeros) / n
    return math.sqrt(varianza)

def process_temperature_tuple(city: str, temps: str) -> tuple:
    """
    Procesa una tupla (ciudad, cadena_de_temperaturas) calculando el promedio y la desviación estándar.
    
    Args:
        city (str): Nombre de la ciudad.
        temps (str): Cadena con números separados por comas.
    
    Returns:
        tuple: (ciudad, promedio, desviación_estándar)
    """
    avg = promedio(temps)
    std_dev = desviacion_estandar(temps)
    return (city, avg, std_dev)

def process_temperatures_py(data: list) -> list:
    """
    Procesa las temperaturas para cada ciudad en paralelo.
    
    Args:
        data (list): Lista de tuplas (ciudad, cadena_de_temperaturas).
    
    Returns:
        list: Lista de tuplas (ciudad, promedio, desviación_estándar).
    """
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(lambda t: process_temperature_tuple(*t), data))
    return results

# Ejemplo de prueba rápida (si se ejecuta el módulo directamente):
if __name__ == "__main__":
    # Datos de ejemplo: cada ciudad tiene una cadena con números separados por comas, 
    # aunque algunos valores pueden ser mensajes de error que se ignoran.
    datos = [
        ("paris", "10,12,11,13,14,15,16,17,18,19"),
        ("london", "8,9,Service temporarily unavailable,11,12,13,14,15,16,17"),
        ("tokyo", "20,21,22,23,24,25,26,27,28,29"),
    ]
    resultados = process_temperatures_py(datos)
    for ciudad, prom, desv in resultados:
        print(f"Ciudad: {ciudad}\n  Promedio: {prom}\n  Desviación estándar: {desv}\n")
