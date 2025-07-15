# espiral_fondo_negro.py
from tortuga import *
from random import *

colores = ['rojo', 'naranja', 'amarillo', 'azul', 'verde', 'morado']

velocidad('mas rapida')
tamano_pluma(3)
color_fondo('negro')
for i in range(300):
    color_pluma(choice(colores))
    adelante(i)
    izquierda(91)
ocultar_tortuga()
hecho()