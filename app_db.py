import mysql.connector

def conectar():
    try:
        return mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "280103",
        database = "lista_compras")

        print('conexão bem sucedida')

    except Exception as e:
        print('Erro ao conectar com o banco de dados',e)

def read_db(conexao_db):
    cursor = conexao_db.cursor() # usado para escrever comandos sql
    cursor.execute('select * from produto')
    resultado = cursor.fetchall() # busca todos os resultados de uma consulta sql feita no cursor em forma de tuplas
    for i in resultado:
        print(i)


def update_db(conexao_db, id, quantidade):
    try:
        cursor = conexao_db.cursor()
        sql = 'UPDATE produto SET quantidade = %s WHERE produto_id = %s'

        valor = (quantidade, id)
        cursor.execute(sql, valor)

        conexao_db.commit()
        print('Alteração realizada')
    except Exception as e:
        print('!!!!!!!', e)

def delete_db(conexao_db, id):
    try:
        cursor = conexao_db.cursor()
        sql = 'DELETE FROM produto WHERE produto_id = %s'
        valor = (id,) # isso é uma tupla de um unnico item, sem a , python entende que é só um numero

        cursor.execute(sql, valor)

        conexao_db.commit()
        print('Produto deletado')
    except Exception as e:
        print(e)


conexao_db = conectar()
read_db(conexao_db)
delete_db(conexao_db, 5)