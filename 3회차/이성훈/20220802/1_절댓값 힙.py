# https://www.acmicpc.net/problem/11286
import sys
import heapq

sys.stdin = open("1_절댓값 힙.txt")
input = sys.stdin.readline

n = int(input())

heap = []

for _ in range(n):
    x = int(input())

    if x != 0:
        heapq.heappush(heap, (abs(x), x))  # tuple type으로 push => tuple type[0](==abs(x))를 기준으로 정렬될 것
    
    else:
        if heap:
            print(heapq.heappop(heap)[1])  # tuple type[1] => abs() 하지 않은 원래 x값
        else:
            print(0)

    
    
