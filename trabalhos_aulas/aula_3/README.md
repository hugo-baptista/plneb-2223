# Resolução dos exercícios da Aula 3 - Text to HTML

## Versão 1
Feito na aula, procede ao seguintes passos de processamento do texto:
- Remoção dos caracteres de Form Feed ("\f").
- Marcação, com "#T=", dos termos, ou seja, das linhas seguidas por "\n\n", dois "new line".
- Marcação, com "#E=", das explicações dos termos, ou seja, das restantes linhas.
- Correção das explicações "desformatadas" pelos carateres de Form Feed, ou seja, que aparecem no formato:
```
<termo>

\f<explicação>
```
- Remoção dos "new line" das explicações, ou seja, "colapsar" linhas que começam por "#E=" em uma só linha.
- Remoção dos marcadores "#T=" e "#E=".

De seguida, procura todas as entradas com o formato regex \n\n(.+)\n(.+), retornando uma lista de tuplos em que o primeiro elemento é um termo e o segundo elemento é a sua explicação.

Assim sendo, utiliza estes tuplos para contruir um ficheiro html que apresenta uma lista destes.

## Versão 2
O processamento do texto é o mesmo da versão 1, mas o ficheiro html que contrói ilustra do dicionário em formato de tabela. Também foi criado um ficheiro css, responsável por alterar as cores e o formato da tabela, para uma leitura mais fácil.

### Problema com a Versão 2
Verifica-se em entradas como "anti-séptico", "análise didática", "eclâmpsia", "elemento", entre outros, que a "correção" das explicações realizada não é suficiente, pois apenas tem em consideração as "desformatações" em que a explicação aparece "separada" do termo, ou seja, de casos do tipo:
```
<termo>

\f<explicação>
```
Mas a explicação também pode ser "desformatada" a meio, e não apenas no início, ou seja, ficar como:
```
<termo>
<início da explicação>

\f<fim da explicação>
```