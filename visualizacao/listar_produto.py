def listar (estoque):
    for produto in estoque:
        total = estoque[produto]["Preco"] * estoque[produto]["Quantidade"]
        print(f"Esse é o valor total: {total}")