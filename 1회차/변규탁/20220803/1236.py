N, M = map(int, input().split())

castle = [list(input()) for _ in range(N)]

count_N = 0
count_M = 0

for i in range(N):
    if "X" not in castle[i]:
        count_N += 1

castle2 = []
temp = []
for i in range(M):
    for j in range(N):
        temp.append(castle[j][i])
    castle2.append(temp)
    temp = []

for i in range(M):
    if "X" not in castle2[i]:
        count_M += 1
       

print(max(count_N, count_M))