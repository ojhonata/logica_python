def palindromo(termo):
    texto = str(termo).upper() # armazena o parametro num na variavel como string
    if texto == texto[::-1]: # se texto for igua a texto invertido 
        print('Palíndromo')
    else:
        print('Não Palíndromo')

palindromo('mirim')