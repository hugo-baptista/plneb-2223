# Resolução do exercício da Aula 6 - Servidor *Flask*

Este exercício teve como objetivo a criação de um servidor *Flask* com informações sobre 3 temas: engenharia, égua e elefante.

Para tal, no ficheiro *flask_server.py*, criou-se o servidor *Flask* na porta 3000 do *localhost*, tendo ele 4 *routes* possíveis:
- *http://localhost:3000/* - Página inicial
- *http://localhost:3000/engenharia* - Página sobre a engenharia
- *http://localhost:3000/egua* - Página sobre a égua
- *http://localhost:3000/elefante* - Página sobre o elefante

De forma a tornar o código mais modular e simples, utilizou-se o *Jinja*. Assim, criou-se, na pasta *templates*, 5 páginas HTML, o *layout.html*, que contém a barra de navegação que aparecerá em todas as *routes* e um bloco que vai ser sustituído pelos restantes HTML na sua *route* respetiva, ou seja, *home.html* na *route* "/", *engenharia.html* na *route* "/engenharia", *egua.html* na *route* "/egua" e *elefante.html* na *route* "/elefante".

A *home.html* tem 3 blocos que redireciona para as restantes *routes*. A *engenharia.html*, *egua.html* e *elefante.html* apresentam uma imagem sobre o tema, um texto e um vídeo.

A diretoria *static* apresenta todos os elementos estáticos do servidor, ou seja, as imagens PNG e ICO e o ficheiro CSS.