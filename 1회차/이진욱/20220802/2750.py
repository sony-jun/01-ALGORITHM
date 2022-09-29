import heapq

N = int(input())

num_list = []

for i in range(N):
    num = int(input())
    heapq.heappush(num_list,num)

for i in range(N):
    print(heapq.heappop(num_list))