'''Função de exibir o cabeçalho'''
def exibir_cabecalho(titulo):
    print("\n" + "=" * 30)
    print(f"{titulo:^30}")
    print("=" * 30)

'''Função de soma'''
def soma(n):
    exibir_cabecalho(f"Soma do {n}")
    for i in range(1, 11):
        print(f"{n} + {i:2} = {n + i:2}")

'''Função de subtração'''
def subtracao(n):
    exibir_cabecalho(f"Subtração do {n}")
    for i in range(1, 11):
        print(f"{n} - {i:2} = {n - i:2}")

'''Função de multiplicação'''
def multiplicacao(n):
    exibir_cabecalho(f"Multiplicação do {n}")
    for i in range(1, 11):
        print(f"{n} x {i:2} = {n * i:2}")

'''Função de menu'''
def menu():
    while True:
        print("\n--- TABUADA ---")
        print("1. Soma")
        print("2. Subtração")
        print("3. Multiplicação")
        print("4. Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == '4':
            print("Saindo...")
            break

        elif opcao in ['1', '2', '3']:
            try:
                num = int(input("Digite o número para a tabuada: "))

                if opcao == '1':
                    soma(num)

                elif opcao == '2':
                    subtracao(num)

                elif opcao == '3':
                    multiplicacao(num)

            except ValueError:
                print("Digite um número válido!")

        else:
            print("Opção inválida! Tente novamente.")


menu()