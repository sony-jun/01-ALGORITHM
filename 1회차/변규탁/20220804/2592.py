numbers = dict()
sum_ = 0
for _ in range(10):
    nums = int(input())
    sum_ += nums
    if nums in numbers :
        numbers[nums] += 1
    else:
        numbers[nums] = 1


max_ = max(numbers.values())
answer = 0
for k, v in numbers.items():
    if v == max_:
        answer = k
        break

print(sum_//10)
print(answer)