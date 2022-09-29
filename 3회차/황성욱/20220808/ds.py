dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
x = 0
y = 0
while x != 4:
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and ny >= 0:
            x += nx
            y += ny
        print(x, y)
