# # https://www.acmicpc.net/problem/2846
import sys

sys.stdin = open("2846_오르막길.txt", "r")

# height = int(input())
# way = list(map(int, input().split()))
# cnt = 0
# list_ = []
# for i in range(1, height): # i는 1부터 입력받은 숫자까지
#     if way[i] > way[i-1]: 
#         cnt += way[i] - way[i-1]
#         if i == height-1:
#             list_.append(cnt)
#     else:
#         list_.append(cnt)
#         cnt = 0
# # print(list_)
# print(max(list_)) 

# # 예제입력 1
# # i = 1 일때 cnt = cnt + 1 ==> cnt = 0 + 1 = 1
# # i = 2 일때 else라서 cnt = 1 append해주고 cnt = 0 으로
# # i = 3 일때 cnt = cnt + 3 ==> cnt = 0 + 3 = 3
# # i = 4 일때 cnt = cnt + 2 ==> cnt = 3 + 2 = 5 
# # i == height-1 에 들어와서 마지막 cnt값 list_에 append 해주기 
N = int(input())
Pi = list(map(int, input().split()))    # 수열들을 리스트로 넣음.
Pi_length = 0       # 수열의 길이를 넣을 변수
list_ = []          # 수열의 길이가 하나가 아니니까 ( 오르막길은 여러개일수 있으니 ) 리스트를 만들어서, 오르막길의 길이를 여기다 넣을 예정
for i in range(N - 1):             
    if Pi[i + 1] > Pi[i]:   # 오르막길이라면 현재의 수보다 다음 수가 더 큼. 즉 다음수 - 현재의 수를 빼면 양수
        Pi_length += Pi[i + 1] - Pi[i]      # 그 값을 길이에 추가시켜줌.
    else:
        list_.append(Pi_length)     # else, 즉 오르막길이 풀린다면, 빈 리스트에 지금 오르막길의 높이를 넣어줌
        Pi_length = 0           # 오르막길은 초기화시킴
    if i == N - 2:                  # 끝까지 왔다면,
        list_.append(Pi_length)         # 길 자체가 끝이니 오르막길의 높이를 리스트에 넣음.

print(max(list_))       # 오르막길의 높이가 담긴 리스트중 최대값을 출력함.