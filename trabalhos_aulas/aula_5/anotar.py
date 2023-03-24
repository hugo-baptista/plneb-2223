import json, re

dicio_f = open("trabalhos_aulas/aula_5/dicionario.json")
dicio = json.load(dicio_f)

livro_f = open("trabalhos_aulas/aula_5/LIVRO-Doenças-do-Aparelho-Digestivo.txt")
text = livro_f.read()

blacklist = {"e", "de", "são"}

nova_lista = dicio.keys() - blacklist

nova_lista.remove("L+")
nova_lista.add("L\+")

expressao = r"\b(" + "|".join(nova_lista) + r")\b"

def anotaTermo(match):
    """
    O input da função é automaticamente inserido, mas ele é um objeto do tipo match,
    no qual o termo de índice 0 é toda a expressão encontrada, o índice 1 o 1º grupo, índice 2 o 2º, etc.
    """
    termo=match[1]
    return f"<a href='' data-toggle='tooltip' title='{dicio.get(termo)}'>{termo}</a>"

text = re.sub(expressao, anotaTermo, text, flags=re.I)
text = re.sub(r"\f", "<hr>", text)
text = re.sub(r"\n", "<br>", text)

dicio_f.close()
livro_f.close()

header = """
<html>
<head>
<meta charset='uft-8' />
</head>
<body>
"""

body = ""
body += text

footer = """
</body>
</html>
"""

html = open("trabalhos_aulas/aula_5/res.html", "w", encoding="utf-8")
html.write(header+body+footer)