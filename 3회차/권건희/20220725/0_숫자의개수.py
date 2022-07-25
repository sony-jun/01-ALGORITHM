# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("0_숫자의개수.txt")
a=int(input())
b=int(input())
c=int(input())
multi=a*b*c
# 멀티를 str로 변환하고 {}생성, 인덱스로 접근, 해당 밸류에 +1하자
multi=str(multi)
numbers={}
for i in range(10):
    numbers[i]=0
for n in multi:
    for i in range(10):
        if n==str(i):
            numbers[i]+=1
for i in range(10):
    print(numbers[i])            