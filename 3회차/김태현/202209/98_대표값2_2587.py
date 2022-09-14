import sys
sys.stdin = open("98_대표값2_2587.txt", "r")

nums = []
for i in range(5):
    nums.append(int(input()))

nums.sort()

avg = sum(nums) // len(nums)
med = nums[2]

print(avg)
print(med)