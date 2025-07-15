# solucion_cuadrados_anidados.py
from tortuga import *
tamano_pluma(4)

longitud_linea = 100
for i in range(4):
    adelante(longitud_linea)
    izquierda(90)

longitud_linea = 150
for i in range(4):
    adelante(longitud_linea)
    izquierda(90)

longitud_linea = 200
for i in range(4):
    adelante(longitud_linea)
    izquierda(90)

longitud_linea = 250
for i in range(4):
    adelante(longitud_linea)
    izquierda(90)

longitud_linea = 300
for i in range(4):
    adelante(longitud_linea)
    izquierda(90)

# O puedes usar:
# for longitud_linea in range(100, 350, 50):
#     for i in range(4):
#         adelante(longitud_linea)
#         izquierda(90)
hecho()
