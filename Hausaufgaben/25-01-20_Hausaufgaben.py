# Aufgabe: Flask-App beschreiben und erweitern

# Aufgabe:
# 1. Beschreibe in eigenen Worten:
# ○ Was passiert, wenn die Route / aufgerufen wird?
# Antwort: Es wird das ausgeben was mit als def hinterlegt ist. 
#          z.B. (def about_func():) gibt den ein print wieder mit dem text:
#          Mein name ist ... und interesiere mich für die Webentwicklung

# ○ Was geben die Routen /info, /team, /hilfe und /kontakt zurück?
# Antwort: So wie in Aufgabe 1.

# ○ Warum wird app.run(port=5000) verwendet?
# Antwort: port:5000 ist unverschlüsselt und wird im lokalen netzwerk verwendet für HTTP
#          Sicherer wäre aber port:5001, diese ist verschlüsselt.


# 2. Starte die App auf deinem Rechner, rufe die Routen im Browser auf und überprüfe
# die Ausgaben.
# 3. Überlege, welche weiteren Inhalte du einer API hinzufügen könntest.



# Teil 2: Eigene GET-Routen hinzufügen

from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, World! Hier ist ein einfacher versuch API über Win zu startet"

@app.route("/about")
def about_func():
    return "Mein name ist ... und interesiere mich für die Webentwicklung"

@app.route("/projekt")
def projekt_func():
    return "Mein aktuelles Projekt ist eine Flask-API für Anfänger"

@app.route("/news")
def news_func():
    return "Heute lernen wir, wie man APIs mit Flask erstellt!"

@app.route("/feedback")
def feedback_func():
    return "Wir freuen uns auf dein Feedback und Muster@muster.de"

@app.route("/support")
def spport_func():
    return "Besuche unseren Support-Seite unter support.example.com"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)