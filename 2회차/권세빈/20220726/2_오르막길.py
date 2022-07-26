# https://www.acmicpc.net/problem/2846

import sys

sys.stdin = open("2_오르막길.txt", "r")

n = int(input())
p = list(map(int,input().split()))
l = []

for i in range(n-1):
    if p[i] < p[i+1]:
        l.append(p[i])