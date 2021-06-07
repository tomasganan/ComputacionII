""" 
Autor: GAÑÁN, Tomás 
Entrega 10: Client JuncoTic
"""
# Importacion de librerias/modulos

import getopt
import socket
import sys

def main():
    
    (opt, arg) = getopt.getopt(sys.argv[1:], 'h:p:')
    
    for option, argument in opt:
        if option == '-h':
            host = argument
        elif option == '-p':
            port = int(argument)
            
    # Crear socket TCP/IP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Conexión del socket
    print("Conexión establecida. Host: {}, Port: {}".format(host,port))
    s.connect((host, port))

    try:
        # Enviando datos
        message = "Hola Mundo"
        s.send(message)
         
        """
        # Buscando respuesta
        amount_received = 0
        amount_expected = len(message)
        
        while amount_received < amount_expected:
            data = s.recv(1024).decode()
            amount_received += len(data)
            print("Recibiendo %s", data)
        """
        
    finally:
        # Cerrando conexión
        print("Cerrando conexión")
        s.close()

if __name__ == "__main__":
    main()