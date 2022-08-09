
import sys

sys.stdin = open("0_문제 21. 무방향 그래프 표현하기.txt")

N, M = map(int, input().split()) 
list_ = []
for _ in range(N+1):
    list_.append([0] * (N+1))

list_2 = []
for _ in range(N+1):
    list_2.append([])

for _ in range(M):
    v1, v2 = map(int, input().split())
    list_[v1][v2] = 1
    list_[v2][v1] = 1
    list_2[v1].append(v2)
    list_2[v2].append(v1)

print(list_)
print(list_2)


    
