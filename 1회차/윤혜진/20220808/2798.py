# https://www.acmicpc.net/problem/2798
# 문제2798번.블랙잭
# 시간제한:1초, 메모리제한:128MB



# 입력
'''
1. 카드의 갯수 N, 제한 숫자 M
- 3 <= N <= 100
- 10 <= M <= 300,000
2. N장의 카드에 쓰여있는 수
- 0 < 수 <= 100,000
'''



# 출력
'''
1. M을 넘지 않으면서 M에 최대한 가까운 카드 3장의 합을 출력
'''



# 코드 1
import sys

sys.stdin = open('input_text/2798.txt')

def find_near_M(nums, N, M):
    near_M = 0   # M에 가장 가까운 카드 3장의 합
    for fst in range(0, N - 2):   # 첫번째 카드
        for sec in range(fst + 1, N - 1):   # 두번째 카드
            for trd in range(sec + 1, N):   # 세번째 카드
                sum_3 = nums[fst] + nums[sec] + nums[trd]

                # M에 가장 가까운 카드 합 갱신
                if near_M < sum_3 <= M:
                    near_M = sum_3
                
                # 불필요한 반복 종료    
                if sum_3 == M:
                    return near_M
    
    return near_M


N, M = map(int, input().split())
cards = list(map(int, input().split()))
print(find_near_M(cards, N, M))



# 실행결과(메모리:30840KB, 시간:96ms)



# 코드 2
import sys
from itertools import combinations

sys.stdin = open('input_text/2798.txt')

N, M = map(int, input().split())
cards = list(map(int, input().split()))
print(max(sum(case) for case in combinations(cards, 3) if sum(case) <= M))



# 실행결과(메모리:30840KB, 시간:108ms)