def remover_produto (estoque):
    while True:
        print("Remover Produto! (y/n)")
        resposta = input("Oque deseja fazer, digite y/n: ")
        if resposta == "y":
            produto = input("Digite o nome do produto: ")
        
        elif resposta == "n":
            print("Movendo para a sessao de Atualizar!")
            atualizar(estoque)
            break    
        if produto in estoque:
            estoque.pop(produto)
            print("Produto removido!")
            print(estoque)

        if produto not in estoque:
            print("Produto nao esta no estoque")
            break