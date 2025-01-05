



my_dict = {
    "Repo": "repo(repository): Ein Ort, an dem ein Projekt gespeichert wird. Cloud basierte Platform. ",
    "Branch": "branch: Eine Kopie des Hauptprojekts,in der Änderungen vorgenommen werden kann, ohne das Original zu beeinflussen.",
    "Commit": "commit: Ein Snapshot einer Änderungen. .",
    "Pull Request (PR)": "(PR): Eine Anfrage, Änderungen von einem Branch in einen anderen (meist den Hauptbranch) zu übernehmen. Es ist wie ein Vorschlag, den andere überprüfen können.",
    "Merge": "Das Zusammenführen von Änderungen aus verschiedenen Branches. Stell dir vor, du bringst zwei Wege wieder zusammen.",
    "Clone": "Eine Kopie eines Repositories auf deinem Computer. Das ist, als würdest du eine Datei von einer Webseite auf deinen PC herunterladen.",
    "Fork": "Eine Kopie eines Repositories, die du verändern kannst, ohne die Originalversion zu beeinflussen. Das ist, als würdest du ein Buch kopieren, um Notizen darin zu machen.",
    "Issue": "Ein Problem oder eine Aufgabe, die im Projekt bearbeitet werden muss. Es ist wie eine To-Do-Liste für das Projekt.",
    "Collaborator": "Jemand, der an einem Repository mitarbeitet. Stell dir vor, es ist ein Teammitglied, das an einem Projekt beteiligt ist.",
    "README": "Eine Datei, die Informationen über dein Projekt enthält. Es ist wie eine Anleitung oder eine Zusammenfassung.",
    "Tag": "Ein markierter Punkt in der Historie eines Repositories, meist für wichtige Versionen. Es ist wie ein Lesezeichen in einem Buch.",
    "Action": "Automatisierte Aufgaben, die ausgeführt werden, wenn bestimmte Ereignisse im Repository auftreten. Das ist wie ein Roboter, der für dich Dinge erledigt.",

}

x = my_dict.keys()
print(x)

while True:
    print("\nVerfügbare Befehle: ")
    for key in my_dict.keys():
        print(key)

    my_userinput = input("\nGib dein Git-Befehl ein für weitere Informationen: ").strip().capitalize().lower()
    sum = 0



    if my_userinput in my_dict:
        print(f"\nDer Befehl {my_userinput} bedeutet: {my_dict[my_userinput]}")
    else:
        print("Der Befehl '{my_userinput}' ist nicht bekannt")

    
    
    continue_input = input("\nMöchtest du weitermachen? (ja/nein): ").strip().lower()
    if continue_input != "ja":
        print("Programm beendet")
        break