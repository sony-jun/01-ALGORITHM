import sys
sys.stdin = open("3052.txt")

numbers = []
for n in range(10):
    n = int(input())
    numbers.append(n % 42)
    remainder = set(numbers)
print(len(remainder))