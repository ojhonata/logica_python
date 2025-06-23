num_romanos = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
}

def converter_romano(numeros):
    numero = numeros[::-1]
    total = 0
    anterior = 0

    try:
        for i in range(len(numero)): #conta quantos indices 
            valor = num_romanos[numero[i]] # pega indice por indice e pega o valor atribuido no dicionário (valor)
            if valor < anterior: # verifica se o numero do primeiro indice é maior que o anterior (variavel)
                total -= valor #subtrai o valor e armazena na variável total
            else:
                total += valor
            anterior = valor
        return total
    except KeyError: # caso o caracter digitado não esteja no dicionário
        return None

numeros = input('Digite um número romano: ').upper() 

resultado = converter_romano(numeros)
print(resultado)