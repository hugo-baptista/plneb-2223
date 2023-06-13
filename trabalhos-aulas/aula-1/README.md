# Resolução dos exercícios da Aula 1

## Parte 1 - Exercícios do slide 17

Para testar as funções, coloquei num ficheiro `texto.txt` o poema "Vem sentar-te comigo, Lídia, à beira do rio." de Ricardo Reis/Fernando Pessoa, que contém caracteres especiais portugueses (acentos e "ç"), alguns espaços em branco e parágrafos.

Assim, para "limpar" o texto, fiz um dicionário em que as keys são os caracteres especiais portugueses (acentos e "ç"), visto que o texto é em português, com os seus valores sendo os caracteres "normais" correspondentes. Caso o texto fosse de outra língua que não o português, seria necessário adicionar os caracteres especiais dessa língua ao dicionário (por exemplo, `"ñ": "n"`, no caso do espanhol, entre outros).

O texto "limpo" final é também adicionado ao ficheiro `texto-limpo.txt` para verificar o bom funcionamento das funções, principalmente se os espaços em branco no final das linhas são removidos, visto que não é possível verificar isso no terminal do VS Code.

## Parte 2 - Exercícios do slide 18