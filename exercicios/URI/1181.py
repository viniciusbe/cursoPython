n = 12
M = [[0 for i in range(n)] for j in range(n)]

linha = int(input())
operacao = input()

for i in range(n):
    for j in range(n):
        M[i][j] = float(input())

resultado = 0
soma = 0
for i in range(n):
    soma += M[linha][i]
    if operacao == 'S':
        resultado = soma
    else:
        resultado = soma/n

print(resultado)
