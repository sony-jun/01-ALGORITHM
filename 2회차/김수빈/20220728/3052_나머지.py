import sys

sys.stdin = open("3052_나머지.txt")

remain = []

for i in range(10):
    n = int(input())
    div = n % 42
    remain.append(div)

print(len(set(remain)))