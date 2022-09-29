import sys
sys.stdin = open('1292.txt')

sum = 0
A, B = map(int, input().split())
numbers = []

for i in range(1, B+1):
    for j in range(i):
        numbers.append(i)

for i in range(A-1, B):
    sum += numbers[i]

print(sum)