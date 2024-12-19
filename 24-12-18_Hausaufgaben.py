



#Aufgabenbeschreibung:
#1. Aktuelles Datum und Uhrzeit ausgeben:
#○ Importiere das datetime-Modul.
#○ Erstelle eine Funktion aktuelles_datum_und_uhrzeit(), die das
#aktuelle Datum und die aktuelle Uhrzeit im Format TT.MM.JJJJ HH:MM:SS
#ausgibt.

# from datetime import datetime
# def aktuelles_datum_und_uhrzeit():
#     aktuelles_datum = datetime.today().strftime('%d.%m.%Y, %X')

#     print(aktuelles_datum)

# aktuelles_datum_und_uhrzeit()



# #2. Differenz bis zum Jahresende berechnen:
# #○ Schreibe eine Funktion tage_bis_jahresende(), die die Anzahl der Tage
# #vom aktuellen Datum bis zum 31. Dezember des aktuellen Jahres berechnet.
# #○ Hinweis: Verwende datetime.date oder datetime.datetime zur
# #Berechnung.
# ####VERSUCH 1.#######

# import datetime
# def Tag_bis_ende_des_jahres():
#     aktuelles_datum = datetime.date()
#     Jahresende = (2024, 12, 31)
#     differenz = aktuelles_datum - Jahresende
#     print(f'Jahres ende {differenz}')

# ######VERSUCH 2.##########

# import datetime
# def Tag_bis_ende_des_jahres():
#     aktuelles_datum = datetime.date.today()
#     Jahresende = datetime.date(2024, 12, 31)
#     differenz = (Jahresende) - aktuelles_datum
#     print(differenz)

# Tag_bis_ende_des_jahres()



# 3. Benutzerdefiniertes Datum:
# ○ Implementiere eine Funktion tage_bis_datum(), die ein vom Benutzer
# eingegebenes Datum im Format TT.MM.JJJJ einliest und die Anzahl der
# Tage vom aktuellen Datum bis zu diesem Datum berechnet.
# ○ Tipp: Verwende input() für die Benutzereingabe und prüfe, ob das
# eingegebene Datum gültig ist. Falls nicht, soll der Benutzer eine neue Eingabe
# machen.

#!!Möglichkeit eins!!#

import datetime

user_input = input('Gebe bitte das datum ein was du vergleichen möchtest(dd.mm.yyyy)')

def tage_bis_jahresende():
    user_date = datetime.datetime.strptime(user_input, '%d.%m.%Y')
    date_today = datetime.datetime.today()
    differenz = user_date - date_today
    print(f'Die Differenz von deinem Datum {user_date} zum Aktuellen Datum sind: {differenz}')

tage_bis_jahresende()

##!! Möglichkeit 2. !!##


import datetime

user_input = input('Gebe bitte das datum ein was du vergleichen möchtest(dd.mm.yyyy)')

def tage_bis_jahresende():
    #Das .date(), wandelt den input was eingeben wurden ist in das richtige format.
    user_date = datetime.datetime.strptime(user_input, '%d.%m.%Y').date()
    date_today = datetime.date.today()
    differenz = user_date - date_today
    #Hierbei ist egal ob im print {user_input} oder der {user_date} genommen wird.
    print(f'Die Differenz von deinem Datum {user_input} zum Aktuellen Datum sind: {differenz}')

tage_bis_jahresende()



#4. Wochentag berechnen:
#○ Erstelle eine Funktion wochentag_berechnen(), die den Wochentag für ein
#beliebiges eingegebenes Datum berechnet und ausgibt (z. B. Montag,
#Dienstag usw.).



import datetime

user_date = input('Gib bitte ein datum ein ')


def weekday():
    date_today = datetime.datetime.strptime(user_date, '%d.%m.%Y')
    day_week = date_today.strftime('%A')
    print(f'Es ist: {day_week}')

weekday()



import datetime
import locale

locale.setlocale(locale.LC_TIME, 'de_DE.UTF-8')

user_date = input('Gib bitte ein Datum ein (dd.mm.yy): ')


def weekday():
    date_today = datetime.datetime.strptime(user_date, '%d.%m.%y')
    day_week = date_today.strftime('%A')
    print(f'Der {user_date} ist ein {day_week}.')

weekday()




#5. Zeitverschiebung berechnen:
#○ Implementiere eine Funktion zeit_in_zukunft(), die eine Eingabe von
#Minuten, Stunden oder Tagen vom Benutzer entgegennimmt und das Datum
#und die Uhrzeit berechnet, die nach dieser Zeitspanne liegt.
#○ Beispiel: Wenn der Benutzer 2 Stunden eingibt und die aktuelle Zeit 14:00
#ist, sollte das Programm 16:00 ausgeben.

##!!!. Erster Versuch ohne hilfe, mit nachschauen über google. !!! ##

import datetime

user_input = input('Bitte gebe deine Stunden Zahl ein (h): ')

def time_in_future():
    time_current = datetime.datetime.now()
    user_hours = datetime.datetime.strftime(user_input, '%x')
    addition = time_current + user_hours
    print(f'In {user_input} Stunde/n ist es {addition}')

time_in_future()

###!!!. Mit hilfe zur verbesserung. !!!###


import datetime

user_input = int(input('Bitte gebe deine Stunden Zahl ein (h): '))

def time_in_future():
    time_current = datetime.datetime.now()
    future_time = time_current + datetime.timedelta(hours=user_input)
    print(f'In {user_input} Stunde/n ist es {future_time.strftime('%H:%M:%S')}')
    
    
time_in_future()








