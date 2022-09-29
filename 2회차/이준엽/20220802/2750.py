n = int(input())
numbers = set()
for i in range(n):
    number = int(input())
    numbers.add(number)
numbers = list(numbers)
numbers.sort()
print(*numbers,sep='\n')