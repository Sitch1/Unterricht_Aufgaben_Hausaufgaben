
#### !!!..Hausaufgaben..!!! ####    17.12.2024


def calc_area(x,y):
    return x * y

def miles_to_km(x):
    return x * 0,621371

def celsius_to_fahrenheit(x):
    return (x * 9/5) + 32

def fahrenheit_in_celsius(x):
    return (x - 32) * 5/9

def calculator():
    while True:
        print('Was möchtest du umrechnen ?')
        print('1. Flächenberechnung (Breite * Höhe)')
        print('2. Meilen in Kilometer umrechnen')
        print('3. Celsius in Fahrenheit umrechnen')
        print('4. Fahrenheit in Celsius umrechnen')

        operation = input('Gib bitte die Nr. ein für die Umrechnung (1/2/3/4): ')



        if operation == '1':
            x = float(input('Bitte gebe die Breite an: '))
            y = float(input('Gib bitte die Höhe an: '))
            result = calc_area(x,y)
            print(f'Flächenberechnung Ergebniss: {result}')

        elif operation == '2':
            x = float(input('Gib bitte die Anzahl der Meilen an: '))
            result = miles_to_km(x)
            print(f'{x} Meilensind {result} Kilometer.')
        
        elif operation == '3':
            x = float(input('Gib bitte die Temperatur in Celsius ein: '))
            result = celsius_to_fahrenheit(x)
            print(f'{x} Grad Celsius sind {result} Grad in Fahrenheit.')

        elif operation == '4':
            x = float(input('Gib bitte die Temperatur in Fahrenheit ein: '))
            result = fahrenheit_in_celsius(x)
            print(f'{x} Grad Fahrenheit sind {result} Grad in Celsius.')
        else:
            print('Bitte gib eine gültige Zahl (1/2/3/4/) ein.')

calculator()



#### Aufgabe 2. #####


import random


def spiel_starten():
    print('Spiele Schere, Stein, Papier mit mir!')

while True:
    print('Bitte wähle: Schere, Stein, Papier')

    eingabe = input ('Wähle weise: ')
    spielzuege = ['Schere', 'Stein', 'Papier']
    
    if eingabe in spielzuege:
            random.shuffle(spielzuege)
            computer =spielzuege[0]


            if computer == eingabe:
                print('Unendschieden')
            if computer == 'Schere' and eingabe == 'Papier':
                print('Du hast verloren')
            if computer == 'Schere' and eingabe == 'Stein':
                print('Du hast Gewonnen')
            if computer == 'Stein' and eingabe == 'Schere':
                print('Du hast verloren')
            if computer == 'Stein' and eingabe == 'Papier':
                print('Du hast gewonnen')
            if computer == 'Papier' and eingabe == 'Stein':
                print('Du hast verloren')
            if computer == 'Papier'and eingabe == 'Schere':
                print('Du hast gewonnen')
    else:
            print('Falsche Eingabe')

    weitermachen = input('\nMöchtest du noch eine runde spielen? (Ja/Nein): ')
    if weitermachen != 'Ja':
        print('Danke fürs Spielen! Bis zum nächsten mal.')
        break
    
            
         
         
    spiel_starten()