hang, yeol = map(int, input().split())
metrix = []

for i in range(hang):
    base = list(map(int, input().split()))
    for i in range(1, len(base)):
        base[i] += base[i - 1]
    metrix.append(base)

print(metrix)
times = int(input())

for _ in range(times):
    s1, s2, f1, f2 = map(int, input().split())
    result = 0
    for i in range(s1 - 1, f1):
        if s2 == 1:
            result += metrix[i][f2 - 1]
        else:
            result += metrix[i][f2 - 1] - metrix[i][s2 -2]
    print(result)