import sys
sys.stdin = open('대칭 차집합.txt')

A,B = map(int,input().split())

A_ = set(map(int,input().split()))

B_ = set(map(int,input().split()))

print(len(A_^B_))

