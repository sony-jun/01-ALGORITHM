# 쉽게 푸는 문제
# 시간초과

a, b = map(int, input().split())

nums = []

for i in range(1, b +1 // 2):
    nums.append(i)
    for j in range(i):
        if i != nums.count(i):
            nums.append(i)

print(sum(nums[a-1:b]))