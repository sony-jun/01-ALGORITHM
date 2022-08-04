import sys
input = sys.stdin.readline

N = int(input()) #방의 크기

room = [list(map(str,input())) for _ in range(N)] 
cnt_row = 0  #가로로 누울 수 있는 경우
cnt_col = 0  #세로로 누울 수 있는 경우

row = 0  #가로 자리
col = 0  #세로 자리

for i in range(N):   #이차원 리스트의 행 범위에서
    cnt_row = 0 
    for j in range(N):
        if room[i][j]== '.':  #만약 '.' 이 있다면 +1
            cnt_row += 1
        else :
            cnt_row = 0  #없다면 0
        if cnt_row == 2: #가로로 누울 수 있는 경우가 2라면
            row += 1  #가로 자리 +1
            

for i in range(N):  #이차원 리스트의 열 범위에서
    cnt_col = 0
    for j in range(N):
        if room[j][i] =='.':
            cnt_col += 1
        else :
            cnt_col = 0
        if cnt_col == 2:
            col += 1    
            

print(row ,col)    

