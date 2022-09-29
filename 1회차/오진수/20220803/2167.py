import sys
sys.stdin=open("input/2167.txt",'r')

N,M = map(int, input().split())
Matrix=[list(map(int, input().split())) for i in range(N)]
K =int(input())
for line in range(K):
    i,j,x,y = map(int, input().split()) 
    sum_=0                                
    if j == y:
        row_max=max(i,x)
        column_max=max(j,y)
    else:
        row_max=N
        column_max=max(j,y)
    while 1:
        sum_ += Matrix[i-1][j-1]
        if i == x and j == y:
            print(sum_)
            break
        elif i < row_max:
            i += 1
        else:
            j +=1
            i = 1