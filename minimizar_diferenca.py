'''Dada uma lista nums, forme pares consecutivos de forma que a maior diferença entre elementos do mesmo par seja a menor possível.'''

def minimizar_diferenca():
    lista = [9, 1, 8, 3, 5, 7]
    lista.sort()

    lista_maior = []
    for i in range(0, len(lista), 2):
        par = (lista[i], lista[i + 1])
        diferenca = par[1] - par[0]
        lista_maior.append(diferenca)
    maior = max(lista_maior)
    print(maior)

minimizar_diferenca()