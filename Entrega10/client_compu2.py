""" 
Autor: GAÑÁN, Tomás 
Entrega 9: Client
"""
# Importacion de librerias/modulos

import getopt
import socket
import sys

# Diccionario con las posibles respuestas

codes = {200: 'OK', 
        400: 'Comando válido, pero fuera de secuencia.', 
        500: 'Comando inválido.',
        404: 'Clave errónea.', 
        405: 'Cadena nula.'}

# Funcion que envia el mensaje al server

def sendServer(conn, message):
    conn.send(message.encode())
    answerCodes = int(conn.recv(1024).decode())
    print("Respueta: ", answerCodes,".", codes.get(answerCodes))
    
    return int(answerCodes)
    
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
        
        verifName = False
        verifEmail = False
        verifKey = False
        
        while not verifName:
            name = "hello" + input("Ingrese su nombre: ")
            verifName = sendServer(s, name) == 200
            
        while not verifEmail:
            email = "email" + input("Ingrese su email: ")
            verifEmail = int(sendServer(s, email)) == 200
        
        while not verifKey:
            key = "key" + input("Ingrese su clave: ")
            verifKey = int(sendServer(s, key)) == 200
    
    finally:
        # Cerrando conexión
        print("Cerrando conexión")
        s.close()

if __name__ == "__main__":
    main()