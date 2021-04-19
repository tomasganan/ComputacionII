""" 
Autor: GAÑÁN, Tomás 
Entrega 4: Signal
"""
# Importacion de librerias/modulos

import signal
import time
import os 

def ping():
    for i in range(10):
        print("Soy el hijo1 con PID: %d: ping" % os.getpid())
        os.kill(os.getppid(), signal.SIGUSR1)
        time.sleep(5)

def pong():
    for i in range(10):
        signal.pause()
        print("Soy el hijo2 con PID: %d: pong" % os.getpid())

def handler(arg1,arg2):
   print("")

def main():
    
    # signal.signal (Num. Señal, Manejador)
    signal.signal(signal.SIGUSR1, handler)
    
    child1 = os.fork()
    if child1 == 0:
        time.sleep(0.1)
        ping()

    child2 = os.fork()
    if child2 == 0:
        pong()

    for i in range(10):
        signal.pause()
        os.kill(child2, signal.SIGUSR1)

if __name__ == "__main__":
    main()