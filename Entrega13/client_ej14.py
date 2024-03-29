""" 
Autor: GAÑÁN, Tomás 
Entrega 13: Client (Ejercicio 14)
"""
# Importacion de librerias/modulos

import getopt
import socket
import sys
from datetime import datetime

def main():

    (opt, arg) = getopt.getopt(sys.argv[1:], 'a:p:l')
    
    for option, argument in opt:
        if option == '-a':
            address = argument
        elif option == '-p':
            port = int(argument)
        elif option == 'l':
            logFile = argument

    # Crear socket TCP/IP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Conexión del socket
    s.connect((address, port))
    print("Conexión establecida. Address: {}, Port: {}".format(address,port))

if __name__ == "__main__":
    main()