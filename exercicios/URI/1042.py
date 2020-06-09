a, b, c = map(int, input().split())

if a < b:
    if a < c:
        print(a)
    elif c < b:
        print(c)
        print(a)
        print(b)