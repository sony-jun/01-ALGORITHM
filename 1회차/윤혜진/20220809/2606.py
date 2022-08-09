# https://www.acmicpc.net/problem/2606
# 문제2606번.바이러스
# 시간제한:1초, 메모리제한:128MB



# 입력
'''
1. 컴퓨터의 수
- 0 < 컴퓨터 수 <= 100
- 각 컴퓨터는 1번부터 차례대로 번호가 매겨짐
2. 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수
3. 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍
'''



# 출력
'''
1. 1번 컴퓨터가 웜 바이러스에 걸렸을때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 첫째 줄에 출력
- 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 됨
'''



# 코드 1 - stack을 이용한 반복문으로 dfs 풀이
import sys
from pprint import pprint

sys.stdin = open('input_text/2606.txt')

# 네트워크로 연결된 컴퓨터 수 반환
def networked_coms(graph, start):   # dfs
    visited = set()
    stack = [start]   # 네트워크로 연결되어 있어 이동 가능한 컴퓨터들
    while stack:
        now = stack.pop()   # 현재 탐색 중인 컴퓨터

        # 현재 탐색 중인 컴퓨터 방문 체크
        visited.add(now)

        # 현재 탐색 중인 컴퓨터와 네트워크로 연결된 컴퓨터 조회
        for com in graph[now]:
            if com not in visited:
                stack.append(com)
    
    return len(visited)


node = int(input())   # 컴퓨터 수
edge = int(input())   # 연결된 컴퓨터 쌍 수 

# 네트워크로 연결된 컴퓨터를 나타내기 (인접 리스트)
graph = [[] for _ in range(node + 1)]   # 인덱스: 컴퓨터 1번 ~ node번
for _ in range(edge):
    c1, c2 = map(int, input().split())
    graph[c1].append(c2)
    graph[c2].append(c1)

# 바이러스에 걸리게 되는 컴퓨터 수 출력
print(networked_coms(graph, 1) - 1)



# 실행결과(메모리:30840KB, 시간:84ms)



# 코드 2 - 재귀를 이용해 dfs 풀이
import sys
from pprint import pprint

sys.stdin = open('input_text/2606.txt')

# 네트워크로 연결된 컴퓨터 수 반환
def networked_coms(graph, node, visited):   # dfs
    # 방문한 컴퓨터 체크
    visited.append(node)

    # 현재 방문한 컴퓨터와 연결된 컴퓨터 탐색
    for com in graph[node]:
        if com not in visited:
            networked_coms(graph, com, visited)


node = int(input())   # 컴퓨터 수
edge = int(input())   # 연결된 컴퓨터 쌍 수 

# 네트워크로 연결된 컴퓨터를 나타내기 (인접 리스트)
graph = [[] for _ in range(node + 1)]   # 인덱스: 컴퓨터 1번 ~ node번
for _ in range(edge):
    c1, c2 = map(int, input().split())
    graph[c1].append(c2)
    graph[c2].append(c1)

# 바이러스에 걸리게 되는 컴퓨터 수 출력
visited = []
networked_coms(graph, 1, visited)
print(len(visited) - 1)



# 실행결과(메모리:30840KB, 시간:80ms)