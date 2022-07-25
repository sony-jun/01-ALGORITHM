# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")

num1, num2 = input().split()

num1 = num1[::-1]
num2 = num2[::-1]
print(num1, num2)
if num1> num2:
    print(num1)
elif num1<num2:
    print(num2)