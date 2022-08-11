import sys
sys.stdin = open('01_input.txt')

x = int(input())
n = int(input())
items = []

for _ in range(n):
    a, b = map(int, input().split())
    items.append(a * b)

# total = sum(items)

print('Yes' if sum(items) == x else 'No')
