import sys
sys.stdin = open("82_대표값_2592.txt", "r")

nums = [int(input()) for _ in range(10)]
print(sum(nums) // 10)
print(max(nums, key=nums.count))