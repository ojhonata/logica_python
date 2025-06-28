palavra = 'banana'

lista = list(palavra)
for f, g in enumerate(lista):
    multi = g * f
    funcao = f'{f}-{g}' if f == 0 else f'{f}-{multi}'
    print(funcao)

print(lista)