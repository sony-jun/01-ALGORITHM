import sys
sys.stdin = open('test.txt', 'r')

n, m = list(map(int, input().split()))
mat = []
for i in range(n):
    line = []
    for j in range(n):
        line.append(0)
    mat.append(line)
start = [0, 0]
# 시작점
move = [[0, 1], [1, 0], [0, -1], [-1, 0]]
# 턴 0 일 때 왼쪽으로 90도 도는데 4번 반복되면 돌기 전의 방향으로 돌아오게 되어있다.
# 그래서 90씩 도는 값들을 순회할 수 있도록 델타이동 시킬 값을 저장해줍니다.
direction = 0
# 현재 이동중인 방향을 나타냅니다.
on = 1
# 보드 위에서 떨어졌는지 상태를 나타냅니다.
j, i = start
# 현재 위치를 지정해줍니다.
for _ in range(m):
    com = list(map(str, input().split()))
    if com[0] == 'MOVE':
        dj, di = move[direction % 4]
        nj = j + dj * int(com[1])
        ni = i + di * int(com[1])
        if nj in range(n) and ni in range(n):
            j, i = nj, ni
        else:
            on = 0
    else:
        if com[1] == '0':
            direction += 1
        else:
            direction += 3
            # 턴이 1일 경우 저장해준 순서의 반대 방향으로 도는데 이는 리스트를 순회하고 
            # 순회를 시작하기 전에 나타나던 방향 이전의 값과 동일하므로 1을 빼주는 것이 아니라 3을 더해줍니다.
if on == 1:
    print(i, j)
else:
    print(-1)