# 예상컨데 node_set을 dfs로 읽으면 연결된 애들끼리는 
# 같은 visited를 반환할 것이다.

n,e = map(int,input().split())
graph_list = [[] for _ in range(n+1)]
node_set = set()

for _ in range(e):
    u,v = map(int,input().split())
    node_set.add(u)
    node_set.add(v)
    graph_list[u].append(v)
    graph_list[v].append(u)

print('graph_list =',graph_list) # [[], [2, 5], [1, 5], [4], [3, 6], [2, 1], [4]]
print('node_set =',node_set)
# dfs code
def dfs(start):
    stack = [start]
    visited = [False]* (n+1) # node를 읽을때마다 visited reset
    visited[start] = True

    while stack:
        cur = stack.pop()
        for adj in graph_list[cur]:
            if not visited[adj]:
                visited[adj] = True
                stack.append(adj)
    return visited
visited_set = [] # set으로 처리하고싶엉ㅆ는데 list가 unhashable한 타입이라 그냥 list 중복 처리
for ns in node_set:
    # print(dfs(ns))
    if dfs(ns) not in visited_set:
        visited_set.append(dfs(ns))
# print('visited_set =',visited_set)
# 아마 len값을 어디 다른 변수에 저장해주면 시간이 좀 줄어들겠죠?
if len(node_set) == n and len(visited_set) >= 1: # 모든 노드가 연결된 노드가 있을 때
    print(len(visited_set))
elif visited_set == []: # 노드 1개일때
    print(1)
elif len(node_set) != n:
    result = len(visited_set) + n - len(node_set) # 일부 노드가 연결된 노드가 없을 때
    print(result)

# 튜터님 말씀 - dfs한번 돌린 후, 방문하지 않은 노드를 방문하는 식으로...
# 일단 출력 조건만 손대면 되서 하던대로 밀고나갔습니다. 한게 아까워서..