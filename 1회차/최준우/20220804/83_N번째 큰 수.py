# https://www.acmicpc.net/problem/2693

T = int(input())

for test_case in range(T):
    A = list(map(int, input().split()))
    A_sorted = sorted(A)
    print(A_sorted[-3])
