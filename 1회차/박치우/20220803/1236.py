N, M = map(int,input().split())

castle = [input().split() for i in range(N)]
count = 0
count_M = set([i for i in range(M)])
set_a = set()

for i in range(N):
    if 'X' not in castle[i]:
        count += 1
    for j in range(M):
        if castle[i][j] == 'X':
            set_a.add(j)

if len(count_M) - len(set_a) > count:
    print(len(count_M) - len(set_a))
else:
    print(count) 