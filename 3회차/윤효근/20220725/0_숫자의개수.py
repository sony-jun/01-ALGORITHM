# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("0_숫자의개수.txt")
a=int(input())
b=int(input())
c=int(input())
tmp=map(int,str(a*b*c))
list1 = list(tmp)
for i in range(0,10):
    print(list(list1).count(i))


