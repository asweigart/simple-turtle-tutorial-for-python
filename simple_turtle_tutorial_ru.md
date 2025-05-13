# Простой учебник по Turtle для Python



## Введение

Графика Turtle — это простой способ изучать программирование с помощью рисования.  
Вы управляете виртуальной ручкой, называемой **черепашкой** (*turtle*), чтобы она перемещалась по экрану и рисовала линии.  
Вы создаёте изображения на компьютере, изучая при этом основы программирования.  
Можно представить себе черепашку как [игру Etch A Sketch](https://ru.wikipedia.org/wiki/Etch_A_Sketch), управляемую программой на Python.

В этом учебнике объясняется, как использовать модуль `turtle` в Python.  
Он не обучает самому языку Python. Полезно уже знать такие понятия, как переменные, операторы, циклы, функции, импорт модулей и случайные числа.  
Бесплатная книга [«Автоматизация рутинных задач с помощью Python»](https://automatetheboringstuff.com/) отлично подойдёт новичкам.

Перед началом убедитесь, что у вас установлен **интерпретатор Python** с сайта [python.org](https://python.org).  
Также понадобится редактор кода, например IDLE, [Mu](https://codewith.mu/) или [Visual Studio Code](https://code.visualstudio.com/download).

Программы, написанные на Python, называются Python-программами. Не все из них используют графику turtle.  
Но в этом руководстве мы будем называть такие программы «Turtle-программами».

Даже если вы ещё не умеете программировать, вы можете просто копировать код из этого руководства в редактор и запускать его.

## Содержание

1. [Введение](#Введение)
1. [Рисуем квадрат](#Рисуем-квадрат)
1. [Рисуем меньший квадрат](#Рисуем-меньший-квадрат)
1. [Частые ошибки и сообщения об ошибках](#Частые-ошибки-и-сообщения-об-ошибках)
1. [Рисуем квадрат с помощью цикла](#Рисуем-квадрат-с-помощью-цикла)
1. [Краткий обзор 1](#Краткий-обзор-1)
1. [Практические упражнения 1](#Практические-упражнения-1)
1. [Пишем текст в окне Turtle](#Пишем-текст-в-окне-Turtle)
1. [Углы](#Углы)
1. [Декартовы координаты XY](#Декартовы-координаты-XY)
1. [Домой, очистить, сбросить, отменить](#Домой-очистить-сбросить-отменить)
1. [Краткий обзор 2](#Краткий-обзор-2)
1. [Практические упражнения 2](#Практические-упражнения-2)
1. [Цвета](#Цвета)
1. [Поднять и опустить ручку](#Поднять-и-опустить-ручку)
1. [Примеры квадратных спиралей](#Примеры-квадратных-спиралей)
1. [Очень быстрое рисование](#Очень-быстрое-рисование)
1. [Интерактивное рисование](#Интерактивное-рисование)
1. [Рисуем кривые и окружности](#Рисуем-кривые-и-окружности)
1. [Программа «Синие цветы»](#Программа-Синие-цветы)
1. [Закрашенные фигуры](#Закрашенные-фигуры)
1. [Дополнительные ресурсы](#Дополнительные-ресурсы)
1. [Сложные задания с Turtle](#Сложные-задания-с-Turtle)
1. [Решения](#Решения)
1. [Связь с автором](#Связь-с-автором)



## Рисуем квадрат

Создадим программу, которая рисует квадрат.  
Откройте редактор кода, создайте новый файл и сохраните его как *first_square.py*.  
Введите следующий код на Python:

```python
# first_square.py

# Это комментарий.
# Всё, что идёт после символа # — это «комментарий» и не выполняется как код.
# Используйте комментарии для заметок и пояснений в коде.

from turtle import *

pensize(4)  # Сделать линии толще обычного.

forward(200)  # Переместить черепашку вперёд на 200 шагов.
left(90)  # Повернуть черепашку влево на 90 градусов.

# Повторить движение вперёд и поворот ещё три раза:
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)

done()  # Без этой строки окно Turtle может сразу закрыться.
```

Сохраните файл и запустите программу.  
(Если вы используете IDLE, нажмите клавишу **F5** или выберите меню **Run > Run Module**.  
В Visual Studio Code — **Run > Run Without Debugging**.)

При запуске откроется новое окно, которое мы будем называть *окном Turtle*. В нём появится изображение:

[<img src="https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_first_square.jpg" style="width: 400px"/>](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_first_square.jpg)

В окне черепашка выглядит как треугольник.  
Представьте, что она рисует линию ручкой, пока движется.

Программа делает следующее:

1. Движется вперёд на 200 шагов (черепашка смотрит вправо).
2. Поворачивает влево на 90°.
3. Движется вперёд на 200 шагов.
4. Поворачивает влево на 90°.
5. Повторяет ещё два раза — в итоге получается квадрат.

Теперь подробнее разберём каждую инструкцию:

```python
# first_square.py

# Это комментарий.
# Всё, что идёт после символа # — это «комментарий» и не выполняется как код.
```

Строки, начинающиеся с `#`, — это **комментарии**. Python их игнорирует.  
Пустые строки также пропускаются.

```python
from turtle import *
```

**Обязательно** пишите эту строку в начале каждой turtle-программы.  
Она подключает модуль `turtle`, чтобы можно было использовать такие функции, как `pensize()`, `forward()`, `left()` и `done()`.

Если забыть эту строку, программа выдаст ошибку `NameError`.

```python
pensize(4)  # Сделать линии толще.
```

`pensize` — это функция, и `pensize(4)` — это её вызов.  
Функции могут принимать аргументы, как здесь — число 4.

Мы всегда будем писать имя функции с `()` — например, `pensize()`, чтобы показать, что это функция.

```python
forward(200)  # Переместить черепашку вперёд на 200 шагов.
left(90)  # Повернуть черепашку влево на 90 градусов.
```

`forward(200)` перемещает черепашку вперёд по текущему направлению и рисует линию.  
`left(90)` поворачивает черепашку влево (против часовой стрелки) на 90 градусов.

Существует также функция `right()`, если нужно повернуть по часовой стрелке.

```python
done()  # Без этой строки окно Turtle может сразу закрыться.
```

Функция `done()` говорит Python подождать, пока пользователь закроет окно.  
Без неё окно может закрыться сразу после завершения программы.

Даже если у функции нет аргументов, как `done`, скобки `()` писать всё равно нужно.

---

В этом уроке вы познакомились с функциями `forward()`, `left()` и `done()` из модуля `turtle`.  
С их помощью можно рисовать фигуры и картинки!

Давайте теперь напишем ещё несколько простых программ.



## Рисуем меньший квадрат

Теперь нарисуем квадрат меньшего размера.  
Вместо `forward(200)` используем `forward(25)`.  
Создайте новый файл и сохраните его как *square_smaller.py*:

```python
# square_smaller.py
from turtle import *

pensize(4)
forward(25)  # Теперь черепашка движется только на 25 шагов.
left(90)
forward(25)
left(90)
forward(25)
left(90)
forward(25)
left(90)
done()
```

Программа рисует меньший квадрат, потому что каждая сторона короче:

[<img src="https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_square_smaller.jpg" style="width: 400px"/>](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_square_smaller.jpg)

**Важно:** необходимо изменить **все четыре** строки с `forward(200)` на `forward(25)`.  
Если вы забудете хотя бы одну, квадрат получится неправильным.

Вот пример с ошибкой — программа *square_smaller_bug.py*:

```python
# square_smaller_bug.py
from turtle import *

pensize(4)
forward(25)
left(90)
forward(25)
left(90)
forward(200)  # Ой! Здесь забыли изменить!
left(90)
forward(25)
left(90)
done()
```

Программа содержит **ошибку (баг)** и рисует неправильную фигуру:

[<img src="https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_square_smaller_bug.jpg" style="width: 400px"/>](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_square_smaller_bug.jpg)

Ошибаться — это нормально! Просто внимательно проверьте код.  
Компьютер делает **ровно то**, что вы ему сказали — не больше и не меньше.  
Важно убедиться, что ваши **намерения** совпадают с тем, что **делает программа**.



## Частые ошибки и сообщения об ошибках

При написании программ вы можете столкнуться с ошибками.  
Обратите внимание на **текст ошибки** и **номер строки**, где она произошла.

Вот самые распространённые ошибки и причины их появления:

- **`ModuleNotFoundError: No module named 'trutle'`** — опечатка в названии модуля. Например, `from trutle import *` вместо `turtle`.

- **`NameError: name 'froward' is not defined`** — опечатка в имени функции или переменной. Например, `froward(100)` вместо `forward(100)`.

- **`TypeError: forward() missing 1 required positional argument: 'distance'`** — вызов функции без нужного аргумента. Например, `forward()` без числа.

- **`TypeError: left() takes 1 positional argument but 2 were given`** — передано слишком много аргументов. Например, `left(90, 45)`.

- **`IndentationError: unexpected indent`** — слишком много пробелов в начале строки.

- **`IndentationError: expected an indented block after 'for' statement on line 5`** — отсутствует отступ после строки с циклом, например: `for i in range(4):`.

- **`SyntaxError: invalid syntax`** — общая ошибка синтаксиса. Python не может понять, что вы имели в виду.

Иногда ошибка указывается на одной строке,  
но **причина** ошибки может быть в предыдущей строке!

Внимательно читайте сообщение об ошибке.  
Оно подсказывает, **в чём проблема** и **где искать**.



## Рисуем квадрат с помощью цикла

Теперь нарисуем квадрат, используя **цикл `for`**.  
Создайте новый файл и сохраните его как *square_for_loop.py*.  
Введите следующий код:

```python
# square_for_loop.py
from turtle import *

pensize(4)

# Вложенные строки выполняются 4 раза:
for i in range(4):  
    forward(200)
    left(90)
done()
```

Строки внутри цикла `for i in range(4):` выполняются **4 раза**.  
Это означает, что черепашка пройдёт 4 стороны квадрата.

Убедитесь, что отступ **точно 4 пробела** перед строками `forward(...)` и `left(...)`.  
Если отступы неправильные, появится ошибка `IndentationError`.

Пример отступов, помеченных точками:

```
for i in range(4):  
....forward(200)
....left(90)
done()
```

Программа нарисует квадрат:

![square](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_first_square.jpg)

---

Теперь изменим угол поворота.  
Сохраните новую версию программы как *square_for_loop_86.py*:

```python
# square_for_loop_86.py
from turtle import *

pensize(4)

for i in range(4):  
    forward(200)
    left(86)  # Повернуть на 86°, а не 90
done()
```

Это создаст немного «искривлённый» квадрат:

![86](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_square_for_loop_86.jpg)

---

Теперь увеличим количество повторений до **50**, чтобы получилась окружность.

Сохраните файл как *square_circle_86.py*:

```python
# square_circle_86.py
from turtle import *

pensize(4)
speed('fastest')

for i in range(50):  # Повторить 50 раз
    forward(200)
    left(86)
hideturtle()
done()
```

Здесь мы также добавили `speed('fastest')`, чтобы ускорить рисование.

`hideturtle()` скрывает треугольник-курсор в конце.

Результат:

![circle](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_square_circle_86.jpg)

---

Можно сделать рисунок **случайным**, используя `randint()` из модуля `random`.

Сохраните файл как *square_random.py*:

```python
# square_random.py
from turtle import *
from random import *

pensize(4)
speed('fastest')

for i in range(50):
    forward(200)
    # Случайный поворот от 80 до 100 градусов:
    left(randint(80, 100))
hideturtle()
done()
```

Каждый запуск даёт **разный результат**:

![random1](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_square_random1.jpg)  
![random2](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_square_random2.jpg)

Функция `randint(80, 100)` возвращает случайное целое число от 80 до 100.

Такие программы создают **генеративное искусство** —  
вы пишете код, а компьютер создаёт изображения!



## Краткий обзор 1

Вот что мы узнали до сих пор:

- Комментарии начинаются с символа `#`:

```python
# Это комментарий
```

Комментарии не влияют на выполнение кода.

---

- Подключаем модуль `turtle`:

```python
from turtle import *
```

---

- Черепашка может двигаться:

```python
forward(100)     # Вперёд на 100 шагов
backward(100)    # Назад на 100 шагов
```

---

- Можно поворачивать:

```python
left(90)      # Влево на 90°
right(45)     # Вправо на 45°
```

Отрицательные числа поворачивают в противоположную сторону.

---

- Устанавливаем толщину линии:

```python
pensize(4)
```

---

- Чтобы окно не закрывалось сразу:

```python
done()
```

---

- Переменные хранят значения:

```python
line_length = 25
forward(line_length)
```

---

- Используем цикл `for`:

```python
for i in range(4):
    forward(200)
    left(90)
```

---

- Ускоряем черепашку:

```python
speed('fastest')
```

---

- Скрываем черепашку:

```python
hideturtle()
```

---

- Случайные числа:

```python
from random import *
left(randint(80, 100))
```

---

## Практические упражнения 1

Попробуйте нарисовать эти фигуры.  
Подсказки даны в описаниях. Решения — в конце учебника.

---

**Равносторонний треугольник**  
Все стороны — 200 шагов, повороты: сначала 60°, затем 120°:

![треугольник](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_solution_equilateral_triangle.jpg)

---

**Пятиугольник**  
5 сторон по 200 шагов. Каждый поворот — 72°:

![пятиугольник](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_solution_pentagon.jpg)

---

**Шестиугольник**  
6 сторон по 200 шагов. Повороты — 60°:

![шестиугольник](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_solution_hexagon.jpg)

---

**Восьмиугольник**  
8 сторон по 100 шагов. Повороты — 45°:

![восьмиугольник](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_solution_octagon.jpg)

---

**Прямоугольный треугольник**  
Стороны: 200, 200 и 282.8 шагов. Повороты: 90° и 135°:

![прямой треугольник](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_solution_right_triangle.jpg)

---

**Звезда**  
5 линий по 200 шагов. Повороты — 144°:

![звезда](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_solution_star.jpg)

---

**Вложенные квадраты**  
Квадраты со сторонами: 100, 150, 200, 250, 300. Можно использовать вложенные циклы:

![вложенные квадраты](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_solution_nested_squares.jpg)

---

**Крест**  
Все линии по 100 шагов. Повороты 90°, включая left и right:

![крест](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_solution_cross.jpg)

---

**Куб**  
Стороны — по 100 шагов. Повороты — 45°, 90°, 135°. Можно накладывать линии:

![куб](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_solution_cube.jpg)

---

**Трифорс**  
Треугольники с поворотами 60° и 120°. Некоторые перемещения — на 50 шагов:

![трифорс](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_solution_triforce.jpg)



## Пишем текст в окне Turtle

Черепашка может писать **текст** в окне, как и рисовать линии.  
Для этого используется функция `write()` — она принимает строку текста и пишет её на экране в текущем положении черепашки.

Создайте файл *write_hello.py* и введите следующий код:

```python
# write_hello.py
from turtle import *

write('Hello, world!')
forward(80)
right(45)
forward(50)
write('123456789', font=('Arial', 48, 'normal'))
right(45)
forward(30)
write('oOoOoOoOoOo')
done()
```

---

Когда вы запускаете эту программу, черепашка пишет текст в окне:

![write](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_write_hello.jpg)

---

Левая нижняя точка текста будет в том месте, где находится черепашка при вызове `write()`.

Пример:

```python
write('Hello, world!')
```

Черепашка пишет текст, затем перемещается вперёд и снова пишет.

---

### Шрифт и стиль

Вы можете указать параметры шрифта с помощью аргумента `font=`:

```python
write('123456789', font=('Arial', 48, 'normal'))
```

Значение `font=` — это кортеж из 3 элементов:

1. Название шрифта: `'Arial'`
2. Размер шрифта: `48` (число, не строка!)
3. Стиль шрифта: `'normal'`, `'bold'`, `'italic'`, `'underline'`, или комбинация (например, `'bold italic'`)

---

Если `font=` не указан, по умолчанию используется `('Arial', 8, 'normal')`.

Убедитесь, что указанный шрифт установлен на вашем компьютере.



## Углы

В Turtle-программах расстояние измеряется в **шагах**.  
Например, `forward(100)` перемещает черепашку на 100 шагов.

Но направление и повороты можно измерять в **градусах**.

---

### Представьте вид сверху

Представьте, что вы смотрите сверху вниз на черепашку.

- Если она поворачивает **вправо** — это **по часовой стрелке**
- Если она поворачивает **влево** — это **против часовой стрелки**

---

### Углы поворота

- **Полный круг** — это 360°
- Поворот на 180° меняет направление на противоположное
- Поворот на 90° — это «обычный» прямой угол
- Четыре поворота по 90° возвращают черепашку в исходное направление

```python
left(90)
left(90)
left(90)
left(90)  # Теперь черепашка смотрит туда же, куда изначально
```

---

### Направление (heading)

Python отслеживает **направление**, куда «смотрит» черепашка:

- 0° — вправо
- 90° — вверх
- 180° — влево
- 270° — вниз
- 360° = 0° — тоже вправо

---

Функция `heading()` возвращает текущее направление черепашки.

---

Пример. Создайте файл *turtle_directions.py*:

```python
# turtle_directions.py
from turtle import *

for i in range(24):
    forward(100)  # Движение вперёд
    write(heading(), font=('Arial', 20, 'normal'))  # Написать текущее направление
    backward(100)  # Вернуться в центр
    left(15)  # Повернуть на 15°
done()
```

![directions](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_turtle_directions.jpg)

---

Функция `left()` и `right()` поворачивают **относительно текущего направления**.

Но функция `setheading()` устанавливает **абсолютное направление**.

---

Пример. Файл *setheading_turtle.py*:

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

---

Черепашка поворачивает случайно, пишет текущее направление,  
а потом `setheading(45)` устанавливает направление на 45° (вверх-вправо).  
На экране отображается `"45.0"`.

Каждый запуск будет начинаться по-разному, но потом всегда направляется под 45°:

![setheading](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_setheading_turtle2.jpg)



## Декартовы координаты XY

Как градусы описывают направление, так **координаты XY** описывают положение черепашки на экране.

---

В системе координат:

- **X** — как далеко черепашка находится **влево или вправо**
- **Y** — как далеко она **вверх или вниз**

---

### Правила координат:

- Центр окна — это **начало координат**: `(0, 0)`
- X увеличивается вправо и уменьшается влево
- Y увеличивается вверх и уменьшается вниз
- Левая половина окна — отрицательный X
- Правая половина — положительный X
- Нижняя часть окна — отрицательный Y
- Верхняя часть — положительный Y

---

Вот пример из Википедии:

![Координаты](cartesian.png)

---

### position()

Функция `position()` возвращает координаты текущего положения черепашки.

Создайте файл *random_position.py*:

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

![random_position](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_random_position.jpg)

---

### goto(x, y)

Функция `goto()` перемещает черепашку в заданную точку (X, Y).

---

Пример. Файл *random_goto.py*:

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

---

Каждый раз координаты случайны. Результаты могут выглядеть так:

![goto1](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_random_goto1.jpg)  
![goto2](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_random_goto2.jpg)

---

Перемещение с помощью `goto(x, y)` не зависит от текущего направления.



## Домой, очистить, сбросить, отменить

Когда черепашка движется, она оставляет за собой линии.  
С помощью следующих функций можно **очистить** или **отменить** действия:

---

### home()

Возвращает черепашку в центр окна — координаты `(0, 0)` —  
и устанавливает направление на 0° (вправо).

То же самое, что:

```python
goto(0, 0)
setheading(0)
```

---

### clear()

Удаляет **все нарисованные линии**, но оставляет черепашку на месте.

---

### reset()

Удаляет всё (как `clear()`),  
и возвращает черепашку в центр (как `home()`).

---

### undo()

Отменяет **последнее действие** черепашки (например, линию).

Можно вызывать `undo()` несколько раз подряд, чтобы поэтапно отменить рисование.

---

Пример использования всех команд:

```python
from turtle import *

forward(100)
left(90)
forward(100)
undo()
undo()
clear()
reset()
done()
```



## Краткий обзор 2

Вот что мы узнали в последних разделах:

---

```python
write('Hello, world!')
write('Привет!', font=('Arial', 48, 'bold italic'))
```

- Функция `write()` выводит текст в текущем положении черепашки.
- Аргумент `font=` задаёт шрифт, размер и стиль (например, `'bold'`, `'italic'`).

---

```python
setheading(90)
current_heading = heading()
```

- `setheading(угол)` задаёт **направление** черепашки в градусах.
- `heading()` возвращает текущий угол направления.

---

```python
goto(250, -100)
```

- `goto(x, y)` перемещает черепашку в указанные координаты.
- Центр окна: `(0, 0)` — это **начало координат**.
- X увеличивается вправо, уменьшается влево.
- Y увеличивается вверх, уменьшается вниз.

---

```python
home()
clear()
reset()
undo()
```

- `home()` возвращает в центр и направляет вправо.
- `clear()` удаляет всё, не меняя положение.
- `reset()` = `clear()` + `home()`.
- `undo()` отменяет последнее действие.



## Практические упражнения 2

Попробуйте написать программы, которые рисуют следующие изображения.  
Подсказки даны ниже. Решения находятся в конце учебника.

---

### Звезда по координатам

Создайте программу *solution_star_outline.py*.  
Используйте только `goto()` для рисования.  
Координаты точек:

```
(0, 300), (70, 95), (285, 95), (110, -35), (175, -260),
(0, -100), (-175, -260), (-110, -35), (-285, 95), (-70, 95), (0, 300)
```

![звезда координаты](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_solution_star_outline.jpg)

---

### Крест с setheading()

Создайте *solution_cross_setheading.py*.  
Используйте только `setheading()`, а не `left()` или `right()`.

Подсказка: все линии по 100 шагов, направления — 0, 90, 180, 270.

![крест](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_solution_cross.jpg)

---

### Случайный текст

Создайте *solution_random_hello.py*.  
Черепашка должна написать «Hello, world!» 100 раз в случайных местах.  
Шрифт — случайного размера от 12 до 48.  
Не рисовать линии, скрыть черепашку.

![hello](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_solution_random_hello.jpg)



## Цвета

Вы можете изменить:

- **Цвет фона окна** с помощью `bgcolor()`
- **Цвет линий черепашки** с помощью `pencolor()`

---

### Примеры стандартных цветов:

```python
bgcolor('black')      # чёрный
pencolor('blue')      # синий
pencolor('orange')    # оранжевый
pencolor('purple')    # фиолетовый
```

---

Вот таблица соответствий цветов и их RGB-значений:

| Цвет       | RGB                     |
|------------|--------------------------|
| `'black'`  | `(0.0, 0.0, 0.0)`        |
| `'white'`  | `(1.0, 1.0, 1.0)`        |
| `'red'`    | `(1.0, 0.0, 0.0)`        |
| `'green'`  | `(0.0, 1.0, 0.0)`        |
| `'blue'`   | `(0.0, 0.0, 1.0)`        |
| `'yellow'` | `(1.0, 1.0, 0.0)`        |
| `'cyan'`   | `(0.0, 1.0, 1.0)`        |
| `'pink'`   | `(1.0, 0.75, 0.8)`       |
| `'gray'`   | `(0.5, 0.5, 0.5)`        |
| `'violet'` | `(0.56, 0.0, 1.0)`       |

---

Цвета можно задавать как **текстовые строки** или **кортежи RGB**.

---

### Пример

Изменим фон и цвет линий в *square_circle_86.py*:

```python
bgcolor('yellow')
pencolor('blue')
```

Результат:

![yellow_bg](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_bgcolor_yellow.jpg)

---

### RGB цвета

Формат RGB использует **красный**, **зелёный** и **синий** компоненты —  
значения от `0.0` (отсутствие) до `1.0` (максимум).

- `(1.0, 0.0, 0.0)` — чисто красный
- `(0.0, 0.0, 0.0)` — чёрный
- `(1.0, 1.0, 1.0)` — белый
- `(1.0, 1.0, 0.0)` — жёлтый

---

Чтобы подобрать цвет, используйте приложение **turtlecolors**.

Скопируйте содержимое:  
[https://raw.githubusercontent.com/asweigart/turtlecolors/refs/heads/main/src/turtlecolors/__init__.py](https://raw.githubusercontent.com/asweigart/turtlecolors/refs/heads/main/src/turtlecolors/__init__.py)  
в файл *turtlecolors.py* и запустите.

Вы увидите окно с ползунками RGB и полученным цветом.

---

Пример:

![turtlecolors](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_turtlecolors1.jpg)



## Поднятие и опускание пера

Представьте, что черепашка держит ручку.  
Когда ручка **прижата к земле**, она рисует.  
Когда ручка **поднята**, черепашка движется, но **не оставляет следа**.

---

Используйте следующие функции:

```python
pendown()   # опустить перо (включить рисование)
penup()     # поднять перо (отключить рисование)
```

---

Черепашка по умолчанию начинает с **опущенным** пером.

---

### Пример: пунктирные линии

Создайте файл *dashed_lines.py*:

```python
# dashed_lines.py
from turtle import *
from random import *

pensize(4)
speed('fastest')

for i in range(12):
    setheading(randint(0, 360))  # случайное направление

    for j in range(6):  # нарисовать 6 штрихов
        pendown()
        forward(10)
        penup()
        forward(10)

    pendown()
    forward(10)  # последний штрих

done()
```

---

Каждый запуск будет разным:

![dashed1](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_dashed1.jpg)  
![dashed2](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_dashed2.jpg)

---

Такой приём можно использовать для пунктирных, прерывистых и составных линий.



## Примеры квадратных спиралей

Создадим программу, которая рисует квадратную спираль.  
Создайте файл *spiral.py* и введите следующий код:

```python
# spiral.py
from turtle import *

speed('fastest')
for i in range(300):
    forward(i)  # перемещение на i шагов
    left(91)
hideturtle()
done()
```

---

Результат:

![spiral](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_spiral.jpg)

---

Здесь переменная `i` увеличивается от 0 до 299.  
Каждая итерация делает линию длиннее, создавая спираль.

---

Теперь добавим случайный цвет каждой линии.

Создайте *spiral_black_bg.py*:

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

---

![spiral color](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_spiral_black_bg.jpg)

---

Теперь нарисуем **радугу**.  
Создайте *spiral_rainbow.py*:

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

---

Результат:

![rainbow spiral](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_spiral_rainbow.jpg)

---

Каждый цвет рисуется своим циклом, начиная с определённой длины.



## Очень быстрое рисование

Иногда `speed('fastest')` недостаточно.  
Можно использовать `tracer()` и `update()` для **очень быстрого** рисования.

---

### tracer(n, delay)

- `tracer(n, 0)` — обновлять экран **каждые n шагов**
- Чем больше `n`, тем быстрее работает программа

---

### update()

После вызова `tracer()`, экран **не обновляется автоматически**.  
Вы должны вызвать `update()`, когда всё нарисовано.

---

Пример: создадим *random_tracer.py*:

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

При `tracer(10, 0)` рисование занимает несколько секунд.

При `tracer(1000, 0)` — почти мгновенно.

---

Если в окне ничего не видно, вы, возможно, забыли вызвать `update()`.

---

### Когда использовать

- При рисовании **тысяч линий**
- При генеративном искусстве
- При отладке программ с большим количеством рисования



## Интерактивное рисование

С помощью Python можно создавать **интерактивные рисунки**.

Функция `getscreen().onclick()` позволяет вызывать вашу функцию при **щелчке мышью**.

---

### Пример: квадраты по клику

Создайте *click_square.py*:

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

getscreen().onclick(draw_square)  # без скобок!
done()
```

---

Щелкая в разных местах окна, вы будете рисовать квадраты:

![click square](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_click_square.jpg)

---

### Пример: спирали по клику

Создайте *click_spiral.py*:

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

После нескольких щелчков вы получите:

![click spiral](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_click_spiral.jpg)

---

### Пример: красные розы

Создайте *click_rose.py*:

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
        pencolor((random(), 0, 0))  # оттенок красного
        pensize(randint(2, 5))
        forward(i)
        left(randint(50, 70))
    update()

bgcolor('black')
getscreen().onclick(draw_rose)

done()
```

---

Результат:

![roses](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_click_rose.jpg)

---

Теперь вы можете создавать генеративное искусство по щелчку мышью!



## Рисуем дуги и круги

Модуль turtle не может рисовать настоящие кривые,  
но можно создать **иллюзию кривизны**, рисуя **много маленьких отрезков**.

---

### Пример: изогнутые линии

Создайте файл *curve_path.py*:

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

---

Результат:

![curves](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_curve_path.jpg)

---

Кривая — это просто **много маленьких прямых**, повернутых под разными углами.

---

### Круги

В turtle есть функция `circle(radius)`, которая рисует **многоугольник с 360 сторонами**,  
что выглядит как круг.

---

Создайте файл *draw_circles.py*:

```python
# draw_circles.py
from turtle import *

speed('fastest')

setheading(0)  # вверх
for i in range(20):
    circle(i * 10)

setheading(180)  # вниз
for i in range(20):
    circle(i * 10)

done()
```

---

![draw_circles](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_draw_circles.jpg)

---

Когда черепашка смотрит вправо (`0`), круг рисуется вверх.  
Когда влево (`180`) — вниз.

---

`circle(i * 10)` рисует круги с радиусом `0`, `10`, `20`, ..., `190`.

---

### Много кругов

Создайте *draw_many_circles.py*:

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

---

Результат:

![draw_many_circles](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_draw_many_circles.jpg)

---

Измените параметры и наблюдайте, как меняется рисунок.  
При необходимости замените `speed('fastest')` на `tracer(1000, 0)` и добавьте `update()`.



## Программа «Синие цветы»

Давайте создадим программу генеративного искусства:  
она рисует синие цветы из шести кругов случайного размера, цвета и толщины пера.

---

Создайте файл *blue_flowers.py*:

```python
from turtle import *
from random import *

tracer(100, 0)

for n in range(50):
    # Переместиться в случайную точку:
    penup()
    x = randint(-300, 300)
    y = randint(-300, 300)
    goto(x, y)
    pendown()

    # Случайный синий цвет:
    pencolor((0, 0, random()))

    # Случайная толщина:
    pensize(randint(1, 5))

    # Случайный радиус:
    circle_size = randint(10, 40)

    # Нарисовать 6 кругов:
    for i in range(6):
        circle(circle_size)
        left(60)

update()
done()
```

---

Результат:

![blue flowers](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_blue_flowers.jpg)

---

Каждый запуск даёт уникальный узор из «цветов» в синей гамме.

Это и есть генеративное искусство — вы создаёте **программу, которая создаёт рисунки**.



## Закрашенные фигуры

До сих пор мы рисовали только линии.  
Но черепашка также может рисовать **залитые фигуры**.

---

### Как закрасить фигуру

1. Установите цвет заливки с помощью `fillcolor()`
2. Вызовите `begin_fill()`
3. Нарисуйте форму
4. Вызовите `end_fill()` для завершения заливки

---

### Пример: закрашенный квадрат

Создайте файл *filled_square.py*:

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

---

Результат:

![filled_square](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_filled_square.jpg)

---

### Пример: случайные квадраты

Создайте *colorful_squares.py*:

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

---

Результат:

![colorful_squares](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_colorful_squares.jpg)

---

### Пример: цветные изогнутые формы

Создайте *curve_path_filled.py*:

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

---

Результат:

![curve filled](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_curve_path_filled.jpg)

---

Функции `begin_fill()` и `end_fill()` работают с **любой формой**,  
не обязательно с прямыми углами.



## Дополнительная информация

В этом учебнике мы рассмотрели основы модуля `turtle` в Python.  
Вот где можно узнать больше:

---

### Документация

- [Официальная документация модуля turtle (на английском)](https://docs.python.org/3/library/turtle.html)
- [Список всех функций turtle](https://docs.python.org/3/library/turtle.html#turtle-methods)

---

### Рекурсивные рисунки

- [Глава 9 из книги *The Recursive Book of Recursion*](https://inventwithpython.com/recursion/chapter9.html)  
  Примеры рекурсивного рисования черепашкой
- [Глава 13 из той же книги](https://inventwithpython.com/recursion/chapter13.html)  
  Фракталы и рекурсия

---

### Программа turtledemo

Python поставляется с встроенной демонстрационной программой **turtledemo**.

Создайте файл со следующим кодом:

```python
import turtledemo.__main__
turtledemo.__main__.main()
```

---

После запуска появится окно с меню.  
Выберите одну из демонстраций и нажмите **Start**.

![peace demo](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_peace.jpg)

---

Слева вы увидите исходный код примера — вы можете изучать, как он работает.

---

Желаю удачи в вашем путешествии по программированию!



## Сложные черепашьи задачи

Если вы ищете более сложные рисунки для рисования программой,  
вдохновитесь работами **Оскара Рейтерсварда**.

---

Оскар Рейтерсвард — шведский художник, известный своими невозможными фигурами.  
Его работы можно найти на сайте [Impossible World](https://im-possible.info/english/library/index.html)  
или через [поиск изображений по имени](https://duckduckgo.com/?q=Oscar+Reutersv%C3%A4rd&iax=images&ia=images)

---

Вот примеры таких рисунков:

![oscar1](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/oscar1.jpg)  
![oscar2](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/oscar2.jpg)  
![oscar3](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/oscar3.jpg)  
![oscar4](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/oscar4.jpg)

---

Попробуйте повторить эти фигуры с помощью turtle-программирования!



## Решения упражнений

Вот решения к практическим заданиям:

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

for line_length in range(100, 350, 50):
    for i in range(4):
        forward(line_length)
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

for i in range(4):
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
right(120)
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
goto(70, 95)
goto(285, 95)
goto(110, -35)
goto(175, -260)
goto(0, -100)
goto(-175, -260)
goto(-110, -35)
goto(-285, 95)
goto(-70, 95)
goto(0, 300)

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
    write('Hello, world!', font=('Arial', randint(12, 48), 'normal'))

update()
done()
```

