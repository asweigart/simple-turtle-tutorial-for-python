# posicion_aleatoria.py
from tortuga import *
from random import *

for i in range(8):
    escribir(posicion(), fuente=('Arial', 18, 'normal'))
    izquierda(randint(0, 90))
    adelante(100)

hecho()
