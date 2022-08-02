# https://www.acmicpc.net/problem/11286
# 문제11286번.절댓값 힙
# 시간제한:1초, 메모리제한:256MB



# 입력
'''
1. 연산의 갯수 N
- 1 <= N <= 100,000
2. N개의 줄에는 연산에 대한 정보를 나타내는 정수 x
- x != 0: 배열에 x라는 값을 추가하는 연산을 의미
- x = 0: 배열에 절댓값이 가장 작은 값을 출력하고 그 값을 배열에서 제거하라는 의미 
'''



# 출력
'''
1. 입력에서 0이 주어진 횟수만큼 답을 출력
- 배열이 비어있는데, 값을 출력하라고 한 경우에는 0을 출력
'''



# 코드
import sys, heapq

sys.stdin = open('input_text/11286.txt')

N = int(input())
heap = []

for _ in range(N):
    num = int(sys.stdin.readline())
    # 0이 아닌 정수인 경우
    if num != 0:
        # 절댓값이 가장 작은 값이 우선되게 push
        # (절댓값, 실제값) 튜플 형식으로 추가
        heapq.heappush(heap, (abs(num), num))
    # 0인 경우
    else:
        if heap:
            # 절댓값이 가장 작은 값을 우선해서 pop
            # (절댓값, 실제값) 튜플 형식을 제거
            print(heapq.heappop(heap)[1])
        else:
            print(0)



# 실행결과(메모리:39544KB, 시간:184ms)