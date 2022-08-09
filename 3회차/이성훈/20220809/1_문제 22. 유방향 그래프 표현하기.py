
from pprint import pprint
import sys

sys.stdin = open("1_문제 22. 유방향 그래프 표현하기.txt")

N, M = map(int, input().split())            # 정점의 개수 N 간선의 개수 M
list_1 = []
list_2 = []

for _ in range(N+1):                        # n+1 * n+1의 크기의 행렬을 0으로 초기화
    list_1.append([0] * (N+1))

for _ in range(N+1):                        # N+1 의 개수만큼 빈 리스트 추가
    list_2.append([])

for _ in range(M):                          
    v1, v2 = map(int, input().split())      # 간선의 갯수 입력
    list_1[v1][v2] = 1                      # v1행v2열에 1 입력
    list_2[v1].append(v2)                   # v1번째 리스트에 v2값 입력


pprint(list_1)
print(list_2)



    
