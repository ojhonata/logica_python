import mysql.connector

try:
    conexao_db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "280103",
        database = "lista_compras"

    )

    print('conexão bem sucedida')

except:
    print('!!!!')

def read_db():
    cursor = conexao_db.cursor() # usado para escrever comandos sql
    cursor.execute('select * from produto')
    resultado = cursor.fetchall() # busca todos os resultados de uma consulta sql feita no cursor em forma de tuplas
    for i in resultado:
        print(i)

read_db()

def update_product(id, quantidade):
    try:
        cursor = conexao_db.cursor()
        sql = 'UPDATE produto SET quantidade = %s WHERE produto_id = %s'

        valor = (quantidade, id)
        cursor.execute(sql, valor)

        conexao_db.commit()
        print('Alteração realizada')
    except Exception as e:
        print('!!!!!!!', e)

update_product(2, 10)