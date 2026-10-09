import mysql.connector


# banco de dados, cadastrar e listar reclamações

#conectar com o banco de dados
def conectar_banco():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="100407",
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


# Chamada da função sem NENHUM espaço antes da palavra:
criar_tabela()

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

# listar_reclamacoes()

# cadastrar nova reclamação
def cadastrar_reclamacao():
    texto = input("Digite a reclamação: ")

    conexao = conectar_banco()
    cursor = conexao.cursor()
    comando = "INSERT INTO ouvidoria (texto) VALUES (%s)"
    cursor.execute(comando, (texto,))
    conexao.commit()

    print("Reclamação registrada com sucesso!")
    conexao.close()

cadastrar_reclamacao()
listar_reclamacoes()
cadastrar_reclamacao()
listar_reclamacoes()

# pesquisas de reclamações
def pesquisar_reclamacao_por_id():
    try:
        id_busca = int(input("\nDigite o ID da reclamação: "))
        
        conexao = conectar_banco()
        cursor = conexao.cursor()
        cursor.execute("SELECT id, texto FROM ouvidoria WHERE id = %s", (id_busca,))
        resultado = cursor.fetchone()
        conexao.close()

        if resultado:
            print(f"Reclamação #{resultado[0]}: {resultado[1]}")
        else:
            print("Nenhuma reclamação encontrada com esse ID.")
            
    except ValueError:
        print("Erro: Digite apenas números inteiros.")

#quantidade de reclamações
def exibir_quantidade_reclamacoes():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("SELECT COUNT(*) FROM ouvidoria")
    total = cursor.fetchone()[0]
    conexao.close()

    print(f"\nTotal de reclamações: {total}")


# editar, excluir e menu de opções