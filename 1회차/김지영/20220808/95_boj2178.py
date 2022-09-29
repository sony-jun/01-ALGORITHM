import sys
sys.stdin = open("95_input.txt")

def ppr(lst):
    for i in lst:
        print(i,end='\n')

# grid
# ['1', '0', '1', '1', '1', '1']
# ['1', '0', '1', '0', '1', '0']
# ['1', '0', '1', '0', '1', '1']
# ['1', '1', '1', '0', '1', '1']
# 진행방향 (0,0) -> (n,m) righit, down, up

n,m = map(int,input().split())
grid = []
for _ in range(n):
    temp = list(input())
    grid.append(temp)
# ppr(grid)
root = [] # 진행방향 판단을 위한 리스트
y,x = 0,0
while True:
    if y == n-1 and x == m-1:
        break
    if grid[y][x] == '1':

        # right
        if grid[y][x+1] == '1':
            root.append('right')
            x += 1

        # up, down을 왔다갔다하면 안되니까 경우를 나누자..
        # root에서 up,down 판단, 반대방향 x

        # down
        elif y+1 < n and (root == [] or root[-1] != 'up') and grid[y+1][x] == '1':   # range error, y = 3, [y+1] cannot found index
            # 'right' or 'down' can continue.
            root.append('down')
            y += 1
        # up
        elif y > 0 and (root == [] or root[-1] != 'down') and grid[y-1][x] == '1': 
            # 'righit or 'up' can continue.
            root.append('up')
            y -= 1
    

        print(root)
# 조건 덕지덕지 너무 싫다..엎을까..


# 탐색
# 1 
# x 1
# 1 
#     u  r d
# dx = [0,1,0]
# dy = [-1,0,1]
# 못써먹겠네!

# for x in range(m):
#     for y in range(n):
#         if grid[y][x] == '1':
            
#             # right 
#             if grid[y][x+1] == '1':
#                 nx = x + dx[1]
#                 ny = y + dy[1]
            
#             # down
#             if grid[y+1][x] == '1':
#                 if root == [] or root[-1] != 'up':
#                     nx = x + dx[2]
#                     ny = y + dy[2]
            
#             # up
#             if grid[y-1][x] == '1':
#                 if root == [] or root[-1] != 'down':
#                     nx = x + dx[0]
#                     ny = y + dy[0]
#         if 0<= nx < n and 0<= ny < m:
#             x = nx
#             y = ny
#         print(root)