def cria_menu(opcoes):
    """
    Exibe um menu interativo e executa a função escolhida.

    Args:
        opcoes (list[str]): Lista com os nomes das opções do menu.
        funcoes (list[callable]): Lista de funções correspondentes
            a cada opção.

    Returns:
        None

    Observações:
        As listas opcoes e funcoes devem ter o mesmo tamanho.
        A opção 0 encerra o menu.
        As funções não devem exigir parâmetros.
    """
    while True:
        print("\n===== MENU =====")

        for i, (nome, funcao) in enumerate(opcoes, start=1):
            print(f"{i} - {nome}")

        print("0 - Sair")

        escolha = input("Escolha: ")

        if escolha == "0":
            break

        if escolha.isdigit() and 1 <= int(escolha) <= len(opcoes):
            opcoes[int(escolha) - 1][1]()
        else:
            print("Opção inválida!")
