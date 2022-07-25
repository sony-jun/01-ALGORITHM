# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("0_숫자의개수.txt")

A = int(input())
B = int(input())
C = int(input())

mul = A * B * C
# print(mul) 17037300
mul_str = str(mul)
ls = []
count = {}
for i in mul_str:
    ls.append(i)
# print(ls)
for j in range(10):
    count[j] = 0
    #print(count)
for num in ls:
    count[int(num)] += 1
for key, val in count.items():
    print(val)


#===================================
    
# A = int(input())
# B = int(input())
# C = int(input())

# mul = A * B * C
# # print(mul) 17037300
# mul_str = str(mul)
# for i in range(10):
# 	print(mul_str.count(str(i)))