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


# criar_tabela()

# Listar as reclamações
def listar_reclamacoes():
    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute("SELECT * FROM ouvidoria")
    resultado = cursor.fetchall()

    if len(resultado) == 0:
        print("Não há reclamações.")
    else:
        print(" ---- Reclamações atualmente ---- ")
        for reclamacao in resultado:
            print(f"{reclamacao[0]}. {reclamacao[1]}")

    conexao.close()

listar_reclamacoes()