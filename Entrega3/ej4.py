""" 
Autor: GAÑÁN, Tomás 
Entrega 3: Fork
"""
# Importacion de librerias/modulos

import os 

# os.fork -> Devuelve un valor entero que representa la identificación del proceso secundario en el proceso principal.
# os.getpid -> Devuelve un valor entero que indica el ID del proceso del proceso actual.

def main():
    pid = os.fork()
    if pid == 0:
        for i in range(5):
            print("Soy el hijo, mi PID es:", os.getpid())
        print("PID", os.getpid(), "terminado")
    else:
        for i in range(2):
            print("Soy el padre, mi PID es:", os.getpid(), "| El PID de mi hijo es: ", pid)
        os.wait()
        print("Mi proceso hijo", pid, "terminó")

if __name__ == '__main__':
    main()