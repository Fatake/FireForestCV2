import argparse
import sys
#
# Funcion que recibe los argumentos de la linea de comandos
#
def argumentos():
    '''
    Argumentos() recibe de la linea de comandos
    -h, --help ayuda de los comandos
    -f, --file nombre de alrchivo .cfg
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
                    version='%(prog)s 1.0')

    args = parser.parse_args()

    #Reviza si recibio los archivos
    if args.archivoImg == None:
        sys.exit("No a ingresado ningun archivo\nUtilice [-h] para ayuda")

    #Retgorna un string con el nombre del archivo
    return ""+args.archivoImg[0]
    '''
    #Busca la existencia de archivos .config
    if archivoImg.find(".cfg") == -1:
        sys.exit("No ingreso un archivo valido")
    '''


if __name__ == '__main__':
    sys.exit("Error, ejecute python program -h")