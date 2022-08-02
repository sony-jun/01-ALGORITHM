# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("0_숫자의개수.txt")

total = 1
for n in range(3):
    i = int(input())
    total *= i
total_str = str(total)  

for num in range(10): 
    num_count = total_str.count(str(num))
    print(num_count)


# A = int(input())
# B = int(input())
# C = int(input())

# total = str(A*B*C)  # cnt method를 위해 숫자를 곱해서 str타입으로 변환

# for int in range(10):  # 0부터 9까지
#     int_cnt = total.count(str(int))
#     print(int_cnt)