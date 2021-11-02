""" 
Autor: GAÑÁN, Tomás 
Entrega 18: Server (Ejercicio 21)
"""
# Importacion de librerias/modulos

import os 
import subprocess
import asyncio

async def handler(reader, writer):
    data = await reader.read(100)
    command = data.decode()

    print(f"Comando recibido: {command!r}")

    process = subprocess.Popen([command], shell=True, universal_newlines=True, stdout=subprocess.PIPE,
                               stderr=subprocess.PIPE)

    stdout, stderr = process.communicate()

    if process.returncode == 0:
        if stdout != 0:
            msg = stdout
            writer.write(msg.encode('UTF-8'))
        elif stdout == 0:
            msg = stderr
            writer.write(msg.encode('UTF-8'))
    else:
        msg = stderr
        writer.write(msg.encode('UTF-8'))
        
    await writer.drain()
    writer.close()

# Main

async def main():
    host = "localhost"
    port = 8000
    server = await asyncio.start_server(handler, host, port)
        
    address = server.sockets[0].getsockname()
    print("El server se inicio en: " + str(address))

    async with server:
        await server.serve_forever()

asyncio.run(main())