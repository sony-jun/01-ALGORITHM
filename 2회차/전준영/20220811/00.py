import sys
from collections import deque
input=sys.stdin.readline
aaa=input().split()
kidx0=aaa[0]
sidx0=aaa[1]
N=aaa[2]
kidx=[ord(kidx0[0].lower())-ord('a'),int(kidx0[1])-1]
sidx=[ord(sidx0[0].lower())-ord('a'),int(sidx0[1])-1]
N=int(N)
dic={'R':(1,0),'L':(-1,0),'B':(0,-1),'T':(0,1),'RT':(1,1),'LT':(-1,1),'RB':(1,-1),'LB':(-1,-1)}
for _ in range(N):
    ip0=input()
    ip1=ip0[:-1]
    ip0=ip1
    ls=dic[ip0]
    if(0<=kidx[0]+ls[0]<8 and 0<=kidx[1]+ls[1]<8 and 0<=sidx[0]+ls[0]<8 and 0<=sidx[1]+ls[1]<8 and kidx[0]+ls[0]==sidx[0] and kidx[1]+ls[1]==sidx[1]):
        kidx[0]+=ls[0]
        kidx[1]+=ls[1]
        sidx[0]+=ls[0]
        sidx[1]+=ls[1]
    elif(0<=kidx[0]+ls[0]<8 and 0<=kidx[1]+ls[1]<8 and (kidx[0]+ls[0]!=sidx[0] or kidx[1]+ls[1]!=sidx[1])):
        kidx[0]+=ls[0]
        kidx[1]+=ls[1]
a0=chr(kidx[0]+ord('A'))+str(kidx[1]+1)
a1=chr(sidx[0]+ord('A'))+str(sidx[1]+1)
print(a0)
print(a1)