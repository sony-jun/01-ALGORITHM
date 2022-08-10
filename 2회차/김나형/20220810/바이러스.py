import sys
sys. stdin = open("input.txt")

n = int(input())
m = int(input())

graph = [[] for _ in range(n + 1)] # 인접 리스트 생성

visited = [0] * (n + 1) # 방문한 컴퓨터를 count할 리스트 생성

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
    # [[], [2, 5], [1, 3, 5], [2], [7], [1, 2, 6], [5], [4]]

def DFS(v):
    visited[v] = 1
    for i in graph[v]:
        if visited[i] == 0: # 중복(2번 방문)을 허용하지 않음
            DFS(i) # 처음 방문한 숫자가 있다면 그 숫자(i)의 자리부터 탐색 

    # 1에서 2, 5 탐색
    # 2를 방문하지 않았으니 cnt에 1을 넣어주고 2부터 탐색
    # 2에서 인접한 숫자중 1은 방문했음으로 (cnt에 1이 들어가있음) 3을 우선 탐색
    # 3은 인접한 수가 2 밖에 없음으로 함수 return True를 만나 종료
    # 3이 종료되고 2로 돌아가 다음 수인 5에 방문
    # 위 상황을 반복하여 모든 for문이 종료되면 출력 (1에서 네트워크를 통해 바이러스가 방문한 수)

DFS(1)
print(sum(visited)-1)  # 방문한 컴퓨터 개수 - 1번 컴퓨터
# visited
# [0, 1, 1, 1, 0, 1, 1, 0]

