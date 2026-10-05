
bd_ouvidoria = []
opcao = 0

while opcao != 6:
    print("Sistema de Ouvidoria!")
    print("1. Vizualizar reclamação")
    print("2. Registrar reclamações")
    print("3. Editar reclamação")
    print("4. Excluir reclamação")
    print("5. Exibir quantidade de reclamações")
    print("6. Sair")



    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        if len(bd_ouvidoria) == 0:
            print("Não há reclamações.")
        else:
            for i in range(len(bd_ouvidoria)):
                print(f"{i + 1}. {bd_ouvidoria[i]}")

    elif opcao == 2:
        texto = input("Digite a reclamação: ")
        bd_ouvidoria.append(texto)
        print("Reclamação registrada!")

    elif opcao == 3:
        if len(bd_ouvidoria) == 0:
            print("Não há reclamações para editar.")
        else:
            posicao = int(input("Digite o número da reclamação que deseja editar: "))
            if posicao >= 1 and posicao <= len(bd_ouvidoria):
                posicao = posicao - 1
                novo_texto = input("Digite o novo texto da reclamação: ")
                bd_ouvidoria[posicao] = novo_texto
                print("Editado com sucesso!")
            else:
                print("Posição inválida.")

    elif opcao == 4:
        if len(bd_ouvidoria) == 0:
            print("Não há reclamações para editar.")
        else:
            posicao = int(input("Digite o número da reclamação que deseja excluir: "))
            if posicao >= 1 and posicao <= len(bd_ouvidoria):
                posicao = posicao - 1
                bd_ouvidoria.pop(posicao)
                print("Reclamação excluída com sucesso!")
            else:
                print("Posição inválida.")

    elif opcao == 5:
        print(f"Quantidade de reclamações: {len(bd_ouvidoria)}")

    elif opcao == 6:
        print("Saindo do sistema de ouvidoria...")

    else:
        print("Opção inválida. Tente novamente.")