""" 
Autor: GAÑÁN, Tomás 
Entrega 9: Client
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
            
    try:
        # Crear socket TCP/IP
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Conexión del socket
        print("Conexión establecida. Host: {}, Port: {}".format(host,port))
        
        s.connect((host, port))
        
        message = False
        
        while message != True:
            message = str(input('Ingrese la palabra a devolver en MAYUS: '))
            s.send(message.encode())
            answerServer = s.recv(1024).decode()
            print(answerServer)
        
    finally:
        # Cerrando conexión
        print("Cerrando conexión")
        s.close()

if __name__ == "__main__":
    main()