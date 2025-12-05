print("Serviço de escolha de nome para animais de estimação")
print("-------------------------------------------------------")

nomes_macho = ["Thor", "Billy", "Max"]
nomes_femea = ["Akira", "Mega", "Mel"]
nomes_outros = ["Pipoca", "Nino", "Bolinha"]

while True:
    print("\nO que deseja fazer?")
    print("1 - Ver listas de nomes")
    print("2 - Adicionar nome")
    print("3 - Remover nome")
    print("4 - Escolher nome(s) para seu animal")
    print("5 - Sair")

    opc = input("Escolha: ")

    # Mostrar listas
    if opc == "1":
        print("\nNomes para machos:", nomes_macho)
        print("Nomes para fêmeas:", nomes_femea)
        print("Nomes para outros animais:", nomes_outros)

    # Adicionar nome
    elif opc == "2":
        categoria = input("O nome é para macho (m), fêmea (f) ou outro (o)? ").lower()
        nome = input("Digite o nome a adicionar: ").strip()

        if categoria == "m":
            lista = nomes_macho
        elif categoria == "f":
            lista = nomes_femea
        else:
            lista = nomes_outros

        if nome not in lista:
            lista.append(nome)
            print("Nome adicionado!")
        else:
            print("Este nome já existe na lista.")

    # Remover nome
    elif opc == "3":
        categoria = input("Remover de macho (m), fêmea (f) ou outro (o)? ").lower()
        nome = input("Nome a remover: ")

        if categoria == "m":
            lista = nomes_macho
        elif categoria == "f":
            lista = nomes_femea
        else:
            lista = nomes_outros

        if nome in lista:
            lista.remove(nome)
            print("Nome removido!")
        else:
            print("Nome não encontrado.")

    # Escolher nome(s)
    elif opc == "4":
        categoria = input("Seu animal é macho (m), fêmea (f) ou outro (o)? ").lower()
        qtd = int(input("Quantos nomes você precisa? "))

        if categoria == "m":
            lista = nomes_macho
        elif categoria == "f":
            lista = nomes_femea
        else:
            lista = nomes_outros

        print("\nSugestões de nomes:")
        for i in range(min(qtd, len(lista))):
            print(f"- {lista[i]}")

    elif opc == "5":
        print("Encerrando o serviço. Até logo!")
        break

    else:
        print("Opção inválida!")
