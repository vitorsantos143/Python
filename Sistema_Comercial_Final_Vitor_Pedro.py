print("=== SISTEMA COMERCIAL ===")


# Autenticação do sistema
def autenticar():
    usuario_correto = "admin"
    senha_correta = "1234"
    tentativas = 0

    while tentativas < 3:
        usuario = input("Digite o login: ")
        senha = input("Digite a senha: ")

        if usuario == usuario_correto and senha == senha_correta:
            print("Login realizado com sucesso!")
            return True
        else:
            tentativas += 1
            print("Login ou senha incorretos.")

    print("Acesso bloqueado.")
    return False


# Valida os valores digitados
def ler_valor(tipo):
    while True:
        try:
            if tipo == "pedido":
                valor = float(input("Digite o valor do pedido: R$ "))
            else:
                valor = float(input("Digite o valor da renovacao: R$ "))

            if valor <= 0:
                print("Valor inválido. Digite um valor maior que zero.")
            else:
                return valor
        except ValueError:
            print("Entrada inválida. Digite somente números.")


# Regras usadas em Pedido e Renovacao
def processar_operacao(tipo, valor):
    if valor < 1000:
        print(tipo + " sem desconto.")
        print("Valor final: R$ %.2f" % valor)

    elif valor <= 5000:
        desconto = valor * 0.12
        total = valor - desconto

        print("Desconto aplicado: 12%")
        print("Valor do desconto: R$ %.2f" % desconto)
        print("Valor final: R$ %.2f" % total)

    else:
        while True:
            if tipo == "Pedido":
                aprovacao = input("Gestor aprovou o pedido? (sim/nao): ").lower()
            else:
                aprovacao = input("Gestor aprovou a renovacao? (sim/nao): ").lower()

            if aprovacao == "sim":
                desconto = valor * 0.15
                total = valor - desconto

                print("Operação aprovada.")
                print("Desconto aplicado: 15%")
                print("Valor do desconto: R$ %.2f" % desconto)
                print("Valor final: R$ %.2f" % total)
                break

            elif aprovacao == "nao":
                print("Operação recusada.")
                break

            else:
                print("Opção inválida. Digite sim ou nao.")


if autenticar():
    print("\n=== PEDIDO ===")
    valor_pedido = ler_valor("pedido")
    processar_operacao("Pedido", valor_pedido)

    print("\n=== RENOVACAO ===")
    valor_renovacao = ler_valor("renovacao")
    processar_operacao("Renovacao", valor_renovacao)

print("\n=== FIM DO SISTEMA ===")
