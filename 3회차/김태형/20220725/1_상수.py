# https://www.acmicpc.net/problem/2908

A,B=input().split()

if int(A[::-1])>int(B[::-1]):
    print(int(A[::-1]))
elif int(A[::-1])<int(B[::-1]):
    print(int(B[::-1]))