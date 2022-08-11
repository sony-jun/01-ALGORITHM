from re import A
import sys

sys.stdin = open("input25305.txt")

X = int(input())
N = int(input())
J = 0

for i in range(N):
    a, b = map(int,input().split())
    c = a * b
    J = J+c
 
if X == J:
        print('Yes')
else:
        print('No')