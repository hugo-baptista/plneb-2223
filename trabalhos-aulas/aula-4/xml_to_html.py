import re

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

entries = re.findall(r"#T=(.+)\n#E=(.+)", text)
print(entries)


html = open("trabalhos-aulas/aula-4/dicionario_medico.html", "w", encoding="utf-8")

header = """
<html>
    <head>
        <link rel="stylesheet" href="styles.css" />
        <meta charset='uft-8' />
    </head>
"""

body = """
    <body>
        <table>
            <tr>
                <th>Termo</th>
                <th>Explicação</th>
            </tr>
"""
for entry in entries:
    body += f"""
            <tr>
                <td>{entry[0]}</td>
                <td>{entry[1]}</td>
            </tr>
"""
    
body += """
        </table>
    </body>
"""

footer = """
</html>
"""

html.write(header+body+footer)