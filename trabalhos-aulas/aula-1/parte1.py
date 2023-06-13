print("---------------- Ex 1 ----------------")
nome = input("Qual o seu nome? ")
print(nome.upper())

print("\n---------------- Ex 2 ----------------")
def print_pares(lista):
    pares = list(x for x in lista if x % 2 == 0)
    print(pares)

print_pares(list(range(10)))

print("\n---------------- Ex 3 ----------------")
def print_ficheiro_inverso(nome):
    ficheiro = open(nome, "r", encoding="utf-8")
    linhas = ficheiro.read().splitlines()
    for linha in linhas[::-1]:
        print(linha)

print_ficheiro_inverso("aula-1/texto.txt")

print("\n---------------- Ex 4 ----------------")
def print_palavras_frequentes(nome):
    ficheiro = open(nome, "r", encoding="utf-8")
    palavras = ficheiro.read().split()
    frequencia = {}
    for palavra in palavras:
        if palavra in frequencia.keys():
            frequencia[palavra] = frequencia[palavra] + 1
        else:
            frequencia[palavra] = 1
    frequencia_ordenada = sorted(frequencia.items(), key=ordena, reverse=True)
    print(frequencia_ordenada[0:10])

def ordena(e):
    return e[1]

print_palavras_frequentes("aula-1/texto.txt")

print("\n---------------- Ex 5 ----------------")
dic_limpar = {"á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u", "à": "a",
              "â": "a", "ê": "e", "ô": "o", "ã": "a", "õ": "o", "ç": "c"}

def limpar_texto(texto):
    # Passar texto para minúsculas
    texto = texto.lower()

    # Remover acentos
    for key in dic_limpar:
        texto = texto.replace(key, dic_limpar.get(key))

    # Separar as palavras da pontuação e caracteres especiais
    texto_tmp = ""
    for indice in range(len(texto)):
        if texto[indice] in [",", ";", ".", ":", "(", ")", "[", "]", "{", "}", "—"]:
            if indice!=0 and texto[indice-1] not in [" ", "\n"]:
                texto_tmp += " "
            texto_tmp += texto[indice]
            if indice!=len(texto)-1 and texto[indice+1] not in [" ", "\n"]:
                texto_tmp += " "
        else:
            texto_tmp += texto[indice]
    texto = texto_tmp

    # Remover parágrafos duplicados e espaços duplicados, no início e no final das linhas
    texto_tmp = ""
    for indice in range(len(texto)):
        if texto[indice]==" ":
            # Remover espaços duplicados, no início e no final das linhas (deixa apenas 1 espaço no final)
            if indice!=0 and texto[indice-1] not in [" ", "\n"]:
                texto_tmp += texto[indice]
        elif texto[indice]=="\n":
            # Remover último espaço no final das linhas
            if indice!=0 and texto[indice-1] in [" "]:
                texto_tmp = texto_tmp[:-1]
            # Remover parágrafos duplicados
            if indice!=0 and texto[indice-1]=="\n" and indice!=1 and texto[indice-2]=="\n":
                texto_tmp = texto_tmp[:-1]
            texto_tmp += texto[indice]
        else:
            texto_tmp += texto[indice]
    texto = texto_tmp

    return texto

nome = "aula-1/texto.txt"
ficheiro = open(nome, "r", encoding="utf-8")
texto = ficheiro.read()
res = limpar_texto(texto)
print(res)
ficheiro_limpo = open("aula-1/texto-limpo.txt", "w", encoding="utf-8")
ficheiro_limpo.write(res)
