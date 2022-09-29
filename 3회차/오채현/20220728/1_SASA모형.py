n, m = map(int, input().split())

if n / 2 == m / 2:
    print(int(n/2))
else:
    print(int(min(n / 2, m / 2)))
