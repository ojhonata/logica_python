# Adicione dois números


def dois_numeros(lista1, lista2):
    lista = []
    try:
        for num1, num2 in zip(lista1, lista2):
            lista.append(num1 + num2)
        return lista[::-1]
    except Exception as e:
        print(e)

l1 = [1, 4, 7]
l2 = [5, 7, 9]

print(dois_numeros(l1, l2))