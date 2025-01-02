# Aufgaben für den Nachmittag: Python-Code in Arbeitsschritte beschreiben

**Abgabe**: Text ()

## Aufgabe 1: Einfache Entscheidungen mit `if`-Statements (25 Punkte)

**Ziel:** Verstehen, wie Entscheidungen im Code in Arbeitsschritte übersetzt werden können.

Code-Beispiel:

```python
zahl = int(input("Gib eine Zahl ein: "))
if zahl > 10:
    print("Die Zahl ist größer als 10.")
else:
    print("Die Zahl ist 10 oder kleiner.")
```

- Schreibe die Arbeitsschritte auf.
- 1. Eingabe der Zahl:
Im ersten Feld, wird eine Eingabe gefordert. Dieser befehl wird durch ```input``` ausgeführt: ```[ zahl =int(input('Gib eine Zahl ein')) ]``` !
!ACHTUNG: Da eine Zahl eingeben wird muss noch der befehl ```int(integer)``` vor das input, damit diese als Zahl erkannt wird und nicht als Wort !

- 2. Bedingung überprüfen:
Nun wird die bediengung geprüft mit ``` if zahl > 10:```, ob die Zahl größer ist als 10. Ist dies der fahl wird mit  ```print("Die Zahl ist größer als 10.")``` , dem benutzer gesagt ob die Zahl größer ist.

- 3. Bedingung falsch:
Wenn die bedingun falsch ist also nicht größer als 10, wird die ```else``` bediungung ausgeführt. Also ist Zahl kleiner als 10 wird mit  ```print("Die Zahl ist 10 oder kleiner.")``` angezeigt.



---

## Aufgabe 2: Listen verstehen und mit Python erstellen (20 Punkte)

**Ziel:** Verstehen, wie Datenstrukturen wie Listen verwendet werden können.

Code-Beispiel:

```python
zahlen = [1, 2, 3, 4, 5]
print("Die erste Zahl ist:", zahlen[0])
print("Die letzte Zahl ist:", zahlen[-1])
```

- Schreibe die Arbeitsschritte auf.

- 1. Liste erstellen:
Um eine liste mit Zahlen zu erstellen, muss eine variable festgelgt werden ```zahlen = [1, 2, 3, 4, 5]```. Mit ```= [1, 2, 3, 4, 5]``` wird der Variable ```zahl``` der liste angehang. Die liste wird mit ```[]``` erstellt.
- 2. Mit ```print("Die erste Zahl ist:", zahlen[0])``` wird nun aus der angehangen list die erste zahl ```(1)``` angezigt und mit ```print("Die letzte Zahl ist:", zahlen[-1])```, die letzte zahl in der liste ```(5)````
- Warum aber ```[0]``` und ```[-1]```:

Die Indizierung in Python funktioniert so:

    zahlen[0]:
    Der Index 0 bedeutet, dass wir auf das erste Element in der Liste zugreifen. In Python beginnt die Zählung von Elementen in einer Liste immer bei 0. Also zahlen[0] gibt die erste Zahl in der Liste aus, in diesem Fall die Zahl 1.

    zahlen[-1]:
    Der Index -1 bedeutet, dass wir auf das letzte Element der Liste zugreifen. Negative Indizes zählen von hinten nach vorne. zahlen[-1] gibt also das letzte Element in der Liste aus, in diesem Fall die Zahl 5.

Zusammengefasst:

    zahlen[0]: Greift auf das erste Element zu.
    zahlen[-1]: Greift auf das letzte Element zu.

**Zusatzaufgabe:** Erstelle selbst eine Liste mit Wochentagen und schreibe die Arbeitsschritte auf.

---

## Aufgabe 3: Entscheidungslogik erweitern (25 Punkte)

**Ziel:** Die Funktionsweise von mehreren Bedingungen in Python verstehen und in Arbeitsschritte übertragen.

Code-Beispiel:

```python
zahl = int(input("Gib eine Zahl ein: "))
if zahl > 0:
    print("Die Zahl ist positiv.")
elif zahl < 0:
    print("Die Zahl ist negativ.")
else:
    print("Die Zahl ist null.")
```

- Schreibe die Arbeitsschritte auf.

- 1. Variable festlegen und input:
Jetzt wird zusätzlich der Variable ```zahl = int(input("Gib eine Zahl ein: "))```, wird noch ein ```input``` angehangen um ein eingabe zu fordern, des Users. !!!ACHTUNG!!! ```int(integer)``` muss vor dem input stehen, da es sonst nicht als Zahl erkannt wird.
- 2. Bedingung prüfen:
Nun wird eine die Bedingung mit ```if zahl > 0:``` gebpfüft. Mit ```if``` wird inerhalb des ```if-Block``` geprüft ob die bedingung ```if zahl > 0:``` posetiv ist, also True. Und mit ```print("Die Zahl ist positiv.")``` dem User das ergebniss angezigt.

Wenn die aussage falsch(false) ist also ```if zahl > 0``` nicht größer ist, tritt die ```elif(else if – sonst wenn)``` Bedingung ein. Die Bedingung ```elif zahl < 0:``` prüft nun ob die Zahl Negativ(kleiner)
ist. Ist die bedingung true so wird wieder mit ```print("Die Zahl ist negativ.")``` der Befehl ausgeführt.

---

## Aufgabe 4: Funktionen verstehen (20 Punkte)

**Ziel:** Lernen, wie Funktionen in Python definiert werden und was in jedem Arbeitsschritt passiert.

Code-Beispiel:

```python
def ist_gerade(zahl):
    if zahl % 2 == 0:
        return True
    else:
        return False

zahl = int(input("Gib eine Zahl ein: "))
if ist_gerade(zahl):
    print("Die Zahl ist gerade.")
else:
    print("Die Zahl ist ungerade.")
```

- Schreibe die Arbeitsschritte auf.

---

## Aufgabe 5: Benutzerinteraktion (10 Punkte)

**Ziel:** Die Struktur eines Programms mit Benutzereingaben und Ausgaben analysieren.

Code-Beispiel:

```python
name = input("Wie heißt du? ")
alter = int(input("Wie alt bist du? "))
print(f"Hallo {name}, in 10 Jahren wirst du {alter + 10} Jahre alt sein!")
```

- Schreibe die Arbeitsschritte auf.

---

Diese Aufgaben sind auf den bisherigen Stand der Vorlesung abgestimmt und bieten eine gute Balance zwischen Verständnis und Anwendung. Punkte sind proportional zur Komplexität der Aufgabe verteilt.