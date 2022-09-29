# https://www.acmicpc.net/problem/2846
# 문제2846번.오르막길
# 시간제한:1초, 메모리제한:128MB



# 입력
'''
1. 나열된 높이의 수 크기 N
- 1 <= N <= 1,000
2. N개의 높이
- 1 <= P <= 1,000
'''



# 출력
'''
1. 가장 큰 오르막길의 크기 출력
- 오르막길이 없는 경우, 0 출력
'''



# 코드 1
import sys

sys.stdin = open('input_text/2846.txt')

N = int(input())   # 높이의 나열 갯수
heights = list(map(int, input().split()))   # 높이의 나열
diff = 0   # 가장 큰 오르막길 높이차
left = 0   # 왼쪽 인덱스
right = left + 1   # 오른쪽 인덱스
while right < N:
    # 오르막길인 경우
    if heights[right - 1] < heights[right]:
        diff = max(diff, heights[right] - heights[left])
        right += 1
    # 오르막길이 아닌 경우(평지, 내리막길)
    else:
        left = right
        right += 1

print(diff)
        


# 실행결과(메모리:30840KB, 시간:68ms)



# 코드 2
sys.stdin = open('input_text/2846.txt')

N = int(input())   # 높이의 나열 갯수
heights = list(map(int, input().split()))   # 높이의 나열
max_diff = 0   # 전체구간에서의 높이차 최댓값
sub_diff = 0   # 부분구간에서의 높이차
for i in range(1, N):
    # 오르막길인 경우
    if heights[i] > heights[i - 1]:
        sub_diff += heights[i] - heights[i - 1]
        max_diff = max(max_diff, sub_diff)
    # 오르막길이 아닌 경우(평지, 내리막길)
    else:
        sub_diff = 0

print(max_diff)



# 실행결과(메모리:30840KB, 시간:68ms)