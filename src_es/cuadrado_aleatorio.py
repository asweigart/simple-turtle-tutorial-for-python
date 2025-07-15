# cuadrado_aleatorio.py
from tortuga import *
from random import *

tamano_pluma(4)
velocidad('mas rapida')

for i in range(50):
    adelante(200)
    # Gira a la izquierda un número aleatorio de grados entre 80 y 100:
    izquierda(randint(80, 100))
ocultar_tortuga()
hecho()
