import mysql.connector

try:
    conexao_db = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "280103",
        database = "lista_compras"

    )

    print('conexão bem sucedida')

    cursor = conexao_db.cursor()

    cursor.execute('select * from produto')

    resultado = cursor.fetchall()
    print(resultado)
except:
    print('!!!!')