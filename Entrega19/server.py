""" 
Autor: GAÑÁN, Tomás 
Entrega 19: Server (Ejercicio 22)
"""
# Importacion de librerias/modulos

import sys
import getopt
import asyncio
import time
import re

def sum(a, b):
    return a+b

def res(a, b):
    return a-b

def mul(a, b):
    return a*b

def div(a, b):
    if b != 0:
        return a/b
    else:
        return str(ZeroDivisionError)

try:
    (opt, arg) = getopt.getopt(sys.argv[1:], 'h:p:')
    
    for option, argument in opt:
        if option == '-h':
            serverIp = (argument)
        elif option == '-p':
            port = int(argument)
            
except getopt.GetoptError as e:
    print("Error: " + str(e))

# Función asíncrona

async def handle(reader, writer):

    num1 = await reader.read(100)
    num2 = await reader.read(100)
    operation = await reader.read(100)

    if (operation) == 'sum':
        result = sum(num1, num2)
        time.sleep(1)
        writer.write(str(result.get()).encode('utf-8'))

    elif (operation) == 'res':
        result = res(num1, num2)
        time.sleep(1)
        writer.write(str(result.get()).encode('utf-8'))

    elif (operation) == 'mul':
        result = mul(num1, num2)
        time.sleep(1)
        writer.write(str(result.get()).encode('utf-8'))
  
    elif (operation) == 'div':
        result = div(num1, num2)
        time.sleep(1)
        writer.write(str(result.get()).encode('utf-8'))
        
    await writer.drain()
    writer.close()

async def main():
    
    server = await asyncio.start_server(handle, serverIp, port)

    async with server:
        await server.serve_forever()

asyncio.run(main())

if __name__ == '__main__':
    main()