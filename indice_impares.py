# Dada uma lista nums, some todos os números nos índices ímpares depois de ordenar.

def idx_impar():
    lista = [4, 2, 9, 1, 5, 3]
    lista.sort()

    soma = 0
    for i in range(1, len(lista), 2):
        print(lista[i])

        soma += lista[i]

idx_impar()