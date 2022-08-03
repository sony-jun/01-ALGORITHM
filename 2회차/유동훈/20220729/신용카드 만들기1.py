T = int(input())

for i in range(1, T+1):
    numbers = list(map(int, input().split()))
    N = 0

    for j in range(15):
        if (j+1) % 2 == 1: 
            N += numbers[j]*2
        else: 
            N += numbers[j]

    for k in range(10):
        if (N + k) % 10 == 0:
            print(f'#{i} {k}')
            break