class Pessoa:
    nome = input(f'Qual seu nome? ')
    salario = float(input(f'Qual seu salario? '))  
    print(f'Olá {nome}, pela informação que você nos forneceu, o seu salario é {salario}, faremos sua organização financeira, ok.')

def despesas():
    lista_despesas = []  # Lista para armazenar as despesas

    while True:
        entrada = input("\nEscreva suas despesas e valores (ex: Aluguel 1200) ou digite 'sair' para encerrar: ")

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

    valor_final = sum(valor for _, valor in lista_despesas) # Soma o valor de todas as despesas
    print(f"\nO valor total das despesas é: R$ {valor_final:.2f}")
valor_final = despesas()
# Chamar a função
despesas()


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
carteira = investimentos()
# Chamar a função
investimentos()


def reserva_emergencia(valor_final, carteira):
    print("\n=== Reserva de Emergência ===")
    print(f"\nSua Reserva de Emergência equivale a no mínimo 6 meses de despesas mensais.\n")
    print(f"🔹 Sua reserva deve ser de R$ {valor_final:.2f}\n")
    print(f"Abaixo está seu plano de reserva de emergência, baseado nos seus ativos de Renda Fixa:\n")

    print(f"🔹 Meta de reserva: R$ {valor_final * 6:.2f}\n")

    # Acessando ativos de Renda Fixa dentro da carteira
    renda_fixa = carteira.get("Renda Fixa", [])

    if not renda_fixa:
        print("⚠️ Você não possui ativos de Renda Fixa cadastrados.")
        return

    print("💰 Seus Ativos de Renda Fixa:")
    for ativo, valor in renda_fixa:
        print(f"- {ativo}: R$ {valor:.2f}")
# Chamar a função 
reserva_emergencia(valor_final, carteira)

