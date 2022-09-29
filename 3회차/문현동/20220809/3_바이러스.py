import sys
sys.stdin = open("3_바이러스.txt", 'r')

N = int(sys.stdin.readline())
M = int(sys.stdin.readline())

adjacent_list = []
edges = []

for _ in range(N + 1):
    adjacent_list.append([])

for _ in range(M):
    edges.append([*map(int ,sys.stdin.readline().split())])

for i in edges:
    adjacent_list[i[0]].append(i[1])
    adjacent_list[i[1]].append(i[0])

visit = set()

def worm(n):
    for i in adjacent_list[n]:
        if i not in visit:
            visit.add(i)
            worm(i)
        else:
            pass
worm(1)
visit.remove(1)
print(len(visit))

# 백준 함수 안쓰고 푼 코드

'''
N=int(input())
M=int(input())
grap=[[] for _ in range(N+1)]
grap_li=[1]
grap_li2=[1]
for i in range(M):
    x,y=map(int, input().split())
    grap[x].append(y)
    grap[y].append(x)
    
while len(grap_li)>0:
    a = grap[grap_li.pop(0)]
    for i in a:
        if i not in grap_li2:
            grap_li.append(i)
            grap_li2.append(i)
            
print(len(grap_li2)-1)
'''