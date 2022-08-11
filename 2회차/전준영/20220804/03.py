import sys
input=sys.stdin.readline
N=int(input())
metrix0=[input() for _ in range(N)]
metrix1=[input() for _ in range(N)]
metrix=[['.']*N for _ in range(N)]
x=0
bo=0
for i in metrix1:
    y=0
    for k in i:
        if(k=='x'):
            if(metrix0[x][y]=='*'):
                metrix[x][y]=0
                bo=1
            else:
                metrix[x][y]=0
        y+=1
    x+=1
if(bo==1):
    x=0
    for i in metrix0:
        y=0
        for k in i:
            if(k=='*'):
                for x0 in range(-1,2):
                    for y0 in range(-1,2):
                        if(0<=x+x0<N and 0<=y+y0<N and metrix[x+x0][y+y0]!='.' and metrix[x+x0][y+y0]!='*'):
                            metrix[x+x0][y+y0]+=1
                metrix[x][y]='*'
            y+=1
        x+=1
else:
    x=0
    for i in metrix0:
        y=0
        for k in i:
            if(k=='*'):
                for x0 in range(-1,2):
                    for y0 in range(-1,2):
                         if(0<=x+x0<N and 0<=y+y0<N and metrix[x+x0][y+y0]!='.' and metrix[x+x0][y+y0]!='*'):
                            metrix[x+x0][y+y0]+=1
                metrix[x][y]='.'
            y+=1
        x+=1
for i in metrix:
    str0=""
    for k in i:
        str0+=str(k)
    print(str0)

