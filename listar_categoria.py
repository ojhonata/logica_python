opcao = [
    {
        'categorias': ['Frutas', 'Cores', 'Nome'],

        'frutas': ['Maçã', 'Pera', 'uva'],
        'cores': ['Azul', 'Verde', 'Vermelho'],
        'nome': ['Jhow', 'Jorge', 'Tobias']
    }
]

def exibir_categorias():
    for menu in opcao:
        for category in menu['categorias']:
            print(category)

def exibir_itens(categoria):
    if opcao == 0:
        print('Lista está vazia!')
    else:
        for itens in opcao:
            print(itens[categoria])

def add_item(category, item):
    for menu in opcao:
        menu[category].append(item)
    print(f'{item} adicionado')

def remove_item(category, item):
    for menu in opcao:
        menu[category].remove(item)
    print(f'{item} removido')

def main():
    while True:
        opcoes = input('Digite o que deseja fazer (Exibir (itens ou categorias), adicionar ou remover): ').lower()
        try:
            if opcoes == 'exibir':
                exibir_categorias()
                itens = str(input('Digite a categoria que queira exibir os itens: ')).lower()
                exibir_itens(itens)
            elif opcoes == 'adicionar':
                categoria = str(input('Selecione a categoria: '))
                item = str(input('Digite o item que deseja adicionar: '))

                add_item(categoria, item)
            elif opcoes == 'remover':
                categoria = str(input('Selecione a categoria: '))
                item = str(input('Digite o item que deseja adicionar: '))

                remove_item(categoria, item)
            else:
                print('Digite uma opção válida!')
        except KeyError:
            print('!!!!!!!!')
        
        sair = input('Deseja sair? [s]im: ').lower().startswith('s')
        if sair is True:
            break

exibir_categorias()
main()