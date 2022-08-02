import sys
sys.stdin = open('2161.txt')

N = int(input())
numbers = list(range(1, N+1))
dis = []

while len(numbers) != 1:
    dis.append(numbers.pop(0))
    numbers.append(numbers.pop(0))

for i in range(len(dis)):
    print(dis[i], end=' ')
print(numbers[0])