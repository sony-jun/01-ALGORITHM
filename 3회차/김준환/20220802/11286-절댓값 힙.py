# import sys
# input = sys.stdin.readline

# n = int(input())


# original_num = []
# absolu_num = []

# for _ in range(n):
#     num = int(input())
#     if num == 0 and len(original_num) == 0:
#         print(0)
#     elif num != 0:
#         original_num.append(num)
#         absolu_num.append(abs(num))
#     else:
#         min_num = min(absolu_num)
#         original_idx = absolu_num.index(min_num)
#         answer = original_num[original_idx]
#         print(answer)
#         original_num.pop(original_idx)
#         absolu_num.pop(original_idx)

import sys
# input = sys.stdin.readline
sys.stdin = open('11286.txt')
import heapq

n = int(input())

heap = []
storage = []

for _ in range(n):
    num = int(input())
    if num == 0 and len(heap)==0:
        print(0)
        continue
    elif num != 0:
        heapq.heappush(heap,num)
    else:
        if len(heap) == 1:
            print(heapq.heappop(heap))
            continue
        print(f'heap = {heap}')
        first = heapq.heappop(heap)
        second = heap[0]
        print(f'first = {first}')
        print(f'heap = {heap}')
        print(f'second = {second}')
        while abs(first) > abs(second):
            storage.append(first)
            first = heapq.heappop(heap)
            second = heap[0]
        print(first)
        for i in storage:
            heapq.heappush(heap,i)
        storage = []