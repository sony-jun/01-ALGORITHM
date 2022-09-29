# https://www.acmicpc.net/problem/2606

import sys
sys.stdin = open('0.txt', 'r')

n = int(input()) # 정점의 수
m = int(input()) # 간선의 수

 # 인접리스트 생성
com = [[] for _ in range(n+1)]

for i in range(m):
    c1, c2 = map(int,input().split())
    com[c1].append(c2)
    com[c2].append(c1)

# 방문 체크용
v = [False] * (n+1)

# 1번 컴퓨터부터 시작
stack = [1]

# 1번 컴퓨터 방문 처리
v[1] = True

# 스택이 비어있지 않다면 계속 반복하기
while stack: 
    # 현재 위치 빼내서 보기
    virus = stack.pop()

    # 1번 컴퓨터와 인접한 컴퓨터 조회
    for j in com[virus]:
        # 방문하지 않았다면, False라면
        if not v[j]: 
            v[j] = True # True로 방문처리

            # 스택에 넣어서 이동할 곳이 있다면 이동할 수 있게 하고,
            # 없다면 그대로 빼서 되돌아 갈 수 있도록 함
            stack.append(j)
            
# True 값을 더하고 시작 컴퓨터 빼기
print(sum(v) - 1)
