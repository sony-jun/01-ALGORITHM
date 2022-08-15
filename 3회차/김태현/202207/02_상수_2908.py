import sys
sys.stdin = open("02_상수_2908.txt", "r")

a, b = map(int, input().split())

a = int(str(a)[::-1])
b = int(str(b)[::-1])
print(max(a, b))