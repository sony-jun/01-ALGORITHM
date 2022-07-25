# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")
number,number2 = map(int,input()[::-1].split())

if number>number2:
    print(number)
else:
    print(number2)