T = int(input())

for _ in range(T):
    S = int(input())
    N = int(input())
    parts = 0
    for _ in range(N):
        a, b = map(int, input().split())
        parts += a*b

    print(S+parts)
