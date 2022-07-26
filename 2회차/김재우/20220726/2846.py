import sys

sys.stdin = open('2846.txt', 'r')

N = int(input())
road = list(map(int, input().split()))
uphill = 0
down = 0
for i in range(1, N):
    if road[i] >= road[i + 1]:
