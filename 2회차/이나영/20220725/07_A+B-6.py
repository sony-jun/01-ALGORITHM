from re import A
import sys

sys.stdin = open("07_A+B-6.txt")

T = int(input())

for i in range(T):
    a,b = map(int, input(). split(','))
    print(a+b)

# input값 사이에 콤마찍기. split(',')