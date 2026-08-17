estoque = {}
while True:
    opcoes = [print("1 - Adicionar produto"),
    print("2 - Remover produto"),
    print("3 - Atualizar produto"),
    print("4 - Listar produtos"),
    print("5 - Buscar produto"),
    print("6 - Sair")]
    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        adcionar_produto(estoque)
    elif opcao == "2":
        remover_produto(estoque)
    elif opcao == "3":
        atualizar(estoque)
    elif opcao == "4":
        listar(estoque)
    elif opcao == "5":
        buscar_produto(estoque)

    elif opcao == "6":
        break
    elif opcao not in opcoes:
        print("Opção Invalida")