# https://www.acmicpc.net/problem/2846
import sys

sys.stdin = open("2_오르막길.txt")

T = int(input())                            # 반복하는 값 입력
N = list(map(int,(input().split())))        # 길 높이 입력
N_list = []                                 
N_sum = 0

for i in range(1, T):
    if N[i] - N[i-1] > 0:                   # 만약 오른쪽 길 높이가 더 크면
        N_sum += N[i] - N[i-1]              # 길 높이 차 만큼 더해라
        if i == T-1:                        # 더 이상 더할 값이 없으면
            N_list.append(N_sum)            # 그동안 더한값을 리스트에 저장해라

    else:                                   # 만약 오른쪽 길 높이가 더 작으면
        N_list.append(N_sum)                # 그동안 더한 값을 리스트에 저장하고
        N_sum = 0                           # 초기화 해라
        
print(max(N_list))                          # 리스트에 저장한 것 중 가장 큰 값 출력

    
