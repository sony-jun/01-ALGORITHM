import heapq
import sys

sys.stdin = open("1_절댓값 힙.txt")

n = int(input())
q_list=[]

for i in range(n):
    a=int(sys.stdin.readline().rstrip())
    if a != 0:
        heapq.heappush(q_list,(abs(a),a))
    else:
        if not q_list:
            print(0)
        else:
            print(heapq.heappop(q_list)[1])