import mysql.connector

#conectar com o banco de dados
def conectar_banco():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1212",
        database="ouvidoria"
    )

    conexao.close()

def criar_tabela():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS ouvidoria (
        id INT AUTO_INCREMENT PRIMARY KEY,
        texto VARCHAR(255) NOT NULL
    )        
    """)
    conexao.commit()
    conexao.close()


criar_tabela()