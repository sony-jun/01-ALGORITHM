# https://www.acmicpc.net/problem/8958
import sys
from tkinter import N

sys.stdin = open("3_OX퀴즈.txt")
T = int(input())

for i in range(1, T+1):
    OX = input()
    count = 1
    sum = 0
    a = list(OX)
    for j in OX: 
 
        if j == 'O' :   
            sum += count
            count += 1
        else :
            count = 1
    print(sum)
        
    
    