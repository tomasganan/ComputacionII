""" 
Autor: GAÑÁN, Tomás 
Entrega 2 Subprocess: Popen
"""
# Importacion de librerias/modulos

import sys
import getopt
import subprocess as subp
from datetime import datetime

# Funcion que retorna fecha y hora actual

def get_datetime():
    current = datetime.now()
    return current

def main():
    
    try:
        (opt, arg) = getopt.getopt(sys.argv[1:], 'c:f:l:')
        
        for option, argument in opt:
            if option == '-c':
                command = argument
            elif option == '-f':
                output_file = argument
            elif option == '-l':
                log_file = argument
        
        # Abrir pipe
        with subp.Popen([command], shell=True, universal_newlines=True, stdout=subp.PIPE, stderr=subp.PIPE) as proc:
            outs, errs = proc.communicate()
            
        with open(output_file, "w") as outFile, open(log_file, "w") as outLog:
            if proc.returncode is 0:
                outFile.write(str(get_datetime()) + " | La salida almacenada es: " + command + outs)   
                outLog.write(str(get_datetime()) + " | " + command + " ejecutado correctamente. \n") 
            else:
                log_file.write(get_datetime() + " - " + errs)

    except getopt.GetoptError as e:
        print("Error: ", str(e))
        sys.exit(1)

if __name__ == '__main__':
    main()