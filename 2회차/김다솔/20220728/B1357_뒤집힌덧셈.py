# https://www.acmicpc.net/problem/1357

import sys
sys.stdin = open('B1357.txt')

x, y = input().split() 
sum_ = str(int(x[::-1]) + int(y[::-1]))
print(int(sum_[::-1]))


# def rev(num):
#     return int(str(num)[::-1])
