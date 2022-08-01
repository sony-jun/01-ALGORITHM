# 1.  교과서 권 수 n, 교과서 더미 m
# i 더미에 쌓인 교과서는  k 두번째는 k 개의 정수
# 내림차순

import sys


sys.stdin = open("_자료공부.txt")

n, m = map(int,input().split())
dumis = []
ok = True
for i in range(m):
    x = int(input())
    k = list(map(int, input().split()))
 