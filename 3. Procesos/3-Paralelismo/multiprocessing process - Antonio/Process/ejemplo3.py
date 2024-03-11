import multiprocessing
import time

def mi_tarea():
    print("Comenzando la tarea...")
    time.sleep(2)
    print("Terminando la tarea...")

if __name__ == "__main__":
    proceso = multiprocessing.Process(target=mi_tarea)
    print("Estado del proceso antes de iniciar:", proceso.is_alive())
    
    proceso.start()
    print("Estado del proceso después de iniciar:", proceso.is_alive())
    
    proceso.join()
    print("Estado del proceso después de terminar:", proceso.is_alive())
