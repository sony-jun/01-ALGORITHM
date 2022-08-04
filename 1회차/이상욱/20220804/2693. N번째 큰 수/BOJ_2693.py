import sys
sys.stdin = open('2693.txt')

T = int(input())

for i in range(1, T+1):
    N = 3
    A = list(map(int, input().split()))

    while N != 1:
        A[A.index(max(A))] = 0
        N -= 1
    print(max(A))


'''
T = int(input())

for i in range(1, T+1):
    N = 3
    A = list(map(int, input().split()))
    A.sort()
    print(A[-N])
'''

