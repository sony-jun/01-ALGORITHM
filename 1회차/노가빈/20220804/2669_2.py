from pprint import pprint


#직사각형 색칠하기(0을 1로 바꾸기)
for _ in range(4):
    i,j,x,y = map(int,input().split(' '))
    maxX = max(i,x)
    maxY = max(j,y)
    numlist = [[0]*maxX for i in range(maxY)]
    pprint(numlist)
    for k in range(i,x):
        for z in range(j,y):
            numlist[k][z] = 1

count = 0
#색칠된 직사각형의 범위(갯수)구하기
for i in range(maxX):
    for j in range(maxY):
        if numlist[i][j] == 1:
            count += 1
pprint(numlist)
pprint(count)