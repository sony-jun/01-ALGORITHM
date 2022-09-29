import heapq
import sys
sys.stdin = open('11286.txt')

numbers = int(input())
heap = []

for _ in range(numbers):
    num = int(sys.stdin.readline())
    if num != 0:
        heapq.heappush(heap, (abs(num), num))
    else:
        if heap :
            print(heapq.heappop(heap)[1])
        else:
            print(0)