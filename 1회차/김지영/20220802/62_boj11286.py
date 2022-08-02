import heapq

n = int(input())
heap = []
result = []
for _ in range(n):
    x = int(input())
    if x != 0:
        heapq.heappush(heap,(abs(x),x))
    else : 
        if heap == []:
            result.append(0)
        else : 
            result.append(heapq.heappop(heap)[1])
# print(result)
for r in result:
    print(r)