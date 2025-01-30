
    
    # Aufgabe 1: Einfache Flask-GET-Anfragen

    # Ziel: Lerne, wie du eine Flask-App erstellst, GET-Routen definierst und URL-Paramet
    # verarbeitest.
    # Schritte:
    # 1. Erstelle eine Flask-App mit mindestens drei GET-Endpunkten.
    # 2. Die GET-Anfragen sollen unterschiedliche Funktionen ausführen:
    # ○ Route 1: /brand/<id>?type=<type>&condition=<condition>
    # ■ Beispiel: http://localhost:6060/brand/10?type=clothes&condition=new
    # ■ Ausgabe: "Brand-ID: 10, Type: clothes, Condition: new"
    # ○ Route 2: /product/<product_id>
    # ■ Beispiel: http://localhost:6060/product/123
    # ■ Ausgabe: "Product-ID: 123"
    # ○ Route 3: /search
    # ■ Beispiel: http://localhost:6060/search?query=shoes
    # ■ Ausgabe: "Searching for: shoes"

    # 3. Bonus: Implementiere eine Validierung der Parameter (z. B. id muss eine Zahl sein).
    # 4. Teste die Routen mit Postman oder deinem Browser.
    # Abgabe:
    # ● Eine funktionierende Flask-App, die auf Port 6060 läuft.
    # ● Klar definierte Routen mit lesbaren Rückgabe


    # 1. Erstelle eine Flask-App
from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
    return "Willkomen, hier sind einfach Flask-Get-Anfragen."

@app.route("/brand/<id>", methods=["GET"])
def get_item(id):
    clothes = request.args.get("clothes")
    color = request.args.get("color")
    condition = request.args.get("condition")
    return f"Die Brand-ID: {id}, Clothes: {clothes} the Color: {color} and condition is: {condition} "


@app.route("/product/<product_id>", methods=["GET"])
def get_product(product_id):
    return f"Product-ID: {product_id}"

@app.route("/search", methods=["GET"])
def get_search():
    query = request.args.get("query")
    return f"Das Prdoukt: {query}"  


if __name__ == "__main__":
    app.run(port=6060, debug=True)



