# https://www.acmicpc.net/problem/7568

import sys
sys.stdin = open("4.txt", "r")

n = int(input())
person = []

for i in range(n):
    w , h = map(int,input().split())
    person.append([w,h])

for j in person:
    rank = 1
    for k in person:
        if j[0] < k[0] and j[1] < k[1]:
            rank += 1 
                      
    print(rank, end=' ')