

#### !!. Taschenrechner .!! ####


#Funktionen Addieren, Subtrahieren, Multiplizieren und Dividieren

def addition(x, y):
    return x + y

def subtract(x, y):
    return x - y

def mult(x, y):
    return x * y

def division(x, y):
    if y == 0:
        return "Fehler: Division durch 0 ist nicht erlaubt"
    return x / y



#Funktionen für den Taschenrechner

def calculator():
    print('Welchen Taschenrechner wird benötigt?')
    print('1. Addieren')
    print('2. Suptrahieren')
    print('3. Multiplizieren')
    print('4. Dividieren')

    operation = input('Gebe bitte die Nummer für die bestimmte rechen art (1/2/3/4): ')




#Eingabe der beiden Zahlen
    x = float(input('Gebe bitte deine erste Zahl ein: '))
    y = float (input('Gebe bitte deine zweite zahl ein:  '))

    #Auswahl und Berechnungen der entsprechenden funktionen

    if operation == '1':
        result = addition(x,y)
        print(f'Addition ergebniss: {result}')

    elif operation == '2':
        result = suptract(x,y)
        print(f'Suptration Ergebniss: {result}')

    elif operation == '3':
        result = mult(x,y)
        print(f'Multiplikation Ergebniss: {result}')

    elif operation == '4':
        result = division(x,y)
        print(f'Division Ergebniss: {result}')
    else:
        print('Falsch zahl bitte gebe die Zahl 1 bis 4 an. ')

calculator()

