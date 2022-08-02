T = int(input())


for i in range(1,T+1):
    a, b, c = map(int, input().split())
    if a == b and b!=c:
        d = c
    elif a == c and b!=c:
        d = b
    elif b == c and b!=a:
        d = a
    elif a == b == c:
        d = a
    print(f'#{i} {d}')