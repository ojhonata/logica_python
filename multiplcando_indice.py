def indice_vezes_letras(palavra):
    lista = list(palavra) # tranforma o paramantro em lista separando as letras
    resultado = []
    for f, g in enumerate(lista): # enumerate é usado para iterar o indice com o conteudo, permitindo fazer o 'for f, g'
        if f == 0: # se o indice for igual a 0
            resultado.append(f'{f}-{g}') # adiciona na lista o indice e o conteudo
        else: # caso contrário
            resultado.append(f'{f}-{g * f}') # adiciona o indice e a multiplicação do indice com a letra
    return resultado # retorna a lista
    
palavra = 'banana'
saida = indice_vezes_letras(palavra)

# se eu fizesse o print(saida) ele iria me retornar o ultimo item da lista
for item in saida: # usando esse loop ele passa item por item e imprime na tela
    print(item)