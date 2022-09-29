import sys
import heapq as h

input = sys.stdin.readline

N = int(input())

numbers = []

for _ in range(N):
    val = int(input().strip())
    if val:
        # https://hellominchan.tistory.com/231
        h.heappush(numbers, (abs(val), val))
    else:
        if numbers:
            print(h.heappop(numbers)[1])
        else:
            print(0)