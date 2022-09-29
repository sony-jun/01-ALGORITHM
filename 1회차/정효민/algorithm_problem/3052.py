
result = []

for i in range(10):
    
    a = int(input())
    y = a % 42
    if y not in result:
        result.append(y)
print(len(result))
