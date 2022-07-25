# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("0_숫자의개수.txt")


A = int(input())
B = int(input())
C = int(input())

re = A * B * C

count = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

for i in str(re):
    count[int(i)] +=1

for j in count:
    print(j) 
    