import sys
sys.stdin = open('B11286.txt')

#heap[0]은 항상 가장 작다 001 00-1 처럼 세개짜리튜플은 후자
import heapq
n = int(input())
heap = []
for _ in range(n):
    x = int(input())
    if x != 0: # 0이 아닌 경우   
        #heap에 []을 넣는데 절댓값 같은 애들이 잇으면 실제값비교해서 넣는다.
        heapq.heappush(heap, [abs(x),x]) #절대값 튜플로 만들어주기
    else: # 0인 경우
        if len(heap) < 1:
            print(0)
        else: 
            print(heapq.heappop(heap)[1])
            
            #다시 풀어보기 
            
    """
    파이썬에서 heap은 최소힙
    그럼 최대힘은 어케 ? 
    """