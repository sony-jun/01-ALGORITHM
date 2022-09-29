import sys
input=sys.stdin.readline
T=int(input())
a0,b0=map(int,input().split())
M=int(input())
arr=[[] for _ in range(T+1)]
for _ in range(M):
    a,b=map(int,input().split())
    arr[a].append(b)
    arr[b].append(a)
boo=[0]*(T+1)#검사한 노드를 표시한다
cnt=0
stack0=[]
stack1=[]
an=0
stack0.append(arr[a0])#두 노드중 하나에서부터 시작한다
ss0=[]
ss0.append(a0)
if(a0!=b0):
    while stack0 or stack1:
        cnt+=1
        while stack0:
            temp=stack0.pop(0)
            boo[ss0.pop(0)]=1
            for i in temp:
                if(boo[i]==0):
                    if(i!=b0):
                        ss0.append(i)  
                        stack1.append(arr[i])
                    else:
                        an=cnt
        cnt+=1
        while stack1:
            temp=stack1.pop(0)
            boo[ss0.pop(0)]=1
            for i in temp:
                if(boo[i]==0):
                    if(i!=b0):
                        ss0.append(i)
                        stack0.append(arr[i])
                    else:
                        an=cnt 
    if(an==0):
        print(-1)
    else:
        print(an)
else:
    print(0)