# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("0_숫자의개수.txt")

a = int(input())
b = int(input())
c = int(input())

re = str(a*b*c) #a b c를 곱한값을 문자열로 바꾼다.

for i in range(10):
    print(re.count(str(i)))