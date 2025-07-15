# solucion_saludo_aleatorio.py
from tortuga import *
from random import *

tasa_dibujo(1000, 0)
pluma_arriba()
ocultar_tortuga()

for i in range(100):
    ir_a(randint(-400, 400), randint(-400, 400))
    escribir('Hello, world!', fuente=('Arial', randint(12, 48), 'normal'))

update()
hecho()
