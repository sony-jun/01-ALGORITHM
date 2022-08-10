## :sparkler:느낀점/배운점/부족한점



#### BOJ 10101

```python
# 삼각형의 세 각을 입력받음
angle = [int(input()) for _ in range(3)]

if sum(angle) == 180:
    if angle[0] == angle[1] == angle[2]: # 세 각의 크기가 모두 60이면
        print('Equilateral')
    # 세 각의 합이 180이고, 두 각이 같은 경우
    elif angle[0] == angle[1] or angle[1] == angle[2] or angle[2] == angle[0]:
        print('Isosceles')
    else: # 세 각의 합이 180이고, 같은 각이 없는 경우
        print('Scalene')
else: # 세 각의 합이 180이 아닌 경우
    print("Error")

```





#### BOJ 1598

```python
a, b = map(int, input().split())
x1 = (a-1)//4 + 1
y1 = (a-1)%4
x2 = (b-1)//4 + 1
y2 = (b-1)%4
print(abs(x2-x1) + abs(y2-y1))
```





#### BOJ 5576

```python
import sys
input = sys.stdin.readline

# 10개씩 나눠서 리스트 만듬
for _ in range(2):
    a = []
    for _ in range(10):
        a.append(int(input()))
    # 인덱스 -1, -2, -3가 가장 높은 수들
    # 가장 높은 수 3개의 합 출력
    print(sum(sorted(a)[-3:]), end=' ')
```





#### 2606

```python
n = int(input())
m = int(input())
graph = [[] for _ in range(n + 1)]
# False로 초기화 되어있는 리스트
# 방문 처리 리스트
visited = [False] * (n + 1)
total = 0

# 인접 리스트 만들기
for _ in range(m):
    v1, c2 = map(int, input().split())
    graph[v1].append(v2)
    graph[v2].append(v1)


visited = [False] * n
def dfs(start):
    # 돌아올때 stack 구현
    # 더 이상 갈 곳이 없을 때 돌아갈 곳
    stack = [start]
    # 처음 시작 방문 처리
    visited[start] = True

    # 더 이상 갈 곳이 없을 때 로직화한 while문
    while stack:
        cur = stack.pop()

        # 예를 들어, 0은 [1, 2]
        # cur에 [1, 2] 대입
        for adj in graph[cur]:
            # 방문해 있지 않았다면 가는 것이다
            if not visited[adj]:
                visited[adj] = True
                # stack에 1 추가
                stack.append(adj)


```





:sparkles::rocket: 그래프 탐색의 깊이 우선 탐색 Depth First Search(DFS)을 단계별로 생각해보고 구현할 수 있어서 좋았고 다양한 성장 문제들을 풀어보면서 원리 이해 중심으로 코딩을 배우는 것이 어떤 문제를 풀던지 굉장히 중요하다라는 것을 많이 느꼈던 것 같습니다. 깊이 우선 탐색의 정점(노선)의 연결과 위치에 따라 구현되는 코딩을 보면 볼수록 눈코딩의 실력도 늘어나는 것 같습니다. 