""" 
Autor: GAÑÁN, Tomás 
Entrega 1 Getopt: Archivo
"""
# Importacion de librerias/modulos

import sys
import getopt
import os

def main():

    try:
        (opt, arg) = getopt.getopt(sys.argv[1:], 'i:o:')
           
    except getopt.GetoptError as e:
        print("Error", str(e))
        sys.exit(1)
        
    for option, argument in opt:
        if option == '-i':
            readFile = open(argument, "r")
            lines = readFile.readlines()
        elif option == '-o':
            writeFile = open(argument, 'w')
            writeFile.writelines(lines)
            print('File copied successfully')
        else:
            print("Invalid option")
            
if __name__ == '__main__':
    main()