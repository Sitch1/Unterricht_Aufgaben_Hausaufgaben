
#Aufgabe 1 - Klassen und Vererbung


class Zutat():
    def __init__(self, name, kalorien, zubereitungszeit):
        self.name = name
        self.kalorien = kalorien
        self.zubereitungszeit = zubereitungszeit

    def anzeige(self):
        print(f"Zutat: {self.name}, Kalorien: {self.kalorien}, zubereitungszeit: {self.zubereitungszeit} minuten")

    def aktualisiere_kalorien(self, neue_kalorien):
        self.kalorien = neue_kalorien

    def aktualisiere_zubereitungszeit(self, neue_zeit):
        self.zubereitungszeit = neue_zeit

# Beispiel für die Nutzung der Klasse
zutat1 = Zutat("Tomate", 18, 5)
zutat2 = Zutat("Zwiebel", 40, 10)

zutat1.anzeigen()
zutat2.anzeige()

# Kalorien und Zubereitungszeit aktualisieren
zutat1.aktualisiere_kalorien(20)
zutat2.aktualisiere_zubereitungszeit(8)

zutat1.anzeige()
zutat2.anzeige()