""" 
Autor: GAÑÁN, Tomás 
Entrega 7: Multiprocessing
"""
# Importacion de librerias/modulos

import signal
import os 
import sys
import multiprocessing
import time

def child(pipe, queue):
    print("Proceso %d, PID: %d" % (pipe, os.getpid()))
    time.sleep(pipe)
    queue.put(str(os.getpid()) + "\t")

def main():
    queue = multiprocessing.Queue()
    childList = []
    
    for i in range (1, 11):
        procX = multiprocessing.Process(target = child, args = (i, queue))
        procX.start()
        childList.append(procX)
        
    for procX in childList:
        procX.join()
    
if __name__ == "__main__":
    main()