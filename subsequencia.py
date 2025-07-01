def subsequencia(sequencia):
    num_repitidas = {}
    maior = 0
    for i in sequencia: # passa número por número do parametro
        if i in num_repitidas: # se o numero já estiver no dicionário
            num_repitidas[i] += 1 # soma mais um no contador
        else:
            num_repitidas[i] = 1 # senão o contador será igual a 1
    for chave, valor in num_repitidas.items(): # percorre chave e valor no dicionario
        if chave + 1 in num_repitidas: # se a chave atual + 1 (1 + 2) existir no dicionario
            soma = valor + num_repitidas[chave + 1] # soma os valores das duas chaves
            if soma > maior: # se a soma for maior que o valor atual de 'maior'
                maior = soma # atualiza 'maior' com essa nova soma
    return maior, num_repitidas

termo = [1, 1, 1, 1, 2, 3, 3, 3, 4, 4, 5,]
funcao = subsequencia(termo)
print(funcao)