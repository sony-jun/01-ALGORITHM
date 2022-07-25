# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("0_숫자의개수.txt")

A = int(input())
A = int(input()) * A
A = int(input()) * A

l = [ 0 for i in range(10) ]

str_A = list(str(A))

for ch in str_A:
    l[int(ch)] += 1
    
for i in l:
    print(i)