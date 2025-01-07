



# class Server():
#     def _init_(self, Name, IPAdresse, Standort):
#         self.Name = Name
#         self.IpAdresse = IPAdresse
#         self.Standort = Standort

#     def text(self):
#         print (f"Dein server: Name:" {self.Name} "IpAdresse:" {self.IpAdresse} "Standort: {self.Standort}")
        
# user1_server = Server("ServerName", "192.168.1.10", "Hamburg")

# user1.text()



class Auto():
    def __init__(self, Name, Motor, reichweite, km):
        self.Name = Name
        self.Motor = Motor
        self.restreichweite = reichweite
        self.kilometeranzahl = km
    
    def fahren(self, km):
        if self.restreichweite >= km:
            self.kilometeranzahl += km
            self.restreichweite -= km
            print(f"Auto fährt {km} km")
        else:
            print("Reichweite nicht mehr ausreichend!")


    def tanken(self, km):
        self.restreichweite += km

    def Auto(self):
        print(f"Das Auto: {self.Name} mit dem Motor: {self.Motor} hat ein restreichweite von: {self.restreichweite} und dein Kilomterstand ist: {self.km}")
        
Car = Auto("Audi-A3","Benziner-2.0 TFSI", 200, 0)
Car.fahren(30)
Car.fahren(100)
Car.fahren(50)

print(Car.restreichweite)
Car.tanken(200)
print(Car.restreichweite)

print(f"Kilometerstand: {Car.kilometeranzahl}")