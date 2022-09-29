A, B = map(int, input().split())
array = []
array.append(0)
result = 0

for i in range(1000):
    for j in range(i):
        array.append(i)
        # array[0, 1, 2, 2, 3, 3, 3 ..., 999]

# for i in range(A, B): # 틀린 답
for i in range(A, B + 1): # A = 3, B = 7 -> range(3, 8) -> 3, 4, 5, 6, 7
    result = array[i] + result

print(result)