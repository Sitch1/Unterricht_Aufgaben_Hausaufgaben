



# Aufgabenstellung:
# Du sollst eine Klasse erstellen, die ein Haustier beschreibt. Die Klasse soll folgende
# Funktionalitäten enthalten:
# 1. Attribute:
# ● name (Name des Haustiers, z. B. "Bello")
# ● species (Tierart, z. B. "Hund", "Katze")
# ● age (Alter in Jahren)
# ● favorite_food (Lieblingsessen des Haustiers, z. B. "Knochen")
# ● energy_level (Energielevel des Haustiers, Standardwert: 100)

# 2. Methoden:
# ● get_description(): Gibt eine Beschreibung des Haustiers zurück, z. B. "Bello ist
# ein 5 Jahre alter Hund."
# ● play(duration): Simuliert, dass das Haustier spielt. Dabei verliert das Haustier
# Energie basierend auf der Dauer (duration) des Spiels. Die Energie sinkt um 5 Punkte
# pro Minute, kann aber nicht unter 0 fallen.
# ○ Beispiel: Bei 10 Minuten Spielen sinkt die Energie um 10 * 5 = 50 Punkte.
# ● feed(food): Füttert das Haustier. Wenn das Essen dem favorite_food entspricht,
# gewinnt das Haustier 30 Punkte Energie. Anderes Essen bringt nur 10 Punkte. Der
# Energielevel kann maximal 100 betragen.

# 3. Erstelle ein Haustier-Objekt:
# ● Name: "Mimi"
# ● Tierart: "Katze"
# ● Alter: 3 Jahre
# ● Lieblingsessen: "Fisch"

# 4. Teste die Klasse:
# ● Lasse das Haustier 15 Minuten spielen.
# ● Füttere es zuerst mit seinem Lieblingsessen und danach mit einem anderen Essen.
# ● Gib zu jedem Schritt die entsprechenden Rückmeldungen aus.



class Haustier:
    def __init__(self, name, species, age, favorite_food, energy_level=100):
        self.name = name
        self.species = species
        self.age = age
        self.favorite_food = favorite_food
        self.energy_level = energy_level
        self.sleep_hours = 0

    def get_description(self):
        return f"{self.name} ist ein {self.age} Jahre alter {self.species}."

    def play(self, duration):
        energy_loss = duration * 10
        self.energy_level = max(0, self.energy_level - energy_loss)
        return f"{self.name} hat {duration} Minuten gespielt und hat jetzt {self.energy_level} Energie."

    def feed(self, food):
        if food == self.favorite_food:
            self.energy_level = min(100, self.energy_level + 30)
            return f"{self.name} hat {food} gegessen und hat jetzt {self.energy_level} Energie."
        else:
            self.energy_level = min(100, self.energy_level + 10)
            return f"{self.name} hat {food} gegessen und hat jetzt {self.energy_level} Energie."
    def sleeping(self, hours):
        self.sleep_hours += hours
        self.energy_level = min(100, self.energy_level + hours * 10)
        return f"{self.name} hat {hours} Stunden geschlafen und hat jetzt  {self.energy_level} Energie"

# Erstellen des Haustier-Objekts
nova = Haustier(name="Nova", species="Chihaua", age=9, favorite_food="Käse")

# Testen der Klasse
print(nova.get_description())

# Mimi spielt 15 Minuten
print(nova.play(15))

# Füttern mit Lieblingsessen
print(nova.feed("Käse"))

# Füttern mit anderem Essen
print(nova.feed("TrockenFutter"))

# Nova schläft 10 Stunden
print(nova.sleeping(10))



# class Pet:
#     def __init__(self, name, species, age, favorite_food, energy_level=100):
#         self.name = name
#         self.species = species
#         self.age = age
#         self.favorite_food = favorite_food
#         self.energy_level = energy_level

#     def get_description(self):
#         return f"{self.name} ist ein {self.age} Jahre alter {self.species}."
    
#     def play(self, duration):
#         energy_loss = duration * 5
#         self.energy_level = max(0, self.energy_level - energy_loss)
#         return f"{self.name} hat {duration} Minuten gespielt und hat jetzt {self.energy_level} Energie."
    
#     def feed(self, food):
#         if food == self.favorite_food:
#             self.energy_level = min(100, self.energy_level + 30)
#             return f"{self.name} hat {food} gegessen und hat jetzt {self.energy_level} Energie."
#         else:
#             self.energy_level = min(100, self.energy_level + 10)
#             return f"{self.name} hat {food} gegessen und hat jetzt {self.energy_level} Energie."

# # Benutzereingaben für das Haustier
# name = input("Gib den Namen deines Haustiers ein: ")
# species = input("Gib die Tierart deines Haustiers ein (z. B. Hund, Katze): ")
# age = int(input("Gib das Alter deines Haustiers in Jahren ein: "))
# favorite_food = input("Gib das Lieblingsessen deines Haustiers ein: ")

# # Erstellen des Haustier-Objekts
# user_pet = Pet(name=name, species=species, age=age, favorite_food=favorite_food)

# # Testen der Klasse
# print(user_pet.get_description())

# # Spielen für eine bestimmte Zeit
# play_duration = int(input("Wie viele Minuten möchtest du mit deinem Haustier spielen? "))
# print(user_pet.play(play_duration))

# # Füttern mit Lieblingsessen
# feed_favorite = input("Füttere dein Haustier mit seinem Lieblingsessen (z. B. " + favorite_food + "): ")
# print(user_pet.feed(feed_favorite))

# # Füttern mit anderem Essen
# feed_other = input("Füttere dein Haustier mit einem anderen Essen (z. B. Käse): ")
# print(user_pet.feed(feed_other))

