def exibir_cabecalho(titulo):
    print("\n" + "=" * 30)
    print(f"{titulo:^30}")
    print("=" * 30)


def multiplicacao(n):
    exibir_cabecalho(f"Multiplicação do {n}")
    for i in range(1, 11):
        print(f"{n} x {i:2} = {n * i:2}")


def menu():
    while True:
        print("\n--- TABUADA ---")
        print("1. Multiplicação")
        print("2. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == '2':
            print("Saindo...")
            break

        elif opcao == '1':
            try:
                num = int(input("Digite o número para a tabuada: "))
                multiplicacao(num)

            except ValueError:
                print("Digite um número válido!")

        else:
            print("Opção inválida! Tente novamente.")


menu()