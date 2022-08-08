N, M = map(int, input().split())

fish = [list(input()) for _ in range(N)]

for i in fish :
    print(''.join(i[::-1]))