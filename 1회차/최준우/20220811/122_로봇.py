# https://www.acmicpc.net/problem/13567

M, n = map(int, input().split())
x = 0
y = 0
direction = 0
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
result = 1

for _ in range(n):
    action, num = input().split()
    num = int(num)

    if action == 'MOVE':
        temp_x = x + dx[direction] * num
        temp_y = y + dy[direction] * num

        if 0 <= temp_x <= M and 0 <= temp_y <= M:
            x = temp_x
            y = temp_y
        else:
            result = -1
    elif action == 'TURN':
        if num == 0:
            direction -= 1
            if direction == -1:
                direction = 3
        else:
            direction += 1
            if direction == 4:
                direction = 0
if result != -1:
    print(x, y)
else:
    print(-1)