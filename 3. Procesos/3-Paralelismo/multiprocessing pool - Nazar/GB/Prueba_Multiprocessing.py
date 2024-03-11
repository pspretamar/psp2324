
from multiprocessing import Pool

def potenciarCuad(numero):
    '''
    Esta función eleva al cuadrado la entrada
    Parametros:
    numero: número que queremos elevar al cuadrado
    '''
    return numero*numero

if __name__ == '__main__':
# Si el archivo actual es el es el programa principal se ejecutará
    with Pool(5) as p:
        print(p.map(potenciarCuad, [2, 3]))
