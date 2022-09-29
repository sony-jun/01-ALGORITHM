# https://www.acmicpc.net/problem/2908
# import sys

# sys.stdin = open("1_상수.txt")

num = input().split()

num_list = []

for i in num :
  i = i[: :-1]
  num_list.append(int(i))

print(max(num_list))