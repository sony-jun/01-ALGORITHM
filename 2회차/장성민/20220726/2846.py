n = int(input())

# 길의 각 높이, 오르막길 높이, 오르막길 높이들 
n_height = list(map(int, input().split()))
n_up = 0
n_ups = []

# 높이가 올라갈수록 그 값을 더해주며 리스트에 저장
for i in range(len(n_height) - 1):
    if n_height[i] >= n_height[i + 1]:
        n_up = 0
    else:
        n_up += (n_height[i + 1] - n_height[i])
    n_ups.append(n_up)

# 가장 큰 오르막길 출력
print(max(n_ups))

