n = 3
m = 3
person = []
result = []

y = []
for _ in range(n):
    line = list(input().split())
    person.append(line)
for i in person:
    for y in range(m):
        result.append(i[y])
print(result)
                
    
