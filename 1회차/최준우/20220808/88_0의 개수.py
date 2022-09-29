# https://www.acmicpc.net/problem/11170

T = int(input())

for test_case in range(T):
    N, M = map(int, input().split())
    result = 0

    for i in range(N, M+1):
        for j in str(i):
            if j == '0':
                result += 1
    print(result)