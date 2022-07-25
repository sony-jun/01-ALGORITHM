# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")
a,b = map(int, input().split())
cnt =0

def changeValue(a):
    n2=0
    value = len(str(a))
    for i in range(value):
        n1 = a % 10
        a = a//10
        n2 += n1*(10**(value-1-i))
    return n2
if changeValue(a) >= changeValue(b):
    print(changeValue(a))
else:
    print(changeValue(b))