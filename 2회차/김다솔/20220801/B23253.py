import sys
sys.stdin = open('B23253.txt')

N, M = map(int, input().split())
for i in range(1, M+1):
    k = int(input())
    i = list(map(int, input().split()))
    for l in range(k-1):
        if i[l] < i[l+1]:
            print['Yes']
        else:
            print('No')
