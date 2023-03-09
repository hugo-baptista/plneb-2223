import re

file = open("plneb-2223/data/dicionario_medico.txt", "r", encoding="utf-8")
text = file.read()

remove_term_ff = re.sub(r"\f(.+\n[A-ZÁÉÍÓÚÀÂÊÔÃÕÇ])", r"\1", text)
remove_explication_ff = re.sub(r"\n\f+", "", remove_term_ff)
mark_terms = re.sub(r"\n\n(.+)", r"\n\n#T=\1", remove_explication_ff)
mark_explications = re.sub(r"\n([^#\s].+)", r"\n#E=\1", mark_terms)
collapse_explications = re.sub(r"(#E=.+)(?:\n#E=(.+))+", r"\1 \2", mark_explications)
remove_marks = re.sub(r"#[TE]=", r"", collapse_explications)
entries = re.findall(r"\n\n(.+)\n(.+)", remove_marks)

newfile1 = open("trabalhos_aulas/aula_3/v3/1_no_term_ff.txt", "w", encoding="utf-8")
newfile1.write(remove_term_ff)
newfile2 = open("trabalhos_aulas/aula_3/v3/2_no_explication_ff.txt", "w", encoding="utf-8")
newfile2.write(remove_explication_ff)
newfile3 = open("trabalhos_aulas/aula_3/v3/3_final.txt", "w", encoding="utf-8")
newfile3.write(remove_marks)



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