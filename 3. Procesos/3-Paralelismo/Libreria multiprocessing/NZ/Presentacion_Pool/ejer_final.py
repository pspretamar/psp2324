from multiprocessing import Pool, cpu_count
from functools import reduce

# Función para procesar una línea y calcular la suma de los números
def procesar_linea(linea):
    numeros = list(map(int, linea.strip().split(',')))
    suma = sum(numeros)
    return suma

if __name__ == '__main__':
    # Nombre del archivo
    nombre_archivo = 'datos.txt'

    # Abrir el archivo y leer todas las líneas
    with open(nombre_archivo, 'r') as archivo:
        lineas = archivo.readlines()

    # Crear un pool de procesos con el número de procesos determinado
    with Pool(processes=4) as pool:
        # Método map para procesar líneas
        resultados_map = pool.map(procesar_linea, lineas)

        # Método apply_async para procesar una línea específica de manera asincrónica
        resultado_apply_async = pool.apply_async(procesar_linea, (lineas[0],))

        # Método map_async para procesar líneas de manera asincrónica
        resultados_map_async = pool.map_async(procesar_linea, lineas)

        # Método apply para procesar una línea específica de manera síncrona
        resultado_apply = pool.apply(procesar_linea, (lineas[1],))

        # Combinar los resultados
        suma_total = reduce(lambda x, y: x + y, resultados_map)

        # Imprimir los resultados
        print("Resultado usando map:", resultados_map)
        print("Resultado usando apply_async:", resultado_apply_async.get())
        print("Resultado usando map_async:", resultados_map_async.get())
        print("Resultado usando apply:", resultado_apply)
        print("Suma total:", suma_total)