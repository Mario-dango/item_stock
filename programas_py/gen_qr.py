import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import CircleModuleDrawer, GappedSquareModuleDrawer, HorizontalBarsDrawer, RoundedModuleDrawer, SquareModuleDrawer, VerticalBarsDrawer
import argparse
import os

# Preparamos el formato para el código QR
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)

# Obtenemos el valor del código QR, o bien por parámetro o bien pidiéndolo al usuario
parser = argparse.ArgumentParser()
parser.add_argument("-d", "--dato", type=str, 
    help="Dato con el que se generará el código QR (URL, texto, ...)")
parser.add_argument("-t", "--tipo", type=str, 
    help="Tipo de QR [círculo, cuadrado, Barra_Vertical, Barra_Horizontal, redondeado, Cuadrado_Grande]")
parser.add_argument("-i", "--imagen", type=str, 
    help="Ruta y nombre de fichero de imagen .png con QR que se generará")
args = parser.parse_args()

# Obtenemos el parámetro -d (dato)
if args.dato:
    valorQR = args.dato
else:
    valorQR = input("Introduzca el valor del código QR: ")

# Obtenemos el parámetro -t (tipo)
if args.tipo:
    tipoQR =  args.tipo
else:    
    tipoQR = input("Introduzca la forma del código QR: \n\
        1: círculo\n\
        2: cuadrado\n\
        3: barra_vertical\n\
        4: barra_horizontal\n\
        5: redondeado\n\
        6: cuadrados_grande\n\
        Recordar colocar el solamente el nombre que figura después de los dos puntos ':' \n\
        Por defecto será cuadrados grandes.\n")

    tipoQR = tipoQR.upper()
    # Establecemos el tipo de QR según el indicado por parámetro -t
    if tipoQR == 'CÍRCULO':
        tipoQRC = CircleModuleDrawer()
    elif tipoQR == 'CUADRADO':
        tipoQRC = GappedSquareModuleDrawer()
    elif tipoQR == 'BARRA_VERTICAL':
        tipoQRC = VerticalBarsDrawer()
    elif tipoQR == 'BARRA_HORIZONTAL':
        tipoQRC = HorizontalBarsDrawer()
    elif tipoQR == 'REDONDEADO':
        tipoQRC = RoundedModuleDrawer()
    elif tipoQR == 'CUADRADO_GRANDE':
        tipoQRC = SquareModuleDrawer()
    else:
        tipoQRC = SquareModuleDrawer()    

# Obtenemos el parámetro -i (fichero de imagen QR)
if args.imagen:
    imagenQR = args.imagen
else:
    ruta = input("incgrese el nombre y/o ruta del archivo a generar\n\
        Ejemplo: '\QRS\tipos_QR\cuadrado.png' \nRecordar que la dirección es la que aparece entre comillas simples. ")
    #ruta = 'drogas.png'
    if not ruta:
        imagenQR = os.path.dirname(os.path.abspath(__file__)) + '\codigo_qr.png'
    else:
        imagenQR = os.path.dirname(os.path.abspath(__file__)) + ruta
    
    # imagenQR = os.path.dirname(os.path.abspath(__file__)) + '\codigo_qr.png'

# Aplicamos el valor al objeto QR
qr.add_data(valorQR)


# Generamos el código QR y lo almacenamos en el fichero de imagen PNG
img = qr.make_image(image_factory=StyledPilImage, module_drawer=tipoQRC)
f = open(imagenQR, "wb")
img.save(f)