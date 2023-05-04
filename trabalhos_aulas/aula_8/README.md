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

### Exercício 3 - "Best friends"

Para verificar quais entidades que mais aparecem conjuntamente em frases dos livros, primeiramente lê-se o ficheiro, e de seguida cria-se uma lista de listas das pessoas que aparecem em conjunto numa frase, ou seja, uma matriz cujas linhas são as entidades com tipo `PER` (ou cujo texto é `Harry` ou `Harry Potter`, pois estes são marcados como `MISC` no documento `harry_potter_pedra_filosofal.txt`) que aparecem numa só frase.

Para isso, lê-se uma frase de cada vez, criando-se uma lista com as entidades previamente descritas dessa frase, sem repetidos. Caso esta lista tenha pelo menos 2 elementos, visto que se quer contar os pares que existem nas frases, é adicionada à matriz.

Se seguida, utilizando a função `combinations` da biblioteca `itertools`, pega-se em cada linha da matriz, e calcula-se o número de combinações 2 a 2 possíveis dos seus elementos, ou seja, caso a linha tenha 3 pessoas, por exemplo `[Carlos, Ega, Maria]`, então existem 3 possíveis combinações: `(Carlos, Ega)`, `(Carlos, Maria)` e `(Ega, Maria)`. Também é importante salientar que se realiza o sort desses tuplos para remover a ordem dos termos, ou seja, para contabilizar `(Carlos, Ega)` e `(Ega, Carlos)` como sendo iguais. Todas estes tuplos das combinações são guardados na lista `combinacoes`.

De seguida, realiza-se o `Counter` dessa lista e apresentam-se os top 10 dos pares com mais ocorrências no texto, de forma semelhante ao `Exercício 2`.