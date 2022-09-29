import sys

sys.stdin = open("콘테스트.txt")

W = [int(input()) for _ in range(10)]
K = [int(input()) for _ in range(10)]

W.sort()
K.sort()

print(W[9] + W[8] + W[7], K[9] + K[8] + K[7])