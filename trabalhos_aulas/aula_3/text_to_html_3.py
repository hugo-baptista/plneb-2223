import re

file = open("plneb-2223/data/dicionario_medico.txt", "r", encoding="utf-8")
text = file.read()



'''
html = open("trabalhos_aulas/aula_3/dicionario_medico_3.html", "w", encoding="utf-8")

header = """
<html>
<head>
<link rel="stylesheet" href="styles.css" />
<meta charset='uft-8' />
</head>
<body>
"""

body = """
<table>
<tr>
<th>Termo</th>
<th>Explicação</th>
</tr>
"""
for entry in entries:
    body += "<tr>"
    body += f"<td>{entry[0]}</td>"
    body += f"<td>{entry[1]}</td>"
    body += "</tr>"
body += "</table>"

footer = """
</body>
</html>
"""

html.write(header+body+footer)
'''