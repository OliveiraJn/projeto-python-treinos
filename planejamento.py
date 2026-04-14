def calcular_imc(peso, altura):
    return peso / (altura ** 2)


def gerar_plano(dados):
    nome = dados["nome"]
    idade = dados["idade"]
    objetivo = dados["objetivo"]
    dias = dados["dias"]
    horario = dados["horario"]
    peso = dados["peso"]
    altura = dados["altura"]

    imc = calcular_imc(peso, altura)

    print("\n=== PLANO PERSONALIZADO ===\n")

    print(f"Aluno: {nome}")
    print(f"Idade: {idade}")
    print(f"Dias disponíveis: {dias}")
    print(f"Horário: {horario}")
    print(f"IMC: {imc:.2f}")

    if objetivo == "1":
        print("\nObjetivo: Perda de peso")
        print("- Treinos intensos e movimentados")
        print("- Cardio + funcional")
        print("- Alta queima calórica")

    elif objetivo == "2":
        print("\nObjetivo: Ganho de massa")
        print("- Treinos de força")
        print("- Musculação + descanso")
        print("- Foco em hipertrofia")

    elif objetivo == "3":
        print("\nObjetivo: Lutar campeonatos")
        print("- Treinos intensos e técnicos")
        print("- Sparring frequente")
        print("- Preparação física avançada")

    else:
        print("\nOpção inválida")

    if idade < 18:
        print("\nObservação: Treino adaptado para menor de idade.")
    else:
        print("\nTreino padrão adulto.")

    if horario.lower() == "manhã":
        print("Recomendação: Começar leve e aumentar intensidade.")
    elif horario.lower() == "noite":
        print("Recomendação: Treino mais intenso liberado.")
    else:
        print("Treino equilibrado.")

    print("\nBons treinos! 💪")