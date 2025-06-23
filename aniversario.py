import datetime

def validar_data(data):
    try:
        return datetime.datetime.strptime(data, '%d/%m/%Y') #string para date
    except:
        return None

def aniversario(data_formatada):
    hoje = datetime.datetime.now().strftime('%d/%m') # date para string
    if data_formatada.strftime('%d/%m') == hoje:
        print('parabéns')
    else:
        print('Calma..')

def verificar_idade(data_nascimento):
    hoje = datetime.datetime.now()
    idade = hoje.year - data_nascimento.year

    if (hoje.month, hoje.day) < (data_nascimento.month, data_nascimento.day):
        idade -= 1
    
    return idade

def main():
    data = input('Digite sua data de aniversário (dd/mm/yyyy): ')
    data_formatda = validar_data(data)

    if data_formatda:
        aniversario(data_formatda)
        idade = verificar_idade(data_formatda)
        print(f'idade: {idade}')
    else:
        print('Data inválida')


main()