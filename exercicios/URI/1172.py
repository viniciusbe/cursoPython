vet = []
for i in range(10):
    N = int(input())
    if N <= 0:
        vet.append(1)
    else:
        vet.append(N)

for i in range(10):
    print("X[%d] = %d" % (i, vet[i]))
