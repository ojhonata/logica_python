'''pegamos a sequencia de numeros e adicionamos em um dicionario junto a um contador as letras com que se repetem

 '''

def subsequencia(sequencia):
    num_repitidas = {}
    maior = 0
    for i in sequencia:
        if i in num_repitidas:
            num_repitidas[i] += 1
        else:
            num_repitidas[i] = 1
    for chave, valor in num_repitidas.items():
        if chave + 1 in num_repitidas:
            soma = valor + num_repitidas[chave + 1]
            if soma > maior:
                maior = soma
                
    return maior, num_repitidas

termo = [1,1,1,1, 2, 3, 3, 3, 4, 4, 5]
funcao = subsequencia(termo)
print(funcao)