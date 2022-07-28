num = []
for i in range(10):
    num_ = int(input())
    num.append(num_ % 42)

result = []
result = set(num)
print(len(result))