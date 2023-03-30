from flask import Flask

head = open("trabalhos_aulas/aula_6/html/head.html", "r").read()

navbar = open("trabalhos_aulas/aula_6/html/navbar.html", "r").read()

tail = open("trabalhos_aulas/aula_6/html/tail.html", "r").read()

def create_html_page(content):
    return f"""
{head}

{navbar}

{content}

{tail}
"""

app = Flask(__name__)

@app.route("/")
def home():
    return create_html_page("""
<p>Home Placeholder</p>
""")

@app.route("/termos")
def termos():
    return create_html_page("""
<p>Termos Placeholder</p>
""")

@app.route("/pesquisar")
def pesquisar():
    return create_html_page("""
<p>Pesquisar Placeholder</p>
""")

@app.route("/tabela")
def tabela():
    return create_html_page("""
<p>Tabela Placeholder</p>
""")

app.run(host="localhost", port=3000, debug=True)