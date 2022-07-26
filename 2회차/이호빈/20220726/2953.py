result = []
for i in range(0, 5):
    a, b, c, d = list(map(int, input().split()))
    sum_ = a + b + c + d
    result.append(sum_)
print(result.index(max(result)) +1, max(result))


    