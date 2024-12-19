# Was macht import #
    # import ist eine befehl um in pyhton3 bestimmte funktionen und klassen aus einem Modul(ordner mit mehrern unter ordner)
    # z.B mit Datum oder Uhrzeiten zu arbeiten.

# Was ist datetime #
    #Was macht datetime?

    # Ermittelt das aktuelle Datum und die Uhrzeit:
    #     Zum Beispiel: datetime.now() gibt das aktuelle Datum und die Uhrzeit zurück.

    # Rechnet mit Zeit:
    #     Du kannst Zeitdifferenzen berechnen, also wie viele Tage, Stunden oder Minuten zwischen zwei Zeitpunkten liegen.

    # Bearbeitet Daten und Zeiten:
    #     Du kannst mit Datumsangaben und Uhrzeiten rechnen, z. B. Tage hinzufügen oder abziehen.

        #!!!. Beispiel . !!!

    #Aktuelles Datum und Uhrzeit anzeigen:
        import datetime
        
        jetzt = datetime.datetime.now() # Holt das aktuelle Datum und die Uhrzeit
        print(jetzt)
        print = (jetzt)

    #Nur das heutige Datum bekommen:
        import datetime

        heute = datetime.date.today()  # Holt nur das heutige Datum
        print(heute)

    #Zeitberchnung (z.B. 3 Tage plus rechnen von heute)
        import datetime

        jetzt =datetime.date.today()
        berechnung = jetzt + datetime.timedelta(days=2) # 2 Tage hinzufügen
        print(berechnung)