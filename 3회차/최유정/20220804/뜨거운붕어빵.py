# https://www.acmicpc.net/problem/11945
import pprint from pprint
#입력 행을 좌우반전
N, M = map(int, input().split())
list_ = []
for i in range(N):
    list_.append(list(map(int,input())))
print(list_)
