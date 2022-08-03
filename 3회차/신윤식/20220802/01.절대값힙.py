import heapq

N = int(input())
lst = []
abs_lst = []
lst2 = []

for i in range(N):
    x = int(input())
    if x:
        lst.append(x)
    else:
        if len(lst) == 0:
            print(0)
        else:
            abs_lst = list(map(abs,lst))
            a = min(abs_lst)
            while True:
                heapq.heapify(lst)
                b = heapq.heappop(lst)
                if abs(b) > a:
                    continue
                elif abs(b) <= a:
                    print(b)
                    break
                heapq.heappush(lst,b)
            # heapq.heapify(lst)
            # 
            # heapq.heapify(abs_lst)
            # if 












            # a = heapq.heappop(abs_lst)

            # while True:
            #     b = heapq.heappop(lst)
            #     abs_b = abs(b)
                
            #     if abs_b > a:
            #         continue
            #     else: 
            #         print(b)
            #         break
                
