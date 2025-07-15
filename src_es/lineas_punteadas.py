# lineas_punteadas.py
from tortuga import *
from random import *

tamano_pluma(4)
velocidad('mas rapida')

for i in range(12):
    # Apunta en una dirección aleatoria:
    establecer_direccion(randint(0, 360))

    # Dibuja una línea punteada:
    for j in range(6):
        pluma_abajo()
        adelante(10)   # Dibuja un segmento.
        pluma_arriba()
        adelante(10)   # Avanza sin dibujar.

    # Último segmento:
    pluma_abajo()
    adelante(10)

hecho()