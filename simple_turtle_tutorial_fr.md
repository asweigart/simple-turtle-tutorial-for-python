
<meta charset="UTF-8">

<!-- TODO : Créer des versions HTML et PDF dans toutes les langues.
Ajouter une partie qui explique comment prendre des captures d'écran dans tous les systèmes d'exploitation ?
Garder des captures d'écran haute résolution pour les éditions imprimées.

Titres possibles :
Turtorial : Apprenez à programmer en Python avec Turtle Graphics
-->

# Un Tutoriel Simple pour le Module turtle.py de Python

*Un guide de programmation pour les élèves, leurs parents, enseignants et formateurs.*

**Ce document est en cours de rédaction et n'est pas encore complet.**

Ceci est un tutoriel de programmation avec Turtle écrit par Al Sweigart, auteur de *Automate the Boring Stuff with Python* et d'autres livres. Vous pouvez lire tous ses livres gratuitement en ligne sur [https://inventwithpython.com](https://inventwithpython.com)

## Table des Matières

1. [Introduction](#introduction)
1. [Dessiner un Carré](#dessiner-un-carré)
1. [Dessiner un Carré Plus Petit](#dessiner-un-carré-plus-petit)
1. [Bugs Courants et Messages d’Erreur](#bugs-courants-et-messages-derreur)
1. [Dessiner un Carré avec une Boucle](#dessiner-un-carré-avec-une-boucle)
1. [Révision Rapide 1](#révision-rapide-1)
1. [Exercices Pratiques 1](#exercices-pratiques-1)
1. [Écrire du Texte dans la Fenêtre Turtle](#écrire-du-texte-dans-la-fenêtre-turtle)
1. [Angles](#angles)
1. [Coordonnées Cartésiennes XY](#coordonnées-cartésiennes-xy)
1. [Home, Clear, Reset, Undo](#home-clear-reset-undo)
1. [Révision Rapide 2](#révision-rapide-2)
1. [Exercices Pratiques 2](#exercices-pratiques-2)
1. [Couleurs](#couleurs)
1. [Lever et Baisser le Stylo](#lever-et-baisser-le-stylo)
1. [Exemples de Spirales Carrées](#exemples-de-spirales-carrées)
1. [Dessiner Très Rapidement](#dessiner-très-rapidement)
1. [Dessin Interactif](#dessin-interactif)
1. [Dessiner des Courbes et des Cercles](#dessiner-des-courbes-et-des-cercles)
1. [Programme Fleurs Bleues](#programme-fleurs-bleues)
1. [Formes Remplies](#formes-remplies)
1. [Pour Plus d’Informations](#pour-plus-dinformations)
1. [Défis Avancés Turtle](#défis-avancés-turtle)
1. [Solutions](#solutions)
1. [Contacter l’Auteur](#contacter-lauteur)

## Introduction

La bibliothèque Turtle est une façon facile d’apprendre la programmation en dessinant avec du code. Vous programmez un stylo virtuel, appelé *la tortue*, pour qu’il se déplace sur l’écran et trace des lignes. Vous créez des images avec un ordinateur tout en apprenant à programmer. Vous pouvez imaginer la tortue comme un [Etch A Sketch](https://fr.wikipedia.org/wiki/Etch_A_Sketch) contrôlé par votre programme Python.

Ce guide explique comment utiliser le module `turtle` de Python. Il n’enseigne pas le langage Python lui-même. Il est utile de déjà connaître des concepts de base en Python comme les variables, les opérateurs, les boucles, les fonctions, l’importation de modules, et les nombres aléatoires. Le livre gratuit [Automate the Boring Stuff with Python](https://automatetheboringstuff.com/) est une bonne introduction pour les débutants.

Avant de commencer, vous devez télécharger et installer l’*interpréteur Python* (le logiciel qui exécute le code Python) depuis [python.org](https://python.org). Vous aurez aussi besoin d’un éditeur de code, comme IDLE, [Mu](https://codewith.mu/), ou [Visual Studio Code](https://code.visualstudio.com/download).

Les programmes écrits en Python sont appelés programmes Python. Tous les programmes Python n’utilisent pas Turtle. Mais dans ce guide, nous appellerons les programmes qui utilisent le module `turtle` des “programmes Turtle”.

Même si vous ne savez pas encore programmer en Python, vous pouvez tout de même copier le code de ce tutoriel dans votre éditeur de code et l’exécuter.



## Dessiner un Carré

Créons un programme qui dessine un carré. Créez un nouveau fichier dans votre éditeur de code. Enregistrez-le sous le nom *first_square.py*. Entrez le code Python suivant :

```python
# first_square.py

# Ceci est un commentaire.
# Tout ce qui suit le symbole # est un commentaire et n’est pas exécuté.
# Utilisez les commentaires pour écrire des notes dans votre code.

from turtle import *

pensize(4)  # Rendre les lignes plus épaisses que la normale.

forward(200)  # Avancer la tortue de 200 unités.
left(90)  # Tourner la tortue de 90 degrés vers la gauche.

# Avancer et tourner trois fois de plus :
forward(200)
left(90)
forward(200)
left(90)
forward(200)
left(90)

done()  # Sans cette ligne, la fenêtre Turtle peut se fermer avant que vous ne voyiez le dessin.
```

Enregistrez le fichier après avoir saisi le code. Ensuite, exécutez le programme. (Si vous utilisez IDLE, vous pouvez appuyer sur F5 ou cliquer sur **Run > Run Module**. Dans Visual Studio Code, cliquez sur **Run > Run Without Debugging**. Dans d’autres éditeurs, les étapes peuvent être différentes.)

Quand vous exécutez ce programme, une nouvelle fenêtre (que nous appellerons la *fenêtre Turtle*) s’ouvre avec le dessin suivant :

![Carré](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_first_square.jpg)

Dans la fenêtre Turtle, la tortue apparaît comme un triangle. Imaginez que la tortue tient un stylo et trace une ligne pendant qu’elle se déplace. Le code Python lui dit comment se déplacer :

1. Avancer de 200 unités (la tortue commence face à droite).
1. Tourner à gauche de 90 degrés.
1. Avancer de 200 unités.
1. Tourner à gauche de 90 degrés.
1. Avancer de 200 unités.
1. Tourner à gauche de 90 degrés.
1. Avancer de 200 unités (la tortue revient à sa position initiale).
1. Tourner à gauche de 90 degrés (elle regarde à nouveau vers la droite).
1. Le programme est terminé, mais la fenêtre Turtle reste ouverte pour que vous puissiez voir le dessin.

Avec ces neuf étapes, la tortue trace un carré.



## Dessiner un Carré Plus Petit

Créons un programme qui dessine un carré plus petit. Nous pouvons remplacer `forward(200)` par `forward(25)` pour dessiner un carré plus petit. Créez un nouveau fichier nommé *square_smaller.py* et entrez le code suivant :

```python
# square_smaller.py
from turtle import *

pensize(4)
forward(25)  # Maintenant la tortue avance seulement de 25 unités.
left(90)
forward(25)
left(90)
forward(25)
left(90)
forward(25)
left(90)
done()
```

Quand vous exécutez ce programme, il trace un carré plus petit car les lignes font seulement 25 unités de long au lieu de 200.

![Petit carré](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_square_smaller.jpg)

Souvenez-vous que vous devez remplacer les **quatre** lignes `forward(200)` par `forward(25)`, sinon le carré sera incorrect. Par exemple, voici un programme nommé *square_smaller_bug.py* qui oublie de changer une ligne :

```python
# square_smaller_bug.py
from turtle import *

pensize(4)
forward(25)
left(90)
forward(25)
left(90)
forward(200)  # Oups, on a oublié de changer cette ligne !
left(90)
forward(25)
left(90)
done()
```

Ce programme contient une *erreur* (ou *bug*) et trace un carré incorrect :

![Bug de carré](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_square_smaller_bug.jpg)

C’est normal de faire des erreurs ! Vous pouvez les corriger. L’ordinateur fait exactement ce que vous lui dites. Mais c’est à vous de vous assurer que ce que vous **voulez** qu’il fasse correspond bien à ce que vous lui **avez dit** de faire. Si votre programme contient un bug, relisez soigneusement le code et trouvez où ça ne fonctionne pas comme prévu.



## Bugs Courants et Messages d’Erreur

En écrivant du code Python, vous pouvez recevoir des messages d’erreur lorsque vous essayez d’exécuter votre programme. Faites attention à ces messages, en particulier à la ligne indiquée comme étant la cause du problème. Voici quelques messages d’erreur courants et leurs causes :

* **`ModuleNotFoundError: No module named 'trutle'`** – Vous avez fait une faute de frappe dans `from turtle import *`. Ici, le mot `trutle` est mal orthographié.
* **`NameError: name 'froward' is not defined`** – Une faute de frappe sur le nom d’une fonction ou d’une variable. Ici, `froward(100)` au lieu de `forward(100)`.
* **`TypeError: forward() missing 1 required positional argument: 'distance'`** – Vous avez oublié de passer un argument à une fonction. Par exemple, `forward()` sans préciser la distance.
* **`TypeError: left() takes 1 positional argument but 2 were given`** – Vous avez passé trop d’arguments à une fonction. Par exemple, `left(90, 45)` alors que `left()` n’attend qu’un seul argument.
* **`IndentationError: unexpected indent`** – Il y a trop d’espaces au début de la ligne.
* **`IndentationError: expected an indented block after 'for' statement on line 5`** – Vous avez oublié d’indenter les lignes après un `for`.
* **`SyntaxError: invalid syntax`** – Il y a une erreur de syntaxe générale que Python ne sait pas comment corriger. Il indique néanmoins la ligne où l’erreur est détectée. Si vous tapez du code aléatoirement, vous aurez probablement ce message.

Quand le message d’erreur indique une erreur à la ligne 5, il se peut que l’erreur réelle soit à la ligne précédente (ligne 4). L’interpréteur Python ne détecte l’erreur que lorsqu’il atteint une incohérence.



## Dessiner un Carré avec une Boucle

Écrivons un programme qui trace un carré en utilisant une boucle `for`. Créez un nouveau fichier et enregistrez-le sous le nom *square_for_loop.py*. Entrez le code Python suivant :

```python
# square_for_loop.py
from turtle import *

pensize(4)

# Les lignes indentées seront exécutées 4 fois :
for i in range(4):  
    forward(200)
    left(90)
done()
```

Le code indenté après `for i in range(4):` s’exécute quatre fois car nous passons `4` à la fonction `range()`.

Assurez-vous d’avoir **exactement quatre espaces** avant les lignes `forward(200)` et `left(90)` ! Si les indentations ne correspondent pas, vous aurez une erreur `IndentationError: unindent does not match any outer indentation level`.

Voici le même code avec des points pour montrer les espaces :

```
for i in range(4):  
....forward(200)
....left(90)
done()
```

Ce programme trace le même carré que précédemment :

![Carré boucle](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_first_square.jpg)

Notre programme appelle `pensize(4)` une seule fois, donc nous le plaçons avant la boucle.

Modifions le code pour que la tortue tourne de 86 degrés au lieu de 90. Créez un fichier *square_for_loop_86.py* :

```python
# square_for_loop_86.py
from turtle import *

pensize(4)

for i in range(4):  
    forward(200)
    left(86)  # Tourner à gauche de 86 degrés au lieu de 90.
done()
```

Cela trace une forme légèrement différente qui n’est pas un carré :

![Carré 86](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_square_for_loop_86.jpg)

Maintenant, bouclons 50 fois au lieu de 4. Créez un fichier nommé *square_circle_86.py* :

```python
# square_circle_86.py
from turtle import *

pensize(4)
speed('fastest')

for i in range(50):  # Boucle 50 fois au lieu de 4.
    forward(200)
    left(86)
hideturtle()
done()
```

Ce programme utilise beaucoup plus de dessin que les précédents, donc on appelle la fonction `speed('fastest')` pour accélérer la tortue. La valeur `'fastest'` est une *chaîne de texte* et doit être entourée de guillemets.

Les arguments valides pour `speed()` sont : `'fastest'`, `'fast'`, `'normal'`, `'slow'` et `'slowest'`.

Ce programme utilise aussi `hideturtle()` pour faire disparaître le curseur de la tortue à la fin.

Voici le résultat :

![Cercle carré 86](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_square_circle_86.jpg)

En expérimentant avec différents nombres, nous pouvons produire toutes sortes d’images. On peut aussi utiliser des nombres aléatoires pour les angles.

Créez un fichier *square_random.py* :

```python
# square_random.py
from turtle import *
from random import *

pensize(4)
speed('fastest')

for i in range(50):
    forward(200)
    # Tourner à gauche d’un nombre aléatoire entre 80 et 100 degrés :
    left(randint(80, 100))
hideturtle()
done()
```

Ce programme utilise des nombres aléatoires, donc le dessin est différent à chaque exécution :

![Random 1](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_square_random1.jpg)
![Random 2](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_square_random2.jpg)
![Random 3](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_square_random3.jpg)
![Random 4](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_square_random4.jpg)

La ligne `from random import *` permet d’utiliser la fonction `randint()`, qui renvoie un nombre entier aléatoire. Par exemple, `left(randint(80, 100))` tourne la tortue d’un nombre aléatoire de degrés entre 80 et 100.

Avec des boucles et des nombres aléatoires, [nous pouvons créer de l’art génératif](https://duckduckgo.com/?t=ffab&q=generative+art&iax=images&ia=images). Nous ne dessinons pas l’art directement, mais nous écrivons les programmes qui le font.



## Révision Rapide 1

Révisons les instructions Python vues jusqu'à présent.

Vous pouvez écrire des commentaires avec le caractère `#` :

```python
# Ceci est un commentaire.
```

Tout ce qui suit le `#` jusqu’à la fin de la ligne est un commentaire. Les commentaires sont des notes pour vous rappeler ce que fait votre programme. Ils n'affectent pas l'exécution du code.

Vos programmes doivent toujours importer le module `turtle` :

```python
from turtle import *
```

Le module doit être importé avant d’utiliser ses fonctions. Placez toujours cette ligne en haut de vos programmes Turtle.

Il existe des fonctions pour déplacer la tortue :

```python
forward(100)  # Avancer de 100 unités.
backward(100)  # Reculer de 100 unités.
forward(-100)  # Reculer aussi de 100 unités.
```

Vous pouvez avancer ou reculer en passant un nombre à `forward()` ou `backward()`. Passer un nombre négatif inverse la direction.

Il existe aussi des fonctions pour tourner la tortue :

```python
left(90)  # Tourner à gauche de 90 degrés.
right(45)  # Tourner à droite de 45 degrés.
```

Vous pouvez tourner la tortue en passant un angle à `left()` ou `right()`. Elle tourne sur place sans se déplacer. Un nombre négatif inverse le sens de rotation.

Par défaut, la tortue trace une ligne fine. Vous pouvez la rendre plus épaisse :

```python
pensize(4)
```

L’épaisseur par défaut est `1`. Passez un nombre plus grand à `pensize()` pour épaissir la ligne.

À la fin de vos programmes Turtle, vous devez appeler `done()` :

```python
done()
```

Cela garde la fenêtre ouverte après la fin du dessin, au lieu de se fermer immédiatement.

Vous pouvez passer des nombres aux fonctions, ou stocker ces nombres dans des variables :

```python
line_length = 25  # La variable contient le nombre 25.
forward(line_length)
```

Ici, `forward(line_length)` est identique à `forward(25)`.

Une boucle `for` vous permet de répéter du code :

```python
for i in range(4):  
    forward(200)
    left(90)
```

Cela répète les deux lignes indentées quatre fois. Cela dessine un carré.

La tortue est lente par défaut. Pour la rendre plus rapide, utilisez :

```python
speed('fastest')
```

N'oubliez pas les guillemets ! Écrivez `speed('fastest')` et non `speed(fastest)`.

Vous pouvez cacher le curseur triangle de la tortue avec :

```python
hideturtle()
```

Cela fait disparaître le curseur triangle de la fenêtre.

Pour générer des nombres aléatoires, importez le module `random` :

```python
from random import *
forward(randint(1, 100))
```

La fonction `randint(1, 100)` renvoie un nombre aléatoire entre 1 et 100.



## Exercices Pratiques 1

Créez des programmes qui dessinent les images de cette section. Les solutions sont à la fin de ce tutoriel. Votre code et vos dessins ne doivent pas forcément être identiques à ceux-ci, mais ils doivent ressembler. Il y a plusieurs façons valides d’écrire ces programmes.

Créez un programme nommé *solution_equilateral_triangle.py* qui dessine l’image suivante. *Indice : tous les côtés du triangle équilatéral font 200 unités. Le premier angle est un virage à droite de 60 degrés. Les suivants sont de 120 degrés.*

![Triangle équilatéral](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_solution_equilateral_triangle.jpg)

Créez un programme nommé *solution_pentagon.py* qui dessine l’image suivante. *Indice : tous les côtés font 200 unités et tous les angles sont de 72 degrés.*

![Pentagone](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_solution_pentagon.jpg)

Créez un programme nommé *solution_hexagon.py* qui dessine l’image suivante. *Indice : tous les côtés font 200 unités et les angles sont de 60 degrés.*

![Hexagone](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_solution_hexagon.jpg)

Créez un programme nommé *solution_octagon.py* qui dessine l’image suivante. *Indice : tous les côtés font 100 unités et les angles sont de 45 degrés.*

![Octogone](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_solution_octagon.jpg)

Créez un programme nommé *solution_right_triangle.py* qui dessine l’image suivante. *Indice : pour ce triangle rectangle, un angle est de 90 degrés et un autre de 135 degrés. Deux côtés font 200 unités. Selon le théorème de Pythagore, le troisième côté mesure 282,8 unités.*

![Triangle rectangle](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_solution_right_triangle.jpg)

Créez un programme nommé *solution_star.py* qui dessine l’image suivante. *Indice : tous les côtés font 200 unités et tous les angles sont de 144 degrés.*

![Étoile](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_solution_star.jpg)

Créez un programme nommé *solution_nested_squares.py* qui dessine l’image suivante. *Indice : dessinez un carré de 100 unités, puis un autre de 150, 200, 250, et 300. Vous pouvez utiliser une boucle à l’intérieur d’une autre.*

![Carrés imbriqués](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_solution_nested_squares.jpg)

Créez un programme nommé *solution_cross.py* qui dessine l’image suivante. *Indice : toutes les lignes font 100 unités. Les angles sont de 90 degrés, mais vous devez tourner à gauche et à droite.*

![Croix](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_solution_cross.jpg)

Créez un programme nommé *solution_cube.py* qui dessine l’image suivante. *Indice : toutes les lignes font 100 unités. Les angles sont de 45, 90 ou 135 degrés. Vous pouvez superposer des lignes pour dessiner le cube. Utilisez `forward(100)` puis `backward(100)` pour revenir à la position précédente.*

![Cube](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_solution_cube.jpg)

Créez un programme nommé *solution_triforce.py* qui dessine l’image suivante. *Indice : vous pouvez tracer des lignes superposées. Les angles sont de 60 ou 120 degrés. Si les côtés extérieurs font 100 unités, vous pouvez déplacer la tortue de 50 unités parfois.*

![Triforce](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_solution_triforce.jpg)



## Écrire du Texte dans la Fenêtre Turtle

La tortue peut écrire du texte dans la fenêtre Turtle, tout comme elle trace des lignes. La fonction `write()` prend une chaîne de texte en argument et l’écrit à la position actuelle de la tortue. Créons un programme qui écrit du texte. Enregistrez-le sous le nom *write_hello.py* :

```python
# write_hello.py

from turtle import *

write('Bonjour le monde !')
forward(80)
right(45)
forward(50)
write('123456789', font=('Arial', 48, 'normal'))
right(45)
forward(30)
write('oOoOoOoOoOo')
done()
```

Quand vous exécutez ce programme, la fenêtre Turtle ressemblera à ceci :

![Écriture Turtle](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_write_hello.jpg)

Le coin inférieur gauche du texte correspond à la position de la tortue. Par exemple, le texte `'Bonjour le monde !'` est écrit au centre de la fenêtre Turtle. Ensuite, la tortue se déplace avec `forward(80)`, `right(45)`, `forward(50)`. Puis, `write('123456789', font=('Arial', 48, 'normal'))` affiche le texte à la nouvelle position.

L’appel `write('123456789', font=('Arial', 48, 'normal'))` inclut un *paramètre nommé* `font=`. On peut passer un argument comme `('Arial', 48, 'normal')` pour changer la police utilisée dans la fenêtre.

Le paramètre `font` contient trois éléments :

* Le nom de la police (`'Arial'`)
* La taille de la police (`48`)
* Le style de la police (`'normal'`)

Si vous ne passez aucun argument, la police par défaut est `('Arial', 8, 'normal')`. Vous pouvez utiliser n’importe quelle police installée sur votre ordinateur. La taille doit être un nombre (par exemple `48` et non `'48'`). Le style peut être `'normal'`, `'bold'`, `'italic'`, `'underline'`, ou une combinaison comme `'bold italic'`.



## Angles

Dans les programmes Turtle, la distance est mesurée en unités (ou "pas"). Par exemple, `forward(100)` fait avancer la tortue de 100 unités. On peut également mesurer les rotations et les directions avec des nombres.

Imaginez que vous regardez la tortue d’en haut. Si elle tourne à droite, elle tourne dans le sens horaire. Si elle tourne à gauche, elle tourne dans le sens antihoraire.

Les angles sont mesurés en degrés. Un tour complet correspond à 360 degrés. Si la tortue tourne de 180 degrés, elle fait demi-tour. Un angle droit est de 90 degrés. Si vous faites quatre fois un virage de 90 degrés, vous revenez dans la même direction, car 90 + 90 + 90 + 90 = 360.

On peut aussi utiliser les degrés pour indiquer l’orientation actuelle de la tortue. Lorsqu’un programme commence, la tortue est orientée vers la droite. Cette direction est 0 degré. En tournant à gauche (sens antihoraire), l’angle augmente :

* 90 degrés = vers le haut
* 180 degrés = vers la gauche
* 270 degrés = vers le bas
* 360 degrés ou 0 degré = vers la droite

La fonction `heading()` retourne l’orientation actuelle de la tortue. On peut l’utiliser avec `write()` pour afficher cet angle dans la fenêtre.

Créez un nouveau programme appelé *turtle_directions.py* :

```python
# turtle_directions.py
from turtle import *

for i in range(24):
    forward(100)  # Avancer dans la direction actuelle.
    write(heading(), font=('Arial', 20, 'normal'))  # Afficher l’angle.
    backward(100)  # Revenir au centre.
    left(15)  # Tourner de 15 degrés.
done()
```

Résultat dans la fenêtre Turtle :

![Directions tortue](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_turtle_directions.jpg)

Les fonctions `left()` et `right()` tournent en fonction de l’angle actuel. Si la tortue est orientée à 45 degrés et qu’on exécute `left(90)`, elle sera à 135 degrés (45 + 90 = 135).

La fonction `setheading()` permet de définir directement une orientation, peu importe celle actuelle.

Par exemple, ce programme affiche une orientation aléatoire puis fixe celle-ci à 45 degrés :

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

Cela affiche un premier angle aléatoire, puis la tortue est orientée vers 45 degrés et avance à nouveau.

Voici quelques exemples de sortie :

![Exemple 1](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_setheading_turtle1.jpg)
![Exemple 2](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_setheading_turtle2.jpg)
![Exemple 3](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_setheading_turtle3.jpg)
![Exemple 4](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_setheading_turtle4.jpg)



## Coordonnées Cartésiennes XY

Tout comme les angles décrivent la direction de la tortue, la *position* de la tortue peut être représentée par deux nombres : les coordonnées *X* et *Y*. Ce système est appelé *système de coordonnées cartésiennes*.

* L’origine, au centre de la fenêtre, a pour coordonnées `0, 0`.
* L’axe X indique la position horizontale (gauche-droite).
* L’axe Y indique la position verticale (haut-bas).
* Le X augmente vers la droite, et diminue vers la gauche.
* Le Y augmente vers le haut, et diminue vers le bas.

Une tortue placée :
* à gauche a un X négatif,
* à droite a un X positif,
* en bas a un Y négatif,
* en haut a un Y positif.

Cette image de Wikipédia illustre les coordonnées cartésiennes :

![Coordonnées](cartesian.png)

Créons un programme qui écrit les coordonnées XY pendant que la tortue se déplace. Enregistrez-le sous le nom *random_position.py* :

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

Ce programme affichera quelque chose comme ceci :

![Position aléatoire](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_random_position.jpg)

La fonction `position()` retourne les coordonnées actuelles de la tortue. Remarquez que X et Y augmentent quand la tortue va vers la droite ou le haut, et diminuent quand elle va vers la gauche ou le bas.

Les fonctions `forward()` et `backward()` déplacent la tortue à partir de sa position actuelle. Mais pour aller à une position précise, on peut utiliser `goto(x, y)`.

Créons un programme qui place la tortue à des coordonnées aléatoires. Enregistrez-le sous le nom *random_goto.py* :

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

Voici quelques exemples de sortie :

![Goto 1](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_random_goto1.jpg)
![Goto 2](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_random_goto2.jpg)
![Goto 3](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_random_goto3.jpg)
![Goto 4](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_random_goto4.jpg)

Ici, `goto(x, y)` déplace la tortue aux coordonnées aléatoires générées avec `randint(-400, 400)`.



## Home, Clear, Reset, Undo

La tortue trace des lignes lorsqu’elle se déplace, mais il existe plusieurs fonctions pour effacer ces lignes :

* `home()` ramène la tortue à la position d’origine (0, 0) et oriente sa direction à 0 degré. C’est équivalent à `goto(0, 0)` suivi de `setheading(0)`.
* `clear()` efface toutes les lignes dessinées, mais ne déplace pas la tortue.
* `reset()` efface toutes les lignes **et** replace la tortue à l’origine en orientation 0. C’est équivalent à `home()` + `clear()`.
* `undo()` annule la dernière action de dessin. Vous pouvez appeler plusieurs fois `undo()` pour effacer plusieurs segments.

Ces fonctions sont utiles lorsque vous voulez réinitialiser le dessin ou expérimenter sans redémarrer le programme.



## Révision Rapide 2

Passons en revue les nouvelles instructions Python apprises :

```python
write('Bonjour le monde !')
write('Bonjour le monde !', font=('Arial', 48, 'normal'))
```

La fonction `write()` écrit du texte dans la fenêtre Turtle à la position actuelle de la tortue. Vous pouvez passer une chaîne de texte, et aussi un paramètre nommé `font=` pour changer la police, la taille et le style.

```python
setheading(90)
orientation_actuelle = heading()
```

La fonction `setheading()` oriente la tortue dans une direction absolue :
- `0` = droite (est)
- `90` = haut (nord)
- `180` = gauche (ouest)
- `270` = bas (sud)

La fonction `heading()` retourne l’orientation actuelle de la tortue. Vous pouvez l’utiliser dans des appels de fonction ou la stocker dans une variable.

```python
goto(250, -100)  # Aller à la position XY (250, -100).
```

* Les coordonnées XY indiquent la position exacte.
* Le centre de la fenêtre Turtle est l’origine (0, 0).
* X augmente vers la droite, diminue vers la gauche.
* Y augmente vers le haut, diminue vers le bas.

Pour recommencer le dessin, vous pouvez appeler :

* `home()` — revient à (0, 0) et oriente à 0 degré.
* `clear()` — efface tout le dessin sans déplacer la tortue.
* `reset()` — efface tout **et** revient à l’origine.
* `undo()` — annule le dernier segment tracé.



## Exercices Pratiques 2

Créez un programme nommé *solution_star_outline.py* qui dessine l’image suivante. Utilisez uniquement `goto()` pour déplacer la tortue.  
*Indice : les coordonnées à passer à `goto()` sont (0, 300), (70, 95), (285, 95), (110, -35), (175, -260), (0, -100), (-175, -260), (-110, -35), (-285, 95), (-70, 95), et (0, 300)*

![Contour étoile](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_solution_star_outline.jpg)

Créez un programme nommé *solution_cross_setheading.py* qui dessine l’image suivante. N’utilisez pas `right()` ni `left()`, mais uniquement `setheading()`.  
*Indice : toutes les lignes font 100 unités. Les directions sont : 0, 90, 180 ou 270.*

![Croix (setheading)](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_solution_cross.jpg)

Créez un programme nommé *solution_random_hello.py* qui écrit "Bonjour le monde !" cent fois à des positions aléatoires dans la fenêtre Turtle. Le texte doit aussi avoir des tailles aléatoires entre 12 et 48. Ne tracez aucune ligne et cachez le curseur. Le programme ressemblera à :

![Bonjour aléatoire](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_solution_random_hello.jpg)



## Couleurs

Vous pouvez changer la couleur de fond de la fenêtre avec la fonction `bgcolor()`, en passant une chaîne de texte correspondant à une couleur, ou une valeur RGB (rouge, vert, bleu) sous forme de trois nombres entre 0.0 et 1.0.

Exemples de couleurs avec leurs valeurs RGB :

* `'black'` = `(0.0, 0.0, 0.0)`
* `'blue'` = `(0.0, 0.0, 1.0)`
* `'brown'` = `(0.6, 0.4, 0.2)`
* `'orange'` = `(1.0, 0.5, 0.0)`
* `'gray'` = `(0.5, 0.5, 0.5)`
* `'green'` = `(0.0, 1.0, 0.0)`
* `'purple'` = `(0.5, 0.0, 0.5)`
* `'violet'` = `(0.56, 0.0, 1.0)`
* `'pink'` = `(1.0, 0.75, 0.8)`
* `'yellow'` = `(1.0, 1.0, 0.0)`
* `'white'` = `(1.0, 1.0, 1.0)`
* `'red'` = `(1.0, 0.0, 0.0)`
* `'magenta'` = `(1.0, 0.0, 1.0)`
* `'cyan'` = `(0.0, 1.0, 1.0)`

Pour changer la couleur des lignes tracées par la tortue, utilisez la fonction `pencolor()`.

Par exemple, si vous ajoutez `bgcolor('yellow')` et `pencolor('blue')` dans le programme *square_circle_86.py*, vous obtenez :

![Fond jaune](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_bgcolor_yellow.jpg)

Les couleurs personnalisées utilisent des valeurs RGB : chaque composante (rouge, vert, bleu) est un nombre entre `0.0` (aucune) et `1.0` (maximum).  
Exemples :

* `(1.0, 0.0, 0.0)` = rouge pur (`'red'`)
* `(1.0, 1.0, 0.0)` = jaune (`'yellow'`)
* `(1.0, 1.0, 0.5)` = jaune clair
* `(0.5, 0.5, 0)` = jaune foncé
* `(0.0, 0.0, 0.0)` = noir (`'black'`)
* `(1.0, 1.0, 1.0)` = blanc (`'white'`)

Vous pouvez tester les couleurs avec l'application `turtlecolors`.  
Téléchargez le fichier depuis [ce lien](https://raw.githubusercontent.com/asweigart/turtlecolors/refs/heads/main/src/turtlecolors/__init__.py), copiez-le dans un fichier nommé *turtlecolors.py*, et exécutez-le. Vous pourrez ajuster les valeurs de rouge, vert et bleu avec des curseurs.

L'application ressemble à ceci :

![turtlecolors 1](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_turtlecolors1.jpg)  
![turtlecolors 2](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_turtlecolors2.jpg)  
![turtlecolors 3](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_turtlecolors3.jpg)  
![turtlecolors 4](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_turtlecolors4.jpg)



## Lever et Baisser le Stylo

Imaginez que la tortue tient un stylo dans sa bouche. Quand le stylo touche le sol, elle trace une ligne en se déplaçant. Si le stylo est levé, la tortue ne trace rien.

Les fonctions suivantes permettent de contrôler cela :

* `pendown()` — le stylo est abaissé, les mouvements tracent des lignes.
* `penup()` — le stylo est levé, les mouvements ne tracent rien.

Par défaut, la tortue commence avec le stylo abaissé.

Créons un programme qui trace une ligne en pointillés. Enregistrez-le sous le nom *dashed_lines.py* :

```python
# dashed_lines.py
from turtle import *
from random import *

pensize(4)
speed('fastest')

for i in range(12):
    # Se tourner dans une direction aléatoire :
    setheading(randint(0, 360))

    # Tracer une ligne en pointillés :
    for j in range(6):
        pendown()
        forward(10)  # Tracer un segment.
        penup()
        forward(10)  # Avancer sans tracer.

    # Un dernier segment pour finir la ligne :
    pendown()
    forward(10)

done()
```

La boucle `for i in range(12):` dessine douze lignes en pointillés.  
Chaque ligne est composée de segments courts grâce à la boucle `for j in range(6):`, avec 10 unités tracées et 10 unités non tracées.

Ce programme utilise des valeurs aléatoires, donc chaque exécution donnera un résultat différent :

![Lignes pointillées 1](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_dashed1.jpg)  
![Lignes pointillées 2](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_dashed2.jpg)



## Exemples de Spirales Carrées

Créons un programme qui trace une spirale carrée. Enregistrez-le sous le nom *spiral.py* :

```python
# spiral.py
from turtle import *

speed('fastest')
for i in range(300):
    forward(i)  # Utilise la variable i pour la longueur.
    left(91)
hideturtle()
done()
```

Quand vous exécutez ce programme, vous obtenez :

![Spirale](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_spiral.jpg)

Dans nos boucles précédentes, nous ignorions souvent la variable `i`. Ici, nous l’utilisons pour définir la longueur des lignes : chaque ligne devient plus longue que la précédente.

`range(300)` fait que `i` va de 0 à 299, donc on appelle :

```python
forward(0)
left(91)
forward(1)
left(91)
forward(2)
left(91)
...
forward(299)
left(91)
```

Cela économise beaucoup de lignes de code !

Essayez de remplacer `91` par un autre nombre entre `30` et `180` pour voir comment cela change le dessin.

---

Créons maintenant une spirale colorée aléatoire. Enregistrez le fichier sous *spiral_black_bg.py* :

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

Résultat :

![Spirale fond noir](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_spiral_black_bg.jpg)

La fonction `choice()` choisit une couleur au hasard dans la liste `colors`.

---

Pour faire une spirale arc-en-ciel, créez le fichier *spiral_rainbow.py* :

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

Chaque boucle utilise une couleur différente et augmente la taille de la spirale.

Résultat :

![Spirale arc-en-ciel](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_spiral_rainbow.jpg)



## Dessiner Très Rapidement

Si `speed('fastest')` n’est pas assez rapide, vous pouvez utiliser `tracer(100, 0)` pour encore accélérer le dessin. Mais vous devez ensuite appeler `update()` à la fin de votre dessin pour que tout s'affiche correctement.

Plus la valeur passée à `tracer()` est grande, plus le dessin est rapide. Exemple : `tracer(1000, 0)` est encore plus rapide que `tracer(100, 0)`.

Créons un programme qui dessine 1 000 lignes rapidement. Enregistrez-le sous *random_tracer.py* :

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

Résultat :

![Tracer rapide](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_random_tracer.jpg)

Avec `tracer(10, 0)`, le programme prend quelques secondes.  
Avec `tracer(100, 0)`, il est plus rapide.  
Avec `tracer(1000, 0)`, il est presque instantané.

À partir d’un certain seuil (vers `1000`), augmenter la valeur n’accélère plus le dessin, car votre ordinateur atteint sa vitesse maximale.

⚠️ Si certaines lignes ne s’affichent pas, vérifiez que vous avez bien ajouté `update()` à la fin du programme.



## Dessin Interactif

L’art généré par ordinateur peut aussi être interactif. En Python, vous pouvez définir vos propres fonctions avec le mot-clé `def`, et utiliser `getscreen().onclick()` pour appeler une fonction quand l’utilisateur clique dans la fenêtre Turtle.

Créez un nouveau fichier nommé *click_square.py* :

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

getscreen().onclick(draw_square)  # Attention : pas de () après draw_square
done()
```

Au début, rien ne se passe. Mais dès que vous cliquez dans la fenêtre, la fonction `draw_square()` est appelée avec les coordonnées `x` et `y` du clic. Elle place la tortue, puis dessine un carré.

Après quelques clics, la fenêtre pourrait ressembler à ceci :

![Carrés cliqués](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_click_square.jpg)

---

Faisons maintenant apparaître une spirale à chaque clic. Enregistrez sous *click_spiral.py* :

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

Résultat après plusieurs clics :

![Spirales cliquées](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_click_spiral.jpg)

---

Faisons des spirales rouges ressemblant à des roses. Enregistrez sous *click_rose.py* :

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

Et voici un magnifique bouquet numérique :

![Roses cliquées](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_click_rose.jpg)



## Tracer des Courbes et des Cercles

Le module `turtle` ne peut tracer que des lignes droites. Mais en enchaînant de très courtes lignes avec des légers virages, on peut créer l’illusion d’une courbe.

Créons un programme nommé *curve_path.py* :

```python
# curve_path.py

from turtle import *
from random import *

tracer(4, 0)

for i in range(100):  # Tracer 100 chemins courbés
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

Ce programme donne une sortie ressemblant à ceci :

![Courbes](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_curve_path.jpg)

Chaque courbe est faite de petits segments d’1 unité, tournés légèrement pour créer un effet de courbure.

---

Pour dessiner un cercle, la fonction `circle()` trace un polygone à 360 côtés.  
Passez-lui un rayon (la moitié de la largeur du cercle).  
Créez un fichier *draw_circles.py* :

```python
# draw_circles.py
from turtle import *

speed('fastest')

# Cercles vers le haut :
setheading(0)
for i in range(20):
    circle(i * 10)

# Cercles vers le bas :
setheading(180)
for i in range(20):
    circle(i * 10)

done()
```

Résultat :

![Cercles](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_draw_circles.jpg)

---

Faisons un dessin avec de nombreux cercles qui se superposent.  
Créez un fichier *draw_many_circles.py* :

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

Résultat :

![Beaucoup de cercles](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_draw_many_circles.jpg)

Testez différentes valeurs pour voir comment le dessin change.  
Pour accélérer, vous pouvez remplacer `speed('fastest')` par `tracer(1000, 0)` et ajouter `update()` juste avant `done()`.



## Programme Fleurs Bleues

Utilisons tout ce que nous avons appris pour créer un programme d'art génératif.  
Ce programme dessine des fleurs bleues en traçant six cercles à une position, taille, épaisseur et couleur aléatoires.  
La couleur sera toujours une nuance de bleu.

Voici le code :

```python
from turtle import *
from random import *

tracer(100, 0)

for n in range(50):
    # Aller à une position aléatoire :
    penup()
    x = randint(-300, 300)
    y = randint(-300, 300)
    goto(x, y)
    pendown()

    # Choisir une nuance aléatoire de bleu :
    pencolor((0, 0, random()))

    # Épaisseur aléatoire :
    pensize(randint(1, 5))

    # Taille aléatoire des cercles :
    circle_size = randint(10, 40)

    # Tracer 6 cercles :
    for i in range(6):
        circle(circle_size)
        left(60)
update()
done()
```

Le résultat dans la fenêtre Turtle ressemble à ceci :

![Fleurs bleues](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_blue_flowers.jpg)

À chaque exécution, le dessin sera différent !



## Formes Remplies

Jusqu'à présent, nous avons seulement dessiné des contours. Mais il est aussi possible de dessiner des formes remplies de couleur.

Utilisez `fillcolor()` pour définir la couleur de remplissage.  
Entourez les instructions de dessin avec `begin_fill()` et `end_fill()` pour remplir la forme.

Exemple : dessinons un carré rempli. Enregistrez-le sous *filled_square.py* :

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

Résultat :

![Carré rempli](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_filled_square.jpg)

---

Créons un programme qui dessine plusieurs carrés remplis avec des tailles et des couleurs aléatoires.  
Enregistrez-le sous *colorful_squares.py* :

```python
# colorful_squares.py

from turtle import *
from random import *

pensize(4)
tracer(10, 0)

for i in range(100):  # Dessiner 100 carrés
    # Aller à une position aléatoire :
    penup()
    goto(randint(-400, 200), randint(-400, 200))
    pendown()

    # Couleurs de remplissage et de trait aléatoires :
    fillcolor((random(), random(), random()))
    pencolor((random(), random(), random()))

    # Taille aléatoire du carré :
    line_length = randint(20, 200)

    begin_fill()
    for j in range(4):
        forward(line_length)
        left(90)
    end_fill()

done()
```

Résultat :

![Carrés colorés](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_colorful_squares.jpg)

---

Et pourquoi pas remplir des formes courbes ?  
Modifions *curve_path.py* en *curve_path_filled.py* :

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

Résultat :

![Formes courbes remplies](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_curve_path_filled.jpg)



## Pour Aller Plus Loin

Ce tutoriel couvre les bases du module `turtle` de Python. Il existe encore bien d'autres fonctions et possibilités !

Ressources supplémentaires :

* [Documentation officielle du module Turtle](https://docs.python.org/3/library/turtle.html)
* [Liste des fonctions Turtle](https://docs.python.org/3/library/turtle.html#turtle-methods)
* [Chapitre 9 du livre *The Recursive Book of Recursion* (tortues récursives)](https://inventwithpython.com/recursion/chapter9.html)
* [Chapitre 13 du même livre (fractales récursives)](https://inventwithpython.com/recursion/chapter13.html)

---

Python inclut aussi un programme appelé `turtledemo`, contenant plusieurs exemples.

Voici comment l'utiliser :

```python
import turtledemo.__main__
turtledemo.__main__.main()
```

En exécutant ce code, vous ouvrirez une fenêtre où vous pourrez choisir des exemples à exécuter.  
Cliquez sur **Start** pour lancer un exemple. Le code source apparaît à gauche.

Exemple (programme "Peace") :

![Peace](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/screenshot_peace.jpg)

Bonne chance dans votre aventure Python !



## Défis Turtle Avancés

Si vous cherchez des formes plus complexes à tracer avec Turtle, consultez les œuvres d’[Oscar Reutersvärd](https://fr.wikipedia.org/wiki/Oscar_Reutersv%C3%A4rd), le pionnier des illusions géométriques.

Le site [Impossible World](https://im-possible.info/english/library/index.html) présente plusieurs de ses dessins que vous pouvez essayer de reproduire avec Turtle.

Vous pouvez aussi faire une [recherche d'images pour "Oscar Reutersvärd"](https://duckduckgo.com/?t=ffab&q=Oscar+Reutersv%C3%A4rd&iax=images&ia=images) pour vous inspirer.

Exemples :

![Oscar 1](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/oscar1.jpg)  
![Oscar 2](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/oscar2.jpg)  
![Oscar 3](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/oscar3.jpg)  
![Oscar 4](https://raw.githubusercontent.com/asweigart/simple-turtle-tutorial-for-python/refs/heads/master/oscar4.jpg)

Ces formes sont de véritables casse-têtes de géométrie, parfaits pour progresser !



## Solutions

Voici les solutions des exercices pratiques mentionnés plus tôt.

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

```python
# solution_pentagon.py
from turtle import *
pensize(4)

for i in range(5):
    left(72)
    forward(200)

done()
```

```python
# solution_hexagon.py
from turtle import *
pensize(4)

for i in range(6):
    left(60)
    forward(200)

done()
```

```python
# solution_octagon.py
from turtle import *
pensize(4)

for i in range(8):
    left(45)
    forward(100)

done()
```

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

```python
# solution_star.py
from turtle import *
pensize(4)

for i in range(5):
    right(144)
    forward(300)

done()
```

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

```python
# solution_cube.py
from turtle import *
pensize(4)

# Carré avant
for i in range(4):
    forward(200)
    right(90)

# Diagonale arrière
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

```python
# solution_random_hello.py
from turtle import *
from random import *

tracer(1000, 0)
penup()
hideturtle()

for i in range(100):
    goto(randint(-400, 400), randint(-400, 400))
    write('Bonjour le monde !', font=('Arial', randint(12, 48), 'normal'))

update()
done()
```

