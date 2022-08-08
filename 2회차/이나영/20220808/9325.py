from re import A
import sys

sys.stdin = open("9325.txt")

T = int(input())

for i in range(T):
    s = int(input())
    n = int(input())
    if n == 0:
        print(s)
    else:
        option = 0
        for _ in range(n):
            q,p = map(int,input().split())
            option += q*p
    
    print(s+option)

