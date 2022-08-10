import heapq
import sys

sys.stdin = open("11286input.txt")
#x_list = [1,-1,0,0,0,1,1,-1,-1,2,-2,0,0,0,0,0,0,0]
x_list = []
input = sys.stdin.readline

t = int(input())

for i in range(t):
    x_list.append(int(input()))
    
min_heap = []
abs_heap = []
abs_min = 0
for i in x_list:
    if i != 0:
        heapq.heappush(min_heap, i)
        heapq.heappush(abs_heap, abs(i))
        #print(min_heap)
        #print(abs_heap)
    elif len(min_heap) != 0:
        abs_min = min(abs_heap)
        #print(abs_min)
        if -(abs_min) in min_heap:
            heapq.heappop(abs_heap)
            min_heap.remove(-(abs_min))
            print(-(abs_min))
        else:
            heapq.heappop(abs_heap)
            min_heap.remove(abs_min)
            print(abs_min)
        #print(min_heap)
        #print(abs_heap)
    else :
        print(0)
        #print(min_heap)
        #print(abs_heap)
