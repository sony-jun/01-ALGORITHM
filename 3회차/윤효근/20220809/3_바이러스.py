import sys
from collections import defaultdict
from collections import deque
from pprint import pprint

sys.stdin = open("3_바이러스..txt")

def dfs(graph, start_node):
    visited = []
    need_visited = deque()
    need_visited.append(start_node)  # 시작 노드 설정해주기

    while need_visited:  # 방문이 필요한 리스트가 아직 존재한다면
        node = need_visited.pop()  # 그 중에서 가장 마지막 데이터를 추출 (스택 구조의 활용)
        if node not in visited:  # 만약 노드가 방문한 리스트에 없다면
            visited.append(node)  # 방문 리스트에 노드를 추가
            need_visited.extend(graph[node])  # 인접 노드들을 방문 예정 리스트에 추가
    return visited  # 방문 리스트를 리턴
# ================================


All_c = int(input())
connect_c=int(input()) # 연결된 노드의 갯수

net = defaultdict(list)
# defaultdict로 net선언 => ()의 기본값을 딕셔너리의 초기값으로 지정
# 디폴트 값이 list인 딕셔너리 net이 만들어짐
for _ in range(connect_c):  # 연결된 노드의 갯수만큼 반복
    k,v = map(int,input().split())  # 주어진 노드의 값을 분리해서
    net[k].append(v)  # net에 저장
    net[v].append(k)
    # 무방향 그래프 이므로 각각의 노드에서 모두 연결됨
    # net[v].append(k)를 제거하면 유방향 그래프가 됨
pprint(net)
print(dfs(net,1))
print(len(dfs(net,1))-1)
# dfs함수의 결과에 시작노드'1'도 포함되어 있으므로 전체 길이에서 1을 빼준 결과를 출력

