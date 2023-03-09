# Resolução dos exercícios da Aula 3 - Text_to_HTML

## Versão 1
Feito na aula, procede ao seguintes passos:
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