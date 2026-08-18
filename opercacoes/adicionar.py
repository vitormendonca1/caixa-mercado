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