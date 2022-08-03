# 2차원 배열의 합
# i,j에서 x,y까지의 합을 구하라
#
n,m = map(int, input().split())
mat = []
for _ in range(n):
    ar = list(map(int, input().split()))
    mat.append(ar) #[[1, 2, 4], [8, 16, 32]]

hab = int(input())
for _ in range(hab):
    i, j, x, y = list(map(int,input().split()))
    result = []
    for i in range(i-1,x): # 0~1
        for j in range(j-1,y): # 0 ~ 2

         result.append(mat[i][j]) # mat[0][1]
    print(result)
    #[
    #  [1,  2,  4],
    #  [8, 16, 32]
    # ]
    # 1 1 2 3
    # 1 2 1 2
    # 1 3 2 3