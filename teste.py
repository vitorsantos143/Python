import time

print("=== SISTEMA COMERCIAL ===")

usuario_adm = "admin"
senha_entrada = "Abc12345!"
tentativas = 0
acesso = False

while tentativas < 3:
    usario = input("Digite o login: ")
    senha = input("Digite a senha: ")
 
    if usario == usuario_adm and senha == senha_entrada:
        print("Login realizado com sucesso!")
    acesso = True
    break
else:
    tentativas = tentativas + 1
    print("Login ou senha incorretos.")

if not acesso:
    print("Acesso bloqueado.")

else:
    print("\n=== PEDIDO ===")

while True:
    try:
        valor = float(input("Digite o valor do pedido: R$ "))

        if valor <= 0:
            print("Valor inválido. Digite um valor maior que zero.")
        else:
            break
    except ValueError:
        print("Entrada inválida. Digite somente números.")

if valor < 1000:
    print("Pedido sem desconto.")
    print("Valor final: R$", valor)
 
elif valor <= 5000:
    desconto = valor * 0.10
    total = valor - desconto

    print("Desconto aplicado: 10%")
    print("Valor do desconto: R$", desconto)
    print("Valor final: R$", total)

else:
    renovacao = input("Gestor aprovou o pedido? (sim/nao): ")
    if renovacao == "sim":
        while True:
            print("FALHA NO SISTEMA – HELP ME PLEASE")
        time.sleep(1)

        desconto = valor * 0.15
        total = valor - desconto
 
        print("Pedido aprovado.")
        print("Desconto aplicado: 15%")
        print("Valor do desconto: R$", desconto)
        print("Valor final: R$", total)

    else:
        print("Pedido recusado.")
        print("\n=== RENOVACAO ===")
while True:
    try:
        renovacao = float(input("Digite o valor da renovacao: R$ "))
        if renovacao <= 0:
            print("Valor inválido. Digite um valor maior que zero.")
        else:
            break
    except ValueError:
        print("Entrada inválida. Digite somente números.")
if renovacao < 1000:
    print("Renovacao sem desconto.")
    print("Valor final: R$", renovacao)
    
elif renovacao <= 5000:
    desconto2 = renovacao * 0.10
    total2 = renovacao - desconto2
    print("Desconto aplicado: 10%")
    print("Valor do desconto: R$", desconto2)
    print("Valor final: R$", total2)
    
else:
    renovacao = input("Gestor aprovou a renovacao? (sim/nao): ")
    
if renovacao == "sim":
    while True:
        print("FALHA NO SISTEMA")
        time.sleep(1)
        desconto2 = renovacao * 0.15
        total2 = renovacao - desconto2
        print("Renovacao aprovada.")
        print("Desconto aplicado: 15%")
        print("Valor do desconto: R$", desconto2)
        print("Valor final: R$", total2)

else:
    print("Renovacao recusada.")

print("\n=== FIM DO SISTEMA ===")
