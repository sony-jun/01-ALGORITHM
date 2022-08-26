# import sys
# sys.setrecursionlimit(10**5)
# def dfs(i,j):
#     global c
#     c+=1
#     for k in range(4):
#         nx=dx[k]+i
#         ny=dy[k]+j
#         if 0<=nx<n and 0<=ny<m and not vist[nx][ny] and s[nx][ny]==1:
#             vist[nx][ny] = True
#             dfs(nx,ny)

# n,m = map(int,input().split())
# s = [list(map(int,input().split())) for _ in range(n)]
# dx=[1,-1,0,0]
# dy=[0,0,1,-1]
# maxs =0
# count=0
# vist = [[False]*m for _ in range(n)]
# for i in range(n):
#     for j in range(m):
#         if s[i][j]==1 and not vist[i][j]:
#             c =0
#             vist[i][j] =True
#             count+=1
#             dfs(i,j)
#             maxs = max(maxs,c)
# print(count)
# print(maxs)\


R = chr(97)
# st[0]= ord(st[0])
print (R)