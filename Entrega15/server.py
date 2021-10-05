""" 
Autor: GAÑÁN, Tomás 
Entrega 15: Server (Ejercicio 18)
"""
# Importacion de librerias/modulos

from multiprocessing import Lock, Process
import os 
import sys
import string
import time
import getopt
import signal
import socket

def atenderCliente(clientSocket, lock, clientAdd):
    filename = None
    opened_file = None

    while True:
        command = clientSocket.recv(256).decode()
        command = command.upper().strip()

        if command == 'Abrir':
            if opened_file is not None:
                clientSocket.send('Archivo abierto \n'.encode())
                continue

            clientSocket.send('Nombre del archivo'.encode())
            try:
                filename = clientSocket.recv(256).decode()
                opened_file = open(filename, 'a')
                clientSocket.send('OK \n'.encode())
            except FileNotFoundError:
                clientSocket.send('El archivo no existe \n'.encode())

        elif command == 'LEER':
            if opened_file is None:
                clientSocket.send('Por favor, abre un archivo! \n'.encode())
                continue

            with open(filename, 'r') as read_fd:
                content = str(read_fd.read()) + '\n'
                clientSocket.send(content.encode())

        elif command == 'CERRAR' or command == 'EXIT':
            clientSocket.send('Cerrando conexión... \n'.encode())
            if opened_file is not None:
                opened_file.close()
            break
        else:
            clientSocket.send(('Comando no valido.''\n').encode())

    print('Cliente', clientAdd, 'desconectado')
    clientSocket.close() 

# Main

def main():
    (opt, arg) = getopt.getopt(sys.argv[1:], 'f:p')

    for option, argument in opt:
        if option == '-f':
            fileName = argument
        elif option == '-p':
            port = argument
    
    try:
        # Crear socket TCP/IP
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind('', port)

        sAdd = socket.gethostbyname(socket.getfqdn())

        # Conexión del socket
        print("Conexión establecida. Server: {}, Port: {}".format(sAdd,port))
        
        lock = multiprocessing.Lock()
        while True:
            s.listen(32)
            clientSocket, conn = s.accept()
            print("Cliente: ", conn[0])
            newProcess = multiprocessing.Process(target=atenderCliente, args=(clientSocket, lock, conn[0]))
            newProcess.start()

if __name__ == '__main__':
    main()