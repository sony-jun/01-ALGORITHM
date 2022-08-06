import sys

sys.stdin = open('성 지키기.txt')

n,m = map(int,input().split())

lst = [list(input()) for _ in range(n)]
print(lst)


