import sys
input = sys.stdin.readline

t = int(input())
room = [list(input()) for _ in range(t)]

#방 한칸당 빈 공간을 세기 위한 cnt변수와
#각 가로 세로마다 누울수 있는 공간의 개수를 파악할
#두 개의 변수를 만든다.

row_cnt = 0
col_cnt = 0

for i in range(t):
    cnt = 0
    for j in range(t):
        if room[i][j] == '.': #'.'이 나올 경우 카운터 1씩추가
            cnt += 1
#'x'가 나올경우 카운터 수가 2이상일 경우 누울 수 있는 자리수 1추가
#카운트 0으로 초기화
        elif room[i][j] == 'X':
            if cnt >= 2:
                row_cnt += 1
            cnt = 0
#1줄이 끝날 때마다 카운트가 2이상이면 누울 수 있는 자리수 1추가하고
#다음 줄로 넘기기 전에 카운트를 0으로 초기화 한다.
    if cnt >= 2:
        row_cnt += 1
    cnt = 0

#아래 세로 줄도 동일하게 한다.
for i in range(t):
    cnt = 0
    for j in range(t):
        if room[j][i] == '.':
            cnt += 1
        elif room[j][i] == 'X':
            if cnt >= 2:
                col_cnt += 1
            cnt = 0
    if cnt >= 2:
        col_cnt += 1
    cnt = 0
            
print(row_cnt, col_cnt)