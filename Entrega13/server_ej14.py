""" 
Autor: GAÑÁN, Tomás 
Entrega 13: Server (Ejercicio 14)
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

        if comando.decode() == 'exit':
            clientSocket.send('Chau.'.encode())
            break

        if comando.decode().startswith("cd"):
            path = comando.decode().split(" ")[1]
            try:
                os.chdir(path)
                clientSocket.send('Ok'.encode())
            except FileNotFoundError:
                clientSocket.send("No such file or directory".encode())
            
        with sp.Popen([comando], shell = True, universal_newlines = True, stdout = sp.PIPE, stderr = sp.PIPE) as proc:
            procStdout, procStderr = proc.communicate()

            if proc.returncode == 0 and procStdout:
                    clientSocket.send(procStdout.encode())

            elif proc.returncode == 0 and not procStdout:
                clientSocket.send('Ok'.encode())

            else:
                clientSocket.send(procStderr.encode())

    print('Cliente', address)
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
    print("Servidor iniciando en la direccion:", localAddress,"y puerto:", port)
    
    while True:
        # Escuchando conexiones entrantes
        print("Esperando conexiones...")
        socketServer.listen(5)
        
        clientAddress, clientSocket = socketServer.accept()
        
        print("Conexion desde: ", clientAddress)
            
        newProcess = multiprocessing.Process(target=gnuClient, args=(clientSocket, clientAddress))
        process.start()
                
if __name__ == "__main__":
    main()