import sys

input = sys.stdin.readline

n = int(input())
#주어진 값을 2차원 배열로 받아준다.
room = [list(input()) for _ in range(n)]

#가로 세로 자리의 수를 구하기 위해 필요한 변수
result = [0, 0]
#방 전체를 돌면서 
for i in range(n):
    row, column = 0, 0
    for j in range(n):
        # 가로 확인 "."이 있으면 0을
        if room[i][j] != ".":
            row = 0
        #아니면 1을 더해주고
        else:
            row += 1
        #만약 길이가 2라면 결과값의 [0]인덱스에 1을 추가
        if row == 2:
            result[0] += 1
        # 세로 확인
        if room[j][i] != ".":
            column = 0
        else:
            column += 1
        #만약 세로의 길이가 2이라면 result[1]에 1을 추가
        if column == 2:
            result[1] += 1

#결과값 출력
for i in result:
    print(i, end = " ")