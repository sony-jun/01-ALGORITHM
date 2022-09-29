import sys
sys.stdin = open("22_X보다 작은 수_10871.txt", "r")


N, X = map(int, (input().split()))
A = list(map(int, input().split()))

for num in A:
    if num < X:
        print(num, end=" ")