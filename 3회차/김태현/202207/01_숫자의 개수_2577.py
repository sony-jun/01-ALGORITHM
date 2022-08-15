import sys
sys.stdin = open("01_숫자의 개수_2577.txt", "r")

A = int(input())
B = int(input())
C = int(input())

num = A * B * C

dic = {i:0 for i in range(10)}
# print(dic, "초기값")

for i in str(num):
    dic[int(i)] += 1
# print(dic, "after")

for j in dic.values():
    print(j)