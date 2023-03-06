# Resolução dos exercícios da Aula 2

## RegexCrossword
Tentei fazer login com o email institucional para aparecer o número de aluno, conforme o indicado pelo professor, mas não consegui, por isso entrei com a conta do GitHub, e por isso o cabeçalho do site não tem identificação. Ainda assim, abri a blackboard e dá para ver, no separador ao lado, o meu nome.

## Ficha_RE_1

### Exercício 2
Assumi que o sinal de pontuação válido para o final de uma expressão pode ser ";", ":", ".", "?" e "!".

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
- Como, para matrículas que apresentem maiúsculas e números apenas os formatos AA-AA-AA e 00-00-00 são inválidas, então pode-se primeiro validar aquelas que apresentam apenas maiúculas e números, filtrando (invalidando) dessas as que apresentam tudo maiúsculas ou tudo números. Assim, para cada matrícula válida, há no máximo 3 procuras.

### Exercício 7
Primeiro, procuro todas as instâncias da forma [PEDIDO], de seguida percorro todas essas instâncias, pedindo o input do utilizados para cada uma delas e substituíndo a primeira instância da forma [PEDIDO] do texto pela resposta.

### Exercício 8
Neste caso, analisa cada palavra individualmente (delimitada por word boundaries), e se as palavras a seguir tiverem os mesmos caracteres (não diferenciando as maiúsculas das minúsculas), substitui todas as instâncias dessa palavra pela primeira (ou seja, se o texto tiver, por exemplo, "EsTe este eSTe", substitui-os por "EsTe" - o primeiro que aparece).