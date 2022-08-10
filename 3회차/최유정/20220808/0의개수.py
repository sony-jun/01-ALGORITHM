# https://www.acmicpc.net/problem/11170
T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    cnt = 0
    for i in range(N, M+1):
        stri = str(i)
        for j in stri:
            if j == '0':
                cnt += 1
    print(cnt)