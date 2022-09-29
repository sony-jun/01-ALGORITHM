import sys

input = sys.stdin.readline

total = int(input())
X = int(input())

check = 0
for _ in range(X):
    a, b = map(int, input().split())
    check += a * b

print("Yes" if check == total else "No")