import math

 # Calculo estadistico de la moda
    # La moda es el valor que mas se repite en una lista de numeros

def calcular_moda(data):
    frecuencia = {}
    for num in data:
        if num in frecuencia:
            frecuencia[num] += 1
        else:
            frecuencia[num] = 1
    
    max_frecuencia = max(frecuencia.values())
    modas = [num for num, freq in frecuencia.items() if freq == max_frecuencia]
    
    return modas

# Calculo estadistico del promedio simple
    # El promedio simple es la suma de todos los valores dividido por la cantidad de valores

def promedio_simple(data_str: str) -> float:
    """
    Calcula el promedio simple de una cadena de números separados por comas.
    
    Ejemplo:
        promedio_simple("1,2,3,4,5")  -> 3.0
    """
    try:
        # Convertir la cadena en una lista de números
        numeros = [float(x.strip()) for x in data_str.split(',') if x.strip()]
    except ValueError as e:
        raise ValueError("Todos los valores deben ser numéricos.") from e

    if not numeros:
        return 0.0
    return sum(numeros) / len(numeros)

def desviacion_estandar(data_str: str) -> float:
    """
    Calcula la desviación estándar de una cadena de números separados por comas.
    Se utiliza la fórmula de la desviación estándar poblacional.
    
    Ejemplo:
        desviacion_estandar("1,2,3,4,5")  -> 1.4142135623730951 (aprox.)
    """
    try:
        numeros = [float(x.strip()) for x in data_str.split(',') if x.strip()]
    except ValueError as e:
        raise ValueError("Todos los valores deben ser numéricos.") from e

    n = len(numeros)
    if n == 0:
        return 0.0
    promedio = sum(numeros) / n
    varianza = sum((x - promedio) ** 2 for x in numeros) / n
    return math.sqrt(varianza)

def promedio_movil(data_str: str, window: int) -> list:
    """
    Calcula el promedio móvil de una cadena de números separados por comas.
    
    Parámetros:
      - data_str: Cadena con los números separados por comas.
      - window: Tamaño de la ventana para calcular el promedio móvil.
    
    Retorna:
      - Una lista con el promedio móvil de cada ventana consecutiva.
      
    Ejemplo:
        promedio_movil("1,2,3,4,5,6", window=3)  -> [2.0, 3.0, 4.0, 5.0]
    """
    try:
        numeros = [float(x.strip()) for x in data_str.split(',') if x.strip()]
    except ValueError as e:
        raise ValueError("Todos los valores deben ser numéricos.") from e

    if window <= 0:
        raise ValueError("El tamaño de la ventana debe ser mayor que 0.")
    if window > len(numeros):
        return []  # No hay suficientes datos para formar una ventana completa.

    promedios = []
    # Se recorre la lista generando ventanas consecutivas de tamaño 'window'
    for i in range(len(numeros) - window + 1):
        ventana = numeros[i:i + window]
        avg = sum(ventana) / window
        promedios.append(avg)
    return promedios
