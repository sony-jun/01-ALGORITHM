# https://www.acmicpc.net/problem/2908
import sys
sys.stdin = open(r"2회차\전준영\20220725\1_상수.txt",'r',encoding='utf-8')
str0=""
arr=[]
int0=999
for i in sys.stdin:
    str0=i[::-1]
    arr=str0.split()
    if(int(arr[1])>int(arr[0])):
        int0=arr[1]
    else:
        int0=arr[1]
    print(int0)