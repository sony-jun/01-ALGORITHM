times = int(input())
count = [0, 0, 0, 0, 0]
for i in range(times):
    x, y = map(int, input().split())
    if x == 0 or y == 0:
        count[4] += 1
    elif x > 0:
        if y > 0:
            count[0] += 1
        elif y < 0:
            count[3] += 1
    elif x < 0:
        if y < 0:
            count[2] += 1
        else:
            count[1] += 1
print(f'Q1: {count[0]}')
print(f'Q2: {count[1]}')
print(f'Q3: {count[2]}')
print(f'Q4: {count[3]}')
print(f'AXIS: {count[4]}')