import sys

sys.stdin = open("4_뒤집힌 덧셈.txt")

a, b =input().split()
x= str(int(a[::-1])+int(b[::-1]))

print(int(x[::-1]))