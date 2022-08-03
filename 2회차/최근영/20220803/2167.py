import sys

N,M = map(int,sys.stdin.readline().split())

matrix = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]

K = int(sys.stdin.readline())

compare_list = [list(map(int,sys.stdin.readline().split())) for __ in range(K)]

for a in compare_list:
    sum_list = []
    y = a.pop()
    x = a.pop()
    j = a.pop()
    i = a.pop()
    for l in range(i-1,x):
        for k in range(j-1,y):
            sum_list.append(matrix[l][k])
    sum_list=sum(sum_list)
    print(sum_list)