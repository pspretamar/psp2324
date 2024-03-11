# main_optimized.py
from concurrent.futures import ThreadPoolExecutor

def main():
    # Función que se ejecutará en paralelo
    def square(x):
        return x * x

    # Lista de números
    numbers = [1, 2, 3, 4, 5]

    print("Iniciando el procesamiento en paralelo...")

    # Utiliza ThreadPoolExecutor para ejecutar square en paralelo usando map
    with ThreadPoolExecutor(max_workers=2) as executor:
        # Mapea la función square a la lista de números y obtén los resultados
        results = list(executor.map(square, numbers))

        # Imprime los resultados
        for result in results:
            print("Resultado de square:", result)

        # Muestra un mensaje antes de ejecutar el método shutdown
        print("Ejecutando método shutdown...")

        # Apaga el ThreadPoolExecutor después de completar todas las tareas
        executor.shutdown(wait=True)
        # wait=True asegura que esperará a que todas las tareas se completen antes de apagar el ThreadPool

        # Muestra un mensaje después de ejecutar el método shutdown
        print("Método shutdown ejecutado.")

    print("Todas las tareas se han completado.")

if __name__ == "__main__":
    main()
