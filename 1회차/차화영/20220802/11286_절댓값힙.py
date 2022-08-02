import sys
import heapq
input = sys.stdin.readline

N = int(input())
arr = [] # 비어 있는 배열에서 시작
for i in range(N):
    x= int(input()) # 정수 x 입력 받음
    
    # if x > 0:                           # x가 양수일 때
    #     heapq.heappush(arr, (x, x))     # arr에 (절대값, 기본값) 추가
    
    # elif x < 0:                         # x가 음수일 때
    #     heapq.heappush(arr, (-x, x))    # arr에 (절대값, 기본값) 추가 - x가 음수이면 -를 곱해야 양수로 절대값이 됨!

    # 위의 두 조건을 합쳐서 다음과 같이 간략하게 작성 가능
    if x != 0:
        heapq.heappush(arr, (abs(x), x)) # tuple type으로 push => tuple type[0](==abs(x))를 기준으로 정렬될 것
    
    else: # 입력이 양수도 음수도 아닌 '0'일 때!
        if len(arr) == 0: # 배열의 길이가 0 -- 비어 있을 때 (if not num: 라고 써도 됨)
            print(0)
        else:
            n, m = heapq.heappop(arr)   # arr에서 가장 작은 원소를 n,m 에 저장하고 pop
            print(m)                    # m을 출력 - 입력 받은 x 그자체 (n:절대값, m:기본값)