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

De seguida, procura todas as entradas com o formato regex \n\n(.+)\n(.+), retornando uma lista de tuplos em que o primeiro elemento é um termo e o segundo elemento é a sua explicação (ou pelo menos, é esse o objetivo).

Assim sendo, utiliza estes tuplos para contruir um ficheiro HTML que apresenta uma lista destes.

## Versão 2
O processamento do texto é o mesmo da versão 1, mas o ficheiro HTML que contrói ilustra o dicionário em formato de tabela. Também foi criado um ficheiro CSS, responsável por alterar as cores e o formato da tabela, para uma leitura mais fácil.

### Problema com a Versão 2
Verifica-se em entradas como "anti-séptico", "análise didática", "eclâmpsia" e "elemento", entre outras, que a "correção" das explicações realizada não é suficiente, pois apenas tem em consideração as "desformatações" em que a explicação aparece "separada" do termo, ou seja, de casos do tipo:
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
Este problema indica que a correção da "desformatação" causada pelos caracteres de Form Feed tem de ser corrigida no momento em que os removemos, e não posteriormente, com recuso aos marcadores do texto, pois nesse momento perdemos a localização das desformatações, que eram marcadas pelos caracteres "\f".

## Versão 3
Assim, verifica-se que os caracteres de Form Feed podem aparecer em 3 situações:
- Antes do termo:
```
\f<termo>
<explicação>
```
- Depois do termo, antes da explicação:
```
<termo>

\f<explicação>
```
- A meio da explicação

```
<termo>
<início da explicação>

\f<fim da explicação>
```

Como será possível distinguir estres 3 casos para os corrigir? Uma possível maneira é o facto da explicação ser sempre iniciada por uma letra maiúscula, enquanto que o termo e o resto da explicação iniciam, em regra geral, por letra minúscula.

Ou seja, no primeiro caso, quando a linha seguinte onde o caracter de Form Feed aparece se inicia por uma letra maiúscula, este tem de ser simplesmente removido. Já no segundo e no terceiro caso, para além da remoção do \f, também podemos remover um \n anterior ao mesmo, para conseguir juntar a explicação ao termo ou à restante explicação.

É este o princípio de funcionamento da versão 3, que realiza as seguintes operações:
- Remoção dos \f em strings do género "\f(.+\n[A-ZÁÉÍÓÚÀÂÊÔÃÕÇ])", ou seja, um \f cuja linha seguinte ao mesmo começa por uma letra maiúscula, seja ela de A a Z ou qualquer outro caractere especial da língua portuguesa (correspondente ao primeiro caso apresentado).
- Remoção dos restantes \n\f+ (correspondente ao segundo e terceiro caso).
- Marcação, com "#T=", dos termos, ou seja, das linhas seguidas por "\n\n".
- Marcação, com "#E=", das explicações dos termos, ou seja, das restantes linhas.
- Remoção dos "new line" das explicações, ou seja, "colapsar" linhas que começam por "#E=" em uma só linha.
- Remoção dos marcadores "#T=" e "#E=".

A restante conversão para o ficheiro HTML é semelhante à realizada na versão 2, ou seja, para uma tabela.

### Problema com a Versão 3
A remoção dos \f em strings do género "\f(.+\n[A-ZÁÉÍÓÚÀÂÊÔÃÕÇ])" pode vir a ter problemas caso existam \f em explicações nas quais a próxima linha comece com uma letra maiúscula, como por exemplo um nome. Para tentar verificar a existência destes casos, criei o ficheiro "search_term_ff.py" que coloca todas as strings do género "\f(.+\n[A-ZÁÉÍÓÚÀÂÊÔÃÕÇ])" num ficheiro de texto "v3/0_search.txt". Efetivamente, verifica-se que este caso acontece nos termos "Fahrenheit" e "parasito":
```
Fahrenheit, termômetro de
Termômetro com graduação de Fahrenheit, marcando 32 graus na congelação e 212 graus na ebulição,

convertida em ºC, escala usada no Brasil, através da seguinte fórmula: ºC = ((F - 32 x 5) / 9). O termo advém de
Daniel Gabriel Fahrenheit, físico alemão (168
```
```
parasito

Ser vivo animal ou vegetal que durante parte ou toda a sua existência vive às custas de outros seres vivos; em
Atenas (a da Grécia clássica) ministros encarregados da colheita do trigo e preparadores dos banquetes às
divindades eram denominados parasitos.
```
Porém, como este apenas ocorre em 2 casos, segundo o indicado por estes ficheiros, mais fácil será corrigir esta "desformatação" manualmente do que arranjar outros padrões para o fazer em python, por se tratar de uma quantidade pequena de casos.

## Versão 4
Esta versão é igual, em código, à versão 3, mas o texto que utiliza é uma alteração do dicionário_medico original que tenha em conta os casos dos termos "Fahrenheit" e "parasito" apresentado.