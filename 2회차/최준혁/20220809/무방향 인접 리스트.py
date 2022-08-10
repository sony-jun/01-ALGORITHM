N, M = map(int, input().split())
# N길이의 빈 2중 리스트 생성
adj_list = [[] for _ in range(N)]

# M길이만큼 반복하며
for _ in range(M):
    # 간선의 시작점(u), 간선의 끝점(v) 추가
    u, v = map(int, input().split()) # 1, 2 / 2, 5 / 5, 1 / 3, 4 / 4, 6
    # 연결된 값 끼리 추가해준다.
    adj_list[v].append(u) # adj_list[2].append(1)
    adj_list[u].append(v) # adj_list[1].append(2)


print(adj_list)
# [[], [2, 5], [1, 5], [4], [3, 6], [2, 1], [4]]