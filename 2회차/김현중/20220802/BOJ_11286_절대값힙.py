import sys                                  # 배열에 정수 x를 넣는다. (2, 2), (2, -2)
import heapq                                # x == 0 : 배열에서 절대값이가장 작은 값을 꺼낸다.
sys.stdin = open('11286.txt')               # 절대값이 가장 작은 값이 여러개면 더 작은 값을 꺼낸다. 1, -1 
input = sys.stdin.readline
N = int(input())

heap = []
heapq.heapify(heap)

for _ in range(N):
    x = int(input())
    if x != 0:
        heapq.heappush(heap, (abs(x), x))   # 절대값이 가장 작은값 순서로 정렬, 원래값도 같이 튜플형태로 추가 
    elif x == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heap)
            print(heapq.heappop(heap)[1])   # 절대값이 같은 숫자중 더 작은 값을 꺼내기 위해