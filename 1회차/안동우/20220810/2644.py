
import sys
sys.stdin = open("2644.txt", "r")

n=int(input())#전체 사람수|
a,b=map(int,input().split())#촌수를 계산해야 하는 두사람의 번호|
m=int(input())#부모 자식들 간의 관계의 개수|
graph = [[] for _ in range(n+1)]#인접리스트
visited = [] * n
c=[]
d=[]
q=[]#상위
w=[]#상위
z=[]
x=[]
for i in range(m):
    x,y=map(int,input().split())#부모 자식간의 관계를 나타내는 두 번호 x,y
    graph[x].append(y)
    graph[y].append(x)
    d.append(*set(graph[y]))
c=list(set(graph[a][::])&set(graph[b][::]))
if len(c)==1:
    print(1)
if len(c)==0:
    q=list(set(graph[a][::])&set(d))#a상위 2
    w=list(set(graph[b][::])&set(d))#B상위 1
if q==w:
    print(2)
if q in d[::] or w==d[::]:
       z=q
       x=w

