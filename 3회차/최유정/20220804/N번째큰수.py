# https://www.acmicpc.net/problem/2693
T = int(input())
for i in range(T):
    A = list(map(int, input().split()))
    A.sort()
    print(A[-3])