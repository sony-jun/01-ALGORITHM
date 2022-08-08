# https://www.acmicpc.net/problem/2798
import sys

sys.stdin = open("0_블랙잭.txt")


max_sum = 0
N, M = map(int, input().split())            # N = 카드 갯수 M = 넘지 말아야 할 숫자

T = list(map(int, (input().split())))       # 입력 하는 카드 값

for i in range(N-2):                        # 첫번째 카드 = 1 ~ 3   0 - 2
    for j in range(i+1,N-1):                # 두번째 카드 = 2 ~ 4   1 - 3
        for k in range(j+1, N):             # 세번째 카드 = 3 ~ 5   2 - 4
            sum_ = T[i]+T[j]+T[k]           # 세 카드의 합

            if M >= sum_ > max_sum:         # 넘지 말아야 할 숫자 >= 현재 세 카드의 합 > 최대 세 카드의 합
                max_sum = sum_              # 최대 세 카드의 합 갱신
                
            if max_sum == M:                # 최대 값 == 넘지 말아야 할 숫자
                break

print(max_sum)