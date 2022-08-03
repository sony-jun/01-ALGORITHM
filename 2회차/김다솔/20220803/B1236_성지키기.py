import sys
sys.stdin = open('B1236.txt')
 
# 없는 행 or 열 개수
n, m = map(int, input().split())
# print(n, m)
castle = [list(input()) for _ in range(n)]
# print(castle)
ncnt = 0
mcnt = 0

for i in range(n):
    # print(castle[i])
    if 'X' not in castle[i]:
        ncnt += 1
        # print(ncnt)
        
for j in range(m):
    # print([castle[i][j] for i in range(n)])
    """
    ['.', '.', 'X', '.', '.']
    ['.', '.', 'X', '.', '.']
    ['.', '.', '.', '.', '.']
    ['.', '.', 'X', '.', '.']
    ['X', '.', '.', '.', '.']
    ['X', '.', 'X', '.', '.']
    ['X', '.', 'X', '.', '.']
    ['X', '.', '.', '.', '.']
    """
    # for i in range(n):
    #     print(castle[i][j])
        # if castle[i][j] != 'X': 
    # 이렇게 for 아래에 if문 쓰면 모든 행열 하나씩 다 훑으면서 카운트하니까 안 됨
    """
    .
    .
    X
    .
    .
    .
    .
    X 생략
    """
    if "X" not in [castle[i][j] for i in range(n)]:
        mcnt += 1
        # print(mcnt)

print(max(ncnt, mcnt))

    

    