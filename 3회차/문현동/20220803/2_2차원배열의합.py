'''import sys
from pprint import pprint
sys.stdin = open("2_2차원배열의합.txt", 'r')

N, M = map(int, sys.stdin.readline().split())
arr = []

for _ in range(N):
    arr.append([*map(int, sys.stdin.readline().split())])

K = int(sys.stdin.readline())

for _ in range(K):
    '''