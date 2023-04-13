from flask import Flask, render_template
import json

app = Flask(__name__)

file = open('./trabalhos_aulas/aula_5/dicionario_pt_en_completo.json')
dictionary = json.load(file)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/terms")
def terms():
    return render_template("terms.html", designations=dictionary.keys())

@app.route("/term/<t>")
def term(t):
    return render_template("term.html", designation=t, value=dictionary.get(t, "404 Not Found"))

@app.route("/terms/search")
def termssearch():
    return render_template("terms-search.html")

app.run(host="localhost", port=3000, debug=True)