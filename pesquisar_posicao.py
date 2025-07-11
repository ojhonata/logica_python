'''Dado um array ordenado de inteiros distintos e um valor de destino, retorne o índice se o destino for encontrado. Caso contrário, retorne o índice onde ele estaria se fosse inserido em ordem.

Você deve escrever um algoritmo com  O(log n)complexidade de tempo de execução.'''


def pesquisar_posicao(num):
    lista = [1, 3, 9, 12, 15]

    if num in lista:
        indice = lista.index(num)
        print(indice)
    else:
        for i, valor in enumerate(lista):
            if num > valor:
                print(i, valor)
            else:
                lista.insert(i, num)
                print(lista.index(num))
                break
                

pesquisar_posicao(7)