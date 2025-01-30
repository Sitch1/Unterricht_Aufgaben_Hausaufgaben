
    # Flask-App mit Nutzeraktionen

    # Erstelle eine Flask-App, die auf GET-Routen reagiert und verschiedene Nutzeraktionen
    # simuliert.
    # Beschreibung:
    # Hintergrund: Du hast eine Liste von Nutzern mit id, name und email:
    # users = [

    # {"id": 1, "name": "Alice", "email": "alice@example.com"},
    # {"id": 2, "name": "Bob", "email": "bob@example.com"},
    # {"id": 3, "name": "Charlie", "email": "charlie@example.com"}

    # ]

    
    # ○ Route 1: /user/<id>
    # Beispiel: http://localhost:6060/user/1
    # Rückgabe: Nutzerdetails wie {"id": 1, "name": "Alice", "email":
    # "alice@example.com"}
    # ○ Route 2: /login/<id>
    # Beispiel: http://localhost:6060/login/2
    # Rückgabe: "User Bob successfully logged in!" (oder Fehler, falls ID nicht
    # existiert)
    # ○ Route 3: /search?name=<name>
    # Beispiel: http://localhost:6060/search?name=Charlie
    # Rückgabe: "Found user: Charlie" oder "No user found with name: Charlie"


# 1. Erstelle eine Flask-App
from flask import Flask, request
from users_list import users

app =Flask("__name__")

# 2. Erstellung einer Users-Liste
users = [
    {"id": 1, "name": "Alice", "email": "alice@example.com", "passwort": "Go1"},
    {"id": 2, "name:": "Bob", "email": "Bob@example.com", "passwort": "Go2"},
    {"id": 3, "name": "Charlie", "email": "Charlie@example.com","passwort": "Go3"}
]
@app.route("/", methods=["GET"])
def get_brand():
    return f"Welcome to our users api!"



# ○ Route 1: /user/<id>
    # Beispiel: http://localhost:6060/user/1
    # Rückgabe: Nutzerdetails wie {"id": 1, "name": "Alice", "email":
    # "alice@example.com"}
@app.route("/users/<int:user_id>", methods=["GET"])
def get_user_by_id(user_id):
    final_user = None

    for user in users:
        if user["id"] == user_id:
            final_user = user

    
    if final_user == None:
        return "User could not a found!"
    
    return f"The User is: {final_user}"



# ○ Route 2: /login/<id>
    # Beispiel: http://localhost:6060/login/2
    # Rückgabe: "User Bob successfully logged in!" (oder Fehler, falls ID nicht
    # existiert)
@app.route("/users/login/<id>", methods=["POST"])
def login():
    credentials = request.get_json()
    username = credentials["username"]
    password = credentials["password"]
    # Now you can access the user based on email and password and return if valid credentials
   
    final_user = None
    for user in users:
        if u["username"] == username:
            final_user = user

    if final_user == None:
        return "User could not be found"
    
    if final_user["password"] != password:
        return f"User with username {username} exists but the password {password} is incorrect"

    return f"Hallo {credentials} {username} {password}"

@app.route("/users/signup", methods=["POST"])
def signup():
    new_user = request.get_json()
    if(
        "username" not in new_user
        or "firstName" not in new_user
        or "password" not in new_user
        or "familyName" not in new_user
    ):
        return "Parameters are missing", 400




# Route 3: /search?name=<name>
# Beispiel: http://localhost:6060/search?name=Charlie
# Rückgabe: "Found user: Charlie" oder "No user found with name: Charlie"
@app.route("/search", methods=["GET"])
def get_user_by_name():
    final_user = None
    name = request.args.get("name")
    for u in users:
        if u["firstName"] == name:
            final_user = u

    if final_user == None:
        return "User could not be found "

    return f"The User is {final_user}"



if __name__ == "__main__":
    app.run(debug=True, port=6060)