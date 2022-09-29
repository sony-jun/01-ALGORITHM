# https://www.acmicpc.net/problem/5576
import sys
sys.stdin = open('B5576.txt')

W = []
K = []
for _ in range(10):
    W.append(int(input()))
for _ in range(10):
    K.append(int(input()))
print(sum(sorted(W)[-3::]), sum(sorted(K)[-3::]))

