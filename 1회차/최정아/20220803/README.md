## :sparkler:느낀점/배운점/부족한점



#### BOJ 1236

```python
# 성의 세로 크기: N, 가로 크기: M 주어짐
n, m = map(int, input().split())
# 성의 빈 리스트 생성
castle = []


for i in range(n):
    castle.append(input())

a, b = 0, 0

for i in range(n):
    # 경비원이 있는 칸 X가 i에 없으면
    if "X" not in castle[i]:
        # a에 1씩 증가
        a += 1

for j in range(m):
    if "X" not in [castle[i][j] for i in range(n)]:
        b += 1
# 경비원의 최솟값 출력
print(max(a, b))
```



#### BOJ 2167

```python
import sys
input = sys.stdin.readline

# 행렬의 크기 입력으로 주어짐
n, m = map(int, input().split())
# List Comprehension 사용해서 이차원 리스트 입력 받음
matrix = [list(map(int,input().split())) for _ in range(n)]

cnt = int(input())
for k in range(cnt):
    mum = 0
    i, j, x, y = map(int,input().split())
    
    for w in range(i-1,x):
        for v in range(j-1,y):
            mum += matrix[w][v]
    print(mum)
```



#### BOJ 1100

```python
# 빈 리스트 생성
chess = []
# 체스판 8x8 크기
# 반복문으로 행을 받음
for _ in range(8):
    # chess에 추가
    chess.append(list(map(str, list(input()))))

answer = 0
for i in range(8):
    for j in range(8):
        # i+j가 짝수면
        if (i + j) % 2 == 0:
            # [i][j]가 말이 있는 칸이면
            if chess[i][j] == 'F':
                # 1 증가
                answer += 1
                
print(answer)
```



:sparkles::rocket: for 반복문과 List Comprehension을 사용해서 행렬의 크기가 주어지거나 입력으로 주어지는 경우에 적용을 해보았고 이차원 리스트에 대해서 조금 더 이해하는 시간이 되었습니다. 