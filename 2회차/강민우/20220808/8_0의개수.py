T = int(input())
for test_case in range(T):
    N, M = map(int, input().split())
    count = 0
    for a in range(N,M+1):
        count += str(a).count('0')
    print(count)