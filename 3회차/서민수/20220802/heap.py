import heapq

numbers = [5, 3, 2, 4, 1]

heapq.heapify(numbers)
print(numbers)
heapq.heappop(numbers)
print(numbers)
heapq.heappush(numbers ,0)


print(numbers)