# https://www.acmicpc.net/problem/2908
import sys

sys.stdin = open("1_상수.txt")

a, b = input().split()

a_list = []
b_list = []
for i in a:
    a_list.append(i)
for j in b:
    b_list.append(j)

temp = a_list[0]
a_list[0] = a_list[2]
a_list[2] = temp

temp2 = b_list[0]
b_list[0] = b_list[2]
b_list[2] = temp2

# a_list = ['4', '3', '7']
# b_list = ['3', '9', '8']
result = a_list[0]+a_list[1]+a_list[2]
result2 = b_list[0]+b_list[1]+b_list[2]
# 437
# 398
if result > result2:
    print(result)
else:
    print(result2)
