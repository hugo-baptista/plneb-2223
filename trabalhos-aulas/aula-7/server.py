from flask import Flask, render_template, request
import json, re

app = Flask(__name__)

try:
    file = open('./trabalhos-aulas/aula-7/database_modified.json')
except:
    file = open('./trabalhos-aulas/aula-7/database_original.json')
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

@app.route("/terms/search")
def search():
    text = request.args.get("text")
    term_list = []
    if text:
        for term, dic in database.items():
            # if text in term or text in dic["des"]:
            if re.search(text, term, flags=re.I) or re.search(text, dic["des"], flags=re.I):
                term_list.append((term, dic["des"]))
    return render_template("search.html", matched=term_list)

@app.route("/term", methods=["POST"])
def add_term():
    term = request.form["term"]
    description = request.form["description"]

    if term not in database:
        database[term]={"des": description}

        file = open('./trabalhos-aulas/aula-7/database_modified.json', "w")
        json.dump(database, file, ensure_ascii=False, indent=4)
        file.close()
        return render_template("terms.html", designations=database.keys(),
                               info_add="The term " + term + " was added!")

    return render_template("terms.html", designations=database.keys(),
                           info_add="The term " + term + " already exists!")

@app.route("/term/<term>", methods=["DELETE"])
def delete_term(term):
    if term in database:
        old_value = database[term]

        del database[term]

        file = open('./trabalhos-aulas/aula-7/database_modified.json', "w")
        json.dump(database, file, ensure_ascii=False, indent=4)
        file.close()

        return {"success": True, "deleted": {term: old_value}}

    return {"success": False, "info": "The entry " + term + " does not exists!"}

@app.route("/terms/search")
def termssearch():
    return render_template("terms-search.html")

@app.route("/table")
def table():
    return render_template("table.html")

app.run(host="localhost", port=3000, debug=True)