
# ● Form der Abgabe: Flussdiagramm (Foto oder Datei).
# ● Aufgabenstellung:
# Entwickle ein Flussdiagramm für einen Algorithmus, der prüft, ob eine Zahl eine
# Primzahl ist.
# ○ Schritte:
# 1. Nimm eine Zahl als Eingabe.
# 2. Überprüfe, ob die Zahl kleiner oder gleich 1 ist (nicht prim).
# 3. Überprüfe für alle Zahlen von 2 bis √n, ob es einen Teiler gibt.
# 4. Gib „Primzahl“ oder „Keine Primzahl“ aus.



user_input = int(input('Gebe bitte eine Zahl ein: '))

if user_input <= 1:
    print('Die Zahl ist kleiner')
elif user_input >= 1:
    print('Die Zahl ist größer')



print(user_input)




    