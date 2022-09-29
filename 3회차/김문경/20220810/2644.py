import sys
sys.stdin = open('test.txt')

# N이 정점 개수 ; 전체 사람 몇명인지
n = int(input())

# 0 인덱스는 사용 안 하니까 N + 1만큼의 빈 리스트 만들기
graph = [[] for _ in range(n + 1)]

# 입력 받은 둘 사이의 촌수 구하기
person1, person2 = map(int, input().split())

# 다음으로 입력받는 숫자만큼 간선 추가하기
for i in range(int(input())):
    v1, v2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)

visited = [False] * (n + 1)

#* -----------------------------
# 입력받은 person1을 시작점으로 두기
stack = [person1]
# 0번은 실제로 없으니까 애초부터 True로 고정
visited[0] = True
# 시작점은 True
visited[person1] = True
cnt = 0
while True:
    cur = stack.pop()
    # 해당 정점에 인접하는 요소가 1개라도 있을때만 고려
    if len(graph[cur]) != 0:
        for i in graph[cur]:
            if visited[i] == False:
                visited[i] = True
                stack.append(i)
        cnt += 1
    # 더이상 탐색이 안 될때
    else:
        continue
    if visited[person2] == False:
        continue
    else:
        break
print(cnt)


