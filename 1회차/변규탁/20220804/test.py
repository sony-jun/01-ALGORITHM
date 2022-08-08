nums = []
for _ in range(10):
    nums.append(int(input()))

max_nums = []

for i in nums:
    max_nums.append(nums.count(i))

print(sum(nums)//len(nums))
print(nums[max_nums.index(max(max_nums))])