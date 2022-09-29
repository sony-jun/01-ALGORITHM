# https://www.acmicpc.net/problem/2750
# 문제2750번.수 정렬하기
# 시간제한:1초, 메모리제한:128MB



# 입력
'''
1. 수의 갯수 N
- 1 <= N <= 1,000
2. N개의 줄에 정수
- -1,000 <= 정수 <= 1,000
- 수는 중복되지 않음
'''



# 출력
'''
1. N개의 줄에 오름차순으로 정렬한 결과를 한 줄에 하나씩 출력
'''



# 코드 1
import sys

sys.stdin = open('input_text/2750.txt')

T = int(input())
nums = [int(input()) for _ in range(T)]

nums.sort()
for n in nums:
    print(n)



# 실행결과(메모리:30840KB, 시간:108ms)



# 코드 2
import sys, heapq

sys.stdin = open('input_text/2750.txt')

T = int(input())
nums = []

# 힙으로 push
for _ in range(T):
    heapq.heappush(nums, int(input()))

# 힙에서 pop
for _ in range(T):
    print(heapq.heappop(nums))



# 실행결과(메모리:32908KB, 시간:148ms)