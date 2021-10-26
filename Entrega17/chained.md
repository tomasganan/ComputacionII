## Chained

_En el siguiente repositorio se encuentra el ejercicio práctico de la cátedra de Computación II de la Universidad de Mendoza sede San Rafael, ciclo 2021. En el mismo se desarrolla un ejercicio práctico sobre el uso de funciones asíncronas_

### Código 🔧

- Importacion de librerias

```
import asyncio
import random
import time
```

- Funciones asíncronas (Primera y segunda)

```
async def primera(n: int) -> str:
    i = random.randint(0, 10)
    print(f"primera({n}) esperando {i}s.")
    await asyncio.sleep(i)
    result = f"result{n}-A"
    print(f"Retornando primera({n}) == {result}.")
    return result
```

```
async def segunda(n: int, arg: str) -> str:
    i = random.randint(0, 10)
    print(f"segunda{n, arg} esperando {i}s.")
    await asyncio.sleep(i)
    result = f"result{n}-B => {arg}"
    print(f"Retornando segunda{n, arg} => {result}.")
    return result
```

En ambas funciones asíncronas se utilizan un random entre 0 y 10 para asignar los segundos de espera. A diferencia de 'time.sleep()' que bloquea la ejecución completa del script y se pone en espera, la utilización de asyncio.sleep() pedirá al bucle de eventos que ejecute algo más mientras su instrucción de espera finaliza su ejecución.

- Funciones asíncrona (Chain)

```
async def chain(n: int) -> None:
    start = time.perf_counter()
    print("Lanzando primera")
    prim = await primera(n)
    print("Lanzando Segunda")
    segu = await segunda(n, prim)
    end = time.perf_counter() - start
    print(f"-->Encadenado result{n} => {segu} (tomó {end:0.2f} s).")
```

La función asíncrona chain/string o cadena en español en primer lugar se hace la utilización de la función 'time.perf_counter()' para devolver el valor flotante del tiempo en segundos. Dicha función se utiliza en el inicio (start) y final (end) de la ejecución.

- Main

```
async def main(*args):
    await asyncio.gather(*(chain(n) for n in args))
```

Por último, el main hace la utilización de la función 'asyncio.gather()' la cual devuelve una instancia futura, lo que permite la agrupación de tareas de alto nivel.

### Construido con 🛠️

* **Python** - Python es un lenguaje de programación de alto nivel que se utiliza para desarrollar aplicaciones de todo tipo. Se trata de un lenguaje de programación multiparadigma, ya que soporta parcialmente la orientación a objetos, programación imperativa y, en menor medida, programación funcional. Mas info: https://www.python.org/

### Autor ✒️

* **Tomás Gañan** 