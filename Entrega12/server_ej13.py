""" 
Autor: GAÑÁN, Tomás 
Entrega 12: Server (Ejercicio 13)
"""
# Importacion de librerias/modulos

import getopt
import socket
import sys
import multiprocessing
import signal
import os
import subprocess as sp

def closeServer(s, frame):
    print("\n Cerrando conexiones...")
    sys.exit(0)

def gnuClient(clientSocket, clientAddress):
    while True:
        comando = clientSocket.recv(2048)

        if comando.decode().startswith("cd"):
            path = comando.decode().split(" ")[1]
            try:
                os.chdir(path)
                clientSocket.send('Ok'.encode())
            except FileNotFoundError:
                clientSocket.send("El directorio no existe".encode())

        if comando.decode() == 'exit':
            clientSocket.send('Chau.'.encode())
            break

    print('Client', address, 'disconnected')
    clientSocket.close()

def main():
    
    (opt, arg) = getopt.getopt(sys.argv[1:], 'p:')
    
    port = int(opt[0][1])

    signal.signal(signal.SIGINT, closeServer)
    localAddress = socket.gethostbyname(socket.getfqdn())

    # Crear socket TCP/IP
    socketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Enlace de socket
    socketServer.bind(('', port))
    print("Servidor iniciando en la direccion: ", localAddress,"y puerto: ", port)
        
    # Escuchando conexiones entrantes
    socketServer.listen(5)
    
    while True:
        # Esperando conexión
        print("Esperando conexiones...")
        clientAddress, clientSocket = socketServer.accept()
        
        try:
            print("Conexion desde: ", clientAddress)
            
            new_process = multiprocessing.Process(target=gnuClient, args=(clientSocket, clientAddress))
            process = multiprocessing.Process()
            process.start()
                
if __name__ == "__main__":
    main()