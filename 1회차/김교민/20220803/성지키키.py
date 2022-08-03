# 세로 길이와 가로 길이 matrix입력
# 필요한 경비원의 수를 저장할 변수를 두 개 만든다.
# for문을 활용해 X의 유무를 판단하게 한다.

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
mat = [list(input()) for _ in range(n)] #리스트 컴프리핸션

#각 열과 행에 x가 있는지 체크할 리스트를 만든다.
nn = [0]*n # n값 만큼 문자열 0이 리스트에 주어진다.
mm = [0]*m # m값 만큼 문자열 0이 리스트에 주어진다.

#성의 크기만큼 순회하면서 
for i in range(n):
    for j in range(m):
        if mat[i][j] == 'X': #행과 열에 x가 있으면
            nn[i] = 1 # 해당 행과 열의 값을 1로 바꾼다.
            mm[j] = 1
            
#필요한 경비원의 수를 저장할 두개의 변수를 만든다.
cnt_n = 0
cnt_m = 0
# 각 행과 열을 따로 순회하면서 x가 아닐 경우 각각 1씩 더해준다.
for i in range(n):
    if nn[i] == 0:
        cnt_n += 1
for j in range(m):
    if mm[j] == 0:
        cnt_m += 1

#열의 카운터와 행의 카운터중 큰 값을 출력한다.
print(max(cnt_n, cnt_m)) 