from re import L
import sys

sys.stdin = open('bj7568.txt', 'r')       


T = int(input())
alist = []  #   키
blist = []  #   몸무게
for i in range(T) :
    a= list(map(int, input().split()))
    print(a)



