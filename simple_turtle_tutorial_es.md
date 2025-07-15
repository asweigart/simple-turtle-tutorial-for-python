
*Una guía de programación para estudiantes y sus padres, profesores e instructores.*

Este es un tutorial de programación con Tortuga escrito por Al Sweigart, autor de *Automate the Boring Stuff with Python* y otros libros de programación. Puedes leer todos sus libros de forma gratuita en [https://inventwithpython.com](https://inventwithpython.com).

Este tutorial fue originalmente escrito en inglés y traducido al español. Los enlaces externos corresponden a recursos en inglés. Si tienes correcciones para este tutorial, por favor envía un correo a [al@inventwithpython.com](mailto:al@inventwithpython.com).


## Tabla de Contenidos

1. [Introducción](#Introduction)
2. [Dibujo de un cuadrado](#Drawing-a-Square)
3. [Dibujo de un cuadrado más pequeño](#Drawing-a-Smaller-Square)
4. [Errores comunes y mensajes de error](#Common-Bugs-and-Error-Messages)
5. [Dibujar un cuadrado con un bucle](#Draw-a-Square-with-a-Loop)
6. [Revisión rápida 1](#Quick-Review-1)
7. [Ejercicios de práctica 1](#Practice-Exercises-1)
8. [Escribir texto en la ventana de Tortuga](#Writing-Text-in-the-Turtle-Window)
9. [Ángulos](#Angles)
10. [Coordenadas cartesianas XY](#XY-Cartesian-Coordinates)
11. [Inicio, borrar, reiniciar, deshacer](#Home-Clear-Reset-Undo)
12. [Revisión rápida 2](#Quick-Review-2)
13. [Ejercicios de práctica 2](#Practice-Exercises-2)
14. [Colores](#Colors)
15. [Levantar y bajar la pluma](#Raising-and-Lowering-the-Pen)
16. [Ejemplos de espirales cuadrados](#Square-Spirals-Examples)
17. [Dibujar muy rápido](#Drawing-Very-Fast)
18. [Dibujo interactivo](#Interactive-Drawing)
19. [Dibujar curvas y círculos](#Draw-Curves-and-Circles)
20. [Programa Flores Azules](#Blue-Flowers-Program)
21. [Formas rellenas](#Filled-In-Shapes)
22. [Para más información](#For-More-Information)
23. [Desafíos avanzados de Tortuga](#Advanced-Turtle-Challenges)
24. [Soluciones](#Solutions)
25. [Contactar al autor](#Contact-the-Author)
26. [Lista de URLs del sitio web en este tutorial](#List-of-Website-URLs-in-this-Tutorial)

<a name="Introduction" />

## Introducción

Los gráficos de Tortuga son una manera fácil de aprender programación dibujando con código. Programas una pluma virtual, llamada *tortuga*, para que se mueva por la pantalla y trace líneas. Haces dibujos con la computadora mientras aprendes a programar. Puedes pensar en la tortuga como un [Etch A Sketch](https://en.wikipedia.org/wiki/Etch_A_Sketch) controlado por tu programa de Python.

Esta guía explica cómo usar el módulo `turtle` de Python a través del paquete Tortuga. No enseña el lenguaje Python en sí. Es bueno ya conocer ideas básicas de Python, como variables, operadores, bucles, funciones, importación de módulos y números aleatorios. El libro gratuito *Automate the Boring Stuff with Python* en [https://automatetheboringstuff.com/](https://automatetheboringstuff.com/) es una introducción para principiantes completos. Si te interesa más programar videojuegos, puedes leer *Invent Your Own Computer Games with Python* en [https://inventwithpython.com](https://inventwithpython.com).

Antes de comenzar, necesitas descargar e instalar el *intérprete de Python* (el software que ejecuta el código Python) desde [https://python.org](https://python.org). Hay una guía para instalar Python en el sitio Real Python, en [https://realpython.com/installing-python/](https://realpython.com/installing-python/).

También necesitas instalar un *editor de código* como:

* IDLE, que viene con el intérprete de Python.
* Mu, gratuito en [https://codewith.mu/](https://codewith.mu/).
* Visual Studio Code, gratuito en [https://code.visualstudio.com/download](https://code.visualstudio.com/download).

Hay una guía para usar IDLE en Real Python, en [https://realpython.com/python-idle/](https://realpython.com/python-idle/).

Los programas escritos en Python se llaman *programas Python*. No todos usan gráficos de Tortuga. Pero en esta guía, llamaremos *programas Tortuga* a los que usan el módulo `turtle` (a través de Tortuga).

Aunque no sepas programar en Python, puedes copiar el código de este tutorial en tu editor y ejecutarlo.

**Nota para las versiones de este tutorial que no están en inglés:** El lenguaje de programación Python incluye el paquete `turtle`. Sin embargo, el código del paquete `turtle` está en inglés. El paquete `tortuga` proporciona código traducido a varios idiomas. Para instalar el paquete `tortuga`, ejecuta el siguiente código desde el intérprete interactivo de Python, también llamado REPL. El intérprete interactivo muestra el prompt `>>>` o `In [1]:`.

```python
import sys, subprocess; subprocess.run([sys.executable, '-m', 'pip', 'install', 'tortuga'])
```

Para verificar si `tortuga` se instaló correctamente, ejecuta el siguiente código desde el intérprete interactivo:

```python
from tortuga import *
```

Si no aparece nada, entonces `tortuga` se instaló correctamente.

Las palabras clave y los mensajes de error del lenguaje de programación Python siguen en inglés. Puedes usar [https://translate.google.com/](https://translate.google.com/) para traducirlos. La versión original en inglés de este tutorial está en [https://inventwithpython.com/stt/](https://inventwithpython.com/stt/)


<div style="page-break-after: always;"></div>

<a name="Drawing-a-Square" />

## Dibujo de un cuadrado

Hagamos un programa que dibuje un cuadrado. Crea un archivo nuevo en tu editor de código. Guárdalo como *primer\_cuadrado.py*. Introduce el siguiente código Python:

```python
# primer_cuadrado.py

# Esto es un comentario.
# Todo lo que esté después de # es un "comentario" y no se ejecuta como código.
# Usa comentarios para hacer anotaciones sobre tu código.

from tortuga import *

tamano_pluma(4)  # Haz que las líneas sean más gruesas de lo normal.

adelante(200)  # Mueve la tortuga adelante 200 pasos.
izquierda(90)  # Gira la tortuga a la izquierda 90 grados.

# Avanza y gira tres veces más:
adelante(200)
izquierda(90)
adelante(200)
izquierda(90)
adelante(200)
izquierda(90)

hecho()  # Sin esto, la ventana de Tortuga podría cerrarse antes de que veas el dibujo.
```

Guarda el archivo tras introducir el código. Luego ejecuta el programa. (En IDLE pulsa F5 o haz clic en **Run > Run Module**. En Visual Studio Code, **Run > Run Without Debugging**. En otros editores, los pasos pueden variar.)

Cuando lo ejecutes, aparecerá una nueva ventana (la *ventana Tortuga*) con el siguiente dibujo:

[<img src="https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_first_square.webp" style="width: 400px"/>](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_first_square.webp)

En la ventana Tortuga, la tortuga aparece como un triángulo. Imagina que la tortuga lleva una pluma en la boca y dibuja líneas al moverse. El código Python le indica cómo moverse:

1. Avanza 200 pasos. (Al iniciar, la tortuga mira hacia la derecha.)
2. Gira 90 grados a la izquierda.
3. Avanza 200 pasos.
4. Gira 90 grados a la izquierda.
5. Avanza 200 pasos.
6. Gira 90 grados a la izquierda.
7. Avanza 200 pasos. (La tortuga vuelve al punto de partida.)
8. Gira 90 grados a la izquierda. (Queda en la dirección original.)
9. El programa termina, pero la ventana Tortuga sigue abierta para que veas el resultado.

Con estos nueve pasos, la tortuga dibuja un cuadrado. Esto es lo básico de cada instrucción:

```python
# primer_cuadrado.py

# Esto es un comentario.
# Todo lo que esté después de # es un "comentario" y no se ejecuta como código.
# Usa comentarios para hacer anotaciones sobre tu código.
```

La línea `# primer_cuadrado.py` es un *comentario* que Python ignora. No es necesario copiarlo; solo identifica el nombre del programa en este tutorial.

Las líneas en blanco también se ignoran.

```python
from tortuga import *
```

Debes tener `from tortuga import *` al inicio de tus programas Tortuga. Esto importa todas las funciones de Tortuga para que puedas usar llamadas como `tamano_pluma()`, `adelante()`, `izquierda()` y `hecho()`. Si olvidas esta línea, tu programa fallará con un error `NameError: name '...' is not defined`.

```python
tamano_pluma(4)  # Haz que las líneas sean más gruesas de lo normal.
```

`pensize` es una función y `pensize(4)` es una llamada a la función. Una *función* es como un mini-programa que contiene código. Tu programa puede ejecutar el código de las funciones realizando una *llamada a la función*. Las llamadas a funciones pueden recibir valores, como el `4` en `pensize(4)`. Estos se llaman *argumentos de función* o simplemente *argumentos*.

En este tutorial, siempre añadimos paréntesis al nombre de una función para que sea fácil ver que es una función: “la función `pensize()`”

```python
adelante(200)  # Mueve la tortuga adelante 200 pasos.
izquierda(90)  # Gira la tortuga a la izquierda 90 grados.

# Avanza y gira tres veces más:
adelante(200)
izquierda(90)
adelante(200)
izquierda(90)
adelante(200)
izquierda(90)
```

La llamada `adelante(200)` hace que la tortuga se mueva hacia adelante en su dirección actual por 100 pasos. Mientras la tortuga se mueve, dibuja una línea detrás de ella. Imagina una tortuga con un marcador negro en la boca, dibujando líneas en el suelo mientras avanza.

La función `izquierda()` hace que la tortuga gire su dirección hacia la izquierda. Imagina que estamos en el cielo mirando hacia abajo a la tortuga en la ventana del programa. La izquierda de la tortuga es en sentido contrario a las agujas del reloj. La llamada `izquierda(90)` en nuestro programa hace que la tortuga gire 90 grados a la izquierda.

(Si quieres que la tortuga gire a la derecha o en sentido horario, también existe la función `derecha()`.)

```python
hecho()  # Sin esto, la ventana de Tortuga podría cerrarse antes de que veas el dibujo.
```

La función `hecho()` mantiene el programa en ejecución hasta que cierres la ventana. Sin ella, Python terminaría el programa y cerraría la ventana al instante.

La llamada a la función `hecho()` no tiene argumentos, pero todavía debes escribir los paréntesis `()` después de `hecho`.

Hay muchas otras funciones como `izquierda()`, `adelante()` y `hecho()`. A medida que aprendas más funciones del módulo `turtle`, podrás dibujar formas y figuras cada vez más complejas.

Pero primero, hagamos algunos programas Tortuga más sencillos.

<div style="page-break-after: always;"></div>

<a name="Drawing-a-Smaller-Square" />

## Dibujo de un cuadrado más pequeño

Hagamos un programa que dibuje un cuadrado más pequeño. Podemos cambiar `adelante(200)` a `adelante(25)` para dibujar un cuadrado reducido. Crea un archivo nuevo en tu editor de código. Guárdalo como *cuadrado\_mas\_pequeno.py*. Introduce el siguiente código Python:

```python
# cuadrado_mas_pequeno.py
from tortuga import *

tamano_pluma(4)  # Haz que las líneas sean más gruesas de lo normal.

adelante(25)  # Ahora la tortuga avanza solo 25 pasos.
izquierda(90)
adelante(25)
izquierda(90)
adelante(25)
izquierda(90)
adelante(25)
izquierda(90)

hecho()  # Sin esto, la ventana de Tortuga podría cerrarse antes de que veas el dibujo.
```

Cuando ejecutes el programa, dibuja un cuadrado más pequeño porque las líneas miden solo 25 pasos en lugar de 200:

[<img src="https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_square_smaller.webp" style="width: 400px"/>](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_square_smaller.webp)

Recuerda que debes cambiar las **cuatro** llamadas de `adelante(200)` a `adelante(25)`, o el cuadrado saldrá mal. Por ejemplo, creé un programa llamado *cuadrado\_mas\_pequeno\_error.py* que solo cambió tres de ellas:

```python
# cuadrado_mas_pequeno_error.py
from tortuga import *

tamano_pluma(4)
adelante(25)
izquierda(90)
adelante(25)
izquierda(90)
adelante(200)  # ¡Ups, olvidamos cambiar esta línea!
izquierda(90)
adelante(25)
izquierda(90)

hecho()
```

Este programa tiene un *bug* y dibuja el cuadrado incorrectamente:

[<img src="https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_square_smaller_bug.webp" style="width: 400px"/>](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_square_smaller_bug.webp)

¡Está bien cometer errores! Puedes corregirlos. Tu computadora hace exactamente lo que le indicas. Está en ti asegurarte de que lo que **quieres** que haga sea lo que le **dices** que haga.

<div style="page-break-after: always;"></div>

<a name="Common-Bugs-and-Error-Messages" />

## Errores comunes y mensajes de error

Al escribir código en Python, puede que obtengas mensajes de error al intentar ejecutar el programa. Presta atención al mensaje, especialmente donde indica el número de línea donde ocurre el error. Aquí algunos errores frecuentes y sus causas:

* **`ModuleNotFoundError: No module named 'trotuga'`** – Has cometido un error tipográfico en `from tortuga import *`. Por ejemplo, `from trotuga import *` provoca este mensaje.
* **`NameError: name 'aedlante' is not defined`** – Has escrito mal el nombre de una función o variable. Por ejemplo, `aedlante(200)` causa este error.
* **`TypeError: adelante() missing 1 required positional argument: 'distancia'`** – Hiciste una llamada a `adelante()` pero olvidaste incluir el argumento de distancia, como en `adelante(200)`.
* **`TypeError: izquierda() takes 1 positional argument but 2 were given`** – Llamaste a `izquierda()` con dos argumentos (`izquierda(90, 45)`), pero esta función solo acepta uno (`izquierda(90)`).
* **`IndentationError: unexpected indent`** – Hay demasiados espacios al inicio de la línea de código.
* **`IndentationError: expected an indented block after 'for' statement on line 5`** – No aumentaste la sangría después de la sentencia `for i in range(4):`.
* **`SyntaxError: invalid syntax`** – Hay un problema general en tu código. Python no puede entenderlo y no sabe cómo corregirlo, aunque te indica la línea donde lo detectó.

Cuando el mensaje señala, por ejemplo, la línea 5, el error real puede estar en la línea anterior: línea 4. El intérprete de Python solo se da cuenta del problema al llegar a la línea 5.

<div style="page-break-after: always;"></div>

<a name="Drawing-a-Square-with-a-Variable-Size" />

## Dibujo de un cuadrado con tamaño variable

En lugar de escribir `25` en `adelante(25)`, creemos una *variable*. La llamaremos `longitud_linea` y su valor será `25`.

Crea un archivo nuevo. Guárdalo como *cuadrado\_variable.py*. Introduce:

```python
# cuadrado_variable.py
from tortuga import *

tamano_pluma(4)
longitud_linea = 25  # Esta variable almacena el número 25.
adelante(longitud_linea)  # La tortuga avanza 25 pasos.
izquierda(90)
adelante(longitud_linea)
izquierda(90)
adelante(longitud_linea)
izquierda(90)
adelante(longitud_linea)
izquierda(90)

hecho()
```

Al ejecutar, dibuja el mismo cuadrado que antes:

[<img src="https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_square_smaller.webp" style="width: 400px"/>](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_square_smaller.webp)

Ahora, para cambiar el tamaño solo necesitas modificar `longitud_linea`, por ejemplo `longitud_linea = 300` o `longitud_linea = 5`.

<div style="page-break-after: always;"></div>

<a name="Draw-a-Square-with-a-Loop" />

## Dibujar un cuadrado con un bucle

Usemos un bucle `for` para dibujar el cuadrado. Crea un archivo nuevo. Guárdalo como *cuadrado\_con\_bucle.py*. Escribe:

```python
# cuadrado_con_bucle.py
from tortuga import *

tamano_pluma(4)

# Las líneas con sangría se ejecutan 4 veces:
for i in range(4):
    adelante(200)
    izquierda(90)
hecho()
```

El código indentado tras `for i in range(4):` se repite cuatro veces.

**Asegúrate** de usar exactamente cuatro espacios de sangría antes de `adelante(200)` y `izquierda(90)`; si no, obtendrás un `IndentationError: unindent does not match any outer indentation level`.

Con puntos para marcar los espacios:

```
for i in range(4):
....adelante(200)
....izquierda(90)
hecho()
```

Este programa dibuja el mismo cuadrado que antes:

[<img src="https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_first_square.webp" style="width: 400px"/>](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_first_square.webp)

Nuestro programa solo necesita llamar a `tamano_pluma(4)` una vez, por eso lo ponemos antes del bucle.

Cambiemos `izquierda(90)` por `izquierda(86)`. Crea un archivo nuevo. Guárdalo como *cuadrado\_bucle\_86.py*. Escribe:

```python
# cuadrado_bucle_86.py
from tortuga import *

tamano_pluma(4)

for i in range(4):
    adelante(200)
    izquierda(86)  # Gira 86 grados en lugar de 90.
hecho()
```

Esto dibuja una figura distinta, no un cuadrado perfecto:

[<img src="https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_square_for_loop_86.webp" style="width: 400px"/>](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_square_for_loop_86.webp)

### Bucle de 50 iteraciones

En lugar de 4, hagamos el bucle 50 veces. Crea un archivo nuevo. Guárdalo como *circulo\_cuadrado\_86.py*. Escribe:

```python
# circulo_cuadrado_86.py
from tortuga import *

tamano_pluma(4)
velocidad('mas rapida')  # Hace que la tortuga se mueva más rápido.

for i in range(50):  # 50 iteraciones en vez de 4.
    adelante(200)
    izquierda(86)
ocultar_tortuga()  # Oculta el cursor de la tortuga al final.
hecho()
```

En este programa llamamos a `velocidad()` con la cadena `'mas rapida'`. A diferencia de 200 o 86, este valor es texto y debe ir entre comillas: `'mas rapida'` o `"mas rapida"`.

Los argumentos que puedes pasar a `velocidad()` son, de más rápido a más lento:
`'mas rapida'`, `'rapida'`, `'normal'`, `'lenta'` y `'mas lenta'`.

Este programa también usa `ocultar_tortuga()` para hacer desaparecer el cursor.

El resultado es muy diferente de un cuadrado simple:

[<img src="https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_square_circle_86.webp" style="width: 400px"/>](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_square_circle_86.webp)

Al experimentar con distintos números podemos crear todo tipo de dibujos. También podemos usar números aleatorios para los giros. Hagamos un programa que dibuje un cuadrado con giros entre 80 y 100 grados. Crea un archivo nuevo. Guárdalo como *cuadrado\_aleatorio.py*. Escribe:

```python
# cuadrado_aleatorio.py
from tortuga import *
from random import *

tamano_pluma(4)
velocidad('mas rapida')

for i in range(50):
    adelante(200)
    # Gira a la izquierda un número aleatorio de grados entre 80 y 100:
    izquierda(randint(80, 100))
ocultar_tortuga()
hecho()
```

Como este programa usa números aleatorios, la imagen será diferente cada vez:

[<img src="https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_square_random1.webp" style="width: 400px"/>](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_square_random1.webp)
[<img src="https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_square_random2.webp" style="width: 400px"/>](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_square_random2.webp)
[<img src="https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_square_random3.webp" style="width: 400px"/>](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_square_random3.webp)
[<img src="https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_square_random4.webp" style="width: 400px"/>](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_square_random4.webp)

La instrucción `from random import *` permite usar la función `randint()`, que devuelve un *entero* aleatorio. La llamada `izquierda(randint(80, 100))` gira la tortuga aleatoriamente entre 80 y 100 grados.

Cuando nuestro programa combina bucles y números aleatorios, podemos crear "arte generativo". No hacemos el arte nosotros mismos, sino los programas que lo generan. Busca en Internet "generative art" para ver ejemplos. ¡Hay muchísimas imágenes que podemos aprender a dibujar con Tortuga!


<div style="page-break-after: always;"></div>

<a name="Quick-Review-1" />

## Revisión rápida 1

Repasemos las instrucciones de Python vistas hasta ahora.

Puedes crear comentarios con el carácter `#`:

```python
# Esto es un comentario.
```

Todo lo que sigue al `#` hasta el final de la línea es un comentario. Los comentarios son notas para recordarte qué hace el programa. Puedes escribir cualquier cosa en un comentario; no cambian el funcionamiento del programa.

Tus programas siempre deben importar el módulo `turtle` (a través de Tortuga):

```python
from tortuga import *
```

Este import debe ir al principio de tu programa antes de llamar a cualquier función de Tortuga.

Hay funciones que mueven la tortuga:

```python
adelante(100)    # Mueve la tortuga 100 pasos hacia adelante.
atras(100)       # Mueve la tortuga 100 pasos hacia atrás.
adelante(-100)   # Mueve la tortuga 100 pasos hacia atrás.
```

Puedes mover la tortuga adelante y atrás llamando a `adelante()` y `atras()`. Pasar un número negativo hace que la tortuga se mueva en la dirección opuesta.

También hay funciones que giran la tortuga:

```python
izquierda(90)    # Gira 90 grados a la izquierda.
derecha(45)      # Gira 45 grados a la derecha.
```

Llamar a `izquierda()` gira la tortuga en sentido contrario a las agujas del reloj, y `derecha()` la gira en el sentido de las agujas del reloj. Pasar un número negativo invierte el sentido del giro.

Por defecto, la tortuga dibuja líneas delgadas. Puedes hacerlas más gruesas:

```python
tamano_pluma(4)
```

El tamaño de pluma es `1` por defecto; pasar un número mayor a `tamano_pluma()` engrosa la línea.

Al final de tu programa Tortuga debes llamar a:

```python
hecho()
```

`hecho()` mantiene la ventana abierta después de que el dibujo ha terminado, evitando que se cierre inmediatamente.

Puedes usar valores numéricos directamente, o almacenarlos en variables:

```python
longitud_linea = 25   # Esta variable almacena el número 25.
adelante(longitud_linea)
```

El código `adelante(longitud_linea)` es equivalente a `adelante(25)`.

Un bucle `for` te permite repetir instrucciones:

```python
for i in range(4):
    adelante(200)
    izquierda(90)
```

El código con sangría tras `for i in range(4):` se ejecuta cuatro veces, dibujando los cuatro lados de un cuadrado.

Por defecto la tortuga dibuja despacio. Puedes acelerar el trazado:

```python
velocidad('mas rapida')
```

Recuerda las comillas: `velocidad('mas rapida')`, no `velocidad(mas rapida)`.

A veces el cursor de la tortuga estorba en el dibujo final. Puedes ocultarlo:

```python
ocultar_tortuga()
```

Para usar números aleatorios:

```python
from random import *
adelante(randint(1, 100))
```

La llamada a la función `randint(1, 100)` devuelve un número aleatorio entre `1` y `100`. Debe ejecutar `from random import *` antes de usar esta función.

<div style="page-break-after: always;"></div>

<a name="Practice-Exercises-1" />

## Ejercicios de práctica 1

Crea programas que dibujen las imágenes de esta sección. Las soluciones están al final del tutorial. Tu código y dibujo no tienen que coincidir exactamente, pero deben ser similares.

---

Crea un programa llamado *solucion\_triangulo\_equilatero.py* que dibuje esta imagen.
**Pista:** Todas las líneas del triángulo equilátero miden 200 pasos. El primer giro es de 60 grados a la derecha; los siguientes, de 120 grados.

[<img src="https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_solution_equilateral_triangle.webp" style="width: 400px"/>](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_solution_equilateral_triangle.webp)

---

Crea un programa llamado *solucion\_pentagono.py* que dibuje esta imagen.
**Pista:** Todas las líneas del pentágono miden 200 pasos. Todos los giros son de 72 grados.

[<img src="https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_solution_pentagon.webp" style="width: 400px"/>](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_solution_pentagon.webp)

---

Crea un programa llamado *solucion\_hexagono.py* que dibuje esta imagen.
**Pista:** Todas las líneas del hexágono miden 200 pasos. Todos los giros son de 60 grados.

[<img src="https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_solution_hexagon.webp" style="width: 400px"/>](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_solution_hexagon.webp)

---

Crea un programa llamado *solucion\_octagono.py* que dibuje esta imagen.
**Pista:** Todas las líneas del octágono miden 100 pasos. Todos los giros son de 45 grados.

[<img src="https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_solution_octagon.webp" style="width: 400px"/>](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_solution_octagon.webp)

---

Crea un programa llamado *solucion\_triangulo\_rectangulo.py* que dibuje esta imagen.
**Pista:** Un giro es de 90 grados y el otro de 135 grados. Dos lados miden 200 pasos. Según el Teorema de Pitágoras, el tercer lado mide 282.8 pasos.

[<img src="https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_solution_right_triangle.webp" style="width: 400px"/>](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_solution_right_triangle.webp)

---

Crea un programa llamado *solucion\_estrella.py* que dibuje esta imagen.
**Pista:** Todas las líneas de la estrella miden 200 pasos. Todos los giros son de 144 grados.

[<img src="https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_solution_star.webp" style="width: 400px"/>](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_solution_star.webp)

---

Crea un programa llamado *solucion\_cuadrados\_anidados.py* que dibuje esta imagen.
**Pista:** Dibuja cuadrados de lados 100, luego 150, 200, 250 y 300 pasos. Puedes usar un `for` dentro de otro `for`.

[<img src="https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_solution_nested_squares.webp" style="width: 400px"/>](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_solution_nested_squares.webp)

---

Crea un programa llamado *solucion\_cruz.py* que dibuje esta imagen.
**Pista:** Todas las líneas de la cruz miden 100 pasos. Todos los giros son de 90 grados, alternando giros a la izquierda y a la derecha.

[<img src="https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_solution_cross.webp" style="width: 400px"/>](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_solution_cross.webp)

---

Crea un programa llamado *solucion\_cubo.py* que dibuje esta imagen.
**Pista:** Todas las líneas miden 100 pasos. Los giros son de 45, 90 o 135 grados. Puede que necesites superponer líneas usando `adelante(100)` y luego `atras(100)` para volver al punto inicial.

[<img src="https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_solution_cube.webp" style="width: 400px"/>](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_solution_cube.webp)

---

Crea un programa llamado *solucion\_trifuerza.py* que dibuje esta imagen.
**Pista:** Los giros son de 60 o 120 grados. Si el triángulo exterior tiene lados de 100 pasos, a veces querrás avanzar 50 pasos en su interior.

[<img src="https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_solution_triforce.webp" style="width: 400px"/>](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_solution_triforce.webp)

<a name="Writing-Text-in-the-Turtle-Window" />

## Escribir texto en la ventana de Tortuga

La tortuga puede escribir texto en la ventana de Tortuga tal como dibuja líneas. La función `escribir()` recibe como argumento una cadena de texto y la imprime en la posición actual de la tortuga. Hagamos un programa que escriba texto en la ventana. Crea un archivo nuevo en tu editor de código. Guárdalo como *escribir\_hola.py*. Introduce el siguiente código Python:

```python
# escribir_hola.py

from tortuga import *

escribir('¡Hola, mundo!')
adelante(80)
derecha(45)
adelante(50)
escribir('123456789', fuente=('Arial', 48, 'normal'))
derecha(45)
adelante(30)
escribir('oOoOoOoOoOo')
hecho()
```

Al ejecutar este programa, verás algo así:

[<img src="https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_write_hello.webp" style="width: 400px"/>](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_write_hello.webp)

La esquina inferior izquierda del texto coincide con la posición de la tortuga. Por ejemplo, `escribir('¡Hola, mundo!')` aparece en el centro de la ventana, donde inicia la tortuga. Luego la tortuga avanza y gira con `adelante(80)`, `derecha(45)` y `adelante(50)`. Cuando se ejecuta `escribir('123456789', fuente=('Arial', 48, 'normal'))`, el texto “123456789” aparece en la nueva posición de la tortuga.

La llamada `escribir('123456789', fuente=('Arial', 48, 'normal'))` también usa un *parámetro con nombre* `fuente=`. Podemos pasarle una tupla como `('Arial', 48, 'normal')` para cambiar la tipografía del texto.

Hay tres partes en el argumento de `fuente=`:

* El nombre de la tipografía. (`'Arial'`)
* El tamaño de la tipografía. (`48`)
* El estilo de la tipografía. (`'normal'`)

Si no pasas este argumento, la tipografía predeterminada es `('Arial', 8, 'normal')`. Puedes cambiar el nombre de la tipografía siempre que esté instalada en tu sistema. El tamaño debe ser un número (sin comillas). El estilo puede ser `'normal'`, `'negrita'`, `'cursiva'`, `'subrayada'` o cualquier combinación como `'negrita cursiva'`.

<div style="page-break-after: always;"></div>

<a name="Angles" />

## Ángulos

En los programas de Tortuga, la distancia se mide en pasos. Por ejemplo, `adelante(100)` mueve la tortuga 100 pasos. También podemos medir giros y dirección usando números.

Imagina que estás en el cielo mirando desde arriba. Si la tortuga gira a la **derecha**, está girando en el sentido de las agujas del reloj. Si gira a la **izquierda**, gira en sentido contrario a las agujas.

Medimos los giros en “grados”. Una vuelta completa son 360 grados. Si la tortuga gira 180 grados, queda mirando hacia el lado opuesto. Un giro “normal” es de 90 grados. Cuatro giros de 90 grados a la derecha suman 360 y devuelven a la tortuga a su orientación inicial.

También usamos grados para describir la *orientación* que tiene la tortuga en cada momento. Al iniciar el programa, la tortuga siempre mira hacia la derecha (0 grados). Al girar **izquierda** (antihorario), su orientación aumenta: 90 grados mira hacia arriba, 180 grados hacia la izquierda, 270 grados hacia abajo. Tanto 360 como 0 grados significan “hacia la derecha”.

La función `direccion()` devuelve la orientación actual en grados. Podemos pasar ese valor a `escribir()` para mostrarla en pantalla.

Crea un programa nuevo llamado *direcciones\_tortuga.py* con este código:

```python
# direcciones_tortuga.py
from tortuga import *

for i in range(24):
    adelante(200)  # Avanza en la dirección actual.
    escribir(direccion(), fuente=('Arial', 12, 'normal'))  # Escribe los grados de orientación.
    atras(200)     # Regresa al centro.
    izquierda(15)  # Gira 15 grados a la izquierda y repite.
hecho()
```

Al ejecutarlo, la ventana de Tortuga se ve así:

[<img src="https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_turtle_directions.webp" style="width: 400px"/>](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_turtle_directions.webp)

Las funciones `izquierda()` y `derecha()` giran según la orientación actual. Si la tortuga mira a 45 grados y llamas `izquierda(90)`, pasará a 135 grados (45 + 90). Sin embargo, la función `establecer_direccion()` fija la tortuga a la orientación indicada, sin importar su estado previo.

Por ejemplo, crea un programa llamado *establecer\_direccion\_tortuga.py* con este código:

```python
# establecer_direccion_tortuga.py

from tortuga import *
from random import *

tamano_pluma(4)
izquierda(randint(0, 360))
escribir(direccion(), fuente=('Arial', 48, 'normal'))
adelante(200)

establecer_direccion(45)
escribir(direccion(), fuente=('Arial', 48, 'normal'))
adelante(200)

hecho()
```

Al ejecutarlo, la tortuga gira a un ángulo aleatorio, escribe ese valor (grados) en pantalla y avanza 200 pasos. Luego `establecer_direccion(45)` fija la orientación a 45 grados, de modo que la segunda llamada a `escribir(direccion())` siempre muestra “45.0”. La tortuga apunta hacia la esquina superior derecha y avanza otros 200 pasos en esa dirección.

Así, sin importar la orientación inicial, `establecer_direccion(45)` hace que la tortuga mire siempre hacia arriba a la derecha. Si ejecutas varias veces, verás algo como esto:

[<img src="https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_setheading_turtle1.webp" style="width: 400px"/>](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_setheading_turtle1.webp)
[<img src="https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_setheading_turtle2.webp" style="width: 400px"/>](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_setheading_turtle2.webp)
[<img src="https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_setheading_turtle3.webp" style="width: 400px"/>](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_setheading_turtle3.webp)
[<img src="https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_setheading_turtle4.webp" style="width: 400px"/>](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_setheading_turtle4.webp)

<a name="XY-Cartesian-Coordinates" />

## Coordenadas cartesianas XY

Así como los grados son números que describen hacia dónde mira la tortuga o cuánto debe girar, la *posición* de la tortuga se representa con dos números. En el *sistema de coordenadas cartesianas*, la *coordenada X* indica qué tan a la izquierda o a la derecha está la tortuga, y la *coordenada Y* qué tan arriba o abajo. Juntas, las coordenadas XY indican exactamente la posición de la tortuga.

* El centro de la ventana se llama *origen* y tiene coordenadas XY `0, 0`.
* Al escribirlas, la coordenada X va primero y la Y después. (4, -7) significa X = 4 e Y = –7.
* Los valores de X aumentan hacia la derecha y disminuyen hacia la izquierda.
* Los valores de Y aumentan hacia arriba y disminuyen hacia abajo.
* Una tortuga en la mitad izquierda tiene siempre X negativo.
* Una tortuga en la mitad derecha tiene siempre X positivo.
* Una tortuga en la mitad inferior tiene siempre Y negativo.
* Una tortuga en la mitad superior tiene siempre Y positivo.

Esta imagen de Wikipedia muestra un sistema cartesiano con algunos puntos de ejemplo:

[<img src="https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_cartesian.webp" style="width: 400px"/>](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_cartesian.webp)

Hagamos un programa que escriba las coordenadas XY en la ventana a medida que la tortuga se mueve. Crea un archivo nuevo en tu editor de código. Guárdalo como *posicion\_aleatoria.py*. Introduce el siguiente código Python:

```python
# posicion_aleatoria.py
from tortuga import *
from random import *

for i in range(8):
    escribir(posicion(), fuente=('Arial', 18, 'normal'))
    izquierda(randint(0, 90))
    adelante(100)

hecho()
```

Al ejecutar este programa, verás algo como esto:

[<img src="https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_random_position.webp" style="width: 400px"/>](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_random_position.webp)

La tortuga comienza en el origen, es decir, en las coordenadas 0, 0. Observa que al moverse a la derecha o arriba, X e Y aumentan; al moverse a la izquierda o abajo, disminuyen.

Las funciones `adelante()` y `atras()` siempre mueven desde la posición actual. Sin embargo, puedes llevar la tortuga a coordenadas específicas con `ir_a(x, y)` pasando los valores X e Y.

Hagamos ahora un programa que mueva la tortuga a coordenadas aleatorias. Crea un archivo nuevo. Guárdalo como *ir\_aleatorio.py*. Introduce el siguiente código Python:

```python
# ir_aleatorio.py
from tortuga import *
from random import *

tamano_pluma(4)

for i in range(6):
    x = randint(-400, 400)
    y = randint(-400, 400)
    ir_a(x, y)
    escribir(posicion(), fuente=('Arial', 18, 'normal'))

hecho()
```

Al ejecutar este programa, verás algo como esto:

[<img src="https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_random_goto1.webp" style="width: 400px"/>](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_random_goto1.webp)
[<img src="https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_random_goto2.webp" style="width: 400px"/>](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_random_goto2.webp)
[<img src="https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_random_goto3.webp" style="width: 400px"/>](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_random_goto3.webp)
[<img src="https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_random_goto4.webp" style="width: 400px"/>](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_random_goto4.webp)

La instrucción `x = randint(-400, 400)` guarda un número entero aleatorio entre –400 y 400 en la variable `x`, y `y = randint(-400, 400)` hace lo mismo para `y`. Luego, `ir_a(x, y)` lleva la tortuga a esas coordenadas.

<div style="page-break-after: always;"></div>
::contentReference[oaicite:0]{index=0}

## Colores

Puedes cambiar el color de fondo de la ventana con la función `color_pluma()` y pasarle uno de estos nombres de color (o su valor RGB si prefieres):

* `'negro'` es `(0.0, 0.0, 0.0)`
* `'azul'` es `(0.0, 0.0, 1.0)`
* `'marron'` es `(0.6, 0.4, 0.2)`
* `'naranja'` es `(1.0, 0.5, 0.0)`
* `'gris'` es `(0.5, 0.5, 0.5)`
* `'verde'` es `(0.0, 1.0, 0.0)`
* `'morado'` es `(0.5, 0.0, 0.5)`
* `'violeta'` es `(0.56, 0.0, 1.0)`
* `'rosa'` es `(1.0, 0.75, 0.8)`
* `'amarillo'` es `(1.0, 1.0, 0.0)`
* `'blanco'` es `(1.0, 1.0, 1.0)`
* `'rojo'` es `(1.0, 0.0, 0.0)`
* `'magenta'` es `(1.0, 0.0, 1.0)`
* `'cian'` es `(0.0, 1.0, 1.0)`
* Un color aleatorio es `(random(), random(), random())` (tras `from random import *`)

Para cambiar el color de las líneas de la tortuga, usa `color_pluma()` de la misma manera.

Por ejemplo, agregando `color_pluma('amarillo')` y `color_pluma('azul')` al programa *circulo\_cuadrado\_86.py*:

[<img src="https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_bgcolor_yellow.webp" style="width: 400px"/>](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_bgcolor_yellow.webp)

Los colores personalizados usan un valor *RGB* (rojo, verde, azul) con cada componente entre `0.0` (ninguno) y `1.0` (máximo). Por ejemplo, `(1.0, 0.0, 0.0)` equivale a `'rojo'`, y `(1.0, 1.0, 0.0)` a `'amarillo'`. Ajusta los valores para obtener tonos más claros o más oscuros.

Puedes usar el programa **Turtle Colors** para explorar valores RGB. Descárgalo desde [https://invpy.com/stt/turtlecolors.py](https://invpy.com/stt/turtlecolors.py) y ejecútalo. Ajusta los tres deslizadores de rojo, verde y azul para ver el color resultante.

[<img src="https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_turtlecolors1.webp" style="width: 200px"/>](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_turtlecolors1.webp)
[<img src="https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_turtlecolors2.webp" style="width: 200px"/>](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_turtlecolors2.webp)
[<img src="https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_turtlecolors3.webp" style="width: 200px"/>](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_turtlecolors3.webp)
[<img src="https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_turtlecolors4.webp" style="width: 200px"/>](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_turtlecolors4.webp)

---

<a name="Raising-and-Lowering-the-Pen" />

## Levantar y bajar la pluma

Imagina que la tortuga lleva una pluma en la boca. Cuando la pluma está tocando el “papel” (la pantalla), dibuja una línea al moverse. Si la pluma está levantada, la tortuga se mueve sin dibujar.

* `pluma_abajo()` baja la pluma y permite dibujar al avanzar.
* `pluma_arriba()` levanta la pluma para moverse sin dibujar.

Por defecto, la pluma está baja al iniciar el programa.

Hagamos un programa que dibuje líneas punteadas. Crea un archivo nuevo y guárdalo como *lineas\_punteadas.py*. Escribe:

```python
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
```

Este programa traza doce líneas punteadas en direcciones aleatorias. Cada línea punteada combina `pluma_abajo()`/`pluma_arriba()` con movimientos de 10 pasos.

[<img src="https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_dashed_lines1.webp" style="width: 400px"/>](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_dashed_lines1.webp)
[<img src="https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_dashed_lines2.webp" style="width: 400px"/>](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_dashed_lines2.webp)

<div style="page-break-after: always;"></div>

<a name="Square-Spirals-Examples" />

## Ejemplos de espirales cuadrados

Hagamos un programa que dibuje una espiral cuadrada. Crea un archivo nuevo en tu editor de código. Guárdalo como *espiral.py*. Introduce el siguiente código Python:

```python
# espiral.py
from tortuga import *

velocidad('mas rapida')
for i in range(300):
    adelante(i)   # Usa la variable i como argumento de la función.
    izquierda(91)
ocultar_tortuga()
hecho()
```

Al ejecutar este programa, se ve así:

[<img src="https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_spiral.webp" style="width: 400px"/>](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_spiral.webp)

En nuestros programas anteriores con bucles `for`, habíamos ignorado la variable `i`. Pero en este programa, la usamos en la instrucción `adelante(i)`.

En este bucle, la variable `i` toma el valor `0` en la primera iteración, de modo que `adelante(i)` equivale a `adelante(0)`. La siguiente vez, `i` vale `1` y `adelante(i)` equivale a `adelante(1)`. El bucle sigue aumentando `i`, haciendo que la tortuga dibuje líneas cada vez más largas.

La variable `i` recorre los valores desde `0` hasta `299` (porque escribimos `for i in range(300):`). Por tanto, en la última iteración, `i` vale `299`.

Esto hace que nuestro programa sea equivalente a:

```python
from tortuga import *

velocidad('mas rapida')

adelante(0)
izquierda(91)
adelante(1)
izquierda(91)
adelante(2)
izquierda(91)
adelante(3)
izquierda(91)
adelante(4)
izquierda(91)

# ... muchas más iteraciones ...

adelante(297)
izquierda(91)
adelante(298)
izquierda(91)
adelante(299)
izquierda(91)

ocultar_tortuga()
hecho()
```

¡Usar el bucle `for` nos ahorra muchísimo tecleo!

Prueba cambiar el `91` en `izquierda(91)` por otros números entre `30` y `180`, y vuelve a ejecutar el programa para ver cómo cambia la figura.

---

A continuación, creemos una espiral colorida aleatoria. Crea un archivo nuevo. Guárdalo como *espiral\_fondo\_negro.py*. Introduce:

```python
# espiral_fondo_negro.py
from tortuga import *
from random import *

colores = ['rojo', 'naranja', 'amarillo', 'azul', 'verde', 'morado']

velocidad('mas rapida')
tamano_pluma(3)
color_fondo('negro')
for i in range(300):
    color_pluma(choice(colores))
    adelante(i)
    izquierda(91)
ocultar_tortuga()
hecho()
```

Al ejecutar este programa, se ve así:

[<img src="https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_spiral_black_bg.webp" style="width: 400px"/>](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_spiral_black_bg.webp)

---

Podemos dibujar una espiral con los colores del arcoíris usando este código. Crea un archivo nuevo. Guárdalo como *espiral\_arcoiris.py*. Introduce:

```python
# espiral_arcoiris.py
from tortuga import *

velocidad('mas rapida')
tamano_pluma(3)
color_fondo('negro')

color_pluma('rojo')
for i in range(60):
    adelante(i)
    izquierda(91)

color_pluma('naranja')
for i in range(60):
    adelante(60 + i)
    izquierda(91)

color_pluma('amarillo')
for i in range(60):
    adelante(120 + i)
    izquierda(91)

color_pluma('verde')
for i in range(60):
    adelante(180 + i)
    izquierda(91)

color_pluma('azul')
for i in range(60):
    adelante(240 + i)
    izquierda(91)

color_pluma('morado')
for i in range(60):
    adelante(300 + i)
    izquierda(91)

hecho()
```

Al ejecutar este programa, se ve así:

[<img src="https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_spiral_rainbow.webp" style="width: 400px"/>](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_spiral_rainbow.webp)

<div style="page-break-after: always;"></div>

<a name="Draw-Curves-and-Circles" />

## Dibujar curvas y círculos

El módulo Tortuga solo puede dibujar líneas rectas. No puede trazar curvas ni círculos. Sin embargo, puedes dibujar líneas muy cortas para que parezca una curva. Crea un archivo nuevo en tu editor de código. Guárdalo como *ruta\_curva.py*. Introduce el siguiente código Python:

```python
# ruta_curva.py

from tortuga import *
from random import *

tasa_dibujo(4, 0)

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
```

No puedes dibujar un círculo directamente, pero sí un polígono de 360 lados que parezca un círculo. Así es como funciona la función `circulo()`. Pasa el radio (la mitad del ancho del círculo) que quieras dibujar. Crea un archivo nuevo en tu editor de código. Guárdalo como *dibujar\_circulos.py*. Introduce:

```python
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
```

Para un dibujo más complejo de círculos que se superponen, crea un archivo nuevo. Guárdalo como *dibujar\_muchos\_circulos.py*. Introduce:

```python
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
```

<div style="page-break-after: always;"></div>

<a name="Blue-Flowers-Program" />

## Programa Flores Azules

Usemos todo lo aprendido para hacer un programa de arte generativo. Este programa dibuja flores azules haciendo seis círculos en ubicaciones, tamaños, grosores de pluma y tonos de azul aleatorios. Crea un archivo nuevo. Guárdalo como *flores\_azules.py*. Introduce:

```python
# flores_azules.py
from tortuga import *
from random import *

tasa_dibujo(100, 0)

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
```

<div style="page-break-after: always;"></div>

<a name="Filled-In-Shapes" />

## Formas rellenas

Hasta ahora solo hemos dibujado líneas. También podemos crear figuras rellenas. Primero, llama a `color_relleno()` y pásale el color que quieras para el interior. Luego llama a `comenzar_rellenar()`, dibuja la forma y llama a `terminar_relleno()` para finalizar el relleno.

Crea un archivo nuevo. Guárdalo como *cuadrado\_relleno.py*. Introduce:

```python
# cuadrado_relleno.py

from tortuga import *

tamano_pluma(4)

color_relleno('azul')

comenzar_rellenar()
for i in range(4):
    adelante(200)
    izquierda(90)
terminar_relleno()

hecho()
```

Para dibujar muchos cuadrados rellenos de colores aleatorios, crea *cuadrados\_coloridos.py*:

```python
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
```

Para versiones curvas rellenas, crea *ruta\_curva\_rellena.py*:

```python
# ruta_curva_rellena.py

from tortuga import *
from random import *

tasa_dibujo(4, 0)

for i in range(50):
    # Color de relleno aleatorio:
    color_relleno((random(), random(), random()))

    # Definir un ángulo aleatorio y dibujar varias líneas cortas:
    establecer_direccion(randint(0, 360))
    comenzar_rellenar()
    for j in range(randint(200, 600)):
        adelante(1)
        izquierda(randint(-4, 4))
    origen()
    terminar_relleno()

actualizar()
hecho()
```

<div style="page-break-after: always;"></div>


<a name="For-More-Information" />

## Para más información

Este tutorial solo ha sido el comienzo de lo que puedes hacer con el módulo `turtle` de Python (a través de Tortuga). Hay muchas otras cosas que puedes aprender sobre programación con Tortuga. Consulta los siguientes enlaces para más información:

* La documentación oficial del módulo Turtle en [https://docs.python.org/3/library/turtle.html](https://docs.python.org/3/library/turtle.html)
* La lista de métodos de Tortuga en la documentación oficial en [https://docs.python.org/3/library/turtle.html#turtle-methods](https://docs.python.org/3/library/turtle.html#turtle-methods)
* Capítulo 9 de *The Recursive Book of Recursion*, con dibujos recursivos de Tortuga en [https://inventwithpython.com/recursion/chapter9.html](https://inventwithpython.com/recursion/chapter9.html)
* Capítulo 13 de *The Recursive Book of Recursion*, con un programa fractal recursivo en [https://inventwithpython.com/recursion/chapter13.html](https://inventwithpython.com/recursion/chapter13.html)
* Charla en PyCon US 2023: *The Creative Art of Algorithmic Embroidery* (Marie Roald, Yngve Mardal Moe) en [https://www.youtube.com/watch?v=OcuhrDIrblo](https://www.youtube.com/watch?v=OcuhrDIrblo)

Python también incluye el programa **turtledemo** que ofrece muchos más ejemplos. Crea un programa con este código:

```python
import turtledemo.__main__
turtledemo.__main__.main()
```

Al ejecutarlo, verás un menú para seleccionar uno de los ejemplos. Haz clic en **Start** para ejecutarlo. El código fuente aparece en el lado izquierdo de la ventana. Este es el programa de ejemplo *Peace*:

[<img src="https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_peace.webp" style="width: 400px"/>](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/orig_screenshot_peace.webp)

¡Buena suerte en tu viaje de programación!

<a name="Advanced-Turtle-Challenges" />

## Desafíos avanzados de Tortuga

Si buscas formas realmente desafiantes para tus programas de Tortuga, echa un vistazo a los dibujos de [Oscar Reutersvärd](https://en.wikipedia.org/wiki/Oscar_Reutersv%C3%A4rd) en el sitio Impossible World: [https://im-possible.info/english/library/](https://im-possible.info/english/library/). También puedes buscar en internet “Oscar Reutersvärd” para ver ejemplos de su arte.

Algunos ejemplos:

[<img src="https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/oscar1.webp" style="width: 400px"/>](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/oscar1.webp)
[<img src="https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/oscar4.webp" style="width: 400px"/>](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/oscar4.webp)

<div style="page-break-after: always;"></div>

<a name="Solutions" />

## Soluciones

*(Las soluciones a los ejercicios están disponibles al final de este tutorial.)*

<a name="Solutions" />

## Soluciones

Aquí están las soluciones a los ejercicios de práctica:

```python
# solucion_triangulo_equilatero.py
from tortuga import *
tamano_pluma(4)

derecha(60)
adelante(200)

derecha(120)
adelante(200)

derecha(120)
adelante(200)

hecho()
```

```python
# solucion_pentagono.py
from tortuga import *
tamano_pluma(4)

izquierda(72)
adelante(200)

izquierda(72)
adelante(200)

izquierda(72)
adelante(200)

izquierda(72)
adelante(200)

izquierda(72)
adelante(200)

# O puedes usar:
# for i in range(5):
#     izquierda(72)
#     adelante(200)
hecho()
```

```python
# solucion_hexagono.py
from tortuga import *
tamano_pluma(4)

for i in range(6):
    izquierda(60)
    adelante(200)

hecho()
```

```python
# solucion_octagono.py
from tortuga import *
tamano_pluma(4)

for i in range(8):
    izquierda(45)
    adelante(100)

hecho()
```

```python
# solucion_triangulo_rectangulo.py
from tortuga import *
tamano_pluma(4)

adelante(200)
derecha(90)
adelante(200)
derecha(135)
adelante(282.8)

hecho()
```

```python
# solucion_estrella.py
from tortuga import *
tamano_pluma(4)

for i in range(5):
    derecha(144)
    adelante(300)

hecho()
```

```python
# solucion_cuadrados_anidados.py
from tortuga import *
tamano_pluma(4)

longitud_linea = 100
for i in range(4):
    adelante(longitud_linea)
    izquierda(90)

longitud_linea = 150
for i in range(4):
    adelante(longitud_linea)
    izquierda(90)

longitud_linea = 200
for i in range(4):
    adelante(longitud_linea)
    izquierda(90)

longitud_linea = 250
for i in range(4):
    adelante(longitud_linea)
    izquierda(90)

longitud_linea = 300
for i in range(4):
    adelante(longitud_linea)
    izquierda(90)

# O puedes usar:
# for longitud_linea in range(100, 350, 50):
#     for i in range(4):
#         adelante(longitud_linea)
#         izquierda(90)
hecho()
```

```python
# solucion_cruz.py
from tortuga import *
tamano_pluma(4)

for i in range(4):
    adelante(100)
    derecha(90)

    adelante(100)
    derecha(90)

    adelante(100)
    izquierda(90)

hecho()
```

```python
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
```

```python
# solucion_triforce.py
from tortuga import *
tamano_pluma(4)

derecha(60)
adelante(400)

derecha(120)
adelante(400)

derecha(120)
adelante(400)

derecha(120)
adelante(200)

derecha(60)
adelante(200)

derecha(120)
adelante(200)

derecha(120)
adelante(200)

hecho()
```

```python
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
```

```python
# solucion_cruz_establecer_direccion.py
from tortuga import *
tamano_pluma(4)

# Saliente derecha:
establecer_direccion(0)
adelante(100)
establecer_direccion(270)
adelante(100)
establecer_direccion(180)
adelante(100)

# Saliente inferior:
establecer_direccion(270)
adelante(100)
establecer_direccion(180)
adelante(100)
establecer_direccion(90)
adelante(100)

# Saliente izquierda:
establecer_direccion(180)
adelante(100)
establecer_direccion(90)
adelante(100)
establecer_direccion(0)
adelante(100)

# Saliente superior:
establecer_direccion(90)
adelante(100)
establecer_direccion(0)
adelante(100)
establecer_direccion(270)
adelante(100)

hecho()
```

```python
# solucion_saludo_aleatorio.py
from tortuga import *
from random import *

tasa_dibujo(1000, 0)
pluma_arriba()
ocultar_tortuga()

for i in range(100):
    ir_a(randint(-400, 400), randint(-400, 400))
    escribir('Hello, world!', fuente=('Arial', randint(12, 48), 'normal'))

update()
hecho()
```
