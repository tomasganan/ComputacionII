""" 
Autor: GAÑÁN, Tomás 
Entrega 9: Server
"""
# Importacion de librerias/modulos

import getopt
import socket
import sys

def main():
    
    (opt, arg) = getopt.getopt(sys.argv[1:], 'p:')
    
    port = int(opt[0][1])
    
    # Crear socket TCP/IP
    socketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # Enlace de socket
    socketServer.bind(('', port))
        
    # Escuchando conexiones entrantes
    socketServer.listen(5)
    
    while True:
        # Esperando conexión
        print("Esperando conexiones...")
        connection, clientAddress = socketServer.accept()
        
        try:
            print("Conexion desde: ", clientAddress)
            
            # Recibe los datos y retransmite    
            while True:
                data = connection.recv(19)
                print("Recibido",data)
                if data:
                    print("Enviando mensaje de vuelta al cliente")
                else:
                    print("No hay mas datos", clientAddress)
                    break
        finally:
            # Cerrando conexion
            connection.close()
                
if __name__ == "__main__":
    main()