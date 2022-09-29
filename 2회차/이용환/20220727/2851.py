result = 0
result_ = 0
for i in range(10):
    score = int(input())
    if result+score > 100:
        result += score
        break
    result += score
    result_ += score
print(result_) if abs(100 - result) > 100 - result_ else print(result)
