numbers = []

for _ in range(5):
    N = int(input())
    numbers.append(N)

numbers.sort()
print(sum(numbers)//len(numbers))
print(numbers[2])