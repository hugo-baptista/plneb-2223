# Resolução do exercício da Aula 7 - Servidor *Flask*

Este exercício teve como objetivo a criação de um servidor *Flask* utilizando o ficheiro JSON criado na aula 5, que contém um dicionário com os termos como chaves, e os seus valores sendo um dicionário, com a descrição do mesmo e a sua traduão para inglês.

Para tal, utilizou-se a *framework Bootstrap* para o desenvolvimento das páginas HTML, com a criação da *navbar*, do *footer*, da *list* dos termos e do *form* para adicionar novos termos.

O servidor *Flask*, na porta 3000 do *localhost*, contém 4 possíveis *routes*:
- *http://localhost:3000/* - Página inicial
- *http://localhost:3000/terms* - Página com a listagem dos termos
- *http://localhost:3000/term/<t>* - Página com as informações do termo <t>
- *http://localhost:3000/terms/search* - Página para a pesquisa de termos (ainda não desenvolvida)