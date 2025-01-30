def begruessung(name):          # name muss in klammer stehen 
    print(f"Hallo, {name}")        # f fehlte und + zeichen weg gegen , ersetzen u. name in {}

begruessung("Max")               # hier fehlte noch zum ausfürhren der befehl mit begruessung

def addiere_zahlen(a, b):        # das zeichen : fehlte am endeder definition
    ergebnis = a + b
    return ergebnis 

def subtrahiere_zahlen(a, b):     
    return a - b                  # falsche argument c muss mit b ersetzt werden

def main():
    zahl1 = int(input("Gib eine Zahl ein: "))           # int muss vor dem input
    zahl2 = int(input("Gib eine weitere Zahl ein: "))   # int muss vor dem input

    summe = addiere_zahlen(zahl1, zahl2)  
    print("Die Summe ist: ", summe)                 # das + mit einem , ersetzen 

    differenz = subtrahiere_zahlen(zahl1, zahl2)
    print("Die Differenz ist: ", differenz)         # das + mit dem , ersetzen 

      

if __name__  == "__main__":
    main()