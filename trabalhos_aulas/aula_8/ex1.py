#! /usr/bin/env python3

# Imports
import re, spacy

# Carregar língua no spaCy
nlp = spacy.load("pt_core_news_md")

# Documento
document1 = '''O Nadador-Salvador é o profissional que exerce a atividade de salvamento em meio-aquático, onde se incluem as praias, as piscinas e outros locais onde ocorram práticas aquáticas, utilizando os meios, procedimentos e técnicas adequados. Este profissional possui, igualmente, competências para o exercício de atividades relacionadas com informação, prevenção, socorrismo e suporte básico de vida, em qualquer circunstância, no âmbito do salvamento aquático.'''

document2 = '''A hipótese de Cristiano Ronaldo voltar ao futebol inglês pode não estar totalmente afastada, com o portal 'Football London' a associar o português ao Chelsea. Os rumores sobre a vontade de CR7 deixar o Al Nassr já no próximo verão têm subido de tom nas últimas semanas e, se em Espanha se especula sobre uma remota chance de voltar ao Real Madrid, em Inglaterra são os blues apontados como principais interessados.'''

# Árvore documental
texto = nlp(document2)

# .sents -> get sentences
num_frase=0
for frase in texto.sents:
    num_frase+=1
    print(f'\nFrase {num_frase}: {frase}')
    # .ents -> get entities
    num_entidade=0
    for entidade in frase.ents:
        num_entidade+=1
        print(f'\tEntidade {num_entidade}: {entidade} | Tipo: {entidade[0].ent_type_}')
    for palavra in frase:
        # POS - Part of Speech
        print(f'\tPalavra: {palavra.text} | Lema: {palavra.lemma_} | POS: {palavra.pos_} | Tag: {palavra.tag_} | Dependência: {palavra.dep_}')

# Exercício 1 - Dado um texto, ir buscar os verbos e calcular as suas ocorrências
contador = {}
for palavra in texto:
    if palavra.pos_=="VERB":
        try:
            contador[palavra.lemma_] = contador[palavra.lemma_] + 1
        except:
            contador[palavra.lemma_] = 1
print(contador)