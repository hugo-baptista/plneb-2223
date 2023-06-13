# Resolução do exercício da Aula 7 - Servidor *Flask*

Este exercício teve como objetivo a criação de um servidor *Flask* utilizando o ficheiro JSON criado na aula 5 (`dicionario_pt_en_completo.json`, copiado para a pasta com o nome `database_original.json`), que contém um dicionário com os termos como chaves, e os seus valores sendo um dicionário, com a descrição do mesmo e a sua traduão para inglês.

Para tal, utilizou-se a *framework Bootstrap 5.0* (https://getbootstrap.com/docs/5.0/getting-started/introduction/) para o desenvolvimento das páginas HTML, com a criação da *navbar*, do *footer*, da *list* dos termos, do *form* para adicionar novos termos e do *button* para eliminar termos.

O servidor *Flask*, na porta 3000 do *localhost*, contém 4 possíveis *routes*:
- `http://localhost:3000/` - Página inicial
- `http://localhost:3000/terms` - Página com a listagem dos termos
- `http://localhost:3000/term/<t>` - Página com as informações do termo `<t>`
- `http://localhost:3000/terms/search` - Página para a pesquisa de termos

A página da listagem dos termos também tem um *form* para adicionar termos e um *button* para cada termo para o apagar do dicionário em memória. De seguida, as alterações ao dicionário em memória são guardadas no ficheiro `database_modified.json`, de modo a não alterar o JSON original. Desta forma, sempre que o servidor é iniciado, ele tenta ler o ficheiro `database_modified.json`, e caso este não exista, lê o `database_original.json`.

A página de procura tem um campo para introduir o texto que queremos pesquisar, sendo o resultado apresentado numa lista na mesma página. A procura é feita verificando se existe *match* do texto com o termo ou a descrição do mesmo.