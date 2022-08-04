T = int(input())

for _ in range(T):
    m, n = map(int, input().split())

    grid = [[] for __ in range(n)]
    for i in range(m):
        line = input().split()
        
        for j in range(n):
            grid[j].append(int(line[j]))

    ret = 0
    for i in range(n):
        temp = sorted(grid[i])

        while 1 in temp:
            ret += temp.index(1) - grid[i].index(1)
            temp.remove(1)
            grid[i].remove(1)

    print(ret)

# https://www.acmicpc.net/source/47170599
# 아래 코드가 훨씬 좋다.
# import sys

# input = sys.stdin.readline

# T = int(input())
# for _ in range(T):
#     m, n = map(int, input().split())
#     arr = [list(map(int, input().split())) for _ in range(m)]
    
#     count = 0 
#     for j in range(n):
#         h = m-1
#         for i in range(m-1, -1, -1):
#             if arr[i][j] == 1:
#                 count += (h-i)
#                 h -= 1

#     print(count)