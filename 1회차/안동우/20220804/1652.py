from operator import le
import sys
from tkinter import N
from pprint import pprint
sys.stdin = open("1652.txt", "r")
input = sys.stdin.readline

N=int(input())
a=[]
r=0
e=0
for i in range(N):
    b=list(input().rstrip())#개행 제거
    a.append(b)

for q in range(N):
     z=0
     x=0
     for w in range(N):
          if a[q][w]==".":#가로 x가 빈자리
               x+=1
          else:#0초기화
               x=0
          if x==2:
               r+=1
               
          if a[w][q]==".":#세로 z가 빈자리
               z+=1
          else:#0초기화
               z=0
          if z==2:
               e+=1

print(r,e)