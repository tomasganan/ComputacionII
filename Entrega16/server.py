""" 
Autor: GAÑÁN, Tomás 
Entrega 16: Server (Ejercicio 19)
"""
# Importacion de librerias/modulos

import os 
import sys
import getopt
import signal
import socket
import socketserver
import threading
import subprocess

class Handler(socketserver.BaseRequestHandler):

    def handle(self):
        try:
            data = self.request.recv(1024)
            print("Mensaje recibido")
            process = subprocess.Popen([data], shell=True, universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            stdout, stderr = process.communicate()
            if process.returncode == 0:
                if stdout != 0:
                    msg = "\n Ok \n" + stdout
                    self.request.send(msg.encode('ASCII'))
                elif stdout == 0:
                    msg = "ERROR: \n" + stderr
                    self.request.send(msg.encode('ASCII'))
            else:
                msg = "ERROR: \n" + stderr
                self.request.send(msg.encode('ASCII'))

        except UnicodeEncodeError:
            msg = 'Comando invalido'
            self.request.send(msg)
        return

class ForkingEchoServer(socketserver.ForkingMixIn,socketserver.TCPServer,):
    pass

class ThreadedEchoServer(socketserver.ThreadingMixIn,socketserver.TCPServer,):
    pass

# Main

def main():
    (opt, arg) = getopt.getopt(sys.argv[1:], 'm')

    for option, argument in opt:
        if option == '-m':
            simulClient = argument
        
    try:
        address = ('localhost', 8000)
        if simulClient == 'p':

            print("| FORKING |")
            server = ForkingEchoServer(address, Handler)
            ip, port = server.server_address

            t = threading.Thread(target = server.serve_forever)
            t.setDaemon(True)
            t.start()

            # Crear socket TCP/IP
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            # Conexión del socket
            print("Conexión establecida. Puerto: ",port)
            s.recv(1024)

        elif simulClient == 't':

            print("| THREADING |")
            server = ThreadedEchoServer(address, Handler)
            ip, port = server.server_address

            t = threading.Thread(target = server.serve_forever)
            t.setDaemon(True)
            t.start()

            # Crear socket TCP/IP
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            # Conexión del socket
            print("Conexión establecida. Puerto: ",port)
            s.recv(1024)

if __name__ == '__main__':
    main()