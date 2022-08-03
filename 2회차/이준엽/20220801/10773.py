n = int(input())
numbers = []
for i in range(n):
    number = int(input())
    if number != 0:
        numbers.append(number)
    else:
        numbers.pop()
print(sum(numbers))