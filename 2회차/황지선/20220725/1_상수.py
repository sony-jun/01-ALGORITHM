# https://www.acmicpc.net/problem/2908
# 2908번 상수

a, b = input().split()

a = int(a[::-1]) 
b = int(b[::-1])

if a > b : 
    print(a)
else :
    print(b)
