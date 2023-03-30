from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html", title="Welcome")

@app.route("/termos")
def termos():
    return render_template("termos.html")

@app.route("/pesquisar")
def pesquisar():
    return render_template("pesquisar.html")

@app.route("/tabela")
def tabela():
    return render_template("tabela.html")

app.run(host="localhost", port=3000, debug=True)