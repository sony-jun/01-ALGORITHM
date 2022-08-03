T = int(input())

for i in range(1, T+1):
    side = list(map(int, input().split()))
    for j in side:
        if side.count(j) == 1 or side.count(j) == 3:
            print(f'#{i} {j}')
            break