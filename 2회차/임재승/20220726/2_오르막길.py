# https://www.acmicpc.net/problem/2846

# 높이를 측정한 횟수
T = int(input())
# 측정한 높이를 받아서 리스트화 시켰습니다.
P = list(map(int, input().split()))
# 가장 마지막값까지 오르막일경우를 고려해서 끝값에 0을 넣어줬습니다.
P += [0]
# start 변수에 첫 높이를 넣어줬고 결과에 0을 넣어줬습니다.
start = P[0]
result = 0

for i in range(1, T+1):
    # 배열 두번째값부터 시작해서 0보다 크면 계속 진행
    if P[i] > P[i-1]:
        continue
    # 아니라면 
    else:
        # 만약 result값이 P[i - 1] - start보다 클경우
        if result > P[i - 1] - start:
            start = P[i]
            continue
        # 아닐경우
        else :
            result = P[i - 1] - start
        # start 값을 재설정
        start = P[i]

print(result)




# n = int(input())

# # 길의 각 높이, 오르막길 높이, 오르막길 높이들 
# n_height = list(map(int, input().split()))
# n_up = 0
# n_ups = []

# # 높이가 올라갈수록 그 값을 더해주며 리스트에 저장
# for i in range(len(n_height) - 1):
#     if n_height[i] >= n_height[i + 1]:
#         n_up = 0
#     else:
#         n_up += (n_height[i + 1] - n_height[i])
#     n_ups.append(n_up)

# # 가장 큰 오르막길 출력
# print(max(n_ups))