def letras_repitidas(palavra):
    dicionario = {} # dicionario vazio

    for letra in palavra: # para cada letra em palavra
        if letra in dicionario: # se letra ja existir em dicionario
            dicionario[letra] += 1 # adiciona mais 1 no contador da letra
        else:
            dicionario[letra] = 1 # caso contrario o contador é igual a 1
    return dicionario # retorna o dicionario

palavra = 'banana'
funcao = letras_repitidas(palavra)
print(funcao)