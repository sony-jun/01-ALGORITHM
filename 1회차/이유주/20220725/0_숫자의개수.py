# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("0_숫자의개수.txt")


#숫자가 몇번 쓰였는지 0부터 9까지 세기

A = int(input())
B = int(input())
C = int(input())

multiply = list(str(A * B * C))

for x in range(10):
    print(multiply.count(str(x)))