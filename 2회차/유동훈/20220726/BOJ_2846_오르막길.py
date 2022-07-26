# https://www.acmicpc.net/problem/2846
# 오르막길

# 풀이
N = int(input())

height = list(map(int, input().split()))
size = []

for i in range(N-1):
    cnt = 0
    while height[i + cnt] < height[i + cnt + 1]:
        cnt += 1 
        if i + cnt == N -1:
            break
    size.append(height[i + cnt] - height[i])

if N == 1 or max(size) == 0:
    print(0)
else:
    print(max(size))