# Resolução do exercício da Aula 4 - XML to HTML

## XML to HTML
Primeiramente, foi criado um programa `xml_to_html.py` que transforma um ficheiro XML num HTML.
Para tal, o ficheiro XML utilizado foi o `dicionario_medico.xml` presente no repositório do professor, seguido de um conjunto de transformações para o adequar ao ficheiro HTML, que são:
- Remoção dos caracteres de Form Feed (`\f`);
- Remoção dos marcadores `<text...>` e `</text>`;
- Marcação dos termos com `#T=`;
- Remoção dos restantes marcadores `<...>`;
- Marcação das explicações com `#E=`;
- Colapsar explicações (remover `\n`).

De seguida, reutilizou-se o código do programa `text_to_html_4.py` para construir o ficheiro HTML final, guardado como `dicionario_medico.html`.

## Anotar ficheiro

### Criar dicionário JSON
Para anotar o ficheiro `LIVRO-Doenças-do-Aparelho-Digestivo.pdf`, será utilizado um dicionário de forma a, a partir do termo, ser acrescentado a sua explicação quando o ponteiro do rato lhe passar por cima.

Assim, foi criado o programa `criar_dicionario_json.py` para esse efeito, reutilizando o tratamento do ficheiro XML criado anteriormente, mas alterando a forma final do ficheiro guardado, que em vez de ser um HTML em forma de tabela, as relações termo-explicação são transferidas para um dicionário python e guardadas num ficheiro em formato json `dicionario.json`.

### Criar anotações
Para a criação do ficheiro final, o ficheiro `LIVRO-Doenças-do-Aparelho-Digestivo.pdf` foi transformado em HTML, com recurso ao comando `pdftohtml`, criando assim 3 ficheiros JPG e 3 HTML, guardados na pasta `html_original`. Os ficheiros JPG correspondem às imagens do PDF original, e os 3 HTML são:
- `LIVRO-Doenças-do-Aparelho-Digestivo_ind.html`
- `LIVRO-Doenças-do-Aparelho-Digestivos.html`
- `LIVRO-Doenças-do-Aparelho-Digestivo.html`

O primeiro corresponde a um índice, que redireciona o utilizados para a pagina pretendida no segundo ficheiro. O segundo ficheiro contem toda a informação do ficheiro original, e o terceiro junta os dois numa só página.

Assim, apenas o segundo ficheiro é necessário para criar as anotações, visto que só este tem a informação do ficheiro original.

Deste modo, leu-se o ficheiro `LIVRO-Doenças-do-Aparelho-Digestivos.html`, dividindo-o por linhas. De seguida, para cada linha, retirou-se os marcadores HTML do tipo `<.+>` presentes no início e no fim das linhas, preservando-os em variáveis, e separando os restantes marcadores das restantes palavras. De seguida, relizou-se o split da linha e verificou-se se as palavras nela contidas estavam presentes no nas keys do `dicinário.json`, dicionando um marcador do género `<a href title=explicação>termo</a>` no seu lugar.