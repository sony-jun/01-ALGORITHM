def Rev(a):
    b = str(a)
    c = b[::-1]
    d = int(c)
    return d
a, b = map(int, input().split())
print(Rev(Rev(a)+Rev(b)))