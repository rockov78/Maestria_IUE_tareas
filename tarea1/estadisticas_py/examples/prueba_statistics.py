# Del paquet estadisticas_py importo el módulo mypy_statistics para luego usar sus funciones promedio_simple, desviacion_estandar, promedio_movil, calcular_moda
from estadisticas_py import mypy_statistics

# Defino una cadena de datos para la prueba
data = "1,2,3,4,5,6,7,8,9,10"

#imprimo el valor de cada función llamando el módulo luego punto y la función:
print("Promedio simple:", mypy_statistics.promedio_simple(data))
print("Desviación estándar:", mypy_statistics.desviacion_estandar(data))
print("Promedio móvil (ventana=3):", mypy_statistics.promedio_movil(data, window=3))
print("Moda:", mypy_statistics.calcular_moda([float(x.strip()) for x in data.split(',') if x.strip()]))


# Esta es una forma de hacerlo si llamo el módulo en la importación y luego las funciones que necesite.
# from estadisticas_py.mypy_statistics import promedio_simple, desviacion_estandar, promedio_movil, calcular_moda

#imprimo el valor de cada función dentro del módulo.
# print("Promedio simple:", promedio_simple(data))
# print("Desviación estándar:", desviacion_estandar(data))
# print("Promedio móvil (ventana=3):", promedio_movil(data, window=3))
# print("Moda:", calcular_moda([float(x.strip()) for x in data.split(',') if x.strip()]))
