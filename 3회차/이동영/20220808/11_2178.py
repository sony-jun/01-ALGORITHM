from collections import deque
import sys

sys.stdin = open("input.txt", "r")

def func(x,y):
   b = deque()
   b.append((x,y))

   while b:
       x, y = b.popleft()
       for i in range(4):
           nx = x + dx[i]
           ny = y + dy[i]
           
           if nx < 0 or nx >= n or ny < 0 or ny >= m:
               continue
           
           if a[nx][ny] == 0:
               continue
           
           if a[nx][ny] == 1:
               a[nx][ny] = a[x][y] + 1
               b.append((nx, ny))
   return a[n-1][m-1]

n, m = map(int, input().split())
a = [list(map(int,input())) for _ in range(n)]
print(a)
dx = [0,0,-1,1]
dy = [-1,1,0,0]

print(func(0,0))