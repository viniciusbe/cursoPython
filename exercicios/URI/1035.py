A, B, C, D = map(int, input().split())

if B > C:
    if D > A:
        if (C+D) > (A+B):
            if C > 0 and D > 0:
                if A % 2 == 0:
                    print("Valores aceitos")
                else:
                    print("Valores nao aceitos")
            else:
                print("Valores nao aceitos")
        else:
            print("Valores nao aceitos")
    else:
        print("Valores nao aceitos")
else:
    print("Valores nao aceitos")
