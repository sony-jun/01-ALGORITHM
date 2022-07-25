# https://www.acmicpc.net/problem/2577
import sys

sys.stdin = open("0_숫자의개수.txt")

abc = []

for three in range(3):
    abc.append(int(input()))
    
abc = list(str(abc[0] * abc[1] * abc[2]))

for i in range(10):
    print(abc.count(str(i)))