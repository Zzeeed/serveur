import json
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def accueil():
    return render_template("accueil.html")


@app.route("/formulaire")
def formulaire():
    return render_template("formulaire.html")


@app.route("/traitement", methods=["POST"])
def traitement():
    nom = request.form["nom"]
    film = request.form["film"]
    return render_template("resultat.html", nom=nom, film=film)


@app.route("/videotheque")
def videotheque():
    with open("videotheque.json", encoding="utf-8") as f:
        donnees = json.load(f)
    return render_template("videotheque.html", videotheque=donnees)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
