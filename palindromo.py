def palindromo(num):
    texto = str(num)
    if texto == texto[::-1]:
        print('Palíndromo')
    else:
        print('Não Palíndromo')

palindromo(121)