# https://www.acmicpc.net/problem/2908
import sys


sys.stdin = open("1_상수.txt")
a, b = input().split(' ')
a_reverse = []
b_reverse = []
for i in range(2,-1,-1):
    a_reverse.append(a[i])
    b_reverse.append(b[i])
a1= "".join(a_reverse)
b1= "".join(b_reverse)
a1 = int(a1)
b1 = int(b1)
if a1 > b1:
    print(a1)
else:
    print(b1)




