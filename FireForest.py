import args
import sys

def procesarArchivo():
    #Recibe los argumentos de la linea de comandos
    nombreArchivo = args.argumentos()

    #Intenta Abrir el Archivo
    try:
        imgInfoFile = open(nombreArchivo,"r")
    except:
        sys.exit("Error al abrir el archivo "+nombreArchivo)
    
    #Procesar el archivo
    print("El archivo %s fue abierto "%(nombreArchivo))
    lineas = imgInfoFile.readlines() 

    # Cierra el archivo
    imgInfoFile.close()

    return lineas

# 
# Main
#
def main():
    lineas = procesarArchivo()
    for linea in lineas:
        # Si inicia una nueva imagen
        if linea.find('img') != -1:
            print(linea)
    print("\n\n")

if __name__ == '__main__':
    main()