A, B = map(int, input().split())

numbers = []
for i in range(50):
    for k in range(i):
        numbers.append(i)

result = 0
for j in range(A-1, B):
    result += numbers[j]
print(result)