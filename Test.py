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
class Pet:
    def __init__(self, name, species, age, favorite_food):
        self.name = name
        self.species = species
        self.age = age
        self.favorite_food = favorite_food
        self.energy_level = 100

    def get_description(self):
        description = f"{self.name} ist ein(e) {self.age} Jahre alte(er) {self.species}"
        return description
    
    def play(self, duration):
        energy_lost = duration * 5
        if self.energy_level <= energy_lost:
            print("Das Haustier ist zu müde zum Spielen!")
        
        if self.energy_level >= energy_lost:
            self.energy_level = self.energy_level - energy_lost
            energy_lost >= 100
            print(f"\n{self.name} hat {duration} min gespielt und hat jetzt ein Energie Level von:, {self.energy_level}%" ) 

        return
    
    def feed(self, food):
        if food == self.favorite_food:
            self.energy_level += 50
            if self.energy_level > 100:
                self.energy_level = 100
            print(f"\n{self.name} hat sein Lieblings Essen gegesen und jetzt ein Energie Level von: {self.energy_level} %")

        if food == self.favorite_food:
            self.energy_level -= 50
            if self.energy_level < 0:
                self.energy_level = 0
            print(f"Leider hat {self.name} Schokolade gegesen und jatzt Bauchweh das Energie level sinkt auf: {self.energy_level} %")
    




    
pet_objekt1 = Pet("Nova", "Chihuahua", 9, "Käse")
pet_objekt2 = Pet("Toni", "Old-English_BullDoge/Mix", 7, "Wurscht")

print(pet_objekt1.get_description())
print(pet_objekt2.get_description())


pet_objekt1.play(5)
pet_objekt2.play(5)
pet_objekt1.feed("Käse")
pet_objekt2.feed("Wurscht")
pet_objekt1.feed("Schokolade")
pet_objekt2.feed("Schokolade")





print(pet_objekt1.name, pet_objekt1.species, pet_objekt1.age, pet_objekt1.favorite_food)
print(pet_objekt2.name, pet_objekt2.species, pet_objekt2.age, pet_objekt2.favorite_food)



