n = int(input())
# n = 5
Q = {'Q1': 0, 'Q2': 0, 'Q3': 0, 'Q4': 0}
axs = 0

for _ in range(n):
    x, y = map(int, input().split())
    if x == 0 or y == 0:
        axs += 1
    elif x > 0 and y > 0:
        Q['Q1'] += 1
    elif x < 0 and y > 0:
        Q['Q2'] += 1
    elif x < 0 and y < 0:
        Q['Q3'] += 1
    else:
        Q['Q4'] += 1

for k, v in Q.items():
    print(f'{k}: {v}')
print(f'AXIS: {axs}')
