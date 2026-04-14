def cadastrar_usuario():
    nome = input("Qual é o seu nome? ")
    idade = int(input("Qual é a sua idade? "))
    peso = float(input("Qual é o seu peso? (kg) "))
    altura = float(input("Qual é a sua altura? (m) "))

    print("\nObjetivos disponíveis:")
    print("1 - Perder peso")
    print("2 - Ganhar massa")
    print("3 - Lutar campeonatos")

    objetivo = input("Escolha o número do seu objetivo: ")

    dias = input("Quais dias você pode treinar? ")
    horario = input("Qual horário prefere? (manhã/tarde/noite) ")

    return {
        "nome": nome,
        "idade": idade,
        "peso": peso,
        "altura": altura,
        "objetivo": objetivo,
        "dias": dias,
        "horario": horario
    }