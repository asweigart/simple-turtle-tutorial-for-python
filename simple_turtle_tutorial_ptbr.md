
## Desenhando Muito Rápido

Se `speed('fastest')` ainda for lento, use `tracer()` e `update()` para desenhar mais rápido.

Por padrão, a tartaruga desenha e atualiza a tela linha por linha,  
mas com `tracer()` você pode dizer para atualizar a tela apenas a cada N linhas.

---

Exemplo: desenhar 1000 linhas aleatórias.

Crie *random_tracer.py*:

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

---

O `tracer(10, 0)` faz a tartaruga desenhar 10 linhas antes de atualizar a tela.  
Quanto maior o número, mais rápido será o desenho.

Tente mudar para `tracer(100)` ou `tracer(1000)` para ver a diferença de velocidade.

Se esquecer de chamar `update()` no final, o desenho pode não aparecer!

Resultado esperado:

![Desenho com tracer](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_random_tracer.jpg)

## Desenho Interativo

Você pode fazer o programa responder a cliques do mouse.  
Use `def` para definir uma função e `getscreen().onclick()` para conectá-la ao clique.

---

Crie *click_square.py*:

```python
# click_square.py
from turtle import *

speed('fastest')

def draw_square(x, y):
    penup()
    goto(x, y)
    pendown()
    for i in range(4):
        forward(100)
        left(90)

getscreen().onclick(draw_square)
done()
```

Cada clique desenha um quadrado onde você clicou.

Resultado:

![Clique desenha quadrado](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_click_square.jpg)

---

Você também pode desenhar espirais.

Crie *click_spiral.py*:

```python
# click_spiral.py
from turtle import *
from random import *

tracer(1000, 0)

def draw_spiral(x, y):
    penup()
    goto(x, y)
    pendown()

    line_length = randint(50, 200)
    turn_radius = randint(50, 70)
    for i in range(randint(50, 200)):
        forward(i)
        left(turn_radius)
    update()

getscreen().onclick(draw_spiral)
done()
```

---

Agora um buquê de rosas vermelhas!

Crie *click_rose.py*:

```python
# click_rose.py
from turtle import *
from random import *

tracer(1000, 0)

def draw_rose(x, y):
    pencolor('red')
    pensize(randint(2, 5))

    penup()
    goto(x, y)
    pendown()

    for i in range(100):
        pencolor((random(), 0, 0))
        pensize(randint(2, 5))
        forward(i)
        left(randint(50, 70))
    update()

bgcolor('black')
getscreen().onclick(draw_rose)
done()
```

Resultado:

![Rosas](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_click_rose.jpg)

## Desenhar Curvas e Círculos

O módulo `turtle` só desenha linhas retas, mas ao fazer muitas linhas curtas com pequenas curvas, criamos curvas suaves.

---

Crie *curve_path.py*:

```python
# curve_path.py
from turtle import *
from random import *

tracer(4, 0)

for i in range(100):
    penup()
    home()
    pendown()

    setheading(randint(0, 360))
    for j in range(randint(200, 600)):
        forward(1)
        left(randint(-4, 4))

update()
done()
```

Resultado:

![Curvas](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_curve_path.jpg)

---

### Função `circle()`

A função `circle()` desenha um polígono com muitos lados que parece um círculo.

Crie *draw_circles.py*:

```python
# draw_circles.py
from turtle import *

speed('fastest')

setheading(0)
for i in range(20):
    circle(i * 10)

setheading(180)
for i in range(20):
    circle(i * 10)

done()
```

Resultado:

![Círculos](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_draw_circles.jpg)

---

Crie *draw_many_circles.py*:

```python
# draw_many_circles.py
from turtle import *

speed('fastest')

for j in range(6):
    setheading(j)
    for i in range(20):
        circle(i * 10)

    setheading(j + 120)
    for i in range(20):
        circle(i * 10)

    setheading(j + 240)
    for i in range(20):
        circle(i * 10)

done()
```

Resultado:

![Muitos círculos](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_draw_many_circles.jpg)

## Programa Flores Azuis

Vamos criar arte generativa com flores azuis feitas de círculos.

Crie *blue_flowers.py*:

```python
from turtle import *
from random import *

tracer(100, 0)

for n in range(50):
    penup()
    x = randint(-300, 300)
    y = randint(-300, 300)
    goto(x, y)
    pendown()

    pencolor((0, 0, random()))
    pensize(randint(1, 5))
    circle_size = randint(10, 40)

    for i in range(6):
        circle(circle_size)
        left(60)

update()
done()
```

---

Esse programa desenha flores em locais aleatórios com tons de azul diferentes.

Resultado:

![Flores azuis](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_blue_flowers.jpg)

## Formas Preenchidas

Você pode preencher formas com cor usando `begin_fill()` e `end_fill()`.

---

Crie *filled_square.py*:

```python
# filled_square.py
from turtle import *

pensize(4)
fillcolor('blue')

begin_fill()
for i in range(4):
    forward(200)
    left(90)
end_fill()

done()
```

Resultado:

![Quadrado preenchido](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_filled_square.jpg)

---

Crie *colorful_squares.py*:

```python
# colorful_squares.py
from turtle import *
from random import *

pensize(4)
tracer(10, 0)

for i in range(100):
    penup()
    goto(randint(-400, 200), randint(-400, 200))
    pendown()

    fillcolor((random(), random(), random()))
    pencolor((random(), random(), random()))
    line_length = randint(20, 200)

    begin_fill()
    for j in range(4):
        forward(line_length)
        left(90)
    end_fill()

done()
```

Resultado:

![Quadrados coloridos](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_colorful_squares.jpg)

---

Crie *curve_path_filled.py* para curvas preenchidas:

```python
# curve_path_filled.py
from turtle import *
from random import *

tracer(4, 0)

for i in range(50):
    fillcolor((random(), random(), random()))

    setheading(randint(0, 360))
    begin_fill()
    for j in range(randint(200, 600)):
        forward(1)
        left(randint(-4, 4))
    home()
    end_fill()

update()
done()
```

Resultado:

![Curvas preenchidas](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_curve_path_filled.jpg)

## Para Saber Mais

Este tutorial cobre apenas o básico. Aqui estão alguns links para aprender mais:

- [Documentação oficial do módulo turtle](https://docs.python.org/3/library/turtle.html)
- [Lista de funções do turtle](https://docs.python.org/3/library/turtle.html#turtle-methods)
- [Capítulo 9 de The Recursive Book of Recursion](https://inventwithpython.com/recursion/chapter9.html)
- [Capítulo 13 com arte fractal recursiva](https://inventwithpython.com/recursion/chapter13.html)

---

O Python vem com o programa `turtledemo` com exemplos visuais. Crie este arquivo:

```python
import turtledemo.__main__
turtledemo.__main__.main()
```

Isso abrirá a interface de demonstração, onde você pode executar exemplos prontos como o "Peace":

![turtledemo](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_peace.jpg)

## Desafios Avançados de Turtle

Se quiser tentar desenhos desafiadores, confira as obras de Oscar Reutersvärd:

- [Página na Wikipédia](https://en.wikipedia.org/wiki/Oscar_Reutersv%C3%A4rd)
- [Coleção no site Impossible World](https://im-possible.info/english/library/index.html)
- [Imagens no DuckDuckGo](https://duckduckgo.com/?t=ffab&q=Oscar+Reutersv%C3%A4rd&iax=images&ia=images)

Exemplos:

![Oscar 1](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/oscar1.jpg)
![Oscar 2](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/oscar2.jpg)
![Oscar 3](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/oscar3.jpg)
![Oscar 4](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/oscar4.jpg)

## Soluções

Aqui estão os códigos das soluções para os exercícios:

---

```python
# solution_equilateral_triangle.py
from turtle import *
pensize(4)

right(60)
forward(200)
right(120)
forward(200)
right(120)
forward(200)

done()
```

---

```python
# solution_pentagon.py
from turtle import *
pensize(4)

for i in range(5):
    left(72)
    forward(200)

done()
```

---

```python
# solution_hexagon.py
from turtle import *
pensize(4)

for i in range(6):
    left(60)
    forward(200)

done()
```

---

```python
# solution_octagon.py
from turtle import *
pensize(4)

for i in range(8):
    left(45)
    forward(100)

done()
```

---

```python
# solution_right_triangle.py
from turtle import *
pensize(4)

forward(200)
right(90)
forward(200)
right(135)
forward(282.8)

done()
```

---

```python
# solution_star.py
from turtle import *
pensize(4)

for i in range(5):
    right(144)
    forward(300)

done()
```

---

```python
# solution_nested_squares.py
from turtle import *
pensize(4)

for length in range(100, 350, 50):
    for i in range(4):
        forward(length)
        left(90)

done()
```

---

```python
# solution_cross.py
from turtle import *
pensize(4)

for i in range(4):
    forward(100)
    right(90)
    forward(100)
    right(90)
    forward(100)
    left(90)

done()
```

---

```python
# solution_cube.py
from turtle import *
pensize(4)

for i in range(4):  # frente
    forward(200)
    right(90)

left(45)
forward(200)
right(45)
forward(200)
right(135)
forward(200)
backward(200)
left(45)
forward(200)
right(45)
forward(200)
backward(200)
right(45)
forward(200)
left(45)
forward(200)
backward(200)
right(135)
forward(200)

done()
```

---

```python
# solution_triforce.py
from turtle import *
pensize(4)

right(60)
forward(400)
right(120)
forward(400)
right(120)
forward(400)

right(120)
forward(200)
right(60)
forward(200)
right(120)
forward(200)

right(180)
forward(200)
right(60)
forward(200)

done()
```

---

```python
# solution_star_outline.py
from turtle import *
pensize(4)

penup()
goto(0, 300)
pendown()

points = [
    (70, 95), (285, 95), (110, -35), (175, -260),
    (0, -100), (-175, -260), (-110, -35), (-285, 95), (-70, 95), (0, 300)
]

for x, y in points:
    goto(x, y)

done()
```

---

```python
# solution_cross_setheading.py
from turtle import *
pensize(4)

setheading(0)
forward(100)
setheading(270)
forward(100)
setheading(180)
forward(100)

setheading(270)
forward(100)
setheading(180)
forward(100)
setheading(90)
forward(100)

setheading(180)
forward(100)
setheading(90)
forward(100)
setheading(0)
forward(100)

setheading(90)
forward(100)
setheading(0)
forward(100)
setheading(270)
forward(100)

done()
```

---

```python
# solution_random_hello.py
from turtle import *
from random import *

tracer(1000, 0)
penup()
hideturtle()

for i in range(100):
    goto(randint(-400, 400), randint(-400, 400))
    write('Olá, mundo!', font=('Arial', randint(12, 48), 'normal'))

update()
done()
```
