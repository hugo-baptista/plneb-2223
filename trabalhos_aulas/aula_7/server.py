from flask import Flask, render_template, request
import json

app = Flask(__name__)

try:
    file = open('./trabalhos_aulas/aula_7/database_modified.json')
except:
    file = open('./trabalhos_aulas/aula_7/database_original.json')
database = json.load(file)
file.close()

notfound={
    "des": "Not in the dictionary",
    "en": "Not in the dictionary"
}

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/terms")
def terms():
    return render_template("terms.html", designations=database.keys())

@app.route("/term/<t>")
def term(t):
    return render_template("term.html", designation=t, value=database.get(t, notfound))

@app.route("/term", methods=["POST"])
def add_term():
    term = request.form["term"]
    description = request.form["description"]

    if term not in database:
        database[term]={"des": description}

        file = open('./trabalhos_aulas/aula_7/database_modified.json', "w")
        json.dump(database, file, ensure_ascii=False, indent=4)
        file.close()
        return render_template("terms.html", designations=database.keys(),
                               info="The term " + term + " was added!")

    return render_template("terms.html", designations=database.keys(),
                           info="The term " + term + " already exists!")

@app.route("/terms/search")
def termssearch():
    return render_template("terms-search.html")

app.run(host="localhost", port=3000, debug=True)