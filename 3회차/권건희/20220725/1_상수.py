# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")

a,b=input().split()
c=""
d=""
for i in a:
    c=i+c
for i in b:
    d=i+d    
if int(c)>int(d):
    print(int(c))
elif int(c)<int(d):
    print(int(d))
