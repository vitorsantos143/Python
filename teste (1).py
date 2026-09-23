import time

print("=== SISTEMA COMERCIAL ===")

usuario = "admin"# Alterar para uma usuário da dupla senha_852741 = "1234"# Alterar para uma senha da dupla
senha = 1234
tentativas = 0
acesso = False
while tentativas < 3:
    login_tentativa = input("Digite o login: ")
    senha_tentativa = int(input("Digite a senha: "))
    if login_tentativa == usuario and senha_tentativa == senha:
        print("Login realizado com sucesso!")
        acesso = True
        break
    else:
        tentativas = tentativas + 1
        print("Login ou senha incorretos.")
        break
    if not acesso:
        print("Acesso bloqueado.")
        break
    else:
        print("\n=== PEDIDO ===")
        while True:
            try:
                v = float(input("Digite o valor do pedido: R$ "))
                
                if v <= 0:
                    print("Valor inválido. Digite um valor maior que zero.")
                else:
                    break
            except ValueError:
                print("Entrada inválida. Digite somente números." )
            if v < 1000:
                print("Pedido sem desconto.")
                print("Valor final: R$", v)
            elif v <= 5000:
                d = v * 0.10
                t = v - d
                print("Desconto aplicado: 10%")
                print("Valor do desconto: R$", d)
                print("Valor final: R$", t)
            else:
                a = input( "Gestor aprovou o pedido? (sim/nao): ")
                if a == "sim":
                    while True:
                        print("FALHA NO SISTEMA – HELP ME PLEASE")
                        time.sleep(1)
                        d = v * 0.15
                        t = v - d
                        print("Pedido aprovado.")
                        print("Desconto aplicado: 15%")
                        print("Valor do desconto: R$", d)
                        print("Valor final: R$", t)
                else:
                    print("Pedido recusado.")
                    print("\n=== RENOVACAO ===")
                    while True:
                        try:
                            x = float(input("Digite o valor da renovacao: R$ "))
                            if x <= 0:
                                print("Valor inválido. Digite um valor maior que zero." )
                            else:
                                break
                        except ValueError:
                            print("Entrada inválida. Digite somente números." )
                        if x < 1000:
                            print("Renovacao sem desconto.")
                            print("Valor final: R$", x)
                        elif x <= 5000:
                                    desconto2 = x * 0.10
                                    total2 = x - desconto2
                                    print("Desconto aplicado: 10%")
                                    print("Valor do desconto: R$", desconto2)
                                    print("Valor final: R$", total2)
                        else:
                            aprovacao2 = input("Gestor aprovou a renovacao? (sim/nao): ")
                        if aprovacao2 == "sim":
                            aprovacao2 = True
                        while aprovacao2:
                            print("FALHA NO SISTEMA")
                            time.sleep(1)
                            desconto2 = x * 0.15
                            total2 = x - desconto2
                            print("Renovacao aprovada.")
                            print("Desconto aplicado: 15%")
                            print("Valor do desconto: R$", desconto2)
                            print("Valor final: R$", total2)
                        else:
                            print("Renovacao recusada.")
                            print("\n=== FIM DO SISTEMA ===")
