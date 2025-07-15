# establecer_direccion_tortuga.py

from tortuga import *
from random import *

tamano_pluma(4)
izquierda(randint(0, 360))
escribir(direccion(), fuente=('Arial', 48, 'normal'))
adelante(200)

establecer_direccion(45)
escribir(direccion(), fuente=('Arial', 48, 'normal'))
adelante(200)

hecho()
