# Resolução do exercício da Aula 8 - Introdução ao spiCy

No ficheiro `ex1.py`, inicialmente, realizou-se uma exploração básica das funcionalidades do spiCy - carregar a língua, o documento (árvore documental), buscar as frases e entidades, bem como os parâmetros destes.

### Exercício 1

Para calcular as ocorrências de um determinado verbo, criou-se um ciclo que verifica a POS (*Part of Speech*) de cada palavra do texto, verificando se esta equivale a um `VERB`, que corresponde a um verbo. Nesse caso, tenta acrescentar em 1 a contagem do lema dessa palavra num dicionário (chamado `contador`). Caso não consiga, é porque o lema não existe nas keys do dicionário, e diciona-o ao mesmo com o valor 1.