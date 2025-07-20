'''Dada uma lista nums com números inteiros, forme pares consecutivos de modo que a soma dos menores números seja máxima.'''

def maior_menor():
    lista = [7, 1, 5, 3]
    lista.sort()

    soma = 0
    for i in range(0, len(lista), 2):
        print(lista[i])
        soma += lista[i]
    return soma

print(maior_menor())