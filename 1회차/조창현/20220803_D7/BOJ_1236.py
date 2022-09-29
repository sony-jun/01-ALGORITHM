from pprint import pprint

import sys

sys.stdin = open("1236.txt")
## 우선 n, m 을 받아
n, m = map(int, input().split())

## 성을 행렬로 만들어 준다.
castle = [list(input()) for i in range(n)]
#pprint(castle)

row_count = 0
col_count = 0
cast_trans = []

## 성의 행을 넣어준다.
for row in castle:
    #print(i)
    ## 행에 X 가 없다면
    if 'X' not in row:
        ## 행카운트를 +1
        row_count += 1
#print(row_count)

## 열을 고정하고
for j in range(m):
    row_temp = []
    ## 행을 돌아가면 반복한다.
    for i in range(n):
        ## 임시 행에 하나씩 축적한다.
        row_temp.append(castle[i][j])
    ## 캐슬 트랜스에 한줄씩 추가해준다.
    cast_trans.insert(j, row_temp)
    #pprint(cast_trans)
pprint(cast_trans)
## 위 과정을 전부 돌면 x=y 대칭처럼 행렬이 돈다.

## 트랜스 행렬의 행을 반복한다.
for row in cast_trans:
    #print(i)
    if 'X' not in row:
        col_count += 1
#print(col_count)

if row_count < col_count:
    print(col_count)
else:
    print(row_count)

