# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("0_숫자의개수.txt")

list=[]
result = 1

for i in range(0,3):
    N = int(input())
    list.append(N)

for j in list:
    result *= j

result = str(result)

for k in range(0,10):
    print(result.count(str(k)))
