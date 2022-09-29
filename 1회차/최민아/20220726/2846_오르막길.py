import sys
sys.stdin = open("20220726/2846_오르막길.txt")

N = int(input())                        # 측정 개수 N
Pi = list(map(int, input().split()))    # 측정한 높이 수열 Pi
height = 0                              # 최대 오르막길 높이 height

for i in range(N):
    for j in range(i+1, N):
        if Pi[j-1] < Pi[j]:             # 직전 높이가 더 작으면 오르막길
            height = max(height, Pi[j]-Pi[i]) # 오르막길 최대 높이 구하기
        else:
            break                       # 내리막길이면 break
print(height)       # 가장 큰 오르막길 출력, 없으면 초기값인 0 출력