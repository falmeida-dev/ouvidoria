import mysql.connector


# banco de dados, cadastrar e listar reclamações

#conectar com o banco de dados
def conectar_banco():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="senha_banco",
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

# cadastrar_reclamacao()
# listar_reclamacoes()
# cadastrar_reclamacao()
# listar_reclamacoes()

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

# pesquisar por termo
def pesquisar_por_termo():
    termo = input("\nDigite o termo que deseja pesquisar: ")

    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("SELECT id, texto FROM ouvidoria WHERE texto LIKE %s", ('%' + termo + '%',))
    resultados = cursor.fetchall()
    conexao.close()

    if resultados:
        print(f"\nReclamações contendo '{termo}':")
        for reclamacao in resultados:
            print(f"{reclamacao[0]}. {reclamacao[1]}")
    else:
        print("Nenhuma reclamação encontrada contendo'.")

#quantidade de reclamações
def exibir_quantidade_reclamacoes():
    conexao = conectar_banco()
    cursor = conexao.cursor()
    cursor.execute("SELECT COUNT(*) FROM ouvidoria")
    total = cursor.fetchone()[0]
    conexao.close()

    print(f"\nTotal de reclamações: {total}")


# editar, excluir e menu de opções
# editar manifestação
def editar_manifestacao():
    codigo_editar = int(input("Digite o código da manifestação que deseja editar: "))

    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute("SELECT id FROM ouvidoria WHERE id = %s", (codigo_editar,))
    if cursor.fetchone() is None:
        print("Código não encontrado.")
    else:
        nova_descricao = input("Digite o novo texto da manifestação: ")
        comando = "UPDATE ouvidoria SET texto = %s WHERE id = %s"
        cursor.execute(comando, (nova_descricao, codigo_editar))
        conexao.commit()
        print("Manifestação editada com sucesso!")

    conexao.close()


#excluir manifestação
def excluir_manifestacao():
    codigo_excluir = int(input("Digite o código da manifestação que deseja excluir: "))

    conexao = conectar_banco()
    cursor = conexao.cursor()

    cursor.execute("SELECT id FROM ouvidoria WHERE id = %s", (codigo_excluir,))
    if cursor.fetchone() is None:
        print("Código não encontrado.")
    else:
        comando = "DELETE FROM ouvidoria WHERE id = %s"
        cursor.execute(comando, (codigo_excluir,))
        conexao.commit()
        print("Manifestação excluída com sucesso!")

    conexao.close()


# Menu principal (opção 8 - Sair)
criar_tabela()

opcao = 0

while opcao != 8:
    print("\n--- SISTEMA DE OUVIDORIA (MySQL) ---")
    print("1. Listar todas as manifestações")
    print("2. Cadastrar nova manifestação")
    print("3. Pesquisar por código")
    print("4. Pesquisar por nome/termo")
    print("5. Editar manifestação")
    print("6. Excluir manifestação")
    print("7. Exibir quantidade total")
    print("8. Sair")

    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        listar_reclamacoes()

    elif opcao == 2:
        cadastrar_reclamacao()

    elif opcao == 3:
        pesquisar_reclamacao_por_id()

    elif opcao == 4:
        pesquisar_por_termo()

    elif opcao == 5:
        editar_manifestacao()

    elif opcao == 6:
        excluir_manifestacao()

    elif opcao == 7:
        exibir_quantidade_reclamacoes()

    elif opcao == 8:
        print("Saindo do sistema de ouvidoria...")

    else:
        print("Opção inválida. Tente novamente.")