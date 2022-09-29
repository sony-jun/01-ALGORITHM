# import heapq

# numbers = [0, 12345678, 1, 2, 0, 0, 0, 0,32]
# heap = []

# for number in numbers:
#     if number != 0:
#         heapq.heappush(numbers,number)
#     else : 
#         if len(heap) == 0:
#             print(0)
#         else:
#             print(heapq.heappop(numbers))


import heapq
from re import X

heap = []

N = int(input())
for _ in range(N):
    X = int(input)
    
    if X != 0:
        heapq.heappush(heap,X)
    else : 
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap))

            ### 계속 런타임오류 남.. 시간초과 나고...ㅠㅠ..###
    
