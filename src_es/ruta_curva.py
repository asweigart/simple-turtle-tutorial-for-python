# ruta_curva.py

from tortuga import *
from random import *

tracer(4, 0)

for i in range(100):  # Dibuja 100 trayectorias curvas.
    # Mover la tortuga de regreso al origen (0, 0):
    pluma_arriba()
    origen()
    pluma_abajo()

    # Fijar un ángulo aleatorio y dibujar varias líneas cortas con cambio de dirección:
    establecer_direccion(randint(0, 360))
    for j in range(randint(200, 600)):  # Cada curva tiene de 200 a 600 segmentos.
        adelante(1)         # Cada segmento mide 1 paso.
        izquierda(randint(-4, 4))  # Cambia ligeramente la dirección

actualizar()
hecho()