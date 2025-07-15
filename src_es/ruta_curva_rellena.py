# ruta_curva_rellena.py

from tortuga import *
from random import *

tasa_dibujo(4, 0)

for i in range(50):
    # Color de relleno aleatorio:
    color_relleno((random(), random(), random()))

    # Definir un ángulo aleatorio y dibujar varias líneas cortas:
    establecer_direccion(randint(0, 360))
    comenzar_rellenar()
    for j in range(randint(200, 600)):
        adelante(1)
        izquierda(randint(-4, 4))
    origen()
    terminar_relleno()

actualizar()
hecho()
