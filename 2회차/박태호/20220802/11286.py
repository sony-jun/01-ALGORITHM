# 절대값 힙
# 배열에 정수 x (x ≠ 0)를 넣는다.
# 배열에서 절댓값이 가장 작은 값을 출력하고,
# 그 값을 배열에서 제거한다. 절댓값이 가장 작은 값이 여러개일 때는,
# 가장 작은 수를 출력하고, 그 값을 배열에서 제거한다.
import heapq

# heap = []
# heapq.heappop(heap)# 비어있으면 출력이 안됨
# print(heap)
import sys
sys.stdin = open('11286.txt','r')
#입력 1
n = int(sys.stdin.readline())
# 힙 생성
heap = []
heapq.heapify(heap)

# n번 입력 및 조건문
for _ in range(n):
    num = int(sys.stdin.readline())
    min_ = 0
    if num != 0:  # 0 이 아니면 추가
        heapq.heappush(heap, (abs(num),num)) # 튜플로 넣음(절대값, 원본) 
    else: # 0 이고
        if heap: # 비어있지 않다면            
            print(heapq.heappop(heap)[1])
        else:  # 비었으면 0
            print(0)
# [1,1,-1,-1,2,-2] -> [-2,1,1,-1,-1,2]
# 출력 = -1 | 1| 0 |
 # 절대값이 가장 작은 수를 찾는다.
 # 여러개면 더 작은 수 출력
 # 처음에 받은 수를 