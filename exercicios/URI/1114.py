senha = 2002
tentativa = 0
while senha != tentativa:
    tentativa = int(input())
    if senha == tentativa:
        print("Acesso Permitido")
    else:
        print("Senha Invalida")
