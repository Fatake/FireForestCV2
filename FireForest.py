import argparse
import sys
import cv2
import numpy as np

#
# Constantes
#
GRID_COLUMS = 8
GRID_ROWS   = 4
TOTAL_GRIDS = GRID_COLUMS * GRID_ROWS

#
# Funcion que recibe los argumentos de la linea de comandos
#
def argumentos():
    '''
    Argumentos() recibe de la linea de comandos
    -h, --help ayuda de los comandos
    -f, --file nombre de alrchivo
    --version  version del programa
    Retorna los argumentos recibidos
    '''
    parser = argparse.ArgumentParser(description='FireForest')

    parser.add_argument('-f','--file', 
                    action='store',
                    default=None,
                    nargs=1,
                    dest='archivoImg',
                    help='Carga las imagenes a leer')

    parser.add_argument('--version', action='version',
                    version='%(prog)s 1.3')

    args = parser.parse_args()

    #Reviza si recibio los archivos
    if args.archivoImg == None:
        sys.exit("No a ingresado ningun archivo\nUtilice [-h] para ayuda")

    #Retgorna un string con el nombre del archivo
    return ""+args.archivoImg[0]

#
# Funcion que procesa El Archivo
#
def procesarArchivo():
    '''
        Abre el archivo recivido del argumento -f, --file
        lo abre y lee todas las lineas y las retorna
        en una lista de listas de strings
    '''
    #Recibe los argumentos de la linea de comandos
    nombreArchivo = argumentos()

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
# Analisis de las imagenes
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
    arffDB.write("@attribute Brillo numeric\n")# Brillo
    arffDB.write("@attribute Saturacion numeric\n")# Saturacion
    arffDB.write("@attribute IsFire {H,N,I}")
    arffDB.write("\n\n@data\n")
    
    # Para Cada imagen
    for imagenes in listaImg:
        contadorGrids = 0
        # Se recorren los grinds
        nameImg = imagenes[0]
        imageFile = cv2.imread(nameImg)
        imgHSV = cv2.cvtColor(imageFile, cv2.COLOR_BGR2HSV)

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
                Brillo, _= cv2.meanStdDev(imgHSV[miny:maxy, minx:maxx, 1])
                Satura, _= cv2.meanStdDev(imgHSV[miny:maxy, minx:maxx, 2])

                #Se escribe en el archivo
                arffDB.write(str(medAzul[0][0])+",")# Media Azul
                arffDB.write(str(medVerd[0][0])+",")# Media Verde
                arffDB.write(str(medRojo[0][0])+",")# Media Roja
                arffDB.write(str(desStAzu[0][0])+",")# Desv Azul
                arffDB.write(str(desStVer[0][0])+",")# Desv Verd
                arffDB.write(str(desStRoj[0][0])+",")# Desv Roja
                arffDB.write(str(Brillo[0][0])+",")# Brillo
                arffDB.write(str(Satura[0][0])+",")# Saturacion
                arffDB.write(imagenes[1][contadorGrids]+"\n")
                # Contador de los grid hasta TOTAL_GRIDS
                contadorGrids += 1


    # Cierra el archivo    
    arffDB.close()

if __name__ == '__main__':
    main()