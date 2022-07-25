# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("0_숫자의개수.txt")


a = int(input())
b = int(input())
c = int(input())
dic = {}
s = a*b*c
for i in range(10):
    dic[str(i)]=0
for char in str(s):
    dic[char] += 1
for n in range(10):
    print(dic[str(n)])