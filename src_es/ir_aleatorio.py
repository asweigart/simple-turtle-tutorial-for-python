# ir_aleatorio.py
from tortuga import *
from random import *

tamano_pluma(4)

for i in range(6):
    x = randint(-400, 400)
    y = randint(-400, 400)
    ir_a(x, y)
    escribir(posicion(), fuente=('Arial', 18, 'normal'))

hecho()