import sys
import collections

sys.stdin = open("0_SASA 모형을 만들어보자.txt")

n,m = map(int,input().split(' '))
print(min(n/2,m/2))
