# main_with_submit.py

from concurrent.futures import ProcessPoolExecutor

# Función que se ejecutará en paralelo
def example_submit(x):
    return x * x

def main():
    with ProcessPoolExecutor(max_workers=2) as executor:
        # Utiliza submit para enviar la tarea
        future = executor.submit(example_submit, 5)
        print(f"Tarea enviada para calcular el cuadrado de 5")

        # La ejecución continúa mientras la tarea está en progreso
        print("La ejecución continúa mientras la tarea está en progreso...")

        # Obtiene el resultado cuando la tarea está completa
        result = future.result()
        print(f"Resultado de submit: {result}")
        print("La tarea se ha completado y el resultado se ha obtenido")

if __name__ == "__main__":
    main()
