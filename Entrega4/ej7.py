""" 
Autor: GAÑÁN, Tomás 
Entrega 4: Signal
"""
# Importacion de librerias/modulos

import signal
import time
import os
import getopt
import sys

def handler(arg1, arg2):
    print("Soy el PID", os.getpid(), "recibí la señal", arg1, "de mi padre PID", os.getppid())

def main():

    signal.signal(signal.SIGUSR2, handler)
    (opt, arg) = getopt.getopt(sys.argv[1:], 'p:', ['process='])
        
    for option, argument in opt:
        if option == '-p' or option == '--process':
            numChild = int(argument)

        for i in range(numChild):
            childFork = os.fork()
            if childFork == 0:
                signal.pause()
            else:
                time.sleep(0.1)
                print("\n Creando proceso: ", str(childFork))
                os.kill(childFork, signal.SIGUSR2)
                time.sleep(0.1)      
  
if __name__ == '__main__':
    main()