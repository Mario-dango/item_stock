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

### Generación de los 60 códigos de las computadoras nuevas en QR
## La idea que el código sea Netbook_B0xx dónde xx sean el número asigando
tipoQRC = SquareModuleDrawer()
img = qr.make_image(image_factory=StyledPilImage, module_drawer=tipoQRC)
for i in range(60,120):
    if i < 10:
        valorQR = "Netbook_B00{}".format(i)
        qr.add_data(valorQR)
        imagenQR = os.path.dirname(os.path.abspath(__file__)) + '\QR_netbooks\{}.png'.format(valorQR)
        f = open(imagenQR, "wb")
        img.save(f)
    elif ((i>=10)&(i<100)):
        valorQR = "Netbook_B0{}".format(i)
        qr.add_data(valorQR)
        imagenQR = os.path.dirname(os.path.abspath(__file__)) + '\QR_netbooks\{}.png'.format(valorQR)
        f = open(imagenQR, "wb")
        img.save(f)
    else:
        valorQR = "Netbook_B{}".format(i)
        qr.add_data(valorQR)
        imagenQR = os.path.dirname(os.path.abspath(__file__)) + '\QR_netbooks\{}.png'.format(valorQR)
        f = open(imagenQR, "wb")
        img.save(f)


for i in range(0,3):
    if i < 10:
        valorQR = "Netbook_B00{}".format(i)
        qr.add_data(valorQR)
        imagenQR = os.path.dirname(os.path.abspath(__file__)) + '\QR_netbooks\{}.png'.format(valorQR)
        f = open(imagenQR, "wb")
        img.save(f)
