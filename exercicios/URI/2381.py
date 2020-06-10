vet = []
alunos, sorteado = map(int, input().split())

for i in range(alunos):
    aluno = input()
    vet.append(aluno)

vet.sort()
print(vet[sorteado-1])
