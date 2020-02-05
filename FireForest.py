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

    listaImg = []
    # Para todas la lineas buscando los archivos y agregando a una lista de listas
    for linea in lineas:
        listaAux = []
        # Separa la linea entre nombre y Atributo Clasificador
        nameImg, imgAC = linea.split(": ")
        nameImg.replace("\n","")
        nameImg += ".jpg"
        
        #Agrega la imagen y atributos a la lista de listas de imagen
        listaAux.append(nameImg)
        listaAux.append(imgAC)
        listaImg.append(listaAux)

    return lineas

# 
# Main
#
def main():
    listaImg = procesarArchivo()
    '''
    donde:
    listaImg[0][0] = String nombre
    listaImg[0][1] = Atributo Clasificador(H,N,I.....)
    '''
    '''
    imageFile = cv2.imread(nameImg)
    cv2.imshow(nameImg,imageFile)
    cv2.waitKey(50)
    '''
    
        
    aux = listaImg[0][1]
    print("Tamaño Lista Listas:"+aux)
    print("\n\n")
    print("Aqui")
    

    #Tabaja en milsegundos
    #cv2.waitKey(0)#= es cualquier tecla
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()