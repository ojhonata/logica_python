def proximo_a_dez(numeros, tolerancia=2): 
    resultado = 0
    for num in numeros: # passamos números por números
        if num + 1 in numeros: # se o número atual + 1 estiver no parametro 'numeros'
            resultado = num + (num + 1) # soma o número atual + o próximo número
            diferenca = abs(resultado - 10) # subtraimos o resultado por 10, se o número for negativo ele torna a ser absoluto/positivo (abs)
        print(f'{resultado} - {diferenca}', True if diferenca <= tolerancia else False) # imprime o resultado da soma - diferença e verificamos se o número é próximo a 10 com a tolerancia que foi difinada no parâmetro da função, se a diferença for menor ou igual a 2 exibimos True.

numeros = [1, 2, 3, 4, 5]
print(numeros)
proximo_a_dez(numeros)