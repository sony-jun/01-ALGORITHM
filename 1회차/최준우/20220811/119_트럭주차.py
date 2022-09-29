# https://www.acmicpc.net/problem/2979

A, B, C = map(int, input().split()) # 주차요금 A, B, C
temp = [[0] * 101 for _ in range(3)] # 임시 시간표 1<= <=100

for i in range(3):
    t1, t2 = map(int, input().split())
    for j in range(t1+1, t2+1):
        temp[i][j] = 1

result = 0
for i in range(101):
    cnt = 0
    if temp[0][i] == 1:
        cnt += 1 
    if temp[1][i] == 1:
        cnt += 1
    if temp[2][i] == 1:
        cnt += 1
    if cnt == 1:
        result += A * cnt
    elif cnt == 2:
        result += B * cnt
    elif cnt == 3:
        result += C * cnt
print(result)