import heapq

T = int(input())
numbers = []
numbers_pop = []
for _ in range(T):
    a = int(input())
    if a > 0:
        heapq.heappush(numbers, a)
    else:
        if len(numbers) == 0:
            numbers_pop.append(0)
        else:
            numbers_pop.append(heapq.heappop(numbers))
for a in numbers_pop:
    print(a)
