import sqlite3

# cria o banco de dados .db
def criar_banco():
    return sqlite3.connect('ouvidoria.db')

# cria a tabela no banco local
def criar_tabela():
    conexao = criar_banco()
    # serve para executar comandos SQL no banco
    cursor = conexao.cursor()
    # executa o comando SQL
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reclamacoes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            texto TEXT NOT NULL
        )
    ''')
    #salva a alteração no banco
    conexao.commit()
    conexao.close()

criar_tabela()