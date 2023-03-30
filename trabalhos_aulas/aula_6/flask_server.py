from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html", title="Welcome")

@app.route("/engenharia")
def termos():
    return render_template("engenharia.html")

@app.route("/egua")
def pesquisar():
    return render_template("egua.html")

@app.route("/elefante")
def tabela():
    return render_template("elefante.html")

app.run(host="localhost", port=3000, debug=True)