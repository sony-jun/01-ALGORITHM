import sys

sys.stdin = open("2_2차원배열의합.txt", 'r')

N, M = map(int, sys.stdin.readline().split())
arr = [[*map(int, sys.stdin.readline().split())] for _ in range(N)]

K = int(sys.stdin.readline())

for _ in range(K):
    total = 0
    i, j, x, y = map(int, sys.stdin.readline().split())
    
    for r in arr[i - 1:x]:
        total += sum(r[j - 1:y])
    
    print(total)
    
# 누적값 카테고리로 들어가있다.