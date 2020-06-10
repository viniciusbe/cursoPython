distanciaTotal = 0

N = int(input())

for i in range(N):
    T, V = map(int, input().split())
    distanciaTotal += T * V
    
print(distanciaTotal)
