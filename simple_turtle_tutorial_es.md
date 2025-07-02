<meta charset="UTF-8">

# Un Tutorial Sencillo de Turtle para el Módulo turtle.py de Python

*Una guía de programación para estudiantes, sus padres, docentes e instructores.*

**Este documento aún está en desarrollo y no está completo.**

## Introducción

Los gráficos de Turtle son una forma fácil de aprender a programar dibujando con código. Programas una pluma virtual, llamada la *tortuga*, para que se mueva por la pantalla y dibuje líneas. Puedes hacer dibujos con una computadora mientras aprendes a programar. Puedes pensar en la tortuga como un [Etch A Sketch](https://es.wikipedia.org/wiki/Etch_A_Sketch) controlado por tu programa de Python.

Esta guía explica cómo usar el módulo `turtle` de Python. No enseña el lenguaje Python en sí. Es recomendable tener conocimientos básicos de Python, como variables, operadores, bucles, funciones, importar módulos y números aleatorios. El libro gratuito [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/) es una introducción para principiantes totales.

Antes de empezar, necesitas descargar e instalar el *intérprete de Python* desde [python.org](https://python.org). También necesitas instalar un editor de código, como IDLE, [Mu](https://codewith.mu/) o [Visual Studio Code](https://code.visualstudio.com/download).

Incluso si no sabes programar en Python, aún puedes copiar el código de este tutorial en tu editor y ejecutarlo.


## Dibujar un Cuadrado

Vamos a hacer un programa que dibuja un cuadrado. Crea un nuevo archivo en tu editor de código. Guárdalo como *first_square.py*. Escribe el siguiente código de Python:

```python
# first_square.py

# Esto es un comentario.
# Todo lo que está después de # es un "comentario" y no se ejecuta como código.
# Usa los comentarios para escribir notas sobre tu código.

from turtle import *

pensize(4)  # Hace que las líneas sean más gruesas de lo normal.

forward(200)  # Mueve la tortuga hacia adelante 200 pasos.
left(90)  # Gira la tortuga 90 grados hacia la izquierda.

# Avanza y gira tres veces más:
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)

done()  # Sin esta línea, la ventana de Turtle puede cerrarse inmediatamente antes de que veas el dibujo.
```

Guarda el archivo después de ingresar el código. Luego ejecuta el programa. (Si estás usando IDLE como editor de código, puedes presionar F5 o hacer clic en el menú **Run > Run Module**. En Visual Studio Code, haz clic en el menú **Run > Run Without Debugging**. En otros editores, los pasos pueden ser diferentes).

Cuando ejecutes este programa, aparecerá una nueva ventana (que llamaremos la *ventana de Turtle*) con el siguiente dibujo:

![Cuadrado dibujado](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_first_square.jpg)

...



## Dibujar un Cuadrado Más Pequeño

Vamos a hacer un programa que dibuje un cuadrado más pequeño. Podemos cambiar `forward(200)` por `forward(25)` para que dibuje un cuadrado más pequeño. Crea un nuevo archivo en tu editor de código. Guárdalo como *square_smaller.py*. Escribe el siguiente código:

```python
# square_smaller.py
from turtle import *

pensize(4)
forward(25)  # Ahora la tortuga se mueve solo 25 pasos hacia adelante.
left(90)
forward(25)
left(90)
forward(25)
left(90)
forward(25)
left(90)
done()
```

Cuando ejecutes el programa, dibuja un cuadrado más pequeño porque las líneas solo tienen 25 pasos de largo en lugar de 200.

![Cuadrado más pequeño](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_square_smaller.jpg)

Recuerda que debes cambiar los cuatro lugares con `forward(200)` a `forward(25)`, o el cuadrado saldrá mal. Por ejemplo, hice un programa llamado *square_smaller_bug.py* que solo hizo el cambio en tres lugares:

```python
# square_smaller_bug.py
from turtle import *

pensize(4)
forward(25)
left(90)
forward(25)
left(90)
forward(200)  # ¡Uy! ¡Olvidamos cambiar esta línea!
left(90)
forward(25)
left(90)
done()
```

Este programa tiene un *error* y dibuja el cuadrado de manera incorrecta:

![Error en cuadrado más pequeño](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_square_smaller_bug.jpg)

¡Está bien cometer errores! Puedes corregirlos. Tu computadora hace exactamente lo que le dices que haga. Pero depende de ti asegurarte de que lo que *quieres* que haga es lo que realmente *le dijiste* que hiciera. Si tu programa tiene un error, lee cuidadosamente tu código y encuentra dónde está el problema.



## Errores Comunes y Mensajes de Error

Mientras escribes código en Python, puede que aparezcan mensajes de error al intentar ejecutar el programa. Presta atención al mensaje de error, especialmente donde dice el número de línea en que ocurrió el error. Aquí tienes algunos errores comunes que podrías ver y qué los causa:

* **`ModuleNotFoundError: No module named 'trutle'`** – Escribiste mal `turtle` en `from turtle import *`. Este error específico fue causado por el error tipográfico `from trutle import *`.
* **`NameError: name 'froward' is not defined`** – Escribiste mal el nombre de una función o variable. Este error específico fue causado por el error tipográfico `froward(100)`.
* **`TypeError: forward() missing 1 required positional argument: 'distance'`** – Llamaste a una función pero olvidaste incluir un argumento. Este error fue causado por `forward()` sin el argumento de distancia como en `forward(200)`.
* **`TypeError: left() takes 1 positional argument but 2 were given`** – Llamaste a una función con demasiados argumentos. Este error fue causado por `left(90, 45)`, pero la función `left()` solo espera un argumento como `left(90)`.
* **`IndentationError: unexpected indent`** – Hay demasiados espacios al principio de una línea de código.
* **`IndentationError: expected an indented block after 'for' statement on line 5`** – No aumentaste la sangría después de iniciar un bucle como `for i in range(4):`.
* **`SyntaxError: invalid syntax`** – Hay un problema general con tu código. Python no puede entenderlo, y no sabe qué sugerencia darte. ¡Pero sí te dice el número de línea donde notó el problema! Si escribes código apretando teclas al azar, probablemente verás este mensaje.

Cuando el mensaje de error dice que el error ocurre en, por ejemplo, la línea 5, es posible que la verdadera causa esté en la línea anterior: la línea 4. El intérprete de Python no pudo detectar el error hasta llegar a la línea siguiente.



## Dibujar un Cuadrado con un Bucle

Vamos a escribir un programa para dibujar un cuadrado usando un bucle `for`. Crea un nuevo archivo en tu editor de código. Guárdalo como *square_for_loop.py*. Escribe el siguiente código:

```python
# square_for_loop.py
from turtle import *

pensize(4)

# Las líneas con sangría se ejecutan 4 veces:
for i in range(4):  
    forward(200)
    left(90)
done()
```

El código con sangría después de `for i in range(4):` se ejecutará cuatro veces porque pasamos `4` a la función `range()`.

¡Asegúrate de tener exactamente cuatro espacios de sangría antes de las líneas `forward(200)` y `left(90)`! Si tienen una cantidad diferente de espacios, obtendrás un error como `IndentationError: unindent does not match any outer indentation level`.

Este es el mismo código, pero con puntos marcando los espacios:

```
for i in range(4):  
....forward(200)
....left(90)
done()
```

Este programa dibuja el mismo cuadrado que antes:

![Cuadrado con bucle](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_first_square.jpg)

Nuestro programa solo necesita llamar a `pensize(4)` una vez, así que lo ponemos antes del bucle.

Cambiemos el código para que la tortuga gire 86 grados en lugar de 90. Crea un nuevo archivo y guárdalo como *square_for_loop_86.py*:

```python
# square_for_loop_86.py
from turtle import *

pensize(4)

for i in range(4):  
    forward(200)
    left(86)  # Gira 86 grados en lugar de 90.
done()
```

Esto dibuja una figura que no es exactamente un cuadrado:

![Cuadrado distorsionado](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_square_for_loop_86.jpg)

En lugar de girar 86 grados cuatro veces, vamos a hacer el bucle 50 veces. Crea un archivo llamado *square_circle_86.py*:

```python
# square_circle_86.py
from turtle import *

pensize(4)
speed('fastest')

for i in range(50):  # Repetir 50 veces.
    forward(200)
    left(86)
hideturtle()
done()
```

Este programa dibuja mucho más que los anteriores, por eso usamos la función `speed()` con el argumento `'fastest'` para hacer que la tortuga se mueva más rápido.

Los argumentos válidos para `speed()` son `'fastest'`, `'fast'`, `'normal'`, `'slow'` y `'slowest'`.

También llamamos a la función `hideturtle()` para que el cursor triangular de la tortuga desaparezca al final del programa.

Este dibujo se ve muy distinto a un simple cuadrado:

![Figura circular con ángulos](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_square_circle_86.jpg)

Al experimentar con diferentes valores y código, podemos crear todo tipo de imágenes. También podemos hacer que Python use números aleatorios para los giros. Crea un archivo llamado *square_random.py*:

```python
# square_random.py
from turtle import *
from random import *

pensize(4)
speed('fastest')

for i in range(50):
    forward(200)
    # Girar a la izquierda un número aleatorio entre 80 y 100 grados:
    left(randint(80, 100))
hideturtle()
done()
```

Como este programa usa números aleatorios, el dibujo será distinto cada vez que lo ejecutes:

![Dibujo aleatorio 1](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_square_random1.jpg)
![Dibujo aleatorio 2](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_square_random2.jpg)

La instrucción `from random import *` permite que el programa llame a la función `randint()`. Esta función devuelve un número entero aleatorio que puedes usar como argumento en otras funciones. La instrucción `left(randint(80, 100))` hace que la tortuga gire una cantidad aleatoria entre 80 y 100 grados.

Cuando combinamos bucles y números aleatorios, [podemos crear arte generativo](https://duckduckgo.com/?t=ffab&q=generative+art&iax=images&ia=images). No creamos el arte directamente, sino que escribimos programas que lo generan. ¡Hay muchas imágenes distintas que podemos hacer con Turtle!



## Revisión Rápida 1

Vamos a repasar las instrucciones de Python que hemos visto hasta ahora.

Puedes crear comentarios con el carácter `#`:

```python
# Esto es un comentario.
```

Todo lo que está después del símbolo `#` hasta el final de la línea es un comentario. Los comentarios son notas que puedes escribir para recordarte qué hace el programa. Puedes escribir lo que quieras en un comentario. No afectan cómo funciona el programa.

Tus programas siempre deben importar el módulo `turtle`:

```python
from turtle import *
```

El módulo `turtle` debe importarse antes de que puedas usar sus funciones. Siempre pon `from turtle import *` al principio de tu programa.

Hay funciones que pueden mover el cursor de la tortuga:

```python
forward(100)  # Mueve la tortuga 100 pasos hacia adelante.
backward(100)  # Mueve la tortuga 100 pasos hacia atrás.
forward(-100)  # También mueve hacia atrás.
```

Puedes mover la tortuga hacia adelante y hacia atrás usando las funciones `forward()` y `backward()`. Si pasas un número negativo, la tortuga se moverá en la dirección opuesta.

También hay funciones que pueden girar la dirección hacia la que apunta la tortuga:

```python
left(90)  # Gira 90 grados a la izquierda.
right(45)  # Gira 45 grados a la derecha.
```

Puedes girar la tortuga a la izquierda (en sentido antihorario) o a la derecha (en sentido horario) pasando el número de grados a las funciones `left()` y `right()`. La tortuga solo gira, no cambia de posición. Si pasas un número negativo, girará en la dirección contraria.

Por defecto, la tortuga dibuja una línea delgada al moverse. Puedes hacer esta línea más gruesa:

```python
pensize(4)
```

El tamaño del lápiz es `1` por defecto, pero puedes pasar un número mayor a `pensize()` para hacer líneas más gruesas.

Lo último que debe hacer tu programa con turtle es llamar a la función `done()`:

```python
done()
```

Llamar a `done()` al final del programa mantiene abierta la ventana después de que se termine de dibujar. Así aseguras que la ventana de Turtle no se cierre automáticamente antes de ver el resultado final.

Puedes usar números como argumentos para funciones, pero también puedes guardar esos números en variables y pasar las variables como argumentos:

```python
line_length = 25  # Esta variable guarda el número 25.
forward(line_length)
```

Este código guarda `25` en una variable llamada `line_length`. El código `forward(line_length)` es lo mismo que `forward(25)`.

Un bucle `for` te permite repetir instrucciones:

```python
for i in range(4):  
    forward(200)
    left(90)
```

Un bucle `for` repetirá las instrucciones con sangría después de él. En este ejemplo, el código `forward(200)` y `left(90)` se ejecuta cuatro veces porque usamos `range(4)`. Esto dibuja los cuatro lados de un cuadrado.

Por defecto, la tortuga se mueve lentamente. Puedes hacer que se mueva más rápido usando `speed('fastest')`:

```python
speed('fastest')
```

Recuerda incluir las comillas. Debes llamar a `speed('fastest')` y no `speed(fastest)`.

A veces el cursor de la tortuga estorba en el dibujo final. Puedes hacerlo desaparecer con `hideturtle()`:

```python
hideturtle()
```

Si no quieres que el triángulo del cursor de la tortuga aparezca en la ventana, llama a la función `hideturtle()`.

En lugar de escribir números tú mismo, puedes hacer que Python genere números aleatorios:

```python
from random import *
forward(randint(1, 100))
```

La llamada a `randint(1, 100)` devuelve un número aleatorio entre 1 y 100. Debes haber ejecutado `from random import *` antes de usar esta función.



## Ejercicios de Práctica 1

Crea programas que dibujen las figuras de esta sección. Las soluciones están al final de este tutorial. Tu código y tus dibujos no tienen que coincidir exactamente con los ejemplos, pero deben verse similares. Hay muchas formas distintas de escribir el código para estos programas.

Crea un programa llamado *solution_equilateral_triangle.py* que dibuje la siguiente figura. *Sugerencia: Todas las líneas del triángulo equilátero miden 200 pasos. El primer giro es de 60 grados a la derecha. Los siguientes giros son de 120 grados.*

![Triángulo equilátero](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_solution_equilateral_triangle.jpg)

Crea un programa llamado *solution_pentagon.py* que dibuje la siguiente figura. *Sugerencia: Todas las líneas del pentágono miden 200 pasos. Todos los giros son de 72 grados.*

![Pentágono](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_solution_pentagon.jpg)

Crea un programa llamado *solution_hexagon.py* que dibuje la siguiente figura. *Sugerencia: Todas las líneas del hexágono miden 200 pasos. Todos los giros son de 60 grados.*

![Hexágono](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_solution_hexagon.jpg)

Crea un programa llamado *solution_octagon.py* que dibuje la siguiente figura. *Sugerencia: Todas las líneas del octágono miden 100 pasos. Todos los giros son de 45 grados.*

![Octágono](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_solution_octagon.jpg)

Crea un programa llamado *solution_right_triangle.py* que dibuje la siguiente figura. *Sugerencia: Para el triángulo rectángulo, un giro es de 90 grados y el otro de 135 grados. Dos lados miden 200 pasos. Según el teorema de Pitágoras, el tercer lado mide 282.8 pasos.*

![Triángulo rectángulo](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_solution_right_triangle.jpg)

Crea un programa llamado *solution_star.py* que dibuje la siguiente figura. *Sugerencia: Todas las líneas de la estrella miden 200 pasos. Todos los giros son de 144 grados.*

![Estrella](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_solution_star.jpg)

Crea un programa llamado *solution_nested_squares.py* que dibuje la siguiente figura. *Sugerencia: Dibuja un cuadrado con lados de 100 pasos. Luego uno de 150, 200, 250 y 300 pasos. Puedes usar un bucle `for` dentro de otro bucle `for` para hacerlo.*

![Cuadrados anidados](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_solution_nested_squares.jpg)

Crea un programa llamado *solution_cross.py* que dibuje la siguiente figura. *Sugerencia: Todas las líneas de la cruz miden 100 pasos. Todos los giros son de 90 grados, pero deberás usar giros a la izquierda y a la derecha.*

![Cruz](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_solution_cross.jpg)

Crea un programa llamado *solution_cube.py* que dibuje la siguiente figura. *Sugerencia: Todas las líneas miden 100 pasos. Todos los giros son de 45, 90 o 135 grados. Puede que debas superponer algunas líneas para dibujar el cubo completo. Puedes usar `forward(100)` seguido de `backward(100)` si quieres dibujar una línea y regresar a la posición original.*

![Cubo](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_solution_cube.jpg)

Crea un programa llamado *solution_triforce.py* que dibuje la siguiente figura. *Sugerencia: Hay muchas formas de dibujar esto. Puedes superponer líneas. Todos los giros son de 60 o 120 grados. Si los lados del triángulo exterior miden 100 pasos, tal vez debas mover la tortuga solo 50 pasos a veces.*

![Trifuerza](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_solution_triforce.jpg)



## Escribir Texto en la Ventana de Turtle

La tortuga puede escribir texto en la ventana de Turtle al igual que dibuja líneas. La función `write()` toma como argumento un texto en forma de cadena y lo escribe donde esté la tortuga. Vamos a crear un programa que escriba texto en la ventana. Crea un nuevo archivo en tu editor de código. Guárdalo como *write_hello.py*. Escribe el siguiente código:

```python
# write_hello.py

from turtle import *

write('¡Hola, mundo!')
forward(80)
right(45)
forward(50)
write('123456789', font=('Arial', 48, 'normal'))
right(45)
forward(30)
write('oOoOoOoOoOo')
done()
```

Cuando ejecutes este programa, se verá así:

![Texto en Turtle](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_write_hello.jpg)

La esquina inferior izquierda del texto está en la posición de la tortuga. Por ejemplo, el código `write('¡Hola, mundo!')` aparece en el centro de la ventana de Turtle, donde comienza la tortuga. Luego la tortuga se mueve con `forward(80)`, `right(45)` y `forward(50)`. Cuando se ejecuta `write('123456789', font=('Arial', 48, 'normal'))`, el texto "123456789" aparece en la nueva posición de la tortuga.

La llamada a la función `write('123456789', font=('Arial', 48, 'normal'))` también tiene un *parámetro con palabra clave* llamado `font=`. Podemos pasarle un argumento como `('Arial', 48, 'normal')` para cambiar la fuente del texto en la ventana de Turtle.

Hay tres partes en el argumento del parámetro `font=`:

* El nombre de la fuente. (`'Arial'`)
* El tamaño de la fuente. (`48`)
* El estilo de la fuente. (`'normal'`)

Si no se pasa ningún argumento, la fuente por defecto es `('Arial', 8, 'normal')`. Puedes cambiar el nombre de la fuente, pero debe estar instalada en tu computadora. El argumento del tamaño debe ser un número, no una cadena: debes pasar `8`, no `'8'`. El argumento de estilo puede ser `'normal'`, `'bold'`, `'italic'`, `'underline'`, o cualquier combinación de estas palabras como `'bold italic'`.



## Ángulos

En los programas con Turtle, podemos medir la distancia en pasos. Por ejemplo, `forward(100)` mueve la tortuga una distancia de 100 pasos. También podemos medir giros y direcciones usando números.

Imagina que estás en el cielo mirando hacia abajo a la tortuga en el suelo. Si la tortuga gira a la "derecha", está girando en sentido horario. Si gira a la izquierda, desde nuestra perspectiva está girando en sentido antihorario.

Medimos los giros en "grados". Un giro completo es de 360 grados. Si la tortuga gira 180 grados, termina apuntando en la dirección opuesta. Un giro “normal” a la izquierda o derecha es de 90 grados. Si haces cuatro giros de 90 grados a la derecha, terminas apuntando en la misma dirección original. Esto es porque 90 + 90 + 90 + 90 = 360.

También podemos usar los grados para describir hacia qué *dirección* o *rumbo* está apuntando la tortuga. Cuando el programa comienza, la tortuga siempre comienza apuntando hacia la derecha. Esta dirección es `0` grados. A medida que la tortuga gira **a la izquierda** (o en sentido antihorario), la dirección aumenta. Apuntar hacia arriba es `90` grados, hacia la izquierda es `180` grados y hacia abajo es `270` grados. Tanto `360` como `0` grados apuntan hacia la derecha.

La función `heading()` devuelve el número que representa la dirección en la que actualmente está mirando la tortuga. Podemos pasarlo a `write()` para mostrar la dirección actual en la ventana de Turtle.

Crea un nuevo programa llamado `turtle_directions.py` con el siguiente código:

```python
# turtle_directions.py
from turtle import *

for i in range(24):
    forward(100)  # Avanza en la dirección actual.
    write(heading(), font=('Arial', 20, 'normal'))  # Escribe los grados de dirección.
    backward(100)  # Regresa al centro.
    left(15)  # Gira 15 grados a la izquierda y repite.
done()
```

Cuando ejecutes este programa, la ventana Turtle se verá así:

![Direcciones](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_turtle_directions.jpg)

Las funciones `left()` y `right()` hacen que la tortuga gire a partir de su dirección actual. Si la tortuga está mirando a 45 grados y llamas a `left(90)`, la nueva dirección será 135 porque 45 + 90 = 135. Pero la función `setheading()` puede hacer que la tortuga mire en una dirección específica sin importar su dirección actual.

La función `heading()` devuelve un número que indica hacia dónde está apuntando la tortuga.

Por ejemplo, crea un nuevo programa llamado `setheading_turtle.py` con el siguiente código:

```python
# setheading_turtle.py

from turtle import *
from random import *

pensize(4)
left(randint(0, 360))
write(heading())
forward(200)

setheading(45)
write(heading())
forward(200)

done()
```

Este programa hace que la tortuga mire en una dirección aleatoria, escribe esa dirección (usando `heading()`) en la ventana y se mueve 200 pasos en esa dirección. Luego, `setheading(45)` cambia la dirección de la tortuga a 45 grados. Por eso, la segunda línea `write(heading())` siempre muestra “45.0” en la ventana. La tortuga apunta hacia la parte superior derecha. Luego la tortuga se mueve 200 pasos en esa nueva dirección.

Esto significa que sin importar la dirección anterior, `setheading(45)` hace que la tortuga siempre mire hacia la parte superior derecha. Si ejecutas el programa varias veces, se verá algo así:

![Ejemplo 1](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_setheading_turtle1.jpg)
![Ejemplo 2](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_setheading_turtle2.jpg)
![Ejemplo 3](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_setheading_turtle3.jpg)
![Ejemplo 4](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_setheading_turtle4.jpg)



## Coordenadas Cartesianas XY

Así como los grados son números que pueden describir hacia dónde está apuntando la tortuga o cuánto debe girar, la *posición* de la tortuga también puede representarse con dos números. En el *sistema de coordenadas cartesianas*, la *coordenada X* representa qué tan a la izquierda o derecha está la tortuga. La *coordenada Y* representa qué tan arriba o abajo está. Juntas, las coordenadas XY indican exactamente dónde está la tortuga.

* El centro de la ventana se llama *origen* y tiene coordenadas XY de `0` y `0`.
* Cuando se escriben juntas, la coordenada X va primero y la Y va después. Las coordenadas (4, -7) significan X = 4 e Y = -7.
* Las coordenadas X aumentan hacia la derecha y disminuyen hacia la izquierda.
* Las coordenadas Y aumentan hacia arriba y disminuyen hacia abajo.
* Una tortuga en la mitad izquierda de la ventana siempre tiene una X negativa.
* Una tortuga en la mitad derecha siempre tiene una X positiva.
* Una tortuga en la mitad inferior siempre tiene una Y negativa.
* Una tortuga en la mitad superior siempre tiene una Y positiva.

Esta imagen de Wikipedia muestra un sistema de coordenadas cartesianas con algunos puntos de ejemplo:

![Coordenadas cartesianas](cartesian.png)

Vamos a crear un programa que escriba las coordenadas XY en la ventana mientras la tortuga se mueve. Crea un archivo llamado *random_position.py* con el siguiente código:

```python
# random_position.py
from turtle import *
from random import *

for i in range(8):
    write(position())
    left(randint(0, 90))
    forward(100)

done()
```

Cuando ejecutes este programa, la salida se verá algo así:

![Coordenadas aleatorias](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_random_position.jpg)

La tortuga comienza en el origen, es decir, en las coordenadas (0, 0). Observa que al moverse hacia la derecha o hacia arriba, las coordenadas X y Y aumentan. Al moverse hacia la izquierda o hacia abajo, disminuyen.

Las funciones `forward()` y `backward()` siempre mueven desde la posición actual de la tortuga. Pero puedes mover la tortuga a coordenadas XY específicas usando la función `goto(x, y)`.

Vamos a crear un programa que mueva la tortuga a coordenadas aleatorias. Guárdalo como *random_goto.py* y escribe el siguiente código:

```python
# random_goto.py
from turtle import *
from random import *

pensize(4)

for i in range(6):    
    x = randint(-400, 400)
    y = randint(-400, 400)
    goto(x, y)
    write(position(), font=('Arial', 18, 'normal'))

done()
```

Cuando ejecutes este programa, la salida será algo como esto:

![Goto aleatorio 1](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_random_goto1.jpg)
![Goto aleatorio 2](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_random_goto2.jpg)
![Goto aleatorio 3](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_random_goto3.jpg)
![Goto aleatorio 4](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_random_goto4.jpg)

La instrucción `x = randint(-400, 400)` guarda un número entero aleatorio en la variable `x`. La siguiente línea hace lo mismo para `y`. Luego `goto(x, y)` mueve la tortuga a las coordenadas aleatorias.



## Inicio, Limpiar, Reiniciar, Deshacer

La tortuga dibuja líneas a medida que se mueve, pero hay varias funciones para borrar estas líneas:

* `home()` mueve la tortuga de regreso a las coordenadas XY (0, 0) y establece la dirección a 0 grados. Es lo mismo que llamar a `goto(0, 0)` y `setheading(0)`.
* `clear()` borra todas las líneas que la tortuga ha dibujado, pero deja la tortuga donde está.
* `reset()` mueve la tortuga al origen y borra todas las líneas. Es lo mismo que llamar a `home()` y `clear()`.
* `undo()` borra la última acción de la tortuga. Puedes llamarla varias veces para deshacer múltiples líneas o movimientos.

Estas funciones son útiles cuando estás experimentando con código y quieres limpiar la pantalla o empezar desde el centro.



## Revisión Rápida 2

Repasemos las instrucciones de Python que hemos aprendido hasta ahora:

```python
write('¡Hola, mundo!')
write('¡Hola, mundo!', font=('Arial', 48, 'normal'))
```

La función `write()` escribe texto en la ventana de Turtle donde esté el cursor de la tortuga. Puedes pasarle un texto como cadena. También puedes usar el argumento con palabra clave `font=` para cambiar el tamaño o estilo de la fuente.

```python
setheading(90)
direccion_actual = heading()
```

La función `setheading()` establece la dirección en la que está apuntando la tortuga. `0` grados apunta hacia la derecha (este), `90` grados hacia arriba (norte), `180` grados hacia la izquierda (oeste) y `270` grados hacia abajo (sur).

La función `heading()` devuelve el valor de la dirección actual de la tortuga. Puedes usar este valor en otras funciones o guardarlo en una variable.

```python
goto(250, -100)  # Mueve el cursor de la tortuga a las coordenadas XY 250, -100.
```

* Una coordenada XY es un par de números que indica la posición de algo.
* El centro de la ventana de Turtle es el *origen*, en (0, 0).
* Las coordenadas X aumentan hacia la derecha y disminuyen hacia la izquierda.
* Las coordenadas Y aumentan hacia arriba y disminuyen hacia abajo.

Para reiniciar tu dibujo, tu programa puede llamar a las siguientes funciones:

* `home()` es lo mismo que llamar a `goto(0, 0)` y `setheading(0)`.
* `clear()` borra todas las líneas que la tortuga ha dibujado.
* `reset()` es lo mismo que llamar a `home()` y `clear()`.
* `undo()` borra la línea más reciente que ha dibujado la tortuga.



## Ejercicios de Práctica 2

Crea un programa llamado *solution_star_outline.py* que dibuje la siguiente figura. Usa únicamente `goto()` para mover la tortuga. *Sugerencia: Las coordenadas que debes pasar a `goto()` son (0, 300), (70, 95), (285, 95), (110, -35), (175, -260),
(0, -100), (-175, -260), (-110, -35), (-285, 95), (-70, 95) y (0, 300).*

![Contorno de estrella](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_solution_star_outline.jpg)

Crea un programa llamado *solution_cross_setheading.py* que dibuje la siguiente figura. No uses `right()` ni `left()` sino únicamente `setheading()`. *Sugerencia: Todas las líneas de la cruz miden 100 pasos. Todas las direcciones son 0, 90, 180 o 270.*

![Cruz con setheading](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_solution_cross.jpg)

Crea un programa llamado *solution_random_hello.py* que escriba "¡Hola, mundo!" cien veces en lugares aleatorios de la ventana Turtle. El texto también debe tener tamaños aleatorios entre 12 y 48. No dibujes líneas y oculta el cursor de la tortuga. El programa se verá algo así:

![Hola mundo aleatorio](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_solution_random_hello.jpg)



## Colores

Puedes cambiar el color de fondo de la ventana usando la función `bgcolor()` y pasándole una cadena de texto con el nombre del color o un valor RGB de tres números (explicado más adelante):

* `'black'` es `(0.0, 0.0, 0.0)`
* `'blue'` es `(0.0, 0.0, 1.0)`
* `'brown'` es `(0.6, 0.4, 0.2)`
* `'orange'` es `(1.0, 0.5, 0.0)`
* `'gray'` es `(0.5, 0.5, 0.5)`
* `'green'` es `(0.0, 1.0, 0.0)`
* `'purple'` es `(0.5, 0.0, 0.5)`
* `'violet'` es `(0.56, 0.0, 1.0)`
* `'pink'` es `(1.0, 0.75, 0.8)`
* `'yellow'` es `(1.0, 1.0, 0.0)`
* `'white'` es `(1.0, 1.0, 1.0)`
* `'red'` es `(1.0, 0.0, 0.0)`
* `'magenta'` es `(1.0, 0.0, 1.0)`
* `'cyan'` es `(0.0, 1.0, 1.0)`

Puedes cambiar el color de las líneas de la tortuga pasando un color a la función `pencolor()`.

Por ejemplo, si añades `bgcolor('yellow')` y `pencolor('blue')`, el fondo será amarillo y las líneas de la tortuga serán azules en el archivo *square_circle_86.py*:

![Fondo amarillo](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_bgcolor_yellow.jpg)

Los colores personalizados usan un *valor RGB*, que se basa en los colores primarios de la luz: rojo, verde y azul. (Esto es diferente a los colores primarios de pigmentos: rojo, amarillo y azul.) Cada uno de los valores de rojo, verde y azul están entre `0.0` (nada) y `1.0` (máximo). Por ejemplo, `(1.0, 0.0, 0.0)` es lo mismo que `'red'` porque tiene rojo al máximo y nada de verde ni azul.

Cuando los tres valores están en su máximo, producen blanco: `(1.0, 1.0, 1.0)` es igual a `'white'`. Cuando los tres valores están en cero, producen negro: `(0.0, 0.0, 0.0)` es igual a `'black'`. Puedes aumentar los valores para obtener colores más claros o disminuirlos para obtener colores más oscuros.

Otro ejemplo: `(1.0, 1.0, 0.0)` es igual a `'yellow'` porque mezcla rojo y verde al máximo sin azul. Sin embargo, `(1.0, 1.0, 0.5)` produce un amarillo más claro, mientras que `(0.5, 0.5, 0)` produce un amarillo más oscuro.

Puedes usar la aplicación `turtlecolors` para ver los valores RGB de diferentes colores. Copia el código de https://raw.githubusercontent.com/asweigart/turtlecolors/refs/heads/main/src/turtlecolors/__init__.py y pégalo en un archivo llamado *turtlecolors.py*, luego ejecuta el programa. Puedes ajustar los tres deslizadores para rojo, verde y azul y ver qué color producen.

La aplicación se ve así al ejecutarla:

![Turtlecolors 1](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_turtlecolors1.jpg)
![Turtlecolors 2](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_turtlecolors2.jpg)
![Turtlecolors 3](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_turtlecolors3.jpg)
![Turtlecolors 4](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_turtlecolors4.jpg)



## Subir y Bajar el Lápiz

Imagina que la tortuga tiene un lápiz en la boca. Cuando el lápiz toca el suelo, la tortuga dibuja una línea al moverse. Si el lápiz está levantado del suelo, la tortuga no dibuja nada al moverse. Las funciones `pendown()` y `penup()` controlan si la tortuga dibuja o no.

Los programas de Turtle siempre comienzan con el lápiz bajado.

Vamos a crear un programa que dibuje una línea punteada. Guarda el archivo como *dashed_lines.py* y escribe el siguiente código:

```python
# dashed_lines.py
from turtle import *
from random import *

pensize(4)
speed('fastest')

for i in range(12):
    # Girar en una dirección aleatoria:
    setheading(randint(0, 360))

    # Dibujar una línea punteada en esa dirección:
    for j in range(6):
        pendown()
        forward(10)  # Dibujar un segmento.
        penup()
        forward(10)  # Moverse sin dibujar.
    
    # Dibujar un último segmento:
    pendown()
    forward(10)

done()
```

El bucle `for i in range(12):` dibuja doce líneas punteadas. Cada línea punteada se dibuja con el bucle `for j in range(6):`. La tortuga se mueve 10 pasos con el lápiz abajo y luego 10 pasos con el lápiz arriba, lo que crea una línea punteada.

Como el programa usa números aleatorios, el dibujo será distinto cada vez que lo ejecutes:

![Líneas punteadas 1](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_dashed1.jpg)
![Líneas punteadas 2](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_dashed2.jpg)



## Ejemplos de Espirales Cuadradas

Vamos a crear un programa que dibuje una espiral cuadrada. Guarda el archivo como *spiral.py* y escribe el siguiente código:

```python
# spiral.py
from turtle import *

speed('fastest')
for i in range(300):
    forward(i)  # Usamos la variable i como argumento de la función.
    left(91)
hideturtle()
done()
```

Cuando ejecutes este programa, se verá así:

![Espiral](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_spiral.jpg)

En nuestros programas anteriores con bucles `for`, hemos ignorado la variable `i`. Pero en este programa, usamos la variable `i` en la línea `forward(i)`.

En este bucle `for`, la variable `i` comienza en `0` y cada vez que se repite el bucle, se incrementa en 1. Así, `forward(i)` se convierte en `forward(0)`, luego `forward(1)`, `forward(2)`, y así sucesivamente hasta `forward(299)`.

Eso significa que el programa hace lo siguiente:

```python
from turtle import *

speed('fastest')

forward(0)
left(91)
forward(1)
left(91)
forward(2)
left(91)
forward(3)
left(91)
forward(4)
left(91)

# ...muchas líneas después...

forward(297)
left(91)
forward(298)
left(91)
forward(299)
left(91)

hideturtle()
done()
```

¡Usar un bucle `for` nos ahorra escribir muchas líneas de código!

Prueba cambiar el `91` en `left(91)` por otros valores entre `30` y `180`. Luego ejecuta el programa nuevamente y observa cómo cambia el dibujo.

Ahora, vamos a crear una espiral colorida y aleatoria. Guarda el archivo como *spiral_black_bg.py* y escribe el siguiente código:

```python
# spiral_black_bg.py
from turtle import *
from random import *

colors = ['red', 'orange', 'yellow', 'blue', 'green', 'purple']

speed('fastest')
pensize(3)
bgcolor('black')
for i in range(300):
    pencolor(choice(colors))
    forward(i)
    left(91)
hideturtle()
done()
```

Cuando ejecutes este programa, se verá así:

![Espiral de colores](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_spiral_black_bg.jpg)

La función `choice()` (del módulo `random`) elige aleatoriamente uno de los valores del listado de colores. Esto hace que cada línea tenga un color diferente.

También podemos crear una espiral con colores en orden como un arcoíris. Guarda el archivo como *spiral_rainbow.py* y escribe este código:

```python
# spiral_rainbow.py
from turtle import *

speed('fastest')
pensize(3)
bgcolor('black')

pencolor('red')
for i in range(60):
    forward(i)
    left(91)

pencolor('orange')
for i in range(60):
    forward(60 + i)
    left(91)

pencolor('yellow')
for i in range(60):
    forward(120 + i)
    left(91)

pencolor('green')
for i in range(60):
    forward(180 + i)
    left(91)

pencolor('blue')
for i in range(60):
    forward(240 + i)
    left(91)

pencolor('purple')
for i in range(60):
    forward(300 + i)
    left(91)

done()
```

Cada uno de los bucles `for` en este programa dibuja líneas de un color diferente. Los bucles también agregan un valor a `i` en cada llamada a `forward()` para hacer líneas cada vez más largas.

Cuando ejecutas este programa, se ve así:

![Espiral arcoíris](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_spiral_rainbow.jpg)



## Dibujar Muy Rápido

Si `speed('fastest')` sigue siendo muy lento, puedes hacer que tu programa use `tracer(100, 0)` en su lugar. Sin embargo, para asegurarte de que todas las líneas aparezcan en la ventana de Turtle, debes recordar llamar a `update()` cuando termines de dibujar. Si necesitas que el programa dibuje aún más rápido, puedes aumentar el número `100` a `1000` o incluso `10000`.

Vamos a demostrar qué tan rápido puede tu computadora dibujar 1,000 líneas. Crea un nuevo archivo llamado *random_tracer.py* y escribe el siguiente código:

```python
# random_tracer.py

from turtle import *
from random import *

tracer(10, 0)

for i in range(1000):
    goto(randint(-400, 400), randint(-400, 400))

update()
done()
```

Cuando ejecutes este programa, la ventana de Turtle se verá algo como esto:

![Trazado rápido](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_random_tracer.jpg)

Con `tracer(10, 0)`, el programa tarda unos segundos en dibujar las 1,000 líneas. Pero si lo cambias por `tracer(100, 0)`, el programa puede terminar en aproximadamente un segundo. Si lo cambias por `tracer(1000, 0)`, puede dibujar casi instantáneamente.

A partir de cierto valor alto, tu computadora estará dibujando lo más rápido que puede, y aumentar el número no acelerará más. (Usualmente ese número es alrededor de `1000`.)

Si tu programa no está mostrando todas las líneas, probablemente olvidaste agregar la llamada a `update()` después de terminar el dibujo.

