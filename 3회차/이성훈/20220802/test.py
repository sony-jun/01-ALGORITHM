import heapq


N = 3

list_2 = []
for _ in range(N):

    T = int(input())

    if T == 0:              # pop해야 할 때
        if list_2 != 0:      # list가 존재 할 때
            print(heapq.heappop(list_2))
        else:               # list가 없으면
            print(0)

    else:                   # 숫자 넣을 때
        heapq.heappush(list_2, T)


