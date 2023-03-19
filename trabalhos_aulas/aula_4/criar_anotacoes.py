import re
import json

# Carregar o dicionário
jsonfile = open("trabalhos_aulas/aula_4/dicionario.json", "r", encoding="utf-8")
dicionario = json.load(jsonfile)

# Abrir o ficheiro HTML
file = open("trabalhos_aulas/aula_4/html_original/LIVRO-Doenças-do-Aparelho-Digestivos.html", "r", encoding="utf-8")
text_lines = file.read().splitlines()

termos = dicionario.keys()



html = open("trabalhos_aulas/aula_4/livro_anotado.html", "w", encoding="utf-8")
html.write(header+body+footer)