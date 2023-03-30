from flask import Flask

head = """
<!DOCTYPE html>
<html>
    <head>
        <title>My Flask Application</title>
        <link rel="stylesheet" href="static/style.css">
    </head>
<body>
"""

navbar = """
<div class="navbar-back">
    <div class="navbar">
        <h1>Flask Server</h1>
        <div class="links">
            <a href="http://localhost:3000/">Home</a>
            <a href="http://localhost:3000/termos">Termos</a>
            <a href="http://localhost:3000/pesquisar">Pesquisar</a>
            <a href="http://localhost:3000/tabela">Tabela</a>
        </div>
    </div>
</div>
"""

tail = """
</body>
</html>
"""

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