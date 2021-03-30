""" 
Autor: GAÑÁN, Tomás 
Entrega 1 Getopt: Calculadora
"""
# Importacion de librerias/modulos

import sys
import getopt

# Funcion calculadora

def calculator(num1, num2, op):
    if op == '+':
        result = num1 + num2
    elif op == '-':
        result = num1 - num2
    elif op == 'x':
        result = num1 * num2
    elif op == '/':
        result = num1 / num2
    return result

def main():

    # try: Primera ejecución. Si no ocurren ninguna excepción, la ejecución try finaliza.
    
    try:
        (opt, arg) = getopt.getopt(sys.argv[1:], 'n:m:o:', ["n1=", "n2=", "operation="])
        
        for option, argument in opt:
            if option == '-n' or option == '--n1':
                n1 = int(argument)
            elif option == '-m' or option == '--n2':
                n2 = int(argument)
            elif option == '-o' or option == '--operation':
                operation = argument

        if operation not in ['+', '-', 'x', '/']:
            print("Invalid operation")
        else:
            print(n1, operation, n2, "=", calculator(n1, n2, operation))
            
    # except: Si ocurre una excepción durante la ejecución de try, la ejecución del try se omite y el except muetra el error.
    
    except getopt.GetoptError as e:
        print("Error: ", str(e))
        sys.exit(1)

# __name__ variable que replica la función main en C

if __name__ == '__main__':
    main()