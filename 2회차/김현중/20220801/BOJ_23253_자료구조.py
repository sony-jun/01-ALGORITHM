import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

N, M = map(int, input().split())
sorting = True                              # 초기 정렬값 = True
for i in range(M):                          # 더미 M 개만큼 순회
    n = int(input())                        # 각 더미에 쌓여있는 책의 개수
    lst = [*map(int, input().split())]      # lst = 더미에 쌓여있는 책의 순서 , [3, 1]
    if lst != sorted(lst, reverse=True):    # 만약 더미의 책의 순서가 내림차순이 아닐 경우,
        sorting = False                     # 정리 할 수 없음.
        break

if sorting == True:                         # 정리 가능
    print('Yes')
else: print('No')