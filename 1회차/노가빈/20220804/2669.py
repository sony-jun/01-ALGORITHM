from pprint import pprint

numlist = [[0]*100 for i in range(100)]

#직사각형 색칠하기(0을 1로 바꾸기)
for _ in range(4):
    i,j,x,y = map(int,input().split(' '))
    for k in range(i,x):
        for z in range(j,y):
            numlist[k][z] = 1

count = 0
#색칠된 직사각형의 범위(갯수)구하기
for i in range(100):
    for j in range(100):
        if numlist[i][j] == 1:
            count += 1
pprint(count)