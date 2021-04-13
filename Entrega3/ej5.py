""" 
Autor: GAÑÁN, Tomás 
Entrega 3: Fork
"""
# Importacion de librerias/modulos

import sys
import getopt
import os 

# os.getppid() -> Se usa para obtener el ID del proceso principal del proceso actual.
# os._exit() -> Se utiliza para salir del proceso.

def main():
     
    try:
        (opt, arg) = getopt.getopt(sys.argv[1:], 'n:')
        
        for option, argument in opt:
            if option == '-n':
                numFork = int(argument)
                
        for i in range(numFork):
            childFork = os.fork()
            if childFork == 0:
                print("Soy el proceso:", os.getpid(), "y mi padre es:", os.getppid())
                os._exit(0) 
                
    except getopt.GetoptError as e:
        print("Error: ", str(e))
        sys.exit(1)
                
if __name__ == '__main__':
    main()