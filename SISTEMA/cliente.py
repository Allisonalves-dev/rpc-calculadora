import xmlrpc.client

# Conecta ao servidor
proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

def menu():
    print("\n=== Cliente RPC - Calculadora Remota ===")
    print("1. Somar")
    print("2. Multiplicar")
    print("3. Dividir")
    print("4. Potência")
    print("5. Fatorial")
    print("0. Sair")
    return input("Escolha uma opção: ")

while True:
    opcao = menu()

    if opcao == "1":
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        print("Resultado:", proxy.somar(a, b))

    elif opcao == "2":
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        print("Resultado:", proxy.multiplicar(a, b))

    elif opcao == "3":
        a = float(input("Digite o dividendo: "))
        b = float(input("Digite o divisor: "))
        print("Resultado:", proxy.dividir(a, b))

    elif opcao == "4":
        base = float(input("Digite a base: "))
        expoente = float(input("Digite o expoente: "))
        print("Resultado:", proxy.potencia(base, expoente))

    elif opcao == "5":
        n = int(input("Digite um número inteiro para o fatorial: "))
        print("Resultado:", proxy.fatorial(n))

    elif opcao == "0":
        print("Saindo...")
        break

    else:
        print("Opção inválida. Tente novamente.")
