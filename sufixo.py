'''Escreva uma função que encontre o maior sufixo comum entre as palavras de uma lista'''

def maior_sufixo(strs):
    sufixo = strs[0]

    for palavra in strs[1:]:
        while not palavra.endswith(sufixo):
            sufixo = sufixo[1:]
            if sufixo == "":
                return ""
    return sufixo

print(maior_sufixo(["natação", "emoção", "ação"]))