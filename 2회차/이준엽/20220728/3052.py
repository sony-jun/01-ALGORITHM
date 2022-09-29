numbers = []
for i in range(10):
    number = int(input())
    numbers.append(number%42)
print(len(list(set(numbers))))
