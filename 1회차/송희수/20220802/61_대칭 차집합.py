import sys

sys.stdin = open("61_대칭 차집합.txt")

A, B = map(int, input().split())

A_set = set(map(str, input().split()))
B_set = set(map(str, input().split()))

print(len(A_set-B_set)+len(B_set-A_set))