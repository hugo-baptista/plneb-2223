import re
import json

file = open("plneb-2223/data/dicionario_medico.xml", "r", encoding="utf-8")
text = file.read()

# Remover Form Feed
text = re.sub(r"\n</?page.*>", r"", text)

# Remover <text...> e </text>
text = re.sub(r"</?text.*?>", r"", text)

# Marcar os termos
text = re.sub(r"<b>", r"#T=", text)

# Remover restantes <...>
text = re.sub(r"<.*?>", r"", text)

# Marcar explicações
text = re.sub(r"\n([^\#\s].+)", r"\n#E=\1", text)

# Colapsar explicações
text = re.sub(r"(#E=.+)\n#E=(.+)", r"\1 \2", text)
while re.search(r"#E=.+\n#E=.+", text) != None:
    text = re.sub(r"(#E=.+)\n#E=(.+)", r"\1 \2", text)

# Procurar Termos (1º grupo) e suas Explicações (2º grupo)
entries = re.findall(r"#T=(.+)\n#E=(.+)", text)

# Criar um dicionário com os Termos como keys e as Explicações como valores
dicionario = {}
for entry in entries:
    dicionario[entry[0]] = entry[1]

jsonfile = open("trabalhos-aulas/aula-4/dicionario.json", "w", encoding="utf-8")

json.dump(dicionario, jsonfile, ensure_ascii=False, indent=4)