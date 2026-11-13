#lista de compras

# CRUD simples de lista de compras

TAMANHO= 50
nomes = [""] * TAMANHO
quantidades = [""] * TAMANHO
opcao = ""

while opcao != "5":
    print("")
    print("===== LISTA DE COMPRAS =====")
    print("1 - Adicionar item")
    print("2 - Ver lista")
    print("3 - Atualizar item")
    print("4 - Remover item")
    print("5 - Sair")
    opcao = input("Escolha uma opcao: ")

    # adiciona
    if opcao == "1":
        nome = input("Nome do item: ")
        quantidade = input("Quantidade: ")

        adicionado = False
        i = 0
        while i < TAMANHO and not adicionado:
            if nomes [i] == "":
                nomes [i] = nome
                quantidades [i] = quantidade
                adicionado = True
            i += 1

        if adicionado:
            print("Item adicionado!")
        else:
            print("A lista esta cheia.")
    # lista
    elif opcao == "2":
        tem_item = False
        print("")
        i = 0
        for nome in nomes:
            if nome != "":
                print("- " + nome + " (qtd: " + quantidades[i] + ")")
                tem_item = True
            i += 1 

        if tem_item == False:
            print("A lista esta vazia.")

    #  atualiza
    elif opcao == "3":
        busca = input("Nome do item que quer atualizar: ")

        encontrado = False
        i = 0
        while i < TAMANHO and not encontrado:
            if nomes[i] == busca:
                novo_nome = input("Novo nome: ")
                nova_quantidade = input("Nova quantidade: ")
                nomes[i] = novo_nome
                quantidades[i] = nova_quantidade
                encontrado = True
            i +=1 

        if encontrado == True:
            print("Item atualizado!")
        else:
            print("Item não encontrado.")

    # remove
    elif opcao == "4":
        busca = input("Nome do item que quer remover: ")

        encontrado = False
        i = 0
        while i < TAMANHO and not encontrado:
            if nomes[i] == busca:
                nomes[i] = ""
                quantidades[i] = ""
                encontrado = True
            i += 1

        if encontrado:
            print("Item removido!")
        else:
            print("Item nao encontrado.")

    elif opcao == "5":
        print("Ate mais!")

    else:
        print("Opcao invalida, tente de novo.")
