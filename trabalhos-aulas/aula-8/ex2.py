from collections import Counter
import spacy
nlp = spacy.load("pt_core_news_md")
nlp.max_length = 1300000

# Exercício 2 - Ver o top 10 de personagens (entitites) pelas suas ocorrências
documento=open('./trabalhos-aulas/aula-8/livros/os_maias.txt', 'r').read()
texto = nlp(documento)

nomes = []
lugares = []
entidades_lista = []
for entidade in texto.ents:
    entidades_lista.append(entidade.text)
    if entidade[0].ent_type_ == 'PER':
        nomes.append(entidade.text)
    if entidade[0].ent_type_ == 'LOC':
        lugares.append(entidade.text)

top=10
personagens = Counter(nomes)
print(f'Top {top} personagens: {personagens.most_common(top)}')
localidades = Counter(lugares)
print(f'Top {top} localidades: {localidades.most_common(top)}')
entidades = Counter(entidades_lista)
print(f'Top {top} entidades: {entidades.most_common(top)}')