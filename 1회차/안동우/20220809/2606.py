from pprint import pprint
import sys
sys.stdin = open("2606.txt", "r")
from pprint import pprint

n=int(input())
m=int(input())
a=[[] for z in range(n) ]
for x in range(m):
    b,c =map(int,input().split())    
    a[b].append(c)
    a[c].append(b)
    pprint(a)