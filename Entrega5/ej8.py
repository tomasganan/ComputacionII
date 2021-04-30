""" 
Autor: GAÑÁN, Tomás 
Entrega 5: Pipe
"""
# Importacion de librerias/modulos

import signal
import time
import os 

def handler(arg1, arg2):
    pass

def main():
    # Metodo para crear tuberia que devuelve descriptores 'read' y 'write'
    read, write = os.pipe()
    
    # signal.signal (Num. Señal, Manejador)
    signal.signal(signal.SIGUSR1, handler)
    
    processA = os.getpid()
    processB = os.fork()
    if not processB:
        processC = os.fork()
        
    # Proceso A, B y C

    if os.getpid() == processA:
        os.close(write)
        # fdopen() metodo para crear un objeto archivo descriptor
        read = os.fdopen(read, 'r')
        os.kill(processB, signal.SIGUSR1)
        print("A (PID=%d) leyendo:" % os.getpid())
        print(read.read())
        
    elif not processB and processC:
        os.close(read)
        write = os.fdopen(write, 'w')
        write.write("Mensaje 1 (PID = %d)\n" % os.getpid())
        os.kill(processC, signal.SIGUSR1)
        
    elif not processC:
        signal.pause()
        os.close(read)
        write = os.fdopen(write, 'w')
        write.write("Mensaje 2 (PID = %d)" % os.getpid())
        os.kill(processA, signal.SIGUSR1)

if __name__ == "__main__":
    main()