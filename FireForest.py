import args
import sys
import cv2
import numpy as np

#
# Constantes
#
GRIND_COLUMS = 8
GRIND_ROWS = 4

def procesarArchivo():
    '''
        Abre el archivo recivido del argumento -f, --file
        lo abre y lee todas las lineas y las retorna
        en una lista de listas de strings
    '''
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
    listaImg = [][]
    '''
    donde:
    listaImg[0][0] = String nombre
    listaImg[0][1] = imagen cv2
    listaImg[0][2] = Atributo Clasificador(H,N,I.....)
    '''
    listaAc = []
    # imagen
    for linea in lineas:
        # Si inicia una nueva imagen
        if linea.find('img') != -1:##Si encuentra un nombre de imagen
            listaAc = []
            nameImg = linea.replace("\n","")
            nameImg = cv2.imread(nameImg)
            listaImg.append(nameImg)
            listaImg.append(nameImg)
            cv2.imshow(nameImg,imagen)
            cv2.waitKey(1000)

    print("\n\n")
    print("Aqui")
    

    #Tabaja en milsegundos
    #cv2.waitKey(0)#= es cualquier tecla
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()