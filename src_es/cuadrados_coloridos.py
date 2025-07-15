# cuadrados_coloridos.py

from tortuga import *
from random import *

tamano_pluma(4)
tasa_dibujo(10, 0)

for i in range(100):  # Dibuja 100 cuadrados.
    # Mover a un lugar aleatorio:
    pluma_arriba()
    ir_a(randint(-400, 200), randint(-400, 200))
    pluma_abajo()

    # Colores de relleno y de pluma aleatorios:
    color_relleno((random(), random(), random()))
    color_pluma((random(), random(), random()))

    # Tamaño del cuadrado aleatorio:
    longitud_linea = randint(20, 200)

    # Dibujar el cuadrado relleno:
    comenzar_rellenar()
    for j in range(4):
        adelante(longitud_linea)
        izquierda(90)
    terminar_relleno()

hecho()
