from pprint import pprint

# 정점과 간선의 개수 입력받기
N, M = map(int, input().split())

# 인접행렬, 인접리스트 사용
all = 7
matrix = [[0] * all for _ in range(all)]
list = [[] for _ in range(all)]

for _ in range(M):
    u, v = map(int, input().split())
    # 방향이 없으므로 대칭 이루도록 행렬 변경
    matrix[u][v] = 1
    matrix[v][u] = 1
    # 연결된 원소만 갖도록 리스트에 추가
    list[u].append(v)
    list[v].append(u)

pprint(matrix)
print(list)
