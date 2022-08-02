import sys
import heapq

sys.stdin = open("01_11286.txt", "r")

N = int(input())

heap = []       # heappush할 목록

for tc in range(1, N + 1):  # 18번 돌릴거야.
    num = int(input())      # txt에 있는 숫자들 넣을거야.
    if num != 0:
        heapq.heappush(heap, (abs(num), num))   # abs는 절대값 함수. 절대값과 원래값을 같이 넣고, 값이 다르면 적은 수(음수)가 추가.
    else:
        try:
            print(heapq.heappop(heap)[1])
        except:
            print(0)