""" 
Autor: GAÑÁN, Tomás 
Entrega 19: Server (Ejercicio 22)
"""
# Importacion de librerias/modulos

import sys
import getopt

# Funcion calculadora

def calculator(num1, operation, num2):
    if operation == '+':
        result = num1 + num2
    elif operation == '-':
        result = num1 - num2
    elif operation == 'x':
        result = num1 * num2
    else:
        result = num1 / num2
    return result

def main():
    try:
        (opt, arg) = getopt.getopt(sys.argv[1:], 'n:m:o:',["number1=", "number2=", "operation="])
        
        for option, argument in opt:
            if option == '-n':
                num1 = int(argument)
            elif option == '-m':
                num2 = int(argument)
            elif option == '-o':
                operation = (argument)

        if operation not in ['+', '-', 'x', '/']:
            print("Operacion invalida")
        else:
            print(num1, operation, num2, "=", calculator(num1, operation, num2))

    except getopt.GetoptError as e:
        print("Error: " + str(e))

if __name__ == '__main__':
    main()