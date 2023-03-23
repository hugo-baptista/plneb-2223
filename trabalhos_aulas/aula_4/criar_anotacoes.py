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
    start = re.search(r"^(<.+?>)*", line)
    line = re.sub(r"^(<.+?>)*", r" ", line)
    end = re.search(r"(<.+?>)*$", line)
    line = re.sub(r"(<.+?>)*$", r" ", line)
    line = re.sub(r"(<.+?>)", r" \1 ", line)
    new_line = ""
    new_line += start[0]
    for word in line.split():
        if word.lower() in termos:
            new_line += f"<a href title=\"{dicionario.get(word.lower())}\">{word}</a>"
        elif word in termos:
            new_line += f"<a href title=\"{dicionario.get(word)}\">{word}</a>"
        else:
            new_line += word
        new_line +=" "
    new_line += end[0]
    new_line += "\n"
    html_text += new_line

html = open("trabalhos_aulas/aula_4/html_anotado/LIVRO-Doenças-do-Aparelho-Digestivos.html", "w", encoding="utf-8")
html.write(html_text)