import heapq

N = int(input())
total = []

for a in range(N):
    num = int(input())
    if num != 0:
        heapq.heappush(total,num)
    if num == 0:
        if len(total) > 0:
            print(heapq.heappop(total))
        else :
            print(0)
     

    

