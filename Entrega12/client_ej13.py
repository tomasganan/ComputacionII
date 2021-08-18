""" 
Autor: GAÑÁN, Tomás 
Entrega 12: Client (Ejercicio 13)
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
    
    try:
        # Crear socket TCP/IP
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Conexión del socket
        print("Conexión establecida. Address: {}, Port: {}".format(address,port))
        
        s.connect((address, port))
        
        comando = False
        
        while comando != True:
            comando = str(input('> '))
            s.send(comando.encode())
            answerServer = s.recv(1024).decode()
            print(answerServer)

            time = datetime.now().strftime("%d/%m/%Y %H:%M")
            with open(logFile, 'a') as file:
                file.write('[' + time + '] ||| ' + comando + '\n')
    finally:
        # Cerrando conexión
        print("Cerrando conexión")
        s.close()

if __name__ == "__main__":
    main()