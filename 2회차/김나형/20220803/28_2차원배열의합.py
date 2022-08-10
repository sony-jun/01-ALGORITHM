import sys

sys.stdin = open("28_2차원배열의합.txt")

n, m = map(int, sys.stdin.readline().split())
li = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]


for _ in range(int(sys.stdin.readline())):
    i, j, x, y = list(map(int, sys.stdin.readline().split()))
    sum = 0
    for row in range(i-1, x):
        for col in range(j-1, y):
            sum += li[row][col]
    print(sum)
    