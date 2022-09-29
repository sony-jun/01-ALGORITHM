paper = [[0 for i in range(101)] for i in range(101)]
for i in range(4):
    x,y,x1,y1 = map(int,input().split())
    for i in range(y,y1):
        for j in range(x,x1):
            paper[i][j] = 1
print(sum(map(sum,paper)))