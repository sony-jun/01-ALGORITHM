import sys
sys.stdin = open('1453.txt')

N = int(input())
list_N = list(map(int, input().split()))
sit = [0] * 101
rej = 0

for i in range(N):
    sit[list_N[i]] += 1
    if sit[list_N[i]] >= 2:
        rej += 1

print(rej)