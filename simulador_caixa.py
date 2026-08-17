estoque = {}
def adcionar_produto(estoque):
    print("Adcionar Produto!")
    produto = str(input("Digite o nome do produto: "))
    if produto in estoque:
        print("Produto ja existe no estoque!")
    else:
        try:
            preco = float(input("Digite o preço do produto:"))
            quantidade = int(input("Digite a quantidade:"))
        except ValueError:
            print("Digite Um Valor Válido!\n" *10)
            return
        estoque[produto] = {"Preco": preco , "Quantidade": quantidade}
        print("Produto Adcionado com Sucesso!")
        print(estoque)

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

def atualizar (estoque):
    produto = input("Qual produto quer atualizar: ")
    if produto not in estoque:
        print("Produto selecionado nao esta no estoque!")
    else:
        controle = str(input("Voce deseja Adcionar ou remover do estoque: ")) .capitalize()
        quantidadeAtual = estoque[produto]["Quantidade"]
        if controle == "Adcionar":
            quantidade = int(input("Qual a quantidade que deseja adcionar: "))
            quantidadeSoma = quantidadeAtual + quantidade
            estoque[produto]["Quantidade"] = quantidadeSoma
            print(f"Essa é a quantidade nova: {quantidadeSoma}")
        
        elif controle == "remover":
            quantidade = int(input("Qual a quantidade que deseja remover: "))                                                                                           
            quantidadeSubtracao = quantidadeAtual - quantidade
            estoque[produto]["Quantidade"] = quantidadeSubtracao
            print(f"Essa é a quantidade nova: {quantidadeSubtracao}")


def listar (estoque):
    for produto in estoque:
        total = estoque[produto]["Preco"] * estoque[produto]["Quantidade"]
        print(f"Esse é o valor total: {total}")


def buscar_produto (estoque):
    buscar = input("Digite o nome do produto que deseja buscar: ")
    if buscar not in estoque:
        print("Produto fora de estoque!")
    else:
      mostrar =  estoque[buscar]["Quantidade"]
      print(f"Produto: {buscar} | Quantidade: {mostrar}")    




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
     