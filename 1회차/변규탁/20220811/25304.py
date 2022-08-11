import sys

sys.stdin = open("_25304.txt", "r")

X = int(input())

x = 0
for _ in range(int(input())):
    a, b = map(int, input().split())
    x += a*b

if X == x:
    print("Yes")
else:
    print("No")