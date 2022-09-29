import sys
sys.stdin=open('2587.txt')

numbers=[]
for i in range(5):
    numbers.append(int(input()))
numbers.sort()

print(int(sum(numbers) / len(numbers)))
print(numbers[2])
