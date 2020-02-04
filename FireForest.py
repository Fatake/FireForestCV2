import argv
from enlace import *
import sys

def procesarArchivo():
    #Recibe los argumentos de la linea de comandos
    nombreArchivo = argv.argumentos()

    #Intenta Abrir el Archivo
    try:
        imgInfoFile = open(nombreArchivo,"r")
    except:
        sys.exit("Error al abrir el archivo "+nombreArchivo)
    
    #Procesar el archivo
    print("El archivo %s fue abierto "%(nombreArchivo))
    imgInfoFile.readline

    while (linea = imgInfoFile.readline()):
        print(linea)
    

    # Cierra el archivo
    archivoConfiguracion.close()

# 
# Main
#
def main():
    
    procesarArchivo()
    print("\n\n")

if __name__ == '__main__':
    main()