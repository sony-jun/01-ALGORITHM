# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")

N, M = input().split()

n = int(N[::-1])
m = int(M[::-1])

if n > m : 
    print(n)

elif n < m :
    print(m)


