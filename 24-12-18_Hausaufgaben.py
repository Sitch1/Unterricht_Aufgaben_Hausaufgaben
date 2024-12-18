



#Aufgabenbeschreibung:
#1. Aktuelles Datum und Uhrzeit ausgeben:
#○ Importiere das datetime-Modul.
#○ Erstelle eine Funktion aktuelles_datum_und_uhrzeit(), die das
#aktuelle Datum und die aktuelle Uhrzeit im Format TT.MM.JJJJ HH:MM:SS
#ausgibt.

from datetime import datetime
def aktuelles_datum_und_uhrzeit():
    aktuelles_datum = datetime.today().strftime('%d.%m.%Y, %X')

    print(aktuelles_datum)

aktuelles_datum_und_uhrzeit()



#2. Differenz bis zum Jahresende berechnen:
#○ Schreibe eine Funktion tage_bis_jahresende(), die die Anzahl der Tage
#vom aktuellen Datum bis zum 31. Dezember des aktuellen Jahres berechnet.
#○ Hinweis: Verwende datetime.date oder datetime.datetime zur
#Berechnung.
####VERSUCH 1.#######

import datetime
def Tag_bis_ende_des_jahres():
    aktuelles_datum = datetime.date()
    Jahresende = (2024, 12, 31)
    differenz = aktuelles_datum - Jahresende
    print(f'Jajres ende {differenz}')

######VERSUCH 2.##########

import datetime
def Tag_bis_ende_des_jahres():
    aktuelles_datum = datetime.date.today()
    Jahresende = datetime.date(2024, 12, 31)
    differenz = aktuelles_datum - (Jahresende)
    print(differenz)

Tag_bis_ende_des_jahres()



#3. Benutzerdefiniertes Datum:
#○ Implementiere eine Funktion tage_bis_datum(), die ein vom Benutzer
#eingegebenes Datum im Format TT.MM.JJJJ einliest und die Anzahl der
#Tage vom aktuellen Datum bis zu diesem Datum berechnet.
#○ Tipp: Verwende input() für die Benutzereingabe und prüfe, ob das
#eingegebene Datum gültig ist. Falls nicht, soll der Benutzer eine neue Eingabe
#machen.

def tag_bis_jahresende():
    
    tag_bis_jahresende = input('Gebe bitte ein Datum ein: ')


#4. Wochentag berechnen:
#○ Erstelle eine Funktion wochentag_berechnen(), die den Wochentag für ein
#beliebiges eingegebenes Datum berechnet und ausgibt (z. B. Montag,
#Dienstag usw.).
#5. Zeitverschiebung berechnen:
#○ Implementiere eine Funktion zeit_in_zukunft(), die eine Eingabe von
#Minuten, Stunden oder Tagen vom Benutzer entgegennimmt und das Datum
#und die Uhrzeit berechnet, die nach dieser Zeitspanne liegt.
#○ Beispiel: Wenn der Benutzer 2 Stunden eingibt und die aktuelle Zeit 14:00
#ist, sollte das Programm 16:00 ausgeben.