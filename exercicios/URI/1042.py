a, b, c = map(int, input().split())

if a < b:
    if a < c:
        if b < c:
            print(a)
            print(b)
            print(c)
        else:
            print(a)
            print(c)
            print(b)
    else:
        print(c)
        print(a)
        print(b)
elif b < c:
    if a < c:
        print(b)
        print(a)
        print(c)
    else:
        print(b)
        print(c)
        print(a)
else:
    print(c)
    print(b)
    print(a)
print("")
print(a)
print(b)
print(c)
