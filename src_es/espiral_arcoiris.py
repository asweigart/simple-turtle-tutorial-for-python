# espiral_arcoiris.py
from tortuga import *

velocidad('mas rapida')
tamano_pluma(3)
color_fondo('negro')

color_pluma('rojo')
for i in range(60):
    adelante(i)
    izquierda(91)

color_pluma('naranja')
for i in range(60):
    adelante(60 + i)
    izquierda(91)

color_pluma('amarillo')
for i in range(60):
    adelante(120 + i)
    izquierda(91)

color_pluma('verde')
for i in range(60):
    adelante(180 + i)
    izquierda(91)

color_pluma('azul')
for i in range(60):
    adelante(240 + i)
    izquierda(91)

color_pluma('morado')
for i in range(60):
    adelante(300 + i)
    izquierda(91)

hecho()