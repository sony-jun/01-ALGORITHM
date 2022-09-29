import heapq

hq = []

input = [1, -1, 2, 3, -4, 4, 5, -6, 7, 0]
print(input, "input")

for i in input:
    heapq.heappush(hq, [abs(i), i])

print(hq, "hq")