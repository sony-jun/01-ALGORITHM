import sys
sys.stdin = open ('2592.txt')

N = 10
numbers = []
mode = []
for i in range(N):
    numbers.append(int(input()))

print(sum(numbers) // N)

for j in numbers:
    mode.append(numbers.count(j))

print(numbers[mode.index(max(mode))])