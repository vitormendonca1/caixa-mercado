from opercacoes import adicionar,atualizar_produto,remover
from visualizacao import buscar,listar_produto


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
        adicionar.adcionar_produto(estoque)
    elif opcao == "2":
        remover.remover_produto(estoque)
    elif opcao == "3":
        atualizar_produto.atualizar(estoque)
    elif opcao == "4":
        listar_produto.listar(estoque)
    elif opcao == "5":
        buscar.buscar_produto(estoque)

    elif opcao == "6":
        break
    elif opcao not in opcoes:
        print("Opcao Inválida")