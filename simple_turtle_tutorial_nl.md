

## XY Cartesische Coördinaten

Net zoals graden gebruikt worden om richting te meten, gebruiken we *XY-coördinaten* om positie aan te duiden.  
In het *cartesisch coördinatensysteem*:

- De **X-coördinaat** bepaalt hoe ver iets naar links of rechts staat.
- De **Y-coördinaat** bepaalt hoe ver iets naar boven of beneden staat.
- Samen vormen ze een positie in het venster.

---

* Het midden van het scherm heet de *oorsprong* en heeft de coördinaten `(0, 0)`.
* X wordt groter als je naar rechts gaat, en kleiner als je naar links gaat.
* Y wordt groter als je naar boven gaat, en kleiner als je naar beneden gaat.
* Een turtle links van het midden heeft een negatieve X-waarde.
* Een turtle onder het midden heeft een negatieve Y-waarde.

Hier is een voorbeelddiagram van Wikipedia:

![cartesisch](cartesian.png)

---

We maken een programma dat telkens de XY-coördinaten toont.  
Sla het op als *random_position.py*:

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

Dit programma tekent acht lijnen en schrijft op elke positie de XY-coördinaten:

![random posities](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_random_position.jpg)

---

De functies `forward()` en `backward()` bewegen relatief vanaf de huidige plek.  
Maar met `goto(x, y)` kun je de turtle naar absolute XY-coördinaten verplaatsen.

Voorbeeld: *random_goto.py*

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

Elke keer kiest de turtle willekeurige X- en Y-waarden tussen -400 en 400 en tekent een lijn naar die plek:

![random goto](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_random_goto1.jpg)

Elke uitvoering levert een ander resultaat op.



## Home, Clear, Reset, Undo

De turtle tekent lijnen terwijl hij beweegt, maar er zijn functies om het scherm op te ruimen:

- `home()` verplaatst de turtle terug naar het midden `(0, 0)` en zet de richting op 0 graden.  
  Dit is hetzelfde als `goto(0, 0)` en `setheading(0)`.

- `clear()` wist alle lijnen die getekend zijn, maar laat de turtle op zijn plaats.

- `reset()` wist alles én verplaatst de turtle terug naar het begin.  
  Dit is dus `clear()` en `home()` tegelijk.

- `undo()` maakt de laatste actie van de turtle ongedaan.  
  Je kunt het meerdere keren gebruiken om meerdere stappen terug te gaan.

Gebruik deze functies als je opnieuw wilt beginnen of een fout wilt herstellen in je tekening.



## Snelle Herhaling 2

Laten we herhalen wat we hebben geleerd sinds de vorige herhaling:

---

### Tekst schrijven:

```python
write('Hallo!')
write('Hallo!', font=('Arial', 48, 'normal'))
```

Met `write()` kun je tekst tekenen op de huidige locatie van de turtle.  
Gebruik het `font=` argument om lettertype, grootte en stijl aan te passen.

---

### Richting van de turtle instellen of uitlezen:

```python
setheading(90)        # Zet richting naar 90 graden (omhoog).
richting = heading()  # Geeft huidige richting als getal terug.
```

0 = rechts, 90 = omhoog, 180 = links, 270 = omlaag.  
`heading()` geeft dit als getal terug dat je kunt afdrukken of gebruiken in je code.

---

### Naar specifieke XY-coördinaten bewegen:

```python
goto(250, -100)
```

* `(0, 0)` is het midden van het scherm.
* X > 0 = rechts, X < 0 = links.
* Y > 0 = boven, Y < 0 = onder.

---

### Het scherm opruimen:

* `home()` — terug naar het midden en richting op 0 graden.
* `clear()` — wist alle tekenlijnen.
* `reset()` — wist alles én zet de turtle terug naar start.
* `undo()` — maakt de laatste actie ongedaan.



## Oefeningen 2

Schrijf programma’s die de volgende tekeningen maken.  
Gebruik de functies `goto()` en `setheading()` waar aangegeven.  
De oplossingen vind je aan het einde van deze handleiding.

---

**1. Ster-omtrek met `goto()`**

Bestandsnaam: *solution_star_outline.py*  
*Tip: gebruik alleen `goto()` en teken met deze coördinaten:  
(0, 300), (70, 95), (285, 95), (110, -35), (175, -260),  
(0, -100), (-175, -260), (-110, -35), (-285, 95), (-70, 95), en terug naar (0, 300).*

![ster omtrek](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_solution_star_outline.jpg)

---

**2. Kruis met `setheading()`**

Bestandsnaam: *solution_cross_setheading.py*  
*Tip: gebruik alleen `setheading()` om de richting te bepalen.  
Gebruik geen `left()` of `right()`. Richtingen zijn: 0, 90, 180, 270 graden.*

![kruis](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_solution_cross.jpg)

---

**3. Honderd keer “Hallo wereld!” op willekeurige plekken**

Bestandsnaam: *solution_random_hello.py*  
*Tip: gebruik `randint()` om willekeurige posities en lettergroottes (12–48) te genereren.  
Teken geen lijnen en verberg de turtle met `hideturtle()`.*

![hallo wereld](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_solution_random_hello.jpg)



## Kleuren

Je kunt de achtergrondkleur van het scherm veranderen met `bgcolor()`.  
Je kunt ook de kleur van de lijnen van de turtle veranderen met `pencolor()`.

Voorbeelden:

```python
bgcolor('yellow')        # Achtergrond wordt geel
pencolor('blue')         # Lijnkleur wordt blauw
```

Voor het programma *square_circle_86.py* geeft dit bijvoorbeeld dit resultaat:

![geel blauw](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_bgcolor_yellow.jpg)

---

### Ondersteunde kleurennamen

Enkele standaardkleurennamen zijn:

- `'black'` → `(0.0, 0.0, 0.0)`
- `'white'` → `(1.0, 1.0, 1.0)`
- `'red'` → `(1.0, 0.0, 0.0)`
- `'green'` → `(0.0, 1.0, 0.0)`
- `'blue'` → `(0.0, 0.0, 1.0)`
- `'yellow'` → `(1.0, 1.0, 0.0)`
- `'orange'` → `(1.0, 0.5, 0.0)`
- `'purple'` → `(0.5, 0.0, 0.5)`
- `'cyan'` → `(0.0, 1.0, 1.0)`
- `'magenta'` → `(1.0, 0.0, 1.0)`
- `'gray'` → `(0.5, 0.5, 0.5)`
- `'brown'` → `(0.6, 0.4, 0.2)`
- `'pink'` → `(1.0, 0.75, 0.8)`
- `'violet'` → `(0.56, 0.0, 1.0)`

---

### RGB-kleuren

Je kunt ook RGB-waarden gebruiken: een *tuple* van drie getallen tussen `0.0` en `1.0`:

- `(1.0, 0.0, 0.0)` → volledig rood
- `(0.0, 1.0, 0.0)` → volledig groen
- `(0.0, 0.0, 1.0)` → volledig blauw
- `(1.0, 1.0, 1.0)` → wit (alles maximaal)
- `(0.0, 0.0, 0.0)` → zwart (alles nul)

Voorbeeld:  
`fillcolor((0.5, 0.2, 0.8))` maakt een paarse kleur.

Gebruik RGB als je zelf kleuren wilt mengen.

---

### Hulpmiddel: turtlecolors

Je kunt de kleuren verkennen met de app *turtlecolors*.  
Download de code via:  
[https://raw.githubusercontent.com/asweigart/turtlecolors/refs/heads/main/src/turtlecolors/__init__.py](https://raw.githubusercontent.com/asweigart/turtlecolors/refs/heads/main/src/turtlecolors/__init__.py)

Sla het op als *turtlecolors.py* en voer het uit.  
Je kunt de schuifregelaars gebruiken om kleuren te mengen.

Voorbeeld van de app:

![turtlecolors](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_turtlecolors2.jpg)



## Pen Opheffen en Neerlaten

Stel je voor dat de turtle een pen vasthoudt.  
Wanneer de pen het oppervlak raakt, tekent de turtle een lijn terwijl hij beweegt.  
Als de pen omhoog is, beweegt de turtle zonder te tekenen.

Gebruik deze functies:

- `pendown()` — de pen raakt het papier: tekenen is ingeschakeld.
- `penup()` — de pen is omhoog: de turtle tekent niet.

Standaard staat de pen *omlaag*, dus tekenen is aan.

---

Laten we een programma maken dat stippellijnen tekent.  
Maak een bestand genaamd *dashed_lines.py*:

```python
# dashed_lines.py
from turtle import *
from random import *

pensize(4)
speed('fastest')

for i in range(12):
    # Kies een willekeurige richting:
    setheading(randint(0, 360))

    # Teken een gestippelde lijn in die richting:
    for j in range(6):
        pendown()
        forward(10)  # Teken een segment
        penup()
        forward(10)  # Beweeg zonder te tekenen
    
    # Teken het laatste segment:
    pendown()
    forward(10)

done()
```

---

Elke iteratie van de buitenste lus tekent een nieuwe stippellijn.  
De binnenste lus maakt de streepjes (10 stappen tekenen, 10 stappen niet tekenen).

Omdat dit programma willekeurige richtingen gebruikt, is het resultaat steeds anders:

![stippellijn 1](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_dashed1.jpg)  
![stippellijn 2](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_dashed2.jpg)



## Voorbeelden van Vierkante Spiralen

Laten we een programma maken dat een vierkante spiraal tekent.  
Sla dit op als *spiral.py*:

```python
# spiral.py
from turtle import *

speed('fastest')
for i in range(300):
    forward(i)  # Gebruik de i-waarde als lengte
    left(91)
hideturtle()
done()
```

---

Wanneer je dit uitvoert, zie je een spiraal:

![spiraal](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_spiral.jpg)

In dit programma gebruiken we de `i`-variabele uit de `for`-lus als stapgrootte.  
De turtle tekent telkens langere lijnen en draait elke keer 91°.

---

Probeer eens `left(91)` te vervangen door andere waarden tussen `30` en `180`.  
Elk getal maakt een andere tekening.

---

### Kleurrijke spiraal

Sla dit op als *spiral_black_bg.py*:

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

Elke lijn heeft een willekeurige kleur.  
Het resultaat ziet er kleurrijk uit:

![kleurenspiraal](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_spiral_black_bg.jpg)

---

### Regenboogspiraal

Sla dit op als *spiral_rainbow.py*:

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

Elke kleur gebruikt een andere `for`-lus en vergroot de lijnlengte telkens.

![regenboogspiraal](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_spiral_rainbow.jpg)



## Zeer Snel Tekenen

Als `speed('fastest')` nog te langzaam is, gebruik dan `tracer(100, 0)`.  
Dat laat de turtle 100 lijnen tekenen voordat het scherm wordt bijgewerkt.

Vergeet niet `update()` aan te roepen aan het einde van je tekening,  
anders wordt het resultaat misschien niet getoond.

---

### Voorbeeld: 1.000 lijnen tekenen

Maak een bestand *random_tracer.py*:

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

Dit programma tekent 1.000 lijnen naar willekeurige locaties.

![random tracer](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_random_tracer.jpg)

Als je `tracer(100, 0)` gebruikt in plaats van `10`,  
gaat het tekenen veel sneller.

Met `tracer(1000, 0)` is het resultaat bijna direct klaar.

> Let op: hogere waarden dan `1000` versnellen het meestal niet meer,  
> omdat je computer dan al zo snel mogelijk tekent.

Vergeet `update()` niet, anders zie je mogelijk niets.



## Interactief Tekenen

We kunnen interactieve kunst maken door functies aan te roepen wanneer de gebruiker klikt.  
Gebruik het sleutelwoord `def` om je eigen functie te maken.  
Met `getscreen().onclick()` kun je een functie aanroepen bij een muisklik.

---

### Voorbeeld: klik om vierkant te tekenen

Bestandsnaam: *click_square.py*

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

getscreen().onclick(draw_square)  # Geen haakjes bij draw_square!
done()
```

Klik in het turtle-venster om vierkanten te tekenen op de klikpositie:

![click square](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_click_square.jpg)

---

### Voorbeeld: klik om spiraal te tekenen

Bestandsnaam: *click_spiral.py*

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

Elke klik tekent een andere spiraal:

![click spiral](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_click_spiral.jpg)

---

### Voorbeeld: klik om roos te tekenen

Bestandsnaam: *click_rose.py*

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

Klik om een veld met rozen te tekenen!

![click rose](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_click_rose.jpg)



## Gebogen Lijnen en Cirkels Tekenen

De turtle-module kan alleen rechte lijnen tekenen.  
Maar door veel korte lijnen te combineren, lijkt het alsof er een boog of cirkel ontstaat.

---

### Voorbeeld: kromme lijnen maken

Sla dit op als *curve_path.py*:

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

Elke gebogen lijn bestaat uit honderden korte rechte lijntjes:

![curve path](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_curve_path.jpg)

---

### De `circle()` functie

De `turtle`-module heeft een ingebouwde functie `circle(radius)`  
die een "cirkel" tekent door een 360-hoekige vorm te maken.

Sla dit op als *draw_circles.py*:

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

Resultaat:

![cirkelreeks](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_draw_circles.jpg)

---

### Veel overlappende cirkels

Sla dit op als *draw_many_circles.py*:

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

![veel cirkels](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_draw_many_circles.jpg)

Je kunt dit aanpassen door andere hoeken, kleuren, of afstanden te proberen.  
Voeg eventueel `tracer(1000, 0)` toe voor snelheid en `update()` op het einde.



## Blauwe Bloemen Programma

Laten we alles combineren wat we geleerd hebben om *generatieve kunst* te maken.

Dit programma tekent willekeurige bloemvormen met blauwe cirkels.

Sla het op als *blue_flowers.py*:

```python
from turtle import *
from random import *

tracer(100, 0)

for n in range(50):
    # Ga naar een willekeurige plek:
    penup()
    x = randint(-300, 300)
    y = randint(-300, 300)
    goto(x, y)
    pendown()

    # Kies een willekeurige blauwe kleur:
    pencolor((0, 0, random()))

    # Kies een willekeurige lijndikte:
    pensize(randint(1, 5))

    # Kies een willekeurige grootte voor de cirkels:
    circle_size = randint(10, 40)

    # Teken zes cirkels:
    for i in range(6):
        circle(circle_size)
        left(60)

update()
done()
```

Resultaat:

![blue flowers](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_blue_flowers.jpg)

---

Door het gebruik van willekeurige kleuren, locatie, grootte en dikte  
krijg je bij elke uitvoer een unieke compositie!



## Ingevulde Figuren

Tot nu toe hebben we alleen lijnen getekend.  
Maar je kunt ook vormen invullen met kleur.

Gebruik deze functies:

- `fillcolor(kleur)` — stel de opvulkleur in.
- `begin_fill()` — begin het invullen.
- `end_fill()` — beëindig en vul de vorm.

---

### Voorbeeld: gevulde vierkant

Bestandsnaam: *filled_square.py*

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

Resultaat:

![filled square](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_filled_square.jpg)

---

### Voorbeeld: willekeurige vierkanten

Bestandsnaam: *colorful_squares.py*

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

Resultaat:

![colorful squares](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_colorful_squares.jpg)

---

### Voorbeeld: ingevulde kromme vormen

Bestandsnaam: *curve_path_filled.py*

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

Resultaat:

![curve path filled](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_curve_path_filled.jpg)



## Voor Meer Informatie

Deze handleiding is slechts een begin.  
Met de turtle-module kun je nog veel meer doen!

Bekijk deze bronnen voor meer uitleg en inspiratie:

---

- [Officiële documentatie van de Turtle-module](https://docs.python.org/3/library/turtle.html)

- [Lijst van turtle-functies](https://docs.python.org/3/library/turtle.html#turtle-methods)

- [Hoofdstuk 9 van *The Recursive Book of Recursion* — recursieve turtle-tekeningen](https://inventwithpython.com/recursion/chapter9.html)

- [Hoofdstuk 13 van *The Recursive Book of Recursion* — fractale figuren](https://inventwithpython.com/recursion/chapter13.html)

---

Python wordt geleverd met een extra programma genaamd `turtledemo`  
dat voorbeeldtekeningen toont.

Sla dit korte script op als *run_turtledemo.py*:

```python
import turtledemo.__main__
turtledemo.__main__.main()
```

Na uitvoeren verschijnt een venster met voorbeelden zoals deze:

![peace demo](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_peace.jpg)

Klik op een programma in de lijst, en dan op **Start** om het uit te voeren.  
De broncode verschijnt aan de linkerkant.

---

Veel plezier met programmeren!



## Geavanceerde Turtle-uitdagingen

Ben je op zoek naar ingewikkelde vormen om na te tekenen met turtle-programma's?  
Bekijk dan de werken van [Oscar Reutersvärd](https://nl.wikipedia.org/wiki/Oscar_Reutersv%C3%A4rd),  
de "vader van de onmogelijke figuren".

Op [Impossible World](https://im-possible.info/english/library/index.html)  
vind je honderden voorbeelden van optische illusies en geometrische kunst.

Of zoek via een zoekmachine op:

> "Oscar Reutersvärd" met afbeeldingsresultaten

---

Voorbeelden:

![oscar1](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/oscar1.jpg)  
![oscar2](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/oscar2.jpg)  
![oscar3](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/oscar3.jpg)  
![oscar4](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/oscar4.jpg)

---

Daag jezelf uit om dit soort figuren te tekenen met de turtle-module!  
Gebruik loops, functies, coördinaten en richtingen om het op te bouwen.



## Oplossingen

Hieronder vind je de voorbeeldoplossingen van de oefenopgaven.

---

### *solution_equilateral_triangle.py*

```python
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

### *solution_pentagon.py*

```python
from turtle import *
pensize(4)

for i in range(5):
    left(72)
    forward(200)

done()
```

---

### *solution_hexagon.py*

```python
from turtle import *
pensize(4)

for i in range(6):
    left(60)
    forward(200)

done()
```

---

### *solution_octagon.py*

```python
from turtle import *
pensize(4)

for i in range(8):
    left(45)
    forward(100)

done()
```

---

### *solution_right_triangle.py*

```python
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

### *solution_star.py*

```python
from turtle import *
pensize(4)

for i in range(5):
    right(144)
    forward(300)

done()
```

---

### *solution_nested_squares.py*

```python
from turtle import *
pensize(4)

for line_length in range(100, 350, 50):
    for i in range(4):
        forward(line_length)
        left(90)

done()
```

---

### *solution_cross.py*

```python
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

### *solution_cube.py*

```python
from turtle import *
pensize(4)

# Voorste vierkant
for i in range(4):
    forward(200)
    right(90)

# Diagonale verbindingen
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

### *solution_star_outline.py*

```python
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

### *solution_cross_setheading.py*

```python
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

### *solution_random_hello.py*

```python
from turtle import *
from random import *

tracer(1000, 0)
penup()
hideturtle()

for i in range(100):
    goto(randint(-400, 400), randint(-400, 400))
    write('Hallo wereld!', font=('Arial', randint(12, 48), 'normal'))

update()
done()
```

