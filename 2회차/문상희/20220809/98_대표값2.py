numbers = []
for i in range(5):
    number = int(input())
    numbers.append(number)
numbers = sorted(numbers)
print(sum(numbers) // 5)
print(numbers[5 // 2])