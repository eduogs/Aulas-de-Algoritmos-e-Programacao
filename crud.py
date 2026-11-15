#lista de compras

# CRUD simples de lista de compras

AVISO_VAZIO = "Você não digitou nada, tente novamente."

nomes = []
quantidades = []
precos = []
opcao = ""

while opcao != "5":
    print("")
    print("===== LISTA DE COMPRAS =====")
    print("1 - Adicionar item")
    print("2 - Ver lista")
    print("3 - Atualizar item")
    print("4 - Remover item")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")
    while opcao == "":
        print(AVISO_VAZIO)
        opcao = input("Escolha uma opção: ")

    # 1 - Adicionar item
    if opcao == "1":
        nome = input("Nome do item: ")
        while nome == "":
            print(AVISO_VAZIO)
            nome = input("Nome do item: ")

        quantidade = input("Quantidade: ")
        while quantidade == "":
            print(AVISO_VAZIO)
            quantidade = input("Quantidade: ")

        preco = input("Preço (R$): ")
        while preco == "":
            print(AVISO_VAZIO)
            preco = input("Preço (R$): ")

        nomes.append(nome)
        quantidades.append(quantidade)
        precos.append(preco)
        print("Item adicionado!")

    # 2 - Ver lista
    elif opcao == "2":
        print("")
        if len(nomes) == 0:
            print("A lista está vazia.")
        else:
            for i in range(len(nomes)):
                print(f"- {nomes[i]} (qtd: {quantidades[i]}) - R$ {precos[i]}")

    # 3 - Atualizar item
    elif opcao == "3":
        busca = input("Nome do item que quer atualizar: ")
        while busca == "":
            print(AVISO_VAZIO)
            busca = input("Nome do item que quer atualizar: ")

        encontrado = False
        i = 0
        while i < len(nomes) and not encontrado:
            if nomes[i] == busca:
                novo_nome = input("Novo nome: ")
                while novo_nome == "":
                    print(AVISO_VAZIO)
                    novo_nome = input("Novo nome: ")

                nova_quantidade = input("Nova quantidade: ")
                while nova_quantidade == "":
                    print(AVISO_VAZIO)
                    nova_quantidade = input("Nova quantidade: ")

                novo_preco = input("Novo preço (R$): ")
                while novo_preco == "":
                    print(AVISO_VAZIO)
                    novo_preco = input("Novo preço (R$): ")

                nomes[i] = novo_nome
                quantidades[i] = nova_quantidade
                precos[i] = novo_preco
                encontrado = True
            i += 1

        if encontrado:
            print("Item atualizado!")
        else:
            print("Item não encontrado.")

    # 4 - Remover item
    elif opcao == "4":
        busca = input("Nome do item que quer remover: ")
        while busca == "":
            print(AVISO_VAZIO)
            busca = input("Nome do item que quer remover: ")

        encontrado = False
        i = 0
        while i < len(nomes) and not encontrado:
            if nomes[i] == busca:
                quantidades.pop(i)
                precos.pop(i)
                nomes.remove(busca)
                encontrado = True
            i += 1

        if encontrado:
            print("Item removido!")
        else:
            print("Item não encontrado.")

    # Qualquer opção diferente de 1, 2, 3, 4 e 5 é inválida
    elif opcao != "5":
        print("Opção inválida, tente de novo.")

# Depois de sair: perguntar se a pessoa comprou tudo
resposta = ""
while resposta != "1" and resposta != "2":
    print("")
    print("Você comprou tudo?")
    print("1 - Sim")
    print("2 - Não")
    resposta = input("Escolha uma opção: ")

    if resposta == "":
        print(AVISO_VAZIO)
    elif resposta != "1" and resposta != "2":
        print("Opção inválida, tente de novo.")

if resposta == "1":
    print("")
    print("Ok, muito obrigado, até mais!")
else:
    print("")
    print("Vamos terminar de comprar!")
    print("")
    if len(nomes) == 0:
        print("A lista está vazia.")
    else:
        for i in range(len(nomes)):
            print(f"- {nomes[i]} (qtd: {quantidades[i]}) - R$ {precos[i]}")
