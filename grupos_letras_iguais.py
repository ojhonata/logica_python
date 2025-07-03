def grupos_letras_iguais(letras):
    contador = 0
    ultima_letra = '' # varável onde será aramzenada a última letra
    for letra in letras: # para cada letra em letras
        
        if ultima_letra != letra: # se a última letra for diferente da letra atual
            ultima_letra = letra # adiciona letra na variável ultima_letra
            contador += 1
    return contador

letras = 'aabbccaa'
print(grupos_letras_iguais(letras))