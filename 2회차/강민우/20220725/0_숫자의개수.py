# https://www.acmicpc.net/problem/2577
from re import L
import sys

sys.stdin = open("0_숫자의개수.txt")

A = int(input())
B = int(input())
C = int(input())

total = A * B * C
total_number = {}
total_list = list(str(total))


for a in range(10) :
    if str(a) in total_list:
        for i in total_list :
            if str(a) == i:
             total_number[str(a)] = total_number.get(str(a) , 0) + 1
    else : total_number[str(a)] =0
        

for result in total_number.values() :
    print(result)

