import re
import json

# Carregar o dicionário
jsonfile = open("trabalhos_aulas/aula_4/dicionario.json", "r", encoding="utf-8")
dicionario = json.load(jsonfile)

# Abrir o ficheiro HTML
file = open("trabalhos_aulas/aula_4/html_original/LIVRO-Doenças-do-Aparelho-Digestivos.html", "r", encoding="utf-8")
text_lines = file.read().splitlines()

termos = dicionario.keys()

html_text =""
for line in text_lines:
    words = re.sub(r"<.+?>", r" ", line)
    for word in re.findall(r"\b.+?\b", words):
        if word.lower() in termos:
            line = re.sub(word, r"<a href title=" + dicionario.get(word.lower()) + r">" + word + "</a>", line)
        elif word in termos:
            line = re.sub(word, r"<a href title=" + dicionario.get(word) + r">" + word + "</a>", line)
    html_text+=line+"\n"

html = open("trabalhos_aulas/aula_4/html_anotado/LIVRO-Doenças-do-Aparelho-Digestivos.html", "w", encoding="utf-8")
html.write(html_text)