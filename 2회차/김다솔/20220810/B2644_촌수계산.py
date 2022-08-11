# https://www.acmicpc.net/problem/2644
import sys
sys.stdin = open('B2644.txt')

def pprint(arr):
    for i in range(len(arr)):
        print(i, arr)
        
N = int(input())
start, end = list(map(int, input().split()))
M = int(input())
relatives = [[] for _ in range(0, n + 1)]

for _ in range(M):
    x, y = list(map(int, input().split()))
    
    #무방향 인접 그래프
    relatives[x].append(y)
    relatives[y].append(x)
    
#방문 표시 할 리스트
visited = [False] * (N + 1)
#dfs 기본값 설정
#스택에 값을 추가할 때 촌수도 같이 추가.

stack = []
stack.append(start)
visited[start] = True

#스택이 비어있지 않으면 반복 
while len(stack) != 0:
    #LIFO 스택 가장 위에 있는 값을 저장 
    num = stack.pop()
    
    #해당하는 값의 인접 그래프를 저장 
    adj_graph = relatives[num]
    print(num, relatives)
    
    #pop을 한 값이 우리가 원하는 값(end)
        for adj_num in adj_graph:
            stack.append()