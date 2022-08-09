## :sparkler:느낀점/배운점/부족한점



#### BOJ 1264

```python
while True: # 참일때까지 실행
    sentence = input()
    count = 0
    if sentence == '#': # 입력의 끝
        break # 문장 탈출
    for c in sentence:
        if c in 'aeiouAEIOU': # 모음이면
            count += 1 # count에 1씩 증가
    print(count)
```





#### BOJ 2587

```python
x = []
for i in range(5):
    x.append(int(input()))
print(int(sum(x) / 5)) # 평균
x.sort() # 정렬
print(x[2]) # 중앙값
```





#### BOJ 1371

```python
import sys
word = sys.stdin.read() 
alphabet = list(range(97, 123)) # 아스키 코드를 통해서 리스트 생성
a = {}
for x in alphabet: # for문 통해서 x 처음부터 끝까지 순회
    a[chr(x)]=word.count(chr(x))
for x in a:
    if a[str(x)] == max(a.values()): # 최대숫자와 같으면
        print(x, end='')
```





#### 101

```python
# 인접 행렬 
N, M = map(int, input().split())

graph = []
for i in range(N + 1):
    graph.append([0]* (N+1))
for i in range(M):
    u, v = map(int, input().split())
    graph[u][v] = 1
    graph[v][u] = 1
print(graph)

# 인접 리스트
N, M = map(int, input().split())

list_adj = [[] * (N + 1) for i in range(N + 1)]
for i in range(N + 1):
    for j in range(N + 1):
        if graph[i][j] == 1:
            list_adj[i].append(j)
print(list_adj)


```





#### BOJ 2897

```python
# R = 행의 개수
# C = 열의 개수
R, C = map(int, input().split())

parking_lot = []
for _ in range(R):
    parking_lot.append(input())

n_zero = 0
n_first = 0
n_second = 0
n_third = 0
n_fourth = 0

for r in range(R):
    for c in range(C):
        if r+1 == R or C+1 == C:
            break
        w = parking_lot[r][c]
        x = parking_lot[r][c+1]
        y = parking_lot[r+1][c]
        z = parking_lot[r+1][c+1]

        tmp = W+X+Y+Z

        if "#" in tmp: # 만약 빌딩이면 계속 실행
            continue
        else:
            n_car = tmp.count("X")
            if n_car == 0:
                n_zero += 1
            elif n_car == 1:
                n_first += 1
            elif n_car == 2:
                n_second += 1
            elif n_car == 3:
                n_third += 1
            elif n_car == 4:
                n_fourth += 1

print(n_zero) # 첫째 줄 출력
print(n_first)
print(n_second)
print(n_third)
print(n_fourth)
```





:sparkles::rocket: 인접 행렬과 인접 리스트를 사용해서 컴퓨터에게 그래프를 표현하는 방법을 수업시간에 배웠는데 실습에서 실제로 구현해보니까 헷갈리는 부분이 많았습니다. 부족한 부분은 다시 노트에 재정리를 해서 설명하는 방식으로 연습을 해야겠고 비슷한 문제들도 더 풀어봐야 겠다고 생각했습니다. 그리고 다양한 문제를 접하면서 이전에 배웠던 내용들을 다시 구현할 수 있어서 좋았던 것 같습니다.