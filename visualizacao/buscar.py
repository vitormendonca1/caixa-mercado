def buscar_produto (estoque):
    buscar = input("Digite o nome do produto que deseja buscar: ")
    if buscar not in estoque:
        print("Produto fora de estoque!")
    else:
      mostrar =  estoque[buscar]["Quantidade"]
      print(f"Produto: {buscar} | Quantidade: {mostrar}")