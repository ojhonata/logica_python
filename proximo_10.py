def proximo_a_dez(numeros, tolerancia=2):
    resultado = 0
    for num in numeros:
        if num + 1 in numeros:
            resultado = num + (num + 1)
            diferenca = abs(resultado - 10)
        print(f'{resultado} - {diferenca}', True if diferenca <= tolerancia else False)

numeros = [1, 2, 3, 4, 5]
proximo_a_dez(numeros)