import sys
input = sys.stdin.readline

chess = [list(input()) for _ in range(8)]
cnt = 0 
# 좌표로 나타내면 (i, j) 하얀칸은 (0, 0) (0, 2), (1, 3), (1, 5) --- i + J 짝수
# 합이 짝수인 칸에 있는 F의 개수를 세는 문제
for i in range(8):
    for j in range(8):
        if i % 2 == 0: # i가 짝수이면
            if j % 2 == 0 and chess[i][j] == 'F': # j가 짝수이고 'F'가 있으면
                cnt += 1 # 1을 더해주고
        elif i % 2 == 1: # i가 홀수이면
            if j % 2 == 1 and chess[i][j] == 'F': # j가 홀수이고 'F'가 있으면
                cnt += 1 # 1을 더해준다.

print(cnt)