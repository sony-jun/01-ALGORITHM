import sys

# sys.stdin = open("./1236.txt")

n, m = map(int, input().split())
arr = [list(input()) for x in range(n)]

# 열과 행에 X가 있는지를 확인하면 풀릴 거라고 생각

## 열 검사
col = []
for i in range(m):
    is_in = False # 열 중에 X가 있는지 확인하기 위한 변수
    for j in range(n):         
        if arr[j][i] == 'X': # 만약 열 중에 X가 있다면 True로 변수를 변환
            is_in = True
    if is_in: # is_in 이 True 면
        col.append('X') # col 에 X를 더해주고
    else:
        col.append('0') # False 면 0을 더해줌 

## 행 검사
row = []
for i in range(n):
    is_in = False
    for j in range(m):
        if arr[i][j] == 'X':
            is_in = True
    
    if is_in:
        row.append('X')
    else:
        row.append('0')


print(max(row.count('0') , col.count('0')))

    

        
        