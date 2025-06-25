opcao = {
    'categorias': ['Frutas', 'Cores', 'Nome'],

    'frutas': ['Maçã', 'Pera', 'uva'],
    'cores': ['Azul', 'Verde', 'Vermelho'],
    'nome': ['Jhow', 'Jorge', 'Tobias']
}

def exibir_categorias():
    for category in opcao['categorias']:
        print(category)

def exibir_itens(categoria):
    if opcao == 0:
        print('Lista está vazia!')
    else:        
        print(opcao[categoria])

def add_item(category, item):
    opcao[category].append(item)
    print(f'{item} adicionado')

def remove_item(category, item):
    if category in opcao['categorias'] and item in opcao[category]:
        opcao[category].remove(item)
        print(f'{item} removido')
    else:
        print('Categoria ou item não encontrado')

def main():
    while True:
        opcoes = input('Digite o que deseja fazer\n 1 - Exibir itens ou categorias \n 2 - adicionar\n 3 - remover \nEscolha: ').lower()
        try:
            if opcoes == '1':
                exibir_categorias()
                itens = str(input('Digite a categoria que queira exibir os itens: ')).lower()
                exibir_itens(itens)
            elif opcoes == '2':
                categoria = str(input('Selecione a categoria: '))
                item = str(input('Digite o item que deseja adicionar: ')).capitalize()

                add_item(categoria, item)
            elif opcoes == '3':
                categoria = str(input('Selecione a categoria: '))
                item = str(input('Digite o item que deseja remover: ')).capitalize()

                remove_item(categoria, item)
            else:
                print('Digite uma opção válida!')
        except KeyError:
            print('!!!!!!!!')
        
        sair = input('Deseja sair? [s]im: ').lower().startswith('s')
        if sair is True:
            break

main()