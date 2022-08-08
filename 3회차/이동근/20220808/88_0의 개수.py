T = int(input())

for _ in range(T):
    N, M = map(int, input().split())

    ret = 0
    for i in range(N, M + 1):
        ret += str(i).count('0')

    print(ret)