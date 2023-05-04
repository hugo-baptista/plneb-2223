from collections import Counter
import spacy
nlp = spacy.load("pt_core_news_md")
nlp.max_length = 1300000
from itertools import combinations

# Exercício 3 - "Best friends"
documento=open('./trabalhos_aulas/aula_8/livros/os_maias.txt', 'r').read()
texto = nlp(documento)

entidades_matriz = []
for frase in texto.sents:
    entidades_lista = []
    for entidade in frase.ents:
        if (entidade[0].ent_type_=='PER' or entidade.text in ['Harry', 'Harry Potter']) and entidade.text not in entidades_lista:
            entidades_lista.append(entidade.text)
    if len(entidades_lista)>1:
        entidades_matriz.append(entidades_lista)

combinacoes = []
for entidades_lista in entidades_matriz:
    for combinacao in combinations(entidades_lista, 2):
        combinacao_ordenada = tuple(sorted(combinacao))
        combinacoes.append(combinacao_ordenada)

top=10
best_friends = Counter(combinacoes)
print(f'Top {top} best friends: {best_friends.most_common(top)}')