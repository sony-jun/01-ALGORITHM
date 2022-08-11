import sys
sys.stdin = open("input.txt")
input = sys.stdin.readline

m, n = map(int, input().split())
x = 0
y = 0
direction = 0

com = []
d = []
ans = []

for i in range(n):
    # 입력 받은 값들 리스트에 넣기
    com_, d_ = input().split()
    com.append(com_)
    d.append(int(d_))

for i in range(n):
    # command가 TURN이면
    if com[i] == 'TURN':
        # 왼쪽으로 90도 회전
        if d[i] == 0:
            if direction == 0:
                direction = 2
            elif direction == 1:
                direction = 3
            elif direction == 2:
                direction = 1
            elif direction == 3:
                direction = 0
        # 오른쪽으로 90도 회전
        elif d[i] == 1:
            if direction == 0:
                direction = 3
            elif direction == 1:
                direction = 2
            elif direction == 2:
                direction = 0
            elif direction == 3:
                direction = 1
    # command가 MOVE이면
    elif com[i] == 'MOVE':
        # 방향에 따라 x, y에 1씩 더하기
        if direction == 0:
            for j in range(int(d[i])):
                x += 1
        elif direction == 1:
            for j in range(int(d[i])):
                x -= 1
        elif direction == 2:
            for j in range(int(d[i])):
                y += 1
        elif direction == 3:
            for j in range(int(d[i])):
                y -= 1
    # 명령어 열이 유효하지 않으면
    if(x < 0 or x > m or y < 0 or y > m):
        # ans 리스트에 -1 추가
        ans.append(-1)

# ans 리스트에 -1이 하나라도 있다면
if -1 in ans:
    # -1 출력
    print(-1)
# ans 리스트에 -1이 없다면
else:
    # 결과 x, y 출력
    print(x, y)