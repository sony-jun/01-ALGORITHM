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
input = sys.stdin.readline
# sys.stdin = open('11286.txt')
import heapq

heap = []

n = int(input())
for _ in range(n):
    num = int(input())
    if num < 0:
        heapq.heappush(heap,[abs(num),-1])
    elif num > 0:
        heapq.heappush(heap,[abs(num),1])
    elif num == 0:
        if len(heap) == 0:
            print(0)
        else:
            number = heapq.heappop(heap)
            print(number[0]*number[1])