import heapq
numbers = [1, -1, 0, 0, 0, 1, 1, -1, -1, 2, -2, 0, 0, 0, 0, 0, 0, 0]
heap = []

for num in numbers:
    if num != 0:
        heapq.heappush(heap, -(num))
    else:
        if len(heap):
            print()
        else:
            heapq.heappop(heap)