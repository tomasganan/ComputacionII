""" 
Autor: GAÑÁN, Tomás 
Entrega 8: Threading (Pipe)
"""
# Importacion de librerias/modulos

import os 
import sys
import multiprocessing
import threading

def readPipe(pipe):
    while True:
        message = pipe.recv()
        print("\n Leyendo (PID: %d): %s" % (threading.get_ident(), message))

def readStdin(stdin):
    sys.stdin = os.fdopen(0)
    message = input("\n Escribir mensaje: ")
    stdin.send(message)

def main():
    pipe, stdin = multiprocessing.Pipe()
    
    proc1 = threading.Thread(target = readStdin, args = (stdin, ))
    proc2 = threading.Thread(target = readPipe, args = (pipe, ))
    
    proc1.start()
    proc2.start()
    proc1.join()
    proc2.join()
    
if __name__ == "__main__":
    main()