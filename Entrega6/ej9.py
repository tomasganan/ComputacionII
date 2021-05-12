""" 
Autor: GAÑÁN, Tomás 
Entrega 6: Multiprocessing
"""
# Importacion de librerias/modulos

import signal
import os 
import sys
import multiprocessing

def readPipe(pipe):
    while True:
        message = pipe.recv()
        print("\n Leyendo (PID: %d): %s" % (os.getpid(),message))

def readStdin(stdin):
    sys.stdin = os.fdopen(0)
    message = input("\n Escribir mensaje: ")
    stdin.send(message)
    
def main():
    pipe, stdin = multiprocessing.Pipe()
    
    proc1 = multiprocessing.Process(target = readStdin, args = (stdin, ))
    proc2 = multiprocessing.Process(target = readPipe, args = (pipe, ))
    
    proc1.start()
    proc2.start()
    proc1.join()
    proc2.join()
    
if __name__ == "__main__":
    main()