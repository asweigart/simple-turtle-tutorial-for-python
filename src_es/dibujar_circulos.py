# dibujar_circulos.py
from tortuga import *

velocidad('mas rapida')

# Dibujar círculos en la mitad superior de la ventana:
establecer_direccion(0)  # Mirar hacia la derecha.
for i in range(20):
    circulo(i * 10)

# Dibujar círculos en la mitad inferior de la ventana:
establecer_direccion(180)  # Mirar hacia la izquierda.
for i in range(20):
    circulo(i * 10)

hecho()