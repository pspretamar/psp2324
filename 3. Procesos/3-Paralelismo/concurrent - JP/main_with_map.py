# main_with_map_inline.py
from concurrent.futures import ProcessPoolExecutor
import time

# Función que se ejecutará en paralelo
def square(x):
    result = x * x
    print(f"Calculando el cuadrado de {x}: {result}")
    return result

def sum_numbers(x):
    result = sum(range(1, x + 1))
    print(f"Calculando la suma de los primeros {x} números: {result}")
    return result

def main():
    # Lista de números (ahora con solo 2 elementos)
    numbers = [2, 3]

    print("Iniciando el procesamiento en paralelo...")

    start_time = time.time()

    # Crear un objeto ProcessPoolExecutor con 2 procesos
    with ProcessPoolExecutor(max_workers=2) as executor:
        # Usar map() para calcular los cuadrados en paralelo
        square_results = list(executor.map(square, numbers))

        # Usar map() para calcular las sumas en paralelo
        sum_results = list(executor.map(sum_numbers, numbers))

    print("Procesamiento en paralelo completado.")
    print("\nResultados obtenidos:")
    for i, number in enumerate(numbers):
        print(f"Resultado de square para {number}: {square_results[i]}")
        print(f"Resultado de sum_numbers para {number}: {sum_results[i]}")

    print("Tiempo de procesamiento en paralelo:", time.time() - start_time)

if __name__ == "__main__":
    main()
