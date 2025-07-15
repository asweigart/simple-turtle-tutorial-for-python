# direcciones_tortuga.py
from tortuga import *

for i in range(24):
    adelante(200)  # Avanza en la dirección actual.
    escribir(direccion(), fuente=('Arial', 12, 'normal'))  # Escribe los grados de orientación.
    atras(200)     # Regresa al centro.
    izquierda(15)  # Gira 15 grados a la izquierda y repite.
hecho()
