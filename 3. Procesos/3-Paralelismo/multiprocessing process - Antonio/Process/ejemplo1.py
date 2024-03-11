import multiprocessing

def calcular_suma(lista):
    return sum(lista)

if __name__ == "__main__":
    lista_grande = list(range(1000000))
    num_procesos = multiprocessing.cpu_count()
    
    chunk_size = len(lista_grande) // num_procesos
    chunks = [lista_grande[i:i+chunk_size] for i in range(0, len(lista_grande), chunk_size)]
    
    with multiprocessing.Pool(processes=num_procesos) as pool:
        resultados = pool.map(calcular_suma, chunks)
    
    suma_total = sum(resultados)
    print("La suma total es:", suma_total)
    