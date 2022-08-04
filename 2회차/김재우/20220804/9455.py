import sys

sys.stdin=open('9455.txt', 'r')

M, N = 5, 4 #열, 행

box = [
    [1, 0, 0, 0],
    [0, 0, 1, 0],
    [1, 0, 0, 1],
    [0, 1, 0, 0],
    [1, 0, 1, 0]
]

space = [[],[],[],[],[]]
s = 0
# for i in range(N):      # 열
for j in range(N):
    for i in range(M):  # 행
        space[0].append(box[i][j])

print(space)
