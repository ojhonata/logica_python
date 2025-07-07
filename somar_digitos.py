def somar_numeros(numeros):
    total = 0
    numero = str(numeros)
    
    for i in numero:
        num_int = int(i)
        print(num_int)
        total += num_int
    return total

print(somar_numeros(1234))