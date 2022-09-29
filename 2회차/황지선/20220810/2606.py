# 2606번 바이러스

# 어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다. 
# 컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때, 
# 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 프로그램을 작성하시오.


# 출력
# 1번 컴퓨터가 웜 바이러스에 걸렸을 때, 
# 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 첫째 줄에 출력한다.


from pprint import pprint

# 첫째 줄에는 컴퓨터의 수가 주어진다. # 정점의 갯수
N = int(input())
# 둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다. # 간선의 갯수
M = int(input())

graph = [[] * N for _ in range(N+1)]

for _ in range(M):
    # 이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다. # 간선들
    u, v = map(int, input().split())
    graph[v].append(u)
    graph[u].append(v)

# pprint(graph)  # 인접 리스트
# ----------------------------------------
# DFS

# 다녀간 정점을 확인하기 위한 변수
count = 0
visited = [False] * (N+1)

def dfs(start):
    # 함수 밖에서 선언한 변수를 같이 쓰기 위해서
    # count 라는 전역변수가 만들어진다! 함수의 실행이 끝난 후에도 없어지지 않는다!
    global count
    # 1번 컴퓨터는 방문처리
    visited[start] = True

    # 위에서 만든 인접 리스트 graph를 돌면서
    for i in graph[start]:
        # 들리지 않은 정점이면 (False 상태) dfs 함수를 이용해서 다시 반복
        if visited[i] == False:
            # 재귀를 이용해서 해당 컴퓨터를 방문처리한 후 count + 1
            dfs(i)
            count += 1

# 1번 정점에서 시작
dfs(1)
print(count)


















# visited = [False] * (N+1)

# def dfs(start):
#     global cnt
#     visited[start] = True

#     for i in graph2[start]:
#         if visited[i] == False:
#             dfs(i)
#             cnt +=1
 
# dfs(1)
# print(cnt)