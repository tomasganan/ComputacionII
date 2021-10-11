""" 
Autor: GAÑÁN, Tomás 
Entrega 16: Client (Ejercicio 19)
"""
# Importacion de librerias/modulos

import socket
import time
import sys

def main():

    # Crear socket TCP/IP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = "localhost"
    port = 8000
    # Conexión del socket
    s.connect((host, port))
    print("Conexión establecida exitosamente")

    while True:
        msg = input("CMD: ")
        s.send(msg.encode('ASCII'))
        time.sleep(10)
        print(s.recv(1024).decode())
        exit()

if __name__ == "__main__":
    main()