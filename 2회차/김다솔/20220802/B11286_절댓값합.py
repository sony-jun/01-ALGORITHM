import sys
sys.stdin = open('B11286.txt')


import heapq
n = int(input())
arr = []
for _ in range(n):
    x = int(input())
    if x != 0: # 0이 아닌 경우
        heapq.heappush(arr, (abs(x),x)) #절대값 튜플로 만들어주기
    else: # 0인 경우
        if len(arr) < 1:
            print(0)
        else: 
            print(heapq.heappop(arr)[1])
            
            #다시 풀어보기 