# flores_azules.py
from tortuga import *
from random import *

tracer(100, 0)

for n in range(50):
    # Mover a una posición aleatoria:
    pluma_arriba()
    x = randint(-300, 300)
    y = randint(-300, 300)
    ir_a(x, y)
    pluma_abajo()

    # Crear un tono de azul aleatorio:
    color_pluma((0, 0, random()))

    # Grosor de pluma aleatorio:
    tamano_pluma(randint(1, 5))

    # Tamaño aleatorio para los círculos:
    tamano_circulo = randint(10, 40)

    # Dibujar seis círculos:
    for i in range(6):
        circulo(tamano_circulo)
        izquierda(60)

actualizar()
hecho()
