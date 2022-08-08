
from re import T
import sys
sys.stdin = open("2798.txt", "r")
N,M=map(int,input().split())

T=list(map(int,input().split()))
z=0
x=0
for q in range(N-2):   
    for w in range(q+1,N-1):
        for e in range(w+1,N):
            if (T[q]+T[w]+T[e]>M):
                continue#크다면 계속
            else:
                z=T[q]+T[w]+T[e]
                if x <= z:
                    x=z
print(x)                 
   