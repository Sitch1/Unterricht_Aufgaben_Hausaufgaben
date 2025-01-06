



Funktionen bei Variablen

Einer Funktion wird also nach dem Funktionsnamen in den folgenden Klammern Werte (und Anweisungen) mit übergeben. Unserer Funktion print(kursname) bekommt also in der Klammer die Variable mit übergeben und weiß somit, was auf dem Bildschirm ausgegeben werden soll.

Es muss allerdings nicht immer einer Funktion weitere Werte und Anweisungen in der Klammer mit übergeben werden. Wird print() einfach mit einer leeren Klammer aufgerufen, dann erhalten wir als Ergebnis eine Leerzeile ausgegeben.

Schauen wir uns eine andere Funktion neben print() an. Zum Bestimmen der Länge eines Strings gibt es die Funktion len(x). Als Information erhalten wir hier die Anzahl der enthaltenen Zeichen. Bei len handelt es sich um die Abkürzung des englischen Worts „length“. Allerdings müssen wir irgendwas mit dieser Information machen. Lassen wir uns diese ausgeben:

kursname = 'Python-lernen.de'
print(len(kursname))


Funktionen können also innerhalb anderer Funktionen genutzt werden.

Funktionen sind unabhängig. Wir können die Funktionen nicht nur für Strings nutzen!

Funktionen sind soweit einfach verständlich. Was aber sind Methoden und was können wir damit bei Variablen anstellen?
Methoden bei Variablen/Strings

Ändern wir unsere Sichtweise. Wenn wir unsere Variable als ein Objekt ansehen, dann kann dieses Objekt verschiedene Möglichkeiten bieten. Ich schreibe hier bewusst Möglichkeiten. Warum? Wenn wir es aus objektorientierter Sicht ansehen, stecken wir schon voll in der objektorientierten Programmierung (OOP). Diese wird später im Detail besprochen. Grundlegend ist, dass bei der OOP die Punktschreibweise genutzt wird. Wir haben unser Objekt, was an erster Stelle steht und wollen hier für dieses Objekt etwas abfragen bzw. eine festgelegte Aktion ausführen: Die Aktion wird über einen Punkt direkt dahinter gepackt.

objektname.aktion

Beispielsweise könnten wir unseren in der Variablen gespeicherten Text komplett in Kleinschreibung erhalten.

kursname = 'www.Python-lernen.de'
kursname.lower()

Wer sich jetzt denkt, das fühlt sich doch an wie eine Funktion, die einfach alles in Kleinbuchstaben umwandelt, liegt nicht wirklich falsch. Es ist einfach eine andere Sichtweise – sprich die objektorientierte Sichtweise. Und somit wird die objektorientierte Schreibweise notwendig.

Die wirkliche Kunst liegt darin zu wissen, welche Objekte welche Möglichkeiten (sprich Methoden) bieten.