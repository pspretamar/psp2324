import time
from multiprocessing import Pool

def potenciarCuad(x):
  """
  Eleva al cuadrado el num. de entrada
  Parámetros:
  x El número a elevar al cuadrado.
  Retorno:
  El cuadrado de x.
  """
  return x ** 2

def ejecutar_normal(listaNumeros):
  inicio = time.time()
  resultado = [potenciarCuad(x) for x in listaNumeros]
  fin = time.time()
  tiempo_ejecucion = fin - inicio
  print(f"Tiempo de ejecución normal: {tiempo_ejecucion:.4f} segundos")
  return resultado

def ejecutar_optimizada(listaNumeros):
  inicio = time.time()
  with Pool(processes = 6) as pool:
    resultado = pool.map(potenciarCuad, listaNumeros)
  fin = time.time()
  tiempo_ejecucion = fin - inicio
  print(f"Tiempo de ejecución optimizada: {tiempo_ejecucion:.4f} segundos")
  return resultado

if __name__ == '__main__':
  ejecutar_normal([2,7,9,10,29,12])
  ejecutar_optimizada([2,7,9,10,29,12])
