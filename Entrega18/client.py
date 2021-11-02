""" 
Autor: GAÑÁN, Tomás 
Entrega 18: Client (Ejercicio 21)
"""
# Importacion de librerias/modulos

import socket
import time
import re
import asyncio

async def client():

    # Crear conexión
    host = "localhost"
    port = 8000
    reader, writer = await asyncio.open_connection(host, port)
    msg = input("\n tomasganan$ > ")
    print(f'Enviando: {msg!r}')

    # Escribir
    writer.write(msg.encode())
    await writer.drain()
    
    # Leer
    data = await reader.read(100)
    formatData = data.decode()
    formatData = re.sub('\s+', ' ', formatData)

    if 'command not found' in formatData:
        print("Comando INVALIDO!")
    else:
        print(f'Comando recibido -> {formatData}')

    # Cerrar conexión
    print('Cerrando conexión...')
    writer.close()
    await writer.wait_closed()

asyncio.run(client())