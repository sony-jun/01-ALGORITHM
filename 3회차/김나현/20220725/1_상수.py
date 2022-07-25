# https://www.acmicpc.net/problem/2908
# from math import remainder
# import sys

# sys.stdin = open("1_상수.txt")

def reverse(num):
    res = 0
    for i in range(2, -1, -1):
        num, remainder = divmod(num, 10)
        res += remainder * 10 ** i
    return res


num1, num2 = map(int, input().split())
rev_num1 = reverse(num1)
# print(rev_num1)
rev_num2 = reverse(num2)
# print(rev_num2)
if rev_num1 > rev_num2:
    print(rev_num1)
else:
    print(rev_num2)
