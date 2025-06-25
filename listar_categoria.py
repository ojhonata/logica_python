# programa que exiba todos os itens de uma determinada categoria 
# o programa irá exibir as categorias exixstentes

opcao = [
    {
        'categorias': ['Frutas', 'Cores', 'Nome'],

        'frutas': ['Maçã', 'Pera', 'uva'],
        'cores': ['Azul', 'Verde', 'Vermelho']
    }
]

for menu in opcao:
    for category in menu['categorias']:
        print(f'Categorias: {category}')

    categoria = input('Digite uma categoria: ').lower()
    print(menu[categoria])
# 1. criar uma lista, dicionario contendo esses itens
# 2. criar uma função para exibir esses itens
# loop para percorrer a lista ou dicionario
# return para exibir a categria

# o usuario podera digitar a categoria que ele quiser para exibir os itens
# 