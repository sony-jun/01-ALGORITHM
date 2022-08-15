cost = int(input())

cost_sum = 0
for _ in range(int(input())) :
    a, b = map(int, input().split())
    cost_sum += a * b

if cost == cost_sum :
    print('Yes')

else :
    print('No')