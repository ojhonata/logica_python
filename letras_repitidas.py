palavra = 'banana'

dicionario = {}

for letra in palavra:
    if letra in dicionario:
        dicionario[letra] += 1
    else:
        dicionario[letra] = 1
print(dicionario)