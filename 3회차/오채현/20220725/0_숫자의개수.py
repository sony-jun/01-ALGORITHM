# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("./0_숫자의개수.txt")

a = int(input())
b = int(input())
c = int(input())

total = str(a * b * c)

for i in range(10): #0부터 9까지 count로 세기
    print(total.count(str(i)))