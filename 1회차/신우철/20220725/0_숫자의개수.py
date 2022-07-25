# https://www.acmicpc.net/problem/2577
from posixpath import split
import sys

sys.stdin = open("0_숫자의개수.txt", "r")
number = int(input())
number2 = int(input())
number3 = int(input())
mul = str(number*number2*number3)
count = [0]*10
# 개수를 세는 list
for i in mul:
    for j in range(0 , 10):
        if int(i) == j:
            count[j]+= 1
        
for z in count:
    print(z)
        

