import sys
from tkinter import N
sys.stdin = open("5063.txt", "r")

N=int(input())
#r 그냥수익
#e 광고하고 수익
#c 광고비
for i in range(1,N+1):
    r,e,c=map(int,input().split())
    if e-c > r:
        print("advertise")
    elif e-c ==r:
        print("does not matter")
    elif e-c <r:
        print("do not advertise")