from multiprocessing import Pool
import random

# Función para dividir un número aleatorio por otro número aleatorio
def divide_random(num):
    divisor = random.randint(1, 10)
    result = num / divisor
    # Simulamos un error si el resultado es menor que 0.2
    if result < 0.2:
        raise ValueError("El resultado es demasiado pequeño")
    return result

# Función de callback que imprime el resultado de una tarea completada
def callback(result):
    print("Tarea completada con resultado:", result)

# Función de error callback que maneja los errores ocurridos durante la ejecución de una tarea
def error_callback(error):

    print("Error:", error)

if __name__ == "__main__":
    # Creamos un pool de procesos con 3 procesos
    with Pool(processes=3) as pool:
        # Creamos una lista de 10 números aleatorios
        numbers = [random.randint(1, 100) for _ in range(10)]
        
        # Aplicamos la función divide_random a cada número de manera asíncrona con map_async
        result_async = pool.map_async(divide_random, numbers, callback=callback, error_callback=error_callback)
        
        # Esperamos a que todas las tareas asíncronas se completen
        result_async.wait()