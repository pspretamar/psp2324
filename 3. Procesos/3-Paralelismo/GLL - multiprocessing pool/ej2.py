import multiprocessing

def square(n):
    # funcion que calcula el cuadrado de un numero.
    return n * n

if __name__ == "__main__":
    # definimos una lista de numeros
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    # se crea una pool con 4 procesos
    with multiprocessing.Pool(processes=4) as pool:
        # Usando pool.map(), asignamos la función cuadrado a cada número de la lista. 
        # Esto distribuye la carga de trabajo entre los procesos disponibles.
        results = pool.map(square, numbers)

    # imprimimos los resultados
    print("Original Numbers:", numbers)
    print("Squared Numbers:", results)