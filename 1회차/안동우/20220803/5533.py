from pprint import pprint
import sys
from tkinter import N
from pprint import pprint
sys.stdin = open("5533.txt", "r")

N=int(input())

qwe=[[],[],[]]
for i in range(N):
    a,b,c,=map(int,input().split())
    qwe[0].append(a)
    qwe[1].append(b)
    qwe[2].append(c)
