# Resolução do exercício da Aula 5

## Anotação
Inicialmente, realizou-se o execício da aula passada, partilhando diversas formas de o realizar. Como eu fiz um que anotava um ficheiro HTML, guardei no ficheiro "anotar.py" uma solução que lê de um ficheiro TXT, guardando a resposta no ficheiro "res.html".

## Tradução
Depois de instalado o package "deep-transator", criei o programa "translate.py" que cria um dicionário com as mesmas keys que o anterior, mas com os seus values sendo um dicionário com 3 entradas: "des", que contem a descrição do termo, "en", que contem a tradução para inglês e "de", a tradução para alemão.

## Formulação do dicionário com tradução para inglês
Primeiramente, visualizou-se a quantidade de entradas presentes nos ficheiros "dicionario.json" e "termos_traduzidos.txt", e verifica-se que o ficheiro JSON tem 9005 elementos, e o TXT tem 8817 elementos, ou seja, haverá elementos no dicionário que não estão presentes nos termos traduzidos.

Portanto, num fase inicial ("translate_pt_en.py"), percorreu-se o ficheiro TXT linha a linha, realizando o split das mesmas pela substring " @ ", e guardou-se no dicionário "dic_pt_en" as traduções dos termos. De seguida, reutilizou-se o código do programa anterior, mas em vez de utilizar o "GoogleTranslator" para a tradução, utilizou-se o dicionário "dic_pt_en" para colocar as traduções. Nos casos em que o "dic_pt_en" não tem a tradução dos termos, colocou-se a string "404 not found", e guardando o resultado no ficheiro "dicionario_pt_en.json".

Procurando pelo termo "404 not found" no ficheiro criado, verifica-se que existem 191 instâncias deste, pelo que uma possível solução será realizar o GoogleTranslator apenas para estes, conforme feito no programa "translate_pt_en_completo.py", guardando o resultado no ficheiro "dicionario_pt_en_completo.json".