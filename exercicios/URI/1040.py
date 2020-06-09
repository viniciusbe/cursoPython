p1, p2, p3, p4 = map(float, input().split())

media = (p1*2 + p2*3 + p3*4 + p4)/10

print("Media: %.1f" % media)

if media >= 7:
    print("Aluno aprovado.")
elif media < 5:
    print("Aluno reprovado.")
else:
    print("Aluno em exame.")
    exame = float(input())
    print("Nota do exame: %.1f" % exame)
    mediaFinal = (exame + media)/2
    if mediaFinal >= 5:
        print("Aluno aprovado.")
    else:
        print("Aluno reprovado.")
    print("Media final: %.1f" % mediaFinal)
