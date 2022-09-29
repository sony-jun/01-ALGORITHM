n = int(input())
numbers = []
result = {
}
result2 = []
for i in range(n):
    number = int(input())
    numbers.append(number)
    result[number] = 0

for i in numbers:
    result[i] +=1

many = max(list(result.values()))

for k, v in result.items():
    if v == many:
        result2.append(k)
print(min(result2))