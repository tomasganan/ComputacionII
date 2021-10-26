""" 
Autor: GAÑÁN, Tomás 
Entrega 17: Interpretacion de código (Ejercicio 20)
"""
# Importacion de librerias/modulos

import asyncio
import random
import time

# Función primera asincrona

async def primera(n: int) -> str:
    i = random.randint(0, 10)
    print(f"primera({n}) esperando {i}s.")
    await asyncio.sleep(i)
    result = f"result{n}-A"
    print(f"Retornando primera({n}) == {result}.")
    return result

# Función segunda asincrona

async def segunda(n: int, arg: str) -> str:
    i = random.randint(0, 10)
    print(f"segunda{n, arg} esperando {i}s.")
    await asyncio.sleep(i)
    result = f"result{n}-B => {arg}"
    print(f"Retornando segunda{n, arg} => {result}.")
    return result

# Función chain asincrona

async def chain(n: int) -> None:
    start = time.perf_counter()
    print("Lanzando primera")
    prim = await primera(n)
    print("Lanzando Segunda")
    segu = await segunda(n, prim)
    end = time.perf_counter() - start
    print(f"-->Encadenado result{n} => {segu} (tomó {end:0.2f} s).")

# Main

async def main(*args):
    await asyncio.gather(*(chain(n) for n in args))
    # asyncio.gather( chain(n1), chain(n2), chain(n3), ...)
    # default: asyncio.gather( chain(1), chain(2), chain(3))

if __name__ == "__main__":
    import sys
    random.seed(414)
    args = [1, 2, 3] if len(sys.argv) == 1 else map(int, sys.argv[1:])
    start = time.perf_counter()
    asyncio.run(main(*args))
    end = time.perf_counter() - start
    print(f"Program finished in {end:0.2f} seconds.")