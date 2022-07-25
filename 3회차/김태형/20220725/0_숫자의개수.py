# https://www.acmicpc.net/problem/2577
# import sys

# sys.stdin = open("0_숫자의개수.txt")
# num = 1
# for i in sys.stdin:
#     num*=int(i)
# for j in range(10):
#     print(str(num).count(str(j)))

A,B,C = map(int,input().split())
num = A*B*C
print(num)
for j in range(10):
    print(str(num).count(str(j)))