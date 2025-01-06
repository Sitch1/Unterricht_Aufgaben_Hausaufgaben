
# Aufgabe 1: Zähle, wie oft etwas passiert (40 Punkte)
# Schreibe ein Programm, das die Häufigkeit eines Buchstabens in einem Text zählt.
# 1. Der Benutzer gibt einen Text und einen Buchstaben ein.
# 2. Dein Programm zählt mit einer Schleife, wie oft dieser Buchstabe im Text vorkommt.


user_input = input("Gebe dein Text ein: ")
user = input("Welcher Buchstabe soll gezählt werden: ")
print(len(user_input))
print("Der String mit der Variable user_input ist ", len(user_input), "zeichen lang")
print("In deinem Text ist", user_input.count(user), "mal erhalten.")



# Aufgabe 2: Summen und Durchschnitt berechnen (40 Punkte)
# Schreibe ein Programm, das:
# 1. Den Benutzer auffordert, 5 Zahlen einzugeben.
# 2. Mit einer Schleife die Summe und den Durchschnitt der Zahlen berechnet.
# 3. Die Ergebnisse ausgibt.

summe = 0
anzahl = 5 

import math
for e in range(anzahl):
    user = float(input(f"Gib die {e+1}. Zahl ein"))
    summe += user

    durchschnitt = summe / anzahl

    print(f"Die Summe ist {summe} ")
    print(f"Der Durchschnitt ist, {durchschnitt} ")



# Aufgabe 3: Muster mit Schleifen erstellen (20 Punkte)
# Erstelle ein Muster mit einer verschachtelten Schleife. Beispiel:
# Der Benutzer gibt die Anzahl der Zeilen ein, und das Programm gibt folgendes Muster aus:




# Benutzer gibt die Anzahl der Zeilen ein
anzahl_zeilen = int(input("Gib die Anzahl der Zeilen ein: "))

# Verschachtelte Schleifen, um das Muster zu erstellen
for i in range(1, anzahl_zeilen + 1):  # Äußere Schleife für die Zeilen
    for _ in range(i):  # Innere Schleife für die Sterne in jeder Zeile
        print("*", end="")  # Ein Stern wird ohne Zeilenumbruch ausgegeben
    print()  # Neue Zeile nach jedem Durchlauf der inneren Schleife
    












