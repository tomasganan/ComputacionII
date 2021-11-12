""" 
Autor: GAÑÁN, Tomás 
Entrega 19: Client (Ejercicio 22)
"""
# Importacion de librerias/mod

import getopt
import time
import re
import asyncio
import sys

try:
    (opt, arg) = getopt.getopt(sys.argv[1:], 'n:p:o:n:m')
    
    for option, argument in opt:
        if option == '-n':
            serverIp = (argument)
        elif option == '-p':
            port = int(argument)
        elif option == '-o':
            operation = (argument)
        elif option == '-n':
            num1 = int(argument)
        elif option == '-m':
            num2 = int(argument)

except getopt.GetoptError as e:
    print("Error: " + str(e))

# Función asíncrona

async def client():
    reader, writer = await asyncio.open_connection(serverIp, port)

    # Envio de num1 y num2
    writer.write(str(num1).encode('utf-8'))
    writer.write(str(num2).encode('utf-8'))
    
    # Envio de operacion
    writer.write(operation.encode('utf-8'))

    await writer.drain()
    result = await reader.read(10)
    time.sleep(1)
    
    # Formateo
    formatData = result.decode('utf-8')
    formatData = re.sub('\s+', ' ', formatData)

    if operation == 'suma':
        print(num1, '+', num2, '=', int(formatData))

    elif operation == 'resta':
        print(num1, '-', num2, '=', int(formatData))

    elif operation == 'multi':
        print(num1, 'x', num2, '=', int(formatData))

    elif operation == 'div' and num2 != 0:
        print(num1, '/', num2, '=', float(formatData))

    print('Cerrando conexión...')
    await writer.wait_closed()

asyncio.run(client())