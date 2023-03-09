import re

file = open("plneb-2223/data/dicionario_medico.txt", "r", encoding="utf-8")
text = file.read()

remove_form_feed = re.sub(r"\f", "", text)
mark_terms = re.sub(r"\n\n(.+)", r"\n\n#T=\1", remove_form_feed)
mark_explications = re.sub(r"\n([^#\s].+)", r"\n#E=\1", mark_terms)
correct_explications = re.sub(r"(#T=.+)\n\n#T=(.+)", r"\1\n#E=\2", mark_explications)
remove_new_lines = re.sub(r"(#E=.+)(?:\n#E=(.+))+", r"\1 \2", correct_explications)
remove_marks = re.sub(r"#[TE]=", r"", remove_new_lines)
entries = re.findall(r"\n\n(.+)\n(.+)", remove_marks)

html = open("trabalhos_aulas/aula_3/dicionario_medico_2.html", "w", encoding="utf-8")

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