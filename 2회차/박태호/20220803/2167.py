# 2차원 배열의 합
# i,j에서 x,y까지의 합을 구하라
#
import sys
n, m = map(int,sys.stdin.readline().strip().split()) # 2 3 

mat = [list(map(int,sys.stdin.readline().split())) for _ in range(n)]
# print(mat) [[1, 2, 4], [8, 16, 32]]

case = int(sys.stdin.readline().strip())

for _ in range(case):
    i,j,x,y = list(map(int,sys.stdin.readline().strip().split()))
    sum_ = 0
    for a in range(i-1,x): # 1,2 -> 0,1
        for b in range(j-1,y): # 3,3 -> 2,2
            
        
            sum_+=(mat[a][b])
    print(sum_)
 # pypy3 제출
 
    #[
    #  [1,  2,  4],
    #  [8, 16, 32]
    # ]
    # 1 1 2 3
    # 1 2 1 2
    # 1 3 2 3