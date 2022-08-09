
from pprint import pprint
import sys

sys.stdin = open("1_문제 22. 유방향 그래프 표현하기.txt")

N, M = map(int, input().split())
list_1 = []
list_2 = []

for _ in range(N+1):
    list_1.append([0] * (N+1))

for _ in range(N+1):
    list_2.append([])

for _ in range(M):
    v1, v2 = map(int, input().split())
    list_1[v1][v2] = 1
    list_2[v1].append(v2)


pprint(list_1)
print(list_2)



    
