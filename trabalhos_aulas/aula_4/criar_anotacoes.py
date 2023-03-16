import re
import json

file = open("plneb-2223/data/dicionario_medico.xml", "r", encoding="utf-8")

jsonfile = open("trabalhos_aulas/aula_4/dicionario.json", "r", encoding="utf-8")

dicionario = json.load(jsonfile)

print(dicionario["ãa"])