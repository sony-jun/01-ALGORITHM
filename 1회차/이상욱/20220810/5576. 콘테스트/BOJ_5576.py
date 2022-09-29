import sys
sys.stdin = open('5576.txt')
N = 10

W = [int(input()) for _ in range(N)]
K = [int(input()) for _ in range(N)]

W.sort(reverse=True)
K.sort(reverse=True)

print(sum(W[0:3]), end = " ")
print(sum(K[0:3]), end = " ")