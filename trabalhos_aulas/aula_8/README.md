# Resolução do exercício da Aula 8 - Introdução ao spiCy

No ficheiro `ex1.py`, inicialmente, realizou-se uma exploração básica das funcionalidades do spiCy - carregar a língua, o documento (árvore documental), buscar as frases e entidades, bem como os parâmetros destes.

### Exercício 1 - Ocorrências de verbos

Para calcular as ocorrências dos verbos num texto, criou-se um ciclo que verifica a POS (*Part of Speech*) de cada palavra do texto, verificando se esta equivale a um `VERB`, que corresponde a um verbo. Nesse caso, tenta acrescentar em 1 a contagem do lema dessa palavra no dicionário `contador`. Caso não consiga acrescentar 1, é porque o lema não existe nas *keys* do dicionário, e adiciona-o ao mesmo com o valor 1.

### Exercício 2 - Ocorrências de entidades, nomes e localidades

Para calcular as ocorrências de entidades, nomes e localidades, lê-se um dos ficheiros presentes na diretoria `livros`, e com um ciclo das entidades presentes no texto, adicionamos as mesmas a três listas diferentes:
- `entidades_lista` - para todos os casos;
- `nomes` - caso o tipo de entidade seja `PER` (ou seja, uma pessoa);
- `lugares` - caso o tipo de entidade seja `LOC` (ou seja, uma localidade).

De seguida, realiza-se a contagem destas listas, apresentando os top 10 elementos com mais ocorrências de cada uma das listas. O número de elementos apresentados pode ser alterado através da mudança da variável `top`.