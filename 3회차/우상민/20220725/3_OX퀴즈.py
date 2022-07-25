# https://www.acmicpc.net/problem/8958
import sys

sys.stdin = open("3_OX퀴즈.txt")

T = int(input())               
for R in range(1, T+1):
    A = input()               
    count = 0
    total = 0
    for i in A:
        if i == ('O'):         
            count += 1        
            total += count   
        else:
            count = 0         
    print(total)
