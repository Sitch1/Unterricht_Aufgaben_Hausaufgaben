


# Wörterbuch (dictionary): Das ist eine Sammlung von deutschen Wörtern als Schlüssel und deren Übersetzungen ins Schwedische als Werte.
dictionary = {
    "Hallo": "Hej", 
    "tschüss": "hej då",
    "Guten Morgen": "God Morgon",
    "Guten Abend": "God afton"
    }

# Benutzereingabe (input): Der Code fordert den Benutzer auf, ein Wort einzugeben, das übersetzt werden soll.
user_input = input("Gebe hier dein Wort ein was du übersetzen möchtest?: ").strip().capitalize() 

# .strip() entfernt überflüssige Leerzeichen am Anfang und Ende der Eingabe.
# capitalize() sorgt dafür, dass nur der erste Buchstabe des eingegebenen Wortes großgeschrieben wird.

# Übersetzung: Der Code sucht dann im Wörterbuch nach dem eingegebenen Wort (user_input) und gibt die Übersetzung aus.
print(f"Die Übersetzung des Wortes {user_input} lautet {dictionary[user_input]}")

#Ausgabe: Die Übersetzung wird formatiert und dem Benutzer angezeigt.

# Ein einfacher Fehler, der auftreten könnte, ist, wenn der Benutzer ein Wort eingibt, 
# das nicht im Wörterbuch steht. In diesem Fall würde der Code einen Fehler auslösen, 
# weil der Schlüssel nicht gefunden werden kann. Man könnte das mit einer Fehlerbehandlung verbessern.






my_dict = {"apfel": "Apple", "wörterbuch": "dictionary"}
my_userinput = input("Gib ein deutsches Wort ein: ")
if my_userinput in my_dict:
    print(f"Die Übersetzung zu {my_userinput} ist {my_dict[my_userinput]}")
else:
    actual_translation = input(
        "Das Wort gibt es noch nicht, gib die engl. Übersetzung ein: "
    )
    my_dict[my_userinput] = actual_translation
    print(f"Die Übersetzung zu {my_userinput} ist {my_dict[my_userinput]}")