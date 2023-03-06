# Resolução dos exercícios da Aula 2

## Ficha_RE_1

### Exercício 2
Assumi que o sinal de pontuação válido para o final de uma expressão pode ser ";", ":", ".", "?" e "!"

## Ficha_RE_2

### Exercício 2
Assumi que a extensão dos ficheiros (por exemplo, ".txt", ".png", ".docx"...) são constituídas apenas por alfanuméricos, ou seja, sem pontos nem hífens.

### Exercício 3
Utilizei 3 grupos para separar os nomes: o 1º grupo captura o primeio nome, o 3º grupo o último nome e o 2º grupo captura todos os nomes intermédios (incluíndo os conectores). Caso o texto apenas apresente o primeiro e último nome, o 2º grupo fica vazio.

### Exercício 4
Considerei que o objetivo da função é dividir e devolver uma lista dos códigos postais válidos, e não apenas dizer quais são ou não válidos (como no exercício 2).

### Exercício 5
Utilizei uma função lambda para conseguir o valor das abreviaturas no dicionário diretamente do re.sub().

### Exercício 6
Fiz 2 resoluções para este exercício:
- Existem 6 formatos possíveis para as matrículas (AA-00-00, AA-AA-00, AA-00-AA, 00-AA-AA, 00-00-AA e 00-AA-00), pelo que, para simplificar, criei uma lista com os 6 possíveis formatos para verificar se as matrículas são válidas. Assim, para cada matrícula, realizam-se 6 procuras distintas.
- Como, para matrículas que apresentem maiúsculas e números apenas os formatos AA-AA-AA e 00-00-00 são inválidas, então pode-se primeiro validar aquelas que apresentam apenas maiúculas e números, filtrando (invalidando) dessas as que apresentam tudo maiúsculas ou tudo números. Assim, para cada matrícula válida, há no máximo 2 procuras.