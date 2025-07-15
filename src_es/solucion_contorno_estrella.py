# solucion_contorno_estrella.py
from tortuga import *
tamano_pluma(4)

pluma_arriba()
ir_a(0, 300)

pluma_abajo()
ir_a(70, 95)
ir_a(285, 95)
ir_a(110, -35)
ir_a(175, -260)
ir_a(0, -100)
ir_a(-175, -260)
ir_a(-110, -35)
ir_a(-285, 95)
ir_a(-70, 95)
ir_a(0, 300)

hecho()
