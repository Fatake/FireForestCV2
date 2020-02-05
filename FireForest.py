import args
import sys
import cv2
import numpy as np

#
# Constantes
#
GRID_COLUMS = 8
GRID_ROWS   = 4
TOTAL_GRIDS = GRID_COLUMS * GRID_ROWS

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

    return listaImg

# 
# Main
#
def main():
    listaImg = procesarArchivo()
    '''
    donde:
    listaImg[][0] = String nombre
    listaImg[][1] = Atributo Clasificador(H,N,I.....)
    '''
    '''
    imageFile = cv2.imread(nameImg)
    cv2.imshow(nameImg,imageFile)
    cv2.waitKey(50)
    '''
    for imagenes in listaImg:
        # Se recorren los grinds
        nameImg = imagenes[0]
        imageFile = cv2.imread(nameImg)
        

        heigth, width, depth = imageFile.shape
        nimage = imageFile
        for gridy in range(0, GRID_ROWS):

            miny = int( gridy * heigth / GRID_ROWS )
            maxy = int( (gridy + 1) * heigth / GRID_ROWS )

            for gridx in range(0, GRID_COLUMS):
                minx = int( gridx * width/ GRID_COLUMS )
                maxx = int( (gridx + 1) * width/ GRID_COLUMS )
                #nueva = cv2.meanStdDev(imageFile[miny:maxy, minx:maxx])
                #nimage[miny:maxy, minx:maxx] = nueva
                cv2.imshow(str(gridx),imageFile[miny:maxy, minx:maxx])
                cv2.waitKey(500)
        
        ##cv2.imwrite("alter"+nameImg, nimage)
                 
    

    #Tabaja en milsegundos
    #cv2.waitKey(0)#= es cualquier tecla
    cv2.destroyAllWindows()

if __name__ == '__main__':
    main()