
import sys

sys.stdin = open("16_쉽게푸는문제.txt")

num_list = []
num = 0
a, b = map(int,input(). split())
for i in range(1,b+1):
    num += 1
    for j in range(i):
        num_list.append(num)

   
print(sum(num_list[a-1: b]))