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