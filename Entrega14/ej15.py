""" 
Autor: GAÑÁN, Tomás 
Entrega 14: Lock/RLock (Ejercicio 15)
"""
# Importacion de librerias/modulos

from multiprocessing import Lock, Process
import os 
import sys
import string
import time
import getopt

# Función para escribir

def write(iterations, letter, fileName, lock):
    # Método 'adquirir' para entrar al bloque
    lock.acquire()
    # Abrir el archivo y escribir
    with open(fileName, 'a') as file:
        for i in range(iterations):
            file.write(letter)
    # Método 'liberar' para salir del bloque
    lock.release()

def main():
    (opt, arg) = getopt.getopt(sys.argv[1:], 'n:r:f:')
    
    for option, argument in opt:
        if option == '-n':
            numProcess = int(argument)
        elif option == '-r':
            iterations = int(argument)
        elif option == '-f':
            fileName = argument

    try:
        # Listado de albafeto en mayúsculas
        abecedaryList = string.ascii_uppercase
        # Crear objeto 
        lock = Lock()
        procList = []

        os.system(fileName) if os.path.isfile(fileName) else os.system(fileName)

        for i in range(numProcess):
            process = Process(target = write, args = (iterations, abecedaryList[i], fileName, lock))
            process.start()
            procList.append(process)
    
    finally:
        for p in procList:
            p.join()
        print('|||||||||||||||||||||||||||')
        print('|||| PROCESO TERMINADO  |||')
        print('|||| FIN DE ESCRITURA.  |||')
        print('|||||||||||||||||||||||||||')
    
if __name__ == "__main__":
    main()
