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
    arffDB = open("ForestFire.arff","w")
    arffDB.write("@relation ForestFireIP\n")
    arffDB.write("\n")
    arffDB.write("@attribute BMean numeric\n")# Azul promedio
    arffDB.write("@attribute GMean numeric\n")# Verde promedio
    arffDB.write("@attribute RMean numeric\n")# Rojo Promedio
    arffDB.write("@attribute BDesEst numeric\n")# Azul Desviacion estandar
    arffDB.write("@attribute GDesEst numeric\n")# Verde Desviacion estandar
    arffDB.write("@attribute RDesEst numeric\n")# Rojo Desviacion estandar
    arffDB.write("@attribute BEntro numeric\n")# Azul Entropia
    arffDB.write("@attribute GEntro numeric\n")# Verde Entropia
    arffDB.write("@attribute REntro numeric\n")# Rojo Entropia
    arffDB.write("@attribute Estado {N,H,I}\n")# Atributo Clasificador
    arffDB.write("\n\n@data\n")
    
    # Para Cada imagen
    for imagenes in listaImg:
        contadorGrids = 0
        # Se recorren los grinds
        nameImg = imagenes[0]
        imageFile = cv2.imread(nameImg)
        nimage = imageFile

        heigth, width, depth = imageFile.shape

        # Para cada Grid de las filas
        for gridy in range(0, GRID_ROWS):
            # Calculo de todos los pixeles en Y que abarca el Grid
            miny = int( gridy * heigth / GRID_ROWS )
            maxy = int( (gridy + 1) * heigth / GRID_ROWS )

            # Para cada Grid de la Columnas
            for gridx in range(0, GRID_COLUMS):
                # Calculo de todos los ixeles en X
                minx = int( gridx * width/ GRID_COLUMS )
                maxx = int( (gridx + 1) * width/ GRID_COLUMS )

                # Obtiene la media del pixel y la Desviacion Estandar
                medAzul, desStAzu = cv2.meanStdDev(imageFile[miny:maxy, minx:maxx, 0])
                medVerd, desStVer = cv2.meanStdDev(imageFile[miny:maxy, minx:maxx, 1])
                medRojo, desStRoj = cv2.meanStdDev(imageFile[miny:maxy, minx:maxx, 2])

                #Se escribe en el archivo
                arffDB.write(str(medAzul[0][0])+",")
                arffDB.write(str(medVerd[0][0])+",")
                arffDB.write(str(medRojo[0][0])+",")
                arffDB.write(str(desStAzu[0][0])+",")
                arffDB.write(str(desStVer[0][0])+",")
                arffDB.write(str(desStRoj[0][0])+",")
                arffDB.write(imagenes[1][contadorGrids]+"\n")
                # Contador de los grid hasta TOTAL_GRIDS
                contadorGrids += 1


    # Cierra el archivo    
    arffDB.close()

if __name__ == '__main__':
    main()