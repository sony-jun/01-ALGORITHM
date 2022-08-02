# N개의 수가 주어졌을 때, 이를 오름차순으로 정렬하는 프로그램을 작성하시오.

from heapq import heappop

N = int(input())
A = []
for i in range(N):
    A.append(int(input()))
    A.sort()
for i in A:
    print(i)