import sys
input = sys.stdin.readline

import heapq
arr = []
command = []
n = int(input())
for i in range(n):
    number = int(input())
    command.append(number)
for com in command:
    if com != 0:
        heapq.heappush(arr, (abs(com),com))
    else:
        if len(arr) == 0:
            print(0)
        else:
            print(heapq.heappop(arr)[1])
        