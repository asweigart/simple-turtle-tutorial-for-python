# dibujar_muchos_circulos.py
from tortuga import *

velocidad('mas rapida')

for j in range(6):
    establecer_direccion(j)
    for i in range(20):
        circulo(i * 10)

    establecer_direccion(j + 120)
    for i in range(20):
        circulo(i * 10)

    establecer_direccion(j + 240)
    for i in range(20):
        circulo(i * 10)

hecho()