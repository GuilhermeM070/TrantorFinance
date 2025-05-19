class Pessoa:
    nome = input(f'Qual seu nome? ')
    salario = float(input(f'Qual seu salario? '))  
    print(f'Olá {nome}, pela informação que você nos forneceu, o seu salario é {salario}, faremos sua organização financeira, ok.')

def despesas():
    lista_despesas = []  # Lista para armazenar as despesas
    valor_final_despesas = 0

    while True:
        entrada = input("\nEscreva suas despesas e valores (ex: Aluguel 1200) ou digite 'sair' para encerrar e ver suas despesas: ")

        if entrada.lower() == 'sair':
            print("\nEncerrando o programa...\n")
            break

        try:
            # Divide a entrada em nome da despesa e valor
            nome, valor = entrada.rsplit(' ', 1)  
            valor = float(valor)  # Converte o valor para número
            lista_despesas.append((nome, valor))  # Adiciona à lista

        except ValueError:
            print("Erro: Formato inválido. Use o formato 'Nome Valor' (ex: 'Luz 150').")

    # Exibir todas as despesas
    print("\n=== Resumo das Despesas ===")
    for nome, valor in lista_despesas:
        print(f"- {nome}: R$ {valor:.2f}")

    valor_final_despesas = sum(valor for _, valor in lista_despesas) # Soma o valor de todas as despesas
    print(f"\nO valor total das despesas é: R$ {valor_final_despesas:.2f}")

    return valor_final_despesas # Retorna o valor total das despesas


def investimentos():
    categorias = {
        1: "Renda Fixa",
        2: "Criptomoedas",
        3: "FIIs",
        4: "Ações"
    }
    
    carteira = {categoria: [] for categoria in categorias.values()}  # Dicionário organizado por categorias

    while True:
        print("\nListaremos sua carteira de Ativos... \nCategorias disponíveis:")
        for k, v in categorias.items():
            print(f"{k} - {v}")

        try:
            escolha = int(input("\nEscolha a categoria do ativo (ou digite 0 para sair): "))
            if escolha == 0:
                break
            if escolha not in categorias:
                print("Opção inválida, tente novamente.")
                continue

            nome_ativo = input("Nome do ativo: ")
            valor = float(input("Valor investido: "))

            carteira[categorias[escolha]].append((nome_ativo, valor))
            print(f"✅ {nome_ativo} adicionado em {categorias[escolha]}!\n")

        except ValueError:
            print("Erro: Digite um número válido.")

    # Ordenando os ativos dentro de cada categoria por valor investido
    for categoria in carteira:
        carteira[categoria].sort(key=lambda x: x[1], reverse=True)

    # Exibindo o resumo final
    print("\n=== Resumo da Carteira ===")
    for categoria, ativos in carteira.items():
        if ativos:
            print(f"\n📌 {categoria}:")
            for ativo, valor in ativos:
                print(f"- {ativo}: R$ {valor:.2f}")

    return carteira  # Retorna os dados para serem usados na próxima classe


def reserva_emergencia(valor_final_despesas, carteira):
    print("\n=== Reserva de Emergência ===")
    print(f"\nSua Reserva de Emergência deve equivaler a no mínimo 6 meses de despesas mensais.")
    print(f'Suas despesas totais hoje são de R$ {valor_final_despesas:.2f}.')
    print(f"Abaixo está seu plano de reserva de emergência, baseado nos seus ativos de Renda Fixa:\n")

    # Acessando ativos de Renda Fixa dentro da carteira
    renda_fixa = carteira.get("Renda Fixa", [])

    if not renda_fixa:
        print("⚠️ Você não possui ativos de Renda Fixa cadastrados.")
        return
    
    # Soma o valor de todos os ativos de Renda Fixa da carteira
    valor_total_renda_fixa = sum(ativo[1] for ativo in renda_fixa)

    # Exibindo os ativos de Renda Fixa
    print("💰 Seus Ativos de Renda Fixa:")
    for ativo, valor in renda_fixa:
        print(f"- {ativo}: R$ {valor:.2f}")
        print(f'- Valor Total Investido: R$ {valor_total_renda_fixa:.2f}')

    # Calcula a reserva de emergência
    res_emergencia = valor_final_despesas * 6

    # Verifica se a reserva de emergência foi atingida
    if valor_total_renda_fixa >= res_emergencia:
        print("\n✅ Sua reserva de emergência foi atingida!")
    else:
        print("\n⚠️ Sua reserva de emergência ainda não foi atingida.")
        print(f'Falta R$ {res_emergencia - valor_total_renda_fixa:.2f} para atingir a reserva de emergência.')


# Fluxo do programa
valor_final_despesas = despesas()  # Chama a função despesas e obtém o total
carteira = investimentos()  # Chama a função investimentos e obtém a carteira
reserva_emergencia(valor_final_despesas, carteira)  # Chama a função reserva_emergencia