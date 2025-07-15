# solucion_cubo.py
from tortuga import *
tamano_pluma(4)

# Cuadrado frontal:
for i in range(4):
    adelante(200)
    derecha(90)

# Diagonal superior izquierda:
izquierda(45)
adelante(200)
derecha(45)

# Lado superior del cuadrado trasero:
adelante(200)
derecha(135)
adelante(200)
atras(200)
izquierda(45)

# Lado derecho del cuadrado trasero:
adelante(200)
derecha(45)
adelante(200)
atras(200)
derecha(45)

# Lado inferior del cuadrado trasero:
adelante(200)
izquierda(45)
adelante(200)
atras(200)

# Lado izquierdo del cuadrado trasero:
derecha(135)
adelante(200)

hecho()
