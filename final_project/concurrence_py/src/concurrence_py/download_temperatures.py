"""
download_temperatures.py

Este módulo implementa la función `download_temperatures` que descarga 
de forma concurrente (usando asyncio y aiohttp) los datos de temperaturas 
máximas para una lista de ciudades de un servidor. La respuesta se procesa 
para extraer los primeros 10 valores, ya sea a partir de un arreglo JSON o 
como CSV, y se retorna una lista de tuplas (ciudad, datos_formateados).
"""

import asyncio
import aiohttp
import json

async def fetch_temperature(session: aiohttp.ClientSession, city: str) -> tuple:
    """
    Descarga los datos de temperatura para una ciudad dada.

    Args:
        session (aiohttp.ClientSession): La sesión HTTP asíncrona.
        city (str): Nombre de la ciudad.

    Returns:
        tuple: (city, formatted_temperature_data) donde formatted_temperature_data
               es una cadena con los primeros 10 números separados por comas.
    """
    city_encoded = city.replace(" ", "%20")
    url = f"https://weather.siel.com.co/city/{city_encoded}/temp/max"
    headers = {"Authorization": "Bearer secret-token-1234"}
    
    try:
        async with session.get(url, headers=headers) as response:
            resp_text = await response.text()
    except Exception as e:
        print(f"Error al descargar datos para {city}: {e}")
        resp_text = ""
    
    # Procesar la respuesta:
    if resp_text.strip().startswith('['):
        # Se espera un arreglo JSON
        try:
            numbers = json.loads(resp_text)
            # Asegurarse de que sean números (float)
            numbers = [float(num) for num in numbers]
            first_ten = numbers[:10]
            formatted = ",".join(str(n) for n in first_ten)
        except Exception as e:
            print(f"Error al parsear JSON para {city}: {e}")
            formatted = ""
    else:
        # Se procesa como CSV simple
        temps = [s.strip() for s in resp_text.split(',') if s.strip()]
        first_ten = temps[:10]
        formatted = ",".join(first_ten)
    
    return city, formatted

async def download_temperatures() -> list:
    """
    Descarga de forma concurrente los datos de temperatura para una lista de ciudades.

    Returns:
        list: Lista de tuplas (city, formatted_temperature_data).
    """
    cities = [
        "paris",
        "london",
        "tokyo",
        "new york",
        "sydney",
        "moscow",
        "cairo",
        "beijing",
        "mumbai",
        "rio de janeiro",
    ]
    
    async with aiohttp.ClientSession() as session:
        tasks = [fetch_temperature(session, city) for city in cities]
        results = await asyncio.gather(*tasks)
    return results

if __name__ == "__main__":
    # Prueba rápida: Ejecuta la descarga y muestra el resultado.
    data = asyncio.run(download_temperatures())
    for city, temps in data:
        print(f"Ciudad: {city} -> Temps: {temps}")
