---
title: Ein Einfaches Turtle-Tutorial für das Modul turtle.py von Python
author: Al Sweigart
language: de
---

<meta charset="UTF-8">

<!-- TODO: HTML- und PDF-Versionen in allen Sprachen erstellen.
Teil hinzufügen, der erklärt, wie man unter allen Betriebssystemen Screenshots macht?
Hochauflösende Screenshots für Druckausgaben aufbewahren.

Mögliche Titel:
Turtorial: Lerne Programmieren mit Turtle-Grafiken in Python
-->

# Ein Einfaches Turtle-Tutorial für das Modul turtle.py von Python

*Ein Programmierhandbuch für Schüler:innen und deren Eltern, Lehrer:innen und Kursleiter:innen.*

**Dieses Dokument befindet sich noch in Arbeit und ist nicht vollständig.**

Dies ist ein Tutorial zur Turtle-Programmierung von Al Sweigart, Autor von *Automate the Boring Stuff with Python* und anderen Büchern. Alle seine Bücher können kostenlos online gelesen werden unter [https://inventwithpython.com](https://inventwithpython.com)

## Inhaltsverzeichnis

1. [Einleitung](#einleitung)
1. [Ein Quadrat Zeichnen](#ein-quadrat-zeichnen)
1. [Ein Kleineres Quadrat Zeichnen](#ein-kleineres-quadrat-zeichnen)
1. [Häufige Fehler und Fehlermeldungen](#häufige-fehler-und-fehlermeldungen)
1. [Ein Quadrat mit einer Schleife Zeichnen](#ein-quadrat-mit-einer-schleife-zeichnen)
1. [Kurze Wiederholung 1](#kurze-wiederholung-1)
1. [Übungsaufgaben 1](#übungsaufgaben-1)
1. [Text im Turtle-Fenster Schreiben](#text-im-turtle-fenster-schreiben)
1. [Winkel](#winkel)
1. [XY-Koordinatensystem](#xy-koordinatensystem)
1. [Home, Löschen, Zurücksetzen, Rückgängig](#home-löschen-zurücksetzen-rückgängig)
1. [Kurze Wiederholung 2](#kurze-wiederholung-2)
1. [Übungsaufgaben 2](#übungsaufgaben-2)
1. [Farben](#farben)
1. [Stift Heben und Senken](#stift-heben-und-senken)
1. [Quadratische Spiralen Beispiele](#quadratische-spiralen-beispiele)
1. [Sehr Schnelles Zeichnen](#sehr-schnelles-zeichnen)
1. [Interaktives Zeichnen](#interaktives-zeichnen)
1. [Kurven und Kreise Zeichnen](#kurven-und-kreise-zeichnen)
1. [Blumenprogramm](#blumenprogramm)
1. [Gefüllte Formen](#gefüllte-formen)
1. [Weitere Informationen](#weitere-informationen)
1. [Fortgeschrittene Turtle-Herausforderungen](#fortgeschrittene-turtle-herausforderungen)
1. [Lösungen](#lösungen)
1. [Autor kontaktieren](#autor-kontaktieren)


## Einleitung

Turtle-Grafik ist eine einfache Möglichkeit, Programmieren durch Zeichnen mit Code zu lernen. Du steuerst einen virtuellen Stift, die sogenannte *Turtle*, die sich auf dem Bildschirm bewegt und dabei Linien zeichnet. Mit dem Computer Bilder zu erstellen ist eine unterhaltsame Art, Programmieren zu lernen. Man kann sich die Turtle wie ein [Etch A Sketch](https://de.wikipedia.org/wiki/Etch_A_Sketch) vorstellen, das über ein Python-Programm gesteuert wird.

Diese Anleitung erklärt, wie man das `turtle`-Modul von Python verwendet. Sie lehrt jedoch nicht die Programmiersprache Python selbst. Es ist hilfreich, wenn du bereits ein paar grundlegende Konzepte kennst, wie Variablen, Operatoren, Schleifen, Funktionen, das Importieren von Modulen und Zufallszahlen. Das kostenlose Buch [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/) ist ein guter Einstieg für komplette Anfänger:innen.

Bevor du loslegst, musst du den *Python-Interpreter* von [python.org](https://python.org) herunterladen und installieren – das ist die Software, die Python-Code ausführt. Du brauchst auch einen Code-Editor, wie IDLE, [Mu](https://codewith.mu/) oder [Visual Studio Code](https://code.visualstudio.com/download).

Programme, die in Python geschrieben sind, nennt man Python-Programme. Nicht alle Python-Programme nutzen Turtle-Grafik. In diesem Handbuch nennen wir Programme, die das `turtle`-Modul verwenden, "Turtle-Programme".

Auch wenn du noch nicht programmieren kannst, kannst du den Beispielcode einfach in deinen Editor kopieren und ausführen.



## Ein Quadrat Zeichnen

Lass uns ein Programm schreiben, das ein Quadrat zeichnet. Erstelle eine neue Datei in deinem Code-Editor. Speichere sie unter dem Namen *first_square.py*. Gib folgenden Python-Code ein:

```python
# first_square.py

# Das ist ein Kommentar.
# Alles nach dem # ist ein "Kommentar" und wird nicht als Code ausgeführt.
# Verwende Kommentare, um dir Notizen zu deinem Code zu machen.

from turtle import *

pensize(4)  # Mache die Linien dicker als normal.

forward(200)  # Bewege die Turtle 200 Schritte vorwärts.
left(90)      # Drehe die Turtle um 90 Grad nach links.

# Noch drei Mal vorwärts bewegen und drehen:
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)

done()  # Ohne diese Zeile würde sich das Turtle-Fenster sofort schließen.
```

Speichere die Datei und führe das Programm aus. (In IDLE kannst du **F5** drücken oder **Run > Run Module** aus dem Menü wählen. In Visual Studio Code klickst du auf **Run > Run Without Debugging**. Bei anderen Editoren kann es anders funktionieren.)

Beim Ausführen erscheint ein neues Fenster (das *Turtle-Fenster*) mit dieser Zeichnung:

![Screenshot Quadrat](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_first_square.jpg)

Die Turtle erscheint als Dreieck. Stell dir vor, sie hält einen Stift und zeichnet beim Bewegen eine Linie. Der Code steuert ihre Bewegung:

1. Bewege dich 200 Schritte vorwärts (die Turtle blickt nach rechts).
2. Drehe dich 90 Grad nach links.
3. Wiederhole das noch dreimal.
4. Am Ende steht die Turtle wieder an der Startposition und blickt in die Ausgangsrichtung.
5. Das Fenster bleibt offen, damit du die Zeichnung betrachten kannst.

Mit diesen neun Schritten zeichnet die Turtle ein Quadrat.

Erklärung der Befehle:

```python
# first_square.py

# Das ist ein Kommentar.
# Alles nach dem # ist ein Kommentar und wird ignoriert.
```

Der Kommentar `# first_square.py` hilft nur zur Orientierung und ist für Python bedeutungslos.

Leere Zeilen werden ebenfalls ignoriert.

```python
from turtle import *
```

Du MUSST diese Zeile am Anfang jedes Turtle-Programms haben. Sie lädt das `turtle`-Modul und ermöglicht die Nutzung der Funktionen wie `pensize()`, `forward()`, `left()` und `done()`.

Wenn du sie vergisst, bekommst du einen Fehler wie `NameError: name 'forward' is not defined`.

```python
pensize(4)  # Mache die Linien dicker.
```

`pensize` ist eine Funktion, und `pensize(4)` ist ein Funktionsaufruf. Eine *Funktion* ist ein kleiner Programmblock, den du ausführen kannst. Der Wert `4` ist das *Argument* der Funktion.

Wir schreiben immer Klammern `()` hinter Funktionsnamen, um sie als Funktion kenntlich zu machen.

```python
forward(200)  # Bewege die Turtle 200 Schritte vorwärts.
left(90)      # Drehe sie 90 Grad nach links.
```

Die Turtle bewegt sich in ihrer aktuellen Blickrichtung und zeichnet eine Linie hinter sich. `left(90)` dreht sie um 90 Grad gegen den Uhrzeigersinn.

Willst du sie im Uhrzeigersinn drehen, verwende `right()`.

```python
done()  # Hält das Fenster offen.
```

Ohne `done()` würde sich das Fenster sofort wieder schließen, wenn das Programm endet. Auch wenn `done()` keine Argumente hat, müssen die Klammern `()` geschrieben werden.

Es gibt viele weitere Turtle-Funktionen. In diesem Tutorial lernst du viele davon kennen, mit denen du schöne Bilder zeichnen kannst.

Aber fangen wir mit noch ein paar einfachen Beispielen an.



## Ein Kleineres Quadrat Zeichnen

Lass uns ein kleineres Quadrat zeichnen. Dazu ändern wir `forward(200)` zu `forward(25)`.  
Erstelle eine neue Datei und speichere sie als *square_smaller.py*. Gib diesen Code ein:

```python
# square_smaller.py
from turtle import *

pensize(4)
forward(25)  # Die Turtle bewegt sich jetzt nur 25 Schritte.
left(90)
forward(25)
left(90)
forward(25)
left(90)
forward(25)
left(90)
done()
```

Wenn du das Programm ausführst, entsteht ein kleineres Quadrat, da die Linien nur 25 Schritte lang sind.

![Kleineres Quadrat](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_square_smaller.jpg)

Achte darauf, **alle vier** `forward(200)`-Befehle auf `forward(25)` zu ändern. Wenn du eine vergisst, wird das Quadrat falsch.

Hier ist ein Beispiel mit einem Fehler – *square_smaller_bug.py*:

```python
# square_smaller_bug.py
from turtle import *

pensize(4)
forward(25)
left(90)
forward(25)
left(90)
forward(200)  # Ups! Diese Zeile wurde nicht geändert!
left(90)
forward(25)
left(90)
done()
```

Dieses Programm enthält einen *Bug* und zeichnet das Quadrat falsch:

![Fehlerhaftes Quadrat](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_square_smaller_bug.jpg)

Fehler passieren! Es ist kein Problem. Du kannst sie beheben.  
Dein Computer tut genau das, was du ihm sagst. Aber es liegt an dir sicherzustellen, dass er auch das tut, **was du eigentlich willst**.  
Wenn dein Programm einen Fehler enthält, lies deinen Code sorgfältig und finde heraus, was nicht stimmt.



## Häufige Fehler und Fehlermeldungen

Wenn du Python-Code schreibst, bekommst du möglicherweise Fehlermeldungen beim Ausführen.  
Achte genau auf die Fehlermeldung – besonders auf die Zeilennummer, an der der Fehler aufgetreten ist.

Hier sind einige häufige Fehler und ihre Ursachen:

* **`ModuleNotFoundError: No module named 'trutle'`** – Tippfehler im Import. Wahrscheinlich hast du `from trutle import *` statt `turtle` geschrieben.
* **`NameError: name 'froward' is not defined`** – Tippfehler bei einem Funktions- oder Variablennamen, z. B. `froward(100)` statt `forward`.
* **`TypeError: forward() missing 1 required positional argument: 'distance'`** – Du hast `forward()` ohne Argument geschrieben, es fehlt also die Anzahl der Schritte.
* **`TypeError: left() takes 1 positional argument but 2 were given`** – Du hast `left()` mit zu vielen Argumenten aufgerufen, z. B. `left(90, 45)`. Die Funktion erwartet nur **ein** Argument.
* **`IndentationError: unexpected indent`** – Zu viele oder unpassende Leerzeichen am Zeilenanfang.
* **`IndentationError: expected an indented block after 'for' statement on line 5`** – Nach einer Schleife wie `for i in range(4):` fehlt eine eingerückte Codezeile.
* **`SyntaxError: invalid syntax`** – Allgemeiner Fehler. Python versteht deinen Code nicht. Meistens passiert das bei Tippfehlern, vergessenen Klammern oder falscher Einrückung.

💡 Wenn der Fehler laut Meldung in Zeile 5 liegt, kann es gut sein, dass der Fehler **eigentlich in Zeile 4** steckt – Python merkt es manchmal erst später.



## Ein Quadrat mit einer Variablen zeichnen

Anstatt direkt `25` in `forward(25)` zu schreiben, können wir eine *Variable* verwenden.  
Der Name der Variable ist `line_length` und sie speichert den Wert `25`.

Speichere eine neue Datei als *square_variable.py* und gib folgenden Code ein:

```python
# square_variable.py
from turtle import *

pensize(4)
line_length = 25  # Diese Variable speichert die Zahl 25.
forward(line_length)  # Die Turtle bewegt sich 25 Schritte vorwärts.
left(90)
forward(line_length)
left(90)
forward(line_length)
left(90)
forward(line_length)
left(90)
done()
```

Wenn du das Programm ausführst, zeichnet es das gleiche Quadrat wie zuvor:

![Quadrat mit Variable](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_square_smaller.jpg)

Jetzt musst du aber nur noch **eine** Stelle ändern, um die Größe des Quadrats zu verändern!  
Versuche es z. B. mit `line_length = 300` oder `line_length = 5`.



## Ein Quadrat mit einer Schleife zeichnen

Nun schreiben wir ein Programm, das ein Quadrat mit einer `for`-Schleife zeichnet.  
Speichere die Datei als *square_for_loop.py* und gib diesen Code ein:

```python
# square_for_loop.py
from turtle import *

pensize(4)

# Der eingerückte Code läuft 4 Mal:
for i in range(4):  
    forward(200)
    left(90)
done()
```

Der eingerückte Code unter `for i in range(4):` wird **vier Mal** ausgeführt.  
Achte genau auf die Einrückung! Es sollten **vier Leerzeichen** vor `forward(200)` und `left(90)` stehen.

Beispiel mit Punkten zur Veranschaulichung:

```
for i in range(4):  
....forward(200)
....left(90)
done()
```

Dieses Programm zeichnet wie zuvor ein Quadrat:

![Quadrat mit Schleife](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_first_square.jpg)

---

Nun ändern wir das Programm so, dass die Turtle sich um **86 Grad** statt 90 dreht.  
Speichere es als *square_for_loop_86.py*:

```python
# square_for_loop_86.py
from turtle import *

pensize(4)

for i in range(4):  
    forward(200)
    left(86)  # Drehe um 86 Grad statt 90.
done()
```

Das ergibt keine perfekte Ecke:

![Quadrat mit 86 Grad](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_square_for_loop_86.jpg)

---

Was passiert, wenn wir diese Schleife 50-mal statt 4-mal wiederholen?

Speichere das folgende Programm als *square_circle_86.py*:

```python
# square_circle_86.py
from turtle import *

pensize(4)
speed('fastest')

for i in range(50):  # 50 Durchläufe statt 4
    forward(200)
    left(86)
hideturtle()
done()
```

Dieses Programm zeichnet deutlich mehr und schneller.  
Wir nutzen `speed('fastest')`, damit die Turtle sich schneller bewegt.  
Die Funktion `hideturtle()` blendet den Pfeil aus.

Das sieht dann so aus:

![Kreisartige Figur mit 86 Grad](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_square_circle_86.jpg)



Nun erweitern wir unser Programm und verwenden **Zufallszahlen** für die Drehung.

Speichere die Datei als *square_random.py*:

```python
# square_random.py
from turtle import *
from random import *

pensize(4)
speed('fastest')

for i in range(50):
    forward(200)
    # Drehe dich zufällig zwischen 80 und 100 Grad:
    left(randint(80, 100))
hideturtle()
done()
```

Da das Programm `randint(80, 100)` verwendet, ist jedes Ergebnis etwas anders.

Hier sind ein paar mögliche Ausgaben:

![Beispiel 1](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_square_random1.jpg)  
![Beispiel 2](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_square_random2.jpg)  
![Beispiel 3](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_square_random3.jpg)  
![Beispiel 4](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_square_random4.jpg)

Die Zeile `from random import *` ermöglicht es, die Funktion `randint()` zu verwenden.  
Diese gibt eine zufällige **ganze Zahl** zurück, die wir direkt an die `left()`-Funktion übergeben können.

Die Zeile `left(randint(80, 100))` dreht die Turtle also jedes Mal anders.

---

Wenn wir Schleifen **und** Zufallszahlen kombinieren, entsteht sogenannte **generative Kunst**.  
Wir erschaffen nicht direkt die Kunst, sondern das **Programm**, das sie generiert.

Es gibt viele kreative Bilder, die du mit Turtle zeichnen kannst!



## Kurze Wiederholung 1

Lass uns wiederholen, welche Python-Anweisungen du bisher kennengelernt hast:

Kommentare beginnen mit dem Zeichen `#`:

```python
# Das ist ein Kommentar.
```

Alles hinter dem `#` wird ignoriert. Kommentare sind Notizen im Code – sie verändern nichts an der Ausführung.

---

Dein Programm muss das Turtle-Modul importieren:

```python
from turtle import *
```

Ohne diese Zeile funktionieren die Turtle-Funktionen nicht.

---

Es gibt Funktionen, die die Turtle bewegen:

```python
forward(100)   # Bewege die Turtle 100 Schritte vorwärts.
backward(100)  # Bewege die Turtle 100 Schritte rückwärts.
forward(-100)  # Ist das gleiche wie rückwärts.
```

---

Funktionen zum Drehen der Turtle:

```python
left(90)    # Drehe nach links (gegen den Uhrzeigersinn).
right(45)   # Drehe nach rechts (im Uhrzeigersinn).
```

Negative Zahlen drehen in die entgegengesetzte Richtung.

---

Standardmäßig zeichnet die Turtle eine dünne Linie. Mit `pensize()` kannst du sie dicker machen:

```python
pensize(4)
```

---

Am Ende deines Programms solltest du `done()` aufrufen:

```python
done()
```

Damit bleibt das Turtle-Fenster offen, bis du es schließt.

---

Du kannst Zahlen direkt übergeben oder in Variablen speichern:

```python
line_length = 25
forward(line_length)
```

---

`for`-Schleifen führen Code mehrfach aus:

```python
for i in range(4):
    forward(200)
    left(90)
```

---

Um die Turtle schneller zu machen, rufe `speed('fastest')` auf:

```python
speed('fastest')
```

---

Willst du den Pfeil (die Turtle) ausblenden, nutze:

```python
hideturtle()
```

---

Du kannst Zufallszahlen nutzen:

```python
from random import *
forward(randint(1, 100))
```

Die Funktion `randint(1, 100)` gibt eine zufällige ganze Zahl zwischen 1 und 100 zurück.



## Übungsaufgaben 1

Erstelle Programme, die die folgenden Bilder zeichnen.  
Die Lösungen findest du später im Abschnitt [Lösungen](#lösungen).  
Dein Code und deine Zeichnungen müssen nicht exakt gleich aussehen – es gibt viele Wege zum Ziel.

---

### Gleichseitiges Dreieck  
Dateiname: *solution_equilateral_triangle.py*  
*Tipp: Alle Seiten sind 200 Schritte lang. Der erste Drehwinkel beträgt 60 Grad, die weiteren 120 Grad.*

![Gleichseitiges Dreieck](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_solution_equilateral_triangle.jpg)

---

### Fünfeck  
Dateiname: *solution_pentagon.py*  
*Tipp: Alle Seiten 200 Schritte. Drehwinkel: 72 Grad.*

![Fünfeck](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_solution_pentagon.jpg)

---

### Sechseck  
Dateiname: *solution_hexagon.py*  
*Tipp: Seitenlänge 200, Drehwinkel 60 Grad.*

![Sechseck](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_solution_hexagon.jpg)

---

### Achteck  
Dateiname: *solution_octagon.py*  
*Tipp: Seitenlänge 100, Drehwinkel 45 Grad.*

![Achteck](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_solution_octagon.jpg)

---

### Rechtwinkliges Dreieck  
Dateiname: *solution_right_triangle.py*  
*Tipp: Zwei Seiten sind je 200 lang, der dritte 282.8 (nach Satz des Pythagoras). Drehwinkel: 90 und 135 Grad.*

![Rechtwinkliges Dreieck](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_solution_right_triangle.jpg)

---

### Stern  
Dateiname: *solution_star.py*  
*Tipp: Alle Linien 200 lang. Drehwinkel: 144 Grad.*

![Stern](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_solution_star.jpg)

---

### Verschachtelte Quadrate  
Dateiname: *solution_nested_squares.py*  
*Tipp: Zeichne Quadrate mit Seitenlängen 100, 150, 200, 250, 300.  
Nutze ggf. eine Schleife in einer Schleife.*

![Verschachtelte Quadrate](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_solution_nested_squares.jpg)

---

### Kreuz  
Dateiname: *solution_cross.py*  
*Tipp: Alle Linien 100 lang. Nutze sowohl `left()` als auch `right()`.*

![Kreuz](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_solution_cross.jpg)

---

### Würfel  
Dateiname: *solution_cube.py*  
*Tipp: Alle Linien 100 lang. Winkel: 45, 90 oder 135 Grad.  
Du kannst `forward()` gefolgt von `backward()` nutzen, um zurück zur Ausgangsposition zu kommen.*

![Würfel](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_solution_cube.jpg)

---

### Triforce  
Dateiname: *solution_triforce.py*  
*Tipp: Linien des äußeren Dreiecks: 100 Schritte. Winkel: 60 oder 120 Grad.  
Du kannst Linien überlagern. Manchmal ist `forward(50)` nützlich.*

![Triforce](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_solution_triforce.jpg)



## Text im Turtle-Fenster schreiben

Die Turtle kann nicht nur Linien zeichnen, sondern auch Text im Fenster schreiben.  
Die Funktion `write()` nimmt einen Text-String als Argument und schreibt ihn an die aktuelle Position der Turtle.

Speichere eine neue Datei als *write_hello.py* und gib diesen Code ein:

```python
# write_hello.py

from turtle import *

write('Hallo, Welt!')
forward(80)
right(45)
forward(50)
write('123456789', font=('Arial', 48, 'normal'))
right(45)
forward(30)
write('oOoOoOoOoOo')
done()
```

Wenn du das Programm ausführst, sieht das Fenster etwa so aus:

![Schriftbeispiel](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_write_hello.jpg)

Die linke untere Ecke des Textes ist die aktuelle Position der Turtle.  
Beispielsweise wird `write('Hallo, Welt!')` in der Mitte des Fensters geschrieben, weil die Turtle dort startet.

Danach bewegt sie sich mit `forward(80)`, `right(45)` und `forward(50)`.

Der Aufruf `write('123456789', font=('Arial', 48, 'normal'))` schreibt den Text in einer größeren Schrift.

Die `font=`-Angabe ist ein **Schlüsselwort-Argument**. Sie besteht aus drei Teilen:

- dem Namen der Schriftart (`'Arial'`)
- der Schriftgröße (z. B. `48`)
- dem Stil (`'normal'`, `'bold'`, `'italic'`, `'underline'` oder Kombinationen wie `'bold italic'`)

Wenn du `font=` weglässt, wird standardmäßig `('Arial', 8, 'normal')` verwendet.

Wichtig: Die Schriftart muss auf deinem Computer installiert sein. Die Größe **muss** eine Zahl sein (nicht `'48'`).



## Winkel

In Turtle-Programmen messen wir Entfernungen in Schritten. Zum Beispiel bewegt `forward(100)` die Turtle 100 Schritte.  
Auch Drehungen und Richtungen werden mit Zahlen – in **Grad** – angegeben.

Stell dir vor, du schaust von oben auf die Turtle.  
Wenn sie sich nach rechts dreht, bewegt sie sich **im Uhrzeigersinn**.  
Dreht sie sich nach links, bewegt sie sich **gegen den Uhrzeigersinn**.

Ein voller Kreis hat **360 Grad**.  
Wenn die Turtle sich um 180 Grad dreht, blickt sie in die entgegengesetzte Richtung.  
Vier 90-Grad-Drehungen ergeben ebenfalls eine volle Umdrehung: 90 + 90 + 90 + 90 = 360.

---

Die **Richtung**, in die die Turtle gerade zeigt, wird *heading* genannt.  
Beim Start eines Programms zeigt die Turtle **nach rechts** – das ist **0 Grad**.  
Dreht sie sich nach links, steigen die Gradzahlen:

- 0 Grad: rechts
- 90 Grad: oben
- 180 Grad: links
- 270 Grad: unten
- 360 Grad: wieder rechts (gleich wie 0 Grad)

---

Die Funktion `heading()` gibt den aktuellen Blickwinkel der Turtle zurück.

Speichere eine neue Datei als *turtle_directions.py*:

```python
# turtle_directions.py
from turtle import *

for i in range(24):
    forward(100)  # Bewege dich in aktueller Richtung.
    write(heading(), font=('Arial', 20, 'normal'))  # Schreibe den Winkel.
    backward(100)  # Gehe zurück zur Mitte.
    left(15)  # Drehe dich 15 Grad nach links.
done()
```

Das Fenster sieht so aus:

![Winkelanzeige](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_turtle_directions.jpg)

---

Die Funktionen `left()` und `right()` drehen die Turtle **relativ zur aktuellen Richtung**.  
Beispiel: Ist der aktuelle Winkel 45 Grad, dann ergibt `left(90)` eine neue Richtung von 135 Grad.

Wenn du willst, dass die Turtle **genau** in eine bestimmte Richtung schaut, nutze `setheading()`.

Speichere dazu dieses Programm als *setheading_turtle.py*:

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

Dieses Programm startet mit einer zufälligen Drehung.  
Dann schreibt es den aktuellen Winkel auf den Bildschirm und bewegt sich 200 Schritte.

Anschließend setzt `setheading(45)` die Richtung **fest** auf 45 Grad (nach oben rechts),  
egal, in welche Richtung die Turtle vorher gezeigt hat.

Hier sind Beispiele:

![Beispiel 1](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_setheading_turtle1.jpg)  
![Beispiel 2](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_setheading_turtle2.jpg)



## XY-Koordinatensystem

Neben Richtungen können wir die **Position** der Turtle auch mit Zahlen beschreiben.  
Das geschieht mit dem sogenannten **kartesischen Koordinatensystem**.

Dabei gibt es zwei Werte:

- Der **X-Wert** beschreibt, wie weit rechts oder links die Turtle ist.
- Der **Y-Wert** beschreibt, wie weit oben oder unten sie ist.

Zusammen geben **X** und **Y** die genaue Position an.

---

Ein paar Regeln:

- Die Mitte des Fensters heißt *Ursprung* und hat die Koordinaten `(0, 0)`
- Der **X-Wert** nimmt zu, wenn man nach rechts geht, und ab, wenn man nach links geht
- Der **Y-Wert** nimmt zu, wenn man nach oben geht, und ab, wenn man nach unten geht
- Turtle links vom Ursprung → negativer X-Wert
- Turtle unten im Fenster → negativer Y-Wert

Hier ist ein Bild zur Veranschaulichung:

![Koordinatensystem](cartesian.png)

---

Speichere ein Programm als *random_position.py*:

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

Ergebnis:

![Positionen anzeigen](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_random_position.jpg)

---

Die Funktionen `forward()` und `backward()` bewegen die Turtle **relativ** zur aktuellen Position.

Willst du die Turtle an eine bestimmte XY-Position setzen, verwende `goto(x, y)`.

Speichere folgendes Programm als *random_goto.py*:

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

Das ergibt eine Zeichnung wie:

![Zufällige Goto-Positionen](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_random_goto1.jpg)

Die Position wird per Zufall gewählt mit `randint(-400, 400)`.  
`goto(x, y)` setzt die Turtle direkt auf diese Koordinaten.



## Home, Clear, Reset, Undo

Die Turtle zeichnet Linien, während sie sich bewegt.  
Es gibt mehrere Funktionen, um die Zeichnung oder die Position zu verändern:

- `home()` bringt die Turtle zurück zur Mitte `(0, 0)` und richtet sie auf 0 Grad aus (nach rechts)
- `clear()` löscht alles, was die Turtle gezeichnet hat (aber nicht die Position oder Richtung)
- `reset()` kombiniert `clear()` und `home()` – also: löschen + zur Mitte zurückkehren
- `undo()` macht den letzten Schritt rückgängig (z. B. die letzte Linie)

Du kannst `undo()` mehrfach aufrufen, um mehrere Aktionen rückgängig zu machen.



## Kurze Wiederholung 2

Lass uns die neuen Anweisungen zusammenfassen:

```python
write('Hallo, Welt!')
write('Hallo, Welt!', font=('Arial', 48, 'normal'))
```

Die Funktion `write()` schreibt Text an die aktuelle Position der Turtle.  
Mit dem Argument `font=` kannst du Schriftart, Größe und Stil angeben.

---

```python
setheading(90)
richtung = heading()
```

- `setheading()` setzt die Blickrichtung der Turtle (0 = rechts, 90 = oben, 180 = links, 270 = unten)
- `heading()` gibt die aktuelle Richtung zurück

---

```python
goto(250, -100)  # Bewege die Turtle zu den Koordinaten 250, -100
```

XY-Koordinaten geben die genaue Position an.

- Ursprung = `(0, 0)`
- X nimmt nach rechts zu, nach links ab
- Y nimmt nach oben zu, nach unten ab

---

Funktionen zum Zurücksetzen oder Löschen:

- `home()` → zurück zur Mitte und Blick nach rechts
- `clear()` → löscht die Zeichnung
- `reset()` → wie `clear()` + `home()`
- `undo()` → macht letzte Aktion rückgängig



## Übungsaufgaben 2

Erstelle Programme, die die folgenden Bilder zeichnen.  
Verwende jeweils die angegebenen Hinweise und Funktionen.

---

### Sternumriss  
Dateiname: *solution_star_outline.py*  
Nur `goto()` verwenden.  
*Tipp: Koordinaten: (0, 300), (70, 95), (285, 95), (110, -35), (175, -260),
(0, -100), (-175, -260), (-110, -35), (-285, 95), (-70, 95), (0, 300)*

![Sternumriss](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_solution_star_outline.jpg)

---

### Kreuz mit `setheading()`  
Dateiname: *solution_cross_setheading.py*  
Kein `left()` oder `right()` verwenden, nur `setheading()`.  
*Tipp: Linien 100 Schritte. Blickrichtungen: 0, 90, 180, 270 Grad.*

![Kreuz mit setheading](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_solution_cross.jpg)

---

### Zufällige Grüße  
Dateiname: *solution_random_hello.py*  
Schreibe 100-mal „Hallo, Welt!“ an zufällige Stellen im Fenster.  
Die Schriftgröße soll zufällig zwischen 12 und 48 liegen.  
Keine Linien zeichnen und die Turtle verstecken.

![Zufällige Grüße](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_solution_random_hello.jpg)



## Farben

Du kannst die Hintergrundfarbe des Fensters mit `bgcolor()` ändern.  
Verwende dazu Farbnamen als Text (z. B. `'red'`) oder RGB-Werte.

Beispiele für Farb-Namen und ihre RGB-Werte:

- `'black'` = `(0.0, 0.0, 0.0)`
- `'blue'` = `(0.0, 0.0, 1.0)`
- `'brown'` = `(0.6, 0.4, 0.2)`
- `'orange'` = `(1.0, 0.5, 0.0)`
- `'gray'` = `(0.5, 0.5, 0.5)`
- `'green'` = `(0.0, 1.0, 0.0)`
- `'purple'` = `(0.5, 0.0, 0.5)`
- `'violet'` = `(0.56, 0.0, 1.0)`
- `'pink'` = `(1.0, 0.75, 0.8)`
- `'yellow'` = `(1.0, 1.0, 0.0)`
- `'white'` = `(1.0, 1.0, 1.0)`
- `'red'` = `(1.0, 0.0, 0.0)`
- `'magenta'` = `(1.0, 0.0, 1.0)`
- `'cyan'` = `(0.0, 1.0, 1.0)`

---

Um die Stiftfarbe (Linienfarbe) zu ändern, verwende `pencolor()`.

Beispiel:

```python
bgcolor('yellow')
pencolor('blue')
```

Dies ergibt einen gelben Hintergrund und blaue Linien – wie hier:

![bgcolor('yellow'), pencolor('blue')](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_bgcolor_yellow.jpg)

---

### RGB-Werte

Farben können auch mit drei Werten erstellt werden: **Rot**, **Grün** und **Blau**.

Jeder Wert ist zwischen `0.0` (kein Anteil) und `1.0` (maximal).

Beispiele:

- `(1.0, 0.0, 0.0)` → Rot
- `(0.0, 1.0, 0.0)` → Grün
- `(0.0, 0.0, 1.0)` → Blau
- `(1.0, 1.0, 0.0)` → Gelb (Rot + Grün)
- `(1.0, 1.0, 1.0)` → Weiß
- `(0.0, 0.0, 0.0)` → Schwarz

Dunklere Farben: kleinere Werte  
Hellere Farben: größere Werte

---

### Farbe selbst anpassen

Nutze das Hilfsprogramm **turtlecolors**:  
Kopiere den Code von  
[https://raw.githubusercontent.com/asweigart/turtlecolors/refs/heads/main/src/turtlecolors/__init__.py](https://raw.githubusercontent.com/asweigart/turtlecolors/refs/heads/main/src/turtlecolors/__init__.py)  
in eine Datei namens `turtlecolors.py` und führe das Programm aus.

Du kannst die Schieberegler für Rot, Grün und Blau bewegen, um neue Farben zu erstellen.

So sieht das Programm aus:

![turtlecolors Beispiel](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_turtlecolors1.jpg)



## Stift anheben und absenken

Stell dir vor, die Turtle hält einen Stift im Mund.  
Wenn der Stift **unten ist**, wird beim Bewegen eine Linie gezeichnet.  
Wenn der Stift **angehoben ist**, bewegt sich die Turtle **ohne zu zeichnen**.

Nutze `pendown()` (Stift senken) und `penup()` (Stift heben), um zu steuern, ob gezeichnet wird.

---

### Beispiel: gestrichelte Linien

Speichere das folgende Programm als *dashed_lines.py*:

```python
# dashed_lines.py
from turtle import *
from random import *

pensize(4)
speed('fastest')

for i in range(12):
    # In zufällige Richtung drehen:
    setheading(randint(0, 360))

    # Eine gestrichelte Linie in dieser Richtung zeichnen:
    for j in range(6):
        pendown()
        forward(10)  # Linie zeichnen
        penup()
        forward(10)  # Lücke lassen
    
    # Letztes Stück zeichnen:
    pendown()
    forward(10)

done()
```

Das äußere `for` wiederholt den Vorgang 12-mal für 12 Striche.  
Im inneren `for` wird jedes Mal 10 Schritte gezeichnet und 10 Schritte ausgelassen.

Beispiele für das Ergebnis:

![Gestrichelte Linien 1](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_dashed1.jpg)  
![Gestrichelte Linien 2](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_dashed2.jpg)



## Quadratische Spiralen

Lass uns ein Programm schreiben, das eine quadratische Spirale zeichnet.  
Speichere eine neue Datei als *spiral.py*:

```python
# spiral.py
from turtle import *

speed('fastest')
for i in range(300):
    forward(i)  # Die Variable i bestimmt die Linienlänge
    left(91)
hideturtle()
done()
```

Das Ergebnis:

![Quadratische Spirale](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_spiral.jpg)

Hier verwenden wir zum ersten Mal die Schleifenvariable `i` tatsächlich in `forward(i)`.

Im ersten Schleifendurchlauf ist `i = 0`, dann `i = 1`, dann `i = 2` usw., bis `i = 299`.  
Dadurch wird jede Linie ein bisschen länger als die vorherige.

---

### Zahlen verändern das Muster

Wenn du `left(91)` z. B. auf `left(88)` oder `left(93)` änderst, ändert sich das Muster.

---

### Farbige Spirale mit Zufall

Speichere folgendes als *spiral_black_bg.py*:

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

Ergebnis:

![Farbige Spirale](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_spiral_black_bg.jpg)

---

### Regenbogen-Spirale

Speichere als *spiral_rainbow.py*:

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

Jede Farbe erhält ihren eigenen Schleifenblock mit zunehmender Startlänge.  
So entsteht eine große, bunte Spirale:

![Regenbogenspirale](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_spiral_rainbow.jpg)



## Sehr schnell zeichnen

Wenn `speed('fastest')` immer noch zu langsam ist, kannst du `tracer()` und `update()` verwenden.

Normalerweise zeichnet Turtle jede Linie nacheinander – das kann bei vielen Linien langsam sein.  
Mit `tracer(1000, 0)` wird nur alle 1000 Linien das Fenster aktualisiert.  
Mit `update()` kannst du dann manuell das Fenster aktualisieren.

---

### Beispiel: 1000 Linien schnell zeichnen

Speichere als *random_tracer.py*:

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

Das Ergebnis:

![random_tracer](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_random_tracer.jpg)

- Mit `tracer(10, 0)` dauert es ein paar Sekunden
- Mit `tracer(1000, 0)` fast sofort
- Noch höhere Werte (z. B. `tracer(10000, 0)`) helfen nur, wenn dein Computer schnell genug ist

**Achtung:** Wenn du `update()` vergisst, wird nichts gezeichnet!



## Interaktives Zeichnen

Mit Turtle kannst du auch interaktive Programme schreiben.  
Dazu brauchst du eigene Funktionen (mit `def`) und das Ereignis `onclick()`.

---

### Beispiel: Klick zeichnet Quadrat

Speichere *click_square.py*:

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

getscreen().onclick(draw_square)  # Achtung: KEINE () nach draw_square!
done()
```

Bei jedem Mausklick wird `draw_square()` aufgerufen.  
Die `x`- und `y`-Werte geben die Klickposition an.  
Dort wird dann ein Quadrat gezeichnet.

Beispiel:

![click_square](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_click_square.jpg)

---

### Spirale bei Klick

Speichere *click_spiral.py*:

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

Ergebnis nach mehreren Klicks:

![click_spiral](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_click_spiral.jpg)

---

### Rote Rosen auf schwarzem Hintergrund

Speichere *click_rose.py*:

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

Erzeuge mit wenigen Klicks ein Rosenbild:

![click_rose](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_click_rose.jpg)



## Kurven und Kreise zeichnen

Das Turtle-Modul kann nur **gerade Linien** zeichnen.  
Aber indem du **viele kleine Linien mit leichten Drehungen** aneinanderreihst,  
kannst du **Kurven und Kreise** erzeugen.

---

### Beispiel: Kurvige Pfade

Speichere *curve_path.py*:

```python
# curve_path.py
from turtle import *
from random import *

tracer(4, 0)

for i in range(100):  # 100 kurvige Pfade
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

Ergebnis:

![Kurvige Pfade](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_curve_path.jpg)

---

### Kreise zeichnen

Turtle hat eine `circle()`-Funktion, die intern aus 360 kurzen Linien besteht.

Speichere *draw_circles.py*:

```python
# draw_circles.py
from turtle import *

speed('fastest')

# Obere Kreise
setheading(0)
for i in range(20):
    circle(i * 10)

# Untere Kreise
setheading(180)
for i in range(20):
    circle(i * 10)

done()
```

- `setheading(0)` → Kreis **nach oben**
- `setheading(180)` → Kreis **nach unten**

Das Programm erzeugt 40 Kreise, die größer werden:

![Kreise oben/unten](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_draw_circles.jpg)

---

### Viele überlappende Kreise

Speichere *draw_many_circles.py*:

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

Das erzeugt ein schönes Blumenmuster:

![Viele Kreise](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_draw_many_circles.jpg)



## Blumen-Programm (Blue Flowers)

Jetzt erstellen wir ein Programm für **generative Kunst** – das heißt:  
Wir programmieren etwas, das Bilder **zufällig** erzeugt.

Dieses Programm zeichnet **blaue Blumen** aus sechs Kreisen,  
an zufälligen Positionen, Größen und Farben.

---

Speichere das folgende Programm:

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

Das Programm zeichnet 50 Blumen an zufälligen Orten.  
Jede Blume besteht aus sechs Kreisen.

Ergebnis:

![Blaue Blumen](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_blue_flowers.jpg)

Du kannst das Programm mehrmals ausführen,  
um jedes Mal ein neues, zufälliges Kunstwerk zu erzeugen.



## Gefüllte Formen

Bisher haben wir nur **Linien** gezeichnet.  
Aber du kannst auch **gefüllte Formen** erstellen.

Dazu verwendest du:

1. `fillcolor('FARBE')` – setzt die Füllfarbe
2. `begin_fill()` – startet den Füllbereich
3. `...` (zeichne die Form)
4. `end_fill()` – füllt den Bereich mit der gewählten Farbe

---

### Beispiel: Gefülltes Quadrat

Speichere *filled_square.py*:

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

Ergebnis:

![Gefülltes Quadrat](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_filled_square.jpg)

---

### Zufällige bunte Quadrate

Speichere *colorful_squares.py*:

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

Das Fenster zeigt dann 100 zufällige, gefüllte Quadrate:

![Bunte Quadrate](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_colorful_squares.jpg)

---

### Gefüllte Kurven

Speichere *curve_path_filled.py*:

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

Das Ergebnis: zufällige bunte Formen:

![Gefüllte Kurven](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_curve_path_filled.jpg)



## Weitere Informationen

Dieses Tutorial zeigt dir nur den Anfang.  
Mit dem `turtle`-Modul kannst du noch viel mehr machen!

Hier findest du weiterführende Informationen:

- [Offizielle Dokumentation von turtle (Python.org)](https://docs.python.org/3/library/turtle.html)
- [Liste aller Turtle-Funktionen](https://docs.python.org/3/library/turtle.html#turtle-methods)
- [Kapitel 9 im Buch *The Recursive Book of Recursion*](https://inventwithpython.com/recursion/chapter9.html)
- [Kapitel 13 im selben Buch (Fraktale mit turtle)](https://inventwithpython.com/recursion/chapter13.html)

---

Python enthält auch ein Programm mit Beispielen namens `turtledemo`.  
Erstelle eine Datei mit folgendem Code:

```python
import turtledemo.__main__
turtledemo.__main__.main()
```

Du kannst aus dem Menü verschiedene Beispielprogramme auswählen und ausführen.  
Der Quellcode wird ebenfalls angezeigt!

Beispiel: das Peace-Symbol

![turtledemo Beispiel](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_peace.jpg)

---

## Fortgeschrittene Turtle-Herausforderungen

Wenn du eine Herausforderung suchst, versuche die Kunstwerke von  
[Oscar Reutersvärd](https://de.wikipedia.org/wiki/Oscar_Reutersv%C3%A4rd) mit turtle nachzubauen.

Viele davon findest du auf der Website [Impossible World](https://im-possible.info/english/library/index.html).

Beispielbilder:

![Oscar 1](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/oscar1.jpg)  
![Oscar 2](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/oscar2.jpg)

---

## Lösungen

Die Lösungen zu den Übungsaufgaben findest du im Original-Tutorial:  
[https://inventwithpython.com/turtle](https://inventwithpython.com/turtle)

Oder direkt im GitHub-Repository:  
[https://github.com/asweigart/simple-turtle-tutorial-for-python](https://github.com/asweigart/simple-turtle-tutorial-for-python)

---

## Kontakt

Wenn du Fragen hast oder beim Übersetzen helfen möchtest,  
schreib eine E-Mail an [al@inventwithpython.com](mailto:al@inventwithpython.com)

