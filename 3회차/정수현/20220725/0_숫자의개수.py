# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("0_숫자의개수.txt")
data = [int(sys.stdin.readline()) for i in range(3)]
data = str(data[0]*data[1]*data[2])
table = {str(i):0 for i in range(10)}

for i in data:
    table[i] += 1

for i in '0123456789':
    print(table[i])