from multiprocessing import Pool

# Función simple para calcular el cuadrado de un número
def square(x):
    return x * x

if __name__ == "__main__":
    # Creamos un pool de procesos con 2 procesos
    with Pool(processes=2) as pool:
        # Usamos apply_async para calcular el cuadrado de un número de manera asíncrona
        result = pool.apply(square, (100000000000000000,))
        
        # El flujo de ejecución del programa principal no espera
        # continuamos haciendo otras operaciones mientras se realiza el cálculo
        print("Esto se imprime antes de obtener el resultado de apply_async")
        
        # Obtenemos el resultado cuando esté disponible
        print("Resultado de apply_async:", result)