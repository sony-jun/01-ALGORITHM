import sys

sys.stdin = open("input.txt", "r")

n, m = map(int, input().split())
a = [list(input()) for _ in range(n)]
truck = []

for x in range(n-1):
    for y in range(m-1):
        truck.append([a[x][y],a[x+1][y],a[x][y+1],a[x+1][y+1]])

result = 0

for i in range(len((truck))):
    if '#' in truck[i]:
        continue

    if truck[i].count('.') == 4:
        result += 1
print(result)

for i in range(1,5):
    result = 0
    for j in range(len(truck)):
        if '#' in truck[j]:
            continue
        if truck[j].count('X') == i:
            result += 1
    print(result)