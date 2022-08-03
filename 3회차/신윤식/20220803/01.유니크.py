# https://www.acmicpc.net/problem/5533

N = int(input())

matrix = [list(map(int,input().split())) for _ in range(N)]

score = [0] * N
lst2 = []

for i in range(3):
    lst = []
    for j in range(N):
        lst.append(matrix[j][i]) 
    lst2.append(lst)

for i in range(3):
    for j in range(N):
        if lst2[i].count(matrix[j][i]) == 1:
            score[j] += matrix[j][i]

for _ in score:
    print(_)