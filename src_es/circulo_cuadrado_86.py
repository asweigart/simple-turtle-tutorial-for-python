# circulo_cuadrado_86.py
from tortuga import *

tamano_pluma(4)
velocidad('mas_rapida')  # Hace que la tortuga se mueva más rápido.

for i in range(50):  # 50 iteraciones en vez de 4.
    adelante(200)
    izquierda(86)
ocultar_tortuga()  # Oculta el cursor de la tortuga al final.
hecho()
